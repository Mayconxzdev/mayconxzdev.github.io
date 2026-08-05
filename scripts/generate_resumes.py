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
OUT = ROOT / "assets" / "cv"
PAGE_W, PAGE_H = A4
LEFT = 44
RIGHT = 44
CONTENT_W = PAGE_W - LEFT - RIGHT

INK = HexColor("#111827")
MUTED = HexColor("#475569")
LINE = HexColor("#CBD5E1")
ACCENT = HexColor("#0F4C81")

FONT_CANDIDATES = [
    (Path(r"C:\Windows\Fonts\arial.ttf"), Path(r"C:\Windows\Fonts\arialbd.ttf")),
    (Path("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"), Path("/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf")),
    (Path("/usr/share/fonts/truetype/lato/Lato-Regular.ttf"), Path("/usr/share/fonts/truetype/lato/Lato-Bold.ttf")),
]


def register_fonts() -> None:
    for regular, bold in FONT_CANDIDATES:
        if regular.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont("ResumeSans", str(regular)))
            pdfmetrics.registerFont(TTFont("ResumeSans-Bold", str(bold)))
            pdfmetrics.registerFontFamily("ResumeSans", normal="ResumeSans", bold="ResumeSans-Bold")
            return
    raise FileNotFoundError("No supported resume font found")


