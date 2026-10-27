# Laboratório Vivo — Maycon Ferreira

Meu portfólio de sistemas, automação, integrações, dados e IA aplicada. Apresento o problema, minha participação, decisões de implementação e evidências de cada trabalho, com o estado e os limites de cada projeto.

[Abrir portfólio](https://mayconxzdev.github.io/) · [Seis currículos PT/EN](https://mayconxzdev.github.io/assets/cv/) · [English](README.en.md)

## O que você encontra

- 18 cases, incluindo Produção Operacional, Manutenção em Campo, Belarc Inventory, ZERO21FOTOS e Hubora.
- Capturas reais ou demonstrações identificadas, com miniaturas, legendas e ampliação integral. Coautoria e áreas privadas são explicitadas.
- Três modos de apresentação: Automático acompanha o dispositivo; Animação é uma escolha explícita; Leitura direta mantém os cinco destaques no fluxo da página.
- Três currículos em português e três equivalentes em inglês: Geral, Desenvolvimento e Automação com IA, Produtos Digitais e Conteúdo com IA.

O portfólio é uma aplicação estática. Ele apresenta os sistemas; não conecta o visitante às bases internas ou às operações dos clientes. As simulações nos cases são demonstrações ilustrativas.

## Stack e execução

Vite, JavaScript, CSS e GSAP. Playwright e axe-core verificam navegação, galerias, movimento, acessibilidade automatizada e responsividade. Node.js 22.12 ou superior é necessário; a CI usa Node 22.

    git clone https://github.com/Mayconxzdev/mayconxzdev.github.io.git
    cd mayconxzdev.github.io
    npm ci
    npm run dev

O desenvolvimento abre em http://127.0.0.1:8789. Para gerar e inspecionar a produção:

    npm run build
    npm run preview

A prévia fica em http://127.0.0.1:4214. O build lê somente arquivos deste repositório, verifica a integridade das mídias e gera 18 páginas antes do Vite. A saída fica em dist/ e não deve ser editada ou commitada.

## Onde editar

| Fonte | Responsabilidade |
|---|---|
| index.html e src/ | Homepage, dados, estilos e interações |
| src/data.js e src/editorial-v13.js | Projetos, autoria, tecnologias e narrativa |
| src/v8-story.json e src/motion-preference.js | Capturas dos cinco destaques e preferência de movimento |
| scripts/evidence-map.mjs | Galerias, IDs estáveis, legendas e origem das evidências |
| templates/case.html e scripts/generate-cases.mjs | Geração dos cases canônicos em public/projetos/ |
| public/ | Mídias autorizadas, fontes, PDFs e páginas históricas preservadas |
| scripts/resumes-content.json | Conteúdo dos seis currículos |
| .github/workflows/pages.yml | Build, testes, publicação e conferência do artefato online |

Os HTML de public/projetos/, lab.css, robots.txt e sitemap.xml são gerados e ficam fora do versionamento. Para alterar um case, edite os dados, o template ou o gerador e rode o build. Os arquivos históricos em /cases/, /en/ e /competencias/ mantêm links antigos e estão identificados como acervo anterior; não são versões ativas adicionais.

## Verificações

Depois de gerar o build:

    npx playwright install chromium
    npm test
    npm run test:full

O runner inicia a prévia automaticamente ou reutiliza uma instância que sirva exatamente o mesmo index.html. A rodada completa cobre homepage e 18 cases em 320, 360, 390, 430, 768, 1024, 1440 e 1920 px, galerias, teclado, menus, Escape, filtros, PDFs, navegação de volta, movimento reduzido, rolagem rápida e páginas históricas. Telas baixas e uma aproximação de zoom a 200% também são exercitadas.

Essas verificações usam Chromium e emulação. Não representam testes em todo hardware, entrevistas com recrutadores, certificação WCAG, aprovação em ATS ou Core Web Vitals de usuários reais. Evidências de execução ficam em evidence/ e não são enviadas automaticamente ao repositório.

## Currículos

Os seis PDFs canônicos e nove aliases de URLs antigas ficam em public/assets/cv/. O catálogo mostra somente as seis versões atuais. O build web preserva os PDFs versionados, sem depender de Python.

Para revisar o conteúdo ou regenerar os PDFs:

    python -m pip install -r requirements-resumes.txt
    npm run resumes:build
    npm run build
    npm run resumes:verify

O gerador usa Arial quando disponível em RESUME_FONT_DIR ou C:/Windows/Fonts, com fallback Helvetica. Uma regeneração em outra plataforma exige conferir os PNGs e a paginação antes de substituir os arquivos; não se presume equivalência visual entre fontes.

## Publicação e rastreabilidade

PRs passam pelo mesmo build e pela regressão. Após integração em main, GitHub Actions publica somente dist/. A etapa seguinte confere o commit em build.txt e os hashes de todos os arquivos contra o manifesto do artefato testado. [build.json](https://mayconxzdev.github.io/build.json) identifica o conteúdo efetivamente servido.

O histórico anterior, quando o repositório guardava somente os arquivos compilados, foi preservado. A árvore atual contém as fontes editáveis. Veja [arquitetura](docs/ARCHITECTURE.md), [deploy e rollback](docs/DEPLOYMENT.md) e [alterações](CHANGELOG.md).

## Imagens, privacidade e reutilização

Mídias de Vesper, Vent Rio e ZERO21FOTOS têm autorização de exibição declarada pelo titular. As capturas de Brasil às Claras e VideoMind foram liberadas em 26/10/2026. Os créditos de terceiros permanecem visíveis; capturas reservadas e dados de clientes ficam fora do Git e do deploy.

[ASSETS.md](ASSETS.md) descreve o escopo e as atribuições. A permissão de exibição no portfólio não concede licença geral para redistribuir imagens, marcas ou sistemas apresentados. Este repositório não declara uma licença irrestrita de reutilização desses materiais.

Para comunicar uma exposição de dados, consulte [SECURITY.md](SECURITY.md).
