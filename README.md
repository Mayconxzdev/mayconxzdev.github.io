# Maycon Ferreira — Automação, IA e integrações

Este é o código do meu portfólio profissional: [mayconxzdev.github.io](https://mayconxzdev.github.io/). Ele reúne cases de automação de processos, integrações, n8n e sistemas internos, sempre separando o que foi comprovado do que depende de ambiente privado ou de um provedor externo.

O objetivo não é mostrar uma coleção de telas. Cada case começa pelo problema operacional, explica a minha participação e registra resultado, evidência pública e limite real.

## O que há no site

- uma página inicial em português e inglês;
- 18 cases por idioma, com rotas próprias;
- links para código público quando existe;
- currículo em PDF e formas diretas de contato;
- navegação, busca e filtros que funcionam sem depender do JavaScript para o conteúdo principal.

## Validação local

```bash
python scripts/validate_site.py
node --check js/site.js
```

## Estrutura do projeto

- `/` — português;
- `/en/` — inglês;
- `/cases/<slug>/` — cases em português;
- `/en/cases/<slug>/` — cases em inglês;
- HTML estático para o conteúdo principal;
- JavaScript somente para menu, busca e filtros;
- currículo em `assets/cv/`;
- Open Graph local em `assets/social/`.

## Notas de qualidade

O workflow do GitHub Pages executa as verificações estáticas antes do deploy. O relatório desta versão está em [`docs/TEST_REPORT.md`](docs/TEST_REPORT.md); decisões de conteúdo e apresentação estão registradas de forma curta em [`docs/DESIGN_STRATEGY.md`](docs/DESIGN_STRATEGY.md).
