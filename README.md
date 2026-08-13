# Portfólio profissional — Maycon Ferreira

Este repositório é a versão pública do meu portfólio profissional em português e inglês. Ele organiza evidências de **automação de processos, IA aplicada, integrações, sistemas internos, transformação digital e produtos operacionais** sem misturar projeto em produção, piloto, teste, laboratório ou desenvolvimento.

Acesse: [mayconxzdev.github.io](https://mayconxzdev.github.io/)

## Posicionamento atual

Atuo como **Analista de Automação, IA e Integrações**, transformando necessidades operacionais em soluções rastreáveis do levantamento à sustentação. Minha base principal inclui **n8n self-hosted, Python, FastAPI, APIs REST/webhooks, SQL/PostgreSQL, Docker, Linux e IA aplicada**. Também uso, conforme o contexto, **BPMN, Power Automate, Make, Zapier, CRM, RAG/LangChain, MCP, LangGraph e CrewAI**.

A apresentação pública separa tecnologia de evidência: uma ferramenta pode fazer parte da minha prática sem ser artificialmente atribuída a um case que não a utiliza.

## Projetos principais

| Projeto | O que demonstra | Estado público |
|---|---|---|
| **Mala Direta** | n8n, filas, deduplicação, cancelamento revalidado, auditoria e operação em volume | Em produção |
| **Produção Operacional** | aplicação Windows, implantação multi-PC, visão coletiva em TV e operação industrial | Em produção |
| **Proposta Comercial** | ODT/PDF, IMAP/SMTP, revisão/aprovação humana, rastreabilidade e ganho de tempo | Uso interno diário |
| **Catálogo Operacional de Compras** | FastAPI, SQLite FTS5, busca, histórico, concorrência e revisão | Uso interno diário |
| **Postagem Redes** | RAG/grounding, LangChain, n8n, Meta Graph API, LLMs e aprovação humana | Validado em teste |
| **CarreiraPessoal** | produto local-first, FastAPI, React/TypeScript, Tauri/Rust, evidências e regras de decisão | Produto pessoal em uso |
| **Central ISO** | requisitos da Qualidade, automação documental, regras determinísticas, n8n, Docker e rastreabilidade | Piloto técnico |
| **Portal** | tenancy/RLS, Action Envelope, aprovações, outbox e arquitetura de sistemas | Em desenvolvimento/revalidação |

O arquivo do portfólio também inclui cases de HelpDesk, ComprasVesper, manutenção, sites industriais, integrações via WhatsApp, StudioCad, Hubora, Compass UOL e outras referências públicas sanitizadas.

## Resultados apresentados

- **10 mil+** execuções de workflows na instância n8n de produção que administro;
- propostas simples de **2–4 minutos para menos de 30 segundos**, com uso diário por 4 profissionais;
- Produção Operacional em **10+ computadores e 1 TV**, apoiando **20+ profissionais em 9 setores**;
- solução de manutenção acompanhando **40+ ativos**, com checklists, evidências, histórico e consulta pela Qualidade;
- **6 campanhas** na Mala Direta sobre base de **1.020 contatos**, incluindo uma para **900+ destinatários**;
- Catálogo Operacional com **24 categorias e 480+ códigos**, usado diariamente por 3 pessoas;
- **30+ pessoas** treinadas/orientadas em escritório, fábrica e acesso remoto;
- CarreiraPessoal v12.5.2 com **283 testes Python** registrados na versão-fonte auditada.

## Processos, automação e IA

Minha prática combina **BPMN e AS-IS/TO-BE, levantamento de requisitos, regras de negócio, documentação e rastreabilidade** com plataformas e código. O n8n é meu núcleo de orquestração, e Power Automate, Make, Zapier e CRM entram quando o ecossistema ou a necessidade faz mais sentido. Para IA, utilizo APIs de LLM, RAG/grounding, LangChain e, conforme a necessidade, MCP, LangGraph e CrewAI, preservando revisão humana em decisões sensíveis.

## Currículos

Os currículos gerais ficam em `assets/cv/`:

- `Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf`
- `Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf`

O pipeline de publicação gera os dois PDFs a partir de `scripts/generate_resumes_general.py`, aplica a evidência profissional atual, valida conteúdo e parsing ATS e mantém cada versão em **uma página A4**, com texto selecionável, uma coluna, headings convencionais e links funcionais.

## Estrutura

- `/` e `/en/` — páginas iniciais em português e inglês;
- `/competencias/` e `/en/skills/` — competências e práticas atuais;
- `/cases/` e `/en/cases/` — estudos de caso e estados reais de cada projeto;
- `/assets/cv/` — currículos PT-BR e EN;
- `/scripts/` — geração, atualização de evidências, QA e validação;
- `/docs/` — documentação complementar e relatórios de qualidade;
- `/.github/workflows/pages.yml` — pipeline de validação, QA visual e deploy.

## Executar localmente

Para visualizar o site:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Abra `http://127.0.0.1:8000`.

A CI instala as dependências de currículo, aplica a evidência atual, gera os PDFs, valida texto/layout, verifica rotas e JavaScript, executa Playwright em desktop/mobile e light/dark, publica no GitHub Pages e confirma que a versão atual chegou ao endereço público.

## Critério de apresentação

Cada case tenta responder rapidamente a cinco perguntas: **qual problema existia, o que eu fiz, quais decisões técnicas importam, qual evidência existe e qual é o estado real hoje**. O objetivo não é exibir a maior quantidade possível de tecnologia, e sim permitir que recrutadores e profissionais técnicos diferenciem experiência em produção, uso interno, teste, piloto, laboratório e desenvolvimento.

## Privacidade e precisão

Nos cases públicos removo credenciais, dados pessoais, preços, documentos, caminhos de rede, fornecedores e informações internas que não deveriam sair do ambiente original. Não apresento como produção aquilo que é teste, laboratório, piloto ou desenvolvimento, e não atribuo uma tecnologia a um projeto apenas para aumentar cobertura de palavras-chave.
