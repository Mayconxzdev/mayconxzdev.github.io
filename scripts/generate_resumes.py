from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "cv"
PAGE_W, PAGE_H = A4
LEFT = 42
RIGHT = 42
CONTENT_W = PAGE_W - LEFT - RIGHT

FONT = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
INK = HexColor("#101828")
MUTED = HexColor("#475467")
LINE = HexColor("#C7D3E0")
ACCENT = HexColor("#0F4C81")

PT = {
    "filename": "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    "title": "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
    "location": "Rio de Janeiro - RJ | remoto, híbrido ou presencial | disponibilidade para viagens",
    "portfolio_label": "Portfólio",
    "phone_label": "Telefone/WhatsApp: +55 (21) 96481-0480",
    "summary_heading": "RESUMO PROFISSIONAL",
    "summary": (
        "Analista de Automação, IA e Integrações com atuação ponta a ponta em processos e sistemas internos. "
        "Administro n8n self-hosted com 10 mil+ execuções em produção e desenvolvo soluções com Python, FastAPI, APIs REST, "
        "bancos de dados e IA generativa, do levantamento à implantação, treinamento e sustentação."
    ),
    "skills_heading": "HABILIDADES TÉCNICAS",
    "skills": [
        "<b>Automação e processos:</b> n8n self-hosted, automação low-code/no-code, workflows, AS-IS/TO-BE, levantamento de requisitos, regras de negócio, aprovação humana, documentação e melhoria contínua.",
        "<b>IA e integrações:</b> OpenAI, Gemini, Ollama/OpenRouter, APIs de LLM, engenharia de prompts, recuperação de contexto/grounding, JSON Schema, pipelines multiestágio, IA multimodal e geração de mídia; APIs REST, webhooks, OAuth 2.0, SMTP/IMAP e Meta Graph API.",
        "<b>Engenharia, dados e confiabilidade:</b> Python, JavaScript/TypeScript, Node.js/Express, FastAPI, SQL, PostgreSQL, SQLite FTS5, Docker, Git/GitHub Actions, AWS S3/EC2/Lambda/Glue/Athena/QuickSight, testes, logs, retries, idempotência, backups e gestão de segredos.",
    ],
    "experience_heading": "EXPERIÊNCIA PROFISSIONAL",
    "vesper_org": "GRUPO VESPER",
    "vesper_company": "Vesper Equipamentos EX e Vent Rio Equipamentos",
    "vesper_date": "12/2025 - presente",
    "vesper_role": "Técnico Júnior em Automação de Processos (cargo formal) | automação, IA aplicada e integrações",
    "vesper_points": [
        "Administro instância n8n self-hosted em Windows/Docker com 10 mil+ execuções em produção, integrando APIs, webhooks, PostgreSQL e SMTP com logs, retries, alertas, backups e auditoria.",
        "Desenvolvi o Vesper Propostas com ODT/PDF, IMAP/SMTP e revisão humana, reduzindo propostas simples de 2-4 minutos para menos de 30 segundos; uso diário por 4 profissionais.",
        "Implantei o Produção Operacional em 10+ computadores e 1 TV, apoiando 20+ profissionais em 9 setores, e um HelpDesk utilizado por 11 usuários; treinei e orientei 30+ pessoas em escritório, fábrica e acesso remoto.",
    ],
    "compasso_org": "COMPASS UOL",
    "compasso_date": "10/2024 - 03/2025",
    "compasso_role": "Programa de Bolsas em Engenharia de Dados",
    "compasso_point": (
        "Concluí 10 sprints práticas e construí pipeline com Python, SQL, Docker e AWS: ingestão CSV/API TMDB, S3, Lambda/boto3, "
        "Glue/PySpark, Parquet, camadas Raw/Trusted/Refined, Athena e QuickSight."
    ),
    "projects_heading": "PROJETOS SELECIONADOS",
    "projects": [
        "<b>Mala Direta:</b> 6 campanhas sobre base de 1.020 contatos, incluindo uma para 900+ destinatários; 2 workflows n8n, com 158 nós no principal e 9 Data Tables, filas, deduplicação, cancelamento revalidado e auditoria.",
        "<b>Catálogo Operacional de Compras:</b> base histórica com 24 categorias e 480+ códigos, usada diariamente por 3 usuários e consultada pela gestão; FastAPI, SQLite FTS5, controle de revisão, backups e OCR.",
        "<b>Postagem Redes:</b> 3 workflows n8n e 58 nós no fluxo de ações; Meta Graph API, OpenAI/Gemini/Ollama, aprovação humana e idempotência, com Facebook e Instagram validados em teste.",
        "<b>Portal - em desenvolvimento:</b> produto multiempresa em React/TypeScript, FastAPI e PostgreSQL, com tenant/RLS, Action Envelope, aprovações e outbox; Procurement implementado em sandbox e revalidação técnica em andamento antes do piloto interno.",
    ],
    "education_heading": "FORMAÇÃO",
    "education": [
        "<b>Tecnólogo em Análise e Desenvolvimento de Sistemas - UNISUAM</b> | conclusão prevista: dez. 2026",
        "Piscine 42 Rio | programa intensivo concluído em jul. 2025",
    ],
    "certs_heading": "CERTIFICAÇÕES",
    "certs": (
        "Ferramentas de IA: Agentes e Automações - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; "
        "Automação de Processos através da RPA - ENAP (25h); Mapeamento e Automação de Processos - ENAP (20h)."
    ),
    "language_heading": "IDIOMAS",
    "language": "Português nativo | Inglês básico; leitura independente de documentação técnica, escrita e conversação básicas.",
}

