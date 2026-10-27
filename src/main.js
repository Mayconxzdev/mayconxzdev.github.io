
import "./style.css";
import "./editorial-v2.css";
import "./lab-v3.css";
import "./v4-home.css";
import "./cinema.css";
import "./v8-world.css";
import "./v8-sections.css";
import "./v9-editorial.css";
import "./v10-performance.css";
import "./v11-design.css";
import "./v12-unified.css";
import "./v14-home.css";
import "./v15-stability.css";
import "./v15-final-polish.css";
import "./v16-cv-focus.css";
import {initHeroPreviewPicker} from "./v15-hero-preview.js";
import {initVisitorExperience} from "./v11-experience.js";
import {evidenceList} from "../scripts/evidence-map.mjs";
import {imageDimensions} from "./image-dimensions.js";
import {initMotionWorld} from "./v8-world.js";
import {initMobileCinema} from "./mobile-cinema.js";
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import {projects,cvList} from "./data.js";
import {editorial} from "./editorial-v13.js";

gsap.registerPlugin(ScrollTrigger);
document.documentElement.classList.add("js");

const $=s=>document.querySelector(s);
const $$=s=>Array.from(document.querySelectorAll(s));
const escapeHTML=(s)=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const clean=(s)=>String(s??"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase();
const safeSearch=x=>clean([x.name,x.kind,x.group,x.status,x.headline,x.summary,x.stack?.join(" ")].join(" "));
const nav=$("#nav"),toggle=$("#menu-toggle");
const closeMenu=(restoreFocus=false)=>{const wasOpen=nav.classList.contains("open");nav.classList.remove("open");toggle.setAttribute("aria-expanded","false");toggle.setAttribute("aria-label","Abrir menu");if(restoreFocus&&wasOpen)toggle.focus()};
toggle.addEventListener("click",()=>{const now=nav.classList.toggle("open");toggle.setAttribute("aria-expanded",String(now));toggle.setAttribute("aria-label",now?"Fechar menu":"Abrir menu")});
nav.addEventListener("click",e=>{if(e.target.closest("a"))closeMenu()});
document.addEventListener("keydown",e=>{if(e.key==="Escape")closeMenu(true)});
document.addEventListener("click",e=>{if(!nav.contains(e.target)&&!toggle.contains(e.target))closeMenu()});

const filterButtons=$$("[data-filter]");
let currentFilter="all", query="", includeFeatured=false;
const featured=new Set(["producao-operacional","manutencao-em-campo","belarc-inventory","zero21fotos","hubora"]);
const showAllButton=document.querySelector("#catalog-show-all");
const grid=$("#catalog-grid"),count=$("#result-count");
const v14Order=["engenharia-de-dados-compass","sites-industriais","compras-e-cotacoes","tradutor-documental","gestao-de-propostas","videomind","brasil-as-claras","arsenalmind","mala-direta","gestao-de-locacao","conversa360"];
const v14Ranks=new Map(v14Order.map((slug,index)=>[slug,index]));
function catalogVisual(p,priority=false){
 const shots=evidenceList(p.slug);
 const shot=p.slug==="zero21fotos"?(shots[1]||shots[0]):shots[0];
 if(!shot)return '<div class="v14-card-art v14-card-art--diagram"><span>ESTUDO TÉCNICO</span><strong>'+escapeHTML(p.name)+'</strong></div>';
 const privateReview=shot.source.includes("AUDITORIA PRIVADA");
 return '<div class="v14-card-art"><img src="'+escapeHTML(shot.src)+'" loading="lazy" decoding="async" alt="'+escapeHTML(shot.caption)+'" width="'+(imageDimensions[shot.src]?.[0]||1440)+'" height="'+(imageDimensions[shot.src]?.[1]||900)+'">'+(privateReview?'<span class="v14-card-evidence">REVISÃO LOCAL · NÃO LIBERADO</span>':'')+'</div>';
}
function catalogFeature(p,i){
 return '<article class="v14-feature" data-project="'+escapeHTML(p.slug)+'">'+
 '<a class="v14-feature-photo" href="/projetos/'+encodeURIComponent(p.slug)+'/" aria-label="Ver case '+escapeHTML(p.name)+'">'+catalogVisual(p,true)+'</a>'+
 '<div class="v14-feature-body"><span class="v14-feature-index">0'+(i+1)+' / SELEÇÃO DO ACERVO</span>'+
 '<div><div class="v14-feature-sub">'+escapeHTML(p.group)+'</div><h3>'+escapeHTML(p.name)+'</h3><p>'+escapeHTML(editorial[p.slug].lead)+'</p></div>'+
 '<a href="/projetos/'+encodeURIComponent(p.slug)+'/"><span>Explorar o trabalho</span><span aria-hidden="true">↗</span></a></div></article>';
}
function catalogCompact(p,i){
 return '<article class="v14-compact" data-project="'+escapeHTML(p.slug)+'">'+
 '<a class="v14-compact-art" href="/projetos/'+encodeURIComponent(p.slug)+'/" aria-label="Ver case '+escapeHTML(p.name)+'">'+catalogVisual(p)+'</a>'+
 '<div class="v14-compact-body"><span>'+escapeHTML(p.group)+' · '+String(i+1).padStart(2,"0")+'</span>'+
 '<h3>'+escapeHTML(p.name)+'</h3><p>'+escapeHTML(editorial[p.slug]?.lead||p.summary)+'</p>'+
 '<a href="/projetos/'+encodeURIComponent(p.slug)+'/">'+escapeHTML(editorial[p.slug]?.status||p.status)+' <span aria-hidden="true">↗</span></a></div></article>';
}
function showProjects(){
 const v14Results=projects.filter(p=>editorial[p.slug]?.priority!=="archive")
 .filter(p=>(currentFilter==="all"||p.kind===currentFilter)&&safeSearch(p).includes(clean(query))&&(includeFeatured||currentFilter!=="all"||clean(query)!==""||!featured.has(p.slug)))
 .sort((a,b)=>(v14Ranks.get(a.slug)??30)-(v14Ranks.get(b.slug)??30));
 const curated=currentFilter==="all"&&!clean(query)&&!includeFeatured;
 const primary=curated?v14Results.filter(p=>v14Ranks.has(p.slug)&&v14Ranks.get(p.slug)<3):[];
 const remaining=v14Results.filter(p=>!primary.includes(p));
 const lead=primary.length?'<div class="v14-selection">'+primary.map(catalogFeature).join("")+'</div>':'';
 const rest=remaining.length?'<div class="v14-catalog-rest">'+remaining.map((p,i)=>catalogCompact(p,i+primary.length)).join("")+'</div>':'';
 grid.innerHTML=lead+rest||'<p class="empty">Nenhum trabalho encontrado. Tente outra busca ou filtro.</p>';
 count.textContent=v14Results.length+" "+(v14Results.length===1?"trabalho":"trabalhos")+" disponíveis"+(curated?" além dos cinco destaques":"")+" · selecione uma área para filtrar";
 if(showAllButton){
  showAllButton.setAttribute("aria-pressed",String(includeFeatured));
  showAllButton.textContent=includeFeatured?"Mostrar só os outros trabalhos":"Incluir os cinco destaques";
 }
}
filterButtons.forEach(btn=>btn.addEventListener("click",()=>{
 currentFilter=btn.dataset.filter;
 filterButtons.forEach(b=>{const active=b===btn;b.classList.toggle("is-active",active);b.setAttribute("aria-pressed",String(active))});
 showProjects();
}));
$("#project-search").addEventListener("input",e=>{query=e.target.value;showProjects()});
showProjects();
if(showAllButton)showAllButton.addEventListener("click",()=>{includeFeatured=!includeFeatured;showProjects();});

const cvGrid=$("#cv-grid");
cvGrid.innerHTML=cvList.map(cv=>'<a class="cv-card'+(cv.featured?' featured':'')+'" href="/assets/cv/'+encodeURIComponent(cv.file)+'" target="_blank" rel="noopener" aria-label="Abrir PDF do currículo '+escapeHTML(cv.title)+'"><div class="cv-top"><span>'+escapeHTML(cv.tag)+'</span><span>PDF ↗</span></div><div class="cv-title">'+escapeHTML(cv.title)+'</div><div class="cv-end"><span>'+ (cv.featured?"Abrir currículo principal":"Visualizar PDF") +'</span><span aria-hidden="true">↗</span></div></a>').join("");

// Optional on case microsites; homepage now focuses on actual projects.
if(document.querySelector("#sim-next")){
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
}

const methods=[
 ["◎","Entender a necessidade.","Ouvir quem executa o processo, observar restrições e reconhecer exceções antes de escolher ferramentas."],
 ["⌘","Especificar o caminho.","Definir o que precisa acontecer, quais dados entram e como reconhecer que a solução funciona."],
 ["◇","Construir a solução.","Desenvolver interfaces, dados e integrações em etapas pequenas, conferindo o resultado de cada mudança."],
 ["✓","Validar o comportamento.","Testar o fluxo completo, conferir falhas e exceções e corrigir os problemas antes da entrega."],
 ["↗","Implantar, observar e evoluir.","Acompanhar a rotina de quem usa, orientar pessoas, registrar problemas e aprimorar o produto com responsabilidade."]
];
const methodLine=document.createElement("div");
methodLine.className="v8-method-path";
methodLine.setAttribute("aria-hidden","true");
methodLine.innerHTML='<div class="v8-method-path-track"><span class="v8-method-path-fill"></span></div>'+Array.from({length:5},(_,i)=>'<span class="v8-method-node" data-path-step="'+i+'">'+String(i+1).padStart(2,"0")+'</span>').join("");
document.getElementById("method-panel")?.insertBefore(methodLine,document.querySelector(".method-symbol"));
const methodButtons=$$("[data-method]");
function updateMethod(i,focus=false){
 const method=methods[i],panel=$("#method-panel");
 methodLine.style.setProperty("--path-complete",(i/4*100)+"%");
 methodLine.querySelectorAll(".v8-method-node").forEach((el,j)=>{el.classList.toggle("is-active",j===i);el.classList.toggle("is-done",j<i)});

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

function progress(){
 const max=document.documentElement.scrollHeight-innerHeight;
 $("#meter").style.width=(max>0?Math.min(100,Math.max(0,scrollY/max*100)):0)+"%";
}
window.addEventListener("scroll",progress,{passive:true});
window.addEventListener("resize",progress,{passive:true});
progress();
initMotionWorld();
initMobileCinema();
initHeroPreviewPicker();
  initVisitorExperience({cvList,updateMethod});
// Signals successful enhancement to the early, recoverable layout guard.
document.documentElement.classList.add("v15-ready");
