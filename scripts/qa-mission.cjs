const {chromium}=require('playwright');
const AxeBuilder=require('@axe-core/playwright').default;
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const crypto=require('node:crypto');
const base=process.env.TEST_BASE||'http://127.0.0.1:4214';
const phase=process.argv.includes('--before')?'before':'after';
const out=path.resolve(process.env.TEST_EVIDENCE||path.resolve(__dirname,'../evidence/mission'),phase,...(process.argv.includes('--flows-only')?['flows-final']:[]));
fs.mkdirSync(out,{recursive:true});
const results=[],failures=[],flows=[];
const pause=ms=>new Promise(r=>setTimeout(r,ms));
async function check(name,fn){console.log('start '+name);try{const value=await fn();flows.push({name,pass:true,value});console.log('PASS '+name);}catch(e){const item={name,pass:false,error:e.message};flows.push(item);failures.push(item);console.log('FAIL '+name+': '+e.message);}}
(async()=>{
 const {projects,cvList}=await import('../src/data.js');
 const dist=path.resolve(__dirname,'../dist/assets');
 const buildHashes=fs.readdirSync(dist).filter(x=>/^index-.*\.(css|js)$/.test(x)).map(file=>({file,sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(dist,file))).digest('hex')}));
 fs.writeFileSync(path.join(out,'build-hashes.json'),JSON.stringify({phase,buildHashes},null,2));
 const browser=await chromium.launch({headless:true});
 const routes=['/',...projects.map(p=>'/projetos/'+p.slug+'/')];
 for(const width of (process.argv.includes('--flows-only')?[]:[320,360,390,430,768,1024,1440,1920])){
  const context=await browser.newContext({viewport:{width,height:width<768?844:900},reducedMotion:'no-preference'});
  const page=await context.newPage();
  for(const route of routes){
   const errors=[],httpErrors=[];
   const onError=e=>errors.push(e.message),onResponse=r=>{if(r.url().startsWith(base)&&r.status()>=400)httpErrors.push({url:r.url(),status:r.status()});};
   page.on('pageerror',onError);page.on('response',onResponse);
   const response=await page.goto(base+route,{waitUntil:'networkidle'});
   await page.evaluate(async()=>{await document.fonts.ready;await Promise.race([Promise.all([...document.images].filter(i=>i.complete&&i.naturalWidth>0).map(i=>i.decode().catch(()=>{}))),new Promise(r=>setTimeout(r,1000))]);});
   const data=await page.evaluate(()=>({title:document.title,h1:document.querySelectorAll('h1').length,overflow:document.documentElement.scrollWidth-innerWidth,broken:[...document.images].filter(i=>i.hasAttribute('src')&&i.complete&&!i.naturalWidth).map(i=>i.getAttribute('src')),missingAlt:[...document.images].filter(i=>!i.hasAttribute('alt')).length,badAnchors:[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.getElementById(h.slice(1))),unsafeExternal:[...document.querySelectorAll('a[target="_blank"]')].filter(a=>!a.rel.includes('noopener')&&!a.rel.includes('noreferrer')).map(a=>a.href)}));
   const item={route,width,status:response.status(),...data,errors,httpErrors};results.push(item);
   if(item.status!==200||item.h1!==1||item.overflow>1||item.broken.length||item.missingAlt||item.badAnchors.length||errors.length||httpErrors.length||item.unsafeExternal.length)failures.push(item);
   if([390,1440].includes(width)){
    await page.screenshot({path:path.join(out,(route==='/'?'home':route.split('/')[2])+'-'+width+'.png'),fullPage:route!=='/',animations:'disabled'});
    if(route==='/')for(const id of ['acervo','metodo','sobre','curriculos','contato'])if(await page.locator('#'+id).count()){await page.locator('#'+id).scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'home-'+id+'-'+width+'.png'),animations:'disabled'});}
   }
   page.removeListener('pageerror',onError);page.removeListener('response',onResponse);
  }
  console.log('completed width '+width);await context.close();
 }
 fs.writeFileSync(path.join(out,'routes.json'),JSON.stringify({phase,results,failures},null,2));
 console.log(JSON.stringify({phase,routeChecks:results.length,routeFailures:failures.length}));
 if(phase==='before'){await browser.close();return;}
 const c=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'reduce'}),p=await c.newPage();
 await p.goto(base,{waitUntil:'networkidle'});
 await check('mobile menu Escape',async()=>{await p.locator('#menu-toggle').click();assert.equal(await p.locator('#menu-toggle').getAttribute('aria-expanded'),'true');await p.keyboard.press('Escape');assert.equal(await p.locator('#menu-toggle').getAttribute('aria-expanded'),'false');});
 await check('menu projects and highlights',async()=>{for(const hash of ['#acervo','#projetos']){await p.locator('#menu-toggle').click();await p.locator('header nav a[href="'+hash+'"]').first().click();assert.equal(new URL(p.url()).hash,hash);assert.equal(await p.locator('#menu-toggle').getAttribute('aria-expanded'),'false');}});
 await check('mobile hero scenes',async()=>{await p.goto(base,{waitUntil:'networkidle'});for(let i=0;i<3;i++){await p.locator('[data-hero-preview="'+i+'"]').click();assert.equal(await p.locator('[data-hero-preview="'+i+'"]').getAttribute('aria-pressed'),'true');assert.equal(await p.locator('.hero-stage .stage-window').nth(i).evaluate(e=>e.inert),false);}});
 await check('five highlights tabs lightbox and Escape',async()=>{for(let i=0;i<5;i++){const slide=p.locator('.world-slide').nth(i);await slide.scrollIntoViewIfNeeded();const tabs=slide.locator('.world-tab');for(let j=0;j<await tabs.count();j++){await tabs.nth(j).click();await p.waitForFunction(({i,j})=>document.querySelectorAll('.world-slide')[i].querySelectorAll('.world-tab')[j].getAttribute('aria-pressed')==='true',{i,j});assert.ok(await slide.locator('.world-main-image').evaluate(e=>e.complete&&e.naturalWidth>0));}await slide.locator('.world-zoom').click();assert.ok(await p.locator('#v8-lightbox').evaluate(e=>e.open));await p.keyboard.press('Escape');assert.equal(await p.locator('#v8-lightbox').evaluate(e=>e.open),false);}});
 await check('archive order filters search empty reset',async()=>{await p.locator('#acervo').scrollIntoViewIfNeeded();await p.locator('[data-filter="all"]').click();const initial=await p.locator('[data-project]').evaluateAll(es=>es.map(e=>e.dataset.project));assert.deepEqual(initial.slice(0,3),['engenharia-de-dados-compass','sites-industriais','compras-e-cotacoes']);for(const filter of ['operacao','ia','web','dados','lab','all']){await p.locator('[data-filter="'+filter+'"]').click();assert.equal(await p.locator('[data-filter="'+filter+'"]').getAttribute('aria-pressed'),'true');}await p.locator('#project-search').fill('Compass');assert.equal(await p.locator('[data-project]').count(),1);await p.locator('#project-search').fill('zxq-sem-resultado');assert.ok(await p.locator('#catalog-grid .empty').isVisible());await p.locator('#project-search').fill('');await p.locator('#catalog-show-all').click();assert.equal(await p.locator('#catalog-show-all').getAttribute('aria-pressed'),'true');});
 await check('two historical cases remain discoverable',async()=>{const history=p.locator('.v15-history');await history.locator('summary').focus();await p.keyboard.press('Enter');assert.ok(await history.getAttribute('open')!==null);const links=history.locator('a');assert.equal(await links.count(),2);for(let i=0;i<2;i++){assert.ok(await links.nth(i).isVisible());const r=await p.request.get(base+await links.nth(i).getAttribute('href'));assert.equal(r.status(),200);}await history.locator('summary').click();});
 await check('three Portuguese resumes and three English downloads',async()=>{
  await p.locator('#curriculos').scrollIntoViewIfNeeded();
  const ptCards=await p.locator('#cv-grid .cv-card').evaluateAll(cards=>cards.map(card=>card.getAttribute('href')));
  assert.equal(ptCards.length,cvList.length);
  assert.deepEqual(ptCards,cvList.map(cv=>'/assets/cv/'+encodeURIComponent(cv.file)));
  const english=await c.newPage();const enResponse=await english.goto(base+'/en/resumes/',{waitUntil:'networkidle'});assert.equal(enResponse.status(),200);
  const enLinks=await english.locator('a.action[href$=".pdf"]').evaluateAll(links=>links.map(link=>link.getAttribute('href')));assert.equal(enLinks.length,3);
  for(const href of [...ptCards,...enLinks]){const response=await p.request.get(base+href);assert.equal(response.status(),200,href);assert.equal((await response.body()).subarray(0,4).toString(),'%PDF',href);}
  await english.close();return {portuguesePdfs:ptCards.length,englishPdfs:enLinks.length,filters:'not part of current interface'};
 });
 await check('method keyboard arrows Home End',async()=>{const first=p.locator('[data-method]').first();await first.focus();await p.keyboard.press('End');assert.equal(await p.locator('[data-method]').last().getAttribute('aria-selected'),'true');await p.keyboard.press('Home');assert.equal(await first.getAttribute('aria-selected'),'true');});
 await check('keyboard visible focus',async()=>{await p.goto(base,{waitUntil:'networkidle'});await p.keyboard.press('Tab');return await p.evaluate(()=>{const e=document.activeElement,s=getComputedStyle(e);if(e===document.body||s.visibility==='hidden')throw Error('no visible focused control');return {tag:e.tagName,text:e.textContent.trim().slice(0,80),outline:s.outline};});});
 await check('motion control persists all three modes',async()=>{const mode=p.locator('#motion-mode');await mode.selectOption('direct');assert.ok(await p.locator('html').evaluate(e=>e.classList.contains('v11-direct')));assert.equal(await p.evaluate(()=>localStorage.getItem('lv-motion-mode')),'direct');await mode.selectOption('motion');assert.equal(await p.locator('html').getAttribute('data-motion-mode'),'motion');assert.equal(await p.locator('html').evaluate(e=>e.classList.contains('v11-direct')),false);await mode.selectOption('auto');assert.equal(await p.locator('html').getAttribute('data-motion-mode'),'auto');});
 for(const item of projects)await check('case gallery '+item.slug,async()=>{
  await p.goto(base+'/projetos/'+item.slug+'/',{waitUntil:'networkidle'});
  if(await p.locator('.v14-protected-disclosure').count())await p.locator('.v14-protected-disclosure summary').click();
  const selections=p.locator('[data-v14-select]');for(let i=0;i<await selections.count();i++){await selections.nth(i).click();assert.equal(await selections.nth(i).getAttribute('aria-pressed'),'true');}
  const trigger=p.locator('.gallery-trigger:visible').first();
  if(await trigger.count()){await trigger.click();assert.ok(await p.locator('#evidence-dialog').evaluate(e=>e.open));const count=await p.locator('#evidence-count').textContent();await p.keyboard.press('ArrowRight');const next=await p.locator('#evidence-count').textContent();if(!count.includes('/ 1'))assert.notEqual(next,count);await p.keyboard.press('Escape');assert.equal(await p.locator('#evidence-dialog').evaluate(e=>e.open),false);}
  const menu=p.locator('.v12-case-menu-toggle');if(await menu.isVisible()){await menu.click();await p.keyboard.press('Escape');assert.equal(await menu.getAttribute('aria-expanded'),'false');}
 });
 await check('browser back retains home navigation',async()=>{await p.goto(base+'/#acervo',{waitUntil:'networkidle'});await p.locator('[data-project] a').first().click();await p.waitForURL('**/projetos/**');await p.goBack({waitUntil:'networkidle'});assert.equal(new URL(p.url()).hash,'#acervo');assert.ok(await p.locator('#project-search').isVisible());});
 await c.close();
 const desktop=await browser.newContext({viewport:{width:1440,height:900}}),d=await desktop.newPage();
 await d.goto(base,{waitUntil:'networkidle'});
 await check('desktop rapid scroll and all direct chapters',async()=>{for(let i=0;i<5;i++){await d.locator('[data-jump="'+i+'"]').click();await pause(120);const s=d.locator('.world-slide').nth(i);assert.equal(await s.getAttribute('aria-hidden'),'false');}await d.evaluate(()=>{window.scrollTo(0,document.body.scrollHeight);window.scrollTo(0,0);window.scrollTo(0,document.body.scrollHeight);});await pause(200);assert.equal(await d.locator('.v11-handoff-ghost').evaluate(e=>getComputedStyle(e).visibility),'hidden');});
 await check('desktop axe WCAG subset',async()=>{const a=await new AxeBuilder({page:d}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();fs.writeFileSync(path.join(out,'axe-home.json'),JSON.stringify(a.violations,null,2));assert.equal(a.violations.length,0);return {violations:a.violations.length,incomplete:a.incomplete.length};});
 await check('200 percent layout and landscape all routes',async()=>{const issues=[];for(const viewport of [{width:720,height:450},{width:844,height:390},{width:1024,height:500}]){await d.setViewportSize(viewport);for(const route of routes){await d.goto(base+route,{waitUntil:'networkidle'});const overflow=await d.evaluate(()=>document.documentElement.scrollWidth-innerWidth);if(overflow>1)issues.push({route,viewport,overflow});if(route==='/'){const states=await d.locator('.world-slide').evaluateAll(es=>es.map(e=>({position:getComputedStyle(e).position,inert:e.inert,height:e.getBoundingClientRect().height})));if(states.some(s=>s.position!=='relative'||s.inert||s.height<190))issues.push({route,viewport,states});for(const i of [0,4])await d.locator('.world-slide').nth(i).screenshot({path:path.join(out,'lowheight-'+viewport.width+'x'+viewport.height+'-scene-'+i+'.png'),animations:'disabled'});}}}assert.deepEqual(issues,[]);return '57 route/short-viewport combinations; all five scenes in readable relative flow. 720 CSS px models content area of 1440 display at 200%; no physical browser zoom claim';});
 await check('resize recomposes mobile desktop and reduced motion',async()=>{await d.setViewportSize({width:390,height:844});await d.goto(base,{waitUntil:'networkidle'});for(const width of [1024,768,1440,390]){await d.setViewportSize({width,height:900});await pause(220);const state=await d.evaluate(()=>({mobile:document.documentElement.classList.contains('v15-mobile-stable'),slides:[...document.querySelectorAll('.world-slide')].map(e=>({inert:e.inert,pos:getComputedStyle(e).position}))}));assert.equal(state.mobile,width<=800);if(width<=800)assert.ok(state.slides.every(s=>!s.inert&&s.pos==='relative'));}await d.emulateMedia({reducedMotion:'reduce'});await pause(180);assert.ok(await d.locator('.world-slide').evaluateAll(es=>es.every(e=>!e.inert)));});
 await desktop.close();
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}}),n=await nojs.newPage();
 await check('no JavaScript real catalog CV and five scenes',async()=>{await n.goto(base,{waitUntil:'networkidle'});for(const selector of ['.hero h1','#catalog-grid a[href^="/projetos/"]','#cv-grid a[href$=".pdf"]'])assert.ok(await n.locator(selector).first().isVisible(),selector);assert.equal(await n.locator('#cv-grid a[href$=".pdf"]').count(),3);const scenes=await n.locator('.world-slide').evaluateAll(es=>es.map(e=>({h:e.getBoundingClientRect().height,visibility:getComputedStyle(e).visibility,opacity:getComputedStyle(e).opacity})));assert.equal(scenes.length,5);assert.ok(scenes.every(s=>s.h>0&&s.visibility==='visible'&&s.opacity!=='0'));return {catalog:await n.locator('#catalog-grid a[href^="/projetos/"]').count(),scenes:scenes.length,portuguesePdfs:3};});
 await nojs.close();await browser.close();
 fs.writeFileSync(path.join(out,'regression.json'),JSON.stringify({phase,routeChecks:results.length,results,flows,failures},null,2));
 console.log(JSON.stringify({routeChecks:results.length,flows:flows.length,failures},null,2));if(failures.length)process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exitCode=1;});
