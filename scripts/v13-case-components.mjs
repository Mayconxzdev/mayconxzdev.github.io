import{evidenceList}from "./evidence-map.mjs";
import{renderGallery}from "./evidence-render.mjs";
import{editorial}from "../src/editorial-v13.js";
const e=x=>String(x??"").replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
export const getEditorial=p=>editorial[p.slug];
export function renderCaseVisual(p){
 const story=getEditorial(p);
 if(!story)throw Error("Missing editorial " + p.slug);
 const shots=evidenceList(p.slug);
 if(shots.length)return '<div class="v13-real-captures"><div class="v13-evidence-caption"><span>REGISTROS DO TRABALHO</span><p>'+e(story.type)+' · '+e(story.status)+'</p></div>'+
 renderGallery(p.slug)
 .replace("Veja as telas reais.",shots.map(x=>x.name).slice(0,3).join(" · "))
 .replace("As imagens abaixo são capturas públicas do projeto ou da demonstração indicada. Clique para examinar sem cortar a interface.",
  shots[0].source.includes("privado")?"Capturas de trabalho local em desenvolvimento. A divulgação pública depende de revisão.":"Imagens reais ou demonstrativas, com fonte indicada. Abra para conferir a interface completa.")+'</div>';
 return '<section class="v13-no-screen"><div class="container"><div class="v13-no-screen-head"><span>'+e(story.type).toUpperCase()+'</span><span>'+e(story.status)+'</span></div>'+
 '<h2>'+e(story.title)+'</h2><p>'+e(story.story)+'</p><div class="v13-no-screen-steps" id="decisoes">'+
 story.steps.map((s,i)=>'<article><small>'+String(i+1).padStart(2,"0")+'</small><strong>'+e(s[0])+'</strong><p>'+e(s[1])+'</p></article>').join("")+
 '</div><div class="v13-no-screen-foot">Apresentação da arquitetura e das decisões registradas. Não é uma tela fictícia de um aplicativo.</div></div></section>';
}
export function renderStory(p){
 const story=getEditorial(p),hasShots=evidenceList(p.slug).length>0;
 if(!hasShots)return '<span class="sr-only" id="problema">Contexto e decisões apresentados acima.</span>';
 return '<section class="v13-story" id="problema"><div class="container"><div class="v13-story-intro"><span>POR DENTRO DO TRABALHO</span><h2>'+e(story.title)+'</h2><p>'+e(story.story)+'</p></div>'+
 '<div class="v13-steps" id="decisoes">'+story.steps.map((s,i)=>'<article class="v13-step"><span>'+String(i+1).padStart(2,"0")+'</span><h3>'+e(s[0])+'</h3><p>'+e(s[1])+'</p></article>').join("")+'</div></div></section>';
}
export function renderCredit(p){
 const story=getEditorial(p);
 const contextLabels={"producao-operacional":"Dados da demonstração","manutencao-em-campo":"Demonstração pública","belarc-inventory":"Dados do inventário","zero21fotos":"Privacidade do cliente","hubora":"Capas e fontes","engenharia-de-dados-compass":"Ambiente de estudo","compras-e-cotacoes":"Dados comerciais","tradutor-documental":"Revisão dos documentos","gestao-de-propostas":"Informações protegidas","videomind":"Em construção","brasil-as-claras":"Estado do projeto","arsenalmind":"Ferramenta local","mala-direta":"Execução sob demanda","gestao-de-locacao":"Acesso reservado","conversa360":"Estado da integração","carreirapessoal":"Uso pessoal","postagem-redes":"Registro histórico","sites-industriais":"Identidades das empresas"};
 return '<section class="v13-authorship" id="autoria"><div class="container"><div class="v13-credits-main"><div><span>MINHA PARTICIPAÇÃO</span><h2>'+e(story.role)+'</h2><p>'+e(story.credit)+'</p></div>'+
 '<aside class="v13-limits"><h3>'+e(contextLabels[p.slug]||"Sobre este trabalho")+'</h3><p>'+e(story.caution)+'</p></aside></div>'+
 '<div class="v13-credits-footer"><div><span>FERRAMENTAS / TECNOLOGIAS</span><p class="case-tech">'+p.stack.map(e).join(" · ")+'</p></div>'+
 '<div class="v13-links">'+[["Ver repositório",p.repository],["Abrir website",p.website]].filter(([,url])=>typeof url==="string"&&/^https:\/\//.test(url)).map(([txt,url])=>'<a href="'+e(url)+'" target="_blank" rel="noopener noreferrer">'+txt+' ↗</a>').join("")+'</div></div></div></section>';
}
export function renderCaseNav(p){
 const hasShots=evidenceList(p.slug).length>0,entry=getEditorial(p);
 const l1=hasShots?"Ver imagens":"Como funciona";
 return '<nav class="v11-case-route v13-case-route" aria-label="Conteúdo deste trabalho">'+
 '<span>'+e(entry.type).toUpperCase()+'</span><a href="#visao">'+l1+'</a>'+
 '<a href="#decisoes">Decisões</a><a href="#autoria">Minha participação</a>'+
 '<a href="/#acervo">← Acervo</a></nav>';
}
