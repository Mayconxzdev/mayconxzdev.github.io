const {chromium}=require('playwright');
const fs=require('fs');
const path=require('path');
(async()=>{
const browser=await chromium.launch({headless:true});
const evidenceDir=path.resolve(process.env.TEST_CV_EVIDENCE||path.resolve(__dirname,'../evidence/cv'));
fs.mkdirSync(evidenceDir,{recursive:true});
const expectedPT=[
'Maycon_Ferreira_Geral_Automacao_IA_PT.pdf',
'Maycon_Ferreira_Agentes_Automacao_n8n_PT.pdf',
'Maycon_Ferreira_Produtos_Conteudo_IA_PT.pdf'
];
const expectedEN=[
'Maycon_Ferreira_General_Automation_AI_EN.pdf',
'Maycon_Ferreira_AI_Agents_Automation_n8n_EN.pdf',
'Maycon_Ferreira_AI_Digital_Products_Content_EN.pdf'
];
const expectedAliases=[
'Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf',
'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
'Maycon_Ferreira_IA_Agentes_MCP.pdf',
'Maycon_Ferreira_Automacao_Integracoes.pdf',
'Maycon_Ferreira_Dados_BI.pdf',
'Maycon_Ferreira_Sistemas_Backend.pdf',
'Maycon_Ferreira_Web_Produtos_Digitais.pdf',
'Maycon_Ferreira_Conteudo_Video_IA.pdf',
'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf'
];
const results=[];
for(const width of [320,360,390,430,768,1024,1440,1920]){
const p=await browser.newPage({viewport:{width,height:width>=1440?900:844}});
const errors=[];p.on('pageerror',e=>errors.push(e.message));
const main=await p.goto('http://127.0.0.1:4214/',{waitUntil:'domcontentloaded'});
await p.locator('#curriculos').scrollIntoViewIfNeeded();await p.waitForTimeout(120);
if([390,1440].includes(width))await p.screenshot({path:path.join(evidenceDir,`home-cv-${width}-after.png`),fullPage:false});
const pt=await p.locator('#cv-grid .cv-card:visible').count();
const ptLinks=await p.locator('#cv-grid .cv-card').evaluateAll(a=>a.map(x=>new URL(x.href).pathname.split('/').pop()));
const enLink=await p.locator('#curriculos .v16-cv-languages a').getAttribute('href');
const english=await p.goto('http://127.0.0.1:4214'+enLink,{waitUntil:'domcontentloaded'});
const enLinks=await p.locator('main a[type="application/pdf"]').evaluateAll(a=>a.map(x=>new URL(x.href).pathname.split('/').pop()));
const enHeadings=await p.locator('main h2').allTextContents();
const enRobots=await p.locator('meta[name="robots"]').getAttribute('content');
const overflow=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
const catalog=await p.goto('http://127.0.0.1:4214/assets/cv/',{waitUntil:'domcontentloaded'});
if([390,1440].includes(width))await p.screenshot({path:path.join(evidenceDir,`catalog-${width}-after.png`),fullPage:true});
const catalogLinks=await p.locator('a[href$=".pdf"]').evaluateAll(a=>a.map(x=>new URL(x.href).pathname.split('/').pop()));
const catalogGeometry=await p.locator('a[href$=".pdf"]').evaluateAll(a=>a.map(x=>{let r=x.getBoundingClientRect();return {left:Math.round(r.left),right:Math.round(r.right),top:Math.round(r.top),bottom:Math.round(r.bottom),width:Math.round(r.width),height:Math.round(r.height)}}));
const catalogOverflow=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
const httpStatuses=[];
for(const name of [...expectedPT,...expectedEN,...expectedAliases]){let res=await p.request.get('http://127.0.0.1:4214/assets/cv/'+name);httpStatuses.push(res.status())}
results.push({width,httpPT:main.status(),httpEN:english.status(),httpCatalog:catalog.status(),pt,en:enLinks.length,ptLinks,enLinks,enHeadings,enRobots,catalogLinks,catalogGeometry,overflow,catalogOverflow,errors,pdfStatuses:httpStatuses});
await p.close();
}
await browser.close();console.log(JSON.stringify(results,null,2));
fs.writeFileSync(path.join(evidenceDir,'cv-qa-current.json'),JSON.stringify({date:new Date().toISOString(),base:'http://127.0.0.1:4214',results},null,2));
if(results.some(r=>r.httpPT!==200||r.httpEN!==200||r.httpCatalog!==200||r.pt!==3||r.en!==3||r.catalogLinks.length!==6||r.catalogLinks.some(x=>![...expectedPT,...expectedEN].includes(x))||r.catalogOverflow>1||r.catalogGeometry.some(g=>g.left<0||g.right>r.width||g.height<35)||r.overflow>1||r.errors.length||r.ptLinks.some((x,i)=>x!==expectedPT[i])||r.enLinks.some((x,i)=>x!==expectedEN[i])||r.enRobots!=='noindex,nofollow'||r.enHeadings.length!==3||!r.enHeadings[1].includes('Development')||!r.enHeadings[2].includes('Digital Products')||r.pdfStatuses.some(x=>x!==200)))process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exitCode=2});
