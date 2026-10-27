const {chromium}=require('playwright');
const AxeBuilder=require('@axe-core/playwright').default;
const fs=require('node:fs'),path=require('node:path');
(async()=>{
 const {projects}=await import('../src/data.js');const browser=await chromium.launch({headless:true}),results=[];
 for(const width of [390,1440]){
  const c=await browser.newContext({viewport:{width,height:900},reducedMotion:'reduce'}),p=await c.newPage();
  for(const route of ['/',...projects.map(x=>'/projetos/'+x.slug+'/')]){
   await p.goto((process.env.TEST_BASE||'http://127.0.0.1:4214')+route,{waitUntil:'networkidle'});
   const a=await new AxeBuilder({page:p}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();
   results.push({route,width,passes:a.passes.length,incomplete:a.incomplete.length,violations:a.violations.map(v=>({id:v.id,impact:v.impact,description:v.description,helpUrl:v.helpUrl,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))}))});
  }
  await c.close();console.log('axe width '+width+' complete');
 }
 await browser.close();const issues=results.filter(x=>x.violations.length),out=path.resolve(process.env.TEST_EVIDENCE||path.resolve(__dirname,'../evidence/mission'),'after');fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'axe-all-routes.json'),JSON.stringify({method:'axe-core WCAG A/AA tags through 2.2, reduced motion, two viewports. Automated subset; incomplete findings and manual screen-reader/device checks require review.',results,issues},null,2));console.log(JSON.stringify({checks:results.length,issuePages:issues.length,issues},null,2));if(issues.length)process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exitCode=1;});
