import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const arg=process.argv.indexOf('--manifest');
const expected=JSON.parse(readFileSync(arg>=0?process.argv[arg+1]:'dist/build.json','utf8'));
const base='https://mayconxzdev.github.io';
const revision=process.env.GITHUB_SHA||expected.sourceRevision;
const delay=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function get(path){
 const url=base+'/'+path.split('/').map(encodeURIComponent).join('/')+'?release='+encodeURIComponent(revision);
 const response=await fetch(url,{headers:{'Cache-Control':'no-cache'},signal:AbortSignal.timeout(20000)});
 if(!response.ok)throw Error(path+': HTTP '+response.status);
 return Buffer.from(await response.arrayBuffer());
}
let ready=false;
for(let attempt=0;attempt<24;attempt++){
 try{if((await get('build.txt')).toString().trim()===revision){ready=true;break;}}catch{}
 await delay(10000);
}
if(!ready)throw Error('The expected commit is not live: '+revision);
const actual=JSON.parse((await get('build.json')).toString());
if(actual.sourceRevision!==revision||JSON.stringify(actual.files)!==JSON.stringify(expected.files))throw Error('Public build manifest differs from the tested artifact.');
const failures=[];let cursor=0;
async function worker(){
 while(cursor<expected.files.length){
  const file=expected.files[cursor++];let error;
  for(let attempt=0;attempt<3;attempt++){
   try{
    const bytes=await get(file.path);
    if(bytes.length!==file.bytes||createHash('sha256').update(bytes).digest('hex')!==file.sha256)throw Error('hash or length differs');
    error=null;break;
   }catch(failure){error=failure.message;await delay(1500);}
  }
  if(error)failures.push({path:file.path,error});
 }
}
await Promise.all(Array.from({length:6},worker));
if(failures.length){console.error(JSON.stringify(failures,null,2));process.exitCode=1;}
else console.log(JSON.stringify({sourceRevision:revision,filesVerified:expected.files.length,result:'LIVE_VERIFIED'},null,2));
