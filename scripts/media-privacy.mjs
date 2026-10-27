import {existsSync,readFileSync,writeFileSync,mkdirSync,readdirSync,renameSync,unlinkSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {createHash} from 'node:crypto';
const root=resolve(import.meta.dirname,'..');
const media=join(root,'public/assets/evidence');
const quarantine=join(root,'private-review/legacy-media');
mkdirSync(quarantine,{recursive:true});
const aws=['compass-runs','compass-athena-data','compass-s3'];
const pending=['portal-approvals','portal-dashboard','portal-helpdesk','portal-kanban','portal-koda','portal-purchases'];
const digest=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
for(const name of [...aws,...pending]){
 const source=join(media,name+'.webp'),target=join(quarantine,name+'.webp');
 if(!existsSync(source))continue;
 if(existsSync(target)){
  if(digest(source)!==digest(target))throw new Error('Quarantine collision: '+name);
  unlinkSync(source);
 }else renameSync(source,target);
}
const walk=dir=>existsSync(dir)?readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(join(dir,e.name)):e.name.endsWith('.html')?[join(dir,e.name)]:[]):[];
for(const file of ['cases','en','competencias'].flatMap(dir=>walk(join(root,'public',dir)))){
 let html=readFileSync(file,'utf8');
 for(const name of aws)html=html.replaceAll(name+'.webp',name+'-sanitized.webp');
 for(const name of pending){
  const image=new RegExp('<img\\b[^>]*\\bsrc="[^"]*'+name+'\\.webp"[^>]*>','g');
  const english=file.includes('\\en\\')||file.includes('/en/');
  const note=english?'Historical screenshot withheld for privacy review. The original remains in the local archive.':'Captura histórica reservada para revisão de privacidade. O original está preservado no acervo local.';
  html=html.replace(image,'<p class="privacy-review-note" role="note">'+note+'</p>');
 }
 html=html.replaceAll('href="/#overview"','href="/#inicio"').replaceAll('href="/#systems"','href="/#acervo"').replaceAll('href="/#experience"','href="/#sobre"').replaceAll('href="/#evidence"','href="/#acervo"').replaceAll('href="/#contact"','href="/#contato"');
 if(html.includes('</header>')&&!html.includes('legacy-review-banner')){
  const english=file.includes('\\en\\')||file.includes('/en/');
  const label=english?'Historical archive · earlier portfolio documents.':'Acervo anterior · documentos históricos do portfólio.';
  const action=english?'View current work ↗':'Ver trabalhos atuais ↗';
  html=html.replace('</header>','</header><aside class="legacy-review-banner">'+label+' <a href="/#acervo">'+action+'</a></aside>');
 }
 if(!html.includes('name="robots"'))html=html.replace('</head>','<meta name="robots" content="noindex,nofollow"></head>');
 writeFileSync(file,html);
}
console.log('Privacy policy: 3 AWS session originals and 6 historical Portal captures preserved outside public; active case media unchanged.');
