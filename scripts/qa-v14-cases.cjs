const {chromium}=require("playwright");
const fs=require("fs"),path=require("path"),assert=require("node:assert/strict");

const base=process.env.TEST_BASE||"http://127.0.0.1:4214";
const out=path.resolve(__dirname,"../evidence/v15");
(async()=>{
 const {projects,cvList}=await import("../src/data.js");
 const b=await chromium.launch({headless:true,...(process.env.PLAYWRIGHT_CHANNEL?{channel:process.env.PLAYWRIGHT_CHANNEL}:{})});const findings=[],failures=[];
 for(const item of projects){
  for(const width of [1440,390]){
   const page=await b.newPage({viewport:{width,height:width===1440?900:844},reducedMotion:"reduce"});
   const errors=[];page.on("pageerror",e=>errors.push(e.message));
   const response=await page.goto(base+"/projetos/"+item.slug+"/",{waitUntil:"domcontentloaded"});
   await page.waitForTimeout(100);
   let modal="none";const gallery=await page.locator(".gallery-trigger").count();
   if(item.slug==="gestao-de-propostas"&&gallery){
    await page.locator(".v14-protected-disclosure summary").click();
   }
   if(gallery){
    await page.locator(".gallery-trigger:visible").first().click();
    modal=String(await page.locator("#evidence-dialog").evaluate(el=>el.open));
    await page.keyboard.press("Escape");
    if(await page.locator("#evidence-dialog").evaluate(el=>el.open))errors.push("dialog did not close");
   }
   const overflowing=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
   const href=await page.locator('.case-header .brand').getAttribute('href');
   const broken=await page.locator("img").evaluateAll(imgs=>imgs.filter(img=>img.hasAttribute("src")&&img.complete&&img.naturalWidth===0).map(i=>i.getAttribute("src")));
   const result={case:item.slug,width,status:response.status(),gallery,modal,overflowing,errors,broken,headerHref:href};
   findings.push(result);
   if(result.status!==200||overflowing||errors.length||broken.length||href!=="/"||(gallery&&modal!=="true"))failures.push(result);
   await page.close();
  }
 }
 const page=await b.newPage();const pdfs=[];
 for(const cv of cvList){
  const result=await page.request.get(base+"/assets/cv/"+encodeURIComponent(cv.file));
  pdfs.push({file:cv.file,status:result.status()});
  if(result.status()!==200)failures.push({pdf:cv.file,status:result.status()});
 }
 await b.close();fs.writeFileSync(path.join(out,"case-regression.json"),JSON.stringify({findings,pdfs,failures},null,2));
 console.log(JSON.stringify({caseChecks:findings.length,pdfs:pdfs.length,failures:failures.slice(0,8)},null,2));
 if(failures.length)process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exit(1)});
