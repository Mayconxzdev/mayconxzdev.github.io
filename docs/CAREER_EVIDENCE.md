# Registro canônico de evidências profissionais

Atualizado em **24/08/2026**. Este arquivo é a referência editorial para manter **currículo, portfólio e GitHub em sincronia**. Ele não substitui a evidência técnica dos repositórios; define quais afirmações podem ser resumidas publicamente, com qual estado e sem inflar maturidade.

O inventário e a classificação de cursos, badges e credenciais ficam em [`CREDENTIALS_EVIDENCE.md`](CREDENTIALS_EVIDENCE.md). Uma credencial pode validar aprendizagem prática sem transformar automaticamente a tecnologia em experiência profissional de produção.

## Posicionamento

**Analista de Automação, IA e Integrações**

Narrativa central: entender o processo e as regras, conversar com usuários/stakeholders, construir a solução adequada, integrar sistemas, testar/UAT/homologar, implantar, treinar, monitorar/observar falhas, medir impacto e sustentar a operação.

O posicionamento é deliberadamente amplo sem inflar senioridade. Ele cobre o núcleo que se repete nas vagas de agosto/2026: automação de processos, integrações/APIs, sistemas internos, processos/BPMN e IA aplicada/agentes.

## Claims quantitativos aprovados

| Evidência | Wording público aprovado | Estado / limite | Fonte principal |
| --- | --- | --- | --- |
| Ambiente n8n | **10 mil+ execuções de workflows em produção** | volume do ambiente administrado; não atribuir a um único workflow nem afirmar “por mês” | perfil GitHub / Mala Direta |
| Proposta Comercial | **2–4 min → menos de 30 s em propostas simples; uso diário por 4 profissionais** | métrica do fluxo operacional já utilizado | case Vesper Propostas |
| Produção Operacional | **10+ PCs + 1 TV; 20+ profissionais; 9 setores** | implantação interna em produção | Produção Operacional |
| HelpDesk | **11 usuários** | uso interno; não inventar redução percentual de tempo | HelpDesk |
| Manutenção | **40+ ativos** | processo interno digitalizado com checklists/evidências/histórico | case de manutenção |
| Adoção | **30+ pessoas treinadas ou orientadas** | pessoas alcançadas; não converter em “30 treinamentos” | experiência Grupo Vesper |
| Mala Direta | **6 campanhas; base de 1.020 contatos; uma com 900+ destinatários** | produção; 10 mil+ execuções pertencem ao ambiente n8n, não a este projeto | Mala Direta |
| Mala Direta — arquitetura | **2 workflows; principal com 158 nós; 9 Data Tables** | snapshot sanitizado; evidência detalhada, não necessária no CV | Mala Direta |
| Catálogo Operacional | **24 categorias; 480+ códigos; uso diário por 3 pessoas** | operação interna atual | Catálogo Operacional |
| CarreiraPessoal | **v12.5.2; 283 testes Python; 102 famílias ATS; 11 coletores diretos** | produto pessoal em uso; repositório público sanitizado | CarreiraPessoal |
| Postagem Redes | **Facebook e Instagram exercitados/validados em teste; evals reproduzíveis** | não chamar de produção; X/LinkedIn dependem de condições externas | Postagem Redes |

## Estados editoriais

- **Em produção:** operação real recorrente e implantada.
- **Uso interno:** solução utilizada na rotina, sem transformar isso em produto homologado para terceiros.
- **Produto pessoal em uso:** solução realmente utilizada pelo autor, sem alegar adoção externa.
- **Validado em teste:** integração exercitada de forma controlada, sem alegação de produção.
- **Piloto técnico:** prova funcional para validar regra/processo, sem certificação ou homologação.
- **Desenvolvimento / revalidação:** implementação em evolução; não promover sem evidência correspondente.
- **Formação / histórico:** prova de aprendizado, não operação empresarial atual.

## Profundidade técnica

### Núcleo profissional

`n8n self-hosted` · `low-code/no-code` · `Python` · `FastAPI` · backend · `APIs REST` · `JSON` · `webhooks` · `OAuth 2.0` · `SQL` · `PostgreSQL` · `Docker` · `BPMN` · `AS-IS/TO-BE` · levantamento de requisitos · stakeholders · regras de negócio · documentação · testes · `UAT/homologação` · métricas de impacto · implantação · treinamento · sustentação/melhoria contínua

O termo **low-code/no-code** descreve a camada de orquestração visual já comprovada por n8n e não rebaixa a profundidade em Python/APIs. **Logs, monitoramento/observabilidade, troubleshooting, tratamento de erros, retries, idempotência, backups e auditoria** podem aparecer quando sustentados pela evidência do projeto.

### Ferramentas complementares / contextuais

`Power Apps` · `Power Automate` · `Make` · `Zapier`

Podem aparecer no currículo e páginas de competências para explicar contexto e melhorar clareza de ATS, **sempre diferenciadas do núcleo profissional**. Power Apps é capacidade validada em laboratório; Power Automate, Make e Zapier permanecem contextuais quando não há evidência equivalente de produção.

