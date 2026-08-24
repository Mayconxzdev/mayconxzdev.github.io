from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'cv'
OUT.mkdir(parents=True, exist_ok=True)

BLACK = colors.HexColor('#111111')
GRAY = colors.HexColor('#555555')
LIGHT = colors.HexColor('#D9D9D9')

CONTACT_PT = (
    'Rio de Janeiro - RJ · '
    '<link href="tel:+5521964810480" color="#555555">+55 (21) 96481-0480</link> · '
    '<link href="mailto:mayconxz00dev@gmail.com" color="#555555">mayconxz00dev@gmail.com</link><br/>'
    '<link href="https://www.linkedin.com/in/maycon-ferreira-7bb870231/" color="#555555">linkedin.com/in/maycon-ferreira-7bb870231</link> · '
    '<link href="https://github.com/Mayconxzdev" color="#555555">github.com/Mayconxzdev</link> · '
    '<link href="https://mayconxzdev.github.io/" color="#555555">mayconxzdev.github.io</link>'
)
CONTACT_EN = (
    'Rio de Janeiro, Brazil · '
    '<link href="tel:+5521964810480" color="#555555">+55 (21) 96481-0480</link> · '
    '<link href="mailto:mayconxz00dev@gmail.com" color="#555555">mayconxz00dev@gmail.com</link><br/>'
    '<link href="https://www.linkedin.com/in/maycon-ferreira-7bb870231/" color="#555555">linkedin.com/in/maycon-ferreira-7bb870231</link> · '
    '<link href="https://github.com/Mayconxzdev" color="#555555">github.com/Mayconxzdev</link> · '
    '<link href="https://mayconxzdev.github.io/" color="#555555">mayconxzdev.github.io</link>'
)


def styles():
    base = getSampleStyleSheet()
    return {
        'name': ParagraphStyle('name', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=19.0, leading=20.5, textColor=BLACK, spaceAfter=1.6 * mm),
        'title': ParagraphStyle('title', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=11.0, leading=12.6, textColor=BLACK, spaceAfter=1.3 * mm),
        'contact': ParagraphStyle('contact', parent=base['Normal'], fontName='Helvetica', fontSize=8.9, leading=11.3, textColor=GRAY, spaceAfter=2.8 * mm),
        'section': ParagraphStyle('section', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=9.8, leading=11.2, textColor=BLACK, spaceBefore=3.15 * mm, spaceAfter=1.8 * mm),
        'body': ParagraphStyle('body', parent=base['Normal'], fontName='Helvetica', fontSize=9.8, leading=12.0, textColor=BLACK, spaceAfter=1.2 * mm),
        'small': ParagraphStyle('small', parent=base['Normal'], fontName='Helvetica', fontSize=9.5, leading=11.9, textColor=BLACK, spaceAfter=0.8 * mm),
        'role': ParagraphStyle('role', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=9.7, leading=11.5, textColor=BLACK, spaceAfter=0.6 * mm),
        'meta': ParagraphStyle('meta', parent=base['Normal'], fontName='Helvetica', fontSize=8.9, leading=10.8, textColor=GRAY, spaceAfter=0.8 * mm),
    }


def line(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.45)
    canvas.line(doc.leftMargin, A4[1] - 18.5 * mm, A4[0] - doc.rightMargin, A4[1] - 18.5 * mm)
    canvas.restoreState()


def bullet(text, style):
    return Paragraph('• ' + text, style)


