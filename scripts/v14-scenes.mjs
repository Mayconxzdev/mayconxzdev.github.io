import{evidenceList}from "./evidence-map.mjs";
import{editorial}from "../src/editorial-v13.js";
import{imageDimensions}from "../src/image-dimensions.js";
import{renderDirection}from "./v14-direction.mjs";
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const modes={
 "engenharia-de-dados-compass":"data","sites-industriais":"studio","compras-e-cotacoes":"workflow",
 "tradutor-documental":"document","gestao-de-propostas":"protected","videomind":"agent",
 "brasil-as-claras":"civic","arsenalmind":"architecture","gestao-de-locacao":"architecture",
 "conversa360":"architecture","mala-direta":"workflow","producao-operacional":"workflow",
 "manutencao-em-campo":"workflow","belarc-inventory":"workflow",
 "zero21fotos":"studio","hubora":"studio","carreirapessoal":"architecture","postagem-redes":"history"
};
const sceneNotes={
 "engenharia-de-dados-compass":["O resultado precisa ser consultável","Processar antes de mostrar","Conferir o dado na origem"],
 "sites-industriais":["Identidade e catálogo industrial","Produtos e soluções ao alcance","Outra marca, outro posicionamento","Apresentação técnica organizada"],
 "compras-e-cotacoes":["Escolher a tarefa","Registrar condições e destinatários","Conferir respostas e pendências"],
 "tradutor-documental":["Uma ferramenta para documentos estruturados"],
 "videomind":["A timeline que acompanha a edição via outro agente"],
 "brasil-as-claras":["Um primeiro contato com a informação pública"],
 "zero21fotos":["O rosto e a história do fotógrafo","Buscar e selecionar coberturas","Acessar as galerias de eventos"],
 "hubora":["Descobrir conteúdo","Organizar a coleção","Explorar outra categoria","Consultar detalhes"],
 "mala-direta":["Panorama da campanha","Preparar a mensagem e os anexos","Conferir a fila"],
 "producao-operacional":["Consultar a ordem","Informar o chão de produção","Personalizar setores"],
 "belarc-inventory":["Estado do equipamento","Visão da operação de TI","Abrir um chamado","Acompanhar atendimento"],
 "manutencao-em-campo":["O ativo em primeiro lugar","Inspecionar com checklist","Revisitar o histórico"]
};
const micro={
data:["DADOS → ANÁLISE","Da ingestão à informação consultável.","O dashboard é a saída do percurso de preparação e consulta dos dados."],
studio:["WEB / EXPERIÊNCIA","Um produto que pode ser visitado.","Capturas das páginas públicas."],
workflow:["OPERAÇÃO / ETAPAS","Cada tela corresponde a uma decisão.","Telas da aplicação em diferentes momentos da rotina."],
agent:["AGENTES / FERRAMENTAS","Uma interface pensada para ser operada.","A integração com outro agente já opera tarefas de edição; os resultados continuam revisáveis."],
document:["DOCUMENTOS / PROCESSAMENTO","O documento importa tanto quanto o texto.","A estrutura de saída exige revisão, não apenas tradução."],
civic:["TECNOLOGIA CÍVICA","Informação pública com contexto.","Produto ainda em desenvolvimento; fonte e interpretação não são a mesma coisa."],
architecture:["ARQUITETURA / DECISÕES","Por trás da interface.","O trabalho é explicado pelos fluxos e contratos documentados."],
protected:["AUTOMAÇÃO DOCUMENTAL","Proteção de dados sem esconder o raciocínio.","As capturas sanitizadas são evidência complementar, não uma apresentação limpa."],
history:["EXPERIMENTO / HISTÓRICO","Um trabalho de aprendizado.","Não faz parte do fluxo profissional atual."]
};
export const getV14Mode=slug=>modes[slug]||"workflow";
export const getV14Story=slug=>editorial[slug];

