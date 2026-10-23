const {chromium}=require('playwright');
const fs=require('node:fs'),path=require('node:path');
(async()=>{
 const browser=await chromium.launch(process.env.CI ? {headless:true} : {channel:'msedge',headless:true});
 const base='http://127.0.0.1:4190';
 const out=path.resolve(__dirname,'../evidence/browser');
 fs.mkdirSync(out,{recursive:true});
 const result=[];
 for(const w of [1440,768,390,320]){
  const page=await browser.newPage({viewport:{width:w,height:w===1440?900:w===768?1024:844},deviceScaleFactor:1});
  const errors=[],fails=[];page.on('pageerror',e=>errors.push(e.message));page.on('requestfailed',r=>fails.push(r.url()));
  await page.goto(base+'/',{waitUntil:'domcontentloaded'});
  await page.waitForTimeout(1400);
  const data={viewport:w,title:await page.title(),h1:await page.locator('h1').first().innerText(),cards:await page.locator('.catalog-item').count(),cvs:await page.locator('.cv-card').count(),horizontalOverflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),errors:[],requestsFailed:[]};
  await page.screenshot({path:path.join(out,'home-'+w+'.png'),fullPage:false});
  await page.locator('#sim-next').click();
  data.simulationAfter=await page.locator('#sim-title').innerText();
  await page.locator('#sim-next').click();data.simulationFinal=await page.locator('#sim-title').innerText();
  await page.locator('#sim-reset').click();data.simulationReset=await page.locator('#sim-title').innerText();
  await page.locator('#project-search').fill('Manutenção');
  data.filtered=await page.locator('.catalog-item').count();
  await page.locator('#project-search').fill('');
  await page.locator('[data-filter=ia]').click();
  data.iaFiltered=await page.locator('.catalog-item').count();
  await page.locator('[data-filter=all]').click();
  await page.locator('[data-method="2"]').click();
  data.method=await page.locator('#method-name').innerText();
  if(w<=768){await page.locator('#menu-toggle').click();data.menuOpen=await page.locator('#nav').evaluate(x=>x.classList.contains('open'));await page.locator('#menu-toggle').click();}
  await page.locator('#projetos').scrollIntoViewIfNeeded();await page.waitForTimeout(400);await page.screenshot({path:path.join(out,'projetos-'+w+'.png'),fullPage:false});
  await page.locator('#curriculos').scrollIntoViewIfNeeded();await page.waitForTimeout(400);await page.screenshot({path:path.join(out,'curriculos-'+w+'.png'),fullPage:false});
  data.imagesBroken=await page.locator('img').evaluateAll(images=>images.filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src));
  data.errors=errors;data.requestsFailed=fails.filter(x=>!x.includes('fonts.googleapis'));
  result.push(data);await page.close();
 }
 const page=await browser.newPage();
 const routes=['/projetos/producao-operacional/','/projetos/manutencao-em-campo/','/projetos/belarc-inventory/','/projetos/zero21fotos/','/cases/producao-operacional/'];
 const routeResults=[];
 for(const route of routes){const r=await page.goto(base+route,{waitUntil:'domcontentloaded'});routeResults.push({route,status:r.status(),title:await page.title()});}
 const resumes=['Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf','Maycon_Ferreira_IA_Agentes_MCP.pdf','Maycon_Ferreira_Automacao_Integracoes.pdf','Maycon_Ferreira_Dados_BI.pdf','Maycon_Ferreira_Sistemas_Backend.pdf','Maycon_Ferreira_Web_Produtos_Digitais.pdf','Maycon_Ferreira_Conteudo_Video_IA.pdf','Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf'];
 const resumeResults=[];
 for(const file of resumes){const response=await page.request.get(base+'/assets/cv/'+file);resumeResults.push({name:file,status:response.status(),bytes:(await response.body()).length});}
 await page.close();await browser.close();
 fs.writeFileSync(path.join(out,'audit.json'),JSON.stringify({viewports:result,routes:routeResults,resumes:resumeResults},null,2));
 console.log(JSON.stringify({viewports:result,routes:routeResults,resumes:resumeResults}));
})().catch(e=>{console.error(e.stack);process.exit(1)})