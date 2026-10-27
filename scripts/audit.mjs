import {projects,cvList} from "../src/data.js";
import {existsSync,readFileSync} from "node:fs";
import {resolve} from "node:path";
import assert from "node:assert/strict";
const root=resolve(import.meta.dirname,"..");
assert(existsSync(resolve(root,"public/404.html")),"Custom 404 page must remain available after source normalization");
const missingPage=readFileSync(resolve(root,"public/404.html"),"utf8");
assert(missingPage.includes('href="/#acervo"')&&missingPage.includes('href="/assets/cv/"'),"404 recovery links must use absolute site paths");
const idset=new Set();
for(const project of projects){
 assert.match(project.slug,/^[a-z0-9-]+$/);
 assert(!idset.has(project.slug),"duplicate slug "+project.slug);idset.add(project.slug);
 for(const x of ["name","summary","headline","problem","solution","role","roleDetail","limitations","status"])assert(project[x]?.length>(x==="name"?2:9),project.slug+" missing "+x);
 assert(existsSync(resolve(root,"public","projetos",project.slug,"index.html")),project.slug+" no generated route");
 if(project.img)assert(existsSync(resolve(root,"public",project.img.slice(1))),project.slug+" missing image "+project.img);
}
const cvSeen=new Set();
for(const cv of cvList){
 assert(!cvSeen.has(cv.file));cvSeen.add(cv.file);
 assert(existsSync(resolve(root,"public","assets","cv",cv.file)),"resume missing "+cv.file);
}
const html=readFileSync(resolve(root,"index.html"),"utf8");
assert(html.includes('id="catalog-grid"')&&html.includes('id="curriculos"'));
assert(!html.includes('id="sim-next"'),"redundant home simulation should stay in project case");
assert(readFileSync(resolve(root,"public","projetos","producao-operacional","index.html"),"utf8").includes('id="demo-create"'),"illustrative interaction preserved in its case");
assert(!projects.some(p=>p.name==="VesperManutenção"),"old product duplicate");
assert(projects.find(p=>p.slug==="brasil-as-claras").status.includes("desenvolvimento"));
console.log(JSON.stringify({cases:projects.length,resumes:cvList.length,assertions:"passed",mediaIntegrityGate:true}));