function shotFigure(shot,i,active){
 const dim=imageDimensions[shot.src]||[1440,900];
 return '<figure class="v14-slide gallery-item" id="media-'+esc(shot.id||'')+'" data-evidence-id="'+esc(shot.id||'')+'" data-v14-shot="'+i+'"'+(active?'':' hidden')+'>'+
 '<button class="gallery-trigger" type="button" data-caption="'+esc(shot.name+" · "+shot.caption)+'" aria-label="Ampliar: '+esc(shot.name)+'">'+
 '<span class="v14-image-shell"><img src="'+esc(shot.src)+'" width="'+dim[0]+'" height="'+dim[1]+'" alt="'+esc(shot.caption)+'" decoding="async" '+(i?'loading="lazy"':'fetchpriority="high"')+'><span class="gallery-load-error" role="status" hidden>Imagem indisponível no momento. A legenda identifica este registro.</span></span>'+
 '</button><figcaption><strong>'+esc(shot.name)+'</strong><span>'+esc(shot.caption)+'</span><small>'+esc(shot.source)+'</small></figcaption></figure>';
}
function dialog(){
 return '<dialog id="evidence-dialog" class="evidence-dialog" aria-label="Imagem do projeto ampliada"><div class="dialog-shell">'+
 '<header class="dialog-head"><span>IMAGEM ORIGINAL / <span id="evidence-count">1</span></span><button id="evidence-close" type="button">Fechar ×</button></header>'+
 '<div class="dialog-image-shell"><img id="evidence-large" alt=""></div>'+
 '<footer class="dialog-navigation"><button id="evidence-prev" type="button" aria-label="Imagem anterior">← Anterior</button><span class="dialog-caption" id="evidence-caption"></span><button id="evidence-next" type="button" aria-label="Próxima imagem">Próxima →</button></footer></div></dialog>';
}
function focusedSingle(slug,story,shots,mode){
 const [prefix,headline,note]=micro[mode]||micro.document;
 return '<section class="case-gallery v14-gallery v14-gallery--focus" aria-label="Imagem principal do projeto">'+
 '<div class="v14-focus-evidence"><span>'+esc(prefix)+'</span><strong>01 captura · a interface completa</strong></div>'+
 '<div class="v14-frame v14-frame--'+mode+'">'+shots.map((s,i)=>shotFigure(s,i,i===0)).join("")+'</div>'+
 '<p class="v14-main-caption">'+esc(note)+' <span>Selecione a imagem para ampliar sem cortes.</span></p>'+dialog()+'</section>';
}
function galleryStory(slug,story,shots,mode){
 const [prefix,headline,note]=micro[mode]||micro.workflow;
 const titles={
  "engenharia-de-dados-compass":["O dado tratado chega à análise.","QuickSight, Glue e Athena em um exercício com dados de filmes."],
  "sites-industriais":["Duas marcas. Dois percursos.","Vesper e Vent Rio: páginas públicas para descobrir produtos e soluções industriais."],
  "compras-e-cotacoes":["Da entrada à resposta.","Escolha a tarefa, prepare a cotação e acompanhe o retorno."],
  "producao-operacional":["A produção vista de cada ponto.","Registro de ordens, visão dos setores e acompanhamento compartilhado."],
  "manutencao-em-campo":["Um ativo, todo o seu percurso.","Identificação, inspeção e histórico na mesma rotina."],
  "belarc-inventory":["Da estação ao atendimento.","Inventário e suporte se encontram no contexto do equipamento."],
  "zero21fotos":["O fotógrafo, o evento, a cobertura.","Identidade e descoberta no site público; venda na plataforma de fotos."],
  "hubora":["Descobrir. Guardar. Voltar.","Uma biblioteca pessoal para navegar entre filmes, séries e jogos."],
  "mala-direta":["Preparar antes de enviar.","Uma operação sob demanda, com revisão antes da execução."],
  "postagem-redes":["Um experimento encerrado.","Editor e automações históricas; o fluxo atual usa publicação manual."]
 };
 const [galleryTitle,galleryLead]=titles[slug]||[story.title,headline];
 const buttons=shots.map((sh,i)=>'<button type="button" class="v14-view-choice'+(i===0?' is-active':'')+'" data-v14-select="'+i+'" aria-pressed="'+(i===0?'true':'false')+'"><span>'+String(i+1).padStart(2,"0")+'</span><strong>'+esc(sh.name)+'</strong><small>'+esc((sceneNotes[slug]||[])[i]||sh.caption)+'</small></button>').join("");
 const view= '<section class="case-gallery v14-gallery v14-gallery--'+mode+'" aria-label="Capturas do projeto" data-v14-gallery="'+esc(slug)+'">'+
 '<div class="v14-gallery-head"><span>CAPTURAS DO TRABALHO</span><h2>'+esc(galleryTitle)+'</h2><p>'+esc(galleryLead)+'</p></div>'+
 '<div class="v14-media-layout"><div class="v14-picks" role="group" aria-label="Escolher captura do trabalho">'+buttons+'</div>'+
 '<div class="v14-frame">'+shots.map((s,i)=>shotFigure(s,i,i===0)).join("")+'</div></div>'+
 '<p class="v14-main-caption">'+esc(note)+' <span>Abra a imagem para ver a captura completa.</span></p>'+dialog()+'</section>';
 // Narrative length and reading depth follow each project.
 const steps=story.steps||[];
 const storyTitles={"producao-operacional":"A informação acompanha a ordem.","manutencao-em-campo":"Manutenção organizada por ativo.","belarc-inventory":"Inventário com contexto para o suporte.","engenharia-de-dados-compass":"Processar, consultar e conferir.","sites-industriais":"Conteúdo técnico que pode ser encontrado.","compras-e-cotacoes":"Organizar a decisão de compra.","hubora":"Uma biblioteca para retomar descobertas.","mala-direta":"Revisão antes de cada execução.","postagem-redes":"O que ficou do experimento."};
 const points='<ol data-v15-points="'+steps.length+'">'+steps.map((step,i)=>'<li><span>'+String(i+1).padStart(2,"0")+'</span><div><strong>'+esc(step[0])+'</strong><p>'+esc(step[1])+'</p></div></li>').join("")+'</ol>';
 const technical=story.narrativeLayout==="technical";
 const explain='<section class="v14-afterstory v15-narrative--'+esc(story.narrativeLayout||"journey")+'"><div><h2>'+esc(storyTitles[slug]||story.title)+'</h2><p>'+esc(story.story)+'</p></div>'+
 (technical?'<details class="v15-technical-notes"><summary>'+esc(story.notesLabel||"Ver decisões técnicas")+'</summary>'+points+'</details>':points)+'</section>';
 return view+(slug==="zero21fotos"?"":explain);
}
function protectedView(slug,story,shots){
 const [prefix,headline,note]=micro.protected;
 return '<section class="v14-protected-view"><div class="v14-protected-lead"><span>REGISTROS DE APOIO</span><h2>Capturas históricas, com informações protegidas.</h2><p>As telas abaixo são registros históricos de apoio. Mantive os desfoques para preservar informações comerciais.</p></div>'+
 '<details class="v14-protected-disclosure"><summary><span>REGISTROS PROTEGIDOS</span><strong>Conferir capturas sanitizadas</strong><span>↘</span></summary>'+
 '<p>Estas imagens ajudam a contextualizar a ferramenta, mas não substituem uma demonstração nítida com dados de exemplo.</p>'+
 '<div class="case-gallery v14-gallery v14-gallery--protected"><div class="v14-frame">'+shots.map((s,i)=>shotFigure(s,i,true)).join("")+'</div>'+dialog()+'</div></details></section>';
}
function zero21PrivateOperations(){
 return '<section class="v15-zero21-operations" aria-label="Bastidores técnicos e fluxo de eventos">'+
 '<div class="v15-zero21-operations-head"><span>ALÉM DA INTERFACE PÚBLICA</span><h2>Uma vitrine que o fotógrafo consegue manter.</h2><p>Além do site público, desenvolvi um painel privado para o fotógrafo atualizar a apresentação e os eventos.</p></div>'+
 '<div class="v15-zero21-operation-grid">'+
 '<article><span>01 / VISITANTE</span><h3>Encontra o evento</h3><p>Busca, filtros e capas ajudam a localizar a cobertura. O clique segue para o evento correspondente na plataforma de venda de fotos.</p></article>'+
 '<article><span>02 / ADMINISTRAÇÃO</span><h3>Edita sua presença</h3><p>O titular pode alterar textos, imagens de apresentação, perfil, links e Instagram por meio do painel administrativo privado.</p></article>'+
 '<article><span>03 / ATUALIZAÇÃO</span><h3>Importa novos eventos</h3><p>Um comando no painel busca novas coberturas na plataforma, recuperando os dados e a capa disponível para reduzir o cadastro manual.</p></article>'+
 '</div><p class="v15-zero21-disclaimer">O painel é privado: explico seu funcionamento sem expor telas ou dados administrativos do cliente.</p></section>';
}
export function renderV14Visual(p){
 const slug=p.slug,story=editorial[slug],shots=evidenceList(slug),mode=getV14Mode(slug);
 if(!story)throw Error("Missing editorial for "+slug);
 const direction=renderDirection(slug);
 const civicCredit=slug==='brasil-as-claras'?'<p class="v15-license-credit">Fotografia que aparece na captura da interface: Geraldo Magela / Agência Senado · <a href="https://creativecommons.org/licenses/by/2.0/" target="_blank" rel="noopener noreferrer">CC BY 2.0</a>. A captura é de uma versão do produto ainda em desenvolvimento.</p>':'';
 if(mode==="protected")return direction+protectedView(slug,story,shots);
 if(!shots.length)return direction;
 if(shots.length===1)return direction+focusedSingle(slug,story,shots,mode)+civicCredit;
 if(slug==="zero21fotos")return galleryStory(slug,story,shots,mode)+zero21PrivateOperations();
 return galleryStory(slug,story,shots,mode);
}
export function renderV14Nav(p){
 const hasShots=evidenceList(p.slug).length>0;
 return '<nav class="v11-case-route v14-route" aria-label="Percurso deste projeto">'+
 '<span>'+esc(editorial[p.slug].type).toUpperCase()+'</span><a href="#visao">'+(hasShots?"Experiência visual":"Como funciona")+'</a>'+
 '<a href="#autoria">Minha contribuição</a><a href="/#acervo">← Todos os trabalhos</a></nav>';
}
