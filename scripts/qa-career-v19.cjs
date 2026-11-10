// Independent, repeatable assertions for the final career release.
// Run after npm run build. Structural checks only; browser QA runs separately.
const fs=require("node:fs"),path=require("node:path"),assert=require("node:assert/strict");
const root=path.resolve(__dirname,".."),dist=path.join(root,"dist");
const read=p=>fs.readFileSync(path.join(dist,p),"utf8");
const exists=p=>fs.existsSync(path.join(dist,p));
const index=read("index.html"),en=read("en/index.html");
const data=JSON.parse(fs.readFileSync(path.join(root,"scripts/resumes-content.json"),"utf8"));
const checks=[];
function check(label,fn){fn();checks.push(label)}
check("four canonical resumes",()=>{
  assert.equal(data.resumes.length,4);
  assert.deepEqual(data.resumes.map(r=>r.id),["pt_ai","pt_sw","en_ai","en_sw"]);
  assert(!data.resumes.find(r=>r.id==="pt_sw").credentials.includes("42 Rio"));
  for(const item of data.resumes)assert(exists("assets/cv/"+item.file),item.file);
});
check("favicon paths",()=>{
  assert(exists("assets/favicon.svg"))
  for (const page of ["404.html","estudos/desapega-ai/index.html"]){
    const pageHtml=read(page);
    assert(pageHtml.includes('href="/assets/favicon.svg"'),"missing favicon in "+page);
    assert(!pageHtml.includes('href="/favicon.svg"'),"old favicon in "+page);
  };
  assert(index.includes('href="/assets/favicon.svg"'));
  assert(en.includes('href="/assets/favicon.svg"'));
  const cases=fs.readdirSync(path.join(dist,"projetos"),{withFileTypes:true}).filter(d=>d.isDirectory()&&exists("projetos/"+d.name+"/index.html"));
  assert.equal(cases.length,18);
  for(const p of cases){
    const html=read("projetos/"+p.name+"/index.html");
    assert(html.includes('href="/assets/favicon.svg"'),"favicon "+p.name);
    assert(!html.includes('href="/favicon.svg"'),"legacy favicon "+p.name);
  }
});
check("English landing is indexable, bilingual and factual",()=>{
  assert(en.includes('<html lang="en">'));
  assert(en.includes('name="robots" content="index,follow"'));
  assert(en.includes('href="https://mayconxzdev.github.io/en/"'));
  assert(en.includes('hreflang="pt-BR"'));
  assert(index.includes('hreflang="en" href="https://mayconxzdev.github.io/en/"'));
  for(const project of ["ArsenalMind Universal","Desapega AI","Belarc Inventory","Production Operations"])assert(en.includes(project),project);
  for(const r of data.resumes.filter(r=>r.lang==="en"))assert(en.includes("/assets/cv/"+r.file),r.id);
  assert(!en.includes("RAG/grounding")&&!en.includes("Maycon da Silva Ferreira"),"stale claims");
  assert(!en.includes("meta name=\"robots\" content=\"noindex"),"legacy noindex");
});
check("English entry navigation and image paths",()=>{
  const ids=new Set([...en.matchAll(/id="([^"]+)"/g)].map(m=>m[1]));
  const anchors=[...en.matchAll(/href="#([^"]+)"/g)].map(m=>m[1]);
  for(const id of anchors)assert(ids.has(id),"missing #"+id);
  for(const m of en.matchAll(/(?:href|src)="(\/assets\/[^"]+)"/g)){
    const local=m[1].replace(/^\//,"");
    assert(exists(local),"asset missing "+local);
  }
});
check("historical English cases remain isolated",()=>{
  assert(exists("en/cases/belarc-inventory/index.html"));
  assert(read("en/cases/belarc-inventory/index.html").includes("noindex"));
});
check("career case and interview descriptions consistent",()=>{
  assert(index.includes("ArsenalMind Universal"));
  assert(index.includes("Desapega AI"));
  assert(index.includes("Co-desenvolvi com Diogo Rodrigues"));
});
const dir=path.join(root,"evidence","career-v19");fs.mkdirSync(dir,{recursive:true});
const output={version:data.version,checks,issues:0,method:"Structural checks on build output. No claim of manual screen reader, real ATS or live MCP verification."};
fs.writeFileSync(path.join(dir,"checks.json"),JSON.stringify(output,null,2));
console.log(JSON.stringify(output));
