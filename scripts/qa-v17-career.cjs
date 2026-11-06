const {chromium}=require("playwright");
const fs=require("fs"),path=require("path");
(async()=>{
const browser=await chromium.launch({headless:true});
const root="http://127.0.0.1:4214";
const results=[],errors=[];
try{
 for(const width of [320,390,768,1440]){
  const ctx=await browser.newContext({viewport:{width,height:900},reducedMotion:"reduce"});
  const p=await ctx.newPage();const jsErrors=[];p.on("pageerror",e=>jsErrors.push(e.message));
  const home=await p.goto(root+"/",{waitUntil:"domcontentloaded"});
  const section=p.locator("#avaliar");
  const cards=section.locator(".career-focus-card");
  const heading=await section.locator("h2").innerText();
  const titles=await cards.locator("h3").allInnerTexts();
  const overflow=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
  const source=await p.locator(".hero-actions a.btn-accent").getAttribute("href");
  const resumes=await p.locator("#cv-grid a").evaluateAll(a=>a.map(x=>x.getAttribute("href")));
  const focusLinks=await section.locator("a[href]").evaluateAll(a=>a.map(x=>x.getAttribute("href")));
  const item={width,status:home.status(),heading,titles,overflow,source,resumes,focusLinks,jsErrors};
  results.push(item);
  if(item.status!==200||!item.heading.includes("construí")||cards&&titles.length!==4||!titles.includes("ArsenalMind Universal")||!titles.includes("Desapega AI")||!titles.includes("Belarc Inventory")||item.overflow>1||item.source!=="#avaliar"||resumes.length!==2||!focusLinks.includes("/estudos/desapega-ai/")||jsErrors.length)errors.push(item);
  if(width===390||width===1440){
   await section.scrollIntoViewIfNeeded();
   const dir=path.resolve("evidence/career-v17");fs.mkdirSync(dir,{recursive:true});
   await p.screenshot({path:path.join(dir,"section-"+width+".png"),animations:"disabled"});
  }
  const caseResponse=await p.goto(root+"/estudos/desapega-ai/",{waitUntil:"domcontentloaded"});
  const body=await p.locator("main").innerText();
  const skip=await p.locator("a.skip").count();
  const caseOverflow=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
  if(caseResponse.status()!==200||!body.includes("estado local")||!body.includes("ArsenalMind")||!body.includes("versão")||skip!==1||caseOverflow>1||jsErrors.length)errors.push({width,route:"/estudos/desapega-ai/",status:caseResponse.status(),overflow:caseOverflow,skip,jsErrors});
  await ctx.close();
 }
}finally{await browser.close()}
const file=path.resolve("evidence/career-v17/recruiter-paths.json");fs.mkdirSync(path.dirname(file),{recursive:true});fs.writeFileSync(file,JSON.stringify({results,errors},null,2));
console.log(JSON.stringify({widths:results.map(x=>x.width),sections:results.length,issues:errors.length,examples:errors.slice(0,3)}));
if(errors.length)process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exitCode=2});
