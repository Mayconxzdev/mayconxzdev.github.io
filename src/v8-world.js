import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import {Flip} from "gsap/Flip";
import scenes from "./v8-story.json";
import {isDirectMotion} from "./motion-preference.js";
import {evidenceIdFor} from "../scripts/evidence-map.mjs";
gsap.registerPlugin(ScrollTrigger,Flip);
const clamp=v=>Math.max(0,Math.min(1,v));
const smooth=v=>{const x=clamp(v);return x*x*(3-2*x)};
const preload=src=>new Promise(resolve=>{
 const img=new Image();img.onload=()=>resolve(true);img.onerror=()=>resolve(false);
 img.src=src;if(img.complete)resolve(img.naturalWidth>0);
});
export function initMotionWorld(){
 const hero=document.querySelector(".hero"),world=document.querySelector(".v8-world");
 if(!hero||!world)return;
 const slides=[...world.querySelectorAll(".world-slide")];
 if(slides.length!==scenes.length)throw Error("V8: scenes and manifest differ");
 const reduced={get matches(){return isDirectMotion()}};
 const small=matchMedia("(max-width:700px)");
 const flowMode=()=>isDirectMotion()||innerWidth<=800||innerHeight<=600;
 const selected=scenes.map(()=>0),tokens=scenes.map(()=>0),groups=[];
 let active=0,opener=null;
 let playing=-1,playTimer=null;
 const playButtons=[];
 const stopRoute=()=>{
  clearTimeout(playTimer);playTimer=null;
  if(playing>=0&&playButtons[playing]){
   playButtons[playing].textContent="Ver percurso";
   playButtons[playing].setAttribute("aria-label","Ver o percurso de "+scenes[playing].name);
   playButtons[playing].setAttribute("aria-pressed","false");
  }
  playing=-1;
 };
 const visibilityPause=()=>{if(document.hidden)stopRoute()};
 document.addEventListener("visibilitychange",visibilityPause);
 const rail=world.querySelector(".v8-rail-fill"),counter=world.querySelector(".v8-rail-current");
 const dialog=document.getElementById("v8-lightbox");
 const dialogImg=document.getElementById("v8-lightbox-img");
 const dialogTitle=document.getElementById("v8-lightbox-title");
 document.getElementById("v8-lightbox-close").addEventListener("click",()=>dialog.close());
 dialog.addEventListener("click",e=>{if(e.target===dialog)dialog.close()});
 dialog.addEventListener("close",()=>{dialogImg.removeAttribute("src");opener?.focus()});
 const mediaFor=view=>small.matches&&view[5]?view[5]:view[2];
 function access(index){
  slides.forEach((slide,j)=>{
   const yes=flowMode()||j===index;
   slide.inert=!yes;slide.setAttribute("aria-hidden",String(!yes));
  });
  counter.textContent=String(index+1).padStart(2,"0")+" / 05";
 }
 // Cache DOM nodes once. No per-scroll querySelectorAll, blur, gradient masks or large-screen filters.
 const layers=slides.map(slide=>({
  slide,css:slide.style,
  stage:slide.querySelector(".world-art").style,
  label:slide.querySelector(".world-scene-label").style,
  caption:slide.querySelector(".world-description").style
 }));
 let lastPair=[-1,-1],lastProgress=-1,lastVisible=-1;
 const reset=index=>{
  if(index<0||index>=layers.length)return;
  const l=layers[index];
  l.css.visibility="hidden";
  l.css.pointerEvents="none";
  l.css.clipPath="none";
  l.css.maskImage="none";
  l.css.webkitMaskImage="none";
  l.css.filter="none";
  l.css.opacity="0";
  l.css.transform="translate3d(0,0,0)";
  l.css.background="";
  l.stage.opacity="";
  l.stage.transform="none";
  l.stage.clipPath="none";
  l.caption.opacity="1";l.label.opacity="1";
 };
 const prepare=index=>{
  const l=layers[index];
  l.slide.querySelector(".world-main-image").loading="eager";
  l.css.visibility="visible";
  l.css.opacity="1";
  l.css.maskImage="none";l.css.webkitMaskImage="none";
  l.css.filter="none";
  l.stage.opacity="1";l.stage.transform="none";
 };
 function frame(p){
  if(reduced.matches)return;
  const safe=clamp(p);
  if(Math.abs(safe-lastProgress)<.00025)return;
  lastProgress=safe;
  const pos=safe*(layers.length-1);
  const i=Math.min(layers.length-1,Math.floor(pos));
  const j=Math.min(layers.length-1,i+1);
  const t=i===layers.length-1?0:smooth(pos-i);
  const incoming=j!==i&&t>0.0003;
  const target=incoming&&t>=.54?j:i;
  if(target!==active){
   if(playing>=0&&playing!==target)stopRoute();
   active=target;access(active);
   document.querySelectorAll(".v11-world-jumpbar [data-jump]").forEach(b=>{
    b.classList.toggle("is-current",Number(b.dataset.jump)===active);
    b.setAttribute("aria-current",Number(b.dataset.jump)===active?"step":"false");
   });
  }
  // Compositor-friendly progress indicator: no repeated height changes.
  rail.style.transform="scaleY("+safe.toFixed(4)+")";
  const pair=[i,incoming?j:-1];
  if(lastPair[0]!==pair[0]||lastPair[1]!==pair[1]){
   for(const index of lastPair)if(index!==i&&index!==j)reset(index);
   lastPair=pair;
  }
  // Change one chapter at a time. The outgoing capture makes room before the
  // next one appears; captions never crossfade and two interfaces never stack.
  const visibleIndex=incoming&&t>=.54?j:i;
  if(lastVisible!==visibleIndex){
   if(lastVisible>=0&&lastVisible!==visibleIndex)reset(lastVisible);
   prepare(visibleIndex);lastVisible=visibleIndex;
  }
  if(!incoming){
   for(const index of [i,j])if(index>=0&&index<layers.length&&index!==visibleIndex)reset(index);
   const current=layers[visibleIndex];
   current.css.zIndex="1";current.css.visibility="visible";current.css.opacity="1";
   current.css.background="var(--v9-paper, #faf9f6)";current.css.clipPath="none";current.css.pointerEvents="auto";
   current.stage.opacity="1";current.stage.clipPath="none";current.stage.transform="none";
   current.caption.opacity="1";current.label.opacity="1";
   return;
  }
  const offsets=[
   {x:0,y:8,scale:.995},
   {x:6,y:0,scale:.995},
   {x:0,y:-6,scale:.995},
   {x:-6,y:0,scale:.995}
  ];
  const motion=offsets[j-1]||{x:0,y:12,scale:.99};
  const current=layers[visibleIndex];
  current.css.zIndex="1";current.css.visibility="visible";current.css.opacity="1";
  current.css.background="var(--v9-paper, #faf9f6)";current.css.clipPath="none";current.css.pointerEvents="auto";
  current.stage.clipPath="none";
  if(visibleIndex===i){
   const exit=smooth((t-.42)/.12);
   current.stage.opacity="1";
   current.stage.transform="translate3d(0,"+(-4*exit).toFixed(1)+"px,0) scale("+(1+.004*exit).toFixed(4)+")";
  }else{
   const enter=smooth((t-.54)/.12);
   current.stage.opacity="1";
   current.stage.transform="translate3d("+(motion.x*(1-enter)).toFixed(1)+"px,"+
    (motion.y*(1-enter)).toFixed(1)+"px,0) scale("+(1+(motion.scale-1)*(1-enter)).toFixed(4)+")";
  }
  current.caption.opacity="1";current.label.opacity="1";
 }
 async function switchView(i,j){
  const project=scenes[i],scene=slides[i],view=project.states[j];
  if(!view||selected[i]===j)return false;
  const request=++tokens[i],url=mediaFor(view);
  const ok=await preload(url);
  if(tokens[i]!==request)return false;
  const imageFallback=scene.querySelector(".world-image-fallback");
  if(!ok){scene.querySelector(".world-route-status").textContent="A captura não carregou. Você pode tentar novamente.";if(imageFallback)imageFallback.hidden=false;stopRoute();return false}
  const img=scene.querySelector(".world-main-image");
  const indicator=scene.querySelector(".world-active-indicator");
  const state=indicator&&!reduced.matches?Flip.getState(indicator):null;
  selected[i]=j;
  img.src=url;img.alt=view[3];img.width=view[4].width;img.height=view[4].height;
  scene.querySelector(".world-atmosphere").style.backgroundImage='url("'+url+'")';
  const fragmentSources=view.at(-1)?.fragments||[];
  scene.querySelectorAll(".world-fragment").forEach((target,k)=>{
   const source=fragmentSources[k];
   if(source){target.hidden=false;target.querySelector("img").src=source}else target.hidden=true;
  });
  const evidence=scene.querySelector(".v11-evidence-message");
  if(evidence)evidence.textContent=(view[6]?.context||view[3]);
  const lens=scene.querySelector(".v11-evidence-lens"),inspect=scene.querySelector(".v11-inspect");
  if(lens&&!fragmentSources.length){lens.hidden=true;inspect.disabled=true;inspect.setAttribute("aria-expanded","false");inspect.title="Não há recortes adicionais para esta captura."}
  else if(lens&&inspect){inspect.disabled=false;inspect.removeAttribute("title")}
  if(lens&&!lens.hidden){
   lens.querySelectorAll("img").forEach((image,k)=>{if(fragmentSources[k])image.src=fragmentSources[k]});
  }
  const story=view[6]||{title:view[1],context:view[3]};
  const descContent=scene.querySelector(".world-desc-content");
  if(descContent&&!reduced.matches){
   gsap.fromTo(descContent,{opacity:.4,y:3},{opacity:1,y:0,duration:.25,ease:"power2.out"});
  }
  scene.querySelector(".world-desc-content h3").textContent=story.title;
  scene.querySelector(".world-desc-context").textContent=story.context;
  scene.querySelector(".world-current-view").textContent=view[0];
  scene.querySelector(".world-page-label").textContent=String(j+1).padStart(2,"0")+" / "+String(project.states.length).padStart(2,"0");
  scene.style.setProperty("--view-progress",j/Math.max(1,project.states.length-1));
  scene.querySelector(".world-route-status").textContent=project.name+": "+view[0]+". "+story.title;
  const caseLink=scene.querySelector(".world-case-link");
  if(caseLink)caseLink.href="/projetos/"+project.key+"/#media-"+evidenceIdFor(project.key,view[2]);
  if(imageFallback)imageFallback.hidden=true;
  groups[i].forEach((button,k)=>{
   button.classList.toggle("is-selected",k===j);
   button.setAttribute("aria-pressed",String(k===j));
  });
  if(indicator){
   groups[i][j].appendChild(indicator);
   if(state)Flip.from(state,{duration:.25,ease:"power2.out",absolute:true,overwrite:true});
  }
  // The real interface remains the protagonist. Direction reflects the journey,
  // without overlapping screenshot text or pretending the product changed live.
  const screen=scene.querySelector(".world-main-screen");
  gsap.killTweensOf(screen);gsap.set(img,{opacity:1,x:0,scale:1});
  if(!reduced.matches){
   const entrances=[{x:20,y:0},{x:0,y:15},{x:8,y:0},{x:0,y:0},{x:16,y:0}];
   gsap.fromTo(screen,{...entrances[i],opacity:.55,scale:i===3?.985:1},{x:0,y:0,opacity:1,scale:1,duration:i===3?.52:.38,ease:"power2.out",overwrite:true});
  }else gsap.set(screen,{x:0,y:0,opacity:1,scale:1});
  return true;
 }
 const advanceRoute=async()=>{
  if(playing<0)return;
  const i=playing,next=selected[i]+1;
  if(next>=scenes[i].states.length){stopRoute();return}
  await switchView(i,next);
  if(playing!==i)return;
  if(next===scenes[i].states.length-1){stopRoute();playButtons[i].textContent="Rever percurso";playButtons[i].setAttribute("aria-label","Rever o percurso de "+scenes[i].name);return}
  playTimer=setTimeout(advanceRoute,6500);
 };
 slides.forEach((slide,i)=>{
  const status=document.createElement("span");
  status.className="world-route-status sr-only";status.setAttribute("role","status");
  slide.querySelector(".world-actions").appendChild(status);
  const play=document.createElement("button");
  play.type="button";play.className="world-route-play";play.textContent="Ver percurso";
  play.setAttribute("aria-label","Ver o percurso de "+scenes[i].name);
  play.setAttribute("aria-pressed","false");playButtons[i]=play;
  slide.querySelector(".world-links").appendChild(play);
  play.addEventListener("click",async()=>{
   if(playing===i){stopRoute();return}
   stopRoute();playing=i;
   play.textContent="Pausar percurso";play.setAttribute("aria-pressed","true");
   play.setAttribute("aria-label","Pausar o percurso de "+scenes[i].name);
   if(selected[i]===scenes[i].states.length-1)await switchView(i,0);
   if(playing===i)playTimer=setTimeout(advanceRoute,6500);
  });
  const group=[...slide.querySelectorAll(".world-tab")];groups[i]=group;
  const mainImage=slide.querySelector(".world-main-image");
  const imageFallback=document.createElement("span");
  imageFallback.className="world-image-fallback";
  imageFallback.setAttribute("role","status");
  imageFallback.hidden=true;
  imageFallback.textContent="Esta captura não está disponível agora. Consulte a legenda ou abra o case para continuar.";
  slide.querySelector(".world-main-screen").appendChild(imageFallback);
  const syncImageFallback=()=>{imageFallback.hidden=mainImage.naturalWidth>0};
  mainImage.addEventListener("load",syncImageFallback);
  mainImage.addEventListener("error",()=>{imageFallback.hidden=false});
  if(mainImage.complete)syncImageFallback();
  group.forEach((button,j)=>{
   button.addEventListener("click",()=>{stopRoute();switchView(i,j)});
   button.addEventListener("keydown",event=>{
    if(!["ArrowLeft","ArrowRight"].includes(event.key))return;
    event.preventDefault();
    const idx=(j+(event.key==="ArrowRight"?1:-1)+group.length)%group.length;
    stopRoute();group[idx].focus();switchView(i,idx);
   });
  });
  const indicator=document.createElement("span");
  indicator.className="world-active-indicator";indicator.setAttribute("aria-hidden","true");
  group[0].appendChild(indicator);
  const inspect=slide.querySelector(".v11-inspect");
  const lens=slide.querySelector(".v11-evidence-lens");
  const close=slide.querySelector(".v11-lens-close");
  const toggleLens=show=>{
   lens.hidden=!show;
   inspect.setAttribute("aria-expanded",String(show));
   if(show){
    const state=scenes[i].states[selected[i]],sources=state.at(-1)?.fragments||[];
    lens.querySelectorAll("img").forEach((img,k)=>{if(sources[k])img.src=sources[k]});
   }
  };
  inspect.addEventListener("click",()=>toggleLens(lens.hidden));
  close.addEventListener("click",()=>{toggleLens(false);inspect.focus()});
  slide.querySelector(".world-zoom").addEventListener("click",event=>{
   stopRoute();
   opener=event.currentTarget;
   const view=scenes[i].states[selected[i]];
   dialogImg.src=mediaFor(view);dialogImg.alt=view[3];
   dialogTitle.textContent=scenes[i].name+" — "+view[0];dialog.showModal();
  });
 });
 const routeVisibility=new IntersectionObserver(entries=>{
  for(const entry of entries)if(slides.indexOf(entry.target)===playing&&!entry.isIntersecting)stopRoute();
 },{threshold:0});
 slides.forEach(slide=>routeVisibility.observe(slide));
 // No scene advances after a visitor leaves it or opens another project.
 world.addEventListener("click",event=>{if(event.target.closest("a"))stopRoute()});
 // On narrow screens use the original mobile site captures when they exist.
 if(small.matches){
  slides.forEach((slide,i)=>{
   const view=scenes[i].states[0];
   if(!view[5])return;
   const img=slide.querySelector(".world-main-image");
   img.src=view[5];
   slide.querySelector(".world-atmosphere").style.backgroundImage='url("'+view[5]+'")';
  });
 }
 const jumpBar=document.querySelector(".v11-world-jumpbar");
 if(jumpBar){
  jumpBar.addEventListener("click",event=>{
   const button=event.target.closest("[data-jump]");
   if(!button)return;
   const index=Number(button.dataset.jump);
   if(!Number.isInteger(index)||index<0||index>=slides.length)return;
   stopRoute();
   if(flowMode()){
    slides[index].scrollIntoView({behavior:"instant",block:"start"});
    return;
   }
   const sectionTop=world.getBoundingClientRect().top+scrollY;
   const distance=world.offsetHeight-innerHeight;
   window.scrollTo({top:sectionTop+distance*(index/(slides.length-1)),behavior:"instant"});
  });
 }
 // A direct link works independently of visiting the home first.
 const deeplink=new URL(location.href).searchParams.get("projeto");
 if(deeplink){
  const index=scenes.findIndex(item=>item.key===deeplink);
  if(index>=0)requestAnimationFrame(()=>requestAnimationFrame(()=>{
   if(flowMode())slides[index].scrollIntoView({behavior:"instant",block:"start"});
   else window.scrollTo({top:world.getBoundingClientRect().top+scrollY+(world.offsetHeight-innerHeight)*(index/(slides.length-1)),behavior:"instant"});
  }));
 }
 const responsive=gsap.matchMedia();
 const configureResponsive=()=>responsive.add({mobile:"(max-width:800px)",desktop:"(min-width:801px)",lowHeight:"(max-height:600px)"},()=>{
 stopRoute();
  const compact=innerWidth<=800||innerHeight<=600;
  document.documentElement.classList.toggle("v15-mobile-stable",compact);
 lastPair=[-1,-1];lastProgress=-1;lastVisible=-1;
  if(reduced.matches||compact){
  layers.forEach(l=>{
   for(const key of ["visibility","pointerEvents","clipPath","maskImage","webkitMaskImage","filter","opacity","transform","zIndex","background"])l.css[key]="";
   l.stage.transform="";l.stage.opacity="";l.stage.clipPath="";l.caption.opacity="";l.label.opacity="";
  });
   access(active);
   if(flowMode()){
   let queued=false;
   const syncMobileChapter=()=>{
    queued=false;
    const targetY=innerHeight*.38;
    let index=0,score=Infinity;
    slides.forEach((slide,i)=>{const rect=slide.getBoundingClientRect();const midpoint=rect.top+Math.min(rect.height,innerHeight)*.5;const distance=Math.abs(midpoint-targetY);if(distance<score){score=distance;index=i}});
    if(playing>=0&&playing!==index)stopRoute();
    active=index;access(index);
    document.querySelectorAll(".v11-world-jumpbar [data-jump]").forEach(button=>{
     const current=Number(button.dataset.jump)===index;
     button.classList.toggle("is-current",current);
     button.setAttribute("aria-current",current?"step":"false");
    });
   };
   const queueMobile=()=>{if(!queued){queued=true;requestAnimationFrame(syncMobileChapter)}};
   addEventListener("scroll",queueMobile,{passive:true});
   addEventListener("resize",queueMobile,{passive:true});
   syncMobileChapter();
   return ()=>{removeEventListener("scroll",queueMobile);removeEventListener("resize",queueMobile)};
   }
   return;
 }
 access(active);
 document.querySelectorAll(".v11-world-jumpbar [data-jump]").forEach(button=>{
  const current=Number(button.dataset.jump)===active;
  button.classList.toggle("is-current",current);
  button.setAttribute("aria-current",current?"step":"false");
 });
 // Preserve the V5 composition exactly; all three windows descend as one group.
 const heroTimeline=gsap.timeline({scrollTrigger:{
  trigger:hero,start:"top top",end:"bottom top",scrub:true,invalidateOnRefresh:true
 }});
 heroTimeline.to(".hero-stage",{y:()=>Math.min(hero.offsetHeight*.93,1100),duration:1,ease:"none"},0)
  .to(".hero-copy",{y:-22,duration:1,ease:"none"},0)
  .to(".hero-foot",{y:-8,duration:1,ease:"none"},0)
  .to(".hero-stage",{opacity:0,duration:.18,ease:"none"},.82);
 // One actual image from the hero morphs toward the first case; no screenshot swap.
 // Fixed, transform-only clone; falls back to ordinary content in direct/reduced motion.
 const source=hero.querySelector(".stage-main");
 const destination=slides[0].querySelector(".world-main-image");
 let handoffGhost=null;
 if(source&&destination&&innerWidth>800){
  const ghost=source.cloneNode(true);handoffGhost=ghost;
  ghost.className="v11-handoff-ghost";
  ghost.removeAttribute("href");
  ghost.removeAttribute("aria-label");
  ghost.setAttribute("aria-hidden","true");
  ghost.querySelector("img")?.removeAttribute("loading");
  document.body.appendChild(ghost);
  let rect=null,delta=null,captionTop=0,worldTop=0;
  const measure=()=>{
   const from=source.getBoundingClientRect();
   const section=world.getBoundingClientRect();
   const to=destination.getBoundingClientRect();
   rect={x:from.x,y:from.y,w:from.width,h:from.height};
   delta={x:to.x-from.x,y:to.y-section.y-from.y,sx:to.width/from.width,sy:to.height/from.height};
   captionTop=slides[0].querySelector(".world-description").getBoundingClientRect().top-section.y;
   worldTop=section.y+scrollY;
   ghost.style.left=rect.x+"px";ghost.style.top=rect.y+"px";
   ghost.style.width=rect.w+"px";ghost.style.height=rect.h+"px";
  };
  ScrollTrigger.create({
   trigger:hero,
   start:"bottom 40%",
   end:"bottom top",
   onEnter:measure,
   onEnterBack:()=>{if(!rect)measure()},
   onUpdate:self=>{
    if(!rect||!delta)measure();
    const t=smooth(self.progress);
    // One owner at a time: crossfading two different rectangles doubled screenshot text.
    const owns=t>=.14&&t<.92;
    ghost.style.visibility=owns?"visible":"hidden";
    ghost.style.opacity=owns?"1":"0";
    source.style.opacity=t<.14?"1":"0";
    destination.style.opacity=t>=.92?"1":"0";
    // Clip against the reading surface, using cached geometry rather than per-frame layout reads.
    const currentHeight=rect.h*(1+(delta.sy-1)*t);
    const currentBottom=rect.y+delta.y*t+currentHeight;
    const captionEdge=Math.max(0,worldTop-scrollY)+captionTop;
    const clipped=clamp((currentBottom-captionEdge)/currentHeight)*100;
    ghost.style.clipPath="inset(0 0 "+clipped.toFixed(3)+"% 0)";
    const bar=ghost.querySelector(".stage-window-top");
    if(bar)bar.style.opacity=(1-smooth(Math.max(0,(t-.22)/.55))).toFixed(3);
    ghost.style.transform="translate3d("+(delta.x*t).toFixed(1)+"px,"+(delta.y*t).toFixed(1)+"px,0) scale("+(1+(delta.sx-1)*t).toFixed(4)+","+(1+(delta.sy-1)*t).toFixed(4)+")";
   },
   onLeave:()=>{ghost.style.visibility="hidden";destination.style.opacity="1";source.style.opacity="1"},
   onLeaveBack:()=>{ghost.style.visibility="hidden";destination.style.opacity="1";source.style.opacity="1"},
   invalidateOnRefresh:true
  });
 }
 ScrollTrigger.create({
  trigger:world,start:"top top",end:"bottom bottom",
  onUpdate:self=>frame(self.progress),onRefresh:self=>frame(self.progress),
  invalidateOnRefresh:true
 });
  const sectionTop=world.getBoundingClientRect().top+scrollY;
  const travel=Math.max(1,world.offsetHeight-innerHeight);
  frame(clamp((scrollY-sectionTop)/travel));access(active);
 if("requestIdleCallback" in window&&innerWidth>800&&innerHeight>600){
  requestIdleCallback(()=>scenes.slice(0,3).forEach(scene=>{
   const img=new Image();img.src=mediaFor(scene.states[0]);
  }));
 }
 return ()=>{
  handoffGhost?.remove();
  layers.forEach(l=>{
   for(const key of ["visibility","pointerEvents","clipPath","maskImage","webkitMaskImage","filter","opacity","transform","zIndex","background"])l.css[key]="";
   l.stage.transform="";l.stage.opacity="";l.stage.clipPath="";l.caption.opacity="";l.label.opacity="";
  });
  source?.style.removeProperty("opacity");destination?.style.removeProperty("opacity");
  rail.style.removeProperty("transform");
 };
 });
 configureResponsive();
 document.addEventListener("lv-motion-change",()=>{
  const worldStart=world.offsetTop;
  const preserveWorld=scrollY>=worldStart-innerHeight*.65&&scrollY<=worldStart+world.offsetHeight,rememberedScene=active;
  stopRoute();
  gsap.matchMediaRefresh();
  requestAnimationFrame(()=>{
   ScrollTrigger.refresh();
   if(preserveWorld){
    if(flowMode())slides[rememberedScene].scrollIntoView({behavior:"instant",block:"start"});
    else{
     const sectionTop=world.getBoundingClientRect().top+scrollY;
     const travel=Math.max(1,world.offsetHeight-innerHeight);
     window.scrollTo({top:sectionTop+travel*(rememberedScene/(slides.length-1)),behavior:"instant"});
    }
   }
  });
 });
}
