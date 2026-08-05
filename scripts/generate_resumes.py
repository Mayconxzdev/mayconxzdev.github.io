"""Generate bilingual one-page, ATS-readable resumes for Maycon Ferreira."""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "cv"
PAGE_W, PAGE_H = A4
LEFT = 40
RIGHT = 40
CONTENT_W = PAGE_W - LEFT - RIGHT
INK = HexColor("#111827")
MUTED = HexColor("#475569")
LINE = HexColor("#CBD5E1")
ACCENT = HexColor("#0F4C81")


def _first_existing(paths: list[str]) -> str:
    for path in paths:
        if Path(path).exists():
            return path
    raise FileNotFoundError(f"No supported font found: {paths}")


def register_fonts() -> None:
    normal = _first_existing([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ])
    bold = _first_existing([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
        r"C:\Windows\Fonts\arialbd.ttf",
    ])
    pdfmetrics.registerFont(TTFont("ResumeSans", normal))
    pdfmetrics.registerFont(TTFont("ResumeSans-Bold", bold))
    pdfmetrics.registerFontFamily(
        "ResumeSans", normal="ResumeSans", bold="ResumeSans-Bold",
        italic="ResumeSans", boldItalic="ResumeSans-Bold"
    )


PT = {
    "filename": "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    "title": "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
    "location": "Rio de Janeiro - RJ, Brasil | Remoto, híbrido ou presencial",
    "portfolio_label": "Portfólio",
    "summary_heading": "RESUMO PROFISSIONAL",
    "summary": (
        "Analista de Automação, IA e Integrações com atuação ponta a ponta na transformação de processos internos em "
        "automações e sistemas em uso. Experiência com n8n self-hosted, Python, APIs REST, IA generativa, agentes e SQL, "
        "incluindo mais de 10 mil execuções registradas em workflows n8n e soluções implantadas em 11 computadores e uma TV de fábrica. "
        "Foco em requisitos, confiabilidade, documentação, implantação e sustentação."
    ),
    "skills_heading": "HABILIDADES TÉCNICAS",
    "skills": [
        "<b>Automação e processos:</b> n8n self-hosted, workflows, AS-IS/TO-BE, levantamento de requisitos, regras de negócio, aprovação humana e melhoria contínua.",
        "<b>IA generativa e agentes:</b> OpenAI, Gemini, Ollama e OpenRouter; engenharia de prompts, orquestração multiestágio, saídas estruturadas/JSON Schema, Google Search Grounding, geração e processamento de texto, imagem e vídeo e revisão humana.",
        "<b>Integrações e desenvolvimento:</b> APIs REST, webhooks, HTTP/JSON, OAuth 2.0, Python, JavaScript/TypeScript, FastAPI, SQL/PostgreSQL, SMTP/IMAP e Google Sheets.",
        "<b>Confiabilidade e entrega:</b> Docker, Git/GitHub Actions, filas, retries, idempotência, logs, alertas, backups, testes, auditoria e gestão de segredos.",
    ],
    "experience_heading": "EXPERIÊNCIA PROFISSIONAL",
    "vesper_org": "GRUPO VESPER - VESPER EQUIPAMENTOS EX E VENT RIO EQUIPAMENTOS",
    "vesper_date": "dez. 2025 - presente",
    "vesper_role": "Técnico Júnior em Automação de Processos (cargo formal) | automação, IA aplicada e integrações",
    "vesper_points": [
        "<b>Reduzi o tempo observado de propostas simples de 2-4 minutos para menos de 30 segundos</b> ao desenvolver o Vesper Propostas, com geração ODT/PDF, IMAP/SMTP e revisão humana.",
        "Administro ambiente n8n self-hosted em Windows/Docker com <b>mais de 10 mil execuções registradas</b>; no Mala Direta, a primeira campanha processou <b>mais de 900 destinatários</b> com filas, validação, deduplicação, retries, idempotência e auditoria.",
        "Implantei o Produção Operacional em <b>11 computadores e uma TV de fábrica</b>, com Python, PySide6, SQLite, OCR, cache local e empacotamento para Windows.",
        "Conduzo levantamento com gestão e usuários, mapeamento AS-IS/TO-BE, regras, arquitetura, testes, implantação, treinamento e sustentação de <b>7+ soluções internas</b>; o HelpDesk atende <b>11 usuários</b> de TI e áreas operacionais.",
    ],
    "compasso_org": "COMPASSO TECNOLOGIA LTDA",
    "compasso_date": "out. 2024 - mar. 2025",
    "compasso_role": "Estagiário de TI/Dados",
    "compasso_point": (
        "<b>Reduzi o processamento de uma rotina de aproximadamente 3 horas para cerca de 5 minutos</b> com Python/Pandas; "
        "atuei também com AWS S3/EC2, boto3, Pandas/Polars, SQL, Docker, suporte e documentação."
    ),
    "education_heading": "FORMAÇÃO E CERTIFICAÇÕES",
    "education": [
        "<b>Formação:</b> Tecnólogo em Análise e Desenvolvimento de Sistemas - UNISUAM | conclusão prevista: dez. 2026. Piscine 42 Rio concluída em jul. 2025.",
        "<b>Certificações:</b> Ferramentas de IA: Agentes e Automações - FIRJAN SENAI (2026, 40h); Google AI Essentials - Google/Coursera (2025); Automação de Processos via RPA - ENAP (2025, 25h); Mapeamento e Automação de Processos - ENAP (2025, 20h); LGPD - ENAP (2025, 10h).",
        "<b>Idiomas:</b> inglês técnico para leitura; escrita e conversação básicas.",
    ],
}

