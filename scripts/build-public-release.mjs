import fs from 'node:fs';import path from 'node:path';import {createHash} from 'node:crypto';import {execFileSync} from 'node:child_process';
const r=path.resolve(import.meta.dirname,'..'),source=path.join(r,'site-release'),dest=path.join(r,'dist');
const m=JSON.parse(fs.readFileSync(path.join(r,'scripts/public-release-manifest.json'),'utf8'));
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>{if(e.isSymbolicLink())throw Error('Symlink refused');return e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)]});
const entries=new Map(m.files.map(x=>[x.path,x]));const actual=walk(source);if(actual.length!==entries.size)throw Error('File count mismatch');
for(const f of actual){const key=path.relative(source,f).replaceAll('\\','/'),x=entries.get(key),b=fs.readFileSync(f);if(!x||x.bytes!==b.length||x.sha256!==createHash('sha256').update(b).digest('hex'))throw Error('Unreviewed artifact: '+key);if(/private-review|LOCAL-PREVIEW-ONLY|\.env(?:$|\.)/i.test(key))throw Error('Private asset: '+key)}
fs.rmSync(dest,{recursive:true,force:true});fs.cpSync(source,dest,{recursive:true});execFileSync(process.execPath,['scripts/write-build-info.mjs'],{cwd:r,stdio:'inherit'});console.log('Release validated:',actual.length,'files; 6 role-specific resumes.');
