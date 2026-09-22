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
        'name': ParagraphStyle('name', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=19.0, leading=20.5, textColor=BLACK, spaceAfter=1.5 * mm),
        'title': ParagraphStyle('title', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=11.0, leading=12.6, textColor=BLACK, spaceAfter=1.2 * mm),
        'contact': ParagraphStyle('contact', parent=base['Normal'], fontName='Helvetica', fontSize=10.0, leading=11.8, textColor=GRAY, spaceAfter=2.4 * mm),
        'section': ParagraphStyle('section', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=10.2, leading=11.8, textColor=BLACK, spaceBefore=3.1 * mm, spaceAfter=1.65 * mm),
        'body': ParagraphStyle('body', parent=base['Normal'], fontName='Helvetica', fontSize=10.1, leading=12.35, textColor=BLACK, spaceAfter=1.0 * mm),
        'small': ParagraphStyle('small', parent=base['Normal'], fontName='Helvetica', fontSize=10.1, leading=12.35, textColor=BLACK, spaceAfter=0.65 * mm),
        'role': ParagraphStyle('role', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=10.15, leading=12.45, textColor=BLACK, spaceAfter=0.5 * mm),
        'meta': ParagraphStyle('meta', parent=base['Normal'], fontName='Helvetica', fontSize=10.0, leading=11.6, textColor=GRAY, spaceAfter=0.7 * mm),
    }


def line(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.45)
    canvas.line(doc.leftMargin, A4[1] - 18.5 * mm, A4[0] - doc.rightMargin, A4[1] - 18.5 * mm)
    canvas.restoreState()


def bullet(text, style):
    return Paragraph('• ' + text, style)


def pt_common():
    return {
        'contact': CONTACT_PT,
        'sections': ['RESUMO PROFISSIONAL', 'EXPERIÊNCIA PROFISSIONAL', 'PROJETOS SELECIONADOS', 'COMPETÊNCIAS TÉCNICAS', 'FORMAÇÃO', 'CREDENCIAIS SELECIONADAS', 'IDIOMAS'],
        'vesper_role': 'GRUPO VESPER — Técnico Júnior em Automação de Processos | dez. 2025 – atual',
        'vesper_meta': 'Vesper Equipamentos EX / Vent Rio · atuação interna em automação, sistemas, dados/BI e IA',
        'vesper_bullets': [
            '<b>Automação:</b> administro n8n self-hosted com 10 mil+ execuções em produção e desenvolvo fluxos com n8n/Power Automate, Python, APIs/webhooks, PostgreSQL e tratamento de erros.',
            '<b>Impacto operacional:</b> desenvolvi e sustento Proposta Comercial (ODT/PDF + IMAP/SMTP), reduzindo propostas simples de 2–4 min para &lt;30 s; implantei Produção Operacional em 10+ PCs e 1 TV para 20+ profissionais em 9 setores.',
            '<b>Engenharia:</b> co-desenvolvo o Belarc Inventory, em uso interno, com agente Windows em Rust/Tokio, servidor Axum/SQLite e coleta PowerShell/CIM.',
            '<b>Dados e processos:</b> crio dashboards Power BI/Excel/Power Query para produção, compras e estoque e atuo em requisitos, BPMN/AS-IS/TO-BE, UAT, implantação e treinamento; 30+ pessoas já orientadas.',
        ],
        'freelance_role': 'INSTRUTOR DE INFORMÁTICA (FREELANCER) | out. 2024 – atual',
        'freelance_meta': 'Aulas pagas semanais (~3h) para públicos de diferentes idades e níveis',
        'freelance_bullets': ['Ensino Excel/Google Sheets, Power BI, Power Query, VBA, Pacote Office, Windows e fundamentos de Linux.'],
        'compass_role': 'COMPASS UOL — Estagiário TI/Dados | out. 2024 – mar. 2025',
        'compass_meta': 'Programa de bolsas em Engenharia de Dados · 10 sprints práticas',
        'compass_bullets': ['Desenvolvi pipeline com Python/SQL/Docker/AWS, integrando CSV/API, S3, Lambda, Glue/PySpark, Parquet, Athena e QuickSight em fluxo ETL/Data Lake.'],
        'education': [
            '<b>Tecnólogo em Análise e Desenvolvimento de Sistemas — UNISUAM</b> · conclusão prevista dez. 2026',
            '<b>Piscine 42 Rio</b> · programa intensivo em Linux/C · concluído jul. 2025',
        ],
        'credentials': [
            '<b>Microsoft Applied Skills:</b> Foundry Agents · MCP Tools with Agents · Power Apps; <b>n8n Academy:</b> N8N102 · N8N103; <b>UiPath:</b> Automation Business Analyst Professional Training.'
        ],
        'languages': ['Português nativo · Inglês: leitura técnica intermediária; escrita e conversação básicas'],
    }