EN = {
    "filename": "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
    "title": "AI AUTOMATION & SYSTEMS INTEGRATION ANALYST",
    "location": "Rio de Janeiro - Brazil | Remote, hybrid or on-site",
    "portfolio_label": "Portfolio",
    "summary_heading": "PROFESSIONAL SUMMARY",
    "summary": (
        "AI Automation and Systems Integration Analyst working end to end to turn internal processes into automations and systems used in daily operations. "
        "Experience with self-hosted n8n, Python, REST APIs, generative AI, agents and SQL, including "
        "more than 10,000 recorded n8n workflow executions and solutions deployed across 11 workstations and a factory TV. Focused on "
        "requirements, reliability, documentation, deployment and support."
    ),
    "skills_heading": "TECHNICAL SKILLS",
    "skills": [
        "<b>Automation and processes:</b> self-hosted n8n, workflows, AS-IS/TO-BE, requirements discovery, business rules, human approval and continuous improvement.",
        "<b>Generative AI and agents:</b> OpenAI, Gemini, Ollama and OpenRouter; prompt engineering, multi-stage orchestration, structured outputs/JSON Schema, Google Search Grounding, generation and processing of text, images and video, and human review.",
        "<b>Integrations and development:</b> REST APIs, webhooks, HTTP/JSON, OAuth 2.0, Python, JavaScript/TypeScript, FastAPI, SQL/PostgreSQL, SMTP/IMAP and Google Sheets.",
        "<b>Reliability and delivery:</b> Docker, Git/GitHub Actions, queues, retries, idempotency, logs, alerts, backups, tests, auditing and secrets management.",
    ],
    "experience_heading": "PROFESSIONAL EXPERIENCE",
    "vesper_org": "GRUPO VESPER - VESPER EQUIPAMENTOS EX AND VENT RIO EQUIPAMENTOS",
    "vesper_date": "Dec. 2025 - Present",
    "vesper_role": "Junior Process Automation Technician (formal title) | automation, applied AI and integrations",
    "vesper_points": [
        "<b>Reduced observed processing time for simple proposals from 2-4 minutes to under 30 seconds</b> by developing Vesper Propostas with ODT/PDF generation, IMAP/SMTP and human review.",
        "Administer a self-hosted n8n environment on Windows/Docker with <b>more than 10,000 recorded executions</b>; the first Mala Direta campaign processed <b>more than 900 recipients</b> with queues, validation, deduplication, retries, idempotency and auditing.",
        "Deployed Produção Operacional across <b>11 workstations and a factory TV</b> using Python, PySide6, SQLite, OCR, local caching and Windows packaging.",
        "Lead discovery with management and users, AS-IS/TO-BE process mapping, business rules, architecture, testing, deployment, training and support for <b>7+ internal solutions</b>; HelpDesk serves <b>11 users</b> across IT and operational areas.",
    ],
    "compasso_org": "COMPASSO TECNOLOGIA LTDA",
    "compasso_date": "Oct. 2024 - Mar. 2025",
    "compasso_role": "IT/Data Intern",
    "compasso_point": (
        "<b>Reduced a processing routine from approximately three hours to about five minutes</b> using Python/Pandas; also worked "
        "with AWS S3/EC2, boto3, Pandas/Polars, SQL, Docker, support and documentation."
    ),
    "education_heading": "EDUCATION & CERTIFICATIONS",
    "education": [
        "<b>Education:</b> Associate Degree in Systems Analysis and Development - UNISUAM | expected completion: Dec. 2026. 42 Rio Piscine completed in Jul. 2025.",
        "<b>Certifications:</b> AI Tools: Agents and Automations - FIRJAN SENAI (2026, 40h); Google AI Essentials - Google/Coursera (2025); Process Automation with RPA - ENAP (2025, 25h); Process Mapping and Automation - ENAP (2025, 20h); LGPD - ENAP (2025, 10h).",
        "<b>Languages:</b> technical English for reading; basic writing and conversation.",
    ],
}


