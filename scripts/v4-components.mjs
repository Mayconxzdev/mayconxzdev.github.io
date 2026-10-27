import {imageDimensions} from "../src/image-dimensions.js";
import {evidenceList} from "./evidence-map.mjs";
const e=(str)=>String(str??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
function imageBox(item,variant){
 const [w,h]=imageDimensions[item.src]||[];if(!w||!h)throw Error("Missing media size: "+item.src);
 return '<figure class="v4-proof v4-proof--'+variant+'"><div class="v4-proof-media"><img src="'+e(item.src)+'" alt="'+e(item.caption)+'" width="'+w+'" height="'+h+'" loading="lazy" decoding="async"></div><figcaption><strong>'+e(item.name)+'</strong><span>'+e(item.source)+'</span></figcaption></figure>';
}
export function renderCaseStage(p){
 const assets=evidenceList(p.slug);
 if(p.slug==="zero21fotos"){
  const home="/assets/live/zero21-home-contexto.webp";
  const events="/assets/live/zero21-eventos.webp";
  return '<div class="v8-client-showcase" aria-label="Páginas reais do site ZERO21FOTOS">'+
  '<div class="v8-client-intro"><span>WEBSITE / EVIDÊNCIA REAL</span><h2>O trabalho está no site.</h2><p>A homepage apresenta o fotógrafo e direciona o visitante aos eventos. A página seguinte organiza as coberturas e facilita encontrar as galerias.</p></div>'+
  '<div class="v8-client-frames">'+
  '<figure class="v8-client-main"><img src="'+home+'" alt="Homepage real da ZERO21FOTOS com menu de navegação, fotógrafo e início dos eventos" width="1440" height="850" loading="eager"><figcaption><strong>01 / Página inicial</strong><small>Identidade, navegação e acesso aos eventos</small></figcaption></figure>'+
  '<figure class="v8-client-second"><img src="'+events+'" alt="Página real de eventos com filtros e coberturas fotográficas" width="1440" height="470" loading="lazy"><figcaption><strong>02 / Eventos</strong><small>Organização das coberturas e descoberta das galerias</small></figcaption></figure>'+
  '</div><p class="v8-client-foot">Capturas de páginas públicas do projeto. As fotografias do cliente são apresentadas como evidência, sujeitas à revisão de direitos de uso.</p></div>';
 }
 if(assets.length>=2){
  const [a,b]=assets;
  return '<div class="v4-stage v4-stage--screens"><div class="v4-stage-heading"><span>VISÃO RÁPIDA / '+e(p.group)+'</span><strong>'+e(p.headline)+'</strong></div><div class="v4-stage-screens">'+imageBox(a,"primary")+imageBox(b,"secondary")+'</div><p class="v4-stage-note">Duas perspectivas do mesmo trabalho. As capturas exibem interfaces publicadas ou ambientes demonstrativos, conforme indicação.</p></div>';
 }
 if(assets.length===1) return '<div class="v4-stage v4-stage--single">'+imageBox(assets[0],"primary")+'</div>';
 const frameNames={
  arsenalmind:"Como controlar agentes e ferramentas sem perder rastreabilidade?",
  "brasil-as-claras":"Como explicar informações cívicas com fontes verificáveis?",
  carreirapessoal:"Como organizar decisões de candidatura e currículo?",
  conversa360:"Como preservar contexto e continuidade das conversas?",
  "gestao-de-locacao":"Como acompanhar locações sem registros espalhados?",
  videomind:"Como organizar o processamento de vídeos com ferramentas locais?"
 };
 const name=frameNames[p.slug]||p.problem;
 return '<div class="v4-stage v4-stage--documented v12-documented">'+
 '<div class="v12-documented-top"><span>ESTUDO DOCUMENTADO / SEM CAPTURA PÚBLICA AUTORIZADA</span><strong>'+e(p.group)+'</strong></div>'+
 '<div class="v12-doc-lead"><h2>'+e(name)+'</h2><span class="v12-doc-status">'+e(p.status)+'</span></div>'+
 '<div class="v12-doc-two"><div><span>NECESSIDADE</span><p>'+e(p.problem)+'</p></div>'+
 '<div><span>ABORDAGEM</span><p>'+e(p.solution)+'</p></div></div>'+
 '<div class="v12-doc-decisions"><span>DECISÕES REGISTRADAS</span><ul>'+(p.decisions||[]).slice(0,2).map(t=>'<li>'+e(t)+'</li>').join('')+'</ul></div>'+
 '<small>Apresentação documental, não uma captura de software. A página detalha autoria, estágio, limitações e fontes disponíveis.</small></div>';

}
export function renderCaseJump(p){ return ""; }
export function caseProfile(p){
 const state=/não lançado|incompleto|desenvolvimento|estudo técnico|histórico|anterior/i.test(p.status)?"Em estudo / histórico":/uso|operação|acessível|publicado|funcional/i.test(p.status)?"Trabalho realizado":"Escopo documentado";
 return '<div class="v4-profile"><span>'+e(p.group)+'</span><span>'+e(state)+'</span><span>'+e(p.role)+'</span></div>';
}
