import {existsSync,mkdirSync,copyFileSync,readdirSync,unlinkSync,readFileSync,writeFileSync} from "node:fs";
import {resolve,join} from "node:path";
const root=resolve(import.meta.dirname,"..");
const target=resolve(root,"public");mkdirSync(target,{recursive:true});
// public/ is the versioned source of static assets; the build never reads a parent workspace.
// Keep only four current CV PDFs (2 PT + 2 EN) in public media.
const cvData=JSON.parse(readFileSync(resolve(root,"scripts","resumes-content.json"),"utf8"));
const allowed=new Set(cvData.resumes.map(x=>x.file));
if(allowed.size!==4)throw new Error("CV release requires four distinct PDFs");
const cvDir=resolve(target,"assets","cv");
for(const name of readdirSync(cvDir)){
 if(name.toLowerCase().endsWith(".pdf")&&!allowed.has(name))unlinkSync(resolve(cvDir,name));
}
for(const name of allowed)if(!existsSync(resolve(cvDir,name)))throw new Error("Missing selected CV "+name);
// Keep one four-item canonical catalog while serving old direct PDF URLs as
// byte-identical aliases to the closest matching current version.
const aliasTargets={
 "Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf":"pt_sw",
 "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf":"pt_ai",
 "Maycon_Ferreira_IA_Agentes_MCP.pdf":"pt_ai",
 "Maycon_Ferreira_Automacao_Integracoes.pdf":"pt_sw",
 "Maycon_Ferreira_Dados_BI.pdf":"pt_sw",
 "Maycon_Ferreira_Sistemas_Backend.pdf":"pt_sw",
 "Maycon_Ferreira_Web_Produtos_Digitais.pdf":"pt_sw",
 "Maycon_Ferreira_Conteudo_Video_IA.pdf":"pt_sw",
 "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf":"en_ai",
 "Maycon_Ferreira_Geral_Automacao_IA_PT.pdf":"pt_sw",
 "Maycon_Ferreira_Agentes_Automacao_n8n_PT.pdf":"pt_ai",
 "Maycon_Ferreira_Produtos_Conteudo_IA_PT.pdf":"pt_sw",
 "Maycon_Ferreira_General_Automation_AI_EN.pdf":"en_sw",
 "Maycon_Ferreira_AI_Agents_Automation_n8n_EN.pdf":"en_ai",
 "Maycon_Ferreira_AI_Digital_Products_Content_EN.pdf":"en_sw"
};
const byId=new Map(cvData.resumes.map(x=>[x.id,x.file]));
for(const [alias,id] of Object.entries(aliasTargets)){
 const canonical=byId.get(id);
 if(!canonical)throw new Error(`No canonical resume mapped for legacy alias ${alias}: ${id}`);
 copyFileSync(resolve(cvDir,canonical),resolve(cvDir,alias));
}
const aliasNames=Object.keys(aliasTargets);
function fixLegacy(dir,underEnglish=false){
 for(const item of readdirSync(dir,{withFileTypes:true})){
  const file=join(dir,item.name);
  if(item.isDirectory()){fixLegacy(file,underEnglish||item.name==="en");continue}
  if(!item.isFile()||!item.name.endsWith(".html"))continue;
  let html=readFileSync(file,"utf8"),updated=html;
  for(const filename of aliasNames){
    // Archived pages point to their semantically closest canonical version.
    // Direct legacy URLs remain functional through byte-identical PDF aliases.
    const id=aliasTargets[filename],canonical=byId.get(id);
    updated=updated.split("/assets/cv/"+filename).join("/assets/cv/"+canonical);
    updated=updated.split("../assets/cv/"+filename).join("../assets/cv/"+canonical);
  }
  if(updated!==html)writeFileSync(file,updated,"utf8");
 }
}
fixLegacy(target);
console.log(`Public assets prepared: ${allowed.size} canonical CVs and ${Object.keys(aliasTargets).length} byte-identical legacy aliases.`);
