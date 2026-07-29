# Relatório de testes — versão editorial

Data da execução: 29 de julho de 2026.

## Resultado

**Aprovado para publicação no GitHub Pages, com medição de desempenho de campo pendente após o deploy.**

## Validação estática

- 39 páginas HTML verificadas;
- página inicial PT e EN;
- 18 cases em português e 18 em inglês;
- referências locais e âncoras verificadas;
- ausência de IDs HTML duplicados;
- títulos e atributo `lang` presentes;
- currículo disponível nas rotas;
- sintaxe de `js/site.js` validada com Node.js.

## Testes de navegador

Foram executadas verificações em todas as páginas em viewport desktop e móvel:

- 39 páginas × 2 viewports = 78 verificações;
- nenhum overflow horizontal observado;
- nenhum erro de JavaScript ou exceção de página observado;
- título e `h1` presentes em todas as páginas;
- menu móvel abriu e fechou pelo teclado (`Escape`);
- índice exibiu 18 projetos;
- busca por `n8n` retornou resultados coerentes;
- filtro de agentes e IA aplicada funcionou;
- links para WhatsApp e currículo presentes;
- rotas dos cases e alternância de idioma verificadas.

## Resoluções e comportamentos cobertos

- desktop amplo;
- notebook;
- tablet;
- celular de 390 px;
- celular de 360 px;
- navegação por teclado;
- redução de movimento;
- conteúdo principal disponível sem depender da execução do JavaScript.

## Limites honestos

- O domínio público ainda precisa receber esta versão antes de uma auditoria final ao vivo.
- LCP, INP, CLS, cache de CDN e comportamento em redes corporativas só podem ser medidos corretamente depois da publicação.
- Links externos dependem da disponibilidade dos respectivos serviços.
- Projetos privados são apresentados por conteúdo sanitizado e não podem ser executados pelo visitante.