def content(lang):
    if lang == 'pt':
        return {
            'filename': 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
            'title': 'ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES',
            'contact': CONTACT_PT,
            'sections': ['RESUMO PROFISSIONAL', 'COMPETÊNCIAS TÉCNICAS', 'EXPERIÊNCIA PROFISSIONAL', 'PROJETOS SELECIONADOS', 'FORMAÇÃO', 'CREDENCIAIS SELECIONADAS', 'IDIOMAS'],
            'summary': (
                'Analista de Automação, IA e Integrações com atuação ponta a ponta em automação de processos, integrações, APIs e sistemas internos. '
                'Administro ambiente n8n self-hosted com 10 mil+ execuções de workflows em produção e transformo necessidades operacionais em soluções com '
                'Python, FastAPI, APIs REST, SQL/PostgreSQL e IA aplicada, do mapeamento BPMN/AS-IS/TO-BE e requisitos à implantação, monitoramento, treinamento e sustentação.'
            ),
            'skills': [
                '<b>Automação, integrações e backend:</b> n8n self-hosted · low-code/no-code · Python · FastAPI · APIs REST · JSON · webhooks · OAuth 2.0 · SQL · PostgreSQL · Docker · contexto: Power Platform (Power Apps/Power Automate) · Make · Zapier',
                '<b>Processos e entrega:</b> BPMN · AS-IS/TO-BE · levantamento de requisitos · stakeholders · regras de negócio · documentação · testes · UAT/homologação · métricas de impacto · implantação · treinamento · sustentação/melhoria contínua',
                '<b>IA aplicada e engenharia:</b> IA generativa/LLMs · APIs de LLM · agentes de IA · RAG/grounding · LangChain · human-in-the-loop · evals · JavaScript/TypeScript · Git/GitHub Actions · CI/CD · logs · monitoramento/observabilidade · tratamento de erros · retries · idempotência · segurança de integrações · gestão de segredos',
            ],
            'vesper_role': 'GRUPO VESPER — Técnico Júnior em Automação de Processos | dez. 2025 – atual',
            'vesper_meta': 'Vesper Equipamentos EX / Vent Rio · automação, IA aplicada, integrações e sistemas internos',
            'vesper_bullets': [
                '<b>n8n e integrações:</b> administro ambiente self-hosted Windows/Docker com 10 mil+ execuções de workflows em produção, integrando APIs, webhooks, PostgreSQL e SMTP com logs, alertas, retries, backups e auditoria.',
                '<b>Proposta Comercial:</b> desenvolvi e sustento fluxo com ODT/PDF, IMAP/SMTP e revisão humana; propostas simples passaram de 2–4 min para &lt;30 s, com uso diário por 4 profissionais.',
                '<b>Produção e manutenção:</b> implantei a Produção Operacional em 10+ PCs e 1 TV, apoiando 20+ profissionais em 9 setores; também digitalizei a manutenção de 40+ ativos com checklists, evidências e histórico consultável.',
                '<b>Processos e adoção:</b> conduzo requisitos, AS-IS/TO-BE/BPMN, testes/UAT, implantação e treinamento com usuários e gestão; já treinei/orientei 30+ pessoas e mantenho HelpDesk em uso por 11 usuários.',
            ],
            'compass_role': 'COMPASS UOL — Estagiário TI/Dados | out. 2024 – mar. 2025',
            'compass_meta': 'Programa de bolsas em Engenharia de Dados · 10 sprints práticas',
            'compass_bullets': ['Construí pipeline em Python/SQL/Docker/AWS: CSV/TMDB API → S3 → Lambda/boto3 → Glue/PySpark → Parquet Raw/Trusted/Refined → Athena → QuickSight; pratiquei Linux, Git, ETL/Data Lake e modelagem.'],
            'projects': [
                '<b>Mala Direta:</b> 6 campanhas sobre base de 1.020 contatos, uma com 900+ destinatários; 2 workflows n8n com fila, deduplicação, cancelamento revalidado, retry e auditoria.',
                '<b>CarreiraPessoal:</b> produto Windows com FastAPI, React/TypeScript e Tauri/Rust; v12.5.2 com 283 testes Python, 102 famílias ATS e 11 coletores diretos.',
                '<b>Catálogo Operacional de Compras:</b> FastAPI + SQLite FTS5; 24 categorias, 480+ códigos, controle de revisão, histórico/backups e uso diário por 3 pessoas.',
                '<b>Postagem Redes:</b> n8n + Meta Graph API + RAG/LangChain + human-in-the-loop + evals; Facebook/Instagram exercitados em teste, com idempotência e isolamento de falhas.',
            ],
            'education': [
                '<b>Tecnólogo em Análise e Desenvolvimento de Sistemas — UNISUAM</b> · conclusão prevista dez. 2026',
                '<b>Piscine 42 Rio</b> · programa intensivo em Linux/C · concluído jul. 2025',
            ],
            'credentials': [
                '<b>Microsoft Applied Skills (3):</b> Microsoft Foundry agents · MCP tools with agents · Canvas Apps with Power Apps; '
                '<b>UiPath Academy:</b> Automation Business Analyst Professional Training; '
                '<b>n8n Academy:</b> N8N102 · N8N103; <b>Make Academy:</b> AI Agent Builder.'
            ],
            'languages': ['Português nativo · Inglês: leitura técnica independente; escrita e conversação básicas'],
        }

    return {
        'filename': 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
        'title': 'AUTOMATION, AI & INTEGRATIONS ANALYST',
        'contact': CONTACT_EN,
        'sections': ['PROFESSIONAL SUMMARY', 'TECHNICAL SKILLS', 'PROFESSIONAL EXPERIENCE', 'SELECTED PROJECTS', 'EDUCATION', 'SELECTED CREDENTIALS', 'LANGUAGES'],
        'summary': (
            'Automation, AI & Integrations Analyst working end to end across process automation, integrations, APIs and internal systems. '
            'I administer a self-hosted n8n environment with 10k+ production workflow executions and turn operational needs into solutions with '
            'Python, FastAPI, REST APIs, SQL/PostgreSQL and applied AI, from BPMN/AS-IS/TO-BE mapping and requirements through deployment, monitoring, training and production support.'
        ),
        'skills': [
            '<b>Automation, integrations & backend:</b> self-hosted n8n · low-code/no-code · Python · FastAPI · REST APIs · JSON · webhooks · OAuth 2.0 · SQL · PostgreSQL · Docker · contextual: Power Platform (Power Apps/Power Automate) · Make · Zapier',
            '<b>Process & delivery:</b> BPMN · AS-IS/TO-BE · requirements discovery · stakeholders · business rules · documentation · testing · UAT · impact metrics · deployment · training · production support/continuous improvement',
            '<b>Applied AI & engineering:</b> generative AI/LLMs · LLM APIs · AI agents · RAG/grounding · LangChain · human-in-the-loop · evals · JavaScript/TypeScript · Git/GitHub Actions · CI/CD · logs · monitoring/observability · error handling · retries · idempotency · integration security · secrets management',
        ],
        'vesper_role': 'GRUPO VESPER — Junior Process Automation Technician | Dec. 2025 – Present',
        'vesper_meta': 'Vesper Equipamentos EX / Vent Rio · automation, applied AI, integrations and internal systems',
        'vesper_bullets': [
            '<b>n8n & integrations:</b> administer a self-hosted Windows/Docker environment with 10k+ production workflow executions, integrating APIs, webhooks, PostgreSQL and SMTP with logs, alerts, retries, backups and auditability.',
            '<b>Commercial Proposals:</b> built and support an ODT/PDF + IMAP/SMTP workflow with human review; simple proposals went from 2–4 min to &lt;30 sec and are used daily by 4 professionals.',
            '<b>Production & maintenance:</b> deployed Production Operations to 10+ PCs and 1 TV supporting 20+ professionals across 9 sectors; also digitized maintenance for 40+ assets with checklists, evidence and searchable history.',
            '<b>Process & adoption:</b> lead requirements discovery, AS-IS/TO-BE/BPMN, testing/UAT, deployment and training with users and management; trained/guided 30+ people and maintain a HelpDesk used by 11 users.',
        ],
        'compass_role': 'COMPASS UOL — IT/Data Intern | Oct. 2024 – Mar. 2025',
        'compass_meta': 'Data Engineering scholarship · 10 practical sprints',
        'compass_bullets': ['Built a Python/SQL/Docker/AWS pipeline: CSV/TMDB API → S3 → Lambda/boto3 → Glue/PySpark → Raw/Trusted/Refined Parquet → Athena → QuickSight; practiced Linux, Git, ETL/Data Lake and data modeling.'],
        'projects': [
            '<b>Mala Direta:</b> 6 campaigns over a 1,020-contact base, one with 900+ recipients; 2 n8n workflows with queues, deduplication, revalidated cancellation, retry and auditing.',
            '<b>CarreiraPessoal:</b> Windows product with FastAPI, React/TypeScript and Tauri/Rust; v12.5.2 with 283 Python tests, 102 ATS role families and 11 direct collectors.',
            '<b>Operational Procurement Catalog:</b> FastAPI + SQLite FTS5; 24 categories, 480+ codes, revision control, history/backups and daily use by 3 people.',
            '<b>Postagem Redes:</b> n8n + Meta Graph API + RAG/LangChain + human-in-the-loop + evals; Facebook/Instagram exercised in testing, with idempotency and per-channel failure isolation.',
        ],
        'education': [
            '<b>Technology Degree in Systems Analysis and Development — UNISUAM</b> · expected Dec. 2026',
            '<b>42 Rio Piscine</b> · intensive Linux/C program · completed Jul. 2025',
        ],
        'credentials': [
            '<b>Microsoft Applied Skills (3):</b> Microsoft Foundry agents · MCP tools with agents · Canvas Apps with Power Apps; '
            '<b>UiPath Academy:</b> Automation Business Analyst Professional Training; '
            '<b>n8n Academy:</b> N8N102 · N8N103; <b>Make Academy:</b> AI Agent Builder.'
        ],
        'languages': ['Portuguese: native · English: independent technical reading; basic writing and conversation'],
    }