def en_common():
    return {
        'contact': CONTACT_EN,
        'sections': ['PROFESSIONAL SUMMARY', 'PROFESSIONAL EXPERIENCE', 'SELECTED PROJECTS', 'TECHNICAL SKILLS', 'EDUCATION', 'SELECTED CREDENTIALS', 'LANGUAGES'],
        'vesper_role': 'GRUPO VESPER — Junior Process Automation Technician | Dec. 2025 – Present',
        'vesper_meta': 'Vesper Equipamentos EX / Vent Rio · internal work across automation, systems, data/BI and AI',
        'vesper_bullets': [
            '<b>Automation:</b> administer self-hosted n8n with 10k+ production executions and build workflows with n8n/Power Automate, Python, APIs/webhooks, PostgreSQL and error handling.',
            '<b>Operational impact:</b> built and support Commercial Proposal (ODT/PDF + IMAP/SMTP), reducing simple proposals from 2–4 min to &lt;30 sec; deployed Production Operations to 10+ PCs and 1 TV for 20+ professionals across 9 areas.',
            '<b>Engineering:</b> co-develop Belarc Inventory, in internal use, with a Rust/Tokio Windows agent, Axum/SQLite server and PowerShell/CIM collection.',
            '<b>Data & process:</b> build Power BI/Excel/Power Query dashboards for production, procurement and inventory and work across requirements, BPMN/AS-IS/TO-BE, UAT, deployment and training; 30+ people guided.',
        ],
        'freelance_role': 'IT INSTRUCTOR (FREELANCE) | Oct. 2024 – Present',
        'freelance_meta': 'Paid weekly classes (~3h) for learners of different ages and skill levels',
        'freelance_bullets': ['Teach Excel/Google Sheets, Power BI, Power Query, VBA, Office, Windows and Linux fundamentals.'],
        'compass_role': 'COMPASS UOL — IT/Data Intern | Oct. 2024 – Mar. 2025',
        'compass_meta': 'Data Engineering scholarship · 10 practical sprints',
        'compass_bullets': ['Built a Python/SQL/Docker/AWS pipeline integrating CSV/API, S3, Lambda, Glue/PySpark, Parquet, Athena and QuickSight in an ETL/Data Lake flow.'],
        'education': [
            '<b>Technology Degree in Systems Analysis and Development — UNISUAM</b> · expected Dec. 2026',
            '<b>42 Rio Piscine</b> · intensive Linux/C program · completed Jul. 2025',
        ],
        'credentials': [
            '<b>Microsoft Applied Skills:</b> Foundry Agents · MCP Tools with Agents · Power Apps; <b>n8n Academy:</b> N8N102 · N8N103; <b>UiPath:</b> Automation Business Analyst Professional Training.'
        ],
        'languages': ['Portuguese: native · English: intermediate technical reading; basic writing and conversation'],
    }


