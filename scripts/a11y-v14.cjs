const {chromium}=require("playwright");
const AxeBuilder=require("@axe-core/playwright").default;
const fs=require("fs"),path=require("path"),out=path.resolve(__dirname,"../evidence/v15");
(async()=>{
 const b=await chromium.launch({headless:true}),results=[],issues=[];
 for(const [width,height,reduced] of [[1440,900,false],[390,844,false],[320,700,true]]){
  const c=await b.newContext({viewport:{width,height},reducedMotion:reduced?"reduce":"no-preference"});
  const p=await c.newPage(),pageErrors=[];
  p.on("pageerror",e=>pageErrors.push(e.message));
  for(const route of ["/","/projetos/zero21fotos/","/projetos/belarc-inventory/"]){
   await p.goto("http://127.0.0.1:4214"+route,{waitUntil:"networkidle"});
   const axe=await new AxeBuilder({page:p}).withTags(["wcag2a","wcag2aa","wcag21aa","wcag22aa"]).analyze();
   const details=axe.violations.map(x=>({id:x.id,impact:x.impact,nodes:x.nodes.slice(0,4).map(n=>n.target)}));
   const overflow=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
   results.push({width,reduced,route,details,incomplete:axe.incomplete.length,overflow,errors:[...pageErrors]});
   if(details.length||overflow||pageErrors.length)issues.push(results.at(-1));
  }
  await c.close();
 }
 await b.close();
 fs.writeFileSync(path.join(out,"axe-v8.json"),JSON.stringify({results,issues},null,2));
 console.log(JSON.stringify({tested:results.length,issues:issues.length,problems:issues.slice(0,8)},null,2));
 if(issues.length)process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exit(1)});
