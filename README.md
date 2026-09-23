# Portfólio — Maycon Ferreira

Código-fonte do portfólio profissional de **Automação e IA aplicada**. O site mostra como entendo processos, construo automações e integrações, e levo soluções internas até implantação, adoção e sustentação.

**Site publicado:** [mayconxzdev.github.io](https://mayconxzdev.github.io/) · [English version](https://mayconxzdev.github.io/en/)

## Cases em destaque

| Case | Evidência principal | Estado |
| --- | --- | --- |
| [Vesper Propostas](cases/vesper-propostas/) | propostas simples de 2–4 min para menos de 30 s, usadas diariamente por 4 profissionais | uso interno; código privado, case sanitizado |
| [Belarc Inventory](cases/belarc-inventory/) | sistema de inventário e contexto de suporte com agente Windows e serviço local | uso interno; co-desenvolvido, evidências sanitizadas |
| [Postagem Redes](cases/postagem-redes/) | grounding/RAG, revisão humana e evals reproduzíveis | validado em teste; não é produção |
| [Produção Operacional](cases/producao-operacional/) | implantação em 10+ computadores e uma TV, apoiando 20+ pessoas em 9 setores | produção |

Outros projetos aparecem no arquivo da página inicial: [ComprasVesper](cases/compras-vesper/) integra e-mail e fila persistente; [Mala Direta](cases/mala-direta/) automatiza campanhas com n8n; [Central ISO](cases/central-iso/) é um piloto técnico.

## Currículos

O repositório mantém quatro PDFs de uma página: currículo geral PT-BR, variação PT-BR para automação e IA, variação PT-BR para Power Platform/BI e espelho geral em inglês. A fonte editável é [`scripts/generate_resumes_general.py`](scripts/generate_resumes_general.py); os PDFs em [`assets/cv/`](assets/cv/) são regenerados, nunca editados manualmente.

Os PDFs são gerados a partir da fonte Python e mantêm os mesmos fatos, datas e métricas. As variações destacam experiências diferentes sem alterar o histórico profissional.

## Estrutura

- `index.html`, `en/` — páginas estáticas em português e inglês;
- `cases/`, `en/cases/` — narrativas dos projetos e seus estados reais;
- `assets/` — identidade visual, evidências sanitizadas e PDFs;
- `css/`, `js/` — estilos e interações do site;
- `docs/VALIDATION.md` — comandos e verificações de manutenção do site;
- `scripts/` — geração de currículos, materialização do site e validadores.

O portfólio é estático, publicado no GitHub Pages. Código empresarial e dados reais não são publicados; cases internos usam descrições, capturas e dados sanitizados.

## Executar localmente

Requer Python 3.10+ e, para as verificações de navegador, Node.js/npm e Chromium para Playwright.

```powershell
python -m http.server 8000
```

Abra `http://127.0.0.1:8000/`. Para regenerar os quatro currículos:

```powershell
python scripts/generate_resumes_general.py
```

## Validar

As dependências de validação de PDF e navegador estão fixadas no workflow de CI (`reportlab`, `pypdf`, `pymupdf`, Playwright e axe-core). Os principais comandos do workflow são:

```powershell
python -m compileall -q scripts
python scripts/validate_general_resumes.py
python scripts/validate_resume_visual.py
python scripts/validate_site.py
python scripts/validate_navigation_targets.py
python scripts/validate_editorial_consistency.py
python scripts/validate_case_visual_consistency.py
python scripts/validate_case_sequence.py
python scripts/performance_budget.py
node scripts/visual_smoke.mjs http://127.0.0.1:8000 work/qa-visual
node scripts/site_interaction_smoke.mjs http://127.0.0.1:8000
node scripts/accessibility_smoke.mjs http://127.0.0.1:8000
```

O CI também confere consistência entre fontes versionadas e materializadores, gera e inspeciona PDFs, percorre páginas e cases com Playwright, executa axe e valida a publicação. Essas verificações cobrem os critérios definidos no repositório e complementam a revisão humana.

## Publicação

Pull requests executam as validações sem publicar o site. Push em `main` executa validação, deploy no GitHub Pages e verificação posterior do SHA publicado e dos quatro PDFs disponíveis.
