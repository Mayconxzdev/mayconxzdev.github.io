import {readFileSync,writeFileSync,readdirSync} from 'node:fs';
import {resolve,join,relative} from 'node:path';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';

const root=resolve(import.meta.dirname,'..'),dist=join(root,'dist');
let revision=process.env.GITHUB_SHA||'local';
if(revision==='local')try{revision=execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8',stdio:['ignore','pipe','ignore']}).trim();}catch{}
writeFileSync(join(dist,'build.txt'),revision+'\n');
const walk=dir=>readdirSync(dir,{withFileTypes:true}).flatMap(entry=>entry.isDirectory()?walk(join(dir,entry.name)):[join(dir,entry.name)]);
const files=walk(dist).filter(file=>relative(dist,file)!=='build.json').sort().map(file=>{
 const bytes=readFileSync(file);
 return {path:relative(dist,file).replaceAll('\\','/'),bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex')};
});
writeFileSync(join(dist,'build.json'),JSON.stringify({schemaVersion:1,sourceRevision:revision,files},null,2)+'\n');
console.log('Build manifest written: '+files.length+' files; source '+revision);