def text_width(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def paragraph(canvas: Canvas, y: float, text: str, style: ParagraphStyle, indent: float = 0) -> float:
    item = Paragraph(text, style)
    _, height = item.wrap(CONTENT_W - indent, 1000)
    item.drawOn(canvas, LEFT + indent, y - height)
    return y - height


def section(canvas: Canvas, y: float, title: str) -> float:
    y -= 10
    canvas.setFillColor(ACCENT)
    canvas.rect(LEFT, y - 2, 3.5, 12, fill=1, stroke=0)
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 10.0)
    canvas.drawString(LEFT + 9, y, title)
    y -= 5
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.55)
    canvas.line(LEFT, y, LEFT + CONTENT_W, y)
    return y - 10


def link_row(canvas: Canvas, y: float, items: list[tuple[str, str]], size: float = 8.55) -> float:
    x = LEFT
    canvas.setFont("ResumeSans", size)
    for label, url in items:
        label = label + "  "
        width = text_width(label, "ResumeSans", size)
        if x != LEFT and x + width > LEFT + CONTENT_W:
            x = LEFT
            y -= 12
        canvas.setFillColor(MUTED)
        canvas.drawString(x, y, label)
        canvas.linkURL(url, (x, y - 2, x + width, y + size + 2), relative=0, thickness=0)
        x += width + 8
    return y - 12


