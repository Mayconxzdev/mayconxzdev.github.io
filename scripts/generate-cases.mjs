import {projects,cvList} from "../src/data.js";
import {renderDemo} from "./demo-sections.mjs";
import {renderGallery} from "./evidence-render.mjs";
import {evidenceList,evidenceIdFor} from "./evidence-map.mjs";
import {getEditorial,renderCredit} from "./v13-case-components.mjs";
import {renderV14Visual,renderV14Nav,getV14Mode} from "./v14-scenes.mjs";
import {readFileSync,writeFileSync,mkdirSync,copyFileSync} from "node:fs";
import {join,resolve} from "node:path";
const root=resolve(import.meta.dirname,"..");
const template=readFileSync(join(root,"templates","case.html"),"utf8");
const esc=(s)=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
// Real links exist before the module loads, including when JavaScript is unavailable.
const homeFile=join(root,"index.html");
let home=readFileSync(homeFile,"utf8");
const fallbackProjects=projects.map(p=>'<a class="v15-static-project" href="/projetos/'+esc(p.slug)+'/">'+
 '<strong>'+esc(p.name)+'</strong><span>'+esc(getEditorial(p).lead)+'</span><small>'+esc(getEditorial(p).status)+' ↗</small></a>').join("");
const fallbackCV=cvList.map(cv=>'<a class="cv-card" href="/assets/cv/'+encodeURIComponent(cv.file)+'" target="_blank" rel="noopener"><strong>'+esc(cv.title)+'</strong><span>Visualizar PDF ↗</span></a>').join("");
home=home.replace(/<div id="catalog-grid" class="catalog-grid">[\s\S]*?<\/div>(?:<!-- static-projects -->)?/, '<div id="catalog-grid" class="catalog-grid">'+fallbackProjects+'</div><!-- static-projects -->');
home=home.replace(/<div id="cv-grid" class="cv-grid">[\s\S]*?<\/div>(?:<!-- static-cv -->)?/, '<div id="cv-grid" class="cv-grid">'+fallbackCV+'</div><!-- static-cv -->');
// Initial HTML and enhanced scenes share a single source, including reordered views.
const scenes=JSON.parse(readFileSync(join(root,"src","v8-story.json"),"utf8"));
let sceneIndex=0;
home=home.replace(/<article class="world-slide"[\s\S]*?<\/article>/g,html=>{
 const scene=scenes[sceneIndex++],view=scene.states[0];
 return html.replace(/(<h3 id="world-heading-\d+">)[\s\S]*?<\/h3>/,'$1'+esc(view[6].title)+'</h3>')
  .replace(/(<p class="world-desc-context">)[\s\S]*?<\/p>/,'$1'+esc(view[6].context)+'</p>')
  .replace(/(<div class="world-actions-head"><span>)[\s\S]*?<\/span>/,'$1'+esc(scene.routeLabel)+'</span>')
  .replace(/(<a class="world-case-link" href=")[^"]+("[^>]*>)/,'$1/projetos/'+esc(scene.key)+'/#media-'+esc(evidenceIdFor(scene.key,view[2]))+'$2')
  .replace(/<span class="world-page-label">[\s\S]*?<\/span>/,'<span class="world-page-label">01 / '+String(scene.states.length).padStart(2,'0')+'</span>')
  .replace(/(<div class="world-tabs"[^>]*>)[\s\S]*?<\/div>/,'$1'+scene.states.map((s,i)=>'<button type="button" class="world-tab'+(i===0?' is-selected':'')+'" data-view="'+i+'" data-evidence-id="'+esc(evidenceIdFor(scene.key,s[2]))+'" aria-pressed="'+(i===0)+'"><img class="world-tab-thumb" src="'+esc(s[2])+'" alt="" loading="lazy"><span class="world-tab-label">'+esc(s[0])+'</span></button>').join('')+'</div>');
});
if(sceneIndex!==scenes.length)throw Error('Home scene markup and manifest differ');
writeFileSync(homeFile,home,"utf8");
const allowedLink=(url)=>{try{const u=new URL(url);return u.protocol==="https:"?u.href:""}catch{return ""}};
writeFileSync(join(root,"public","lab.css"),readFileSync(join(root,"src","style.css"),"utf8")+"\n"+readFileSync(join(root,"src","editorial-v2.css"),"utf8")+"\n"+readFileSync(join(root,"src","lab-v3.css"),"utf8"));
for(const p of projects){
 const entry=getEditorial(p);
 if(!entry)throw new Error("Missing per-project editorial: "+p.slug);
 const fields={
  TITLE:p.name,SUMMARY:entry.lead,GROUP:p.group,HEADLINE:entry.title,STACK:p.stack.join(" · "),MODE:getV14Mode(p.slug),
  STATUS:entry.status,ROLE:entry.role,TYPE:entry.type,KIND:p.kind,
  ROBOTS:'<meta name="robots" content="'+(entry.priority==='archive'?'noindex,nofollow':'index,follow')+'"><link rel="canonical" href="https://mayconxzdev.github.io/projetos/'+esc(p.slug)+'/"><meta property="og:url" content="https://mayconxzdev.github.io/projetos/'+esc(p.slug)+'/">',
  NAV:renderV14Nav(p),VISUAL:renderV14Visual(p),STORY:"",
  CREDIT:renderCredit(p),EXPERIENCE:renderDemo(p.slug)
 };
 let html=template;
 for(const [key,value] of Object.entries(fields)) html=html.replaceAll("{{"+key+"}}",["NAV","VISUAL","STORY","CREDIT","ROBOTS","EXPERIENCE"].includes(key)?value:esc(value));
 const out=join(root,"public","projetos",p.slug);mkdirSync(out,{recursive:true});writeFileSync(join(out,"index.html"),html,"utf8");
}
const sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+['/','/projetos/'].concat(projects.filter(p=>getEditorial(p).priority!=='archive').map(p=>'/projetos/'+p.slug+'/')).filter(x=>x!=='/projetos/').map(path=>' <url><loc>https://mayconxzdev.github.io'+path+'</loc></url>').join("\n")+'\n</urlset>\n';
writeFileSync(join(root,"public","sitemap.xml"),sitemap);
writeFileSync(join(root,"public","robots.txt"),"User-agent: *\nAllow: /\nDisallow: /cases/\nDisallow: /en/\nDisallow: /competencias/\nSitemap: https://mayconxzdev.github.io/sitemap.xml\n");
console.log(JSON.stringify({generatedCases:projects.length,publicAssets:"versioned public assets",cvFiles:"six canonical files plus legacy aliases",status:"production build; deployment verified separately"}));
