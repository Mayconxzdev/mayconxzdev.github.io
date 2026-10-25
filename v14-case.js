(()=>{"use strict";
 const scene=document.querySelector("[data-v14-scene]");
 if(scene){
  const choices=[...scene.querySelectorAll("[data-v14-frame]")],stock=[...scene.querySelectorAll(".v14-stock .gallery-trigger")];
  const img=scene.querySelector(".v14-scene-main"),title=scene.querySelector("[data-v14-title]"),
   caption=scene.querySelector("[data-v14-caption]"),origin=scene.querySelector("[data-v14-origin]");
  let selected=0;
  const select=i=>{
   const n=choices[i];if(!n)return;
   selected=i;
   const source=stock[i]?.querySelector("img");
   if(!source)return;
   img.classList.add("is-changing");
   // Set content synchronously; animation is cosmetic only and never gates the evidence.
   img.src=source.getAttribute("src");img.alt=source.alt;
   const label=n.querySelector("span")?.textContent||"";
   title.textContent=label.replace(/^\d+\s*\/\s*/,"");
   caption.textContent=source.alt;
   origin.textContent=n.dataset.origin||"Captura de projeto";
   choices.forEach((c,k)=>{c.classList.toggle("is-selected",k===i);c.setAttribute("aria-pressed",String(k===i))});
   if(!matchMedia("(prefers-reduced-motion:reduce)").matches)requestAnimationFrame(()=>img.classList.remove("is-changing"));
   else img.classList.remove("is-changing");
  };
  choices.forEach((c,i)=>c.addEventListener("click",()=>select(i)));
  scene.querySelector(".v14-zoom")?.addEventListener("click",()=>stock[selected]?.click());
 }
 const arch=document.querySelector(".v14-architecture");
 if(arch){
  const buttons=[...arch.querySelectorAll("[data-v14-step]")],detail=arch.querySelector(".v14-arch-detail");
  const texts=buttons.map(x=>x.dataset.v14Detail);
  buttons.forEach((b,i)=>b.addEventListener("click",()=>{
   buttons.forEach((x,j)=>{x.classList.toggle("is-selected",j===i);x.setAttribute("aria-pressed",String(i===j))});
   detail.textContent=texts[i]||b.textContent;
  }));
 }
})();