PT = {
    "filename": "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    "title": "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
    "location": "Rio de Janeiro - RJ | remoto, híbrido ou presencial",
    "portfolio_label": "Portfólio",
    "summary_heading": "RESUMO PROFISSIONAL",
    "summary": (
        "Analista de Automação, IA e Integrações com atuação ponta a ponta na transformação de processos internos em "
        "automações e sistemas em uso. Experiência com n8n self-hosted, Python, APIs REST, IA generativa, agentes e bancos "
        "de dados, incluindo mais de 10 mil execuções em produção. Foco em confiabilidade, documentação, monitoramento e sustentação."
    ),
    "skills_heading": "HABILIDADES TÉCNICAS",
    "skills": [
        "<b>Automação e processos:</b> n8n self-hosted, workflows, AS-IS/TO-BE, levantamento de requisitos, regras de negócio, aprovação humana e melhoria contínua.",
        "<b>IA generativa e agentes de IA:</b> OpenAI, Gemini e Ollama/OpenRouter; APIs de LLM, engenharia de prompts, RAG/grounding, JSON Schema, pipelines multiestágio, IA multimodal, text-to-video, fallback, auditoria e revisão humana.",
        "<b>Integração de sistemas e ferramentas:</b> APIs REST, webhooks, HTTP/JSON, OAuth 2.0, SMTP/IMAP, Meta Graph API, Evolution API/WPPConnect e Google Sheets.",
        "<b>Engenharia e confiabilidade:</b> Python, JavaScript/TypeScript, Node.js, FastAPI/Flask, SQL, PostgreSQL/SQLite, Docker, Git/GitHub Actions, CI/CD, testes, logs, retries, idempotência, backups e gestão de segredos.",
    ],
    "experience_heading": "EXPERIÊNCIA PROFISSIONAL",
    "vesper_org": "GRUPO VESPER - VESPER EQUIPAMENTOS EX E VENT RIO EQUIPAMENTOS",
    "vesper_date": "12/2025 - presente",
    "vesper_role": "Técnico Júnior em Automação de Processos (cargo formal) | atuação em automação, IA aplicada e integrações",
    "vesper_points": [
        "Administro ambiente n8n self-hosted em Windows/Docker com mais de 10 mil execuções em produção, integrando APIs, webhooks, PostgreSQL, SMTP e ferramentas internas com logs, retries, alertas, backups e auditoria.",
        "Desenvolvi o Vesper Propostas com geração ODT/PDF, IMAP/SMTP e revisão humana; propostas simples passaram de aproximadamente 2-4 minutos para menos de 30 segundos, em uso diário por 4 profissionais.",
        "Implantei o Produção Operacional em 11 computadores e uma TV de fábrica e o HelpDesk para 11 usuários; também entreguei soluções para compras, catálogo, comunicação e publicação multicanal.",
        "Conduzo levantamento com gestão e usuários, mapeamento AS-IS/TO-BE, arquitetura, testes, implantação, treinamento, monitoramento e sustentação.",
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
        '<b>Mala Direta:</b> automação n8n em produção com 158 nós, 9 Data Tables, fila por destinatário, deduplicação, SMTP, cancelamento revalidado e campanha com mais de 900 destinatários.',
        '<b>Postagem Redes:</b> três workflows n8n e 58 nós, integração com Meta Graph API e cadeia OpenAI - Gemini - Ollama com aprovação humana, idempotência e resultado independente por rede.',
    ],
    "education_heading": "FORMAÇÃO",
    "education": [
        "<b>Tecnólogo em Análise e Desenvolvimento de Sistemas - UNISUAM</b> | conclusão prevista: dez. 2026",
        "Piscine 42 Rio | programa intensivo concluído em jul. 2025",
    ],
    "certs_heading": "CERTIFICAÇÕES",
    "certs": (
        "Ferramentas de IA: Agentes e Automações - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; "
        "Automação de Processos através da RPA - ENAP (25h); Fundamentos da Transformação Digital: Mapeamento e Automação de Processos - ENAP (20h); Introdução à LGPD - ENAP (10h)."
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
        "AI Automation and Integrations Analyst working end to end to turn internal processes into production automations and systems. "
        "Experience with self-hosted n8n, Python, REST APIs, generative AI, agents and databases, including more than 10,000 "
        "production executions. Focused on reliability, documentation, monitoring and support."
    ),
    "skills_heading": "TECHNICAL SKILLS",
    "skills": [
        "<b>Automation and processes:</b> self-hosted n8n, workflows, AS-IS/TO-BE, requirements discovery, business rules, human approval and continuous improvement.",
        "<b>Generative AI and AI agents:</b> OpenAI, Gemini and Ollama/OpenRouter; LLM APIs, prompt engineering, RAG/grounding, JSON Schema, multi-stage pipelines, multimodal AI, text-to-video, fallback, auditing and human review.",
        "<b>Systems and tools integration:</b> REST APIs, webhooks, HTTP/JSON, OAuth 2.0, SMTP/IMAP, Meta Graph API, Evolution API/WPPConnect and Google Sheets.",
        "<b>Engineering and reliability:</b> Python, JavaScript/TypeScript, Node.js, FastAPI/Flask, SQL, PostgreSQL/SQLite, Docker, Git/GitHub Actions, CI/CD, tests, logs, retries, idempotency, backups and secrets management.",
    ],
    "experience_heading": "PROFESSIONAL EXPERIENCE",
    "vesper_org": "GRUPO VESPER - VESPER EQUIPAMENTOS EX AND VENT RIO EQUIPAMENTOS",
    "vesper_date": "12/2025 - Present",
    "vesper_role": "Junior Process Automation Technician (formal title) | automation, applied AI and integrations",
    "vesper_points": [
        "Administer a self-hosted n8n environment on Windows/Docker with more than 10,000 production executions, integrating APIs, webhooks, PostgreSQL, SMTP and internal tools with logs, retries, alerts, backups and auditing.",
        "Developed Vesper Propostas with ODT/PDF generation, IMAP/SMTP and human review; simple proposals went from approximately 2-4 minutes to under 30 seconds, with daily use by 4 professionals.",
        "Deployed Produção Operacional to 11 workstations and a factory TV and HelpDesk to 11 users; also delivered solutions for purchasing, catalog management, communication and multichannel publishing.",
        "Lead discovery with management and users, AS-IS/TO-BE process mapping, architecture, testing, deployment, training, monitoring and support.",
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
        '<b>Mala Direta:</b> production n8n automation with 158 nodes, 9 Data Tables, per-recipient queue, deduplication, SMTP, revalidated cancellation and a campaign with more than 900 recipients.',
        '<b>Postagem Redes:</b> three n8n workflows and 58 nodes, Meta Graph API integration and an OpenAI - Gemini - Ollama chain with human approval, idempotency and independent results per channel.',
    ],
    "education_heading": "EDUCATION",
    "education": [
        "<b>Associate Degree in Systems Analysis and Development - UNISUAM</b> | expected completion: Dec. 2026",
        "42 Rio Piscine | intensive program completed in Jul. 2025",
    ],
    "certs_heading": "CERTIFICATIONS",
    "certs": (
        "AI Tools: Agents and Automations - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; "
        "Process Automation through RPA - ENAP (25h); Digital Transformation Fundamentals: Process Mapping and Automation - ENAP (20h); Introduction to Brazil's Data Protection Law - ENAP (10h)."
    ),
    "language_heading": "LANGUAGES",
    "language": "Technical English for reading; basic writing and conversation.",
}


