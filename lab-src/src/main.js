
import "./style.css";
import "./mobile-refinement.css";
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import {projects,cvList} from "./data.js";

gsap.registerPlugin(ScrollTrigger);
document.documentElement.classList.add("js");
const $=s=>document.querySelector(s);
const $$=s=>Array.from(document.querySelectorAll(s));
const reduced=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const escapeHTML=(s)=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const clean=(s)=>String(s??"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase();
const safeSearch=x=>clean([x.name,x.kind,x.group,x.status,x.headline,x.summary,x.stack?.join(" ")].join(" "));
const nav=$("#nav"),toggle=$("#menu-toggle");
const closeMenu=()=>{nav.classList.remove("open");toggle.setAttribute("aria-expanded","false");toggle.setAttribute("aria-label","Abrir menu")};
toggle.addEventListener("click",()=>{const now=nav.classList.toggle("open");toggle.setAttribute("aria-expanded",String(now));toggle.setAttribute("aria-label",now?"Fechar menu":"Abrir menu")});
nav.addEventListener("click",e=>{if(e.target.closest("a"))closeMenu()});
document.addEventListener("keydown",e=>{if(e.key==="Escape")closeMenu()});

const filterButtons=$$("[data-filter]");
let currentFilter="all", query="";
const grid=$("#catalog-grid"),count=$("#result-count");
function showProjects(){
  const visible=projects.filter(p=>(currentFilter==="all"||p.kind===currentFilter)&&safeSearch(p).includes(clean(query)));
  grid.innerHTML=visible.length?visible.map((p,i)=>'<article class="catalog-item"><div class="catalog-item-top"><span>'+escapeHTML(p.group)+'</span><span>'+String(i+1).padStart(2,"0")+'</span></div><h3>'+escapeHTML(p.name)+'</h3><p>'+escapeHTML(p.summary)+'</p><a href="/projetos/'+encodeURIComponent(p.slug)+'/"><span>'+escapeHTML(p.status)+'</span><span aria-hidden="true">↗</span></a></article>').join(""):'<p class="empty">Nenhum trabalho encontrado. Tente outra busca ou filtro.</p>';
  count.textContent=visible.length+" "+(visible.length===1?"trabalho":"trabalhos")+" exibidos · estados declarados no case";
}
filterButtons.forEach(btn=>btn.addEventListener("click",()=>{
 currentFilter=btn.dataset.filter;
 filterButtons.forEach(b=>{const active=b===btn;b.classList.toggle("is-active",active);b.setAttribute("aria-pressed",String(active))});
 showProjects();
}));
$("#project-search").addEventListener("input",e=>{query=e.target.value;showProjects()});
showProjects();

const cvGrid=$("#cv-grid");
cvGrid.innerHTML=cvList.map(cv=>'<a class="cv-card'+(cv.featured?' featured':'')+'" href="/assets/cv/'+encodeURIComponent(cv.file)+'" target="_blank" rel="noopener" aria-label="Abrir PDF do currículo '+escapeHTML(cv.title)+'"><div class="cv-top"><span>'+escapeHTML(cv.tag)+'</span><span>PDF ↗</span></div><div class="cv-title">'+escapeHTML(cv.title)+'</div><div class="cv-end"><span>'+ (cv.featured?"Abrir currículo principal":"Visualizar PDF") +'</span><span aria-hidden="true">↗</span></div></a>').join("");

const stages=[
 {label:"ESTADO 01 / ENTRADA",title:"Nova solicitação recebida",detail:"Um registro fictício está pronto para ser analisado. Nenhum dado real é carregado.",state:"Aguardando validação",revision:"REV. 00",action:"Validar solicitação"},
 {label:"ESTADO 02 / VERIFICAÇÃO",title:"Informação validada",detail:"O formato e os campos essenciais do exemplo foram conferidos. Uma revisão está preparada para registro.",state:"Validação concluída",revision:"REV. 01",action:"Registrar alteração"},
 {label:"ESTADO 03 / REGISTRO",title:"Registro consistente",detail:"A alteração fictícia foi registrada uma única vez. O estado final pode ser consultado sem reenvio.",state:"Registro efetuado",revision:"REV. 01",action:"Testar duplicidade"},
 {label:"ESTADO 04 / PROTEÇÃO",title:"Duplicidade bloqueada",detail:"Uma segunda tentativa com a mesma identidade foi rejeitada pela simulação. O registro válido permanece preservado.",state:"Sem efeito duplicado",revision:"REV. 01",action:"Reiniciar ensaio"}
];
let simIndex=0,simManual=false;
const stageButtons=$$("[data-stage]");
function updateStage(next){
 simIndex=Math.max(0,Math.min(3,next));
 const stage=stages[simIndex];
 $("#stage-text").textContent=stage.label;
 $("#sim-title").textContent=stage.title;
 $("#sim-detail").textContent=stage.detail;
 $("#sim-state").textContent=stage.state;
 $("#sim-revision").textContent=stage.revision;
 $("#sim-next").innerHTML=escapeHTML(stage.action)+' <span aria-hidden="true">→</span>';
 $("#sim-announcement").textContent=stage.title+". "+stage.detail;
 $$(".flow-unit").forEach((el,i)=>{el.classList.toggle("active",i===Math.min(simIndex,2));el.classList.toggle("done",i<Math.min(simIndex,2))});
 $$(".flow-link").forEach((el,i)=>el.classList.toggle("complete",simIndex>i));
 stageButtons.forEach((b,i)=>{b.classList.toggle("is-active",i===Math.min(simIndex,2));b.setAttribute("aria-pressed",String(i===Math.min(simIndex,2)))});
}
stageButtons.forEach((b,i)=>b.addEventListener("click",()=>{simManual=true;updateStage(i)}));
$("#sim-next").addEventListener("click",()=>{simManual=true;updateStage(simIndex===3?0:simIndex+1)});
$("#sim-reset").addEventListener("click",()=>{simManual=true;updateStage(0)});
updateStage(0);

const methods=[
 ["◎","Entender a necessidade.","Ouvir quem executa o processo, observar restrições e reconhecer exceções antes de escolher ferramentas."],
 ["⌘","Especificar o caminho.","Traduzir contexto em requisitos, regras, interfaces, contratos e critérios de aceitação que possam ser verificados."],
 ["◇","Construir com agentes supervisionados.","Usar IA e ferramentas para acelerar a implementação, com direção, limites de acesso e contexto suficiente."],
 ["✓","Validar o comportamento.","Revisar diffs, testar falhas e estados inesperados, avaliar segurança e corrigir o que não funciona."],
 ["↗","Implantar, observar e evoluir.","Acompanhar a rotina de quem usa, orientar pessoas, registrar problemas e aprimorar o produto com responsabilidade."]
];
const methodButtons=$$("[data-method]");
function updateMethod(i,focus=false){
 const method=methods[i],panel=$("#method-panel");
 $("#method-symbol").textContent=method[0];
 $("#method-name").textContent=method[1];
 $("#method-description").textContent=method[2];
 $("#method-index").textContent=String(i+1).padStart(2,"0")+" / 05";
 methodButtons.forEach((b,n)=>{b.classList.toggle("is-active",i===n);b.setAttribute("aria-selected",String(i===n));b.tabIndex=i===n?0:-1});
 panel.setAttribute("aria-labelledby","tab-"+i);
 if(focus)methodButtons[i].focus();
}
methodButtons.forEach((b,i)=>{
 b.addEventListener("click",()=>updateMethod(i));
 b.addEventListener("keydown",e=>{if(["ArrowRight","ArrowDown","ArrowLeft","ArrowUp","Home","End"].includes(e.key)){e.preventDefault();let next=e.key==="Home"?0:e.key==="End"?4:(i+(["ArrowRight","ArrowDown"].includes(e.key)?1:4))%5;updateMethod(next,true)}});
});
updateMethod(0);

const observer=new IntersectionObserver(items=>{items.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add("is-visible");observer.unobserve(entry.target)}})},{threshold:0.07});
$$(".reveal").forEach(el=>observer.observe(el));

