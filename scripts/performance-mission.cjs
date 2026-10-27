// Lab observations from Chromium, never field Core Web Vitals or an INP claim.
const {chromium}=require('playwright');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const phase=process.argv.includes('--before')?'before':'after';
const base=process.env.TEST_BASE||'http://127.0.0.1:4214';
(async()=>{
 const assetDir=path.resolve(__dirname,'../dist/assets');
 const buildHashes=fs.readdirSync(assetDir).filter(n=>/^index-.*\.(css|js)$/.test(n)).map(file=>({file,sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(assetDir,file))).digest('hex')}));
 const b=await chromium.launch({headless:true}),results=[];
 for(const mobile of [false,true])for(const route of ['/','/projetos/producao-operacional/','/projetos/engenharia-de-dados-compass/']){
  if(process.argv.includes('--home-mobile')&&(!mobile||route!=='/'))continue;
  const c=await b.newContext({viewport:mobile?{width:390,height:844}:{width:1440,height:900}}),p=await c.newPage();
  await p.addInitScript(()=>{
   window.__lab={lcp:[],cls:[],longTasks:[]};
   for(const [type,key] of [['largest-contentful-paint','lcp'],['layout-shift','cls'],['longtask','longTasks']])try{new PerformanceObserver(list=>{for(const e of list.getEntries())window.__lab[key].push({startTime:e.startTime,duration:e.duration,value:e.value||0,hadRecentInput:e.hadRecentInput||false,element:e.element?.tagName,url:e.url||'',sources:e.sources?.map(s=>({node:s.node?.tagName+'.'+s.node?.className,previousRect:s.previousRect.toJSON(),currentRect:s.currentRect.toJSON()}))});}).observe({type,buffered:true});}catch{}
  });
  const cd=await c.newCDPSession(p);
  await cd.send('Network.enable');await cd.send('Network.setCacheDisabled',{cacheDisabled:true});
  if(mobile){await cd.send('Emulation.setCPUThrottlingRate',{rate:4});await cd.send('Network.emulateNetworkConditions',{offline:false,downloadThroughput:1600000/8,uploadThroughput:750000/8,latency:150});}
  const started=Date.now();await p.goto(base+route,{waitUntil:'networkidle',timeout:120000});await p.waitForTimeout(1500);
  const metrics=await p.evaluate(()=>({lcpMs:window.__lab.lcp.at(-1)?.startTime??null,lcpElement:window.__lab.lcp.at(-1)?.element??null,lcpUrl:window.__lab.lcp.at(-1)?.url??null,cls:window.__lab.cls.filter(e=>!e.hadRecentInput).reduce((n,e)=>n+e.value,0),shifts:window.__lab.cls,longTaskCount:window.__lab.longTasks.length,longTaskTimeMs:window.__lab.longTasks.reduce((n,e)=>n+e.duration,0),transferBytes:performance.getEntriesByType('resource').reduce((n,e)=>n+e.transferSize,0),resources:performance.getEntriesByType('resource').length,resourceTiming:performance.getEntriesByType('resource').map(r=>({url:r.name,start:r.startTime,end:r.responseEnd,bytes:r.transferSize,type:r.initiatorType})),navigation:performance.getEntriesByType('navigation')[0].toJSON()}));
  results.push({route,mobile,elapsedMs:Date.now()-started,...metrics});console.log(JSON.stringify(results.at(-1)));await c.close();
 }
 await b.close();const out=path.resolve(process.env.TEST_EVIDENCE||path.resolve(__dirname,'../evidence/mission'),phase);fs.mkdirSync(out,{recursive:true});
 fs.writeFileSync(path.join(out,process.argv.includes('--home-mobile')?'performance-home-mobile-detail.json':'performance.json'),JSON.stringify({method:'One cold-cache local Chromium lab sample per route/profile; mobile CPU 4x, 1.6Mbps download, 750kbps upload, 150ms latency; desktop unthrottled. LCP/CLS sampled before interaction; not field CWV or Lighthouse; INP not measured.',buildHashes,targets:{lcpMs:2500,cls:0.1},results},null,2));
})().catch(e=>{console.error(e.stack);process.exitCode=1;});
