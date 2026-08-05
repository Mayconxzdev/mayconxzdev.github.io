# Maycon Ferreira — Automação, IA e integrações

Portfólio profissional de **Maycon Ferreira, Analista de Automação, IA e Integrações**: [mayconxzdev.github.io](https://mayconxzdev.github.io/).

O site reúne sistemas em produção, cases sanitizados, repositórios públicos e competências comprovadas em n8n, Python, APIs REST, automação low-code, IA generativa, agentes e confiabilidade operacional. O objetivo não é acumular telas ou palavras-chave: cada case começa pelo problema, informa o estado real da entrega, descreve a participação e apresenta resultado, evidência e limite.

## Estrutura pública

- página inicial em português e inglês;
- 18 cases por idioma, com rotas próprias;
- página de competências em português e inglês;
- currículo de uma página em PT-BR e inglês;
- links para código público quando existe;
- provas visuais públicas ou sanitizadas, identificadas pelo contexto;
- tema claro e escuro, navegação por teclado, busca e filtros progressivos.

## Currículos

Os PDFs em `assets/cv/` são gerados por código para manter o conteúdo e o layout reproduzíveis:

- `Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf`
- `Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf`

A validação automatizada exige uma página A4, texto selecionável, cinco links funcionais, seções ATS convencionais, termos e métricas obrigatórios, ausência de PDFs antigos, margens seguras, fonte mínima definida e nenhuma colisão visual.

## Validação local

```bash
python -m pip install reportlab==4.4.9 pypdf==5.9.0 pymupdf==1.26.7
python scripts/generate_resumes.py
python scripts/normalize_portfolio_content.py
python scripts/validate_resumes.py
python scripts/validate_resume_visual.py
python scripts/validate_site.py
node --check js/site.js
```

Para repetir a inspeção das rotas estratégicas em navegador:

```bash
npm install --no-save playwright@1.54.2
npx playwright install chromium
python -m http.server 8000 --bind 127.0.0.1
PORTFOLIO_BASE_URL=http://127.0.0.1:8000 node scripts/visual_smoke.mjs
```

O smoke test renderiza a home e a página de competências em PT-BR e inglês, nos temas claro e escuro e em desktop e mobile. Ele falha quando encontra posicionamento ausente, overflow horizontal, imagens quebradas, texto recortado, links de currículo antigos ou menu móvel inconsistente.

## Critérios de evidência

Capturas públicas pertencem ao produto publicado ou a versões sanitizadas e explicitamente identificadas. Credenciais, dados pessoais, anexos operacionais, caminhos locais, IPs e detalhes privados de integrações não são expostos. Quando não existe tela publicável, o case usa uma composição arquitetural identificada como explicativa — nunca uma interface fictícia apresentada como produto real.

## Estrutura do projeto

- `/` — portfólio em português;
- `/en/` — versão em inglês;
- `/competencias/` e `/en/skills/` — matriz pública de competências;
- `/cases/<slug>/` e `/en/cases/<slug>/` — cases;
- `/assets/cv/` — currículos gerados;
- `/scripts/` — geração, normalização e validação;
- `/docs/` — estratégia e relatório de qualidade.

## Qualidade publicada

O workflow **Validate and deploy GitHub Pages** só libera o deploy depois de validar fontes Python, conteúdo dos currículos, parsing por duas bibliotecas, renderização e geometria dos PDFs, referências locais, higiene de conteúdo, JavaScript e as 16 combinações visuais das rotas estratégicas. O estado auditado está documentado em [`docs/TEST_REPORT.md`](docs/TEST_REPORT.md), e as decisões de apresentação em [`docs/DESIGN_STRATEGY.md`](docs/DESIGN_STRATEGY.md).
