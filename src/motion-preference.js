const KEY="lv-motion-mode";
const LEGACY_KEY="lv-motion";
const modes=new Set(["auto","motion","direct"]);
const systemPreference=matchMedia("(prefers-reduced-motion: reduce)");
let sessionMode=null;

export function getMotionMode(){
 if(modes.has(sessionMode))return sessionMode;
 try{
  const saved=localStorage.getItem(KEY);
  if(modes.has(saved))return saved;
  const legacy=localStorage.getItem(LEGACY_KEY);
  if(legacy==="direct"||legacy==="motion"){
   try{localStorage.setItem(KEY,legacy);localStorage.removeItem(LEGACY_KEY)}catch{}
   return legacy;
  }
 }catch{}
 const pageMode=document.documentElement.dataset.motionMode;
 return modes.has(pageMode)?pageMode:"auto";
}

export function isDirectMotion(){
 const mode=getMotionMode();
 return mode==="direct"||(mode==="auto"&&systemPreference.matches);
}

function syncMotionMode(announce=false){
 const mode=getMotionMode();
 const direct=mode==="direct"||(mode==="auto"&&systemPreference.matches);
 const root=document.documentElement;
 root.dataset.motionMode=mode;
 root.dataset.motionEffective=direct?"direct":"animated";
 root.classList.toggle("v11-direct",direct);
 if(announce)document.dispatchEvent(new CustomEvent("lv-motion-change",{detail:{mode,effective:direct?"direct":"animated"}}));
 return {mode,direct};
}

export function setMotionMode(mode){
 if(!modes.has(mode))return syncMotionMode();
 sessionMode=mode;
 try{
  localStorage.setItem(KEY,mode);
  localStorage.removeItem(LEGACY_KEY);
 }catch{}
 return syncMotionMode(true);
}

syncMotionMode();
systemPreference.addEventListener("change",()=>syncMotionMode(true));
