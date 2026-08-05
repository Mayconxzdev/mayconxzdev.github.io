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
    "summary_heading": "RESUMO PROFISSIONAL",
    "summary": (
        "Analista de Automação, IA e Integrações que transforma processos internos em automações e sistemas em produção. "
        "Experiência com n8n self-hosted, Python, APIs REST, IA generativa, agentes e bancos de dados, com mais de 10 mil "
        "execuções. Atuação do levantamento à sustentação, com foco em confiabilidade e resultados mensuráveis."
    ),
    "skills_heading": "HABILIDADES TÉCNICAS",
    "skills": [
        "<b>Automação e processos:</b> n8n self-hosted, workflows, AS-IS/TO-BE, requisitos, regras de negócio, aprovação humana, documentação e melhoria contínua.",
        "<b>IA generativa e agentes de IA:</b> OpenAI, Gemini, Ollama/OpenRouter, APIs de LLM, engenharia de prompts, recuperação de contexto/grounding, JSON Schema, pipelines multiestágio, IA multimodal, text-to-video e revisão humana.",
        "<b>Integração de sistemas e ferramentas:</b> APIs REST, webhooks, HTTP/JSON, OAuth 2.0, SMTP/IMAP, Meta Graph API, Evolution API/WPPConnect e Google Sheets.",
        "<b>Engenharia e confiabilidade:</b> Python, JavaScript/TypeScript, Node.js/Express, FastAPI, SQL, PostgreSQL/SQLite, Docker, Git/GitHub Actions, CI/CD, testes, logs, retries, idempotência, backups e gestão de segredos.",
    ],
    "experience_heading": "EXPERIÊNCIA PROFISSIONAL",
    "vesper_org": "GRUPO VESPER - VESPER EQUIPAMENTOS EX E VENT RIO EQUIPAMENTOS",
    "vesper_date": "12/2025 - presente",
    "vesper_role": "Técnico Júnior em Automação de Processos (cargo formal) | automação, IA aplicada e integrações",
    "vesper_points": [
        "Administro ambiente n8n self-hosted em Windows/Docker com mais de 10 mil execuções em produção, integrando APIs, webhooks, PostgreSQL, SMTP e ferramentas internas com logs, retries, alertas, backups e auditoria.",
        "Desenvolvi o Vesper Propostas com geração ODT/PDF, IMAP/SMTP e revisão humana; propostas simples passaram de aproximadamente 2-4 minutos para menos de 30 segundos, em uso diário por 4 profissionais.",
        "Implantei o Produção Operacional em 11 computadores e uma TV de fábrica e o HelpDesk para 11 usuários; conduzo requisitos, mapeamento AS-IS/TO-BE, arquitetura, testes, implantação, treinamento, monitoramento e sustentação.",
    ],
    "compasso_org": "COMPASSO TECNOLOGIA LTDA",
    "compasso_date": "10/2024 - 03/2025",
    "compasso_role": "Estagiário de TI/Dados",
    "compasso_point": (
        "Reduzi de aproximadamente 3 horas para cerca de 5 minutos o processamento de uma rotina com Python/Pandas; "
        "atuei também com AWS S3/EC2, boto3, Pandas/Polars, SQL, Docker, suporte e documentação."
    ),
    "projects_heading": "PROJETOS SELECIONADOS",
    "projects": [
        "<b>Mala Direta:</b> automação n8n em produção com 158 nós, 9 Data Tables, fila por destinatário, deduplicação, SMTP, cancelamento revalidado e campanha com mais de 900 destinatários.",
        "<b>Postagem Redes:</b> 3 workflows e 58 nós, Meta Graph API e cadeia OpenAI - Gemini - Ollama com aprovação humana, idempotência e resultado independente por rede.",
    ],
    "education_heading": "FORMAÇÃO",
    "education": [
        "<b>Tecnólogo em Análise e Desenvolvimento de Sistemas - UNISUAM</b> | conclusão prevista: dez. 2026",
        "Piscine 42 Rio | programa intensivo concluído em jul. 2025",
    ],
    "certs_heading": "CERTIFICAÇÕES",
    "certs": (
        "Ferramentas de IA: Agentes e Automações - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; "
        "Automação de Processos através da RPA - ENAP (25h); Mapeamento e Automação de Processos - ENAP (20h); "
        "Introdução à LGPD - ENAP (10h)."
    ),
    "language_heading": "IDIOMAS",
    "language": "Inglês técnico para leitura; escrita e conversação básicas.",
}

