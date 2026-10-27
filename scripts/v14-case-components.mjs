import {evidenceList} from "./evidence-map.mjs";
import {renderGallery} from "./evidence-render.mjs";
import {editorial} from "../src/editorial-v13.js";
const esc = v => String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const designs={
 "engenharia-de-dados-compass":["pipeline","DADOS EM MOVIMENTO","Da origem à análise","O dashboard mostra o que o pipeline tornou consultável."],
 "sites-industriais":["web","DOIS NEGÓCIOS, DUAS IDENTIDADES","Produtos técnicos. Comunicação clara.","A Vesper abre a visita; a Vent Rio mostra outra solução de navegação e identidade."],
 "compras-e-cotacoes":["procurement","UMA COTAÇÃO POR VEZ","Registrar. Comparar. Acompanhar.","Da condição inicial até a continuidade do processo."],
 "tradutor-documental":["document","ARQUIVOS INTACTOS","Não basta trocar palavras.","Traduzir mantendo estrutura, tabelas e revisão."],
 "gestao-de-propostas":["document","DOCUMENTOS COMERCIAIS","Modelos que precisam continuar corretos.","Captura sanitizada: a recaptura com dados fictícios ainda é necessária."],
 "videomind":["studio","UM EDITOR PARA AGENTES","Meu agente precisa de ferramentas de edição.","Timeline registrada no desenvolvimento; a automação integral ainda está em evolução."],
 "brasil-as-claras":["civic","INFORMAÇÃO CÍVICA ACESSÍVEL","Entender antes de opinar.","Tela de desenvolvimento: linguagem simples, dados e fontes oficiais."],
 "arsenalmind":["architecture","FERRAMENTAS PARA AGENTES","Capacidades, contexto e limites.","Um componente técnico, não um aplicativo comercial."],
 "gestao-de-locacao":["desktop","OPERAÇÃO DE LOCAÇÕES","Uma ferramenta Windows feita para a rotina.","Sem captura divulgável: arquitetura e decisões, não uma interface inventada."],
 "conversa360":["architecture","ATENDIMENTO E CONTEXTO","Uma conversa precisa atravessar etapas.","Um projeto incompleto, com integrações pendentes."],
 "mala-direta":["workflow","CAMPANHAS SOB DEMANDA","Preparar antes de enviar.","O controle de envio começa na conferência."],
 "producao-operacional":["operations","ROTINA DE PRODUÇÃO","Da ordem ao acompanhamento coletivo.","Ordens, estados e comunicação visual entre setores."],
 "manutencao-em-campo":["field","INSPEÇÃO E HISTÓRICO","O ativo organiza o atendimento.","Visão, checklist e registro da manutenção."],
 "belarc-inventory":["infrastructure","TI COM CONTEXTO","A máquina e o chamado se encontram.","Inventário e atendimento construídos em colaboração."],
 "zero21fotos":["web","FOTOGRAFIA COMO CONTEÚDO","O evento é o caminho de descoberta.","A navegação do site real deve ser a protagonista."],
 "hubora":["media","BIBLIOTECA PESSOAL","Descobrir não é o mesmo que guardar.","Uma experiência para explorar e organizar mídias."],
 "carreirapessoal":["document","UM ORGANIZADOR PESSOAL","Informações e decisões num só lugar.","Registro histórico de uma ferramenta pessoal."],
 "postagem-redes":["studio","EXPERIMENTO ENCERRADO","Um aprendizado em automação de mídia.","Não é uma operação recorrente em uso."]
};
const get=p=>editorial[p.slug];
export const getEditorial=get;
export function renderCaseVisual(p){
 const item=get(p), shots=evidenceList(p.slug), [type,label,title,deck]=designs[p.slug];
 if(!shots.length){
  return '<section class="v14-architecture v14-theme-'+type+'"><div class="v14-art-head"><span>'+esc(label)+'</span><span>'+esc(item.status)+'</span></div><div class="v14-architecture-main"><div><small>POR QUE EXISTE</small><h2>'+esc(title)+'</h2><p>'+esc(item.story)+'</p></div><div class="v14-architecture-rail" id="decisoes" aria-label="Partes documentadas">'+
   item.steps.map((s,i)=>'<button type="button" class="v14-arch-step'+(i===0?' is-selected':'')+'" data-v14-step="'+i+'" data-v14-detail="'+esc(s[1])+'" aria-pressed="'+(i===0?'true':'false')+'"><span>'+String(i+1).padStart(2,"0")+'</span><strong>'+esc(s[0])+'</strong></button>').join("")+
   '<div class="v14-arch-detail" role="status">'+esc(item.steps[0][1])+'</div></div></div><p class="v14-arch-disclaimer">Fluxo documental baseado nas decisões do trabalho. Não é uma tela do software nem um serviço publicado.</p></section>';
 }
 const fullscreen=shots.length>1;
 const dialog=(renderGallery(p.slug).match(/<dialog id="evidence-dialog"[\s\S]*?<\/dialog>/)||[])[0]||"";
 const thumbs=shots.map((s,i)=>'<button type="button" class="v14-scene-choice'+(i===0?' is-selected':'')+'" data-v14-frame="'+i+'" data-origin="'+esc(s.source)+'" data-caption="'+esc(s.name+" — "+s.caption)+'" aria-pressed="'+(i===0?'true':'false')+'" aria-label="Selecionar e ampliar: '+esc(s.name)+'"><img src="'+esc(s.src)+'" alt="'+esc(s.caption)+'" loading="lazy"><span>'+String(i+1).padStart(2,"0")+' / '+esc(s.name)+'</span></button>').join("");
 const stock='<div class="v14-stock" hidden>'+shots.map(s=>'<button type="button" class="gallery-trigger" data-caption="'+esc(s.name+' — '+s.caption)+'"><img src="'+esc(s.src)+'" alt="'+esc(s.caption)+'"></button>').join("")+'</div>';
 const meta=shots[0].source;
 return '<section class="v14-scene v14-scene--'+type+' case-gallery" data-v14-scene>'+
   '<div class="v14-scene-head"><span>'+esc(label)+'</span><span>'+esc(item.status)+'</span></div>'+
   '<div class="v14-scene-intro"><div><span>VISTA DOCUMENTADA</span><h2>'+esc(title)+'</h2></div><p>'+esc(deck)+'</p></div>'+
   '<div class="v14-scene-stage"><div class="v14-scene-canvas"><img class="v14-scene-main" src="'+esc(shots[0].src)+'" alt="'+esc(shots[0].caption)+'" fetchpriority="high">'+
   '<div class="v14-scene-tint" aria-hidden="true"></div><span class="gallery-load-error" role="status" hidden>Esta captura não carregou. Use a legenda ou escolha outra imagem abaixo.</span></div><div class="v14-scene-aside"><span>O QUE ESTÁ NA TELA</span>'+
   '<h3 data-v14-title>'+esc(shots[0].name)+'</h3><p data-v14-caption>'+esc(shots[0].caption)+'</p>'+
   '<small data-v14-origin>'+esc(meta)+'</small>'+
   '<button type="button" class="v14-zoom" aria-label="Ampliar a imagem selecionada">Ampliar interface ↗</button></div></div>'+
   '<nav class="v14-scene-strip" aria-label="Escolher visualização do projeto">'+thumbs+'</nav>'+
   (shots.length===1?'<p class="v14-single">Uma captura relevante é suficiente; não repetimos imagens para preencher espaço.</p>':'')+
   (meta.toLowerCase().includes('privad')?'<p class="v14-local-warning">Captura do pacote mestre em revisão local. Não aprovada para publicação.</p>':'')+
   stock+dialog+'</section>';
}
export function renderStory(p){
 const entry=get(p), [type]=designs[p.slug];
 if(evidenceList(p.slug).length===0)return "";
 // Each context maps onto a distinct layout. One clear argument, no recycled question cards.
 return '<section class="v14-context v14-context--'+type+'" id="problema"><div class="v14-context-lead"><span>O QUE MOTIVOU ESTE TRABALHO</span><h2>'+esc(entry.title)+'</h2><p>'+esc(entry.story)+'</p></div><div class="v14-context-path" id="decisoes">'+
 entry.steps.map((s,i)=>'<article class="v14-context-part"><span>'+String(i+1).padStart(2,"0")+'</span><h3>'+esc(s[0])+'</h3><p>'+esc(s[1])+'</p></article>').join("")+
 '</div></section>';
}
export function renderCredit(p){
 const entry=get(p);
 return '<section class="v14-credits" id="autoria"><div><span>O QUE EU FIZ</span><h2>'+esc(entry.role)+'</h2><p>'+esc(entry.credit)+'</p></div><aside><span>O QUE É IMPORTANTE SABER</span><p>'+esc(entry.caution)+'</p><small>'+p.stack.map(esc).join(" · ")+'</small></aside></section>';
}
export function renderCaseNav(p){
 const has=evidenceList(p.slug).length>0;
 return '<nav class="v14-nav" aria-label="Navegar pelo trabalho"><span>'+esc(get(p).type)+'</span><a href="#visao">'+(has?"Interface":"Como funciona")+'</a><a href="#decisoes">Decisões</a><a href="#autoria">Minha participação</a><a href="/#acervo">← Acervo</a></nav>';
}
