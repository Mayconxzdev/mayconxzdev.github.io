import {readFileSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {spawn,spawnSync} from 'node:child_process';

const root=resolve(import.meta.dirname,'..'),base='http://127.0.0.1:4214';
const expected=readFileSync(join(root,'dist/index.html'),'utf8');
let server;
const delay=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function running(){try{const response=await fetch(base+'/',{signal:AbortSignal.timeout(1500)});return response.ok?await response.text():null;}catch{return null;}}
try{
 let html=await running();
 if(html!==null&&html!==expected)throw Error('Port 4214 serves a different build. Close that preview before running tests.');
 if(html===null){
  server=spawn(process.execPath,[join(root,'node_modules/vite/bin/vite.js'),'preview','--host','127.0.0.1','--port','4214','--strictPort'],{cwd:root,stdio:'inherit'});
  for(let i=0;i<80;i++){await delay(250);html=await running();if(html!==null)break;}
  if(html!==expected)throw Error('Preview did not start with the expected dist/index.html.');
 }
 const scripts=['audit.mjs','audit-evidence.mjs','qa-v15.cjs','qa-v14.cjs','qa-v14-cases.cjs','qa-v14-handoffs.cjs','a11y-v14.cjs','qa-v14-cv.cjs','qa-motion-gallery-fix.cjs'];
 if(process.argv.includes('--full'))scripts.push('qa-mission.cjs','qa-motion-mission.cjs','qa-legacy-mission.cjs');
 for(const script of scripts){
  console.log('\nRunning '+script);
  const result=spawnSync(process.execPath,[join(root,'scripts',script)],{cwd:root,stdio:'inherit',timeout:900000});
  if(result.error)throw result.error;
  if(result.status!==0)throw Error(script+' failed with exit '+result.status);
 }
 console.log('\nPortfolio validation passed.');
}catch(error){console.error(error.message);process.exitCode=1;}
finally{if(server)server.kill();}