EN = {
    "filename": "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
    "title": "AI AUTOMATION & INTEGRATIONS ANALYST",
    "location": "Rio de Janeiro - Brazil | remote, hybrid or on-site | available to travel",
    "portfolio_label": "Portfolio",
    "phone_label": "Phone/WhatsApp: +55 (21) 96481-0480",
    "summary_heading": "PROFESSIONAL SUMMARY",
    "summary": (
        "AI Automation and Integrations Analyst with end-to-end experience in internal processes and systems. Administers a self-hosted "
        "n8n environment with 10,000+ production executions and builds solutions with Python, FastAPI, REST APIs, databases and generative AI, "
        "from discovery through deployment, training and support."
    ),
    "skills_heading": "TECHNICAL SKILLS",
    "skills": [
        "<b>Automation and processes:</b> self-hosted n8n, low-code/no-code automation, workflows, AS-IS/TO-BE, requirements discovery, business rules, human approval, documentation and continuous improvement.",
        "<b>AI and integrations:</b> OpenAI, Gemini, Ollama/OpenRouter, LLM APIs, prompt engineering, context retrieval/grounding, JSON Schema, multi-stage pipelines, multimodal AI and media generation; REST APIs, webhooks, OAuth 2.0, SMTP/IMAP and Meta Graph API.",
        "<b>Engineering, data and reliability:</b> Python, JavaScript/TypeScript, Node.js/Express, FastAPI, SQL, PostgreSQL, SQLite FTS5, Docker, Git/GitHub Actions, AWS S3/EC2/Lambda/Glue/Athena/QuickSight, tests, logs, retries, idempotency, backups and secrets management.",
    ],
    "experience_heading": "PROFESSIONAL EXPERIENCE",
    "vesper_org": "GRUPO VESPER",
    "vesper_company": "Vesper Equipamentos EX e Vent Rio Equipamentos",
    "vesper_date": "12/2025 - Present",
    "vesper_role": "Junior Process Automation Technician (formal title) | automation, applied AI and integrations",
    "vesper_points": [
        "Administer a self-hosted n8n environment on Windows/Docker with 10,000+ production executions, integrating APIs, webhooks, PostgreSQL and SMTP with logs, retries, alerts, backups and auditing.",
        "Developed Vesper Propostas with ODT/PDF, IMAP/SMTP and human review, reducing simple proposals from 2-4 minutes to under 30 seconds; used daily by 4 professionals.",
        "Deployed Produção Operacional to 10+ workstations and 1 factory TV, supporting 20+ professionals across 9 production areas, plus a HelpDesk used by 11 users; trained and guided 30+ people in office, factory and remote settings.",
    ],
    "compasso_org": "COMPASS UOL",
    "compasso_date": "10/2024 - 03/2025",
    "compasso_role": "Data Engineering Scholarship Program",
    "compasso_point": (
        "Completed 10 practical sprints and built a pipeline with Python, SQL, Docker and AWS: CSV/TMDB API ingestion, S3, Lambda/boto3, "
        "Glue/PySpark, Parquet, Raw/Trusted/Refined layers, Athena and QuickSight."
    ),
    "projects_heading": "SELECTED PROJECTS",
    "projects": [
        "<b>Mala Direta:</b> 6 campaigns over a 1,020-contact base, including one for 900+ recipients; 2 n8n workflows, with 158 nodes in the main flow and 9 Data Tables, queues, deduplication, revalidated cancellation and auditing.",
        "<b>Operational Procurement Catalog:</b> historical base with 24 categories and 480+ material codes, used daily by 3 users and consulted by management; FastAPI, SQLite FTS5, revision control, backups and OCR.",
        "<b>Postagem Redes:</b> 3 n8n workflows and 58 nodes in the actions flow; Meta Graph API, OpenAI/Gemini/Ollama, human approval and idempotency, with Facebook and Instagram validated in testing.",
        "<b>Portal - in development:</b> multi-tenant product using React/TypeScript, FastAPI and PostgreSQL, with tenant/RLS, Action Envelopes, approvals and outbox; Procurement implemented in sandbox and technical revalidation underway before an internal pilot.",
    ],
    "education_heading": "EDUCATION",
    "education": [
        "<b>Technology Degree in Systems Analysis and Development - UNISUAM</b> | expected completion: Dec. 2026",
        "42 Rio Piscine | intensive program completed in Jul. 2025",
    ],
    "certs_heading": "CERTIFICATIONS",
    "certs": (
        "AI Tools: Agents and Automations - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; "
        "Process Automation through RPA - ENAP (25h); Process Mapping and Automation - ENAP (20h)."
    ),
    "language_heading": "LANGUAGES",
    "language": "Portuguese: native | English: basic; independently reads technical documentation; basic writing and conversation.",
}