EN = {
    "filename": "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
    "title": "AI AUTOMATION & INTEGRATIONS ANALYST",
    "location": "Rio de Janeiro - Brazil | remote, hybrid or on-site",
    "portfolio_label": "Portfolio",
    "summary_heading": "PROFESSIONAL SUMMARY",
    "summary": (
        "AI Automation and Integrations Analyst who turns internal processes into production automations and systems. "
        "Experience with self-hosted n8n, Python, REST APIs, generative AI, agents and databases, with more than 10,000 "
        "executions. Works from discovery through support, focused on reliability and measurable outcomes."
    ),
    "skills_heading": "TECHNICAL SKILLS",
    "skills": [
        "<b>Automation and processes:</b> self-hosted n8n, workflows, AS-IS/TO-BE, requirements, business rules, human approval, documentation and continuous improvement.",
        "<b>Generative AI and AI agents:</b> OpenAI, Gemini, Ollama/OpenRouter, LLM APIs, prompt engineering, context retrieval/grounding, JSON Schema, multi-stage pipelines, multimodal AI, text-to-video and human review.",
        "<b>Systems and tools integration:</b> REST APIs, webhooks, HTTP/JSON, OAuth 2.0, SMTP/IMAP, Meta Graph API, Evolution API/WPPConnect and Google Sheets.",
        "<b>Engineering and reliability:</b> Python, JavaScript/TypeScript, Node.js/Express, FastAPI, SQL, PostgreSQL/SQLite, Docker, Git/GitHub Actions, CI/CD, tests, logs, retries, idempotency, backups and secrets management.",
    ],
    "experience_heading": "PROFESSIONAL EXPERIENCE",
    "vesper_org": "GRUPO VESPER - VESPER EQUIPAMENTOS EX AND VENT RIO EQUIPAMENTOS",
    "vesper_date": "12/2025 - Present",
    "vesper_role": "Junior Process Automation Technician (formal title) | automation, applied AI and integrations",
    "vesper_points": [
        "Administer a self-hosted n8n environment on Windows/Docker with more than 10,000 production executions, integrating APIs, webhooks, PostgreSQL, SMTP and internal tools with logs, retries, alerts, backups and auditing.",
        "Developed Vesper Propostas with ODT/PDF generation, IMAP/SMTP and human review; simple proposals went from approximately 2-4 minutes to under 30 seconds, with daily use by 4 professionals.",
        "Deployed Produção Operacional to 11 workstations and a factory TV and HelpDesk to 11 users; lead requirements, AS-IS/TO-BE mapping, architecture, testing, deployment, training, monitoring and support.",
    ],
    "compasso_org": "COMPASSO TECNOLOGIA LTDA",
    "compasso_date": "10/2024 - 03/2025",
    "compasso_role": "IT/Data Intern",
    "compasso_point": (
        "Reduced a processing routine from approximately 3 hours to around 5 minutes with Python/Pandas; also worked with "
        "AWS S3/EC2, boto3, Pandas/Polars, SQL, Docker, support and documentation."
    ),
    "projects_heading": "SELECTED PROJECTS",
    "projects": [
        "<b>Mala Direta:</b> production n8n automation with 158 nodes, 9 Data Tables, per-recipient queue, deduplication, SMTP, revalidated cancellation and a campaign with more than 900 recipients.",
        "<b>Postagem Redes:</b> 3 workflows and 58 nodes, Meta Graph API and an OpenAI - Gemini - Ollama chain with human approval, idempotency and independent results per channel.",
    ],
    "education_heading": "EDUCATION",
    "education": [
        "<b>Associate Degree in Systems Analysis and Development - UNISUAM</b> | expected completion: Dec. 2026",
        "42 Rio Piscine | intensive program completed in Jul. 2025",
    ],
    "certs_heading": "CERTIFICATIONS",
    "certs": (
        "AI Tools: Agents and Automations - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; "
        "Process Automation through RPA - ENAP (25h); Process Mapping and Automation - ENAP (20h); "
        "Introduction to Brazil's Data Protection Law - ENAP (10h)."
    ),
    "language_heading": "LANGUAGES",
    "language": "Technical English for reading; basic writing and conversation.",
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
        for previous, current in zip(self.blocks, self.blocks[1:]):
            if previous.name.startswith("section:") or current.name.startswith("section:"):
                continue
            gap = previous.bottom - current.top
            if gap < -0.25:
                raise RuntimeError(f"negative visual gap between {previous.name} and {current.name}: {gap:.1f}pt")


def paragraph(
    text: str,
    style: ParagraphStyle,
    canvas: Canvas,
    y: float,
    audit: LayoutAudit,
    name: str,
    indent: float = 0,
) -> float:
    item = Paragraph(text, style)
    _, height = item.wrap(CONTENT_W - indent, 999)
    bottom = y - height
    item.drawOn(canvas, LEFT + indent, bottom)
    audit.add(name, y, bottom)
    return bottom


def section(canvas: Canvas, title: str, y: float, audit: LayoutAudit) -> float:
    top = y - 9
    heading_baseline = top - 10.5
    bar_bottom = heading_baseline - 1
    line_y = heading_baseline - 5.5
    bottom = line_y - 9

    canvas.setFillColor(ACCENT)
    canvas.rect(LEFT, bar_bottom, 4, 12, fill=1, stroke=0)
    canvas.setFillColor(INK)
    canvas.setFont(FONT_BOLD, 9.9)
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
    size = 8.35
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


def draw_role_header(
    canvas: Canvas,
    y: float,
    organization: str,
    date: str,
    audit: LayoutAudit,
    name: str,
) -> float:
    top = y
    org_size = 9.0
    date_size = 8.0
    date_width = text_width(date, FONT, date_size)
    org_width = text_width(organization, FONT_BOLD, org_size)
    available = CONTENT_W - date_width - 14
    if org_width > available:
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
    canvas.setSubject("One-page resume for process automation, AI agents, generative AI and systems integration roles")
    canvas.setKeywords(
        "automation, process automation, process mapping, AS-IS, TO-BE, n8n, generative AI, AI agents, prompt engineering, "
        "context retrieval, grounding, multimodal AI, text-to-video, systems integration, REST APIs, webhooks, Python, JavaScript, TypeScript, SQL, Docker"
    )
    canvas.setCreator("Maycon Ferreira")

    base = ParagraphStyle("base", fontName=FONT, fontSize=9.75, leading=12.3, textColor=INK)
    skill = ParagraphStyle("skill", parent=base, fontSize=9.4, leading=11.8)
    role = ParagraphStyle("role", parent=base, fontSize=9.15, leading=11.5, textColor=MUTED)
    bullet = ParagraphStyle("bullet", parent=base, fontSize=9.15, leading=11.7, leftIndent=13, firstLineIndent=-9)
    compact = ParagraphStyle("compact", parent=base, fontSize=9.15, leading=11.5)

    audit = LayoutAudit()
    y = PAGE_H - 36
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H - 6, PAGE_W, 6, fill=1, stroke=0)

    name_top = y + 4
    canvas.setFillColor(INK)
    canvas.setFont(FONT_BOLD, 18.7)
    canvas.drawString(LEFT, y, "MAYCON FERREIRA")
    audit.add("header:name", name_top, y - 4)
    y -= 17

    title_top = y + 2
    canvas.setFillColor(ACCENT)
    canvas.setFont(FONT_BOLD, 10.3)
    canvas.drawString(LEFT, y, str(data["title"]))
    audit.add("header:title", title_top, y - 3)
    y -= 14

    location_top = y + 2
    canvas.setFillColor(MUTED)
    canvas.setFont(FONT, 8.65)
    canvas.drawString(LEFT, y, str(data["location"]))
    audit.add("header:location", location_top, y - 3)
    y -= 12

    y = link_line(
        canvas,
        y,
        [
            ("WhatsApp: +55 (21) 96481-0480", "https://wa.me/5521964810480"),
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
    canvas.setLineWidth(0.6)
    canvas.line(LEFT, y - 1, LEFT + CONTENT_W, y - 1)
    y -= 3

    y = section(canvas, str(data["summary_heading"]), y, audit)
    y = paragraph(escape(str(data["summary"])), base, canvas, y, audit, "summary")

    y = section(canvas, str(data["skills_heading"]), y, audit)
    for index, item in enumerate(data["skills"]):
        y = paragraph(str(item), skill, canvas, y, audit, f"skill:{index + 1}")
        y -= 2.5

    y = section(canvas, str(data["experience_heading"]), y, audit)
    y = draw_role_header(
        canvas, y, str(data["vesper_org"]), str(data["vesper_date"]), audit, "role:vesper-header"
    )
    y = paragraph(escape(str(data["vesper_role"])), role, canvas, y, audit, "role:vesper-title")
    y -= 2
    for index, item in enumerate(data["vesper_points"]):
        y = paragraph("- " + escape(str(item)), bullet, canvas, y, audit, f"vesper-bullet:{index + 1}")
        y -= 2.5

    y -= 4
    y = draw_role_header(
        canvas, y, str(data["compasso_org"]), str(data["compasso_date"]), audit, "role:compasso-header"
    )
    y = paragraph(escape(str(data["compasso_role"])), role, canvas, y, audit, "role:compasso-title")
    y -= 1.5
    y = paragraph("- " + escape(str(data["compasso_point"])), bullet, canvas, y, audit, "compasso-bullet")

    y = section(canvas, str(data["projects_heading"]), y, audit)
    for index, item in enumerate(data["projects"]):
        y = paragraph("- " + str(item), bullet, canvas, y, audit, f"project:{index + 1}")
        y -= 2.5

    y = section(canvas, str(data["education_heading"]), y, audit)
    for index, item in enumerate(data["education"]):
        y = paragraph(str(item), compact, canvas, y, audit, f"education:{index + 1}")
        y -= 1.5

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
