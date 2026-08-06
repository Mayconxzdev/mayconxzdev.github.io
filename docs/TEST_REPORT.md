# Verificação da versão publicada

Atualizado em **6 de agosto de 2026**, após revisão dos repositórios atuais, métricas, posicionamento, redundância entre projetos, consistência bilíngue e apresentação visual.

## Currículos PT-BR e inglês

Confirmado automaticamente em cada execução do GitHub Actions:

- uma página A4 e uma única coluna;
- texto selecionável e extraível por `pypdf` e PyMuPDF;
- seções convencionais em ordem: resumo, habilidades, experiência, projetos, formação, certificações e idiomas;
- cinco links clicáveis e somente os dois PDFs vigentes;
- título profissional explícito, datas consistentes e cargo formal preservado;
- métricas públicas: 10 mil+ execuções em produção, 2-4 minutos para menos de 30 segundos, 11 computadores e uma TV, 11 usuários, 900+ destinatários e aproximadamente 3 horas para 5 minutos;
- quatro projetos selecionados com provas não redundantes: Mala Direta, Catálogo Operacional de Compras, Postagem Redes e Portal;
- distinção explícita entre dois workflows da Mala Direta e 158 nós no workflow principal;
- distinção explícita entre três workflows do Postagem Redes e 58 nós no workflow de ações;
- Catálogo apresentado com FastAPI, SQLite FTS5, controle de concorrência por revisão e uso diário;
- Portal apresentado como produto multiempresa em desenvolvimento, Procurement validado em sandbox e preparação para piloto interno;
- ausência de nomes antigos, combinações ambíguas de métricas, PDFs legados, texto fora das margens e colisões visuais;
- fonte mínima de 8 pontos nas informações auxiliares e corpo principal acima desse limite;
- renderização raster válida e PDF não escaneado.

## Portfólio

O validador estático confere:

- 41 páginas HTML;
- 18 cases em português e 18 equivalentes em inglês;
- 40 URLs no sitemap;
- títulos, `lang`, meta descriptions, canonical, `hreflang` e controle de tema;
- referências locais existentes, imagens com texto alternativo e provas visuais rastreáveis;
- seis indicadores principais ligados aos cases correspondentes;
- identidade **Catálogo Operacional de Compras** nas superfícies estratégicas;
- Portal sem identidade específica de empresa e com status pré-piloto;
- telas antigas do Portal identificadas como referência histórica;
- competências ligadas a evidências de automação, IA, backend, dados, confiabilidade e governança;
- bloqueio de `5 workflows/158`, `3 workflows/58`, `Portal Vesper`, nomes antigos visíveis e outras descrições ambíguas.

## Inspeção em navegador

O smoke test com Chromium produz **32 capturas completas**:

- home PT-BR e inglês;
- competências PT-BR e inglês;
- Catálogo Operacional de Compras PT-BR e inglês;
- Portal PT-BR e inglês;
- desktop 1440 × 1000 e mobile 390 × 844;
- temas claro e escuro.

Em cada combinação são verificados posicionamento visível, tema aplicado, ausência de overflow horizontal, carregamento de imagens, ausência de recorte em textos, links de currículo atuais, seções estratégicas e funcionamento do menu móvel.

## Critério editorial

A primeira leitura deve responder rapidamente:

1. qual função profissional está sendo apresentada;
2. quais problemas empresariais foram resolvidos;
3. quais tecnologias sustentam a atuação;
4. qual escala ou resultado foi observado;
5. qual é o estado real da entrega;
6. onde a evidência pode ser revisada.

A seleção de projetos foi distribuída por dimensão técnica:

- n8n, escala e confiabilidade;
- backend, busca e integridade de dados;
- IA generativa e APIs externas;
- arquitetura full-stack e governança.

Produção Operacional, HelpDesk e Vesper Propostas permanecem na experiência profissional e no portfólio, mas não são repetidos como projetos selecionados no currículo.

## Limites declarados

Este relatório não afirma compatibilidade perfeita com todo ATS, aprovação automática em vagas, teste em todos os navegadores ou validação de ambientes privados. O novo Portal não é apresentado como produção multiempresa; o Catálogo não é apresentado como ERP. A automação reduz riscos técnicos e editoriais, mas a correspondência final continua dependendo da vaga, dos filtros configurados e da leitura humana.
