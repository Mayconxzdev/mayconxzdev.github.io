import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import scenes from "./cinema-scenes.json";

const motionQuery=window.matchMedia("(prefers-reduced-motion: reduce)");
const mobileQuery=window.matchMedia("(max-width: 800px)");
const detailImage=(url)=>{const image=new Image();image.decoding="async";image.src=url;return image};
export function initRealScenes(){
 const section=document.querySelector(".cinema-section");
 if(!section)return;
 const chapters=Array.from(section.querySelectorAll("[data-cinema-chapter]"));
 const controls=Array.from(section.querySelectorAll("[data-scene]"));
 const primary=section.querySelector("#wb-image"),secondary=section.querySelector("#wb-image-secondary");
 const board=section.querySelector(".cinema-board");
 const name=section.querySelector("#wb-name");
 const source=section.querySelector("#wb-source");
 const link=section.querySelector("#wb-link");
 const count=section.querySelector("#wb-counter");
 const mainCaption=section.querySelector("#wb-main-caption");
 const secondaryCaption=section.querySelector("#wb-secondary-caption");
 const title=section.querySelector("#cinema-active-title");
 const live=section.querySelector("#wb-live");
 let active=-1;
 if(chapters.length!==scenes.length||controls.length!==scenes.length)throw new Error("Narrative steps do not match the five case entries");
 function update(i,manual=false){
  if(i<0||i>=scenes.length||i===active&&!manual)return;
  const changed=i!==active; active=i;
  const item=scenes[i],reduced=motionQuery.matches;
  chapters.forEach((c,j)=>c.classList.toggle("is-active",j===i));
  controls.forEach((c,j)=>{c.classList.toggle("is-selected",j===i);c.setAttribute("aria-pressed",String(i===j));});
  name.textContent=item.name;
  count.textContent=item.index+" / 05";
  title.textContent=item.index+" / "+item.name;
  source.textContent=item.source;
  board.style.setProperty("--cinema-accent",item.color);
  link.href="/projetos/"+item.key+"/";
  primary.src=item.a;primary.alt=item.alt_a;
  secondary.src=item.b;secondary.alt=item.alt_b;
  mainCaption.textContent=item.caption_a;
  secondaryCaption.textContent=item.caption_b;
  if(manual){live.setAttribute("aria-live","polite");live.textContent="Projeto selecionado: "+item.name;}
  if(changed&&!reduced&&!mobileQuery.matches){
   gsap.killTweensOf([board,primary,secondary]);
   gsap.fromTo([primary,secondary],{autoAlpha:.75,y:8,scale:.994},{autoAlpha:1,y:0,scale:1,stagger:.05,duration:.38,ease:"power2.out",overwrite:true});
   gsap.fromTo(board,{borderColor:item.color},{borderColor:"#f0f0ec",duration:.7,ease:"power1.out",overwrite:true});
  }
 }
 controls.forEach((btn,i)=>btn.addEventListener("click",()=>{
  update(i,true);
  chapters[i].scrollIntoView({block:"center",behavior:motionQuery.matches?"instant":"smooth"});
 }));
 update(0);
 // Scroll-triggered focus follows the five story chapters; scrolling itself remains native.
 const mm=gsap.matchMedia();
 mm.add("(min-width: 801px)",()=>{
  const relativeFocus=()=>window.innerHeight*.52;
  const selectClosest=()=>{
   let best=0,shortest=Infinity;
   chapters.forEach((ch,i)=>{
    const rect=ch.getBoundingClientRect();
    const center=(rect.top+rect.bottom)*.5;
    const distance=Math.abs(center-relativeFocus());
    if(distance<shortest){best=i;shortest=distance}
   });
   update(best);
  };
  const trigger=ScrollTrigger.create({
    trigger:section,start:"top 70%",end:"bottom 30%",
    onEnter:selectClosest,onEnterBack:selectClosest,onUpdate:selectClosest
  });
  // ScrollTrigger handles reverse scrolling as well as forward scrolling.
  selectClosest();
  return ()=>{trigger.kill();gsap.killTweensOf([board,primary,secondary]);};
 });
 mm.add("(max-width: 800px)",()=>{
  // No pinned panel on phones: each chapter owns its two screenshots in document order.
  if(!("IntersectionObserver" in window))return;
  const io=new IntersectionObserver(entries=>{
   for(const e of entries)if(e.isIntersecting){
    const i=Number(e.target.dataset.cinemaChapter);
    if(Number.isInteger(i))update(i);
    e.target.classList.add("is-seen");
   }
  },{rootMargin:"-18% 0px -40% 0px",threshold:0});
  chapters.forEach(c=>io.observe(c));
  return ()=>io.disconnect();
 });
 // Only preload the small selection of already-published images that follows first.
 const warm=()=>scenes.slice(1,3).forEach(s=>{detailImage(s.a);detailImage(s.b)});
 if("requestIdleCallback" in window)window.requestIdleCallback(warm);else warm();
}