def content(lang='pt', track='general'):
    if lang == 'pt':
        data = pt_common()
        tracks = {
            'general': {
                'filename': 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
                'title': 'ANALISTA DE AUTOMAÇÃO E IA | n8n · Power Automate · Python',
                'summary': (
                    'Analista de Automação e IA com atuação ponta a ponta em n8n, Power Automate, Python/APIs e sistemas internos. '
                    'Administro n8n self-hosted com 10 mil+ execuções em produção e entreguei automações que reduziram processos de 2–4 min para <30 s. '
                    'Experiência com Power BI/Power Query, LLMs/RAG, PostgreSQL/Redis, Docker e engenharia Windows/Rust.'
                ),
                'projects': [
                    '<b>Postagem Redes:</b> n8n + APIs + RAG/LangChain + Prompt Engineering + human-in-the-loop + evals; OAuth2, idempotência e falha isolada por canal.',
                    '<b>Hubora:</b> produto web local-first com React/TypeScript, Supabase/RLS, PWA, IndexedDB, testes E2E e validação de acessibilidade.',
                ],
                'skills': [
                    '<b>Automação e integrações:</b> n8n self-hosted · Power Automate Cloud/Desktop · Python/FastAPI · REST/JSON · Webhooks/OAuth · PostgreSQL/Redis · Docker · Git/GitHub Actions',
                    '<b>IA aplicada:</b> Prompt Engineering · APIs de LLM · agentes · RAG/LangChain · MCP · human-in-the-loop · evals',
                    '<b>Engenharia, dados e BI:</b> Rust/Axum · PowerShell/CIM · Power BI · DAX · Power Query · Excel/VBA · SQL',
                ],
            },
            'ai': {
                'filename': 'Maycon_Ferreira_Automacao_IA_n8n_Python_LLMs.pdf',
                'title': 'ANALISTA DE AUTOMAÇÃO E IA | n8n · Python · LLMs/RAG',
                'summary': (
                    'Analista de Automação e IA com experiência em n8n, Python/APIs e soluções com LLMs/agentes. '
                    'Administro n8n self-hosted com 10 mil+ execuções em produção e desenvolvo integrações com Prompt Engineering, RAG/LangChain, MCP, evals e revisão humana. '
                    'Também atuo com PostgreSQL/Redis, Docker e sustentação ponta a ponta.'
                ),
                'projects': [
                    '<b>HelpDesk & IT Operations:</b> sistema interno usado por 11 pessoas; agente operacional cruza contexto de estação, inventário, chamados e vencimentos para enriquecer alertas e diagnóstico.',
                    '<b>Postagem Redes:</b> n8n + Meta Graph API + RAG/LangChain + Prompt Engineering + human-in-the-loop + evals; Facebook/Instagram validados em ambiente de teste.',
                ],
                'skills': [
                    '<b>IA aplicada:</b> Prompt Engineering · APIs de LLM · agentes · RAG/LangChain · MCP · human-in-the-loop · evals · Supabase/Qdrant',
                    '<b>Automação e backend:</b> n8n self-hosted · Python/FastAPI · REST/Webhooks/OAuth · WhatsApp Cloud API · PostgreSQL/Redis · Docker',
                    '<b>Dados e BI:</b> SQL · Power BI · Power Query · Excel/Google Sheets',
                ],
            },
            'bi': {
                'filename': 'Maycon_Ferreira_Automacao_BI_Power_Automate_Power_BI.pdf',
                'title': 'ANALISTA DE AUTOMAÇÃO E BI | Power Automate · Power BI · Python',
                'summary': (
                    'Analista de Automação e BI com atuação em Power Automate, Python/APIs, Power BI/Power Query e melhoria de processos. '
                    'Administro automações em produção, crio dashboards e análises para produção, compras e estoque e entreguei fluxos que reduziram processos de 2–4 min para <30 s. '
                    'Experiência com SQL/PostgreSQL, ETL, Excel/VBA, requisitos e sustentação.'
                ),
                'projects': [
                    '<b>Catálogo Operacional:</b> busca e controle de dados para 24 categorias e 480+ códigos, com uso diário, histórico, integridade e revisão otimista.',
                    '<b>ComprasVesper:</b> aplicação interna de compras/cotações com Python/PySide6, SQLite WAL, IMAP/SMTP, fila persistente, backoff, idempotência e tracking.',
                ],
                'skills': [
                    '<b>Automação e BI:</b> Power Automate Cloud/Desktop · Power BI · DAX · Power Query · Python · Excel/Google Sheets · VBA · SQL',
                    '<b>Integrações e dados:</b> REST/Webhooks/OAuth · PostgreSQL · MySQL · Redis · ETL/Data Lake · Docker',
                    '<b>Processos:</b> requisitos · BPMN/AS-IS/TO-BE · testes/UAT · implantação · treinamento · sustentação',
                ],
            },
        }
        data.update(tracks[track])
        return data

    data = en_common()
    data.update({
        'filename': 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
        'title': 'AUTOMATION & AI ANALYST | n8n · Power Automate · Python',
        'summary': (
            'Automation & AI Analyst working end to end across n8n, Power Automate, Python/APIs and internal systems. '
            'I administer self-hosted n8n with 10k+ production executions and delivered automations that reduced processes from 2–4 min to <30 sec. '
            'Hands-on with Power BI/Power Query, LLMs/RAG, PostgreSQL/Redis, Docker and Windows/Rust engineering.'
        ),
        'projects': [
            '<b>Postagem Redes:</b> n8n + APIs + RAG/LangChain + Prompt Engineering + human-in-the-loop + evals, with OAuth2, idempotency and channel-isolated failures.',
            '<b>Hubora:</b> local-first web product with React/TypeScript, Supabase/RLS, PWA, IndexedDB, E2E tests and accessibility validation.',
        ],
        'skills': [
            '<b>Automation & integrations:</b> self-hosted n8n · Power Automate Cloud/Desktop · Python/FastAPI · REST/JSON · Webhooks/OAuth · PostgreSQL/Redis · Docker · Git/GitHub Actions',
            '<b>Applied AI:</b> Prompt Engineering · LLM APIs · agents · RAG/LangChain · MCP · human-in-the-loop · evals',
            '<b>Engineering, data & BI:</b> Rust/Axum · PowerShell/CIM · Power BI · DAX · Power Query · Excel/VBA · SQL',
        ],
    })
    return data


