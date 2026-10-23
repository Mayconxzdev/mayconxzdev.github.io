import {cpSync,existsSync,mkdirSync,copyFileSync} from "node:fs";
import {resolve} from "node:path";
const root=resolve(import.meta.dirname,".."),parent=resolve(root,"..");
const target=resolve(root,"public");mkdirSync(target,{recursive:true});
const dirs=["assets","cases","css","js","en","competencias"];
for(const dir of dirs){const p=resolve(parent,dir);if(existsSync(p))cpSync(p,resolve(target,dir),{recursive:true,force:true})}
const fallback=resolve(parent,"assets","favicon.svg");
if(!existsSync(resolve(target,"favicon.svg"))&&existsSync(fallback))copyFileSync(fallback,resolve(target,"favicon.svg"));
console.log("Public assets prepared from already published portfolio, when repository root is present.");