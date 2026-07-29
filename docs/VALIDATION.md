# Verificações do site

## Verificações automatizadas

```bash
python scripts/validate_site.py
node --check js/site.js
```

O workflow do GitHub Pages executa essas verificações antes do deploy.

Esses comandos conferem a estrutura e o JavaScript antes do deploy. A checagem visual é feita no navegador, com atenção para leitura, teclado, mobile e rotas de currículo/contato. Métricas de campo são acompanhadas separadamente no domínio publicado.