if(!reduced){
 gsap.from(".hero-copy > *",{opacity:0,y:25,duration:.85,stagger:.12,ease:"power3.out",delay:.12});
 gsap.from(".stage-primary",{opacity:0,y:75,rotation:-7,duration:1.2,ease:"power3.out",delay:.5});
 gsap.from(".stage-secondary",{opacity:0,y:95,scale:.85,duration:1,ease:"power3.out",delay:.9});
 gsap.from(".stage-code",{opacity:0,y:45,duration:.9,ease:"power3.out",delay:1.05});
 ScrollTrigger.matchMedia({
  "(min-width: 801px)":()=>{
    gsap.to(".hero-stage",{y:120,rotation:2,scrollTrigger:{trigger:".hero",start:"top top",end:"bottom top",scrub:1.1}});
    gsap.to(".stage-secondary",{y:-90,x:45,rotation:-4,scrollTrigger:{trigger:".hero",start:"top top",end:"bottom top",scrub:1.1}});
    gsap.to(".hero-glow",{x:-135,scrollTrigger:{trigger:".hero",start:"top top",end:"bottom top",scrub:1}});
    ScrollTrigger.create({trigger:".experience",start:"top 68%",end:"bottom 30%",onUpdate:self=>{if(!simManual)updateStage(Math.min(2,Math.floor(self.progress*3))) }});
  }
 });
 const statements=$$(".statement h2, .work-heading h2, .method-top h2, .archive-header h2, .resumes h2");
 statements.forEach(el=>gsap.from(el,{opacity:0,y:37,duration:.9,ease:"power2.out",scrollTrigger:{trigger:el,start:"top 90%",toggleActions:"play none none none"}}));
}
if(!reduced&&window.matchMedia("(min-width: 801px) and (pointer:fine)").matches){
 const visual=$(".hero-stage");
 const primary=$(".stage-primary"),secondary=$(".stage-secondary");
 const xShift=gsap.quickTo(primary,"x",{duration:0.7,ease:"power3.out"});
 const yShift=gsap.quickTo(primary,"y",{duration:0.7,ease:"power3.out"});
 visual.addEventListener("pointermove",e=>{
   const box=visual.getBoundingClientRect();
   const px=(e.clientX-box.left)/box.width-.5;
   const py=(e.clientY-box.top)/box.height-.5;
   xShift(px*28);yShift(py*22);
 });
 visual.addEventListener("pointerleave",()=>{xShift(0);yShift(0)});
 $$(".feature-image img").forEach(img=>gsap.fromTo(img,{yPercent:-3},{yPercent:3,ease:"none",scrollTrigger:{trigger:img.closest(".feature-image"),start:"top bottom",end:"bottom top",scrub:true}}));
}
function progress(){
 const max=document.documentElement.scrollHeight-innerHeight;
 $("#meter").style.width=(max>0?Math.min(100,Math.max(0,scrollY/max*100)):0)+"%";
}
window.addEventListener("scroll",progress,{passive:true});
window.addEventListener("resize",progress,{passive:true});
progress();