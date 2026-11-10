const {chromium}=require("playwright"),fs=require("fs"),path=require("path");
(async()=>{
 const browser=await chromium.launch({headless:true});
 const dir=path.resolve(__dirname,"../evidence/cv");fs.mkdirSync(dir,{recursive:true});
 const pt=["Maycon_Ferreira_IA_Aplicada_Agentes_PT_2026_V2.pdf","Maycon_Ferreira_Backend_Integracoes_PT_2026_V2.pdf"];
 const en=["Maycon_Ferreira_Applied_AI_Agents_EN_2026_V2.pdf","Maycon_Ferreira_Backend_Integrations_EN_2026_V2.pdf"];
 const legacy=["Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf","Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf","Maycon_Ferreira_IA_Agentes_MCP.pdf","Maycon_Ferreira_Automacao_Integracoes.pdf","Maycon_Ferreira_Dados_BI.pdf","Maycon_Ferreira_Sistemas_Backend.pdf","Maycon_Ferreira_Web_Produtos_Digitais.pdf","Maycon_Ferreira_Conteudo_Video_IA.pdf","Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf","Maycon_Ferreira_Geral_Automacao_IA_PT.pdf","Maycon_Ferreira_Agentes_Automacao_n8n_PT.pdf","Maycon_Ferreira_Produtos_Conteudo_IA_PT.pdf","Maycon_Ferreira_General_Automation_AI_EN.pdf","Maycon_Ferreira_AI_Agents_Automation_n8n_EN.pdf","Maycon_Ferreira_AI_Digital_Products_Content_EN.pdf"];
 const result=[],issues=[],base="http://127.0.0.1:4214";
 try{
 for(const width of [320,390,768,1440]){
  const p=await browser.newPage({viewport:{width,height:900}});
  const errors=[];p.on("pageerror",e=>errors.push(e.message));
  let res=await p.goto(base+"/",{waitUntil:"domcontentloaded"});
  const ptCards=await p.locator("#cv-grid .cv-card").evaluateAll(xs=>xs.map(x=>new URL(x.href).pathname.split("/").pop()));
  let overflow=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
  let english=await p.goto(base+"/en/resumes/",{waitUntil:"domcontentloaded"});
  const enCards=await p.locator('a[type="application/pdf"]').evaluateAll(xs=>xs.map(x=>new URL(x.href).pathname.split("/").pop()));
  const enRobots=await p.locator('meta[name="robots"]').getAttribute("content");
  let catalog=await p.goto(base+"/assets/cv/",{waitUntil:"domcontentloaded"});
  const catalogLinks=await p.locator('a[href$=".pdf"]').evaluateAll(xs=>xs.map(x=>new URL(x.href).pathname.split("/").pop()));
  const geo=await p.locator('a[href$=".pdf"]').evaluateAll(xs=>xs.map(x=>({left:x.getBoundingClientRect().left,right:x.getBoundingClientRect().right,height:x.getBoundingClientRect().height})));
  const catOverflow=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
  if([390,1440].includes(width))await p.screenshot({path:path.join(dir,"current-"+width+".png"),fullPage:true,animations:"disabled"});
  const statuses=[];
  for(const name of [...pt,...en,...legacy])statuses.push((await p.request.get(base+"/assets/cv/"+name)).status());
  const test={width,home:res.status(),english:english.status(),catalog:catalog.status(),ptCards,enCards,catalogLinks,enRobots,overflow,catOverflow,geo,errors,pdfStatuses:statuses};
  result.push(test);
  if(test.home!==200||test.english!==200||test.catalog!==200||JSON.stringify(ptCards)!==JSON.stringify(pt)||JSON.stringify(enCards)!==JSON.stringify(en)||catalogLinks.length!==4||catalogLinks.some(x=>![...pt,...en].includes(x))||overflow>1||catOverflow>1||geo.some(g=>g.left<0||g.right>width||g.height<35)||errors.length||statuses.some(x=>x!==200)||enRobots!=="noindex,follow")issues.push(test);
  await p.close();
 }
 }finally{await browser.close();}
 fs.writeFileSync(path.join(dir,"cv-qa-current.json"),JSON.stringify({results:result,issues},null,2));
 console.log(JSON.stringify({widths:result.map(x=>x.width),failures:issues.length,curricula:4,legacy:legacy.length,examples:issues.slice(0,2)},null,2).slice(0,8000));
 if(issues.length)process.exitCode=2;
})().catch(e=>{console.error(e.stack);process.exitCode=2});
