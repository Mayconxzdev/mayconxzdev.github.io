(() => {"use strict";
 const gallery=document.querySelector(".case-gallery");
 const dialog=document.querySelector("#evidence-dialog");
 if(!gallery||!dialog)return;
 const buttons=Array.from(gallery.querySelectorAll(".gallery-trigger"));
 gallery.querySelectorAll(".gallery-item img").forEach(image=>{
  const fallback=image.closest(".gallery-item")?.querySelector(".gallery-load-error");
  if(!fallback)return;
  image.addEventListener("error",()=>{fallback.hidden=false});
  image.addEventListener("load",()=>{fallback.hidden=true});
  if(image.complete&&!image.naturalWidth)fallback.hidden=false;
 });
 const big=dialog.querySelector("#evidence-large");
 const counter=dialog.querySelector("#evidence-count");
 const caption=dialog.querySelector("#evidence-caption");
 const prev=dialog.querySelector("#evidence-prev"),next=dialog.querySelector("#evidence-next");
 let current=0,returnFocus=null;
 const show=(idx)=>{
  current=(idx+buttons.length)%buttons.length;
  const b=buttons[current];
  const pic=b.querySelector("img");
  big.src=pic.getAttribute("src");
  big.alt=pic.alt;
  caption.textContent=b.dataset.caption||pic.alt;
  counter.textContent=(current+1)+" / "+buttons.length;
 };
 buttons.forEach((button,index)=>button.addEventListener("click",()=>{
  returnFocus=button;show(index);dialog.showModal();
 }));
 prev.addEventListener("click",()=>show(current-1));
 next.addEventListener("click",()=>show(current+1));
 dialog.querySelector("#evidence-close").addEventListener("click",()=>dialog.close());
 dialog.addEventListener("click",e=>{if(e.target===dialog)dialog.close()});
 dialog.addEventListener("keydown",e=>{if(e.key==="ArrowLeft"){e.preventDefault();show(current-1)}if(e.key==="ArrowRight"){e.preventDefault();show(current+1)}});
 dialog.addEventListener("close",()=>{big.removeAttribute("src");returnFocus?.focus()});
})();
