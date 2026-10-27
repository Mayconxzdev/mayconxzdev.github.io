const {chromium}=require("playwright"),fs=require("fs"),path=require("path");
(async()=>{
const browser=await chromium.launch({headless:true});
const base="http://127.0.0.1:4214",out="evidence/v15";
fs.mkdirSync(out,{recursive:true});
const results=[],issues=[];
for(const width of [320,390,430,768,1024,1440]){
 for(const mode of ["no-preference","reduce"]){
  const isMobile=width<=800;
  const ctx=await browser.newContext({viewport:{width,height:width<600?844:900},reducedMotion:mode});
  const page=await ctx.newPage();const errors=[];
  page.on("pageerror",e=>errors.push(e.message));
  await page.goto(base,{waitUntil:"networkidle"});
  const initial=await page.evaluate(()=>({
   mobileStable:document.documentElement.classList.contains("v15-mobile-stable"),
   overflow:document.documentElement.scrollWidth>innerWidth,
   slides:[...document.querySelectorAll(".world-slide")].map(s=>({vis:getComputedStyle(s).visibility,position:getComputedStyle(s).position,height:s.getBoundingClientRect().height,opacity:getComputedStyle(s).opacity,inert:s.inert}))
  }));
  if(initial.mobileStable!==isMobile||initial.overflow)issues.push({width,mode,issue:"initial",initial});
  if(isMobile){
   const slides=page.locator(".world-slide");
   for(let n=0;n<5;n++){
    const slide=slides.nth(n);
    const status=await slide.evaluate(e=>({rect:e.getBoundingClientRect().toJSON(),heading:e.querySelector("h3")?.textContent,img:e.querySelector(".world-main-image")?.naturalWidth}));
    if(status.rect.height<190||initial.slides[n].vis!=="visible"||initial.slides[n].inert||initial.slides[n].position!=="relative")issues.push({width,mode,issue:"slide",n,status,initial:initial.slides[n]});
    const tabs=slide.locator(".world-tab");
    if(await tabs.count()>1){await tabs.nth(1).click({timeout:15000});await page.waitForTimeout(140);const selected=await tabs.nth(1).getAttribute("aria-pressed");if(selected!=="true")issues.push({width,mode,issue:"tab",n,selected});}
   }
  }
  const menu=page.locator("#menu-toggle");
  if(isMobile)await menu.click();
  const nav=page.locator('header nav a[href="#acervo"]').first();
  await nav.click();
  await page.waitForTimeout(500);
  const navinfo=await page.evaluate(()=>{const a=document.getElementById("acervo"),rect=a.getBoundingClientRect(),world=document.querySelector(".v8-world").getBoundingClientRect(),ghost=document.querySelector(".v11-handoff-ghost");return {hash:location.hash,top:rect.top,archiveVisible:rect.top<innerHeight&&rect.bottom>0,worldBottom:world.bottom,ghost:ghost?{visibility:getComputedStyle(ghost).visibility,opacity:getComputedStyle(ghost).opacity}:null,overflow:document.documentElement.scrollWidth>innerWidth};});
  if(!navinfo.archiveVisible||!["#acervo"].includes(navinfo.hash)||navinfo.top<0||navinfo.top>160||navinfo.worldBottom>navinfo.top+1||navinfo.overflow)issues.push({width,mode,issue:"navigation",navinfo});
  if(mode==="no-preference")await page.screenshot({path:path.join(out,"nav-"+width+".png"),animations:"disabled"});
  results.push({width,mode,initial:{stable:initial.mobileStable,overflow:initial.overflow,slides:initial.slides.map(x=>({pos:x.position,h:x.height,vis:x.vis,inert:x.inert}))},navinfo,errors});
  if(errors.length)issues.push({width,mode,issue:"pageerror",errors});
  await ctx.close();
 }
}
for(const width of [390,1440]){
 const ctx=await browser.newContext({viewport:{width,height:900},reducedMotion:"no-preference"});
 const page=await ctx.newPage();const errors=[];page.on("pageerror",e=>errors.push(e.message));
 const res=await page.goto(base+"/projetos/zero21fotos/",{waitUntil:"networkidle"});
 const tabsGallery=page.locator("[data-v14-select]");
 for(let j=0;j<3;j++){await tabsGallery.nth(j).click();await page.waitForFunction(k=>{const img=document.querySelectorAll(".v14-slide img")[k];return img&&img.complete&&img.naturalWidth>0;},j,{timeout:12000});}
 const paths=await page.locator(".v14-slide img").evaluateAll(els=>els.map(x=>({src:x.getAttribute("src"),ok:x.naturalWidth>0})));
 const block=page.locator(".v15-zero21-operations");
 const t=await block.innerText();
 if(res.status()!==200||paths.length!==3||paths.some(x=>!x.ok||!x.src.includes("zero21-v15"))||!t.includes("Importa novos eventos")||!t.includes("painel"))issues.push({width,issue:"zero21",status:res.status(),paths,t:t.slice(0,600)});
 const buttons=page.locator('[data-v14-select]');if(await buttons.count()>=3){await buttons.nth(2).click();if(await buttons.nth(2).getAttribute('aria-pressed')!=="true")issues.push({width,issue:"zero-gallery"});}
 await page.locator("#visao").scrollIntoViewIfNeeded();
 await page.screenshot({path:path.join(out,"zero21-case-"+width+".png"),animations:"disabled"});
 if(errors.length)issues.push({width,issue:"zero21-errors",errors});
 await ctx.close();
}
await browser.close();const summary={count:results.length,failures:issues.length,issues,results};fs.writeFileSync(path.join(out,"regression.json"),JSON.stringify(summary,null,2));console.log(JSON.stringify({checks:results.length,failures:issues.length,examples:issues.slice(0,8)},null,2).slice(0,9000));if(issues.length)process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exit(2)});