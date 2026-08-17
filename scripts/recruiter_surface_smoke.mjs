import { chromium } from 'playwright';

const base=(process.argv[2]||'http://127.0.0.1:8000').replace(/\/$/,'');
const browser=await chromium.launch({headless:true});
const failures=[];

async function visibleRows(page){
  return page.locator('#project-grid .archive-row:visible').count();
}

try{
  const mobile=await browser.newPage({viewport:{width:390,height:844}});
  await mobile.goto(base+'/',{waitUntil:'networkidle'});
  const button=mobile.locator('.archive-expand');
  if(!await button.isVisible())failures.push('PT mobile: archive expand control is not visible');
  const collapsed=await visibleRows(mobile);
  if(collapsed!==6)failures.push(`PT mobile: expected 6 secondary projects by default, got ${collapsed}`);
  await button.click();
  const expanded=await visibleRows(mobile);
  if(expanded!==13)failures.push(`PT mobile: expected all 13 secondary projects after expand, got ${expanded}`);
  if(await button.getAttribute('aria-expanded')!=='true')failures.push('PT mobile: expand control aria-expanded did not become true');

  const central=mobile.locator('.filter-button[data-filter="process"]');
  await central.click();
  if(await button.isVisible())failures.push('PT mobile: archive expand control should hide while filtering');
  const filtered=await visibleRows(mobile);
  if(filtered<1||filtered>=13)failures.push(`PT mobile: process filter returned suspicious row count ${filtered}`);

  await mobile.locator('.filter-button[data-filter="all"]').click();
  const search=mobile.locator('#project-search');
  await search.fill('central iso');
  const searched=await visibleRows(mobile);
  if(searched!==1)failures.push(`PT mobile: search for Central ISO expected 1 row, got ${searched}`);
  await search.fill('');

  const en=await browser.newPage({viewport:{width:390,height:844}});
  await en.goto(base+'/en/',{waitUntil:'networkidle'});
  if(!await en.locator('.archive-expand').isVisible())failures.push('EN mobile: archive expand control is not visible');
  if(await visibleRows(en)!==6)failures.push(`EN mobile: expected 6 secondary projects by default, got ${await visibleRows(en)}`);
  await en.locator('.archive-expand').click();
  if(await visibleRows(en)!==13)failures.push(`EN mobile: expected 13 secondary projects after expand, got ${await visibleRows(en)}`);

  const desktop=await browser.newPage({viewport:{width:1440,height:1000}});
  await desktop.goto(base+'/',{waitUntil:'networkidle'});
  if(await desktop.locator('.archive-expand').isVisible())failures.push('Desktop: archive expand control should remain hidden');
  if(await visibleRows(desktop)!==13)failures.push(`Desktop: expected all 13 secondary projects, got ${await visibleRows(desktop)}`);
}finally{
  await browser.close();
}

if(failures.length){
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log('Recruiter surface smoke passed: responsive archive, expand/collapse, filter and search behaviors are coherent.');
