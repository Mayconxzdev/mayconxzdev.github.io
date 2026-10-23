import {projects} from "../src/data.js";
import {readFileSync,writeFileSync,mkdirSync,copyFileSync} from "node:fs";
import {join,resolve} from "node:path";
const root=resolve(import.meta.dirname,"..");
const template=readFileSync(join(root,"templates","case.html"),"utf8");
const esc=(s)=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const allowedLink=(url)=>{try{const u=new URL(url);return u.protocol==="https:"?u.href:""}catch{return ""}};
copyFileSync(join(root,"src","style.css"),join(root,"public","lab.css"));
for(const p of projects){
 const parts=(p.decisions||[]).map((line,i)=>'<article class="decision"><span>'+String(i+1).padStart(2,"0")+' / 03</span><p>'+esc(line)+'</p></article>').join("");
 const img=p.img ? '<figure><img src="'+esc(p.img)+'" alt="'+esc(p.imageLabel)+'" loading="lazy" width="1200" height="750"><figcaption>'+esc(p.imageLabel)+'</figcaption></figure>' : '<figure><div class="case-abstract" aria-label="Representação abstrata editorial, não captura do software"><strong>'+esc(p.name.split(" ")[0])+'</strong></div><figcaption>'+esc(p.imageLabel)+'</figcaption></figure>';
 const links=[["Repositório público",p.repository],["Produto / site externo",p.website],["Case anterior preservado",p.legacy]].filter(([,href])=>href&&(href.startsWith("/")||allowedLink(href))).map(([label,url])=>'<a href="'+esc(url)+'" '+(url.startsWith("/")?"":'target="_blank" rel="noopener noreferrer"')+'>'+esc(label)+' ↗</a>').join("");
 const fields={
  TITLE:p.name,SUMMARY:p.summary,GROUP:p.group,HEADLINE:p.headline,STATUS:p.status,ROLE:p.role,PROBLEM:p.problem,SOLUTION:p.solution,DECISIONS:parts,
  SHOWCASE:img,ROLE_DETAIL:p.roleDetail,LIMITATIONS:p.limitations,STACK:p.stack.join(" · "),LINKS:'<div class="case-links">'+links+'</div>'
 };
 let html=template;
 for(const [key,value] of Object.entries(fields)) html=html.replaceAll("{{"+key+"}}",["DECISIONS","SHOWCASE","LINKS"].includes(key)?value:esc(value));
 const out=join(root,"public","projetos",p.slug);mkdirSync(out,{recursive:true});writeFileSync(join(out,"index.html"),html,"utf8");
}
const sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+['/','/projetos/'].concat(projects.map(p=>'/projetos/'+p.slug+'/')).filter(x=>x!=='/projetos/').map(path=>' <url><loc>https://mayconxzdev.github.io'+path+'</loc></url>').join("\n")+'\n</urlset>\n';
writeFileSync(join(root,"public","sitemap.xml"),sitemap);
writeFileSync(join(root,"public","robots.txt"),"User-agent: *\nAllow: /\nSitemap: https://mayconxzdev.github.io/sitemap.xml\n");
console.log(JSON.stringify({generatedCases:projects.length,publicAssets:"historical public-only",cvFiles:"preserved from public repository",status:"candidate/staging; not released"}));