@dataclass
class Block:
    name: str
    top: float
    bottom: float


class LayoutAudit:
    def __init__(self) -> None:
        self.blocks: list[Block] = []

    def add(self, name: str, top: float, bottom: float) -> None:
        if top < bottom:
            raise RuntimeError(f"invalid block geometry: {name} top={top:.1f}, bottom={bottom:.1f}")
        if self.blocks:
            previous = self.blocks[-1]
            gap = previous.bottom - top
            if gap < -0.25:
                raise RuntimeError(
                    f"layout overlap: {previous.name} ({previous.bottom:.1f}) and {name} ({top:.1f}), overlap={-gap:.1f}pt"
                )
        self.blocks.append(Block(name, top, bottom))

    def validate(self, filename: str, final_y: float) -> None:
        if final_y < 30:
            raise RuntimeError(f"content overflow: {filename} ends at y={final_y:.1f}")


def paragraph(text: str, style: ParagraphStyle, canvas: Canvas, y: float, audit: LayoutAudit, name: str) -> float:
    item = Paragraph(text, style)
    _, height = item.wrap(CONTENT_W, 999)
    bottom = y - height
    item.drawOn(canvas, LEFT, bottom)
    audit.add(name, y, bottom)
    return bottom


def section(canvas: Canvas, title: str, y: float, audit: LayoutAudit) -> float:
    top = y - 7
    heading_baseline = top - 10.0
    bar_bottom = heading_baseline - 1
    line_y = heading_baseline - 5.2
    bottom = line_y - 7
    canvas.setFillColor(ACCENT)
    canvas.rect(LEFT, bar_bottom, 4, 12, fill=1, stroke=0)
    canvas.setFillColor(INK)
    canvas.setFont(FONT_BOLD, 9.8)
    canvas.drawString(LEFT + 10, heading_baseline, title)
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(LEFT, line_y, LEFT + CONTENT_W, line_y)
    audit.add(f"section:{title}", top, bottom)
    return bottom


