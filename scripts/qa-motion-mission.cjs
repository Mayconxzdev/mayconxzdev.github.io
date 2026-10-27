const {chromium}=require('playwright');
const fs=require('node:fs'),path=require('node:path');
const out=path.resolve(process.env.TEST_EVIDENCE||path.resolve(__dirname,'../evidence/mission'),'motion');
fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch();const report=[];
 for(const [width,height,motion] of [[1440,900,'no-preference'],[1024,500,'no-preference'],[390,844,'no-preference'],[1440,900,'reduce']]){
  const page=await browser.newPage({viewport:{width,height},reducedMotion:motion});const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.goto('http://127.0.0.1:4214/',{waitUntil:'networkidle'});
  const mobile=width<=800||height<=600||motion==='reduce';
  for(let step=0;step<=(mobile?4:8);step++){
   if(mobile)await page.locator('.world-slide').nth(step).scrollIntoViewIfNeeded();
   else await page.evaluate(progress=>{const world=document.querySelector('.v8-world');scrollTo(0,world.getBoundingClientRect().top+scrollY+(world.offsetHeight-innerHeight)*progress)},step/8);
   await page.waitForTimeout(160);
   const state=await page.evaluate(()=>({scrollY,overflow:document.documentElement.scrollWidth-innerWidth,ghost:[...document.querySelectorAll('.v11-handoff-ghost')].filter(e=>getComputedStyle(e).visibility!=='hidden'&&+getComputedStyle(e).opacity>.01).length,slides:[...document.querySelectorAll('.world-slide')].map(e=>({name:e.id,hidden:e.getAttribute('aria-hidden'),inert:e.inert,display:getComputedStyle(e).visibility,caption:+getComputedStyle(e.querySelector('.world-description')).opacity,image:e.querySelector('.world-main-image').naturalWidth}))}));
   report.push({width,height,motion,step,...state,errors:[...errors]});
   await page.screenshot({path:path.join(out,`${width}-${height}-${motion}-${step}.png`)});
  }
  await page.close();
 }
 await browser.close();
 fs.writeFileSync(path.join(out,'states.json'),JSON.stringify(report,null,2));
 const failures=report.filter(x=>x.errors.length||x.overflow>1||x.ghost>0); console.log(JSON.stringify({states:report.length,errors:failures.length}));if(failures.length)throw Error('Motion regression: '+failures.length+' states');
})().catch(e=>{console.error(e);process.exitCode=1});
