# Registro canônico de evidências profissionais

Atualizado em **19/08/2026**. Este arquivo é a referência editorial para manter **currículo, portfólio e GitHub em sincronia**. Ele não substitui a evidência técnica dos repositórios; define quais afirmações podem ser resumidas publicamente, com qual estado e sem inflar maturidade.

O inventário e a classificação de cursos, badges e credenciais ficam em [`CREDENTIALS_EVIDENCE.md`](CREDENTIALS_EVIDENCE.md). Uma credencial pode validar aprendizagem prática sem transformar automaticamente a tecnologia em experiência profissional de produção.

## Posicionamento

**Analista de Automação, IA e Integrações**

Narrativa central: entender o processo e as regras, conversar com usuários/stakeholders, construir a solução adequada, integrar sistemas, testar/homologar, implantar, treinar, monitorar falhas e sustentar a operação.

Este posicionamento é deliberadamente amplo sem inflar senioridade. Ele cobre as famílias recorrentes no mercado de agosto/2026: automação de processos, automação inteligente, integrações/APIs, sistemas internos, processos/BPMN e IA aplicada/agentes.

## Claims quantitativos aprovados

| Evidência | Wording público aprovado | Estado / limite | Fonte principal |
| --- | --- | --- | --- |
| Ambiente n8n | **10 mil+ execuções de workflows em produção** | volume do ambiente administrado, não de um único workflow e não afirmar “por mês” | perfil GitHub / Mala Direta |
| Proposta Comercial | **2–4 min → menos de 30 s em propostas simples; uso diário por 4 profissionais** | a métrica pertence ao fluxo operacional já utilizado; uma nova candidata técnica não deve ser confundida com homologação | case Vesper Propostas |
| Produção Operacional | **10+ PCs + 1 TV; 20+ profissionais; 9 setores** | implantação interna em produção | Produção Operacional |
| HelpDesk | **11 usuários** | uso interno; não inventar redução percentual de tempo de atendimento | HelpDesk |
| Manutenção | **40+ ativos** | processo interno digitalizado com checklists/evidências/histórico | case de manutenção |
| Adoção | **30+ pessoas treinadas ou orientadas** | pessoas alcançadas nas soluções implantadas; não converter em “30 treinamentos” | experiência Grupo Vesper |
| Mala Direta | **6 campanhas; base de 1.020 contatos; uma com 900+ destinatários** | produção; não atribuir as 10 mil+ execuções somente a este projeto | Mala Direta |
| Mala Direta — arquitetura | **2 workflows; principal com 158 nós; 9 Data Tables** | snapshot público sanitizado; a contagem de nós é evidência detalhada, não precisa ocupar o currículo geral | Mala Direta |
| Catálogo Operacional | **24 categorias; 480+ códigos; uso diário por 3 pessoas** | operação interna atual | Catálogo Operacional |
| CarreiraPessoal | **v12.5.2; 283 testes Python; 102 famílias ATS/plataformas; 11 coletores diretos** | produto pessoal em uso; repositório público é edição sanitizada | CarreiraPessoal |
| Postagem Redes | **Facebook e Instagram validados em teste; evals offline reproduzíveis** | não chamar de produção; X e LinkedIn dependem de condições externas | Postagem Redes |

## Estados editoriais

Use os estados abaixo de forma consistente:

- **Em produção:** operação real recorrente e implantada.
- **Uso interno:** solução utilizada na rotina, sem transformar isso automaticamente em produto homologado para terceiros.
- **Produto pessoal em uso:** solução que eu realmente utilizo, sem alegar adoção externa.
- **Validado em teste:** integração exercitada de forma controlada, sem alegação de produção.
- **Piloto técnico:** prova funcional para validar regras/processo, sem certificação ou homologação.
- **Desenvolvimento / revalidação:** implementação em evolução; não promover para piloto ou produção sem evidência correspondente.
- **Formação / histórico:** projeto ou programa que prova aprendizado, não operação empresarial atual.

## Profundidade técnica

### Núcleo profissional

`n8n self-hosted` · `low-code/no-code` · `Python` · `FastAPI` · `APIs REST/JSON` · `webhooks` · `OAuth 2.0` · `SQL/PostgreSQL` · `Docker` · `BPMN` · `AS-IS/TO-BE` · levantamento de requisitos · stakeholders · regras de negócio · testes · `UAT/homologação` · documentação · implantação · treinamento · sustentação