def text_width(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def link_line(canvas: Canvas, y: float, items: list[tuple[str, str]], audit: LayoutAudit, name: str) -> float:
    x = LEFT
    size = 8.2
    leading = 11.3
    line_top = y + 2
    line_bottom = y - size - 1
    canvas.setFont(FONT, size)
    for label, url in items:
        rendered = label + "  "
        width = text_width(rendered, FONT, size)
        if x != LEFT and x + width > LEFT + CONTENT_W:
            audit.add(name, line_top, line_bottom)
            x = LEFT
            y -= leading
            line_top = y + 2
            line_bottom = y - size - 1
        canvas.setFillColor(MUTED)
        canvas.drawString(x, y, rendered)
        canvas.linkURL(url, (x, y - 2, x + width, y + size + 2), relative=0, thickness=0)
        x += width + 10
    audit.add(name, line_top, line_bottom)
    return y - leading


def draw_role_header(canvas: Canvas, y: float, organization: str, date: str, audit: LayoutAudit, name: str) -> float:
    top = y
    org_size = 9.0
    date_size = 8.0
    date_width = text_width(date, FONT, date_size)
    org_width = text_width(organization, FONT_BOLD, org_size)
    if org_width > CONTENT_W - date_width - 14:
        raise RuntimeError(f"organization/date collision risk: {organization}")
    baseline = y - 8.8
    canvas.setFillColor(INK)
    canvas.setFont(FONT_BOLD, org_size)
    canvas.drawString(LEFT, baseline, organization)
    canvas.setFillColor(MUTED)
    canvas.setFont(FONT, date_size)
    canvas.drawRightString(LEFT + CONTENT_W, baseline, date)
    bottom = baseline - 3
    audit.add(name, top, bottom)
    return bottom - 3


def generate(data: dict[str, object]) -> Path:
    path = OUT / str(data["filename"])
    canvas = Canvas(str(path), pagesize=A4, pageCompression=1, invariant=1)
    canvas.setTitle(f"Maycon Ferreira - {data['title']}")
    canvas.setAuthor("Maycon Ferreira")
    canvas.setSubject("One-page resume for process automation, AI, integrations and internal systems roles")
    canvas.setKeywords(
        "automation, process automation, n8n, low-code, process mapping, AS-IS, TO-BE, generative AI, AI agents, "
        "multimodal AI, media generation, systems integration, REST APIs, webhooks, Python, JavaScript, TypeScript, "
        "FastAPI, PostgreSQL, SQLite FTS5, Docker, AWS, data engineering, PySpark, RLS, outbox, Action Envelope"
    )
    canvas.setCreator("Maycon Ferreira")

    base = ParagraphStyle("base", fontName=FONT, fontSize=9.35, leading=11.55, textColor=INK)
    skill = ParagraphStyle("skill", parent=base, fontSize=8.9, leading=10.9)
    role = ParagraphStyle("role", parent=base, fontSize=8.7, leading=10.7, textColor=MUTED)
    bullet = ParagraphStyle("bullet", parent=base, fontSize=8.7, leading=10.85, leftIndent=13, firstLineIndent=-9)
    project = ParagraphStyle("project", parent=base, fontSize=8.25, leading=10.0, leftIndent=13, firstLineIndent=-9)
    compact = ParagraphStyle("compact", parent=base, fontSize=8.65, leading=10.65)

    audit = LayoutAudit()
    y = PAGE_H - 35
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H - 6, PAGE_W, 6, fill=1, stroke=0)

    canvas.setFillColor(INK)
    canvas.setFont(FONT_BOLD, 18.5)
    canvas.drawString(LEFT, y, "MAYCON FERREIRA")
    audit.add("header:name", y + 4, y - 4)
    y -= 17
    canvas.setFillColor(ACCENT)
    canvas.setFont(FONT_BOLD, 10.2)
    canvas.drawString(LEFT, y, str(data["title"]))
    audit.add("header:title", y + 2, y - 3)
    y -= 14
    canvas.setFillColor(MUTED)
    canvas.setFont(FONT, 8.5)
    canvas.drawString(LEFT, y, str(data["location"]))
    audit.add("header:location", y + 2, y - 3)
    y -= 12

    y = link_line(
        canvas,
        y,
        [
            (str(data["phone_label"]), "https://wa.me/5521964810480"),
            ("E-mail: mayconxz00dev@gmail.com", "mailto:mayconxz00dev@gmail.com"),
        ],
        audit,
        "header:contact",
    )
    y = link_line(
        canvas,
        y,
        [
            ("LinkedIn: linkedin.com/in/maycon-ferreira-7bb870231/", "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"),
            ("GitHub: github.com/Mayconxzdev", "https://github.com/Mayconxzdev"),
            (f"{data['portfolio_label']}: mayconxzdev.github.io", "https://mayconxzdev.github.io/"),
        ],
        audit,
        "header:profiles",
    )
    canvas.setStrokeColor(LINE)
    canvas.line(LEFT, y - 1, LEFT + CONTENT_W, y - 1)
    y -= 3

    y = section(canvas, str(data["summary_heading"]), y, audit)
    y = paragraph(escape(str(data["summary"])), base, canvas, y, audit, "summary")

    y = section(canvas, str(data["skills_heading"]), y, audit)
    for index, item in enumerate(data["skills"]):
        y = paragraph(str(item), skill, canvas, y, audit, f"skill:{index + 1}") - 1.8

    y = section(canvas, str(data["experience_heading"]), y, audit)
    y = draw_role_header(canvas, y, str(data["vesper_org"]), str(data["vesper_date"]), audit, "role:vesper-header")
    y = paragraph(escape(str(data["vesper_company"])), role, canvas, y, audit, "role:vesper-company") - 0.3
    y = paragraph(escape(str(data["vesper_role"])), role, canvas, y, audit, "role:vesper-title") - 1.3
    for index, item in enumerate(data["vesper_points"]):
        y = paragraph("- " + escape(str(item)), bullet, canvas, y, audit, f"vesper-bullet:{index + 1}") - 1.8

    y -= 2.5
    y = draw_role_header(canvas, y, str(data["compasso_org"]), str(data["compasso_date"]), audit, "role:compasso-header")
    y = paragraph(escape(str(data["compasso_role"])), role, canvas, y, audit, "role:compasso-title") - 0.8
    y = paragraph("- " + escape(str(data["compasso_point"])), bullet, canvas, y, audit, "compasso-bullet")

    y = section(canvas, str(data["projects_heading"]), y, audit)
    for index, item in enumerate(data["projects"]):
        y = paragraph("- " + str(item), project, canvas, y, audit, f"project:{index + 1}") - 1.5

    y = section(canvas, str(data["education_heading"]), y, audit)
    for index, item in enumerate(data["education"]):
        y = paragraph(str(item), compact, canvas, y, audit, f"education:{index + 1}") - 0.8

    y = section(canvas, str(data["certs_heading"]), y, audit)
    y = paragraph(escape(str(data["certs"])), compact, canvas, y, audit, "certifications")

    y = section(canvas, str(data["language_heading"]), y, audit)
    y = paragraph(escape(str(data["language"])), compact, canvas, y, audit, "languages")

    audit.validate(path.name, y)
    canvas.save()
    print(f"generated {path} | final y={y:.1f} | blocks={len(audit.blocks)}")
    return path


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for data in (PT, EN):
        generate(data)


if __name__ == "__main__":
    main()