def paragraph(text: str, style: ParagraphStyle, canvas: Canvas, y: float, indent: float = 0) -> float:
    item = Paragraph(text, style)
    _, height = item.wrap(CONTENT_W - indent, 999)
    item.drawOn(canvas, LEFT + indent, y - height)
    return y - height


def section(canvas: Canvas, title: str, y: float) -> float:
    y -= 9
    canvas.setFillColor(ACCENT)
    canvas.rect(LEFT, y - 2, 4, 12, fill=1, stroke=0)
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 10.2)
    canvas.drawString(LEFT + 10, y, title)
    y -= 5
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.55)
    canvas.line(LEFT, y, LEFT + CONTENT_W, y)
    return y - 9


def text_width(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def link_line(canvas: Canvas, y: float, items: list[tuple[str, str]]) -> float:
    x = LEFT
    size = 8.8
    leading = 13
    canvas.setFont("ResumeSans", size)
    for label, url in items:
        rendered = label + "  "
        width = text_width(rendered, "ResumeSans", size)
        if x != LEFT and x + width > LEFT + CONTENT_W:
            x = LEFT
            y -= leading
        canvas.setFillColor(MUTED)
        canvas.drawString(x, y, rendered)
        canvas.linkURL(url, (x, y - 2, x + width, y + size + 2), relative=0, thickness=0)
        x += width + 11
    return y - leading


def draw_role_header(canvas: Canvas, y: float, organization: str, date: str) -> float:
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 9.3)
    canvas.drawString(LEFT, y, organization)
    canvas.setFillColor(MUTED)
    canvas.setFont("ResumeSans", 8.4)
    canvas.drawRightString(LEFT + CONTENT_W, y, date)
    return y - 13


