# Portfólio profissional — Maycon Ferreira

Este repositório contém meu portfólio em português e inglês, com projetos de automação de processos, IA aplicada, integrações, sistemas internos e produtos digitais.

Acesse: [mayconxzdev.github.io](https://mayconxzdev.github.io/)

## O que está publicado

Os projetos principais mostram partes diferentes da minha atuação:

- **Mala Direta:** campanhas em n8n, filas, deduplicação, cancelamento e auditoria;
- **Produção Operacional:** aplicação desktop Windows, integração somente leitura com NAS, implantação e modo TV;
- **Vesper Propostas:** geração de ODT/PDF, IMAP/SMTP e revisão humana;
- **Catálogo Operacional de Compras:** FastAPI, SQLite FTS5, histórico e controle de concorrência;
- **Postagem Redes:** IA generativa, Meta Graph API, OAuth2 e aprovação humana;
- **HelpDesk:** Flask, Electron, Socket.IO, ativos, acessos e IA local opcional;
- **Programa Compass UOL:** Python, SQL, Docker, AWS, Glue/PySpark, Athena e QuickSight;
- **Portal:** produto multiempresa em desenvolvimento, com tenancy/RLS, ações governadas e outbox.

Também mantenho cases de sites industriais, aplicações pessoais e versões públicas sanitizadas de sistemas privados.

## Resultados apresentados

- 10 mil+ execuções na instância n8n de produção, distribuídas entre diferentes automações;
- seis campanhas na Mala Direta sobre uma base de 1.020 contatos, incluindo uma campanha para 900+ destinatários;
- Produção Operacional em 10+ computadores e uma TV, apoiando 20+ profissionais em nove setores;
- HelpDesk utilizado por 11 pessoas;
- treinamento e orientação de 30+ pessoas em escritório, fábrica e acesso remoto;
- propostas simples reduzidas de 2–4 minutos para menos de 30 segundos;
- Catálogo Operacional com 24 categorias e 480+ códigos, utilizado diariamente por três pessoas;
- dez sprints do Programa Compass com um pipeline de dados em AWS.

## Currículos

Os dois currículos ficam em `assets/cv/`:

- `Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf`
- `Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf`

Eles são gerados por `scripts/generate_resumes.py` e mantidos em uma página A4, com texto selecionável, estrutura de uma coluna, seções convencionais e links para contato, LinkedIn, GitHub e portfólio.

## Estrutura

- `/` e `/en/` — páginas iniciais em português e inglês;
- `/competencias/` e `/en/skills/` — tecnologias e práticas que utilizo;
- `/cases/` e `/en/cases/` — detalhes dos projetos;
- `/assets/cv/` — currículos gerados;
- `/scripts/` — geração, normalização e validação;
- `/docs/` — decisões técnicas e relatórios internos de qualidade.

## Executar localmente

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Abra `http://127.0.0.1:8000`.

Para gerar e validar os currículos e as páginas:

```bash
python -m pip install reportlab==4.4.9 pypdf==5.9.0 pymupdf==1.26.7
python scripts/generate_resumes.py
python scripts/normalize_portfolio_content.py
python scripts/normalize_canonical_routes.py
python scripts/apply_verified_career_facts_v2.py
python scripts/final_text_patch.py
python scripts/rewrite_public_voice.py
python scripts/validate_resumes.py
python scripts/validate_resume_visual.py
python scripts/validate_site.py
python scripts/validate_public_voice.py
node --check js/site.js
node --check scripts/visual_smoke.mjs
```

## Validação automática

O GitHub Actions verifica:

- geração e leitura dos PDFs;
- quantidade de páginas, margens, fonte e sobreposição;
- rotas, links, imagens e versões em português e inglês;
- ausência de métricas antigas nas áreas principais;
- linguagem pública escrita como apresentação dos meus projetos, sem parecer um relatório de recrutamento;
- navegação em desktop e celular, nos temas claro e escuro.

Os detalhes técnicos dessas verificações ficam em [`docs/TEST_REPORT.md`](docs/TEST_REPORT.md).

## Privacidade e precisão

Nos cases públicos, removo credenciais, dados pessoais, fornecedores, preços, documentos, caminhos de rede e informações internas. Quando um projeto está em demonstração, teste, desenvolvimento ou referência histórica, isso aparece de forma explícita na própria página.
