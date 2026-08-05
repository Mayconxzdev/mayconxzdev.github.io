# Verificação da versão publicada

Atualizado em **5 de agosto de 2026**, após auditoria de posicionamento, ATS, conteúdo, métricas, consistência bilíngue e apresentação visual.

## Currículos PT-BR e inglês

Confirmado automaticamente em cada execução do GitHub Actions:

- uma página A4 e uma única coluna;
- texto selecionável e perfil extraível por `pypdf` e PyMuPDF;
- seções convencionais em ordem: resumo, habilidades, experiência, projetos, formação, certificações e idiomas;
- cinco links clicáveis e somente os dois nomes de PDF vigentes;
- título profissional explícito e datas consistentes;
- métricas públicas preservadas: 10 mil+ execuções de workflows em produção, 2-4 minutos para menos de 30 segundos, 11 computadores e uma TV, 11 usuários, 900+ destinatários e aproximadamente 3 horas para 5 minutos;
- termos-alvo comprovados, incluindo n8n, automação low-code, Python, APIs REST, IA generativa, agentes, Codex, JSON Schema, IA multimodal, text-to-video, Node.js/Express, FastAPI, Docker e CI/CD;
- ausência de expressões antigas ou não sustentadas, PDFs legados, texto fora das margens, colisões entre blocos, títulos encostados e fonte abaixo do limite definido;
- renderização raster válida, PDF não criptografado e não escaneado.

## Portfólio

O validador estático confere:

- 41 páginas HTML;
- 18 cases em português e 18 equivalentes em inglês;
- 40 URLs no sitemap;
- títulos, `lang`, meta descriptions, canonical, `hreflang` e controle de tema;
- referências locais existentes, imagens com texto alternativo e provas visuais rastreáveis nos cases;
- seis indicadores principais com ligação direta para suas evidências;
- links de currículo restritos às versões atuais;
- posicionamento profissional explícito na primeira tela e nas páginas de competências;
- consistência entre PT-BR e inglês;
- bloqueio de termos, descrições, cargas horárias e nomenclaturas antigas nas áreas estratégicas.

## Inspeção em navegador

O smoke test com Chromium produz **16 capturas completas**:

- home PT-BR;
- home em inglês;
- competências PT-BR;
- skills em inglês;
- desktop 1440 × 1000 e mobile 390 × 844;
- temas claro e escuro.

Em cada combinação são verificados: texto de posicionamento visível, ausência de overflow horizontal, imagens carregadas, ausência de recorte em títulos e textos principais, links de currículo atuais, existência das seções estratégicas e abertura/fechamento do menu móvel com `Escape`.

## Critério editorial

A primeira leitura deve responder rapidamente:

1. qual função profissional está sendo apresentada;
2. quais problemas são resolvidos;
3. quais tecnologias sustentam a atuação;
4. qual escala ou resultado já foi observado;
5. onde o recrutador pode verificar a evidência.

A linguagem evita superlativos sem prova. Sistemas implantados, cases confidenciais, pilotos e protótipos são classificados separadamente. Projetos privados ampliam a demonstração de stack, mas não são descritos como produção.

## Limites declarados

Este relatório não afirma compatibilidade perfeita com todo ATS, aprovação automática em vagas, medição de Core Web Vitals de campo, teste em todos os navegadores ou validação de ambientes corporativos privados. A correspondência de um currículo continua dependendo da descrição da vaga, dos filtros configurados e da leitura humana. A automação reduz riscos técnicos e editoriais; não substitui adaptação responsável a cada oportunidade.
