import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const base=(process.argv[2]||'http://127.0.0.1:8000').replace(/\/$/,'');
const routes=['/','/competencias/','/cases/mala-direta/','/cases/carreira-pessoal/','/en/','/en/skills/'];
const browser=await chromium.launch({headless:true});
const failures=[];

try{
  for(const route of routes){
    const page=await browser.newPage({viewport:{width:1440,height:1000}});
    const response=await page.goto(base+route,{waitUntil:'networkidle'});
    if(!response?.ok()){
      failures.push(`${route}: HTTP ${response?.status()}`);
      await page.close();
      continue;
    }
    const results=await new AxeBuilder({page}).analyze();
    const severe=results.violations.filter(item=>['serious','critical'].includes(item.impact||''));
    if(severe.length){
      failures.push(`${route}: ${severe.map(item=>`${item.id}(${item.impact}) x${item.nodes.length}`).join(', ')}`);
    }
    const moderate=results.violations.filter(item=>item.impact==='moderate').length;
    console.log(`${route}: ${severe.length} serious/critical; ${moderate} moderate violations`);
    await page.close();
  }
}finally{
  await browser.close();
}

if(failures.length){
  console.error('Accessibility gate failed:\n'+failures.join('\n'));
  process.exit(1);
}
console.log('Accessibility gate passed for recruiter-facing PT/EN surfaces.');
