import {existsSync,readdirSync,readFileSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {createHash} from 'node:crypto';
const root=resolve(import.meta.dirname,'..');
const pendingDir=join(root,'public/assets/v13-local-review');
const pending=existsSync(pendingDir)?readdirSync(pendingDir):[];
if(pending.length)throw Error('RELEASE BLOCKED: '+pending.length+' pending audit-package images.');
const manifest=JSON.parse(readFileSync(join(root,'scripts/public-media-approvals.json'),'utf8'));
if(manifest.items.length!==2)throw Error('RELEASE BLOCKED: approval manifest incomplete.');
for(const media of manifest.items){
 const path=join(root,'public',media.path);
 if(!existsSync(path))throw Error('RELEASE BLOCKED: missing approved image '+media.path);
 const hash=createHash('sha256').update(readFileSync(path)).digest('hex');
 if(hash!==media.sha256)throw Error('RELEASE BLOCKED: changed image '+media.path);
}
const evidence=readFileSync(join(root,'scripts/evidence-map.mjs'),'utf8');
if(evidence.includes('/assets/v13-local-review/'))throw Error('RELEASE BLOCKED: old stage reference remains.');
console.log('Approved screenshot hashes verified; technical integrity checks PASS.');
const inventory=JSON.parse(readFileSync(join(root,'scripts/media-release-inventory.json'),'utf8'));
const mediaExtensions=/\.(png|jpe?g|webp|avif|gif|svg)$/i;
const walk=dir=>readdirSync(dir,{withFileTypes:true}).flatMap(entry=>entry.isDirectory()?walk(join(dir,entry.name)):[join(dir,entry.name)]);
const current=walk(join(root,'public')).filter(file=>mediaExtensions.test(file));
if(current.length!==inventory.items.length)throw Error('RELEASE BLOCKED: media inventory changed; review the added or removed files.');
for(const item of inventory.items){
 const path=join(root,'public',item.path);
 if(!existsSync(path)||createHash('sha256').update(readFileSync(path)).digest('hex')!==item.sha256)throw Error('RELEASE BLOCKED: media differs from reviewed inventory: '+item.path);
}
console.log('Reviewed media inventory verified: '+inventory.items.length+' files.');
const rights=JSON.parse(readFileSync(join(root,'scripts/publication-rights-review.json'),'utf8'));
const unresolved=rights.items.filter(item=>item.status!=='cleared');
if(rights.status!=='cleared'||unresolved.length){
 console.error(`RELEASE BLOCKED: ${unresolved.length} rights/privacy review items remain unresolved.`);
 for(const item of unresolved)console.error(`- ${item.id}: ${item.summary}`);
 console.error('Do not publish from this workspace until each item is reviewed and the local review register is updated with file-level evidence.');
 process.exitCode=1;
}else console.log('Publication rights/privacy review: CLEAR.');
