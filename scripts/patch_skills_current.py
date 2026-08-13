from pathlib import Path
root=Path(__file__).resolve().parents[1]

def patch(rel,pairs):
    p=root/rel; text=p.read_text(encoding='utf-8')
    for old,new in pairs:
        if old not in text: raise RuntimeError(f'{rel}: missing source phrase')
        text=text.replace(old,new,1)
    p.write_text(text,encoding='utf-8')

patch('competencias/index.html',[
('Mapeio processos AS-IS/TO-BE, requisitos, regras de negócio, exceções e aprovações. No n8n, desenvolvo interfaces, webhooks, filas, agendamentos, persistência, tratamento de falhas e integrações, sem retirar a supervisão humana quando a decisão precisa ser revisada.','Mapeio processos AS-IS/TO-BE, requisitos, regras de negócio, exceções, aprovações e necessidades de rastreabilidade. No n8n e em sistemas internos, desenvolvo interfaces, webhooks, filas, persistência, tratamento de falhas e integrações, preservando revisão humana quando a decisão é sensível.'),
('n8n self-hosted · low-code/no-code · AS-IS/TO-BE · requisitos · regras de negócio · workflows · aprovação humana · documentação','n8n self-hosted · AS-IS/TO-BE · requisitos · regras de negócio · workflows · rastreabilidade · aprovação humana · documentação'),
('Utilizo OpenAI, Gemini, Ollama, OpenRouter e Codex em criação assistida, análise, classificação e recuperação de contexto. Em projetos de mídia, trabalho com texto, imagem e áudio, sempre com revisão humana e fallbacks quando a integração permite.','Utilizo OpenAI, Gemini e Ollama por APIs de LLM, engenharia de prompts, respostas estruturadas e recuperação de contexto. No Postagem Redes, também implementei RAG/grounding com LangChain, Supabase e n8n/Docker para reduzir respostas sem base nas informações da empresa.'),
('OpenAI · Gemini · Ollama · OpenRouter · Codex · APIs de LLM · prompts · grounding · JSON Schema · IA multimodal','OpenAI · Gemini · Ollama · APIs de LLM · prompts · RAG/grounding · LangChain · JSON/JSON Schema · human-in-the-loop'),
('Desenvolvo com Python, JavaScript/TypeScript, Node.js/Express e FastAPI. Utilizo SQL, PostgreSQL, SQLite e FTS5, além de Docker e GitHub Actions. No Programa Compass, trabalhei com S3, Lambda, Glue/PySpark, Parquet, Athena e QuickSight.','Desenvolvo com Python, JavaScript/TypeScript e FastAPI. Utilizo SQL, PostgreSQL, SQLite/FTS5, Docker, Linux e Git/GitHub Actions. No Programa Compass, trabalhei com ETL/Data Lake, S3, Lambda, Glue/PySpark, Parquet, Athena e QuickSight.'),
('Python · JavaScript/TypeScript · Node.js/Express · FastAPI · SQL · PostgreSQL · SQLite FTS5 · Docker · AWS · PySpark · Git/GitHub Actions','Python · JavaScript/TypeScript · FastAPI · SQL · PostgreSQL · SQLite FTS5 · Docker · Linux · AWS/PySpark · Git/GitHub Actions'),
('CONFIABILIDADE E SEGURANÇA','RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA'),
('Utilizo logs, alertas, retries, filas de erro, idempotência, backups, migrações, validações e gestão de segredos. Quando uma integração externa falha, procuro isolar o canal e manter o restante da operação disponível.','Utilizo histórico, trilha de auditoria, controle de mudanças, logs, alertas, retries, idempotência, backups, validações e gestão de segredos. Em processos de Qualidade e manutenção, evidências e responsáveis precisam permanecer consultáveis sem sobrescrever execuções anteriores.'),
('logs · alertas · retries · idempotência · filas · backups · auditoria · DPAPI · cofre n8n · .env · RLS · sanitização','rastreabilidade · auditoria · logs · alertas · retries · idempotência · backups · gestão de segredos · RLS · sanitização'),
])
print('Current PT skills evidence applied.')
