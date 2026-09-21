# Registro canônico de evidências profissionais

Atualizado em **21/09/2026**. Este arquivo é a referência editorial para manter **currículo, portfólio e GitHub em sincronia**. Ele não substitui a evidência técnica dos repositórios; define quais afirmações podem ser resumidas publicamente, com qual estado e sem inflar maturidade.

O inventário e a classificação de cursos, badges e credenciais ficam em [`CREDENTIALS_EVIDENCE.md`](CREDENTIALS_EVIDENCE.md). Uma credencial pode validar aprendizagem prática sem transformar automaticamente a tecnologia em experiência profissional de produção.

## Posicionamento

**Analista de Automação e IA**

Narrativa central: entender o processo e as regras, conversar com usuários/stakeholders, construir a solução adequada, integrar sistemas, testar/UAT/homologar, implantar, treinar, monitorar/observar falhas, medir impacto e sustentar a operação.

O posicionamento prioriza vagas de **automação e IA aplicada** sem inflar senioridade. Integrações/APIs, sistemas internos e processos/BPMN aparecem como competências que sustentam esse foco, não como um terceiro posicionamento concorrente.

## Claims quantitativos aprovados

| Evidência | Wording público aprovado | Estado / limite | Fonte principal |
| --- | --- | --- | --- |
| Ambiente n8n | **10 mil+ execuções de workflows em produção** | volume do ambiente administrado; não atribuir a um único workflow nem afirmar “por mês” | perfil GitHub / Mala Direta |
| Proposta Comercial | **2–4 min → menos de 30 s em propostas simples; uso diário por 4 profissionais** | métrica do fluxo operacional já utilizado | case Vesper Propostas |
| Produção Operacional | **10+ PCs + 1 TV; 20+ profissionais; 9 setores** | implantação interna em produção | Produção Operacional |
| HelpDesk | **11 usuários** | uso interno; não inventar redução percentual de tempo | HelpDesk |
| Manutenção | **40+ ativos** | processo interno digitalizado com checklists/evidências/histórico | case de manutenção |
| Adoção | **30+ pessoas treinadas ou orientadas** | pessoas alcançadas; não converter em “30 treinamentos” | experiência Grupo Vesper |
| Instrutor freelancer | **aulas pagas de informática desde out. 2024; rotina atual semanal de ~3h** | públicos de diferentes idades/níveis; não inventar quantidade total de alunos | relato profissional do autor |
| Dados e BI | **Power BI/Excel/Power Query usados em dashboards e análises para produção, compras e estoque** | uso profissional atual; não inventar número de dashboards/usuários sem nova evidência | experiência Grupo Vesper |
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

`n8n self-hosted` · `Power Automate Cloud/Desktop` · `Python` · `FastAPI` · `APIs REST/JSON` · `webhooks` · `OAuth 2.0` · `WhatsApp Cloud API` · `SQL` · `PostgreSQL` · `Redis` · `Docker` · `Power BI` · `DAX` · `Power Query` · `Excel/Google Sheets` · `VBA` · `BPMN` · `AS-IS/TO-BE` · levantamento de requisitos · stakeholders · testes/UAT · implantação · treinamento · sustentação/melhoria contínua

n8n, Power Automate e Python/APIs formam o núcleo de automação. Power BI/Power Query/Excel/VBA formam o núcleo de dados/BI. **Logs, monitoramento/observabilidade, troubleshooting, tratamento de erros, retries, idempotência, backups e auditoria** podem aparecer quando sustentados pela evidência do projeto.

### Ferramentas complementares / contextuais

`Power Apps` · `Make` · `Zapier` · `Selenium` · `Playwright` · `Puppeteer` · `PyAutoGUI` · `UiPath`

Podem aparecer no portfólio/LinkedIn quando relevantes. No currículo principal, entram somente quando a vaga justificar ou quando houver espaço sem competir com o núcleo. Power Apps possui validação prática por Microsoft Applied Skills; as ferramentas de automação web/RPA foram relatadas como já utilizadas, mas não recebem claim de produção específico sem evidência pública adicional.

Não usar `CRM` isoladamente como skill do currículo geral: é amplo demais sem produto/plataforma específica. A palavra pode aparecer dentro de cases reais quando a integração correspondente exigir.

### Competências práticas e credencializadas

`Microsoft Foundry` · `MCP com agentes` · `Power Apps Canvas Apps` · `Make AI Agent Builder` · `UiPath Automation Business Analysis`

Além das Microsoft Applied Skills, o autor relata prática própria com **servidor MCP, cliente MCP, tools e integração com agentes**. MCP pode aparecer como competência prática; não atribuir escala/produção específica sem evidência de projeto. Make/UiPath/Power Apps continuam úteis como ferramentas complementares quando não houver case profissional equivalente.

