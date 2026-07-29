# Validação do portfólio

## Objetivo

Confirmar estrutura, links, responsividade, acessibilidade básica e funcionamento progressivo antes da publicação.

## Verificações automatizadas

```bash
python scripts/validate_site.py
node --check js/site.js
```

O workflow do GitHub Pages executa essas verificações antes do deploy.

## Verificações de navegador

- página inicial em português e inglês;
- 18 cases em cada idioma;
- menu móvel;
- busca e filtros;
- links do currículo, GitHub, LinkedIn, e-mail e WhatsApp;
- navegação por teclado;
- movimento reduzido;
- larguras 1440, 1024, 768, 390 e 360 px;
- ausência de overflow horizontal;
- conteúdo principal legível sem JavaScript.

## Limite honesto

Métricas de campo como LCP, INP e CLS devem ser medidas novamente depois da publicação no domínio real.
