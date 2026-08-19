from pathlib import Path

root = Path(__file__).resolve().parents[1]


def apply_target(text: str, target: str, candidates: tuple[str, ...], rel: str) -> str:
    if target in text:
        return text
    for old in candidates:
        if old in text:
            return text.replace(old, target, 1)
    raise RuntimeError(f'{rel}: no supported source phrase found for target: {target[:100]}')


def patch(rel: str, specs: list[tuple[str, tuple[str, ...]]], normalizations=()):
    p = root / rel
    text = p.read_text(encoding='utf-8')
    for broken, fixed in normalizations:
        text = text.replace(broken, fixed)
    for target, candidates in specs:
        text = apply_target(text, target, candidates, rel)
    p.write_text(text, encoding='utf-8')


patch('competencias/index.html', [
    (
        'Faço mapeamento de processos com BPMN e AS-IS/TO-BE, levanto requisitos com usuários e stakeholders, documento regras de negócio, exceções, aprovações e necessidades de rastreabilidade. Meu núcleo é n8n self-hosted em uma abordagem híbrida low-code/no-code + Python/APIs. Power Platform, Make, Zapier e CRM entram como ferramentas complementares/contextuais quando o ecossistema pede outra abordagem; não as apresento no mesmo nível de profundidade do meu trabalho com n8n, Python e APIs.',
        (
            'Faço mapeamento de processos com BPMN e AS-IS/TO-BE, levanto requisitos, regras de negócio, exceções, aprovações e necessidades de rastreabilidade. Meu núcleo é n8n self-hosted. Power Automate, Make, Zapier e CRM entram como ferramentas complementares/contextuais quando o ecossistema pede outra abordagem; não as apresento no mesmo nível de profundidade do meu trabalho com n8n, Python e APIs.',
            'Faço mapeamento de processos com BPMN e AS-IS/TO-BE, levanto requisitos, regras de negócio, exceções, aprovações e necessidades de rastreabilidade. Meu núcleo é n8n self-hosted, mas também uso Power Automate, Make e Zapier quando o contexto pede outro ecossistema, além de CRM em rotinas de integração e automação. Também explico e oriento outras pessoas sobre essas ferramentas quando necessário.',
            'Mapeio processos AS-IS/TO-BE, requisitos, regras de negócio, exceções e aprovações. No n8n, desenvolvo interfaces, webhooks, filas, agendamentos, persistência, tratamento de falhas e integrações, sem retirar a supervisão humana quando a decisão precisa ser revisada.',
        ),
    ),
    (
        'n8n self-hosted · low-code/no-code · BPMN · AS-IS/TO-BE · requisitos/stakeholders · regras de negócio · rastreabilidade · aprovação humana · documentação · Power Platform/Make/Zapier/CRM (uso contextual)',
        (
            'n8n self-hosted · BPMN · AS-IS/TO-BE · requisitos · regras de negócio · rastreabilidade · aprovação humana · documentação · Power Automate/Make/Zapier/CRM (uso contextual)',
            'n8n self-hosted · Power Automate · Make · Zapier · CRM · BPMN · AS-IS/TO-BE · requisitos · regras de negócio · rastreabilidade · aprovação humana · documentação',
            'n8n self-hosted · low-code/no-code · AS-IS/TO-BE · requisitos · regras de negócio · workflows · aprovação humana · documentação',
        ),
    ),
    (
        'Utilizo APIs de LLM, engenharia de prompts, respostas estruturadas e recuperação de contexto. No Postagem Redes, implementei RAG/grounding com LangChain, Supabase e n8n/Docker, revisão humana e evals offline reproduzíveis para validar grounding, fontes autorizadas e ação segura. MCP e Microsoft Foundry contam também com validação prática por Microsoft Applied Skills em integração de ferramentas MCP com agentes; LangGraph e CrewAI permanecem em estudos e protótipos. Não apresento essas tecnologias no mesmo nível do meu núcleo profissional em n8n, Python e APIs.',
        (
            'Utilizo OpenAI, Gemini e Ollama por APIs de LLM, engenharia de prompts, respostas estruturadas e recuperação de contexto. No Postagem Redes, implementei RAG/grounding com LangChain, Supabase e n8n/Docker para reduzir respostas sem base nas informações da empresa. MCP e Microsoft Foundry contam também com validação prática por Microsoft Applied Skills em integração de ferramentas MCP com agentes; LangGraph e CrewAI permanecem em estudos e protótipos. Não apresento essas tecnologias no mesmo nível do meu núcleo profissional em n8n, Python e APIs.',
            'Utilizo OpenAI, Gemini e Ollama por APIs de LLM, engenharia de prompts, respostas estruturadas e recuperação de contexto. No Postagem Redes, implementei RAG/grounding com LangChain, Supabase e n8n/Docker para reduzir respostas sem base nas informações da empresa. Em estudos e protótipos, também pratiquei MCP, LangGraph e CrewAI para explorar ferramentas de agentes e orquestração; não apresento essas ferramentas no mesmo nível do meu núcleo em n8n, Python e APIs.',
            'Utilizo OpenAI, Gemini, Ollama, OpenRouter e Codex em criação assistida, análise, classificação e recuperação de contexto. Em projetos de mídia, trabalho com texto, imagem e áudio, sempre com revisão humana e fallbacks quando a integração permite.',
        ),
    ),
    (
        'IA generativa/LLMs · APIs de LLM · prompts · respostas estruturadas · RAG/grounding · LangChain · agentes de IA · human-in-the-loop · evals offline · MCP/Microsoft Foundry (Microsoft Applied Skills) · LangGraph/CrewAI (uso contextual)',
        (
            'OpenAI · Gemini · Ollama · APIs de LLM · prompts · RAG/grounding · LangChain · human-in-the-loop · MCP/Microsoft Foundry (Microsoft Applied Skills) · LangGraph/CrewAI (uso contextual)',
            'OpenAI · Gemini · Ollama · APIs de LLM · prompts · RAG/grounding · LangChain · human-in-the-loop · MCP/LangGraph/CrewAI (uso contextual)',
            'OpenAI · Gemini · Ollama · OpenRouter · Codex · APIs de LLM · prompts · grounding · JSON Schema · IA multimodal',
        ),
    ),
    (
        'Desenvolvo com Python, JavaScript/TypeScript e FastAPI. Utilizo SQL, PostgreSQL, SQLite/FTS5, Docker, Linux e Git/GitHub Actions. No Programa Compass, trabalhei com ETL/Data Lake, S3, Lambda, Glue/PySpark, Parquet, Athena e QuickSight.',
        (
            'Desenvolvo com Python, JavaScript/TypeScript, Node.js/Express e FastAPI. Utilizo SQL, PostgreSQL, SQLite e FTS5, além de Docker e GitHub Actions. No Programa Compass, trabalhei com S3, Lambda, Glue/PySpark, Parquet, Athena e QuickSight.',
        ),
    ),
    (
        'Python · JavaScript/TypeScript · FastAPI · SQL · PostgreSQL · SQLite FTS5 · Docker · Linux · AWS/PySpark · Git/GitHub Actions · CI/CD',
        (
            'Python · JavaScript/TypeScript · FastAPI · SQL · PostgreSQL · SQLite FTS5 · Docker · Linux · AWS/PySpark · Git/GitHub Actions',
            'Python · JavaScript/TypeScript · Node.js/Express · FastAPI · SQL · PostgreSQL · SQLite FTS5 · Docker · AWS · PySpark · Git/GitHub Actions',
        ),
    ),
    (
        'RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA',
        ('CONFIABILIDADE E SEGURANÇA',),
    ),
    (
        'Utilizo histórico, trilha de auditoria, controle de mudanças, logs/monitoramento, troubleshooting, tratamento de erros, retries, idempotência, backups, validações, isolamento de falhas e gestão de segredos. Em processos de Qualidade e manutenção, evidências e responsáveis precisam permanecer consultáveis sem sobrescrever execuções anteriores.',
        (
            'Utilizo histórico, trilha de auditoria, controle de mudanças, logs, alertas, retries, idempotência, backups, validações e gestão de segredos. Em processos de Qualidade e manutenção, evidências e responsáveis precisam permanecer consultáveis sem sobrescrever execuções anteriores.',
            'Utilizo logs, alertas, retries, filas de erro, idempotência, backups, migrações, validações e gestão de segredos. Quando uma integração externa falha, procuro isolar o canal e manter o restante da operação disponível.',
        ),
    ),
    (
        'rastreabilidade · auditoria · logs/monitoramento · troubleshooting · tratamento de erros · retries · idempotência · backups · isolamento de falhas · segurança de integrações · gestão de segredos · RLS · sanitização',
        (
            'rastreabilidade · auditoria · logs · alertas · retries · idempotência · backups · gestão de segredos · RLS · sanitização',
            'logs · alertas · retries · idempotência · filas · backups · auditoria · DPAPI · cofre n8n · .env · RLS · sanitização',
        ),
    ),
], normalizations=[
    ('RASTREABILIDADE, RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA', 'RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA'),
])

