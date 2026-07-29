# Maycon Ferreira — Sistemas em Operação

Portfólio profissional bilíngue para GitHub Pages, com foco em **Automação, IA, integrações e sistemas internos reais**.

A direção visual é editorial e técnica: hierarquia tipográfica, grid, evidências, screenshots reais, diagramas derivados da arquitetura e estados declarados. O site evita dashboard genérico, neon, glassmorphism, excesso de cards e efeitos sem função.

## Publicação

1. Substitua o conteúdo de `Mayconxzdev/mayconxzdev.github.io` pelos arquivos deste pacote.
2. Em **Settings → Pages**, selecione **GitHub Actions**.
3. Faça commit na branch `main`.

O workflow valida páginas, referências locais e sintaxe JavaScript antes do deploy.

## Validação local

```bash
python scripts/validate_site.py
node --check js/site.js
```

## Estrutura

- `/` — português;
- `/en/` — inglês;
- `/cases/<slug>/` — cases em português;
- `/en/cases/<slug>/` — cases em inglês;
- HTML estático para o conteúdo principal;
- JavaScript somente para menu, busca e filtros;
- currículo em `assets/cv/`;
- Open Graph local em `assets/social/`.

## Documentação

- [`docs/DESIGN_STRATEGY.md`](docs/DESIGN_STRATEGY.md) — público, conceito, direção visual e arquitetura da informação;
- [`docs/VALIDATION.md`](docs/VALIDATION.md) — plano de validação;
- [`docs/TEST_REPORT.md`](docs/TEST_REPORT.md) — resultados observados e limites.

## Identidade

O pacote usa uma marca tipográfica local, sem depender de imagens externas. Uma fotografia autorizada pode ser adicionada depois sem alterar a estrutura do site.
