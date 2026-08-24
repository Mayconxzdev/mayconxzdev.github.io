# Portfólio — Maycon Ferreira

Código-fonte do meu portfólio profissional como **Analista de Automação, IA e Integrações**.

O site é organizado para responder rapidamente a três perguntas: **qual problema eu resolvi, qual foi o resultado e qual evidência existe**. Em vez de exibir o maior número possível de tecnologias, cada case prova uma parte diferente da minha atuação: processo, automação, integrações, implantação, dados, IA aplicada, confiabilidade e produto.

**Site:** https://mayconxzdev.github.io/

## Projetos principais

A vitrine segue uma ordem deliberada, sem repetir a mesma competência em todos os cases:

| Projeto | Principal evidência |
| --- | --- |
| [Mala Direta](cases/mala-direta/) | n8n em produção, filas, deduplicação, retry, cancelamento e auditoria |
| [Produção Operacional](cases/producao-operacional/) | implantação em 10+ PCs + 1 TV, apoiando 20+ profissionais em 9 setores |
| [Proposta Comercial](cases/vesper-propostas/) | documentos/e-mail e redução de 2–4 min para menos de 30 s em propostas simples |
| [CarreiraPessoal](cases/carreira-pessoal/) | produto Windows em uso, arquitetura full-stack, evidências, QA e IA opcional |
| [Catálogo Operacional](cases/catalogo-operacional-compras/) | FastAPI, FTS5, integridade de dados, revisão/histórico e uso diário |
| [Postagem Redes](cases/postagem-redes/) | IA aplicada, RAG/LangChain, APIs externas, human-in-the-loop, evals e idempotência |

## Outros recortes importantes

- [HelpDesk](cases/helpdesk/) — sistema interno em uso por 11 pessoas, tempo real, ativos, acessos e segurança;
- [ComprasVesper](cases/compras-vesper/) — desktop, SMTP/IMAP, fila durável, backoff e idempotência;
- [Central ISO](cases/central-iso/) — Qualidade, regras determinísticas, read-only, rastreabilidade e piloto técnico;
- [StudioCad](cases/studiocad/) — IA aplicada, conversão/visualização técnica, hashes e segurança de arquivos;
- [Manutenção em Campo](cases/manutencao-campo/) — ativos, checklists, evidências, histórico e PWA;
- [Compass UOL](cases/compass/) — Linux, Python, SQL, Docker, ETL/Data Lake, AWS e PySpark;
- [Sites industriais](cases/sites-industriais/) — aplicações web públicas em produção;
- [Hubora](cases/hubora/) — produto pessoal/PWA/local-first;
- [Portal](cases/portal/) — arquitetura empresarial em **desenvolvimento/revalidação**; não é apresentado como produção.

## Fonte de verdade profissional

O portfólio segue regras explícitas para impedir que uma apresentação bonita vire exagero:

- métricas só entram quando existe base real;
- projeto em teste não é chamado de produção;
- piloto não é tratado como sistema certificado;
- tecnologia contextual não é apresentada com a mesma profundidade do núcleo profissional;
- uma tecnologia não é atribuída artificialmente a um case que não a utiliza;
- dados e código corporativos sensíveis são substituídos por material sanitizado, dados sintéticos ou explicação técnica;
- IA aplicada continua sujeita a revisão humana nos fluxos sensíveis;
- currículo, portfólio e GitHub devem usar os mesmos números e estados.

O registro editorial usado para essa sincronização está em [`docs/CAREER_EVIDENCE.md`](docs/CAREER_EVIDENCE.md).

## Currículo geral

O portfólio publica **um currículo geral de uma página em PT-BR e seu espelho semântico em inglês**. Não existem versões artificiais por vaga: o documento concentra o núcleo transferível que mais se repete em automação, integrações, processos e IA aplicada.

- [Currículo PT-BR](assets/cv/Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf)
- [Resume EN](assets/cv/Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf)

Os PDFs são gerados por `scripts/generate_resumes_general.py` e priorizam:

- **automação, integrações e backend:** n8n, Python, FastAPI, REST/JSON, webhooks, OAuth 2.0, SQL/PostgreSQL, Docker e exposição contextual a Power Apps/Power Automate/Make/Zapier;
- **processos e entrega:** BPMN, AS-IS/TO-BE, requisitos, UAT, documentação, métricas de impacto, implantação, treinamento e sustentação;
- **IA aplicada e engenharia:** LLM APIs, agentes, RAG/grounding, LangChain, human-in-the-loop, evals, CI/CD, logs, monitoramento/observabilidade, retries e idempotência;
- **evidência:** resultados, adoção e estados verificáveis em vez de listas extensas de cursos ou buzzwords.

Projetos já demonstrados na experiência profissional não são repetidos desnecessariamente na seção de projetos; essa seção complementa a narrativa com automação robusta, produto/QA, backend/dados e IA aplicada.

## Validação

O pipeline do GitHub Pages executa geração e validação dos currículos, checagem de links e rotas, sintaxe JavaScript, smoke de navegador, acessibilidade e verificação visual. Os PDFs precisam permanecer em uma página, textuais/selecionáveis, com contatos ATS-visíveis e clicáveis, e sem fonte abaixo do limite de legibilidade definido pelo projeto.

O deploy também verifica a versão publicada após o GitHub Pages concluir a publicação, reduzindo o risco de o portfólio e os PDFs servirem builds diferentes.

## Privacidade

Quando um case nasceu de um problema corporativo, publico somente o que pode ser mostrado com segurança: tela sanitizada, arquitetura, dados fictícios, código público preparado para avaliação ou descrição do fluxo. O objetivo é provar capacidade sem expor cliente, credencial, caminho de rede, documento ou dado pessoal.

## Contato

**Maycon Ferreira**  
Analista de Automação, IA e Integrações  
[LinkedIn](https://www.linkedin.com/in/maycon-ferreira-7bb870231/) · [GitHub](https://github.com/Mayconxzdev) · [Portfólio](https://mayconxzdev.github.io/)