O termo **low-code/no-code** descreve a camada de orquestração visual já comprovada por n8n e não rebaixa a profundidade técnica em Python/APIs. **Troubleshooting, tratamento de erros, logs/monitoramento, retries e idempotência** podem aparecer porque são sustentados por operação e projetos reais.

### Ferramentas complementares / contextuais

`Power Platform (Power Apps/Power Automate)` · `Make` · `Zapier` · `CRM`

Essas ferramentas podem aparecer em currículo e páginas de competências quando ajudarem ATS/recrutador ou explicarem um contexto real, **sempre diferenciadas do núcleo profissional**. Power Apps é capacidade validada em laboratório; Power Automate/Make/Zapier são contextuais. Não apresentá-las no mesmo nível de profundidade do trabalho comprovado com n8n, Python e APIs.

### Competências práticas credencializadas, ainda contextuais

`Microsoft Foundry` · `MCP com agentes` · `Power Apps Canvas Apps` · `Make AI Agent Builder` · `UiPath Automation Business Analysis`

As Microsoft Applied Skills validam tarefas práticas em laboratório, Make AI Agent Builder valida uma trilha com assessment e UiPath Automation Business Analyst Professional Training valida formação estruturada no ciclo de análise/implementação de automação. Isso permite mencionar essas competências como **aprendizagem prática credencializada**, mas não como experiência profissional de produção equivalente ao núcleo.

### IA aplicada

Pode aparecer no currículo geral como **IA generativa/LLMs, agentes de IA, RAG/grounding, human-in-the-loop e evals offline reproduzíveis**. Postagem Redes fornece evidência pública de grounding, revisão humana, guardrails e evals sintéticos. **MCP** possui validação prática externa por Microsoft Applied Skills, mas permanece contextual enquanto não houver evidência de produção. **LangGraph e CrewAI** continuam no material de estudo/contexto e não devem ser elevados ao mesmo nível do núcleo profissional.

Não afirmar sem evidência que o RAG atual usa `pgvector`, Pinecone, Qdrant, função de relevância customizada, multi-agent supervisor, Redis ou filas distribuídas. A implementação pública aprovada é a documentada em cada projeto.

### Confiabilidade e segurança

Valorizar quando sustentado pelo projeto: rastreabilidade, auditoria, logs/monitoramento, troubleshooting, tratamento de erros, retries, idempotência, filas quando realmente existentes no projeto, alertas, backups, gestão de segredos, sanitização, revisão humana, read-only, hashes e isolamento de falhas.

No currículo geral, priorizar **logs/monitoramento · troubleshooting · tratamento de erros · retries · idempotência · segurança de integrações · gestão de segredos**. Alertas/backups continuam como evidência detalhada na experiência e nos repositórios, sem consumir espaço adicional no bloco de competências.

### Cloud e engenharia de software

A experiência da Compass prova prática com **AWS S3, Lambda, Glue/PySpark, Athena e QuickSight**, além de Python/SQL/Docker/ETL/Data Lake. Portanto, não classificar cloud como “ausente”. Também não elevar essa experiência histórica a “AWS em produção enterprise atual”.

FastAPI não está restrito a scripts dentro do n8n: **Catálogo Operacional** e **CarreiraPessoal** já fornecem evidência independente de backend/aplicação. Não inventar OAuth em endpoints FastAPI, microserviços ou arquitetura distribuída quando o repositório correspondente não comprovar.

## Formação e credenciais resumíveis

O currículo geral de uma página deve priorizar somente a camada de maior sinal:

- Microsoft Applied Skills — agentes no Microsoft Foundry, MCP com agentes e Canvas Apps com Power Apps;
- UiPath Academy — **Automation Business Analyst Professional Training**, como training/badge, não UiPath Certified Professional;
- n8n Academy — N8N102 e N8N103, como **certificados de conclusão**, não certificações profissionais;
- Make Academy — AI Agent Builder;
- FIRJAN SENAI — Agentes de IA e Automações (40h).

Google AI Essentials, ENAP, OpenAI Academy, badges Microsoft Learn e DIO/Santander continuam no inventário detalhado/LinkedIn, mas não precisam ocupar o currículo geral quando competem por espaço com experiência, resultados e credenciais de maior sinal.

Não transformar achievement, curso, badge ou trilha em “certificação profissional” quando a instituição não a classificar dessa forma. O agregado público pode ser descrito como **55+ registros de aprendizagem/credenciais**, nunca como “55+ certificações”.

