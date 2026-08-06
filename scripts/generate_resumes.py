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
LEFT = 44
RIGHT = 44
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
    "location": "Rio de Janeiro - RJ | remoto, híbrido ou presencial",
    "portfolio_label": "Portfólio",
    "phone_label": "Telefone/WhatsApp: +55 (21) 96481-0480",
    "summary_heading": "RESUMO PROFISSIONAL",
    "summary": (
        "Analista de Automação, IA e Integrações com atuação ponta a ponta em processos e sistemas internos. "
        "Experiência com n8n self-hosted, Python, APIs REST, IA generativa, agentes e bancos de dados, incluindo mais de "
        "10 mil execuções de workflows em produção. Entrego do levantamento à sustentação, com confiabilidade e impacto mensurável."
    ),
    "skills_heading": "HABILIDADES TÉCNICAS",
    "skills": [
        "<b>Automação e processos:</b> n8n self-hosted, automação low-code, workflows, AS-IS/TO-BE, requisitos, regras de negócio, aprovação humana, documentação e melhoria contínua.",
        "<b>IA generativa e agentes:</b> OpenAI, Gemini, Ollama/OpenRouter, Codex, APIs de LLM, engenharia de prompts, recuperação de contexto/grounding, JSON Schema, pipelines multiestágio, IA multimodal, text-to-video e revisão humana.",
        "<b>Integrações, engenharia e confiabilidade:</b> APIs REST, webhooks, OAuth 2.0, SMTP/IMAP, Meta Graph API, Python, JavaScript/TypeScript, Node.js/Express, FastAPI, SQL, PostgreSQL/SQLite, Docker, Git/GitHub Actions, CI/CD, testes, logs, retries, idempotência, backups e segredos.",
    ],
    "experience_heading": "EXPERIÊNCIA PROFISSIONAL",
    "vesper_org": "GRUPO VESPER",
    "vesper_company": "Vesper Equipamentos EX e Vent Rio Equipamentos",
    "vesper_date": "12/2025 - presente",
    "vesper_role": "Técnico Júnior em Automação de Processos (cargo formal) | automação, IA aplicada e integrações",
    "vesper_points": [
        "Administro n8n self-hosted em Windows/Docker com mais de 10 mil execuções de workflows em produção, integrando APIs, webhooks, PostgreSQL e SMTP com logs, retries, alertas, backups e auditoria.",
        "Desenvolvi o Vesper Propostas com ODT/PDF, IMAP/SMTP e revisão humana, reduzindo propostas simples de 2-4 minutos para menos de 30 segundos; uso diário por 4 profissionais.",
        "Implantei o Produção Operacional em 11 computadores e uma TV de fábrica e o HelpDesk para 11 usuários; conduzo requisitos, AS-IS/TO-BE, arquitetura, testes, implantação, treinamento e sustentação.",
    ],
    "compasso_org": "COMPASSO TECNOLOGIA LTDA",
    "compasso_date": "10/2024 - 03/2025",
    "compasso_role": "Estagiário de TI/Dados",
    "compasso_point": (
        "Reduzi de aproximadamente 3 horas para cerca de 5 minutos uma rotina com Python/Pandas; atuei também com AWS S3/EC2, "
        "boto3, Pandas/Polars, SQL, Docker, suporte e documentação."
    ),
    "projects_heading": "PROJETOS SELECIONADOS",
    "projects": [
        "<b>Mala Direta:</b> automação n8n em produção com 2 workflows; fluxo principal com 158 nós e 9 Data Tables de domínio, fila por destinatário, deduplicação, SMTP, auditoria e campanha para 900+ destinatários.",
        "<b>Catálogo Operacional de Compras:</b> sistema interno usado diariamente por 3 usuários e consultado pela gestão; FastAPI, busca SQLite FTS5 por código/nome/fornecedor, controle de concorrência por revisão, backups e OCR.",
        "<b>Postagem Redes:</b> 3 workflows n8n para portal, ações e mídia; workflow de ações com 58 nós, Meta Graph API, OpenAI/Gemini/Ollama, aprovação humana, idempotência e Facebook validado em teste.",
        "<b>Portal - em desenvolvimento:</b> Business Operating Platform multiempresa em React/TypeScript, FastAPI e PostgreSQL, com tenant/RLS, Action Envelope, aprovações versionadas e outbox; Procurement validado em sandbox e em preparação para piloto interno.",
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
    "language": "Português nativo | Inglês técnico para leitura; escrita e conversação básicas.",
}

