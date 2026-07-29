# Estratégia de design — Registro de Sistemas em Operação

## Produto

Portfólio profissional de Maycon Ferreira para recrutadores, RH, gestores técnicos, desenvolvedores seniores e arquitetos que avaliam experiência em automação, IA, integrações e sistemas internos.

## Critério de sucesso

Em até 10 segundos, o visitante deve reconhecer nome, área e proposta de valor. Em aproximadamente dois minutos, deve encontrar resultados, abrir um case, consultar evidências, baixar o currículo e localizar contato.

## Conceito

**Registro de Sistemas em Operação** — uma publicação editorial e técnica sobre soluções que saíram de necessidades operacionais e passaram a ser usadas na rotina.

A identidade nasce de:

- hierarquia tipográfica;
- grid rigoroso e assimetria controlada;
- linhas, margens, índices e legendas;
- screenshots e diagramas reais;
- números sempre acompanhados de contexto;
- estados e limitações declarados;
- composição específica para cada case principal.

## O que foi rejeitado

- dashboard genérico;
- estética de startup de IA;
- neon, glow, glassmorphism e gradientes decorativos;
- órbitas, partículas, terminais falsos e hologramas;
- bento grid e excesso de cards;
- mockups falsos de dispositivos;
- movimento contínuo;
- métricas, integrações ou imagens inventadas.

## Sistema visual

- Base clara: papel técnico quente e branco de leitura.
- Texto: grafite de alto contraste.
- Acento principal: laranja operacional.
- Azul: referências técnicas e links.
- Verde, amarelo e vermelho: estados semânticos.
- Tipografia: famílias de sistema com títulos condensados e metadados monoespaçados.
- Forma: cantos discretos, linhas de 1 px, pouca sombra e espaço negativo.

## Arquitetura da informação

1. apresentação e posicionamento;
2. resultados contextualizados;
3. método de trabalho;
4. seis sistemas principais;
5. índice completo de projetos;
6. competência → evidência;
7. incidentes e aprendizados;
8. experiência, formação e certificações;
9. contato e currículo.

Cada case possui URL própria, versão em português e inglês, estado real, contexto, responsabilidade, arquitetura, decisões, resultados, evidências, limitações e caminho de evolução.

## Movimento e JavaScript

O conteúdo principal existe em HTML estático. JavaScript é melhoria progressiva para menu, busca e filtros. O movimento é breve e funcional, com respeito a `prefers-reduced-motion`.

## Limites

O site não apresenta projetos privados como código público e não transforma arquitetura de referência em implantação concluída. Métricas de campo, como Core Web Vitals, precisam ser medidas novamente depois do deploy no domínio real.
