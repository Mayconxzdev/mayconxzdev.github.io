import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);
import scenes from "./fullscreen-scenes.json";

/* Fullscreen editorial: native scroll selects projects; only a click changes the view.
 * Static HTML already contains the first view of every project (no-JS fallback).
 */
export function initFullscreenScenes(){
 const section=document.querySelector(".fullscreen-film");
 if(!section)return;
 const cases=[...section.querySelectorAll(".film-project")];
 const shortcuts=[...section.querySelectorAll(".film-shortcuts a")];
 const reduce=window.matchMedia("(prefers-reduced-motion: reduce)");
 if(cases.length!==scenes.length)throw new Error("Fullscreen narrative and evidence manifest differ");
 const requestTokens=new Array(cases.length).fill(0);
 const currentViews=new Array(cases.length).fill(0);
 let active=-1,scheduled=0;

 const getFile=(state)=>state[2];
 const loadImage=(src)=>new Promise(resolve=>{
  const img=new Image();
  img.decoding="async";
  img.onload=()=>resolve(true);
  img.onerror=()=>resolve(false);
  img.src=src;
  if(img.complete)resolve(img.naturalWidth>0);
 });

 async function chooseView(i,index,announce=true){
  const project=scenes[i],stage=cases[i];
  if(!project||!stage||!project.states[index])return;
  const same=currentViews[i]===index;
  if(same&&announce)return;
  const token=++requestTokens[i];
  const state=project.states[index];
  const src=getFile(state);
  const mobile=state[5]||src;
  const visibleSrc=window.matchMedia("(max-width: 700px)").matches?mobile:src;
  const ready=await loadImage(visibleSrc);
  if(token!==requestTokens[i])return;
  if(!ready){stage.querySelector(".film-sr-status").textContent="Não foi possível carregar a imagem selecionada.";return}
  currentViews[i]=index;
  const image=stage.querySelector(".film-screen");
  const oldAnimations=image.getAnimations();
  oldAnimations.forEach(animation=>animation.cancel());
  const responsiveSource=stage.querySelector(".film-mobile-source");
  if(responsiveSource)responsiveSource.srcset=mobile;
  image.src=src;
  image.alt=state[3];
  if(state[4]){
   image.width=state[4].width;
   image.height=state[4].height;
  }
  stage.querySelector(".film-atmosphere").style.backgroundImage="url('"+visibleSrc+"')";
  const story=state[6]||{};
  stage.querySelector(".film-about h3").textContent=story.title||state[1];
  stage.querySelector("[data-description]").textContent=story.context||state[3];
  stage.querySelector(".film-view-count").textContent=String(index+1).padStart(2,"0")+" / "+String(project.states.length).padStart(2,"0");
  stage.querySelectorAll(".film-view").forEach((b,j)=>{
   const selected=j===index;
   b.classList.toggle("is-selected",selected);
   b.setAttribute("aria-pressed",String(selected));
  });
  if(announce){
   stage.querySelector(".film-sr-status").textContent="Agora: "+state[0]+". "+state[3];
  }
  if(!reduce.matches&&announce){
   const entrances=[
    [{opacity:.4,transform:"translateX(28px)"},{opacity:1,transform:"translateX(0)"}],
    [{opacity:.4,transform:"translateY(22px)"},{opacity:1,transform:"translateY(0)"}],
    [{opacity:.4,clipPath:"inset(0 70% 0 0)"},{opacity:1,clipPath:"inset(0)"}],
    [{opacity:.4,transform:"scale(1.02)"},{opacity:1,transform:"scale(1)"}],
    [{opacity:.4,transform:"translateX(-24px)"},{opacity:1,transform:"translateX(0)"}]
   ];
   image.animate(entrances[i],{duration:260,easing:"cubic-bezier(.2,.8,.2,1)"});
  }
 }
 cases.forEach((stage,i)=>{
  stage.querySelectorAll(".film-view").forEach(button=>{
   button.addEventListener("click",()=>chooseView(i,Number(button.dataset.view)));
   button.addEventListener("keydown",e=>{
    if(e.key!=="ArrowRight"&&e.key!=="ArrowLeft")return;
    e.preventDefault();
    const buttons=[...stage.querySelectorAll(".film-view")];
    const idx=buttons.indexOf(button);
    const next=buttons[(idx+(e.key==="ArrowRight"?1:-1)+buttons.length)%buttons.length];
    next.focus();
    chooseView(i,Number(next.dataset.view));
   });
  });
 });

 const clamp=(v)=>Math.max(0,Math.min(1,v));
 const arrived=cases.map(()=>1),leaving=cases.map(()=>0);
 function updateCaptionBlend(i){
  const entrance=Math.max(0,Math.min(1,(arrived[i]-.35)/.50));
  const departure=1-leaving[i]*.6;
  cases[i].querySelector(".film-stage").style.setProperty("--film-caption-alpha",(entrance*departure).toFixed(3));
 }
 const enterDirs=[
  {x:100,y:0,clip:"left"},
  {x:0,y:80,clip:"top"},
  {x:-90,y:0,clip:"left"},
  {x:50,y:20,clip:"diagonal"},
  {x:-85,y:0,clip:"right"}
 ];
 function entrance(i,progress){
  const p=clamp(progress);
  arrived[i]=p;
  updateCaptionBlend(i);
  const stage=cases[i].querySelector(".film-stage");
  const dir=enterDirs[i];
  const q=1-p;
  stage.style.setProperty("--film-motion-x",(dir.x*q).toFixed(1)+"px");
  stage.style.setProperty("--film-motion-y",(dir.y*q).toFixed(1)+"px");
  stage.style.setProperty("--film-motion-scale",(1+.035*q).toFixed(4));
  stage.style.setProperty("--film-panel-shift",(18*q).toFixed(1)+"px");
  // The reveal is proportional to scroll. Both project scenes remain partially visible
  // during a handoff, including when scrolling stops halfway.
  if(dir.clip==="left")stage.style.clipPath="inset(0 0 0 "+(q*24).toFixed(2)+"%)";
  else if(dir.clip==="right")stage.style.clipPath="inset(0 "+(q*24).toFixed(2)+"% 0 0)";
  else if(dir.clip==="top")stage.style.clipPath="inset("+(q*20).toFixed(2)+"% 0 0 0)";
  else stage.style.clipPath="polygon(0 0,"+(100-q*24).toFixed(2)+"% 0,100% 100%,0 100%)";
  stage.style.opacity=(.82+.18*p).toFixed(3);
 }
 function departure(i,progress){
  const p=clamp(progress),stage=cases[i].querySelector(".film-stage");
  leaving[i]=p;
  updateCaptionBlend(i);
  stage.style.setProperty("--film-depart-y",(-p*35).toFixed(1)+"px");
  stage.style.setProperty("--film-depart-scale",(1+p*.014).toFixed(4));
  stage.style.setProperty("--film-panel-exit",(-p*13).toFixed(1)+"px");
  // The previous frame gently dims as it moves out. No snap at project boundaries.
  stage.style.filter="brightness("+(1-.12*p).toFixed(3)+")";
 }
 if(!reduce.matches){
  document.documentElement.classList.add("film-motion");
  cases.forEach((c,i)=>{
   const enter=ScrollTrigger.create({
    trigger:c,start:"top bottom",end:"top top",invalidateOnRefresh:true,
    onUpdate:self=>entrance(i,self.progress),
    onLeave:()=>entrance(i,1),onLeaveBack:()=>entrance(i,0)
   });
   const exit=ScrollTrigger.create({
    trigger:c,start:"bottom bottom",end:"bottom top",invalidateOnRefresh:true,
    onUpdate:self=>departure(i,self.progress),
    onLeave:()=>departure(i,1),onLeaveBack:()=>departure(i,0)
   });
   // The two partial frames are physically present in their respective sections.
   entrance(i,enter.progress);
   departure(i,exit.progress);
  });
 }
 // The capture viewer is shared by all five cases and does not navigate away.
 const viewer=section.querySelector("#film-capture-dialog");
 const viewerImage=section.querySelector("#film-capture-image");
 const viewerTitle=section.querySelector("#film-capture-title");
 const zoomControl=section.querySelector("#film-capture-zoom");
 let opener=null;
 cases.forEach((film,i)=>{
  film.querySelector(".film-open-capture").addEventListener("click",e=>{
   opener=e.currentTarget;
   const state=scenes[i].states[currentViews[i]];
   const mobile=window.matchMedia("(max-width:700px)").matches && state[5];
   viewerImage.src=mobile?state[5]:state[2];
   viewerImage.alt=state[3];
   viewerTitle.textContent=scenes[i].name+" — "+state[0];
   viewer.classList.remove("is-zoomed");
   zoomControl.textContent="Ver tamanho original";
   if(typeof viewer.showModal==="function")viewer.showModal();
  });
 });
 section.querySelector("#film-capture-close").addEventListener("click",()=>viewer.close());
 viewer.addEventListener("click",e=>{if(e.target===viewer)viewer.close()});
 viewer.addEventListener("close",()=>{
  viewerImage.removeAttribute("src");
  viewer.classList.remove("is-zoomed");
  opener?.focus();
 });
 zoomControl.addEventListener("click",()=>{
  const enlarged=viewer.classList.toggle("is-zoomed");
  zoomControl.textContent=enlarged?"Ajustar à janela":"Ver tamanho original";
 });
 function frame(){
  scheduled=0;
  const midpoint=innerHeight*.5;
  let hit=-1;
  for(let i=0;i<cases.length;i++){
   const bounds=cases[i].getBoundingClientRect();
   if(bounds.top<=midpoint&&bounds.bottom>=midpoint)hit=i;
   const range=Math.max(1,bounds.height-innerHeight);
   const percent=Math.min(1,Math.max(0,-bounds.top/range));
   cases[i].querySelector(".film-progress-fill").style.width=(percent*100).toFixed(2)+"%";
  }
  document.body.classList.toggle("film-in-view",hit>=0);
  if(hit===active)return;
  if(active>=0)cases[active].classList.remove("is-current");
  active=hit;
  if(active>=0)cases[active].classList.add("is-current");
  shortcuts.forEach((a,j)=>{
   a.classList.toggle("is-current",j===active);
   if(j===active)a.setAttribute("aria-current","true");
   else a.removeAttribute("aria-current");
  });
  // Do not silently change views when the user scrolls; selection persists.
 }
 function onScroll(){if(!scheduled)scheduled=requestAnimationFrame(frame)}
 window.addEventListener("scroll",onScroll,{passive:true});
 window.addEventListener("resize",onScroll);
 frame();
 // Preload first views after initial content is ready. Other views are fetched on demand.
 if("requestIdleCallback" in window){
  window.requestIdleCallback(()=>scenes.slice(1,4).forEach(s=>{const img=new Image();img.src=s.states[0][2]}));
 }
}