## Regra de contato e parsing ATS

No currículo geral, os caminhos de contato essenciais devem existir **como texto extraível e também como hyperlinks clicáveis**. Não depender somente de rótulos como “E-mail”, “LinkedIn”, “GitHub” ou “Portfólio”.

Expor de forma compacta:

- telefone;
- endereço de e-mail completo;
- URL/slug do LinkedIn;
- URL do GitHub;
- URL do portfólio.

A apresentação pode usar duas linhas para preservar legibilidade. O validador do currículo deve falhar se e-mail, LinkedIn, GitHub ou portfólio deixarem de aparecer no texto extraído, mesmo que a anotação clicável continue existindo.

## Vocabulário de mercado — auditoria 19/08/2026

Famílias de busca relevantes, sem alterar o cargo formal no Grupo Vesper:

- Analista de Automação e Integrações;
- Analista de Automação de Processos e IA;
- Analista de Automação Inteligente;
- Analista de Processos e Automação;
- Analista de Sistemas e Processos;
- Analista de Integrações / Sistemas;
- Automation Business Analyst / Business Process Automation Analyst;
- Desenvolvedor de Automação e Integrações — Júnior / Pleno inicial.

A amostra de mercado revisada em agosto de 2026 reforça como sinais recorrentes e transversais: **n8n/workflow automation, low-code/no-code, Python, FastAPI, APIs REST/webhooks/OAuth/JSON, SQL/PostgreSQL, BPMN/AS-IS/TO-BE, requisitos/stakeholders, documentação, UAT/homologação, monitoramento/confiabilidade, troubleshooting, IA generativa/LLMs, agentes de IA, RAG/grounding e segurança de integrações**.

Empresas maiores tendem a adicionar governança, UAT, compliance, segurança, observabilidade e ferramentas enterprise; startups tendem a enfatizar autonomia, entrega ponta a ponta, APIs, n8n/Make, Python/JS, agentes e troubleshooting. O currículo geral deve cobrir o **núcleo comum**, não copiar a cauda específica de cada vaga.

### Não reivindicar sem evidência suficiente

Mesmo quando aparecerem em vagas relacionadas, não adicionar ao currículo geral ou elevar a “domínio” apenas por keyword matching:

- Process Mining como experiência prática/profissional;
- UiPath Studio/Orchestrator/REFramework como desenvolvimento de produção;
- Automation Anywhere;
- Camunda e Airflow;
- SOAP/XML e middleware enterprise;
- Kafka, RabbitMQ, ActiveMQ ou mensageria/event-driven em produção;
- Redis/queue mode/workers distribuídos sem evidência do projeto;
- SLI/SLO, OpenTelemetry, Datadog, Grafana ou observabilidade enterprise sem evidência;
- SAP/OIC/OFS ou ERP específico como domínio;
- multi-agent supervisor/arquitetura multiagente em produção;
- `pgvector`, Pinecone, Qdrant ou outro vector DB específico sem evidência direta do projeto;
- experiência profissional de desenvolvimento/produção em UiPath;
- título **UiPath Certified Automation Business Analyst Professional** sem aprovação no exame separado;
- experiência de produção enterprise em Azure/GCP;
- Microsoft Foundry/MCP como profundidade de produção equivalente ao núcleo profissional;
- LangGraph/CrewAI como profundidade equivalente ao núcleo profissional;
- senioridade “Pleno”, “Sênior”, “Especialista”, “Engineer” ou “Consultor” como cargo atual sem base formal.

Se uma vaga exigir uma dessas tecnologias como requisito obrigatório, tratar como **gap da vaga**, formação contextual quando houver credencial correspondente ou direção de aprendizado futura; nunca como oportunidade para inflar experiência.

## Correções de pesquisas externas recebidas em 19/08/2026

Relatórios externos podem ser usados para descobrir hipóteses de mercado, mas não como fonte de verdade sobre a experiência pessoal. Rejeitar recomendações que alterem fatos. Exemplos já identificados:

- graduação correta: **Tecnólogo em Análise e Desenvolvimento de Sistemas — UNISUAM**, não bacharelado em Sistemas de Informação;
- `10 mil+` significa execuções do ambiente administrado, não “10 mil+ por mês”;
- não existe evidência aprovada de “40% de redução no tempo médio de resposta” do HelpDesk;
- não existe evidência aprovada de agente multiagente com Supervisor Agent + Redis;
- não existe evidência aprovada de RAG com `pgvector` e função de relevância personalizada;
- cloud/AWS não está ausente: existe evidência prática histórica na Compass;
- FastAPI não está limitado a scripts dentro do n8n;
- Automation Business Analyst Professional Training é **training/badge**, não a certificação profissional obtida por exame.

