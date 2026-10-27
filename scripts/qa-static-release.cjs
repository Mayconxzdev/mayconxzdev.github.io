const fs=require('fs'),path=require('path'),http=require('http'),{chromium}=require('playwright');
const folder=path.resolve(__dirname,'../../PUBLICAR_SITE_V15');
const mimetype={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json','.png':'image/png','.jpg':'image/jpeg','.webp':'image/webp','.pdf':'application/pdf','.svg':'image/svg+xml','.woff2':'font/woff2','.xml':'application/xml','.txt':'text/plain'};
const server=http.createServer((req,res)=>{let file=decodeURIComponent(req.url.split('?')[0]).split('#')[0];const loc=path.resolve(folder,'.'+file);if(!loc.startsWith(folder+path.sep)&&loc!==folder){res.writeHead(403);return res.end()}let target=loc;if(fs.existsSync(target)&&fs.statSync(target).isDirectory())target=path.join(target,'index.html');if(!fs.existsSync(target)){res.writeHead(404);return res.end()}res.writeHead(200,{'Content-Type':mimetype[path.extname(target)]||'application/octet-stream'});fs.createReadStream(target).pipe(res)});
(async()=>{
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const url='http://127.0.0.1:'+server.address().port;
const browser=await chromium.launch({headless:true}),results=[];
const cases=fs.readdirSync(path.join(folder,'projetos'),{withFileTypes:true}).filter(x=>x.isDirectory()&&fs.existsSync(path.join(folder,'projetos',x.name,'index.html'))).map(x=>'/projetos/'+x.name+'/');
try{
for(const width of [390,1440]){
const context=await browser.newContext({viewport:{width,height:900},reducedMotion:'reduce'});
for(const route of ['/',...cases]){
const p=await context.newPage();let errors=[];p.on('pageerror',e=>errors.push(e.message));
let r=await p.goto(url+route,{waitUntil:'domcontentloaded',timeout:15000});await p.waitForTimeout(80);
const stats=await p.evaluate(()=>({noindex:document.querySelector('meta[name=robots]')?.content||null,bodyOverflow:document.documentElement.scrollWidth-innerWidth,imgs:[...document.images].filter(i=>i.getAttribute('src')&&i.complete&&!i.naturalWidth).length}));
results.push({width,route,status:r.status(),errors,...stats});await p.close()}
await context.close();
}
const pdf=await browser.newPage();
let resume=await pdf.request.get(url+'/assets/cv/Maycon_Ferreira_Geral_Automacao_IA_PT.pdf');
let robots=await(await pdf.request.get(url+'/robots.txt')).text();
await pdf.close();
const fails=results.filter(x=>x.status!==200||x.errors.length||x.bodyOverflow>1||x.imgs||x.noindex==='noindex,nofollow'&&!/carreirapessoal|postagem-redes/.test(x.route));
const report={routes:results.length,failures:fails.length,errors:fails,cvHttp:resume.status(),robotsAllowsIndexing:robots.includes('Allow: /')&&!robots.includes('Disallow: /'),results};
fs.writeFileSync(path.resolve(folder,'../ENTREGA_V15_TESTE_ESTATICO.json'),JSON.stringify(report,null,2));
console.log(JSON.stringify({checks:results.length,failures:fails.length,pdf:resume.status(),robots:report.robotsAllowsIndexing,examples:fails.slice(0,5)},null,2));
if(fails.length||!report.robotsAllowsIndexing||resume.status()!==200)process.exitCode=2;
}finally{await browser.close();server.close()}
})().catch(e=>{console.error(e.stack);server.close();process.exitCode=2});
