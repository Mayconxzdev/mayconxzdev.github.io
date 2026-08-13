from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def renumber_between(text: str, start_marker: str, end_marker: str, pattern: re.Pattern[str], first: int) -> tuple[str, int]:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    block = text[start:end]
    current = first

    def repl(match: re.Match[str]) -> str:
        nonlocal current
        value = f"{current:02d}"
        current += 1
        return f"{match.group(1)}{value}{match.group(3)}"

    block = pattern.sub(repl, block)
    return text[:start] + block + text[end:], current


for rel, lang in (("index.html", "pt"), ("en/index.html", "en")):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")

    if lang == "pt":
        text = text.replace(
            "Automação, sistemas internos, backend, IA, APIs externas e arquitetura full-stack, sem repetir a mesma competência em todos os cases.",
            "Automação, sistemas internos, backend, IA, APIs externas e arquitetura de sistemas, sem repetir a mesma competência em todos os cases.",
        )
        text = text.replace(
            "<div><dt>Python e desktop</dt><dd>Vesper Propostas · Produção Operacional · ComprasVesper</dd></div>",
            "<div><dt>Python e desktop</dt><dd>Proposta Comercial · Produção Operacional · ComprasVesper</dd></div>",
        )
        text = text.replace(
            "<h3>Vesper Manutenção</h3><p>Documentos, áudios, histórico e busca de conhecimento técnico.</p>",
            "<h3>Vesper Manutenção</h3><p>Ativos, checklists, evidências e histórico rastreável para a manutenção de 40+ equipamentos.</p>",
        )
        old_ld = '"knowsAbout":["n8n","Automação de processos","Low-code","Mapeamento AS-IS/TO-BE","IA generativa","Agentes de IA","Engenharia de prompts","Grounding","JSON Schema","IA multimodal","Geração de mídia","APIs REST","Webhooks","Python","JavaScript","TypeScript","FastAPI","PostgreSQL","SQLite FTS5","Docker","AWS","PySpark","CI/CD","Idempotência","RLS","Transactional outbox"]'
        new_ld = '"knowsAbout":["n8n","Power Automate","Make","Zapier","CRM","BPMN","Automação de processos","Mapeamento de processos AS-IS/TO-BE","Levantamento de requisitos","Regras de negócio","APIs REST","Webhooks","JSON","OAuth 2.0","Python","FastAPI","PostgreSQL","SQLite FTS5","Docker","Linux","IA generativa","RAG","LangChain","MCP","LangGraph","CrewAI","Human-in-the-loop","Rastreabilidade","Auditoria","GitHub Actions","AWS","PySpark"]'
    else:
        text = text.replace(
            "Automation, internal systems, backend, AI, external APIs and full-stack architecture, without repeating the same skill set in every case.",
            "Automation, internal systems, backend, AI, external APIs and systems architecture, without repeating the same skill set in every case.",
        )
        text = text.replace(
            "<div><dt>Python and desktop</dt><dd>Vesper Propostas · Produção Operacional · ComprasVesper</dd></div>",
            "<div><dt>Python and desktop</dt><dd>Proposta Comercial · Produção Operacional · ComprasVesper</dd></div>",
        )
        text = text.replace(
            "<h3>Vesper Maintenance</h3><p>Documents, audio, history and technical-knowledge search.</p>",
            "<h3>Vesper Maintenance</h3><p>Assets, checklists, evidence and traceable history for maintenance across 40+ pieces of equipment.</p>",
        )
        old_ld = '"knowsAbout":["n8n","Process automation","Low-code","AS-IS/TO-BE mapping","Generative AI","AI agents","Prompt engineering","Grounding","JSON Schema","Multimodal AI","Media generation","REST APIs","Webhooks","Python","JavaScript","TypeScript","FastAPI","PostgreSQL","SQLite FTS5","Docker","AWS","PySpark","CI/CD","Idempotency","RLS","Transactional outbox"]'
        new_ld = '"knowsAbout":["n8n","Power Automate","Make","Zapier","CRM","BPMN","Process automation","Process mapping AS-IS/TO-BE","Requirements discovery","Business rules","REST APIs","Webhooks","JSON","OAuth 2.0","Python","FastAPI","PostgreSQL","SQLite FTS5","Docker","Linux","Generative AI","RAG","LangChain","MCP","LangGraph","CrewAI","Human-in-the-loop","Traceability","Auditing","GitHub Actions","AWS","PySpark"]'

    if old_ld in text:
        text = text.replace(old_ld, new_ld, 1)

    feature_pattern = re.compile(r'(<div class="case-index"><span>)([^<]+)(</span>)')
    archive_pattern = re.compile(r'(<span class="archive-number">)([^<]+)(</span>)')
    text, next_number = renumber_between(
        text,
        '<section class="featured" id="systems">',
        '<section class="experience" id="experience">',
        feature_pattern,
        1,
    )
    text, _ = renumber_between(
        text,
        '<section class="archive" id="archive">',
        '<section class="journey">',
        archive_pattern,
        next_number,
    )

    path.write_text(text, encoding="utf-8")

for rel in ("competencias/index.html", "en/skills/index.html"):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    text = text.replace("Vesper Propostas", "Proposta Comercial")
    path.write_text(text, encoding="utf-8")

print("Portfolio numbering, naming, structured data and archive evidence are consistent.")
