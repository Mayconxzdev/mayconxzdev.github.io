const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const base=process.env.TEST_BASE||'http://127.0.0.1:4214';
const out=path.resolve(process.env.TEST_EVIDENCE||path.resolve(__dirname,'../evidence/motion-gallery-fix/after'));
fs.mkdirSync(out,{recursive:true});
const report={viewports:[],motion:[],cases:[],failures:[]};
const viewportSet=[
 {width:320,height:780,name:'320'}, {width:360,height:800,name:'360'},
 {width:390,height:844,name:'390'}, {width:430,height:900,name:'430'},
 {width:768,height:1024,name:'768'}, {width:1024,height:768,name:'1024'},
 {width:1440,height:900,name:'1440'}, {width:1920,height:1080,name:'1920'},
 {width:844,height:390,name:'landscape-844x390'}, {width:1024,height:500,name:'landscape-1024x500'},
 {width:720,height:450,name:'zoom-200-percent-proxy'}
];
const sleep=ms=>new Promise(resolve=>setTimeout(resolve,ms));

(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
  // Direct reading: each chapter is in document flow and every capture fits its stage.
  for(const viewport of viewportSet){
   const page=await browser.newPage({viewport:{width:viewport.width,height:viewport.height},reducedMotion:'no-preference'});
   const errors=[];page.on('pageerror',error=>errors.push(error.message));
   const response=await page.goto(base+'/',{waitUntil:'networkidle'});assert.equal(response.status(),200);
   await page.locator('#motion-mode').selectOption('direct');
   const direct=await page.evaluate(()=>({
    mode:document.documentElement.dataset.motionMode,
    width:innerWidth,
    overflow:document.documentElement.scrollWidth-innerWidth,
    slides:[...document.querySelectorAll('.world-slide')].map(slide=>({
     position:getComputedStyle(slide).position,visible:getComputedStyle(slide).visibility,
     inert:slide.inert,thumbs:slide.querySelectorAll('.world-tab-thumb').length
    }))
   }));
   assert.equal(direct.mode,'direct');assert.ok(direct.overflow<=1);assert.equal(direct.slides.length,5);
   assert.ok(direct.slides.every(slide=>slide.position==='relative'&&slide.visible==='visible'&&!slide.inert));
   const captionReadability=await page.locator('.world-slide').first().evaluate(slide=>{
    const caption=slide.querySelector('.world-description'),heading=caption.querySelector('h3'),body=caption.querySelector('.world-desc-context');
    return {background:getComputedStyle(caption).backgroundColor,heading:getComputedStyle(heading).color,body:getComputedStyle(body).color,summary:getComputedStyle(caption.querySelector('.world-actions-head')).color,kicker:getComputedStyle(caption.querySelector('.world-desc-kicker')).color};
   });
   assert.equal(captionReadability.background,'rgb(250, 249, 246)',`${viewport.name}: direct caption must have an opaque reading surface`);
   assert.equal(captionReadability.heading,'rgb(18, 25, 29)',`${viewport.name}: direct heading contrast regressed`);
   assert.equal(captionReadability.summary,'rgb(32, 51, 64)',`${viewport.name}: direct evidence summary contrast regressed`);
   assert.equal(captionReadability.kicker,'rgb(148, 53, 31)',`${viewport.name}: direct caption kicker contrast regressed`);
   let imageMeasures=[],thumbsChecked=0;
   for(let i=0;i<5;i++){
    const slide=page.locator('.world-slide').nth(i);await slide.scrollIntoViewIfNeeded();
    const tabs=slide.locator('.world-tab');
    for(let j=0;j<await tabs.count();j++){
     await tabs.nth(j).click();
     await page.waitForFunction(({i,j})=>document.querySelectorAll('.world-slide')[i].querySelectorAll('.world-tab')[j].getAttribute('aria-pressed')==='true',{i,j});
     const image=slide.locator('.world-main-image');
     await image.evaluate(img=>img.decode().catch(()=>{}));
     const measure=await image.evaluate(img=>{const r=img.getBoundingClientRect();return {src:new URL(img.currentSrc||img.src).pathname,width:r.width,height:r.height,naturalWidth:img.naturalWidth,complete:img.complete,maxHeight:getComputedStyle(img).maxHeight}});
     assert.ok(measure.complete&&measure.naturalWidth>0,`${viewport.name} highlight ${i+1}, capture ${j+1} did not load`);
     const thumb=tabs.nth(j).locator('.world-tab-thumb');
     if(await thumb.count()){
      await thumb.evaluate(img=>img.decode().catch(()=>{}));
      assert.ok(await thumb.evaluate(img=>img.complete&&img.naturalWidth>0),`${viewport.name} highlight ${i+1}, thumbnail ${j+1} did not load`);thumbsChecked++;
     }
     assert.ok(measure.width<=viewport.width+1,`${viewport.name}: image wider than viewport ${measure.width}`);
     assert.ok(measure.height<=520+1,`${viewport.name}: image exceeded direct-read cap ${measure.height}`);
     const evidenceId=await tabs.nth(j).getAttribute('data-evidence-id');
     assert.ok((await slide.locator('.world-case-link').getAttribute('href')).endsWith('#media-'+evidenceId),`${viewport.name}: case link does not target capture ${evidenceId}`);
     imageMeasures.push(measure);
    }
   }
   if(['390','1440'].includes(viewport.name)){
    await page.locator('.world-slide').first().locator('.world-tab').first().click();
    await page.waitForFunction(()=>document.querySelector('.world-slide .world-tab').getAttribute('aria-pressed')==='true');
    await page.locator('.world-slide').first().evaluate(slide=>slide.scrollIntoView({block:'start'}));await sleep(140);
    await page.screenshot({path:path.join(out,`after-direct-${viewport.name}.png`)});
    if(viewport.name==='390')await page.screenshot({path:path.join(out,'after-direct-390-full.png'),fullPage:true});
   }
   report.viewports.push({viewport,direct,captionReadability,imagesChecked:imageMeasures.length,thumbsChecked,maxImageHeight:Math.max(...imageMeasures.map(image=>image.height)),errors});
   assert.deepEqual(errors,[]);
   await page.close();
  }

  // Automatic follows the OS; explicit motion restores the desktop narrative even on reduce.
  for(const preference of ['no-preference','reduce']){
   const page=await browser.newPage({viewport:{width:1440,height:900},reducedMotion:preference});
   const errors=[];page.on('pageerror',error=>errors.push(error.message));
   await page.goto(base+'/',{waitUntil:'networkidle'});
   const auto=await page.evaluate(()=>({effective:document.documentElement.dataset.motionEffective,sticky:getComputedStyle(document.querySelector('.v8-world-sticky')).position}));
   assert.equal(auto.effective,preference==='reduce'?'direct':'animated');
   if(preference==='reduce')assert.equal(auto.sticky,'static');
   await page.locator('#motion-mode').selectOption('motion');await sleep(150);
   const forced=await page.evaluate(()=>({mode:document.documentElement.dataset.motionMode,direct:document.documentElement.classList.contains('v11-direct'),sticky:getComputedStyle(document.querySelector('.v8-world-sticky')).position,worldHeight:document.querySelector('.v8-world').offsetHeight}));
   assert.equal(forced.mode,'motion');assert.equal(forced.direct,false);assert.equal(forced.sticky,'sticky');
   const active=[],progressSamples=[0,.125,.25,.375,.5,.625,.75,.875,1],expectedActive=[0,0,1,1,2,2,3,3,4];
   for(const [step,progress] of progressSamples.entries()){
    await page.evaluate(progress=>{const world=document.querySelector('.v8-world');scrollTo(0,world.getBoundingClientRect().top+scrollY+(world.offsetHeight-innerHeight)*progress)},progress);
    await sleep(110);
    const state=await page.evaluate(()=>({active:[...document.querySelectorAll('.world-slide')].findIndex(slide=>slide.getAttribute('aria-hidden')==='false'),visible:[...document.querySelectorAll('.world-slide')].filter(slide=>getComputedStyle(slide).visibility==='visible').length,opacity:+getComputedStyle(document.querySelector('.world-slide[aria-hidden="false"] .world-art')).opacity,overflow:document.documentElement.scrollWidth-innerWidth}));
    active.push(state.active);assert.ok(state.overflow<=1);assert.equal(state.active,expectedActive[step]);
    assert.equal(state.visible,1,`${preference} at ${progress}: scenes must never stack`);
    assert.ok(state.opacity>=.03,`${preference} at ${progress}: the active capture became imperceptible`);
    if(step===0||step===4||step===8)await page.screenshot({path:path.join(out,`motion-${preference}-${step===0?0:step===4?2:4}.png`)});
    if([1,3,5,7].includes(step))await page.screenshot({path:path.join(out,`motion-transition-${preference}-${progress.toString().replace('.','-')}.png`)});
   }
   assert.deepEqual(active,expectedActive);
   if(errors.length)throw new Error(errors.join('\n'));
   report.motion.push({preference,auto,forced,activeSequence:active,errors});await page.close();
  }

  // The OS reduced-motion preference in Auto must also fit the narrowest viewport.
  {
   const page=await browser.newPage({viewport:{width:320,height:700},reducedMotion:'reduce'});await page.goto(base+'/',{waitUntil:'networkidle'});
   const state=await page.evaluate(()=>({mode:document.documentElement.dataset.motionMode,effective:document.documentElement.dataset.motionEffective,overflow:document.documentElement.scrollWidth-innerWidth,slides:[...document.querySelectorAll('.world-slide')].map(slide=>({visible:getComputedStyle(slide).visibility,position:getComputedStyle(slide).position,inert:slide.inert})),labels:[...document.querySelectorAll('.world-scene-label')].map(label=>({left:label.getBoundingClientRect().left,right:label.getBoundingClientRect().right}))}));
   assert.equal(state.mode,'auto');assert.equal(state.effective,'direct');assert.ok(state.overflow<=1);assert.ok(state.slides.every(slide=>slide.visible==='visible'&&slide.position==='relative'&&!slide.inert));assert.ok(state.labels.every(label=>label.left>=0&&label.right<=320));
   report.motion.push({preference:'auto-reduced-320',state});await page.close();
  }

  // Changing preference keeps the active project and its selected capture.
  {
   const page=await browser.newPage({viewport:{width:1440,height:900}});await page.goto(base+'/',{waitUntil:'networkidle'});
   await page.evaluate(()=>{const w=document.querySelector('.v8-world');scrollTo(0,w.getBoundingClientRect().top+scrollY+(w.offsetHeight-innerHeight)*.5)});await sleep(160);
   const selectedProject=page.locator('.world-slide').nth(2);await selectedProject.locator('.world-tab').nth(2).click();await sleep(60);
   await page.locator('#motion-mode').selectOption('direct');await sleep(180);
   const directState=await page.evaluate(()=>({active:Number(document.querySelector('.v11-world-jumpbar .is-current')?.dataset.jump??0),selected:[...document.querySelectorAll('.world-slide')][2].querySelector('.world-tab[aria-pressed="true"]')?.dataset.view}));
   assert.equal(directState.active,2);assert.equal(directState.selected,'2');
   await page.locator('#motion-mode').selectOption('motion');await sleep(180);
   const animatedState=await page.evaluate(()=>({active:[...document.querySelectorAll('.world-slide')].findIndex(slide=>slide.getAttribute('aria-hidden')==='false'),selected:[...document.querySelectorAll('.world-slide')][2].querySelector('.world-tab[aria-pressed="true"]')?.dataset.view}));
   assert.equal(animatedState.active,2);assert.equal(animatedState.selected,'2');
   report.motion.push({preference:'mode-switch-preservation',directState,animatedState});await page.close();
  }

  // Storage denial and image failures must degrade to usable text instead of blocking the page.
  {
   const page=await browser.newPage({viewport:{width:390,height:844}});
   await page.addInitScript(()=>{Storage.prototype.setItem=function(){throw new Error('storage denied for QA')}});
   await page.goto(base+'/',{waitUntil:'networkidle'});await page.locator('#motion-mode').selectOption('direct');
   assert.equal(await page.locator('html').getAttribute('data-motion-mode'),'direct');
   await page.locator('.world-slide').first().evaluate(slide=>{slide.querySelector('.world-main-image').src='/assets/missing-motion-qa.png'});
   await page.waitForFunction(()=>document.querySelector('.world-slide .world-image-fallback')?.hidden===false);
   assert.ok(await page.locator('.world-slide').first().locator('.world-image-fallback').isVisible());
   report.storageAndFallback={preferenceWorksWithoutStorage:true,homeImageFailureShowsMessage:true};await page.close();
  }

  // Every case route, gallery image and deep link is checked against the generated evidence list.
  const {projects}=await import('../src/data.js');
  for(const project of projects){
   const page=await browser.newPage({viewport:{width:390,height:844}});const errors=[],responses=[];
   page.on('pageerror',error=>errors.push(error.message));
   page.on('response',response=>{if(response.url().startsWith(base)&&response.status()>=400)responses.push({url:response.url(),status:response.status()})});
   const response=await page.goto(base+'/projetos/'+project.slug+'/',{waitUntil:'networkidle'});assert.equal(response.status(),200,project.slug);
   if(await page.locator('.v14-protected-disclosure').count())await page.locator('.v14-protected-disclosure summary').click();
   const choices=page.locator('[data-v14-select]');
   for(let i=0;i<await choices.count();i++){
    await choices.nth(i).click();
    const active=page.locator('.v14-slide:not([hidden]) img').first();
    if(await active.count()){
     await active.scrollIntoViewIfNeeded();await active.evaluate(img=>img.decode().catch(()=>{}));
     assert.ok(await active.evaluate(img=>img.complete&&img.naturalWidth>0),`${project.slug}: gallery image ${i+1} missing`);
    }
   }
   const evidence=await page.locator('.gallery-item[data-evidence-id]').evaluateAll(items=>items.map(item=>({id:item.dataset.evidenceId,hidden:item.hidden,src:item.querySelector('img')?.getAttribute('src')})));
   const ids=new Set(evidence.map(item=>item.id));assert.equal(ids.size,evidence.length,`${project.slug}: duplicate evidence IDs`);
   for(const item of evidence){
    const figure=page.locator(`#media-${item.id}`),trigger=figure.locator('.gallery-trigger').first();
    if(await trigger.count()){
     if(await page.locator('#evidence-dialog').count()){
      if(await page.locator('#evidence-dialog').evaluate(dialog=>dialog.open))await page.locator('#evidence-close').click();
      if(await figure.evaluate(element=>element.hidden)){
       const frame=await figure.getAttribute('data-v14-shot');
       const control=frame===null?page.locator(`[data-v14-select="${evidence.findIndex(shot=>shot.id===item.id)}"]`):page.locator(`[data-v14-select="${frame}"]`);
       if(await control.count())await control.click();
      }
      await trigger.click();assert.ok(await page.locator('#evidence-dialog').evaluate(dialog=>dialog.open));await page.keyboard.press('Escape');assert.equal(await page.locator('#evidence-dialog').evaluate(dialog=>dialog.open),false);
     }
    }
   }
   if(errors.length||responses.length)throw new Error(`${project.slug}: ${JSON.stringify({errors,responses})}`);
   report.cases.push({slug:project.slug,status:response.status(),evidenceCount:evidence.length,evidenceIds:evidence.map(item=>item.id),errors,responses});
   if(project.slug==='producao-operacional'){
    assert.deepEqual(await page.locator('[data-v14-select] strong').allTextContents(),['Painel de dados','Ordens de produção','Acompanhamento na TV','Setores e configuração']);
    await page.locator('[data-v14-select="0"]').click();
    await page.screenshot({path:path.join(out,'after-production-case-mobile.png'),fullPage:true});
    for(let i=0;i<4;i++){
     const id=await page.locator(`.v14-slide[data-v14-shot="${i}"]`).getAttribute('id');
     const deep=await browser.newPage({viewport:{width:390,height:844}});
     await deep.goto(base+'/projetos/producao-operacional/#'+id,{waitUntil:'networkidle'});
     const target=deep.locator('#'+id);assert.equal(await target.evaluate(figure=>figure.hidden),false,`Production deep link ${i+1} did not select its screenshot`);
     const image=target.locator('img');await image.evaluate(img=>img.decode().catch(()=>{}));assert.ok(await image.evaluate(img=>img.complete&&img.naturalWidth>0));await deep.close();
    }
   }
   await page.close();
  }

  // No-JavaScript path: the same five sections and their first real captures remain in flow.
  {
   const page=await browser.newPage({viewport:{width:390,height:844},javaScriptEnabled:false});
   await page.goto(base+'/',{waitUntil:'networkidle'});
   const state=await page.locator('.world-slide').evaluateAll(slides=>slides.map(slide=>({height:slide.getBoundingClientRect().height,position:getComputedStyle(slide).position,visibility:getComputedStyle(slide).visibility,opacity:getComputedStyle(slide).opacity,image:slide.querySelector('.world-main-image')?.getAttribute('src')})));
   assert.equal(state.length,5);assert.ok(state.every(slide=>slide.height>0&&slide.position==='relative'&&slide.visibility==='visible'&&slide.opacity!=='0'&&slide.image));
   await page.screenshot({path:path.join(out,'after-nojs-mobile.png'),fullPage:true});report.noJavascript={scenes:state};await page.close();
  }
 }catch(error){report.failures.push(error.stack||error);throw error}
 finally{
  fs.writeFileSync(path.join(out,'qa-motion-gallery-fix.json'),JSON.stringify(report,null,2));await browser.close();
 }
 console.log(JSON.stringify({viewports:report.viewports.length,cases:report.cases.length,motion:report.motion.length,failures:report.failures.length}));
})().catch(error=>{console.error(error.stack||error);process.exitCode=1});