Não usar `CRM` isoladamente como skill do currículo geral: é amplo demais sem produto/plataforma específica. A palavra pode aparecer dentro de cases reais quando a integração correspondente exigir.

### Competências práticas credencializadas, ainda contextuais

`Microsoft Foundry` · `MCP com agentes` · `Power Apps Canvas Apps` · `Make AI Agent Builder` · `UiPath Automation Business Analysis`

As Microsoft Applied Skills validam tarefas práticas em laboratório. Make AI Agent Builder inclui assessment. UiPath Automation Business Analyst Professional Training valida formação estruturada no ciclo de análise/implementação. Isso permite mencionar **aprendizagem prática credencializada**, mas não produção equivalente ao núcleo.

### IA aplicada

No currículo geral podem aparecer, porque existe base verificável: **IA generativa/LLMs · APIs de LLM · agentes de IA · RAG/grounding · LangChain · human-in-the-loop · evals**.

Postagem Redes fornece evidência pública de grounding com LangChain/Supabase/n8n, revisão humana, guardrails e evals sintéticos/reproduzíveis. **MCP** possui validação prática por Microsoft Applied Skills e permanece contextual enquanto não houver evidência de produção equivalente. **LangGraph e CrewAI** ficam como estudo/protótipo e não entram no currículo geral como profundidade profissional.

Não afirmar sem evidência que o RAG atual usa `pgvector`, Pinecone, Qdrant, reranker customizado, multi-agent supervisor, Redis ou filas distribuídas.

### Confiabilidade e segurança

Valorizar quando sustentado pelo projeto: rastreabilidade, auditoria, logs, monitoramento/observabilidade, troubleshooting, tratamento de erros, retries, idempotência, alertas, backups, gestão de segredos, sanitização, revisão humana, read-only, hashes e isolamento de falhas.

No currículo geral, a forma prioritária é: **logs · monitoramento/observabilidade · tratamento de erros · retries · idempotência · segurança de integrações/segredos**. Detalhes como alertas, backups, hashes e filas ficam na experiência/cases quando agregarem evidência.

### Cloud e engenharia de software

A experiência Compass comprova prática com **AWS S3, Lambda, Glue/PySpark, Athena e QuickSight**, além de Python/SQL/Docker/ETL/Data Lake. Não classificar cloud como ausente; também não elevar isso a experiência enterprise atual em AWS.

FastAPI tem evidência independente em **Catálogo Operacional** e **CarreiraPessoal**, portanto `backend` é um descritor defensável no currículo geral.

## Formação e credenciais resumíveis

No currículo geral de uma página, priorizar somente a camada de maior sinal e cortar antes de reduzir legibilidade:

- Microsoft Applied Skills — Foundry Agents, MCP Tools with Agents e Canvas Apps with Power Apps;
- UiPath Academy — **Automation Business Analyst Professional Training**, como training/badge, não UiPath Certified Professional;
- n8n Academy — N8N102 e N8N103, como certificados de conclusão;
- Make Academy — AI Agent Builder.

**FIRJAN SENAI — Agentes e Automações (40h)** permanece relevante no portfólio/LinkedIn e pode retornar ao PDF se houver espaço sem prejudicar leitura. Google AI Essentials, ENAP, OpenAI Academy, badges Microsoft Learn e DIO/Santander permanecem no inventário detalhado.

Nunca transformar achievement, curso, badge ou trilha em “certificação profissional” quando a instituição não a classificar assim. O agregado pode ser descrito como **55+ registros de aprendizagem/credenciais**, nunca “55+ certificações”.

## Regra de contato, ATS e legibilidade

O currículo geral deve manter telefone, e-mail completo, LinkedIn, GitHub e portfólio **como texto extraível e hyperlinks clicáveis**. Não depender de ícones, caixas de texto, header/footer ou imagens.

Regras de release:

- uma página A4;
- uma coluna;
- PDF textual/selecionável;
- PT-BR e EN como espelhos semânticos;
- headline PT: **ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES**;
- headline EN: **AUTOMATION, AI & INTEGRATIONS ANALYST**;
- seções explícitas `COMPETÊNCIAS TÉCNICAS / TECHNICAL SKILLS` e `EXPERIÊNCIA PROFISSIONAL / PROFESSIONAL EXPERIENCE`;
- quatro projetos complementares, sem repetir a experiência;
- nenhuma soft-skill list, foto, barra de progresso, tabela visual ou buzzword sem prova;
- validação automática de uma página, texto extraído, links, renderização, área segura e legibilidade;
- fonte do conteúdo principal deve ficar em torno de 9,5 pt ou acima; metadados/contato não podem cair abaixo do limite visual de release;
- cortar conteúdo secundário antes de reduzir fonte.

## Vocabulário de mercado — auditoria 24/08/2026

Famílias de busca relevantes, sem alterar o cargo formal no Grupo Vesper:

- Analista de Automação e Integrações;
- Analista de Automação de Processos e IA;
- Analista de Automação Inteligente;
- Analista de Processos e Automação;
- Analista de Sistemas e Processos;
- Analista de Integrações / Sistemas;
- Automation Business Analyst / Business Process Automation Analyst;
- Desenvolvedor de Automação e Integrações — Júnior / Pleno inicial.

