import {editorial} from "../src/editorial-v13.js";
// Direção artística local: mapas de decisão, nunca capturas inventadas.
// Conteúdo editorial verificado contra os dossiês V14. Números não comprovados não são usados.
const scenes={
"engenharia-de-dados-compass":{kind:"data",label:"01 / Engenharia de dados",title:"O gráfico é o fim da história. O trabalho começa antes.",lead:"Um registro vai da origem até uma resposta consultável. A vitrine mostra a saída; este percurso mostra por que ela existe.",words:["INGESTÃO","TRANSFORMAÇÃO","CONSULTA"],beats:[
["Receber e organizar","Arquivos e fontes precisam chegar com estrutura clara antes de qualquer gráfico.","Python · AWS S3"],
["Tratar para consultar","A preparação do dado separa a origem do formato que será analisado.","Python · AWS Glue"],
["Conferir o resultado","Consultas em Athena e uma visualização ajudam a verificar o que foi transformado.","Athena · Dashboard"]],bottom:"Capturas históricas do estágio, não apresentação de ambientes de clientes."},
"sites-industriais":{kind:"studio",label:"02 / Experiência web",title:"Engenharia também precisa ser compreendida na primeira visita.",lead:"Duas identidades comerciais; a mesma responsabilidade: tornar produtos, especificações e caminhos de contato fáceis de encontrar.",words:["Vesper · abertura","Catálogo · navegação","Vent Rio · outra marca"],beats:[
["Abertura com presença","A página da Vesper comunica o segmento e dá protagonismo ao equipamento.","Captura de site publicado"],
["Informação técnica navegável","Organizar produtos e soluções exige hierarquia, terminologia e conteúdo correto.","Conteúdo técnico · navegação"],
["Duas marcas, não duas cópias","A Vent Rio entra como contraponto para mostrar adaptação de identidade e conteúdo.","Captura de site publicado"]],bottom:"As empresas mantêm suas marcas; este case descreve atuação no desenvolvimento e manutenção."},
"compras-e-cotacoes":{kind:"workflow",label:"03 / Operação comercial",title:"Da entrada da solicitação ao acompanhamento da cotação.",lead:"A experiência acompanha três momentos da rotina: escolher a tarefa, registrar condições e acompanhar as respostas.",words:["ENTRADA","COTAÇÃO","ACOMPANHAMENTO"],beats:[
["Escolher a tarefa","A entrada distingue materiais, painéis, fretes e ordens de compra.","Menu de tarefas"],
["Registrar as condições","Material, medidas, anexos e transportadoras ficam reunidos antes da conferência.","Cotação · Frete"],
["Acompanhar respostas","A consulta organiza respostas e pendências; a captura mostra o estado sem cotações.","Acompanhamento · estado vazio"]],bottom:"Imagens demonstrativas; condições comerciais reais não aparecem."},
"tradutor-documental":{kind:"document",label:"04 / Documentos técnicos",title:"Tradução de documentos com estrutura e revisão.",lead:"Para um documento técnico, estilos, tabelas, ordem e terminologia fazem parte do resultado; a conferência é parte do processo.",words:["DOCX / ODT","TRADUÇÃO","ARQUIVO REVISTO"],beats:[
["Ler o documento como estrutura","Tabelas, parágrafos e estilos não podem ser tratados apenas como uma sequência de texto.","Entrada estruturada"],
["Aplicar tradução e terminologia","O processo mantém regras e consistência de termos recorrentes.","Tratamento local"],
["Revisar antes de entregar","O documento produzido exige testes de formato e leitura humana para casos especiais.","Saída conferível"]],bottom:"A tela exibida adiante é do software; este diagrama é explicativo."},
"gestao-de-propostas":{kind:"protected",label:"05 / Automação documental",title:"Modelos comerciais, revisão e geração de PDF.",lead:"Modelos e informações passam por preparação, revisão e conversão. O esquema apresenta o processo; as capturas protegidas ficam como consulta complementar.",words:["MODELO","REVISÃO","PDF"],beats:[
["Preparar o modelo","Um documento-base organiza elementos que serão reaproveitados.","ODT · Modelos"],
["Conferir dados e campos","Antes de gerar a saída, a consistência deve ser validada sem expor clientes.","Dados fictícios na explicação"],
["Gerar e revisar o PDF","A saída é um documento, não apenas uma tela preenchida.","Conversão · revisão"]],bottom:"Esquema ilustrativo. Capturas originais sanitizadas ficam em área separada."},
"videomind":{kind:"agent",label:"06 / IA aplicada à edição",title:"Edição de vídeo com ferramentas acionadas por outro agente.",lead:"O VideoMind já opera em conjunto com outro agente para executar cortes, legendas e exportação; a interface permanece em evolução e a saída exige revisão.",words:["PEDIDO","FERRAMENTAS","REVISÃO"],beats:[
["Instrução e integração","O agente parceiro recebe o objetivo e utiliza as ferramentas de edição disponíveis. A orquestração depende da integração.","Integração em funcionamento"],
["Ações sobre mídia","Cortes, legendas e exportação já podem ser executados em conjunto com o agente parceiro, com validação do resultado.","Operações integradas"],
["Revisão da saída","A timeline permite inspecionar mídia, camadas e montagem. Esta imagem comprova a interface, não mostra um agente executando comandos.","Captura real da timeline"]],bottom:"Integração real informada pelo autor; este screenshot isolado não prova autonomia irrestrita nem substituição completa de um editor."},
"brasil-as-claras":{kind:"civic",label:"07 / Informação cívica",title:"Da pergunta comum até o dado que pode ser conferido.",lead:"Uma pessoa não deveria conhecer o vocabulário do Congresso para entender uma votação. A proposta é apresentar fontes, contexto e ressalvas.",words:["PERGUNTA","EXPLICAÇÃO","FONTE"],beats:[
["Começar com uma pergunta","Por exemplo: como conferir o voto de um representante em uma proposta?","Exemplo ilustrativo"],
["Traduzir o dado público","Termos institucionais precisam de contexto e linguagem acessível.","Produto em desenvolvimento"],
["Verificar na origem","Diferenciar dado oficial, interpretação e conclusão evita julgamentos precipitados.","Câmara · Senado · TSE"]],bottom:"Em desenvolvimento, não lançado. O exemplo não constitui avaliação política."},
"arsenalmind":{kind:"architecture",label:"08 / Engenharia de agentes",title:"Capacidades, contexto e validação antes da execução.",lead:"Ferramentas descobertas, contratos definidos e verificações criam um caminho compreensível do pedido à execução.",words:["AGENTE","MCP / CAPACIDADES","VALIDAÇÃO"],beats:[
["Descobrir uma capacidade","O agente conhece as ferramentas disponíveis e como chamar cada uma.","Contrato de ferramenta"],
["Preservar contexto útil","Decisões e dados de trabalho orientam tarefas com múltiplas etapas.","Contexto · skills"],
["Aplicar limites","Entradas e acesso são verificados conforme a ferramenta; não existe promessa de segurança absoluta.","Políticas · validação"]],bottom:"Mapa das capacidades, contratos e limites de execução desenvolvidos para meu próprio ambiente de trabalho com agentes."},
"mala-direta":{kind:"workflow",label:"09 / Automação sob demanda",title:"Preparação e revisão antes da campanha.",lead:"A ferramenta organiza o preparo e a conferência antes da execução pontual.",words:["PREPARAR","CONFERIR","EXECUTAR"],beats:[
["Selecionar destinatários","Contatos e dados precisam de revisão antes de iniciar a campanha.","Lista e contexto"],
["Revisar mensagem e fila","A operação exige conferir conteúdo, destinatários e estado das mensagens.","Validação humana"],
["Acionar quando necessário","O fluxo atende solicitações específicas; não é disparo contínuo.","Execução sob demanda"]],bottom:"Não exibe contatos ou resultados de campanha reais."},
"gestao-de-locacao":{kind:"architecture",label:"10 / Software desktop",title:"Registro e consulta de locações no Windows.",lead:"A solução Windows organiza entrada, consulta e acompanhamento de locações em um fluxo único.",words:["REGISTRO","CONSULTA","ACOMPANHAMENTO"],beats:[
["Registrar a locação","A entrada consistente reduz a dispersão dos dados do processo.","C# · WPF"],
["Encontrar o registro","A interface desktop foi pensada para o ambiente de trabalho utilizado.","Busca e consulta"],
["Revisar a situação","O acompanhamento depende de registros recuperáveis e legíveis.","Fluxo empresarial"]],bottom:"Apresento a arquitetura e os fluxos desenvolvidos em C#/.NET e WPF. Dados comerciais e contratos da empresa são mantidos privados."},
"conversa360":{kind:"architecture",label:"11 / Mensageria",title:"Histórico e entrega de mensagens com estados definidos.",lead:"A arquitetura em evolução diferencia receber, guardar e entregar mensagens — inclusive quando existem falhas.",words:["RECEBER","PERSISTIR","ENTREGAR"],beats:[
["Recebimento e histórico","A mensagem precisa se relacionar com contatos e eventos anteriores.","Modelo previsto"],
["Estado confiável","Filas e outbox ajudam a tratar reprocessamento e falhas sem inventar entregas.","Arquitetura em desenvolvimento"],
["Integração verificável","O envio real depende da integração e homologação de cada serviço.","Pendente de validação"]],bottom:"Fluxo conceitual, não simulação de integração real concluída."},
"producao-operacional":{kind:"workflow",label:"Destaque / Produção",title:"A ordem começa no sistema. O acompanhamento chega à operação.",lead:"Informação de produção precisa circular entre quem registra, quem executa e quem acompanha o andamento.",words:["ORDEM","STATUS","MODO TV"],beats:[
["Registrar a ordem","Uma visão central de etapas e situações de produção.","Aplicativo operacional"],
["Atualizar o processo","A etapa da ordem precisa ser reconhecível pela equipe.","Acompanhamento"],
["Exibir para a equipe","O modo TV traduz o andamento em leitura coletiva.","Tela compartilhada"]],bottom:"Telas demonstrativas; nenhum dado operacional sigiloso é exibido."},
"manutencao-em-campo":{kind:"workflow",label:"Destaque / Manutenção",title:"Uma inspeção não pode perder o histórico do equipamento.",lead:"Tudo parte do ativo: localizar, inspecionar e recuperar o que já aconteceu.",words:["ATIVO","CHECKLIST","HISTÓRICO"],beats:[
["Identificar o ativo","A consulta do equipamento dá início a uma intervenção contextualizada.","Identificação"],
["Executar uma inspeção","Registros e checklist orientam o trabalho sem perder detalhes.","Campo"],
["Revisar o histórico","Informações passadas apoiam próximas decisões.","Rastreabilidade"]],bottom:"Aplicação desenvolvida para rotina operacional em campo; capturas apresentam dados de teste e ativos liberados."},
"belarc-inventory":{kind:"architecture",label:"Destaque / Infraestrutura",title:"O chamado não começa do zero quando a máquina já tem contexto.",lead:"Inventário de estações e acompanhamento de suporte fazem parte de uma mesma história de atendimento.",words:["ESTAÇÃO","INVENTÁRIO","CHAMADO"],beats:[
["Coletar o estado","Características do computador e informações de inventário formam o contexto.","Agente Windows"],
["Consolidar no servidor","Registros podem ser atualizados e consultados por suporte.","Servidor · sincronização"],
["Atender com contexto","Chamados e quadros de acompanhamento se relacionam com a máquina.","Trabalho em colaboração"]],bottom:"Co-desenvolvimento com Diogo Rodrigues; não é autoria individual exclusiva."},
"zero21fotos":{kind:"studio",label:"Destaque / Produto para fotógrafo",title:"Da emoção da fotografia à autonomia de quem publica.",lead:"Um site de eventos ligado à venda de fotos, acompanhado por painel administrativo e descoberta de novas coberturas.",words:["IDENTIDADE","DESCOBERTA","AUTONOMIA"],beats:[
["Apresentar quem fotografa","A página Sobre humaniza o projeto e constrói a identidade visual do profissional.","Página pública real"],
["Encontrar e acessar fotos","Filtros, busca e capas orientam a escolha. Um clique em cada evento leva à galeria na plataforma de venda.","Navegação real"],
["Manter a vitrine atualizada","Desenvolvi o painel privado para editar conteúdos e importar novos eventos sob demanda, reutilizando informações e capas existentes.","Painel privado de administração · mantido sob sigilo do cliente"]],bottom:"Capturas do site público. A administração é privada; uso de fotos sujeito à autorização do titular."},
"hubora":{kind:"studio",label:"Destaque / Produto digital",title:"Descobrir, escolher e guardar: três momentos da mesma biblioteca.",lead:"Filmes, séries e jogos ganham caminhos de navegação e uma coleção pessoal organizada.",words:["DESCOBRIR","DETALHES","BIBLIOTECA"],beats:[
["Descobrir um título","Navegação por categorias para reduzir a fricção da escolha.","Catálogo"],
["Examinar detalhes","A ficha dá contexto antes de adicionar à coleção.","Informação por mídia"],
["Organizar a biblioteca","O acervo pessoal pode ser consultado no dispositivo.","Aplicação web"]],bottom:"Capturas históricas; imagens de obras são de seus respectivos titulares."},
"carreirapessoal":{kind:"architecture",label:"Registro / Projeto pessoal",title:"Organizar candidaturas também é tratar informação.",lead:"Exploração de uma rotina própria com registros, etapas e versões de currículo.",words:["OPORTUNIDADE","DECISÃO","MATERIAL"],beats:[
["Registrar oportunidades","Agrupar dados em vez de procurar informações soltas.","Uso pessoal"],
["Acompanhar decisões","Acompanhar próximos passos e a continuidade de cada processo.","Organização"],
["Preparar versões","A ideia é facilitar recuperação e revisão de documentos.","Sem lançamento público"]],bottom:"Projeto pessoal, sem implantação comercial atestada."},
"postagem-redes":{kind:"history",label:"Arquivo / Experimento",title:"Nem toda automação permanece na versão final do processo.",lead:"Esta experiência serviu para explorar publicação e revisão de conteúdo, mas o fluxo recorrente foi descontinuado.",words:["EXPERIMENTAR","AVALIAR","ARQUIVAR"],beats:[
["Experimentar o fluxo","Exploração de integração entre tarefas de mídia e publicação.","Histórico"],
["Comparar com a prática","A revisão humana e outras ferramentas mudaram o fluxo.","Aprendizado"],
["Encerrar o experimento","O projeto é mantido como registro, não como automação ativa.","Descontinuado"]],bottom:"Registro histórico; não demonstrar como solução ativa."}
};
// The number of decisions follows the project, not a fixed three-card template.
const words={
 "producao-operacional":["ENTRADA","SETORES","TV","CONSULTA"],
 "manutencao-em-campo":["ATIVO","INSPEÇÃO","HISTÓRICO"],
 "belarc-inventory":["AGENTE / SERVIDOR","ATENDIMENTO"],
 "zero21fotos":["FOTÓGRAFO","EVENTO","ADMINISTRAÇÃO"],
 "hubora":["DESCOBERTA","BIBLIOTECA"],
 "arsenalmind":["DESCOBERTA","CONTRATO","CONTEXTO","LIMITES"],
 "gestao-de-locacao":["REGISTROS","WINDOWS"],
 "gestao-de-propostas":["MODELO","REVISÃO / PDF"],
 "compras-e-cotacoes":["ENTRADA","CONDIÇÕES","ACOMPANHAMENTO"],
 "tradutor-documental":["ESTRUTURA","REVISÃO"],
 "sites-industriais":["VESPER","VENT RIO"],
 "engenharia-de-dados-compass":["INGESTÃO","TRANSFORMAÇÃO","ANÁLISE"],
 "mala-direta":["PREPARAR","EXECUTAR"],
 "videomind":["PROTÓTIPO ATUAL","PRÓXIMAS INTEGRAÇÕES"],
 "carreirapessoal":["OPORTUNIDADES","DOCUMENTOS"],
 "brasil-as-claras":["ENTENDER","CONFERIR"],
 "conversa360":["COMPONENTES LOCAIS","ARQUITETURA","INTEGRAÇÕES"],
 "postagem-redes":["EXPERIMENTO","ESCOLHA ATUAL"]
};
const proof={
 "engenharia-de-dados-compass":["Python · AWS S3","Glue · PySpark","Athena · QuickSight"],
 "sites-industriais":["Site público · identidade Vesper","Site público · identidade Vent Rio"],
 "tradutor-documental":["DOCX · ODT · terminologia","Testes de formato · revisão"],
 "gestao-de-propostas":["Modelos ODT","Conferência · saída PDF"],
 "videomind":["Componentes e timeline em desenvolvimento","Operação por agentes ainda em construção"],
 "arsenalmind":["Registro de capacidades","Entradas e saídas","Informações entre etapas","Validação por ferramenta"],
 "gestao-de-locacao":["Fluxo documentado","C# · .NET · WPF"],
 "conversa360":["Componentes locais em desenvolvimento","Filas · outbox · estados","Homologação pendente por serviço"],
 "brasil-as-claras":["Produto ainda não lançado","Câmara · Senado · fontes eleitorais"],
 "carreirapessoal":["Ferramenta pessoal","Materiais revisados pelo próprio candidato"],
 "postagem-redes":["Registro histórico","Publicação manual no fluxo atual"]
};
const foot={
 "arsenalmind":"Mapa das capacidades que desenvolvi. Não representa uma interface gráfica do produto.",
 "gestao-de-locacao":"Fluxo documentado da aplicação. Não há captura pública autorizada dos registros empresariais.",
 "conversa360":"Componentes e arquitetura em desenvolvimento; integrações reais ainda dependem de homologação.",
 "zero21fotos":"Páginas públicas do site que desenvolvi. A administração e os dados do cliente permanecem privados.",
 "postagem-redes":"Registro de um experimento encerrado. Hoje faço a publicação manualmente.",
 "carreirapessoal":"Ferramenta pessoal para organizar candidaturas; sem promessa de aprovação ou contratação.",
 "sites-industriais":"Sites públicos; marcas e imagens pertencem às empresas e aos respectivos titulares.",
 "manutencao-em-campo":"Demonstração pública com dados fictícios, separada da versão utilizada na operação."
};
for(const [slug,entry] of Object.entries(editorial)){
 const scene=scenes[slug];
 if(!scene)continue;
 scene.title=entry.title;scene.lead=entry.story;
 scene.words=words[slug];
 scene.beats=entry.steps.map((step,i)=>[...step,proof[slug]?.[i]||scene.beats[i]?.[2]||entry.type]);
 if(foot[slug])scene.bottom=foot[slug];
}
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
export function renderDirection(slug){
 const x=scenes[slug];if(!x)throw Error("Direção ausente: "+slug);
 const steps=x.beats;
 const chapterTitles={"tradutor-documental":"Estrutura antes da tradução.","gestao-de-propostas":"Do modelo ao PDF.","videomind":"Da timeline às ações.","brasil-as-claras":"Entender e conferir.","arsenalmind":"Ferramentas com contratos claros.","gestao-de-locacao":"Registros de locação.","conversa360":"Manter o contexto da conversa.","carreirapessoal":"Retomar cada candidatura."};
 return `<section class="v14-direction v14-direction--${esc(x.kind)} v14-direction--${esc(slug)}" data-v14-direction aria-label="Como desenvolvi este projeto">
  <div class="v14-direction-intro"><span class="v14-direction-kicker">${esc(x.label)}</span><h2>${esc(chapterTitles[slug]||x.title)}</h2><p>${esc(x.lead)}</p></div>
  <div class="v15-direction-static"><dl>${steps.map(step=>`<div><dt>${esc(step[0])}</dt><dd>${esc(step[1])}</dd></div>`).join('')}</dl></div>
  <div class="v14-direction-stage"><div class="v14-beat-navigation" data-v15-count="${steps.length}" role="group" aria-label="Momentos deste trabalho">
   ${steps.map((step,i)=>`<button type="button" data-v14-beat data-title="${esc(step[0])}" data-detail="${esc(step[1])}" data-proof="${esc(step[2])}" aria-pressed="${i===0}" class="v14-beat-button${i===0?" is-selected":""}"><span>${String(i+1).padStart(2,"0")}</span><strong>${esc(x.words[i])}</strong><small>${esc(step[0])}</small></button>`).join("")}
  </div><div class="v14-beat-focus" aria-live="polite" aria-atomic="true"><div class="v14-beat-ornament" aria-hidden="true"><i></i><i></i><i></i></div><span class="v14-beat-marker">01 / ${String(steps.length).padStart(2,"0")}</span><h3 data-v14-beat-title>${esc(steps[0][0])}</h3><p data-v14-beat-detail>${esc(steps[0][1])}</p><span class="v14-beat-proof" data-v14-beat-proof>${esc(steps[0][2])}</span></div></div>
  <p class="v14-direction-foot"><span>VERSÃO E PRIVACIDADE</span>${esc(x.bottom)}</p>
 </section>`;
}
export const directionIds=Object.keys(scenes);