patch('en/skills/index.html', [
    (
        'I map processes with BPMN and AS-IS/TO-BE, gather requirements with users and stakeholders, document business rules, exceptions, approvals and traceability needs. My core is self-hosted n8n in a hybrid low-code/no-code + Python/API approach. Power Platform, Make, Zapier and CRM are complementary/contextual tools when another ecosystem calls for them; I do not present them at the same depth as my work with n8n, Python and APIs.',
        (
            'I map processes with BPMN and AS-IS/TO-BE, gather requirements, business rules, exceptions, approvals and traceability needs. My core platform is self-hosted n8n. Power Automate, Make, Zapier and CRM are complementary/contextual tools when another ecosystem calls for them; I do not present them at the same depth as my work with n8n, Python and APIs.',
            'I map processes with BPMN and AS-IS/TO-BE, gather requirements, business rules, exceptions, approvals and traceability needs. My core platform is self-hosted n8n, but I also use Power Automate, Make and Zapier when another ecosystem fits the context, plus CRM in integration and automation routines. I also explain and guide others on these tools when needed.',
            'I map AS-IS/TO-BE processes, requirements, business rules, exceptions and approvals. In n8n, I build interfaces, webhooks, queues, schedules, persistence, failure handling and integrations while preserving human supervision when a decision must be reviewed.',
        ),
    ),
    (
        'self-hosted n8n · low-code/no-code · BPMN · AS-IS/TO-BE · requirements/stakeholders · business rules · traceability · human approval · documentation · Power Platform/Make/Zapier/CRM (contextual use)',
        (
            'self-hosted n8n · BPMN · AS-IS/TO-BE · requirements · business rules · traceability · human approval · documentation · Power Automate/Make/Zapier/CRM (contextual use)',
            'self-hosted n8n · Power Automate · Make · Zapier · CRM · BPMN · AS-IS/TO-BE · requirements · business rules · traceability · human approval · documentation',
            'self-hosted n8n · low-code/no-code · AS-IS/TO-BE · requirements · business rules · workflows · human approval · documentation',
        ),
    ),
    (
        'I use LLM APIs, prompt engineering, structured outputs and context retrieval. In Postagem Redes, I implemented RAG/grounding with LangChain, Supabase and n8n/Docker, human review and reproducible offline evals for grounding, authorized sources and safe action. MCP and Microsoft Foundry also have hands-on validation through Microsoft Applied Skills for integrating MCP tools with agents; LangGraph and CrewAI remain study/prototype tools. I do not present these technologies at the same depth as my professional core in n8n, Python and APIs.',
        (
            'I use OpenAI, Gemini and Ollama through LLM APIs, prompt engineering, structured outputs and context retrieval. In Postagem Redes, I implemented RAG/grounding with LangChain, Supabase and n8n/Docker to reduce answers that are not grounded in company information. MCP and Microsoft Foundry also have hands-on validation through Microsoft Applied Skills for integrating MCP tools with agents; LangGraph and CrewAI remain study/prototype tools. I do not present these technologies at the same depth as my professional core in n8n, Python and APIs.',
            'I use OpenAI, Gemini and Ollama through LLM APIs, prompt engineering, structured outputs and context retrieval. In Postagem Redes, I implemented RAG/grounding with LangChain, Supabase and n8n/Docker to reduce answers that are not grounded in company information. In studies and prototypes, I have also practiced MCP, LangGraph and CrewAI to explore agent tooling and orchestration; I do not present them at the same experience level as my core work with n8n, Python and APIs.',
            'I use OpenAI, Gemini, Ollama, OpenRouter and Codex for assisted creation, analysis, classification and context retrieval. In media projects, I work with text, image and audio, with human review and fallbacks when the integration supports them.',
        ),
    ),
    (
        'generative AI/LLMs · LLM APIs · prompts · structured outputs · RAG/grounding · LangChain · AI agents · human-in-the-loop · offline evals · MCP/Microsoft Foundry (Microsoft Applied Skills) · LangGraph/CrewAI (contextual use)',
        (
            'OpenAI · Gemini · Ollama · LLM APIs · prompts · RAG/grounding · LangChain · human-in-the-loop · MCP/Microsoft Foundry (Microsoft Applied Skills) · LangGraph/CrewAI (contextual use)',
            'OpenAI · Gemini · Ollama · LLM APIs · prompts · RAG/grounding · LangChain · human-in-the-loop · MCP/LangGraph/CrewAI (contextual use)',
            'OpenAI · Gemini · Ollama · OpenRouter · Codex · LLM APIs · prompts · grounding · JSON Schema · multimodal AI',
        ),
    ),
    (
        'I build with Python, JavaScript/TypeScript and FastAPI. I use SQL, PostgreSQL, SQLite/FTS5, Docker, Linux and Git/GitHub Actions. During the Compass Program, I worked with ETL/Data Lake, S3, Lambda, Glue/PySpark, Parquet, Athena and QuickSight.',
        (
            'I build with Python, JavaScript/TypeScript, Node.js/Express and FastAPI. I use SQL, PostgreSQL, SQLite and FTS5, along with Docker and GitHub Actions. During the Compass Program, I worked with S3, Lambda, Glue/PySpark, Parquet, Athena and QuickSight.',
        ),
    ),
    (
        'Python · JavaScript/TypeScript · FastAPI · SQL · PostgreSQL · SQLite FTS5 · Docker · Linux · AWS/PySpark · Git/GitHub Actions · CI/CD',
        (
            'Python · JavaScript/TypeScript · FastAPI · SQL · PostgreSQL · SQLite FTS5 · Docker · Linux · AWS/PySpark · Git/GitHub Actions',
            'Python · JavaScript/TypeScript · Node.js/Express · FastAPI · SQL · PostgreSQL · SQLite FTS5 · Docker · AWS · PySpark · Git/GitHub Actions',
        ),
    ),
    (
        'TRACEABILITY, RELIABILITY AND SECURITY',
        ('RELIABILITY AND SECURITY',),
    ),
    (
        'I use history, audit trails, change control, logs/monitoring, troubleshooting, error handling, retries, idempotency, backups, validation, failure isolation and secret management. In Quality and maintenance processes, evidence and responsible users remain traceable without overwriting previous executions.',
        (
            'I use history, audit trails, change control, logs, alerts, retries, idempotency, backups, validation and secrets management. In Quality and maintenance processes, evidence and responsible users remain traceable without overwriting previous executions.',
            'I use logs, alerts, retries, error queues, idempotency, backups, migrations, validation and secrets management. When an external integration fails, I isolate the channel and keep the rest of the operation available whenever possible.',
        ),
    ),
    (
        'traceability · auditing · logs/monitoring · troubleshooting · error handling · retries · idempotency · backups · failure isolation · integration security · secrets management · RLS · sanitization',
        (
            'traceability · auditing · logs · alerts · retries · idempotency · backups · secrets management · RLS · sanitization',
            'logs · alerts · retries · idempotency · queues · backups · auditing · DPAPI · n8n vault · .env · RLS · sanitization',
        ),
    ),
], normalizations=[
    ('TRACEABILITY, TRACEABILITY, RELIABILITY AND SECURITY', 'TRACEABILITY, RELIABILITY AND SECURITY'),
])

print('Current PT/EN skills evidence applied idempotently with core/context depth separated.')