Sinais transversais que devem estar cobertos pelo documento geral quando sustentados por evidência: **n8n/workflow automation, low-code/no-code, Python, FastAPI/backend, APIs REST, JSON, webhooks, OAuth, SQL/PostgreSQL, BPMN/AS-IS/TO-BE, requisitos/stakeholders, documentação, UAT, métricas de impacto, IA generativa/LLMs, agentes, RAG/grounding, LangChain, evals, Git/CI-CD, logs, monitoramento/observabilidade, retries, idempotência e segurança de integrações**.

Empresas maiores tendem a adicionar governança, compliance, segurança, observabilidade e ferramentas enterprise; startups tendem a enfatizar autonomia, ponta a ponta, APIs, n8n/Make, Python/JS, agentes e troubleshooting. O currículo geral cobre o **núcleo comum**, sem copiar a cauda específica de cada vaga.

### Não reivindicar sem evidência suficiente

Mesmo quando aparecerem em vagas, não adicionar ao currículo geral ou elevar a “domínio” apenas por keyword matching:

- Process Mining como experiência profissional;
- UiPath Studio/Orchestrator/REFramework como desenvolvimento de produção;
- Automation Anywhere;
- Camunda e Airflow;
- SOAP/XML e middleware enterprise;
- Kafka, RabbitMQ, ActiveMQ ou mensageria distribuída em produção;
- Redis/queue mode/workers distribuídos sem evidência;
- SLI/SLO, OpenTelemetry, Datadog ou Grafana como observabilidade enterprise sem evidência;
- SAP/OIC/OFS/TOTVS ou ERP específico como domínio;
- multi-agent supervisor/arquitetura multiagente em produção;
- `pgvector`, Pinecone, Qdrant, Weaviate ou outro vector DB específico sem evidência direta;
- experiência profissional de desenvolvimento/produção em UiPath;
- título **UiPath Certified Automation Business Analyst Professional** sem aprovação no exame separado;
- experiência enterprise em Azure/GCP;
- Microsoft Foundry/MCP como profundidade de produção equivalente ao núcleo;
- LangGraph/CrewAI como profundidade equivalente ao núcleo;
- senioridade “Pleno”, “Sênior”, “Especialista”, “Engineer” ou “Consultor” como cargo atual sem base formal.

Se uma vaga exigir uma dessas tecnologias como requisito obrigatório, tratar como **gap da vaga**, contexto de aprendizado ou direção futura; nunca inflar experiência.

## Curadoria por superfície

### Currículo geral — uma página

Manter **um único currículo geral PT-BR e um espelho semântico EN**. Não criar versões A/B/C por família de vaga.

A experiência profissional já carrega n8n, Proposta Comercial, Produção/Manutenção, HelpDesk e adoção. A seção de projetos complementa:

1. Mala Direta — automação/n8n e confiabilidade;
2. CarreiraPessoal — produto, arquitetura, evidências e QA;
3. Catálogo Operacional — backend, busca e integridade de dados;
4. Postagem Redes — IA aplicada, RAG/LangChain, human-in-the-loop, evals e APIs externas.

Mala Direta prioriza escala operacional, fila/deduplicação/cancelamento/retry/auditoria; a contagem de 158 nós fica no portfólio. Postagem Redes prioriza RAG/LangChain, human-in-the-loop, evals, idempotência e isolamento de falhas.

### Portfólio — projetos principais

1. Mala Direta;
2. Produção Operacional;
3. Vesper Propostas;
4. CarreiraPessoal;
5. Catálogo Operacional;
6. Postagem Redes.

O **Portal** permanece como arquitetura em **desenvolvimento/revalidação**, fora da vitrine principal até nova evidência justificar promoção. No mobile, seis projetos principais ficam visíveis; o arquivo secundário pode usar progressive disclosure desde que busca/filtros revelem todo o conjunto. A homepage mostra apenas credenciais selecionadas; inventário completo fica em `/competencias/credenciais/` e `/en/credentials/`.

### GitHub

O README do perfil deve conduzir primeiro a cinco projetos:

1. MalaDireta;
2. ProducaoOperacional;
3. CarreiraPessoal;
4. CatalogoOperacional;
5. PostagemRedes.

HelpDesk é a sexta opção natural para pin. O README deve diferenciar **núcleo profissional**, **ferramentas contextuais** e **credenciais**. A versão inglesa permanece dedicada.

### Cases e READMEs individuais

Cada case deve provar problema, estado real, decisões, arquitetura quando útil, resultado, segurança/confiabilidade e como validar. Priorizar resumo rápido, métricas aprovadas, screenshots/demo sanitizados, testes/evals/CI quando existirem e limites honestos.

## Regra de atualização

Uma nova métrica ou mudança de estado deve nascer primeiro na evidência do projeto. Uma nova credencial deve ser classificada primeiro em `CREDENTIALS_EVIDENCE.md`. Depois, este registro e as superfícies públicas podem ser sincronizados. Nunca promover status, métrica, senioridade ou tecnologia apenas para melhorar apresentação ou ATS.
