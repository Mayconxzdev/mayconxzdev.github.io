import {getMotionMode,setMotionMode} from "./motion-preference.js";

export function initVisitorExperience({cvList,updateMethod}){
 const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
 const modeControl=$("#motion-mode"),modeStatus=$("#motion-mode-status");
 const explainMode=()=>{
  const mode=getMotionMode(),reduced=matchMedia("(prefers-reduced-motion: reduce)").matches;
  if(modeControl){
   modeControl.value=mode;
   modeControl.title=mode==="auto"&&reduced
    ?"Automático: o dispositivo solicita movimento reduzido. Escolha Animação para ativar os efeitos."
    :mode==="motion"&&reduced
     ?"Animação ativada por escolha explícita; o dispositivo solicita movimento reduzido."
     :"Modo de movimento: "+({auto:"Automático",motion:"Animação",direct:"Leitura direta"}[mode])+".";
  }
 };
 explainMode();
 modeControl?.addEventListener("change",()=>{
  const {mode,direct}=setMotionMode(modeControl.value);
  explainMode();
  if(modeStatus)modeStatus.textContent=direct
   ?(mode==="auto"?"Leitura direta: preferência do dispositivo.":"Leitura direta ativada.")
   :(mode==="motion"?"Animação ativada.":"Animação automática ativada.");
 });
 matchMedia("(prefers-reduced-motion: reduce)").addEventListener("change",explainMode);
 // Subject-specific discovery shortcuts: they never conceal other projects permanently.
 $$("[data-discover]").forEach(button=>button.addEventListener("click",()=>{
  const filter=$('[data-filter="'+button.dataset.discover+'"]');
  if(filter){filter.click();$("#project-search")?.focus({preventScroll:true})}
  $$("[data-discover]").forEach(b=>b.classList.toggle("is-active",b===button));
 }));
 // The Portuguese portfolio has exactly three Portuguese resumes.
 // English translations are presented only on /en/resumes/.
 const cards=$$("#cv-grid .cv-card");
 cards.forEach((card,i)=>card.dataset.cvId=cvList[i]?.id||"");
 // Method examples reflect documented cases; no invented before/after or deployment metrics.
 const examples=[
  ["producao-operacional","Produção: da rotina aos requisitos"],
  ["manutencao-em-campo","Campo: organizar a inspeção"],
  ["belarc-inventory","Belarc: inventário e atendimento"],
  ["producao-operacional","Produção: testar regras e exceções"],
  ["zero21fotos","ZERO21: entregar e manter um site"]
 ];
 const methodLink=$("#v11-method-evidence");
 if(methodLink){
  const refresh=()=>{
   const ix=Math.max(0,$$("[data-method]").findIndex(b=>b.getAttribute("aria-selected")==="true"));
   methodLink.href="/projetos/"+examples[ix][0]+"/";
   methodLink.textContent=examples[ix][1]+" ↗";
  };
  $$("[data-method]").forEach(b=>b.addEventListener("click",refresh));
  const tabs=$("#method-panel")?.parentNode;
  tabs?.addEventListener("keyup",refresh);
  refresh();
 }
 // Asset disclosure attached to each screenshot is explicit and never represents live behavior.
 const facts=$$(".v11-screen-proof");
 facts.forEach(el=>{
  el.title="Descrição editorial baseada na captura do projeto. A imagem original pode ser ampliada.";
 });
}
