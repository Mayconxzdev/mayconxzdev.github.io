// Mobile-only, user-controlled expansion of the three real hero screenshots.
// Unlike a scroll-pinned carousel, this never intercepts wheel/touch/anchor navigation.
export function initHeroPreviewPicker(){
 const stage=document.querySelector(".hero-stage");
 const buttons=[...document.querySelectorAll("[data-hero-preview]")];
 const links=[...stage?.querySelectorAll(".stage-window")||[]];
 if(!stage||buttons.length!==3||links.length!==3)return;
 const mobile=matchMedia("(max-width: 550px)");
 let selected=0,hasInteracted=false;
 const paint=()=>{
  const inspect=mobile.matches&&hasInteracted;
  stage.classList.toggle("v15-preview-engaged",inspect);
  stage.dataset.preview=String(selected);
  buttons.forEach((button,index)=>{
   const current=index===selected;
   button.setAttribute("aria-pressed",String(current));
  });
  links.forEach((link,index)=>{
   link.classList.toggle('v15-preview-active', inspect&&index===selected);
   // All are accessible in the default composition; after manual selection,
   // the non-selected screenshots are not keyboard-tabbable behind it.
   if(inspect){
    link.inert=index!==selected;
    link.setAttribute("aria-hidden",String(index!==selected));
   }else{
    link.inert=false;
    link.removeAttribute("aria-hidden");
   }
  });
 };
 buttons.forEach((button,index)=>button.addEventListener("click",()=>{
  hasInteracted=true;selected=index;paint();
 }));
 const update=()=>{
  if(!mobile.matches){hasInteracted=false;selected=0;}
  paint();
 };
 mobile.addEventListener?.("change",update);
 update();
}
