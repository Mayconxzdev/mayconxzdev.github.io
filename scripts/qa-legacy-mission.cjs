const {chromium}=require('playwright'),fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../public'),out=path.resolve(__dirname,'../evidence/mission/legacy');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):e.name.endsWith('.html')?[path.join(d,e.name)]:[]);
(async()=>{
 fs.mkdirSync(out,{recursive:true});
 const files=walk(root).filter(p=>!p.includes(path.sep+'projetos'+path.sep));
 const browser=await chromium.launch(),results=[];
 for(const width of [390,1440]){
  const context=await browser.newContext({viewport:{width,height:900},reducedMotion:'reduce'}),page=await context.newPage();
  for(const file of files){
   const rel=path.relative(root,file).replaceAll(path.sep,'/'),route='/'+rel.replace(/index\.html$/,'');
   const errors=[];const listen=e=>errors.push(e.message);page.on('pageerror',listen);
   const response=await page.goto('http://127.0.0.1:4214'+route,{waitUntil:'networkidle'});
   const data=await page.evaluate(()=>({title:document.title,h1:[...document.querySelectorAll('h1')].map(x=>x.textContent.trim()),description:document.querySelector('meta[name="description"]')?.content,overflow:document.documentElement.scrollWidth-innerWidth,broken:[...document.images].filter(i=>i.getAttribute('src')&&i.complete&&!i.naturalWidth).map(i=>i.getAttribute('src')),missingAnchors:[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.getElementById(h.slice(1))),firstEvidence:document.querySelector('figure figcaption')?.textContent.trim(),privacyNotes:document.querySelectorAll('.privacy-review-note').length,headings:[...document.querySelectorAll('h2')].map(x=>x.textContent.trim())}));
   results.push({route,width,status:response.status(),...data,errors});
   await page.screenshot({path:path.join(out,rel.replaceAll('/','-').replace('.html','')+'-'+width+'.png'),animations:'disabled'});
   page.removeListener('pageerror',listen);
  }
  await context.close();console.log('legacy width '+width+' complete');
 }
 await browser.close();const issues=results.filter(x=>x.status!==200||x.overflow>1||x.broken.length||x.errors.length||x.missingAnchors.length);
 fs.writeFileSync(path.join(out,'routes.json'),JSON.stringify({note:'Historical documents bundled in public; separate from the 18 current cases. Inventory, resource/route checks and first viewport captures, not a claimed complete redesign of historical projects.',results,issues},null,2));
 console.log(JSON.stringify({routes:files.length,checks:results.length,issues}));if(issues.length)process.exitCode=2;
})().catch(e=>{console.error(e);process.exitCode=1});
