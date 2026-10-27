(()=>{"use strict";
 const galleries=[...document.querySelectorAll("[data-v14-gallery]")];
 galleries.forEach(gallery=>{
  const choices=[...gallery.querySelectorAll("[data-v14-select]")];
  const slides=[...gallery.querySelectorAll("[data-v14-shot]")];
  if(!choices.length||!slides.length)return;
  let current=0;
  const select=(n,focus=false)=>{
   current=(n+slides.length)%slides.length;
   slides.forEach((slide,i)=>{slide.hidden=i!==current});
   const selectedImage=slides[current]?.querySelector("img");
   if(selectedImage){selectedImage.loading="eager";selectedImage.fetchPriority="high";}
   choices.forEach((button,i)=>{
    const on=i===current;
    button.setAttribute("aria-pressed",String(on));
    button.classList.toggle("is-active",on);
    if(on&&focus)button.focus();
   });
  };
  choices.forEach((button,i)=>{
   button.addEventListener("click",()=>select(i));
   button.addEventListener("keydown",event=>{
    if(event.key==="ArrowRight"||event.key==="ArrowDown"){event.preventDefault();select(i+1,true)}
    if(event.key==="ArrowLeft"||event.key==="ArrowUp"){event.preventDefault();select(i-1,true)}
    if(event.key==="Home"){event.preventDefault();select(0,true)}
    if(event.key==="End"){event.preventDefault();select(slides.length-1,true)}
   });
  });
  const hashId=decodeURIComponent(location.hash.slice(1));
  const linked=slides.findIndex(slide=>slide.id===hashId);
  select(linked>=0?linked:0);
  if(linked>=0)requestAnimationFrame(()=>slides[linked].scrollIntoView({block:"start"}));
 });
})();
