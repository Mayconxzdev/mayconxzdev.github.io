import {isDirectMotion} from "./motion-preference.js";

// Small, reversible movement in normal document flow. It never pins mobile scroll.
export function initMobileCinema(){
 const reduced=matchMedia("(prefers-reduced-motion: reduce)");
 const compact=matchMedia("(max-width: 800px), (max-height: 600px)");
 const slides=[...document.querySelectorAll(".v8-world .world-slide")];
 if(!slides.length)return()=>{};
 const panels=slides.map(slide=>slide.querySelector(".world-main-screen"));
 let frame=0;
 const reset=()=>{
  for(const panel of panels){
   if(!panel)continue;
   for(const key of ["transform","opacity","clipPath","willChange"])panel.style.removeProperty(key.replace(/[A-Z]/g,m=>"-"+m.toLowerCase()));
  }
  delete document.documentElement.dataset.mobileCinema;
 };
 const run=()=>{
  frame=0;
  if(!compact.matches||isDirectMotion()){reset();return}
  const height=innerHeight;let visible=false;
  for(let i=0;i<slides.length;i++){
   const panel=panels[i];if(!panel)continue;
   const rect=slides[i].getBoundingClientRect();
   if(rect.bottom < -height||rect.top > height*1.8){panel.style.removeProperty("will-change");continue}
   visible=true;
   const progress=Math.max(0,Math.min(1,(height*.91-rect.top)/(height*.69)));
   const remaining=1-progress;
   const x=(i%2?10:-10)*remaining,y=32*remaining,scale=.962+.038*progress;
   panel.style.transform=`translate3d(${x.toFixed(1)}px,${y.toFixed(1)}px,0) scale(${scale.toFixed(4)})`;
   panel.style.opacity=(.82+.18*progress).toFixed(3);
   panel.style.clipPath=`inset(0 0 ${(10*remaining).toFixed(2)}% 0)`;
   panel.style.willChange=remaining>.001?"transform,opacity,clip-path":"auto";
  }
  document.documentElement.dataset.mobileCinema=visible?"active":"ready";
 };
 const queue=()=>{if(!frame)frame=requestAnimationFrame(run)};
 addEventListener("scroll",queue,{passive:true});
 addEventListener("resize",queue,{passive:true});
 addEventListener("pageshow",queue);
 compact.addEventListener("change",queue);
 reduced.addEventListener("change",queue);
 document.addEventListener("lv-motion-change",queue);
 queue();
 return()=>{
  cancelAnimationFrame(frame);frame=0;reset();
  removeEventListener("scroll",queue);removeEventListener("resize",queue);removeEventListener("pageshow",queue);
  compact.removeEventListener("change",queue);reduced.removeEventListener("change",queue);
  document.removeEventListener("lv-motion-change",queue);
 };
}
