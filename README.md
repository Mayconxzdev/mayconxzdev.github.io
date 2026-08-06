# Maycon Ferreira — Automação, IA e integrações

Portfólio profissional de **Maycon Ferreira, Analista de Automação, IA e Integrações**: [mayconxzdev.github.io](https://mayconxzdev.github.io/).

O site reúne sistemas em produção, uso interno, cases sanitizados, repositórios públicos e produtos em desenvolvimento. Cada case declara problema, participação, stack, resultado, evidência, limitações e estado real — sem tratar implementação, teste, sandbox, piloto e produção como sinônimos.

## Posicionamento e seleção estratégica

Os materiais prioritários demonstram competências diferentes e complementares:

- **Mala Direta** — n8n, filas, cancelamento, deduplicação, campanhas e auditoria;
- **Produção Operacional** — desktop Windows, NAS, implantação, TV industrial, treinamento e sustentação;
- **Catálogo Operacional de Compras** — FastAPI, SQLite FTS5, busca, histórico e concorrência;
- **Postagem Redes** — IA generativa, Meta Graph API, OAuth2, aprovação humana e entrega por canal;
- **HelpDesk** — Flask, Electron, Socket.IO, ativos, acessos, segurança e IA local opcional;
- **Programa Compass UOL** — Python, SQL, Docker, AWS, ETL, Glue/PySpark, Athena e QuickSight;
- **Portal** — produto multiempresa em desenvolvimento, tenancy/RLS, Action Envelope, aprovações e outbox.

## Evidências atualmente confirmadas

- 10 mil+ execuções na instância n8n de produção, distribuídas entre diferentes automações;
- seis campanhas na Mala Direta sobre uma base de 1.020 contatos, incluindo uma campanha para 900+ destinatários;
- Produção Operacional em 10+ computadores e uma TV, apoiando 20+ profissionais em nove setores produtivos;
- HelpDesk utilizado por 11 usuários;
- treinamento e orientação de 30+ pessoas em escritório, fábrica e acesso remoto;
- propostas simples reduzidas de 2–4 minutos para menos de 30 segundos, com uso diário por quatro profissionais;
- Catálogo Operacional com 24 categorias e 480+ códigos de materiais, usado diariamente por três usuários e consultado pela gestão;
- Programa Compass concluído em dez sprints, com pipeline CSV/API TMDB, S3, Lambda/boto3, Glue/PySpark, Parquet, Raw/Trusted/Refined, Athena e QuickSight.

## Estrutura pública

- página inicial em português e inglês;
- 17 cases ativos por idioma;
- página de competências em português e inglês;
- currículo de uma página em PT-BR e inglês;
- links para código público quando existe;
- provas visuais públicas, sanitizadas ou identificadas como referência histórica;
- tema claro e escuro, navegação por teclado, busca e filtros progressivos;
- seis rotas antigas preservadas apenas como redirecionamentos, fora do sitemap.

Rotas canônicas relevantes:

- `/cases/catalogo-operacional-compras/` e `/en/cases/operational-procurement-catalog/`;
- `/cases/portal/` e `/en/cases/portal/`;
- `/cases/compass/` e `/en/cases/compass/`.

## Currículos

Os PDFs em `assets/cv/` são gerados por código:

- `Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf`
- `Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf`

A validação exige uma página A4, texto selecionável, cinco links funcionais, seções ATS convencionais, datas consistentes, inventário sem versões antigas, margens seguras, fonte mínima e ausência de colisões. Também bloqueia claims antigos ou frágeis, como:

- atribuir as 10 mil execuções exclusivamente à Mala Direta;
- associar 158 nós aos dois workflows ou 58 nós aos três workflows;
- utilizar a métrica histórica Compass de 3h → 5min sem artefato isolado reproduzível;
- apresentar `text-to-video` como competência central sem prova pública direta;
- tratar o head atual do Portal como validado ou pronto para piloto antes da revalidação técnica.

## Validação local

```bash
python -m pip install reportlab==4.4.9 pypdf==5.9.0 pymupdf==1.26.7
python scripts/generate_resumes.py
python scripts/normalize_portfolio_content.py
python scripts/normalize_canonical_routes.py
python scripts/apply_verified_career_facts_v2.py
python scripts/final_text_patch.py
python scripts/validate_resumes.py
python scripts/validate_resume_visual.py
python scripts/validate_site.py
node --check js/site.js
node --check scripts/visual_smoke.mjs
```

Para repetir a inspeção em navegador:

```bash
npm install --no-save playwright@1.54.2
npx playwright install chromium
python -m http.server 8000 --bind 127.0.0.1
PORTFOLIO_BASE_URL=http://127.0.0.1:8000 node scripts/visual_smoke.mjs
```

O smoke test cobre home, competências, Catálogo Operacional de Compras e Portal em PT-BR e inglês, nos temas claro e escuro e em desktop e mobile: **32 capturas completas**. Ele falha com overflow horizontal, imagens quebradas, texto recortado, posicionamento ausente, links de currículo antigos ou menu móvel inconsistente.

## Critérios de evidência

- valores de nós, workflows, usuários e resultados pertencem ao componente exato que os sustenta;
- experiência formal, projetos pessoais e formação prática não são somados artificialmente como anos de experiência profissional;
- código privado é identificado como privado;
- telas da arquitetura anterior do Portal são rotuladas como referência histórica;
- o Portal atual é apresentado como em desenvolvimento, com revalidação técnica antes do piloto;
- o Programa Compass é apresentado como formação prática, não como ambiente empresarial de produção;
- IA multimodal e geração de mídia são descritas sem sugerir integração por API com todos os provedores utilizados;
- credenciais, dados pessoais, fornecedores, preços, caminhos e detalhes privados não são expostos.

## Estrutura do projeto

- `/` e `/en/` — portfólio bilíngue;
- `/competencias/` e `/en/skills/` — competências ligadas a provas;
- `/cases/<slug>/` e `/en/cases/<slug>/` — cases ativos e redirects compatíveis;
- `/assets/cv/` — currículos gerados;
- `/scripts/` — geração, normalização, validação e smoke visual;
- `/docs/` — estratégia e relatório de qualidade.

## Qualidade publicada

O workflow **Validate and deploy GitHub Pages** só libera o deploy após validar fontes Python, conteúdo e parsing dos currículos, geometria dos PDFs, referências locais, rotas canônicas, redirects, sitemap, higiene de conteúdo, JavaScript e 32 renderizações estratégicas. O estado auditado está em [`docs/TEST_REPORT.md`](docs/TEST_REPORT.md).
