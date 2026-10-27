const{chromium}=require('playwright'),fs=require('fs');
(async()=>{
const browser=await chromium.launch({headless:true}),base='http://127.0.0.1:4214',checks=[],issues=[],out='evidence/v15';
fs.mkdirSync(out,{recursive:true});
for(const width of [1440,390,320]){
 const context=await browser.newContext({viewport:{width,height:width===1440?900:width===390?844:700},reducedMotion:'reduce'});
 const home=await context.newPage();const errs=[];home.on('pageerror',e=>errs.push(e.message));
 const response=await home.goto(base,{waitUntil:'networkidle'});
 await home.locator('#acervo').scrollIntoViewIfNeeded();
 await home.screenshot({path:out+'/archive-'+width+'.png',animations:'disabled'});
 const order=await home.locator('#catalog-grid [data-project]').evaluateAll(els=>els.map(el=>el.dataset.project));
 const overflow=await home.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 checks.push({width,page:'home',http:response.status(),order,overflow,errors:errs});
 if(overflow||order.slice(0,3).join()!=='engenharia-de-dados-compass,sites-industriais,compras-e-cotacoes'||errs.length)issues.push({width,page:'home',order:order.slice(0,3),overflow,errs});
 await home.close();
 const slugs=['engenharia-de-dados-compass','sites-industriais','compras-e-cotacoes','tradutor-documental','gestao-de-propostas','videomind','brasil-as-claras','arsenalmind','gestao-de-locacao','conversa360','producao-operacional','zero21fotos'];
 for(const slug of slugs){
  const page=await context.newPage();let errors=[];page.on('pageerror',e=>errors.push(e.message));
  let res=await page.goto(base+'/projetos/'+slug+'/',{waitUntil:'networkidle'});
  let g=page.locator('[data-v14-gallery]'),n=await g.count(),gallery=page.locator('.case-gallery'),cnt=await gallery.count();
  let selected='',hiddenCount=0,dialogs=await page.locator('#evidence-dialog').count();
  if(n){
   const buttons=g.locator('[data-v14-select]');let count=await buttons.count();
   if(count>1){await buttons.nth(1).click(); selected=await buttons.nth(1).getAttribute('aria-pressed');}
   hiddenCount=await g.locator('.v14-slide[hidden]').count();
  }
  if(slug==='gestao-de-propostas')await page.locator('.v14-protected-disclosure summary').click();
  const trigger=page.locator('.gallery-trigger:visible').first();
  let modal=false;
  if(await trigger.count()){
   await trigger.click();modal=await page.locator('#evidence-dialog').evaluate(el=>el.open);
   await page.locator('#evidence-close').click();
  }
  const summary=await page.evaluate(()=>({
    overflow:document.documentElement.scrollWidth>innerWidth,
    imageCount:document.querySelectorAll('.v14-slide img').length,
    broken:[...document.querySelectorAll('.v14-slide img')].filter(i=>i.complete&&(!i.naturalWidth)).length,
    h1:document.querySelectorAll('h1').length,
    subject:document.querySelector('.v14-diagram h2,.v14-gallery-head h2,.v14-intro h2,.v14-protected-lead h2')?.textContent.slice(0,110)||'',
    status:document.querySelector('.v13-status')?.textContent
  }));
  if(width!==320||['sites-industriais','tradutor-documental'].includes(slug))await page.screenshot({path:out+'/'+slug+'-'+width+'.png',animations:'disabled'});
  const result={width,slug,http:res.status(),count:cnt,tabs:n,selected,hiddenCount,dialogs,modal,...summary,errors};
  checks.push(result);
  if(res.status()!==200||summary.h1!==1||summary.overflow||summary.broken||cnt>1||errors.length||(cnt&& !modal)|| (n&&selected!=='true'))issues.push(result);
  await page.close();
 }
 await context.close();
}
await browser.close();fs.writeFileSync(out+'/qa-main.json',JSON.stringify({checks,issues},null,2));
console.log(JSON.stringify({checks:checks.length,issues:issues.slice(0,5),failureCount:issues.length,home:checks[0]},null,2).slice(0,4500));
if(issues.length)process.exitCode=2;
})().catch(err=>{console.error(err.stack);process.exit(2)});