def draw_header(canvas: Canvas, data: dict[str, object]) -> float:
    y = PAGE_H - 34
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H - 6, PAGE_W, 6, fill=1, stroke=0)
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 18.0)
    canvas.drawString(LEFT, y, "MAYCON FERREIRA")
    y -= 15
    canvas.setFillColor(ACCENT)
    canvas.setFont("ResumeSans-Bold", 10.3)
    canvas.drawString(LEFT, y, str(data["title"]))
    y -= 14
    canvas.setFillColor(MUTED)
    canvas.setFont("ResumeSans", 8.7)
    canvas.drawString(LEFT, y, str(data["location"]))
    y -= 12
    y = link_row(canvas, y, [
        ("WhatsApp: +55 (21) 96481-0480", "https://wa.me/5521964810480"),
        ("E-mail: mayconxz00dev@gmail.com", "mailto:mayconxz00dev@gmail.com"),
    ])
    y = link_row(canvas, y, [
        ("LinkedIn: linkedin.com/in/maycon-ferreira-7bb870231/", "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"),
        ("GitHub: github.com/Mayconxzdev", "https://github.com/Mayconxzdev"),
        (f"{data['portfolio_label']}: mayconxzdev.github.io", "https://mayconxzdev.github.io/"),
    ])
    canvas.setStrokeColor(LINE)
    canvas.line(LEFT, y + 2, LEFT + CONTENT_W, y + 2)
    return y - 2


def generate(data: dict[str, object]) -> Path:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    out = OUTPUT / str(data["filename"])
    canvas = Canvas(str(out), pagesize=A4, pageCompression=1, invariant=1)
    canvas.setTitle(f"Maycon Ferreira - {data['title']}")
    canvas.setAuthor("Maycon Ferreira")
    canvas.setSubject("ATS-ready one-page resume for automation, applied AI and systems integration roles")
    canvas.setKeywords("automation, n8n, applied AI, generative AI, agents, process mapping, systems integration, APIs, Python, SQL, Docker")
    canvas.setCreator("Maycon Ferreira")

    base = ParagraphStyle("base", fontName="ResumeSans", fontSize=10.0, leading=12.9, textColor=INK)
    skill = ParagraphStyle("skill", parent=base, fontSize=9.75, leading=12.45)
    role = ParagraphStyle("role", parent=base, fontSize=9.65, leading=12.25, textColor=MUTED)
    bullet = ParagraphStyle("bullet", parent=base, fontSize=9.65, leading=12.35, leftIndent=11, firstLineIndent=-8)
    small = ParagraphStyle("small", parent=base, fontSize=9.35, leading=11.95)

    y = draw_header(canvas, data)
    y = section(canvas, y, str(data["summary_heading"]))
    y = paragraph(canvas, y, escape(str(data["summary"])), base)

    y = section(canvas, y, str(data["skills_heading"]))
    for item in data["skills"]:  # type: ignore[index]
        y = paragraph(canvas, y, str(item), skill)
        y -= 1.2

    y = section(canvas, y, str(data["experience_heading"]))
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 9.55)
    canvas.drawString(LEFT, y, str(data["vesper_org"]))
    canvas.setFillColor(MUTED)
    canvas.setFont("ResumeSans", 8.55)
    canvas.drawRightString(LEFT + CONTENT_W, y, str(data["vesper_date"]))
    y -= 12
    y = paragraph(canvas, y, escape(str(data["vesper_role"])), role)
    for point in data["vesper_points"]:  # type: ignore[index]
        y -= 0.8
        y = paragraph(canvas, y, "- " + str(point), bullet)

    y -= 6
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 9.55)
    canvas.drawString(LEFT, y, str(data["compasso_org"]))
    canvas.setFillColor(MUTED)
    canvas.setFont("ResumeSans", 8.55)
    canvas.drawRightString(LEFT + CONTENT_W, y, str(data["compasso_date"]))
    y -= 12
    y = paragraph(canvas, y, escape(str(data["compasso_role"])), role)
    y = paragraph(canvas, y - 1, "- " + str(data["compasso_point"]), bullet)

    y = section(canvas, y, str(data["education_heading"]))
    for item in data["education"]:  # type: ignore[index]
        y = paragraph(canvas, y, str(item), small)
        y -= 1.0

    if y < 23:
        raise RuntimeError(f"Content overflowed page: {out.name}, y={y:.1f}")
    canvas.save()
    return out


def main() -> None:
    register_fonts()
    for dataset in (PT, EN):
        print(generate(dataset))


if __name__ == "__main__":
    main()
