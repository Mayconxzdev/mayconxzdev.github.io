/* Arquivos já públicos no portfólio antigo + capturas do site ao vivo, 23-10-2026.
 * Nunca copiar screenshots do pacote privado automaticamente. */
const E=(name,src,caption,source="Captura pública de demonstração")=>({name,src,caption,source});
const mediaKey=src=>String(src).split("/").pop().replace(/\.[^.]+$/g,"").toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"");
export const evidenceIdFor=(slug,src)=>slug+"--"+mediaKey(src);
export const evidence={
 "producao-operacional":[
  E("Painel de dados","/assets/evidence/producao-relatorio-mensal-clientes-desfocados.webp","Painel de indicadores com dados de clientes desfocados; evidencia a visão geral da produção","Captura publicada do projeto · dados sensíveis desfocados"),
  E("Ordens de produção","/assets/evidence/producao-tela-inicial.png","Tela publicada com dados demonstrativos e estados de produção"),
  E("Acompanhamento na TV","/assets/evidence/producao-tv-foco.png","Visualização de acompanhamento na TV"),
  E("Setores e configuração","/assets/evidence/producao-personalizacao-setores.png","Configuração de setores, ordem e cores para adaptar a visualização da operação")
 ],
 "manutencao-em-campo":[
  E("Painel","/assets/evidence/campo-dashboard.webp","Visão do início da manutenção em campo"),
  E("Checklist","/assets/evidence/campo-checklist.webp","Seleção de equipamento para iniciar ou continuar uma inspeção; dados de demonstração"),
  E("Histórico","/assets/evidence/campo-historico.webp","Registro demonstrativo concluído com checklist respondido, responsáveis e evidência de manutenção")
 ],
 "belarc-inventory":[
  E("Inventário","/assets/evidence/belarc-inventario.jpg","Informações detalhadas de um inventário demonstrativo"),
  E("Painel","/assets/evidence/belarc-bi.jpg","Indicadores de chamados em ambiente demonstrativo; os números não são resultados da operação real"),
  E("Atendimento","/assets/evidence/belarc-portal.jpg","Formulário de chamado de suporte"),
  E("Kanban","/assets/evidence/belarc-kanban.jpg","Acompanhamento em quadro")
 ],
 "zero21fotos":[
  E("Fotógrafo em ação","/assets/live/zero21-fotografo-acao.webp","Foto original do fotógrafo em ação, publicada no site ZERO21FOTOS","Fotografia pública / ZERO21FOTOS"),
  E("Cavalgada Rancho do Elias","/assets/live/zero21-evento-cavalgada.webp","Capa pública de uma cobertura fotográfica do evento Rancho do Elias","Capa de evento pública / ZERO21FOTOS"),
  E("Cavalgada do Iguim","/assets/live/zero21-evento-show.webp","Capa pública de uma cobertura fotográfica do evento Iguim","Capa de evento pública / ZERO21FOTOS"),
  E("Página inicial","/assets/live/zero21-home.webp","Topo da homepage real de ZERO21FOTOS","Screenshot do site público em 23/10/2026"),
  E("Eventos","/assets/live/zero21-eventos.webp","Seção real de eventos e fotografias do cliente","Screenshot do site público em 23/10/2026"),
  E("Sobre","/assets/live/zero21-sobre.webp","Página Sobre do site original","Screenshot do site público em 23/10/2026"),
  E("Contato","/assets/live/zero21-contato.webp","Página de contato do site real","Screenshot do site público em 23/10/2026"),
  E("Celular","/assets/live/zero21-mobile.webp","Versão móvel da página inicial","Screenshot do site público em 23/10/2026")
 ],
 "hubora":[
  E("Início","/assets/evidence/hubora-home.webp","Página inicial registrada na documentação pública","Captura histórica publicada do projeto"),
  E("Biblioteca","/assets/evidence/hubora-library.webp","Biblioteca de filmes e outras mídias","Captura histórica publicada do projeto"),
  E("Jogos","/assets/evidence/hubora-games.webp","Catálogo e descoberta de jogos","Captura histórica publicada do projeto"),
  E("Detalhes","/assets/evidence/hubora-details.webp","Ficha de um título com sinopse e ações de biblioteca; não comprova acesso à obra ou streaming","Captura histórica publicada do projeto")
 ],
 "gestao-de-propostas":[
  E("Revisão sanitizada","/assets/evidence/proposta-revisao-sanitizada.webp","Documento em revisão com informações protegidas","Captura sanitizada"),
  E("Envio sanitizado","/assets/evidence/proposta-envio-sanitizada.webp","Fluxo de envio com dados empresariais protegidos","Captura sanitizada")
 ],
 "compras-e-cotacoes":[
  E("Entrada e tarefas","/assets/evidence/compras-painel-inicial.png","Entrada da demonstração: escolha entre cotação de material, painéis, frete e ordem de compra","Captura pública demonstrativa · dados fictícios"),
  E("Cotação de frete","/assets/evidence/compras-cotacao-frete.png","Formulário de material, medidas, anexos e seleção de transportadoras; nenhum envio é realizado no portfólio","Captura pública demonstrativa · formulário vazio"),
  E("Acompanhamento","/assets/evidence/compras-acompanhamento.png","Consulta de respostas e pendências, exibida sem cotações cadastradas; não representa resultados de compras","Captura pública demonstrativa · estado vazio")
 ],
 "tradutor-documental":[
  E("Interface de tradução","/assets/evidence/tradutor-interface-bilingue.png","Visão principal da ferramenta de tradução de documentos","Captura pública do projeto")
 ],
 "sites-industriais":[
  E("Vesper · página inicial","/assets/evidence/vesper-home-desktop.webp","Homepage desktop da Vesper com apresentação industrial","Página publicada; captura histórica"),
  E("Vesper · soluções","/assets/evidence/vesper-solutions.webp","Página de soluções industriais da Vesper","Página publicada; captura histórica"),
  E("Vent Rio · página inicial","/assets/evidence/ventrio-home-desktop.webp","Homepage desktop com a identidade visual da Vent Rio","Página publicada; captura histórica"),
  E("Vent Rio · soluções","/assets/evidence/ventrio-solutions.webp","Página de soluções da Vent Rio","Página publicada; captura histórica")
 ],
 "engenharia-de-dados-compass":[
  E("Painel analítico","/assets/evidence/compass-dashboard.webp","Análise de filmes no QuickSight: relação entre orçamento, receita e retorno sobre investimento; exercício do estágio","Captura histórica do case"),
  E("Processamento AWS","/assets/evidence/compass-runs-sanitized.webp","Histórico de execuções no AWS Glue; registro de processamento do exercício, não métrica de produção","Captura histórica · barra de identidade removida"),
  E("Consulta Athena","/assets/evidence/compass-athena-data-sanitized.webp","Consulta SQL no Athena à dimensão de filmes e seus resultados; evidência da saída consultável","Captura histórica · barra de identidade removida")
 ],
 "mala-direta":[
  E("Visão","/assets/evidence/mala-dashboard.webp","Panorama de campanhas com números fictícios; não são métricas reais de envio"),
  E("Preparar mensagem","/assets/evidence/mala-editor.webp","Mensagem, assinatura e anexos antes da revisão; campanha de demonstração com Empresa Exemplo, sem envio no portfólio","Captura pública de demonstração · dados fictícios"),
  E("Fila","/assets/evidence/mala-fila.webp","Lista demonstrativa de campanhas, estados e ações; não exibe destinatários ou mensagens reais")
 ],
 "postagem-redes":[
  E("Editor histórico","/assets/evidence/postagem-editor.webp","Interface histórica, não utilizada atualmente"),
  E("Fluxo histórico","/assets/evidence/postagem-actions.webp","Fluxo de automação experimental")
 ]
};
// Author-approved original portfolio screenshots, sha256 verified by scripts/public-media-approvals.json.
evidence["brasil-as-claras"]=[
 E("Visão geral desktop","/assets/portfolio-approved/brasil_as_claras_01_desktop.png","Homepage do protótipo cívico em desenvolvimento; ainda não lançado","Captura do produto autorizada pelo autor em 26/10/2026")
];
evidence["videomind"]=[
 E("Editor com timeline","/assets/portfolio-approved/videomind_ui_timeline.png","Timeline da ferramenta local com biblioteca e trilhas; edição por integração com outro agente, com operações e saída sujeitas à revisão","Captura do produto autorizada pelo autor em 26/10/2026")
];
// Screenshots of the website, not isolated client photos.
evidence["zero21fotos"]=[
 E("O fotógrafo e sua identidade","/assets/live/zero21-v15-sobre.webp","Página Sobre do site real: fotógrafo, identidade e proposta humana","Captura do site público em 24/10/2026"),
 E("Encontre seu evento","/assets/live/zero21-v15-eventos-entrada.webp","Abertura e catálogo: busca, categorias e acesso às coberturas","Captura do site público em 24/10/2026"),
 E("Galerias e coberturas","/assets/live/zero21-v15-eventos-catalogo.webp","Grade de eventos com capas reais, filtros e caminho para as galerias","Captura do site público em 24/10/2026")
];
export const evidenceList=(slug)=>(evidence[slug]||[]).map((shot,index)=>({...shot,id:evidenceIdFor(slug,shot.src),index}));