def build(lang='pt', track='general'):
    data = content(lang, track)
    s = styles()
    path = OUT / data['filename']
    name = 'MAYCON FERREIRA'
    doc = SimpleDocTemplate(
        str(path), pagesize=A4,
        leftMargin=12 * mm, rightMargin=12 * mm,
        topMargin=10.5 * mm, bottomMargin=10.5 * mm,
        title=name + ' - ' + data['title'],
        author='Maycon Ferreira',
        subject='One-page resume focused on automation, applied AI, integrations and production-ready internal systems',
    )
    story = [Paragraph(name, s['name']), Paragraph(data['title'], s['title']), Paragraph(data['contact'], s['contact'])]

    def section(label):
        story.append(Paragraph(label, s['section']))

    section(data['sections'][0])
    story.append(Paragraph(data['summary'], s['body']))
    section(data['sections'][1])
    story.extend([Paragraph(data['vesper_role'], s['role']), Paragraph(data['vesper_meta'], s['meta'])])
    for item in data['vesper_bullets']:
        story.append(bullet(item, s['small']))
    story.extend([Spacer(1, 0.6 * mm), Paragraph(data['freelance_role'], s['role']), Paragraph(data['freelance_meta'], s['meta'])])
    for item in data['freelance_bullets']:
        story.append(bullet(item, s['small']))
    story.extend([Spacer(1, 0.6 * mm), Paragraph(data['compass_role'], s['role']), Paragraph(data['compass_meta'], s['meta'])])
    for item in data['compass_bullets']:
        story.append(bullet(item, s['small']))
    section(data['sections'][2])
    for item in data['projects']:
        story.append(bullet(item, s['small']))
    section(data['sections'][3])
    for item in data['skills']:
        story.append(Paragraph(item, s['small']))
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
    print(build('pt', 'general'))
    print(build('pt', 'ai'))
    print(build('pt', 'bi'))
    print(build('en', 'general'))