## Curadoria por superfície

### Currículo geral — 1 página

Manter **um único currículo geral**. Não criar versões A/B/C por família de vaga. A experiência profissional já carrega n8n, Proposta Comercial, Produção/Manutenção, HelpDesk e adoção. A seção de projetos complementa sem repetir:

1. Mala Direta — automação/n8n e confiabilidade;
2. CarreiraPessoal — produto, arquitetura, evidências e QA;
3. Catálogo Operacional — backend, busca e integridade de dados;
4. Postagem Redes — IA aplicada, RAG, evals e APIs externas.

No currículo geral, Mala Direta deve priorizar **escala operacional + fila por destinatário + deduplicação + cancelamento + retry + auditoria**. A contagem de 158 nós permanece disponível no GitHub/portfólio como evidência detalhada, sem ser necessária no CV.

Postagem Redes deve priorizar **RAG/grounding + human-in-the-loop + evals offline reproduzíveis + idempotência + isolamento de falhas**, em vez de listar vários provedores de LLM ou frameworks.

Ferramentas complementares/contextuais só entram no bloco de competências com qualificador de profundidade; não devem deslocar resultados, BPMN, RAG, UAT ou confiabilidade. Credenciais entram em bloco próprio e curto.

### Portfólio — projetos principais

1. Mala Direta;
2. Produção Operacional;
3. Vesper Propostas;
4. CarreiraPessoal;
5. Catálogo Operacional;
6. Postagem Redes.

O **Portal** permanece como recorte de arquitetura em **desenvolvimento/revalidação**, fora da vitrine principal até existir nova evidência de maturidade que justifique promoção.

No mobile, os seis projetos principais permanecem integralmente visíveis. O arquivo secundário pode usar progressive disclosure para reduzir fadiga de rolagem, desde que busca e filtros revelem o conjunto completo e o desktop não esconda projetos.

A homepage mostra apenas credenciais selecionadas de alto sinal; o inventário completo fica em `/competencias/credenciais/` e `/en/credentials/`.

### GitHub

O README do perfil deve apontar primeiro para projetos que provam trabalho real e não apenas amplitude técnica. A documentação oficial do GitHub recomenda destacar **3–5 projetos** para avaliação de contratação. Portanto, a recomendação editorial passa a ser **cinco prioridades no texto**, embora a interface do GitHub permita até seis pins:

1. MalaDireta;
2. ProducaoOperacional;
3. CarreiraPessoal;
4. CatalogoOperacional;
5. PostagemRedes.

HelpDesk permanece importante no README/portfólio e pode continuar pinado se houver uma sexta vaga disponível, mas não precisa competir com os cinco principais na narrativa inicial.

No README do perfil, separar visualmente **núcleo profissional**, **ferramentas complementares/contextuais** e uma lista curta de **credenciais selecionadas**, para que a presença de uma keyword não seja interpretada como profundidade equivalente. Manter uma versão inglesa dedicada facilita avaliação internacional sem duplicar PT/EN no mesmo fluxo de leitura.

**Nome neutro de repositório:** manter `ComprasProducao` como nome público do repositório para não criar associação desnecessária com a empresa no identificador técnico. Não renomear para `ComprasVesper`.

### Cases e READMEs individuais

Não transformar projetos em mural de certificados. Um case deve provar problema, estado real, decisões, arquitetura, resultado, segurança/confiabilidade e como validar. Priorizar:

- resumo de 30 segundos;
- estado real explícito;
- métricas aprovadas;
- diagrama/arquitetura quando agrega;
- screenshots/demo sanitizados;
- setup mínimo quando reproduzível;
- testes/evals/CI quando existem;
- segurança e limites;
- próximos passos somente quando realmente futuros.

Credenciais só entram em case/README individual quando explicarem um contexto específico que o próprio projeto não comunica sozinho.

## Regra de atualização

Uma nova métrica ou mudança de estado deve ser atualizada primeiro na evidência do projeto. Uma nova credencial deve ser classificada primeiro em `CREDENTIALS_EVIDENCE.md`. Depois, este registro e as superfícies públicas podem ser sincronizados. Nunca promover status, métrica, senioridade ou tecnologia apenas para melhorar a apresentação.