### IA aplicada

No currículo principal podem aparecer, porque existe base verificável ou prática declarada: **IA generativa/LLMs · APIs de LLM · Prompt Engineering · agentes de IA · RAG/grounding · LangChain · MCP · human-in-the-loop · evals**.

Postagem Redes fornece evidência pública de grounding com LangChain/Supabase/n8n, revisão humana, guardrails, Prompt Engineering e evals sintéticos/reproduzíveis. O autor também relata uso de **Supabase e Qdrant** em RAG e prática completa de MCP. **LangGraph e CrewAI** ficam como estudo/protótipo e não entram no currículo principal como profundidade profissional.

Não afirmar sem evidência que o RAG atual usa `pgvector`, Pinecone, reranker customizado ou multi-agent supervisor. `Qdrant` e `Redis` podem aparecer como competências práticas, sem atribuir produção/escala específica quando não houver case público.

### Dados, BI e ensino

O autor relata uso profissional e ensino pago desde out. 2024 de **Power BI, DAX, Power Query, Excel/Google Sheets e VBA**, além de Word, PowerPoint, Outlook, Windows e fundamentos de Linux. Na Vesper, Power BI/Excel/Power Query apoiam dashboards e análises de produção, compras e estoque. O currículo pode apresentar a experiência como **Instrutor de Informática (Freelancer)** em paralelo à experiência principal.

### Confiabilidade e segurança

Valorizar quando sustentado pelo projeto: rastreabilidade, auditoria, logs, monitoramento/observabilidade, troubleshooting, tratamento de erros, retries, idempotência, alertas, backups, gestão de segredos, sanitização, revisão humana, read-only, hashes e isolamento de falhas.

No currículo principal, a forma prioritária é: **logs/monitoramento · tratamento de erros · retries · idempotência**. Detalhes como alertas, backups, hashes, filas e gestão de segredos ficam na experiência/cases quando agregarem evidência.

### Cloud e engenharia de software

A experiência Compass comprova prática com **AWS S3, Lambda, Glue/PySpark, Athena e QuickSight**, além de Python/SQL/Docker/ETL/Data Lake. Não classificar cloud como ausente; também não elevar isso a experiência enterprise atual em AWS.

FastAPI tem evidência independente em **Catálogo Operacional** e **CarreiraPessoal**; no currículo principal, porém, ele aparece como suporte técnico à automação e IA, sem disputar o posicionamento principal.

## Formação e credenciais resumíveis

No currículo principal de uma página, priorizar somente a camada de maior sinal e cortar antes de reduzir legibilidade:

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
- headline PT geral: **ANALISTA DE AUTOMAÇÃO E IA | n8n · Power Automate · Python**;
- headline EN geral: **AUTOMATION & AI ANALYST | n8n · Power Automate · Python**;
- seções explícitas `COMPETÊNCIAS TÉCNICAS / TECHNICAL SKILLS` e `EXPERIÊNCIA PROFISSIONAL / PROFESSIONAL EXPERIENCE`;
- dois projetos públicos de maior aderência, sem repetir a experiência;
- nenhuma soft-skill list, foto, barra de progresso, tabela visual ou buzzword sem prova;
- validação automática de uma página, texto extraído, links, renderização, área segura e legibilidade;
- fonte do conteúdo principal deve ficar em torno de 10 pt; metadados/contato devem permanecer legíveis e nunca forçar compressão desnecessária;
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

Sinais transversais que devem estar cobertos pelo documento geral quando sustentados por evidência: **n8n/workflow automation, Power Automate, Python, FastAPI, APIs REST/JSON, webhooks, OAuth, WhatsApp API, SQL/PostgreSQL, Redis, Power BI/Power Query, Excel/VBA, BPMN/AS-IS/TO-BE, requisitos/stakeholders, UAT, IA generativa/LLMs, Prompt Engineering, agentes, RAG/grounding, LangChain, MCP, evals, Git/CI-CD, logs, retries e idempotência**.

Empresas maiores tendem a adicionar governança, compliance, segurança, observabilidade e ferramentas enterprise; startups tendem a enfatizar autonomia, ponta a ponta, APIs, n8n/Make, Python/JS, agentes e troubleshooting. O currículo geral cobre o **núcleo comum**, sem copiar a cauda específica de cada vaga.

### Não reivindicar sem evidência suficiente

Mesmo quando aparecerem em vagas, não adicionar ao currículo geral ou elevar a “domínio” apenas por keyword matching:

