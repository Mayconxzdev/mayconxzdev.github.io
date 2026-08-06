# Maycon Ferreira — Automação, IA e integrações

Portfólio profissional de **Maycon Ferreira, Analista de Automação, IA e Integrações**: [mayconxzdev.github.io](https://mayconxzdev.github.io/).

O site reúne sistemas em produção, uso interno, cases sanitizados, repositórios públicos e produtos em desenvolvimento. Cada case declara problema, participação, stack, resultado, evidência, limitações e estado real — sem tratar sandbox, piloto e produção como sinônimos.

## Posicionamento e seleção estratégica

Os materiais principais demonstram dimensões diferentes, evitando repetir o mesmo tipo de projeto:

- **Mala Direta** — n8n, escala, filas, cancelamento e auditoria;
- **Catálogo Operacional de Compras** — FastAPI, SQLite FTS5, busca, histórico e concorrência;
- **Postagem Redes** — IA generativa, Meta Graph API, aprovação humana e entrega multicanal;
- **Portal** — produto multiempresa em desenvolvimento, tenancy/RLS, Action Envelope, aprovações e outbox;
- **Produção Operacional, Vesper Propostas e HelpDesk** — implantação, adoção e sustentação em ambiente empresarial.

## Estrutura pública

- página inicial em português e inglês;
- 18 cases por idioma;
- página de competências em português e inglês;
- currículo de uma página em PT-BR e inglês;
- links para código público quando existe;
- provas visuais públicas, sanitizadas ou identificadas como referência histórica;
- tema claro e escuro, navegação por teclado, busca e filtros progressivos.

## Currículos

Os PDFs em `assets/cv/` são gerados por código:

- `Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf`
- `Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf`

A validação exige uma página A4, texto selecionável, cinco links funcionais, seções ATS convencionais, datas consistentes, inventário sem versões antigas, margens seguras, fonte mínima e ausência de colisões. Também bloqueia métricas ambíguas, como associar 158 nós a todos os workflows da Mala Direta ou 58 nós aos três workflows do Postagem Redes.

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

Para repetir a inspeção visual:

```bash
npm install --no-save playwright@1.54.2
npx playwright install chromium
python -m http.server 8000 --bind 127.0.0.1
PORTFOLIO_BASE_URL=http://127.0.0.1:8000 node scripts/visual_smoke.mjs
```

O smoke test cobre home, competências, Catálogo Operacional de Compras e Portal em PT-BR e inglês, nos temas claro e escuro e em desktop e mobile: **32 capturas completas**. Ele falha com overflow horizontal, imagens quebradas, texto recortado, posicionamento ausente, links de currículo antigos ou menu móvel inconsistente.

## Critérios de evidência

- valores de nós, workflows, usuários e resultados pertencem ao componente exato que os sustenta;
- projetos usados na experiência profissional não são repetidos na seção de projetos do currículo;
- código privado é identificado como privado;
- telas da arquitetura anterior do Portal são rotuladas como referência histórica;
- o novo Portal é apresentado como em desenvolvimento e pré-piloto, não como produção;
- credenciais, dados pessoais, fornecedores, preços, caminhos e detalhes privados não são expostos.

## Estrutura do projeto

- `/` e `/en/` — portfólio bilíngue;
- `/competencias/` e `/en/skills/` — competências ligadas a provas;
- `/cases/<slug>/` e `/en/cases/<slug>/` — cases;
- `/assets/cv/` — currículos gerados;
- `/scripts/` — geração, normalização, validação e smoke visual;
- `/docs/` — estratégia e relatório de qualidade.

## Qualidade publicada

O workflow **Validate and deploy GitHub Pages** só libera o deploy após validar fontes Python, conteúdo e parsing dos currículos, geometria dos PDFs, referências locais, higiene de conteúdo, JavaScript e 32 renderizações estratégicas. O estado auditado está em [`docs/TEST_REPORT.md`](docs/TEST_REPORT.md).
