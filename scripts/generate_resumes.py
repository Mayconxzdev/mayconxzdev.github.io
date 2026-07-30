"""Generate the public PT-BR and English one-page resume PDFs.

The PDFs are deliberately generated from this source rather than manually edited.
It keeps the public versions equivalent, preserves selectable ATS text and makes every
contact destination an actual PDF hyperlink.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "cv"

PAGE_W, PAGE_H = A4
LEFT = 48
RIGHT = 48
CONTENT_W = PAGE_W - LEFT - RIGHT

INK = HexColor("#111827")
MUTED = HexColor("#475569")
LINE = HexColor("#CBD5E1")
ACCENT = HexColor("#0F4C81")
PALE = HexColor("#EAF2FA")


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("ResumeSans", r"C:\Windows\Fonts\arial.ttf"))
    pdfmetrics.registerFont(TTFont("ResumeSans-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
    pdfmetrics.registerFontFamily(
        "ResumeSans", normal="ResumeSans", bold="ResumeSans-Bold", italic="ResumeSans", boldItalic="ResumeSans-Bold"
    )


PT = {
    "filename": "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    "title": "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
    "location": "Rio de Janeiro - RJ, Brasil",
    "footer": "Portfólio público: mayconxzdev.github.io",
    "portfolio_label": "Portfólio",
    "summary_heading": "RESUMO PROFISSIONAL",
    "summary": (
        "Profissional de automação, IA aplicada e integrações com atuação ponta a ponta em sistemas internos: "
        "mapeamento de processos, requisitos, arquitetura, desenvolvimento, implantação, treinamento, monitoramento e sustentação. "
        "Experiência com n8n self-hosted, Python, APIs REST, bancos de dados e fluxos com aprovação humana, filas, idempotência, auditoria e tratamento de falhas."
    ),
    "skills_heading": "COMPETÊNCIAS PRINCIPAIS",
    "skills": [
        "<b>Automação e processos:</b> n8n self-hosted, workflows, low-code, AS-IS/TO-BE, requisitos, regras de negócio, documentação, treinamento e aprovação humana.",
        "<b>IA aplicada:</b> OpenAI, Gemini, Ollama e OpenRouter; assistentes e agentes com ferramentas, memória, recuperação de contexto, saída estruturada, fallback e revisão humana.",
        "<b>Integrações:</b> APIs REST, webhooks, HTTP/JSON, OAuth 2.0, SMTP/IMAP, Meta Graph API, Evolution API/WPPConnect, Supabase, Firebase e Postman.",
        "<b>Engenharia e confiabilidade:</b> Python, JavaScript/TypeScript, FastAPI, SQL, PostgreSQL, SQLite, Docker, Git/GitHub Actions, testes, logs, backups, alertas, retries, idempotência e gestão de segredos.",
    ],
    "experience_heading": "EXPERIÊNCIA PROFISSIONAL",
    "vesper_org": "GRUPO VESPER - VESPER EQUIPAMENTOS EX E VENT RIO EQUIPAMENTOS",
    "vesper_date": "dez. 2025 - atual",
    "vesper_role": "Técnico Júnior em Automação de Processos (cargo formal) | automação, IA aplicada e integrações",
    "vesper_points": [
        "Conduzo o ciclo técnico de soluções internas: levantamento com gestão e usuários, regras, arquitetura, desenvolvimento, testes, implantação, documentação, treinamento e sustentação.",
        "Administro automações n8n self-hosted em Windows/Docker, com APIs, webhooks, persistência, backups, alertas, retries, auditoria e diagnóstico.",
        "Desenvolvi Vesper Propostas com geração ODT/PDF, IMAP/SMTP e revisão humana; o case documenta redução observada no tempo de propostas simples.",
        "Implementei HelpDesk, Produção Operacional, ProcureFlow, ComprasVesper, Mala Direta e Postagem Redes para rotinas de TI, produção, compras e comunicação, com limites operacionais declarados.",
    ],
    "compasso_org": "COMPASSO TECNOLOGIA LTDA",
    "compasso_date": "out. 2024 - mar. 2025",
    "compasso_role": "Estagiário de TI/Dados",
    "compasso_point": "Automatizei rotina em Python/Pandas, reduzindo processamento observado de aproximadamente 3 horas para cerca de 5 minutos; atuei também com AWS S3/EC2, boto3, Pandas/Polars, SQL, Docker, suporte e documentação.",
    "education_heading": "EVIDÊNCIAS, FORMAÇÃO E CERTIFICAÇÕES",
    "education": [
        "<b>Portfólio:</b> cases públicos e sanitizados com arquitetura, screenshots, testes e CI para automação n8n, integrações, desktop, PWA e sistemas internos.",
        "<b>Formação:</b> Tecnólogo em Análise e Desenvolvimento de Sistemas - UNISUAM | conclusão prevista: dez. 2026. Piscine 42 Rio concluída em jul. 2025.",
        "<b>Certificações:</b> Ferramentas de IA: Agentes e Automações - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; RPA para Transformação Digital - ENAP (25h); Mapeamento e Automação de Processos - ENAP (20h); LGPD - ENAP (10h).",
        "<b>Idiomas e disponibilidade:</b> inglês técnico para leitura; escrita e conversação básicas. Disponível para trabalho remoto, híbrido ou presencial; viagens e mudança.",
    ],
}

EN = {
    "filename": "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
    "title": "AI AUTOMATION & INTEGRATIONS ANALYST",
    "location": "Rio de Janeiro - Brazil",
    "footer": "Public portfolio: mayconxzdev.github.io",
    "portfolio_label": "Portfolio",
    "summary_heading": "PROFESSIONAL SUMMARY",
    "summary": (
        "Automation, applied AI and integrations professional working end to end on internal systems: process mapping, requirements, architecture, development, deployment, training, monitoring and support. "
        "Experience with self-hosted n8n, Python, REST APIs, databases and workflows with human approval, queues, idempotency, auditing and failure handling."
    ),
    "skills_heading": "CORE COMPETENCIES",
    "skills": [
        "<b>Automation and processes:</b> self-hosted n8n, workflows, low-code, AS-IS/TO-BE, requirements, business rules, documentation, training and human approval.",
        "<b>Applied AI:</b> OpenAI, Gemini, Ollama and OpenRouter; assistants and agents with tools, memory, context retrieval, structured output, fallback and human review.",
        "<b>Integrations:</b> REST APIs, webhooks, HTTP/JSON, OAuth 2.0, SMTP/IMAP, Meta Graph API, Evolution API/WPPConnect, Supabase, Firebase and Postman.",
        "<b>Engineering and reliability:</b> Python, JavaScript/TypeScript, FastAPI, SQL, PostgreSQL, SQLite, Docker, Git/GitHub Actions, tests, logs, backups, alerts, retries, idempotency and secrets management.",
    ],
    "experience_heading": "PROFESSIONAL EXPERIENCE",
    "vesper_org": "GRUPO VESPER - VESPER EQUIPAMENTOS EX AND VENT RIO EQUIPAMENTOS",
    "vesper_date": "Dec. 2025 - Present",
    "vesper_role": "Junior Process Automation Technician (formal job title) | automation, applied AI and integrations",
    "vesper_points": [
        "Lead the technical lifecycle of internal solutions: discovery with management and users, rules, architecture, development, testing, deployment, documentation, training and support.",
        "Administer self-hosted n8n automations in Windows/Docker with APIs, webhooks, persistence, backups, alerts, retries, auditing and diagnosis.",
        "Developed Vesper Propostas with ODT/PDF generation, IMAP/SMTP and human review; the case documents an observed reduction in simple-proposal time.",
        "Implemented HelpDesk, Produção Operacional, ProcureFlow, ComprasVesper, Mala Direta and Postagem Redes for IT, production, purchasing and communication routines, with declared operational limits.",
    ],
    "compasso_org": "COMPASSO TECNOLOGIA LTDA",
    "compasso_date": "Oct. 2024 - Mar. 2025",
    "compasso_role": "IT/Data Intern",
    "compasso_point": "Automated a Python/Pandas routine, reducing observed processing time from approximately three hours to around five minutes; also worked with AWS S3/EC2, boto3, Pandas/Polars, SQL, Docker, support and documentation.",
    "education_heading": "EVIDENCE, EDUCATION & CERTIFICATIONS",
    "education": [
        "<b>Portfolio:</b> public and sanitized case studies with architecture, screenshots, tests and CI for n8n automation, integrations, desktop apps, PWA and internal systems.",
        "<b>Education:</b> Associate Degree in Systems Analysis and Development - UNISUAM | expected completion: Dec. 2026. 42 Rio Piscine completed in Jul. 2025.",
        "<b>Certifications:</b> AI Tools: Agents and Automations - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; Process Automation by RPA - ENAP (25h); Process Mapping and Automation - ENAP (20h); LGPD - ENAP (10h).",
        "<b>Languages and availability:</b> technical English for reading; basic writing and conversation. Available for remote, hybrid or on-site work; travel and relocation.",
    ],
}


def paragraph(text: str, style: ParagraphStyle, canvas: Canvas, y: float, indent: float = 0) -> float:
    item = Paragraph(text, style)
    width = CONTENT_W - indent
    _, height = item.wrap(width, 999)
    item.drawOn(canvas, LEFT + indent, y - height)
    return y - height


def section(canvas: Canvas, title: str, y: float) -> float:
    # Headings deliberately create breathing room instead of letting the next
    # organisation/title visually touch the divider line.
    y -= 15
    canvas.setFillColor(ACCENT)
    canvas.rect(LEFT, y - 2, 4, 13, fill=1, stroke=0)
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 10.2)
    canvas.drawString(LEFT + 10, y, title)
    y -= 6
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(LEFT, y, LEFT + CONTENT_W, y)
    return y - 13


def text_width(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def link_line(canvas: Canvas, y: float, items: list[tuple[str, str]]) -> float:
    """Draw labelled contacts, wrapping at a natural boundary, with a link on every value."""
    x = LEFT
    font = "ResumeSans"
    size = 9.35
    leading = 14
    canvas.setFont(font, size)
    for label, url in items:
        label_text = label + "  "
        width = text_width(label_text, font, size)
        if x != LEFT and x + width > LEFT + CONTENT_W:
            x = LEFT
            y -= leading
        canvas.setFillColor(MUTED)
        canvas.drawString(x, y, label_text)
        canvas.linkURL(url, (x, y - 2, x + width, y + size + 2), relative=0, thickness=0)
        x += width + 12
    return y - leading


def draw_header(canvas: Canvas, data: dict[str, object]) -> float:
    y = PAGE_H - 42
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H - 8, PAGE_W, 8, fill=1, stroke=0)
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 19)
    canvas.drawString(LEFT, y, "MAYCON FERREIRA")
    y -= 17
    canvas.setFillColor(ACCENT)
    canvas.setFont("ResumeSans-Bold", 10.7)
    canvas.drawString(LEFT, y, str(data["title"]))
    y -= 16
    canvas.setFillColor(MUTED)
    canvas.setFont("ResumeSans", 9.1)
    canvas.drawString(LEFT, y, str(data["location"]))
    y -= 14
    y = link_line(canvas, y, [
        ("WhatsApp: +55 (21) 96481-0480", "https://wa.me/5521964810480"),
        ("E-mail: mayconxz00dev@gmail.com", "mailto:mayconxz00dev@gmail.com"),
    ])
    y = link_line(canvas, y, [
        ("LinkedIn: www.linkedin.com/in/maycon-ferreira-7bb870231/", "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"),
        ("GitHub: github.com/Mayconxzdev", "https://github.com/Mayconxzdev"),
        (f"{data['portfolio_label']}: mayconxzdev.github.io", "https://mayconxzdev.github.io/"),
    ])
    canvas.setStrokeColor(LINE)
    canvas.line(LEFT, y - 2, LEFT + CONTENT_W, y - 2)
    return y - 10


def generate(data: dict[str, object]) -> Path:
    out = OUTPUT / str(data["filename"])
    canvas = Canvas(str(out), pagesize=A4, pageCompression=1)
    canvas.setTitle(f"Maycon Ferreira - {data['title']}")
    canvas.setAuthor("Maycon Ferreira")
    canvas.setSubject("Professional resume for automation, applied AI and systems integrations roles")
    canvas.setKeywords("automation, applied AI, integrations, n8n, Python, APIs, FastAPI, SQL, Docker")
    canvas.setCreator("Maycon Ferreira")

    # A recruiter should be able to read this at 100% without zooming. The
    # leading uses the available page height rather than compressing content.
    base = ParagraphStyle("base", fontName="ResumeSans", fontSize=9.75, leading=13.35, textColor=INK, spaceAfter=0)
    skill = ParagraphStyle("skill", parent=base, fontSize=9.5, leading=12.85)
    role = ParagraphStyle("role", parent=base, fontSize=9.6, leading=12.75, textColor=MUTED)
    bullet = ParagraphStyle("bullet", parent=base, fontSize=9.4, leading=12.7, leftIndent=12, firstLineIndent=-8)
    evidence = ParagraphStyle("evidence", parent=base, fontSize=9.25, leading=12.45)

    y = draw_header(canvas, data)
    y = section(canvas, str(data["summary_heading"]), y)
    y = paragraph(escape(str(data["summary"])), base, canvas, y)

    y = section(canvas, str(data["skills_heading"]), y)
    for item in data["skills"]:  # type: ignore[index]
        y = paragraph(str(item), skill, canvas, y)
        y -= 3

    y = section(canvas, str(data["experience_heading"]), y)
    canvas.setFont("ResumeSans-Bold", 9.7)
    canvas.setFillColor(INK)
    canvas.drawString(LEFT, y, str(data["vesper_org"]))
    canvas.setFont("ResumeSans", 8.8)
    date_w = text_width(str(data["vesper_date"]), "ResumeSans", 8.8)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(LEFT + CONTENT_W, y, str(data["vesper_date"]))
    y -= 14
    y = paragraph(escape(str(data["vesper_role"])), role, canvas, y)
    y -= 2
    for item in data["vesper_points"]:  # type: ignore[index]
        y = paragraph("- " + escape(str(item)), bullet, canvas, y)
        y -= 2
    # Keep the next employer visually independent even when the final Vesper
    # item wraps to a second or third line in one language.
    y -= 10
    canvas.setFont("ResumeSans-Bold", 9.7)
    canvas.setFillColor(INK)
    canvas.drawString(LEFT, y, str(data["compasso_org"]))
    canvas.setFont("ResumeSans", 8.8)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(LEFT + CONTENT_W, y, str(data["compasso_date"]))
    y -= 14
    y = paragraph(escape(str(data["compasso_role"])), role, canvas, y)
    y -= 2
    y = paragraph("- " + escape(str(data["compasso_point"])), bullet, canvas, y)

    y = section(canvas, str(data["education_heading"]), y)
    for item in data["education"]:  # type: ignore[index]
        y = paragraph(str(item), evidence, canvas, y)
        y -= 3

    if y < 42:
        raise RuntimeError(f"Content overflowed the page ({out.name} ends at y={y:.1f}).")
    canvas.setFillColor(MUTED)
    canvas.setFont("ResumeSans", 7.4)
    footer = str(data["footer"])
    footer_w = text_width(footer, "ResumeSans", 7.4)
    footer_x = LEFT + CONTENT_W - footer_w
    canvas.drawString(footer_x, 28, footer)
    canvas.linkURL("https://mayconxzdev.github.io/", (footer_x, 26, footer_x + footer_w, 38), relative=0, thickness=0)
    canvas.save()
    return out


def main() -> None:
    register_fonts()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for data in (PT, EN):
        print(generate(data))


if __name__ == "__main__":
    main()
