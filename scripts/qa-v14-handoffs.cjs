const {chromium}=require('playwright'),fs=require('fs'),path=require('path');
const out=path.resolve('evidence/v15'),fails=[],results=[];
(async()=>{
 const browser=await chromium.launch({headless:true});
 for(const [width,height] of [[1440,900],[390,844],[320,700]]){
  const context=await browser.newContext({viewport:{width,height}});
  const page=await context.newPage(),errs=[];
  page.on('pageerror',e=>errs.push(e.message));
  await page.goto('http://127.0.0.1:4214/',{waitUntil:'networkidle'});
  for(let j=0;j<4;j++){
   const section=page.locator('.v8-world');
   const y=await section.evaluate((e,i)=>scrollY+e.getBoundingClientRect().top+(e.offsetHeight-innerHeight)*((i+.50)/4),j);
   await page.evaluate(y=>scrollTo({top:y,behavior:'instant'}),y);
   await page.waitForTimeout(130);
   const state=await page.evaluate(index=>{
    const slides=[...document.querySelectorAll('.world-slide')];
    const layer=el=>({opacity:getComputedStyle(el).opacity,visibility:getComputedStyle(el).visibility,position:getComputedStyle(el).position,
    clip:getComputedStyle(el).clipPath,ariaHidden:el.getAttribute('aria-hidden'),
    loaded:el.querySelector('img.world-main-image').complete&&el.querySelector('img.world-main-image').naturalWidth>0});
    return {current:layer(slides[index]),incoming:layer(slides[index+1]),cinematic:innerWidth>800&&innerHeight>600,overflow:document.documentElement.scrollWidth>innerWidth};
   },j);
   const validHandoff=state.cinematic
    ?state.current.visibility==='visible'&&state.current.ariaHidden==='false'&&state.incoming.visibility==='hidden'&&state.incoming.ariaHidden==='true'
    :state.current.visibility==='visible'&&state.incoming.visibility==='visible'&&state.current.position==='relative'&&state.incoming.position==='relative';
   if(!validHandoff||!state.current.loaded||!state.incoming.loaded||state.overflow||errs.length)fails.push({width,j,state,errs});
   results.push({width,j,state});
   await page.screenshot({path:path.join(out,'handoff-'+(j+1)+'-'+width+'.png'),animations:'disabled'});
  }
  await context.close();
 }
 await browser.close();
 fs.writeFileSync(path.join(out,'qa-all-handoffs.json'),JSON.stringify({results,failures:fails},null,2));
 console.log(JSON.stringify({testCount:results.length,failures:fails.slice(0,3),success:fails.length===0},null,2));
 if(fails.length)process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exit(1)});
