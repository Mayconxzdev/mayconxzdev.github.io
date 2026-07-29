# Verificação da versão publicada

Atualizado em 29 de julho de 2026, após a revisão visual, de conteúdo e de acessibilidade da versão pública.

## Confirmado nesta versão

- o validador estático conferiu 39 páginas HTML, 18 cases em português, 18 em inglês e 722 referências locais;
- todas as páginas possuem título, `lang`, descrição, canonical, controle de tema acessível e, fora da página 404, ligação `hreflang`;
- os 36 cases possuem uma evidência visual principal e todas as imagens públicas têm texto alternativo;
- os currículos PT-BR e em inglês existem no pacote publicado;
- `node --check js/site.js` passou;
- o workflow **Validate and deploy GitHub Pages** concluiu com sucesso no commit publicado;
- 38 rotas do sitemap foram renderizadas em 1440 × 900 e 390 × 844, nos temas claro e escuro: 152 combinações sem overflow horizontal, texto recortado, contraste insuficiente no teste automatizado ou links sem nome acessível;
- as galerias dos 36 cases foram percorridas em viewport móvel; as imagens com carregamento tardio concluíram sem falhas;
- o menu móvel abre, fecha com `Escape` e atualiza `aria-expanded` corretamente;
- o tema escolhido é restaurado após recarregar a página, inclusive na versão em inglês;
- a página 404 segue a mesma navegação, tema, metadata e contenção visual do restante do site.

## Revisão visual por amostragem

Foram inspecionadas visualmente a home em português no tema escuro, a home em inglês no tema claro e o case industrial em desktop e mobile no tema escuro. A revisão confirmou hierarquia legível, evidência visível na primeira leitura e ausência do antigo sobreposição sobre o título.

## O que não está alegado aqui

Este documento não afirma medição de Core Web Vitals de campo, testes em todos os navegadores e sistemas operacionais, validação de redes corporativas ou fluxos privados. Esses pontos dependem de medição contínua e dos respectivos ambientes.