def generate(data: dict[str, object]) -> Path:
    path = OUT / str(data["filename"])
    canvas = Canvas(str(path), pagesize=A4, pageCompression=1, invariant=1)
    canvas.setTitle(f"Maycon Ferreira - {data['title']}")
    canvas.setAuthor("Maycon Ferreira")
    canvas.setSubject("One-page resume for process automation, AI agents, generative AI and systems integration roles")
    canvas.setKeywords(
        "automation, process automation, process mapping, AS-IS, TO-BE, n8n, generative AI, AI agents, prompt engineering, "
        "RAG, multimodal AI, text-to-video, systems integration, REST APIs, webhooks, Python, JavaScript, TypeScript, SQL, Docker"
    )
    canvas.setCreator("Maycon Ferreira")

    base = ParagraphStyle("base", fontName="ResumeSans", fontSize=10.2, leading=13.15, textColor=INK)
    skill = ParagraphStyle("skill", parent=base, fontSize=10.0, leading=12.55)
    role = ParagraphStyle("role", parent=base, fontSize=10.0, leading=12.25, textColor=MUTED)
    bullet = ParagraphStyle("bullet", parent=base, fontSize=10.0, leading=12.35, leftIndent=12, firstLineIndent=-8)
    compact = ParagraphStyle("compact", parent=base, fontSize=10.0, leading=12.3)

    y = PAGE_H - 37
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H - 7, PAGE_W, 7, fill=1, stroke=0)
    canvas.setFillColor(INK)
    canvas.setFont("ResumeSans-Bold", 19)
    canvas.drawString(LEFT, y, "MAYCON FERREIRA")
    y -= 17
    canvas.setFillColor(ACCENT)
    canvas.setFont("ResumeSans-Bold", 10.7)
    canvas.drawString(LEFT, y, str(data["title"]))
    y -= 15
    canvas.setFillColor(MUTED)
    canvas.setFont("ResumeSans", 9.1)
    canvas.drawString(LEFT, y, str(data["location"]))
    y -= 13
    y = link_line(
        canvas,
        y,
        [
            ("WhatsApp: +55 (21) 96481-0480", "https://wa.me/5521964810480"),
            ("E-mail: mayconxz00dev@gmail.com", "mailto:mayconxz00dev@gmail.com"),
        ],
    )
    y = link_line(
        canvas,
        y,
        [
            ("LinkedIn: linkedin.com/in/maycon-ferreira-7bb870231/", "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"),
            ("GitHub: github.com/Mayconxzdev", "https://github.com/Mayconxzdev"),
            (f"{data['portfolio_label']}: mayconxzdev.github.io", "https://mayconxzdev.github.io/"),
        ],
    )
    canvas.setStrokeColor(LINE)
    canvas.line(LEFT, y - 2, LEFT + CONTENT_W, y - 2)
    y -= 8

    y = section(canvas, str(data["summary_heading"]), y)
    y = paragraph(escape(str(data["summary"])), base, canvas, y)

    y = section(canvas, str(data["skills_heading"]), y)
    for item in data["skills"]:  # type: ignore[index]
        y = paragraph(str(item), skill, canvas, y)
        y -= 1.5

    y = section(canvas, str(data["experience_heading"]), y)
    y = draw_role_header(canvas, y, str(data["vesper_org"]), str(data["vesper_date"]))
    y = paragraph(escape(str(data["vesper_role"])), role, canvas, y)
    y -= 1
    for item in data["vesper_points"]:  # type: ignore[index]
        y = paragraph("- " + escape(str(item)), bullet, canvas, y)
        y -= 1

    y -= 5
    y = draw_role_header(canvas, y, str(data["compasso_org"]), str(data["compasso_date"]))
    y = paragraph(escape(str(data["compasso_role"])), role, canvas, y)
    y = paragraph("- " + escape(str(data["compasso_point"])), bullet, canvas, y)

    y = section(canvas, str(data["projects_heading"]), y)
    for item in data["projects"]:  # type: ignore[index]
        y = paragraph("- " + str(item), bullet, canvas, y)
        y -= 1

    y = section(canvas, str(data["education_heading"]), y)
    for item in data["education"]:  # type: ignore[index]
        y = paragraph(str(item), compact, canvas, y)
        y -= 1

    y = section(canvas, str(data["certs_heading"]), y)
    y = paragraph(escape(str(data["certs"])), compact, canvas, y)

    y = section(canvas, str(data["language_heading"]), y)
    y = paragraph(escape(str(data["language"])), compact, canvas, y)

    if y < 28:
        raise RuntimeError(f"Content overflowed the page: {path.name} ends at y={y:.1f}")

    canvas.save()
    print(f"generated {path} | final y={y:.1f}")
    return path


def main() -> None:
    register_fonts()
    OUT.mkdir(parents=True, exist_ok=True)
    for data in (PT, EN):
        generate(data)


if __name__ == "__main__":
    main()
