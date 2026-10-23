import {projects,cvList} from "../src/data.js";
import {existsSync,readFileSync} from "node:fs";
import {resolve} from "node:path";
import assert from "node:assert/strict";
const root=resolve(import.meta.dirname,"..");
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
assert(html.includes('id="catalog-grid"')&&html.includes('id="sim-next"')&&html.includes('id="curriculos"'));
assert(!projects.some(p=>p.name==="VesperManutenção"),"old product duplicate");
assert(projects.find(p=>p.slug==="brasil-as-claras").status.includes("desenvolvimento"));
console.log(JSON.stringify({cases:projects.length,resumes:cvList.length,assertions:"passed",release:false}));