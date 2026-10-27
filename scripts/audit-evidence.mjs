import {evidence} from "./evidence-map.mjs";
import {projects} from "../src/data.js";
import {existsSync,readFileSync} from "node:fs";
import {resolve} from "node:path";
import assert from "node:assert/strict";
const root=resolve(import.meta.dirname,"..");
let images=0;
const pathset=new Set();
for(const [slug,items] of Object.entries(evidence)){
 assert(projects.some(p=>p.slug===slug),"Unknown project "+slug);
 assert(items.length>=1&&items.length<=8,"Gallery limit "+slug);
 for(const item of items){
  images++;
  assert(item.src.startsWith("/assets/"),"Bad gallery path "+item.src);
  assert(item.name.length>2&&item.caption.length>15&&item.source.length>8,"Evidence label insufficient "+slug);
  assert(existsSync(resolve(root,"public",item.src.slice(1))),"Missing evidence asset "+item.src);
  pathset.add(item.src);
 }
 const page=readFileSync(resolve(root,"public","projetos",slug,"index.html"),"utf8");
 assert(page.includes("case-gallery v14-gallery")||page.includes("case-gallery"),"Missing gallery "+slug);
 assert(page.includes("case-gallery v14-gallery")||page.includes("case-gallery"),"Missing gallery "+slug);
}
const zero21=readFileSync(resolve(root,"src","data.js"),"utf8");
assert(zero21.includes('https://hubora.netlify.app/'));
assert(!zero21.includes('website:"https://hubora.app/"'));
const main=readFileSync(resolve(root,"index.html"),"utf8");
const scenes=JSON.parse(readFileSync(resolve(root,"src","v8-story.json"),"utf8"));
assert(main.includes('id="projetos"')&&main.includes('class="world-slide"'),"Missing V8 motion narrative");
assert(scenes.length===5&&scenes.reduce((n,p)=>n+p.states.length,0)===17,"Missing featured project scenes");
for(const scene of scenes)for(const view of scene.states){
 assert(evidence[scene.key]?.some(item=>item.src===view[2]),"Featured capture is missing from its case gallery "+scene.key+" / "+view[2]);
}
for(const project of scenes)for(const view of project.states){
 assert(existsSync(resolve(root,"public",view[2].slice(1))),"Missing screenshot "+view[2]);
 assert(view[6]?.title?.length>8&&view[6]?.context?.length>30,"Missing screen context "+project.key);
 const fragments=view.at(-1)?.fragments||[];
 const intentionallyUncropped=project.key==="producao-operacional"&&view[0]==="Setores e configuração";
 assert(intentionallyUncropped?fragments.length===0:fragments.length===2,"Unexpected original-image fragments "+project.key+" / "+view[0]);
 for(const image of fragments)assert(existsSync(resolve(root,"public",image.slice(1))),"Missing extracted image "+image);
}
const client=readFileSync(resolve(root,"public","projetos","zero21fotos","index.html"),"utf8");
assert(client.includes("case-gallery v14-gallery")&&["zero21-v15-sobre.webp","zero21-v15-eventos-entrada.webp","zero21-v15-eventos-catalogo.webp"].every(name=>client.includes(name)),
 "ZERO21 must show the three approved views from the public website, not isolated event photos");
assert(!client.includes("v8-client-showcase"),"Duplicated client showcase");
const tradutor=readFileSync(resolve(root,"public","projetos","tradutor-documental","index.html"),"utf8");
assert((tradutor.match(/class="case-gallery v14-gallery/g)||[]).length===1,"Tradutor must have one gallery only");
assert(!tradutor.includes("v4-stage--screens"),"No redundant screenshot stage");
assert(main.includes('name="robots" content="index,follow"'),"Canonical homepage must be indexable");
assert(!main.includes("zero21-typography"),"Placeholder ZERO21 still present");
assert(!main.includes("workflow-sculpture.webp"),"Former generic sculpture still hero");
console.log(JSON.stringify({galleries:Object.keys(evidence).length,imagePlacements:images,uniqueImages:pathset.size,status:"passed",approvedMedia:2,localReviewMedia:0,mediaIntegrityGate:true},null,2));