- Process Mining como experiência profissional;
- UiPath Studio/Orchestrator/REFramework como desenvolvimento de produção;
- Automation Anywhere;
- Camunda e Airflow;
- SOAP/XML e middleware enterprise;
- Kafka, RabbitMQ, ActiveMQ ou mensageria distribuída em produção;
- SLI/SLO, OpenTelemetry, Datadog ou Grafana como observabilidade enterprise sem evidência;
- SAP/OIC/OFS/TOTVS ou ERP específico como domínio;
- multi-agent supervisor/arquitetura multiagente em produção;
- `pgvector`, Pinecone, Weaviate ou outro vector DB específico sem evidência direta;
- experiência profissional de desenvolvimento/produção em UiPath;
- título **UiPath Certified Automation Business Analyst Professional** sem aprovação no exame separado;
- experiência enterprise em Azure/GCP;
- Microsoft Foundry como profundidade de produção equivalente ao núcleo sem case específico;
- LangGraph/CrewAI como profundidade equivalente ao núcleo;
- senioridade “Pleno”, “Sênior”, “Especialista”, “Engineer” ou “Consultor” como cargo atual sem base formal.

Se uma vaga exigir uma dessas tecnologias como requisito obrigatório, tratar como **gap da vaga**, contexto de aprendizado ou direção futura; nunca inflar experiência.

## Curadoria por superfície

### Currículo principal — uma página

Manter **um currículo-base PT-BR**, duas variações direcionadas (IA/agentes e Power Platform/BI) e um espelho semântico EN do currículo-base. As variações mudam apenas headline, resumo, ordem/seleção de projetos e skills; fatos, datas e métricas permanecem idênticos.

A experiência profissional passa a carregar n8n/Power Automate, Proposta Comercial, sistemas internos, BI/dados, adoção e o trabalho paralelo como instrutor. A seção de projetos complementa:

Currículo-base:
1. Mala Direta — automação n8n, filas e confiabilidade em produção;
2. HelpDesk — uso interno por 11 pessoas, agente operacional e contexto técnico.

Variação IA/agentes:
1. HelpDesk;
2. Postagem Redes — Prompt Engineering, RAG/LangChain, human-in-the-loop, evals e APIs externas.

Variação Power Platform/BI:
1. Mala Direta;
2. Catálogo Operacional — dados, busca, integridade e uso diário.

### Portfólio — projetos principais

1. Mala Direta;
2. Vesper Propostas;
3. HelpDesk;
4. Postagem Redes.

O **Portal** permanece como arquitetura em **desenvolvimento/revalidação**, fora da vitrine principal até nova evidência justificar promoção. No mobile, apenas quatro projetos principais ficam visíveis antes da experiência; o arquivo secundário usa progressive disclosure. A homepage mostra apenas credenciais selecionadas; inventário completo fica em `/competencias/credenciais/` e `/en/credentials/`.

### GitHub

O README do perfil deve conduzir primeiro a cinco projetos:

1. MalaDireta;
2. HelpDesk;
3. PostagemRedes;
4. ProducaoOperacional;
5. CatalogoOperacional;
6. Central-ISO.

CarreiraPessoal continua como prova de engenharia/QA, mas não antecede HelpDesk na narrativa de Automação + IA. O README deve diferenciar **núcleo profissional**, **ferramentas contextuais** e **credenciais**. A versão inglesa permanece dedicada.

### Cases e READMEs individuais

Cada case deve provar problema, estado real, decisões, arquitetura quando útil, resultado, segurança/confiabilidade e como validar. Priorizar resumo rápido, métricas aprovadas, screenshots/demo sanitizados, testes/evals/CI quando existirem e limites honestos.

## Regra de atualização

Uma nova métrica ou mudança de estado deve nascer primeiro na evidência do projeto. Uma nova credencial deve ser classificada primeiro em `CREDENTIALS_EVIDENCE.md`. Depois, este registro e as superfícies públicas podem ser sincronizados. Nunca promover status, métrica, senioridade ou tecnologia apenas para melhorar apresentação ou ATS.


### Projeto de laboratório — Auditoria e Aprovação de Contratos

O sistema descrito com **Microsoft Forms → SharePoint → Approvals → HTTP → Power Automate Desktop → ERP legado**, incluindo tratamento Try/Catch e roteamento multinível, foi um **projeto de laboratório/estudo**.

Pode ser citado apenas como evidência de prática técnica em **Power Automate Cloud/Desktop, Approvals, SharePoint, WDL, HTTP e RPA**.  
**Não publicar como experiência profissional, implantação em cliente/empresa ou resultado real de negócio.**  
O claim **“12 dias → menos de 4 horas”** não deve aparecer em currículo, LinkedIn, portfólio ou bio como métrica real.