EN = {
    "filename": "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
    "title": "AI AUTOMATION & INTEGRATIONS ANALYST",
    "location": "Rio de Janeiro - Brazil | remote, hybrid or on-site",
    "portfolio_label": "Portfolio",
    "phone_label": "Phone/WhatsApp: +55 (21) 96481-0480",
    "summary_heading": "PROFESSIONAL SUMMARY",
    "summary": (
        "AI Automation and Integrations Analyst with end-to-end experience in processes and internal systems. Skilled in self-hosted n8n, "
        "Python, REST APIs, generative AI, agents and databases, including more than 10,000 production workflow executions. "
        "Delivers from discovery through support, focused on reliability and measurable impact."
    ),
    "skills_heading": "TECHNICAL SKILLS",
    "skills": [
        "<b>Automation and processes:</b> self-hosted n8n, low-code automation, workflows, AS-IS/TO-BE, requirements, business rules, human approval, documentation and continuous improvement.",
        "<b>Generative AI and agents:</b> OpenAI, Gemini, Ollama/OpenRouter, Codex, LLM APIs, prompt engineering, context retrieval/grounding, JSON Schema, multi-stage pipelines, multimodal AI, text-to-video and human review.",
        "<b>Integrations, engineering and reliability:</b> REST APIs, webhooks, OAuth 2.0, SMTP/IMAP, Meta Graph API, Python, JavaScript/TypeScript, Node.js/Express, FastAPI, SQL, PostgreSQL/SQLite, Docker, Git/GitHub Actions, CI/CD, tests, logs, retries, idempotency, backups and secrets.",
    ],
    "experience_heading": "PROFESSIONAL EXPERIENCE",
    "vesper_org": "GRUPO VESPER",
    "vesper_company": "Vesper Equipamentos EX e Vent Rio Equipamentos",
    "vesper_date": "12/2025 - Present",
    "vesper_role": "Junior Process Automation Technician (formal title) | automation, applied AI and integrations",
    "vesper_points": [
        "Administer self-hosted n8n on Windows/Docker with more than 10,000 production workflow executions, integrating APIs, webhooks, PostgreSQL and SMTP with logs, retries, alerts, backups and auditing.",
        "Developed Vesper Propostas with ODT/PDF, IMAP/SMTP and human review, reducing simple proposals from 2-4 minutes to under 30 seconds; used daily by 4 professionals.",
        "Deployed Produção Operacional to 11 workstations and a factory TV and HelpDesk to 11 users; lead requirements, AS-IS/TO-BE, architecture, testing, deployment, training and support.",
    ],
    "compasso_org": "COMPASSO TECNOLOGIA LTDA",
    "compasso_date": "10/2024 - 03/2025",
    "compasso_role": "IT/Data Intern",
    "compasso_point": (
        "Reduced a routine from approximately 3 hours to around 5 minutes with Python/Pandas; also worked with AWS S3/EC2, boto3, "
        "Pandas/Polars, SQL, Docker, support and documentation."
    ),
    "projects_heading": "SELECTED PROJECTS",
    "projects": [
        "<b>Mala Direta:</b> production n8n automation with 2 workflows; the main workflow has 158 nodes and 9 domain Data Tables, per-recipient queues, deduplication, SMTP, auditing and a 900+ recipient campaign.",
        "<b>Operational Procurement Catalog:</b> internal system used daily by 3 users and consulted by management; FastAPI, SQLite FTS5 search by code/name/supplier, optimistic revision control, backups and OCR.",
        "<b>Postagem Redes:</b> 3 n8n workflows for portal, actions and media; the actions workflow has 58 nodes, Meta Graph API, OpenAI/Gemini/Ollama, human approval, idempotency and Facebook validated in testing.",
        "<b>Portal - in development:</b> multi-tenant Business Operating Platform using React/TypeScript, FastAPI and PostgreSQL, with tenant/RLS, versioned Action Envelopes, approvals and outbox; Procurement validated in sandbox and being prepared for an internal pilot.",
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
    "language": "Portuguese: native | English: technical reading; basic writing and conversation.",
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
    top = y - 8
    heading_baseline = top - 10.2
    bar_bottom = heading_baseline - 1
    line_y = heading_baseline - 5.3
    bottom = line_y - 8
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
    size = 8.3
    leading = 11.5
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
        "automation, process automation, process mapping, AS-IS, TO-BE, n8n, low-code, generative AI, AI agents, Codex, "
        "multimodal AI, text-to-video, systems integration, REST APIs, webhooks, Python, JavaScript, TypeScript, FastAPI, "
        "PostgreSQL, FTS5, Docker, RLS, outbox, Action Envelope"
    )
    canvas.setCreator("Maycon Ferreira")

    base = ParagraphStyle("base", fontName=FONT, fontSize=9.55, leading=11.9, textColor=INK)
    skill = ParagraphStyle("skill", parent=base, fontSize=9.15, leading=11.35)
    role = ParagraphStyle("role", parent=base, fontSize=8.95, leading=11.2, textColor=MUTED)
    bullet = ParagraphStyle("bullet", parent=base, fontSize=8.95, leading=11.25, leftIndent=13, firstLineIndent=-9)
    project = ParagraphStyle("project", parent=base, fontSize=8.55, leading=10.55, leftIndent=13, firstLineIndent=-9)
    compact = ParagraphStyle("compact", parent=base, fontSize=8.95, leading=11.15)

    audit = LayoutAudit()
    y = PAGE_H - 36
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H - 6, PAGE_W, 6, fill=1, stroke=0)

    canvas.setFillColor(INK)
    canvas.setFont(FONT_BOLD, 18.7)
    canvas.drawString(LEFT, y, "MAYCON FERREIRA")
    audit.add("header:name", y + 4, y - 4)
    y -= 17
    canvas.setFillColor(ACCENT)
    canvas.setFont(FONT_BOLD, 10.3)
    canvas.drawString(LEFT, y, str(data["title"]))
    audit.add("header:title", y + 2, y - 3)
    y -= 14
    canvas.setFillColor(MUTED)
    canvas.setFont(FONT, 8.65)
    canvas.drawString(LEFT, y, str(data["location"]))
    audit.add("header:location", y + 2, y - 3)
    y -= 12

    y = link_line(canvas, y, [(str(data["phone_label"]), "https://wa.me/5521964810480"), ("E-mail: mayconxz00dev@gmail.com", "mailto:mayconxz00dev@gmail.com")], audit, "header:contact")
    y = link_line(canvas, y, [("LinkedIn: linkedin.com/in/maycon-ferreira-7bb870231/", "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"), ("GitHub: github.com/Mayconxzdev", "https://github.com/Mayconxzdev"), (f"{data['portfolio_label']}: mayconxzdev.github.io", "https://mayconxzdev.github.io/")], audit, "header:profiles")
    canvas.setStrokeColor(LINE)
    canvas.line(LEFT, y - 1, LEFT + CONTENT_W, y - 1)
    y -= 3

    y = section(canvas, str(data["summary_heading"]), y, audit)
    y = paragraph(escape(str(data["summary"])), base, canvas, y, audit, "summary")

    y = section(canvas, str(data["skills_heading"]), y, audit)
    for index, item in enumerate(data["skills"]):
        y = paragraph(str(item), skill, canvas, y, audit, f"skill:{index + 1}") - 2.0

    y = section(canvas, str(data["experience_heading"]), y, audit)
    y = draw_role_header(canvas, y, str(data["vesper_org"]), str(data["vesper_date"]), audit, "role:vesper-header")
    y = paragraph(escape(str(data["vesper_company"])), role, canvas, y, audit, "role:vesper-company") - 0.5
    y = paragraph(escape(str(data["vesper_role"])), role, canvas, y, audit, "role:vesper-title") - 1.5
    for index, item in enumerate(data["vesper_points"]):
        y = paragraph("- " + escape(str(item)), bullet, canvas, y, audit, f"vesper-bullet:{index + 1}") - 2.0

    y -= 3
    y = draw_role_header(canvas, y, str(data["compasso_org"]), str(data["compasso_date"]), audit, "role:compasso-header")
    y = paragraph(escape(str(data["compasso_role"])), role, canvas, y, audit, "role:compasso-title") - 1
    y = paragraph("- " + escape(str(data["compasso_point"])), bullet, canvas, y, audit, "compasso-bullet")

    y = section(canvas, str(data["projects_heading"]), y, audit)
    for index, item in enumerate(data["projects"]):
        y = paragraph("- " + str(item), project, canvas, y, audit, f"project:{index + 1}") - 1.8

    y = section(canvas, str(data["education_heading"]), y, audit)
    for index, item in enumerate(data["education"]):
        y = paragraph(str(item), compact, canvas, y, audit, f"education:{index + 1}") - 1

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
