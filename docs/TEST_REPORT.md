# Verificação da versão publicada

Atualizado em **6 de agosto de 2026**, após nova auditoria dos repositórios, métricas, currículo, posicionamento profissional, consistência bilíngue, rotas canônicas e apresentação visual.

## Currículos PT-BR e inglês

A validação automatizada exige:

- uma página A4 e uma única coluna;
- texto selecionável e extraível por `pypdf` e PyMuPDF;
- seções convencionais em ordem: resumo, habilidades, experiência, projetos, formação, certificações e idiomas;
- cinco links clicáveis e somente os dois PDFs vigentes;
- título profissional neutro em senioridade: **Analista de Automação, IA e Integrações**;
- cargo formal atual preservado;
- datas consistentes;
- margens seguras, fonte mínima de 8 pontos e ausência de colisões;
- renderização raster válida e PDF não escaneado.

### Evidências permitidas nos currículos

- 10 mil+ execuções atribuídas à instância n8n completa;
- Vesper Propostas de 2–4 minutos para menos de 30 segundos em propostas simples, com uso diário por quatro profissionais;
- Produção Operacional em 10+ computadores e uma TV, apoiando 20+ profissionais em nove setores;
- HelpDesk utilizado por 11 usuários;
- treinamento e orientação de 30+ pessoas;
- Mala Direta com seis campanhas sobre base de 1.020 contatos, incluindo uma campanha para 900+ destinatários;
- Catálogo Operacional com 24 categorias e 480+ códigos, uso diário por três usuários e consulta pela gestão;
- Postagem Redes com três workflows, 58 nós no fluxo de ações e Facebook/Instagram exercitados em teste;
- Programa Compass com dez sprints e pipeline de dados em AWS;
- Portal em desenvolvimento, com Procurement implementado em sandbox e revalidação do head atual antes do piloto.

### Claims bloqueados

- métrica Compass `3h → 5min` como argumento de contratação, pois o artefato histórico exato não foi isolado;
- `text-to-video` como competência central sem prova pública direta;
- 11 computadores no Produção Operacional;
- 10 mil execuções atribuídas exclusivamente à Mala Direta;
- `PlanilhaCompras`, `ProcureFlow` ou `Portal Vesper` como identidades atuais;
- Portal apresentado como produção multiempresa, piloto iniciado ou head atual plenamente validado;
- experiência pessoal ou acadêmica somada artificialmente como anos de experiência profissional.

## Portfólio

O validador estático confere:

- **45 páginas HTML** no total;
- **17 cases ativos em português e 17 equivalentes em inglês**;
- **seis redirects legados** preservando links compartilhados;
- **38 URLs canônicas no sitemap**, sem rotas antigas;
- títulos, `lang`, meta descriptions, canonical, `hreflang` e controle de tema;
- referências locais existentes, imagens com texto alternativo e provas visuais rastreáveis;
- seis indicadores principais ligados aos cases correspondentes;
- links ingleses permanecendo dentro de `/en/cases/`;
- identidade **Catálogo Operacional de Compras** e repositório canônico `CatalogoOperacional`;
- Portal sem identidade específica da empresa e com status de revalidação pré-piloto;
- Programa Compass consolidado em um case completo, sem case ativo baseado na métrica não reproduzível;
- competências ligadas a automação, IA, integrações, backend, dados, AWS, confiabilidade e governança.

### Rotas canônicas verificadas

- `/cases/catalogo-operacional-compras/`;
- `/en/cases/operational-procurement-catalog/`;
- `/cases/portal/`;
- `/en/cases/portal/`;
- `/cases/compass/`;
- `/en/cases/compass/`.

As rotas de `procureflow`, `portal-vesper` e `compass-automation`, em ambos os idiomas, existem somente como redirects compatíveis e ficam fora do sitemap.

## Inspeção em navegador

O smoke test com Chromium produz **32 capturas completas**:

- home PT-BR e inglês;
- competências PT-BR e inglês;
- Catálogo Operacional de Compras PT-BR e inglês;
- Portal PT-BR e inglês;
- desktop 1440 × 1000 e mobile 390 × 844;
- temas claro e escuro.

Em cada combinação são verificados:

- posicionamento profissional visível;
- tema aplicado;
- ausência de overflow horizontal;
- carregamento das imagens;
- ausência de texto recortado;
- links dos currículos atuais;
- seções estratégicas;
- funcionamento do menu móvel.

## Leitura como recrutador e ATS

A primeira tela e a primeira página precisam responder rapidamente:

1. qual função profissional está sendo apresentada;
2. quais problemas empresariais foram resolvidos;
3. quais tecnologias sustentam a atuação;
4. qual escala, adoção ou resultado foi observado;
5. qual é o estado real de cada entrega;
6. onde a evidência pode ser revisada.

A seleção dos quatro projetos no currículo foi distribuída por dimensão técnica:

- **Mala Direta:** n8n, escala e confiabilidade;
- **Catálogo Operacional:** backend, busca e integridade de dados;
- **Postagem Redes:** IA generativa e APIs externas;
- **Portal:** arquitetura full-stack e governança.

Produção Operacional, HelpDesk e Vesper Propostas permanecem na experiência profissional e no portfólio, evitando repetição na seção de projetos. Compass permanece na experiência porque adiciona dados, Docker e AWS sem competir com os cases operacionais atuais.

## Adequação por porte de empresa

- **pequenas empresas e indústrias:** destaca autonomia, implantação, treinamento e sustentação;
- **empresas médias:** equilibra impacto operacional, processos, integrações, backend e confiabilidade;
- **grandes empresas:** preserva cargo formal, distingue formação de produção e utiliza seções compatíveis com ATS;
- **empresas de tecnologia:** mostra código público, testes, CI, limites arquiteturais e estados de validação;
- **processos internacionais:** oferece currículo e portfólio em inglês, descrevendo o nível de inglês sem exagero.

## Limites declarados

Este relatório não afirma compatibilidade perfeita com todo ATS, aprovação automática em vagas, teste em todos os navegadores ou validação de ambientes privados. O Portal não é apresentado como produção multiempresa; o Catálogo não é apresentado como ERP; o Programa Compass não é apresentado como experiência de produção. A validação reduz riscos técnicos e editoriais, mas a correspondência final continua dependendo da vaga, das perguntas eliminatórias, dos filtros configurados e da leitura humana.
