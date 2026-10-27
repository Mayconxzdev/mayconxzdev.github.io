import {caseCopy} from "./v4-copy.js";

export const cvList=[
 {id:"general_pt",title:"Sistemas, automação e IA aplicada",file:"Maycon_Ferreira_Geral_Automacao_IA_PT.pdf",tag:"GERAL · PT-BR",featured:true},
 {id:"agents_pt",title:"Desenvolvimento e automação com IA",file:"Maycon_Ferreira_Agentes_Automacao_n8n_PT.pdf",tag:"PYTHON · n8n · APIs · MCP",featured:false},
 {id:"creative_pt",title:"Produtos digitais e conteúdo com IA",file:"Maycon_Ferreira_Produtos_Conteudo_IA_PT.pdf",tag:"WEB · AUDIOVISUAL · AUTOMAÇÃO",featured:false}
];

export const projects=[
  {
    "slug": "producao-operacional",
    "name": "Produção Operacional",
    "kind": "operacao",
    "group": "Software operacional",
    "status": "Uso operacional interno",
    "role": "Desenvolvimento principal",
    "headline": "Da ordem de produção ao acompanhamento de cada etapa.",
    "summary": "Ordens, etapas, setores e acompanhamento visual reunidos numa mesma rotina.",
    "problem": "O escritório e a produção precisam saber qual ordem está em andamento, em qual setor e o que mudou desde a última atualização.",
    "solution": "Organizei o fluxo em estados, telas de consulta, relatórios e um painel de acompanhamento para a rotina operacional.",
    "decisions": [
      "Registrar sem duplicar: Organizei a entrada das ordens com validação e prevenção de duplicidades.",
      "Acompanhar por setor: Separei estados, etapas e consultas para a equipe localizar o que está em andamento.",
      "Levar a informação à TV: O painel compartilhado permite acompanhar o andamento sem abrir cada registro.",
      "Consultar depois: Relatórios e histórico apoiam a conferência quando uma ordem muda ou precisa ser revisitada."
    ],
    "roleDetail": "Conduzi a análise da rotina, o desenvolvimento do aplicativo Windows e os ajustes durante a implantação.",
    "limitations": "Uso capturas de demonstração e dados sanitizados para preservar ordens, clientes e indicadores internos.",
    "stack": [
      "Python",
      "PySide6",
      "SQLite",
      "Relatórios"
    ],
    "img": "/assets/evidence/producao-relatorio-mensal-clientes-desfocados.png",
    "imageLabel": "Captura pública de demonstração com conteúdo sanitizado",
    "repository": "https://github.com/Mayconxzdev/ProducaoOperacional",
    "legacy": "/cases/producao-operacional/"
  },
  {
    "slug": "manutencao-em-campo",
    "name": "Manutenção em Campo",
    "kind": "operacao",
    "group": "Operação industrial",
    "status": "Em uso na operação",
    "role": "Desenvolvimento principal",
    "headline": "O equipamento é o ponto de partida.",
    "summary": "Ativos, inspeções e histórico, do campo até a consulta de registros.",
    "problem": "Sem identificação e histórico organizados, cada inspeção exige procurar dados em lugares diferentes.",
    "solution": "Reuni equipamentos, ordens, checklists e registros de inspeção numa experiência voltada ao uso em campo.",
    "decisions": [
      "Identificação no campo: A consulta do ativo e o QR Code dão contexto antes de iniciar o registro.",
      "Checklist com evidências: Reuni inspeção, anexos e observações para que o registro acompanhe o serviço.",
      "Histórico para a próxima visita: Mantive os registros ligados ao equipamento para recuperar o que já aconteceu."
    ],
    "roleDetail": "Conduzi o desenvolvimento e a evolução da ferramenta conforme as necessidades da rotina operacional.",
    "limitations": "A demonstração pública usa dados fictícios e pode ter recursos diferentes da versão interna.",
    "stack": [
      "Python",
      "FastAPI",
      "SQLite",
      "Web responsiva"
    ],
    "img": "/assets/evidence/campo-dashboard.webp",
    "imageLabel": "Imagem pública sanitizada da apresentação de ativos",
    "repository": "https://github.com/Mayconxzdev/ManutencaoEmCampo",
    "legacy": "/cases/manutencao-campo/"
  },
  {
    "slug": "belarc-inventory",
    "name": "Belarc Inventory",
    "kind": "operacao",
    "group": "Infraestrutura & suporte",
    "status": "Ferramenta interna",
    "role": "Co-desenvolvimento com Diogo Rodrigues",
    "headline": "Antes do chamado, entender a máquina.",
    "summary": "Inventário Windows e atendimento de TI vistos como partes da mesma operação.",
    "problem": "O suporte precisa consultar informações consistentes sobre equipamentos, mudanças e atendimentos.",
    "solution": "O trabalho integra coleta por agente, recebimento por serviço e interfaces para inventário e atendimento.",
    "decisions": [
      "Do agente ao servidor: Separamos a coleta no Windows da recepção e consulta dos registros, considerando computadores sem comunicação ou com dados desatualizados.",
      "Do inventário ao atendimento: Ligamos as informações técnicas ao fluxo de chamados, para reduzir consultas dispersas durante o suporte."
    ],
    "roleDetail": "Co-desenvolvi a solução com Diogo Rodrigues, da organização do inventário aos fluxos de suporte.",
    "limitations": "As telas usam dados de demonstração. O parque real de computadores permanece privado.",
    "stack": [
      "Rust",
      "Axum",
      "SQLite",
      "Windows"
    ],
    "img": "/assets/evidence/belarc-inventario.jpg",
    "imageLabel": "Captura demonstrativa publicada de inventário com dados fictícios",
    "repository": "https://github.com/Mayconxzdev/Belarc-Inventory",
    "legacy": "/cases/belarc-inventory/"
  },
  {
    "slug": "zero21fotos",
    "name": "ZERO21FOTOS",
    "kind": "web",
    "group": "Produto para cliente",
    "status": "Site publicado",
    "role": "Desenvolvimento freelance",
    "headline": "O público encontra o evento. O fotógrafo mantém a vitrine.",
    "summary": "Site de fotografia com busca de eventos, acesso às galerias de venda e painel privado para manter o conteúdo.",
    "problem": "As fotos precisam aparecer no contexto de cada evento, com uma navegação que funcione também no celular.",
    "solution": "Desenvolvi páginas de apresentação, catálogo de eventos e acesso às galerias, com foco na experiência de quem procura uma cobertura.",
    "decisions": [
      "Identidade do fotógrafo: Desenvolvi páginas para apresentar seu trabalho, sua história e as coberturas.",
      "Eventos e galerias: Organizei busca, filtros e capas; cada evento leva à sua galeria na plataforma de venda de fotos.",
      "Manutenção do conteúdo: Criei o painel privado para editar o site e buscar novos eventos sob demanda, reutilizando dados e capas."
    ],
    "roleDetail": "Desenvolvi a experiência pública, o painel administrativo e a integração de atualização de eventos como trabalho freelance para cliente.",
    "limitations": "Mostro somente páginas públicas. O painel do cliente e seus dados administrativos ficam privados; os direitos das fotografias pertencem aos respectivos titulares.",
    "stack": [
      "HTML",
      "CSS",
      "JavaScript",
      "API HTTP/JSON"
    ],
    "img": "/assets/live/zero21-home.webp",
    "imageLabel": "Screenshot da página pública real em 23/10/2026",
    "website": "https://zero21fotos.com.br/"
  },
  {
    "slug": "hubora",
    "name": "Hubora",
    "kind": "web",
    "group": "Produto web",
    "status": "Publicado e acessível",
    "role": "Projeto pessoal apresentado na Casa Firjan",
    "headline": "Da descoberta à biblioteca pessoal.",
    "summary": "Buscar, descobrir e organizar filmes, séries e jogos num acervo pessoal.",
    "problem": "Interesses espalhados em plataformas diferentes tornam difícil acompanhar o que foi visto, salvo ou descoberto.",
    "solution": "Projetei uma biblioteca pessoal navegável, com pesquisa, fontes externas e armazenamento no dispositivo.",
    "decisions": [
      "Navegar antes de escolher: Organizei categorias e páginas de detalhes respeitando as diferenças entre cada tipo de mídia.",
      "Guardar e retomar: A biblioteca fica no dispositivo, permitindo reencontrar conteúdos salvos em uma experiência responsiva."
    ],
    "roleDetail": "Concebi e desenvolvi a aplicação web/PWA como projeto pessoal e trabalho final da formação.",
    "limitations": "As capturas registram uma versão do produto; as capas são de seus titulares. A apresentação na Casa Firjan fez parte da formação, sem homologação institucional do aplicativo.",
    "stack": [
      "React",
      "TypeScript",
      "Vite",
      "IndexedDB"
    ],
    "img": "/assets/evidence/hubora-library.webp",
    "imageLabel": "Captura histórica publicada da biblioteca Hubora; capas de terceiros aparecem no contexto da interface",
    "repository": "https://github.com/Mayconxzdev/Hubora",
    "website": "https://hubora.netlify.app/"
  },
  {
    "slug": "arsenalmind",
    "name": "ArsenalMind",
    "kind": "ia",
    "group": "IA e engenharia de contexto",
    "status": "Ferramenta pessoal local",
    "role": "Desenvolvimento pessoal",
    "headline": "Dar ao agente uma ferramenta e um contrato para usá-la.",
    "summary": "Ferramentas e contexto organizados para os agentes que uso no meu trabalho.",
    "problem": "Uma ferramenta disponível não significa que toda ação é adequada. Contexto, entradas e efeitos precisam ser compreendidos.",
    "solution": "Desenhei contratos e verificações para estudar como agentes consultam e acionam ferramentas sob revisão.",
    "decisions": [
      "Descoberta: Registro capacidades e instruções para que o agente encontre a ferramenta adequada.",
      "Contrato: Defino entradas e saídas para tornar a chamada verificável.",
      "Contexto: Guardo decisões e informações úteis entre etapas da tarefa.",
      "Limites: Valido entradas e destinos de rede conforme cada ferramenta. Essas verificações reduzem riscos, mas não garantem segurança absoluta."
    ],
    "roleDetail": "Desenvolvi o núcleo e as integrações da ferramenta para meu próprio fluxo de trabalho.",
    "limitations": "Esta apresentação é um mapa das capacidades documentadas. A ferramenta é local e pessoal; não há interface SaaS ou auditoria independente de segurança.",
    "stack": [
      "MCP",
      "TypeScript",
      "Node.js",
      "Segurança"
    ],
    "img": "",
    "imageLabel": "Sem screenshot público autorizado nesta edição"
  },
  {
    "slug": "gestao-de-locacao",
    "name": "Gestão de Locação",
    "kind": "operacao",
    "group": "Software desktop",
    "status": "Ferramenta construída para empresa",
    "role": "Desenvolvimento principal",
    "headline": "Registrar e consultar locações no Windows.",
    "summary": "Registro e consulta de locações em uma interface Windows própria.",
    "problem": "A rotina de locação exige manter registros consultáveis e reduzir retrabalho na organização de arquivos.",
    "solution": "Estruturei uma interface desktop e um modelo de dados orientados às consultas e aos registros dessa rotina.",
    "decisions": [
      "Registros recuperáveis: Reuni as informações para facilitar entrada, consulta e acompanhamento, incluindo revisão e exportação.",
      "Aplicação para o ambiente de trabalho: Escolhi uma interface Windows adequada aos computadores utilizados na operação."
    ],
    "roleDetail": "Desenvolvi a aplicação para uma necessidade empresarial específica.",
    "limitations": "Apresento o fluxo documentado porque não há captura pública autorizada da aplicação. Não exponho contratos ou dados comerciais.",
    "stack": [
      "C#",
      ".NET",
      "WPF",
      "SQLite"
    ],
    "img": "",
    "imageLabel": "Sem captura de produção autorizada"
  },
  {
    "slug": "gestao-de-propostas",
    "name": "Gestão de Propostas",
    "kind": "operacao",
    "group": "Automação documental",
    "status": "Ferramenta de uso interno",
    "role": "Desenvolvimento principal",
    "headline": "Propostas comerciais com modelos, revisão e saída em PDF.",
    "summary": "Modelos de proposta, preenchimento, revisão e geração de PDF.",
    "problem": "Preparar documentos comerciais envolve etapas repetidas, mas não pode abrir mão da revisão dos dados e da formatação.",
    "solution": "Separei preenchimento, validação e conversão para manter o controle sobre o documento gerado.",
    "decisions": [
      "Reaproveitar os modelos: Preservei os documentos-base e suas regras de preenchimento.",
      "Conferir antes de enviar: Separei preenchimento, revisão e geração do PDF, mantendo a conferência das informações comerciais."
    ],
    "roleDetail": "Desenvolvi a ferramenta de automação documental para uso interno.",
    "limitations": "As capturas históricas têm desfoques para proteger informações comerciais. Uma demonstração nítida com dados de exemplo ainda depende de preparação autorizada.",
    "stack": [
      "Python",
      "PySide6",
      "ODT",
      "PDF"
    ],
    "img": "",
    "imageLabel": "Demonstração editorial sem arquivos reais"
  },
  {
    "slug": "compras-e-cotacoes",
    "name": "Compras e Cotações",
    "kind": "operacao",
    "group": "Operação comercial",
    "status": "Ferramenta de uso interno",
    "role": "Desenvolvimento principal",
    "headline": "Preparar a cotação e acompanhar a resposta.",
    "summary": "Fornecedores, cotações, fretes e acompanhamento em uma rotina consultável.",
    "problem": "Informações de pedidos, fretes e fornecedores se tornam difíceis de comparar quando ficam dispersas.",
    "solution": "Organizei telas de consulta e comparação, com estados e validações para apoiar o acompanhamento.",
    "decisions": [
      "Entrada: Separei as tarefas para que o usuário escolha o tipo de cotação antes de preencher informações.",
      "Condições: Reuni materiais, medidas, anexos e destinatários na preparação da solicitação.",
      "Acompanhamento: Organizei a consulta de respostas e pendências. A captura de acompanhamento mostra um estado vazio demonstrativo."
    ],
    "roleDetail": "Desenvolvi e ajustei ferramentas para apoiar o processo de compras na empresa.",
    "limitations": "As capturas são demonstrativas ou sanitizadas; fornecedores, valores e negociações reais ficam privados.",
    "stack": [
      "Python",
      "PySide6",
      "SQLite"
    ],
    "img": "/assets/projects/compras-dashboard.webp",
    "imageLabel": "Captura de case público com dados sanitizados",
    "repository": "https://github.com/Mayconxzdev/ComprasProducao",
    "legacy": "/cases/compras-cotacoes/"
  },
  {
    "slug": "tradutor-documental",
    "name": "Tradutor Documental",
    "kind": "ia",
    "group": "Documentos e linguagem",
    "status": "Ferramenta local utilizada",
    "role": "Desenvolvimento principal",
    "headline": "Tradução técnica com estrutura e terminologia preservadas.",
    "summary": "Tradução de documentos técnicos com atenção a tabelas, estilos e terminologia.",
    "problem": "Uma tradução pode preservar o significado e mesmo assim entregar um arquivo com estrutura comprometida.",
    "solution": "Separei leitura, transformação e revisão para trabalhar conteúdos e formatos documentais de forma controlada.",
    "decisions": [
      "Estrutura e terminologia: Separei conteúdo e organização do documento, aplicando regras e memória de tradução aos termos recorrentes.",
      "Arquivo que pode ser revisado: Testei diferenças de formato e casos especiais; a conferência de conteúdo e diagramação continua necessária."
    ],
    "roleDetail": "Desenvolvi a ferramenta local e trabalho na revisão de seus formatos e resultados.",
    "limitations": "A captura mostra a aplicação com um documento de demonstração, sem conteúdo técnico confidencial. A preservação de formato depende do arquivo e exige revisão.",
    "stack": [
      "Python",
      "DOCX",
      "ODT",
      "Processamento"
    ],
    "img": "/assets/evidence/tradutor-interface-bilingue.png",
    "imageLabel": "Captura da interface bilíngue da ferramenta local"
  },
  {
    "slug": "sites-industriais",
    "name": "Sites Institucionais Industriais",
    "kind": "web",
    "group": "Sites publicados",
    "status": "Sites publicados",
    "role": "Desenvolvimento e manutenção",
    "headline": "Informação técnica que o visitante consegue encontrar.",
    "summary": "Sites e catálogos para apresentar produtos industriais de forma compreensível.",
    "problem": "Equipamentos industriais exigem nomenclatura consistente, informação técnica clara e caminhos fáceis até o produto.",
    "solution": "Trabalhei navegação, conteúdo, páginas responsivas e organização de produtos para comunicação institucional.",
    "decisions": [
      "Vesper: Dei protagonismo aos equipamentos e organizei o conteúdo técnico para a consulta do catálogo.",
      "Vent Rio: Adaptei identidade, produtos e apresentação, mantendo navegação responsiva e conteúdo acessível ao público de cada site."
    ],
    "roleDetail": "Atuei no desenvolvimento, reconstrução, conteúdo e manutenção dos sites industriais.",
    "limitations": "As capturas documentam sites públicos. Marcas e imagens pertencem às empresas e aos respectivos titulares.",
    "stack": [
      "HTML",
      "CSS",
      "JavaScript",
      "SEO"
    ],
    "img": "/assets/projects/ventrio-live-home.webp",
    "imageLabel": "Imagem publicada do site institucional",
    "website": "https://www.ventrio.ind.br/",
    "legacy": "/cases/sites-industriais/"
  },
  {
    "slug": "engenharia-de-dados-compass",
    "name": "Engenharia de Dados · Compass UOL",
    "kind": "dados",
    "group": "Formação prática",
    "status": "Estágio concluído",
    "role": "Estagiário de dados",
    "headline": "Da ingestão à consulta.",
    "summary": "Da preparação dos dados na AWS à consulta e visualização no QuickSight.",
    "problem": "Os dados precisam percorrer etapas definidas antes de se tornarem úteis para análise.",
    "solution": "Trabalhei exercícios de ingestão, processamento e consulta com serviços AWS no contexto de formação prática.",
    "decisions": [
      "Origem e ingestão: Organizei dados de arquivos e APIs no armazenamento AWS.",
      "Transformação: Trabalhei com Glue e PySpark para preparar a estrutura que seria consultada.",
      "Consulta e visualização: Usei Athena e QuickSight para explorar a saída e conferir o que o processamento produziu."
    ],
    "roleDetail": "Realizei o trabalho durante o estágio e programa de formação prática em Engenharia de Dados.",
    "limitations": "As imagens são do exercício de formação. O ambiente AWS utilizado não está mais ativo; os gráficos não representam resultados de clientes.",
    "stack": [
      "Python",
      "AWS S3",
      "Glue / PySpark",
      "Athena",
      "QuickSight"
    ],
    "img": "/assets/projects/compass-dashboard.webp",
    "imageLabel": "Captura publicada do case formativo",
    "repository": "https://github.com/Mayconxzdev/Estagio-CompassUOL"
  },
  {
    "slug": "mala-direta",
    "name": "Mala Direta",
    "kind": "ia",
    "group": "Automação B2B",
    "status": "Executada quando necessária",
    "role": "Desenvolvimento principal",
    "headline": "Preparar, revisar e executar campanhas sob demanda.",
    "summary": "Preparar destinatários e mensagens, revisar e executar a campanha quando solicitado.",
    "problem": "Um fluxo de mensagens pode repetir destinos ou executar ações sem que o conteúdo tenha sido validado.",
    "solution": "Modelei pontos de revisão, filas e tratamento de estados para execução sob demanda.",
    "decisions": [
      "Preparar e conferir: Reuni destinatários, conteúdo e anexos para revisar o que será enviado.",
      "Executar sob demanda: A campanha é acionada quando há solicitação, com acompanhamento da fila, tratamento de duplicidades e cancelamentos."
    ],
    "roleDetail": "Desenvolvi o fluxo para atender solicitações pontuais.",
    "limitations": "As telas usam dados de exemplo. Os controles deste portfólio não enviam mensagens nem acessam contatos reais.",
    "stack": [
      "n8n",
      "SMTP",
      "Node.js",
      "Workflows"
    ],
    "img": "/assets/projects/n8n-overview.webp",
    "imageLabel": "Visão contextual pública do ambiente, não métrica deste fluxo",
    "repository": "https://github.com/Mayconxzdev/MalaDireta"
  },
  {
    "slug": "videomind",
    "name": "VideoMind",
    "kind": "ia",
    "group": "Ferramentas criativas",
    "status": "Ferramenta pessoal em evolução",
    "role": "Desenvolvimento pessoal",
    "headline": "Construindo um ambiente de edição operável por agentes.",
    "summary": "Ferramentas de edição para que agentes possam organizar cenas, cortes e legendas.",
    "problem": "Operações repetidas de edição e processamento podem ser difíceis de reproduzir sem um fluxo organizado.",
    "solution": "Desenvolvi ferramentas locais de edição que operam em integração com outro agente, com timeline para inspecionar mídia, cortes e faixas de texto e áudio.",
    "decisions": [
      "O que já exploro: Desenvolvi e testei componentes de organização de mídia, faixas e processamento local. A captura mostra a timeline do protótipo.",
      "O que estou construindo: A integração com outro agente já executa cortes, legendas e exportações; continuo refinando verificações, fluxos e revisão da saída."
    ],
    "roleDetail": "Desenvolvi e testei componentes locais da ferramenta de edição e processamento.",
    "limitations": "Projeto pessoal em evolução. A captura mostra a interface autorizada; não comprova sozinha o agente em ação nem substitui a revisão do resultado.",
    "stack": [
      "Python",
      "FFmpeg",
      "Vídeo",
      "Desktop"
    ],
    "img": "/assets/portfolio-approved/videomind_ui_timeline.png",
    "imageLabel": "Captura autorizada da timeline; a integração com outro agente foi informada pelo autor"
  },
  {
    "slug": "carreirapessoal",
    "name": "CarreiraPessoal",
    "kind": "ia",
    "group": "Ferramenta pessoal",
    "status": "Uso pessoal",
    "role": "Projeto próprio",
    "headline": "Organizar o próprio processo de carreira.",
    "summary": "Organizar candidaturas e versões de currículo, sem depender de planilhas soltas.",
    "problem": "Comparar oportunidades e manter diferentes currículos se torna confuso quando cada decisão está em um lugar.",
    "solution": "Estruturei um fluxo local de organização e revisão de informações, com apoio de análise assistida.",
    "decisions": [
      "Oportunidades e próximos passos: Reúno informações e acompanho decisões da minha busca profissional.",
      "Versões e documentos: Organizo materiais para recuperar e revisar o que faz sentido em cada oportunidade."
    ],
    "roleDetail": "Projeto pessoal que desenvolvi para minhas próprias rotinas.",
    "limitations": "Ferramenta de uso pessoal. Não há serviço comercial de recrutamento nem promessa de aprovação em candidaturas.",
    "stack": [
      "Python",
      "SQLite",
      "PDF",
      "Produtividade"
    ],
    "img": "",
    "imageLabel": "Sem dados pessoais no site",
    "repository": "https://github.com/Mayconxzdev/CarreiraPessoal"
  },
  {
    "slug": "brasil-as-claras",
    "name": "Brasil às Claras",
    "kind": "lab",
    "group": "Civic tech",
    "status": "Em desenvolvimento · não lançado",
    "role": "Projeto pessoal",
    "headline": "Consultar dados públicos, entender o contexto e conferir a fonte.",
    "summary": "Consultar dados públicos, entender o contexto e voltar à fonte oficial.",
    "problem": "Informações públicas podem ser difíceis de encontrar, interpretar e relacionar com decisões do cotidiano.",
    "solution": "Estou explorando consultas a fontes oficiais, visualizações e explicações, sem tratar a pesquisa como produto lançado.",
    "decisions": [
      "Encontrar e entender: Organizo as consultas e explico termos que dificultam a leitura de quem não acompanha o tema.",
      "Conferir na origem: Mantenho a distinção entre fonte oficial, interpretação e conclusão. Uma despesa isolada não demonstra irregularidade."
    ],
    "roleDetail": "Concebi e desenvolvo a arquitetura e as interfaces do projeto, ainda não lançado.",
    "limitations": "Projeto em desenvolvimento, ainda não lançado. A captura foi autorizada pelo autor; a fotografia de acervo da Agência Senado mantém crédito e licença CC BY 2.0.",
    "stack": [
      "Dados públicos",
      "Python",
      "Visualização",
      "Acessibilidade"
    ],
    "img": "/assets/portfolio-approved/brasil_as_claras_01_desktop.png",
    "imageLabel": "Captura autorizada do protótipo, em desenvolvimento e não lançado"
  },
  {
    "slug": "conversa360",
    "name": "Conversa360",
    "kind": "lab",
    "group": "Arquitetura experimental",
    "status": "Em desenvolvimento · incompleto",
    "role": "Projeto pessoal",
    "headline": "Continuidade de conversas entre histórico, eventos e canais.",
    "summary": "Histórico e contexto para continuar atendimentos entre componentes de mensageria.",
    "problem": "Mensagens, arquivos e atualizações de estado exigem atenção a repetição, ordem de eventos e falhas.",
    "solution": "Modelei contratos e componentes experimentais para investigar consistência e tratamento de eventos.",
    "decisions": [
      "Componentes locais: Organizo o modelo de contatos, conversas e eventos para manter o contexto de cada atendimento.",
      "Arquitetura de entrega: Estudo filas e outbox para separar persistência e envio, com estados recuperáveis.",
      "Integrações pendentes: O envio real depende da integração e homologação de cada serviço; testes locais não comprovam conexão com todos os canais."
    ],
    "roleDetail": "Desenvolvo a arquitetura e os componentes locais deste produto ainda incompleto.",
    "limitations": "Produto incompleto, sem lançamento público. O mapa diferencia componentes locais e integração planejada.",
    "stack": [
      "FastAPI",
      "WebSockets",
      "Outbox",
      "Segurança"
    ],
    "img": "",
    "imageLabel": "Sem visual de produção"
  },
  {
    "slug": "postagem-redes",
    "name": "Postagem Redes",
    "kind": "lab",
    "group": "Automação histórica",
    "status": "Experimento encerrado",
    "role": "Experimento próprio",
    "headline": "Experimento útil, mas não parte do meu fluxo atual.",
    "summary": "O que aprendi ao testar automação de criação e publicação de conteúdo.",
    "problem": "Automatizar a preparação de conteúdo não elimina a necessidade de revisar antes de ações externas.",
    "solution": "Experimentei fluxos com pontos de aprovação, mantendo separada a ideia de automação da prática atual de publicação.",
    "decisions": [
      "O experimento: Testei integrações entre tarefas de mídia, revisão e publicação.",
      "A escolha que ficou: Mantive a revisão e as ferramentas que ajudam na criação, mas deixei de usar o disparo recorrente desse fluxo."
    ],
    "roleDetail": "Criei e testei o experimento. Hoje o preservo como registro de aprendizado.",
    "limitations": "Experimento encerrado. As capturas são históricas e não mostram uma automação ativa.",
    "stack": [
      "n8n",
      "Python",
      "APIs de IA",
      "Meta API"
    ],
    "img": "/assets/projects/postagem-editor.webp",
    "imageLabel": "Captura pública do case histórico",
    "repository": "https://github.com/Mayconxzdev/PostagemRedes"
  }
];