def build(lang='pt'):
    data = content(lang)
    s = styles()
    path = OUT / data['filename']
    name = 'MAYCON FERREIRA'
    doc = SimpleDocTemplate(
        str(path), pagesize=A4,
        leftMargin=12 * mm, rightMargin=12 * mm,
        topMargin=10.5 * mm, bottomMargin=10.5 * mm,
        title=name + ' - ' + data['title'],
        author='Maycon Ferreira',
        subject='One-page general resume for automation, applied AI, integrations, internal systems and process roles',
    )
    story = [Paragraph(name, s['name']), Paragraph(data['title'], s['title']), Paragraph(data['contact'], s['contact'])]

    def section(label):
        story.append(Paragraph(label, s['section']))

    section(data['sections'][0])
    story.append(Paragraph(data['summary'], s['body']))
    section(data['sections'][1])
    for item in data['skills']:
        story.append(Paragraph(item, s['small']))
    section(data['sections'][2])
    story.extend([Paragraph(data['vesper_role'], s['role']), Paragraph(data['vesper_meta'], s['meta'])])
    for item in data['vesper_bullets']:
        story.append(bullet(item, s['small']))
    story.extend([Spacer(1, 1.0 * mm), Paragraph(data['compass_role'], s['role']), Paragraph(data['compass_meta'], s['meta'])])
    for item in data['compass_bullets']:
        story.append(bullet(item, s['small']))
    section(data['sections'][3])
    for item in data['projects']:
        story.append(bullet(item, s['small']))
    section(data['sections'][4])
    for item in data['education']:
        story.append(Paragraph(item, s['small']))
    section(data['sections'][5])
    for item in data['credentials']:
        story.append(Paragraph(item, s['small']))
    section(data['sections'][6])
    for item in data['languages']:
        story.append(Paragraph(item, s['small']))

    doc.build(story, onFirstPage=line)
    return path


if __name__ == '__main__':
    print(build('pt'))
    print(build('en'))
