from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'cv'
OUT.mkdir(parents=True, exist_ok=True)

BLACK = colors.HexColor('#111111')
GRAY = colors.HexColor('#555555')
LIGHT = colors.HexColor('#D9D9D9')

CONTACT_PT = 'Rio de Janeiro - RJ · +55 (21) 96481-0480 · mayconxz00dev@gmail.com · linkedin.com/in/maycon-ferreira-7bb870231/ · github.com/Mayconxzdev · mayconxzdev.github.io'
CONTACT_EN = 'Rio de Janeiro, Brazil · +55 (21) 96481-0480 · mayconxz00dev@gmail.com · linkedin.com/in/maycon-ferreira-7bb870231/ · github.com/Mayconxzdev · mayconxzdev.github.io'


def styles():
    base = getSampleStyleSheet()
    return {
        'name': ParagraphStyle('name', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=15.2, leading=16.2, textColor=BLACK, spaceAfter=1.4*mm),
        'title': ParagraphStyle('title', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=9.2, leading=10.3, textColor=BLACK, spaceAfter=1.1*mm),
        'contact': ParagraphStyle('contact', parent=base['Normal'], fontName='Helvetica', fontSize=6.55, leading=7.5, textColor=GRAY, spaceAfter=2.2*mm),
        'section': ParagraphStyle('section', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=8.4, textColor=BLACK, spaceBefore=1.55*mm, spaceAfter=0.8*mm),
        'body': ParagraphStyle('body', parent=base['Normal'], fontName='Helvetica', fontSize=7.05, leading=8.45, textColor=BLACK, spaceAfter=0.65*mm),
        'small': ParagraphStyle('small', parent=base['Normal'], fontName='Helvetica', fontSize=6.75, leading=8.05, textColor=BLACK, spaceAfter=0.45*mm),
        'role': ParagraphStyle('role', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=7.25, leading=8.45, textColor=BLACK, spaceAfter=0.35*mm),
        'meta': ParagraphStyle('meta', parent=base['Normal'], fontName='Helvetica', fontSize=6.7, leading=7.8, textColor=GRAY, spaceAfter=0.55*mm),
    }


def line(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.45)
    canvas.line(doc.leftMargin, A4[1]-18.4*mm, A4[0]-doc.rightMargin, A4[1]-18.4*mm)
    canvas.restoreState()


def bullet(text, st):
    return Paragraph('• ' + text, st)


def build(lang='pt'):
    s = styles()
    if lang == 'pt':
        path = OUT / 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf'
        name = 'MAYCON FERREIRA'
        title = 'ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES'
        contact = CONTACT_PT
        sections = {'summary':'RESUMO PROFISSIONAL','skills':'COMPETÊNCIAS','exp':'EXPERIÊNCIA','projects':'PROJETOS SELECIONADOS','edu':'FORMAÇÃO','courses':'CURSOS E CERTIFICAÇÕES','lang':'IDIOMAS'}
        summary = ('Analista de Automação, IA e Integrações. Transformo processos operacionais em automações e sistemas internos, do levantamento à sustentação. Administro n8n self-hosted com 10 mil+ execuções em produção e trabalho com Python, FastAPI, APIs REST, PostgreSQL, Docker e IA aplicada.')
        skills = [
            '<b>Núcleo:</b> n8n self-hosted · Python · FastAPI · APIs REST/webhooks · JSON/JSON Schema · OAuth 2.0 · SQL/PostgreSQL · Docker',
            '<b>Processos e automação:</b> BPMN · AS-IS/TO-BE · requisitos · regras de negócio · Power Automate · Make/Zapier · CRM · rastreabilidade · documentação',
            '<b>IA aplicada e engenharia:</b> OpenAI · Gemini · Ollama · RAG/LangChain · MCP · LangGraph/CrewAI · human-in-the-loop · JavaScript/TypeScript · Linux · Git/GitHub Actions · testes · monitoramento · logs · retries · idempotência · alertas · backups',
        ]
        vesper_role = 'GRUPO VESPER — Técnico Júnior em Automação de Processos | dez. 2025 – atual'
        vesper_meta = 'Vesper Equipamentos EX / Vent Rio · automação, IA aplicada, integrações e sistemas internos'
        vesper_bullets = [
            '<b>n8n:</b> administro ambiente self-hosted Windows/Docker com 10 mil+ execuções de workflows em produção, integrando APIs, webhooks, PostgreSQL e SMTP com logs, retries, alertas, backups e auditoria.',
            '<b>Proposta Comercial:</b> desenvolvi e sustento o fluxo de propostas com ODT/PDF, IMAP/SMTP e revisão humana; propostas simples passaram de 2–4 min para &lt;30 s, com uso diário por 4 profissionais.',
            '<b>Produção e manutenção:</b> implantei a Produção Operacional em 10+ PCs e 1 TV para 20+ profissionais em 9 setores e digitalizei manutenção de 40+ ativos com checklists, fotos/evidências, histórico e consulta da Qualidade.',
            '<b>Processos e adoção:</b> levanto requisitos e modelo AS-IS/TO-BE/BPMN com usuários, Produção, Qualidade e gestão; conforme o contexto uso n8n, Power Automate, Make/Zapier e CRM. Já treinei/orientei 30+ pessoas.',
        ]
        compass_role = 'COMPASS UOL — Estagiário TI/Dados | out. 2024 – mar. 2025'
        compass_meta = 'Programa de bolsas em Data Engineering · 10 sprints práticas'
        compass_bullets = ['Construí pipeline em Python/SQL/Docker/AWS: ingestão CSV/TMDB API → S3 → Lambda/boto3 → Glue/PySpark → Parquet Raw/Trusted/Refined → Athena → QuickSight; pratiquei Linux, Git, ETL/Data Lake e modelagem.']
        projects = [
            '<b>Mala Direta:</b> 6 campanhas sobre base de 1.020 contatos, uma com 900+; 2 workflows n8n, principal com 158 nós e 9 Data Tables, filas, deduplicação, cancelamento e auditoria.',
            '<b>CarreiraPessoal:</b> produto pessoal Windows (FastAPI + React/TS + Tauri/Rust) para descoberta, deduplicação, Career Goal, evidências e roteamento de currículo; v12.5.2 com 283 testes Python aprovados.',
            '<b>Catálogo Operacional:</b> FastAPI + SQLite FTS5, 24 categorias e 480+ códigos, busca sem depender do código do item, revisão/histórico de preço, backups e uso diário.',
            '<b>Postagem Redes:</b> n8n + Meta Graph + OpenAI/Gemini/Ollama, RAG/grounding com LangChain, revisão humana e idempotência; Facebook/Instagram validados em teste.',
        ]
        edu = ['<b>Análise e Desenvolvimento de Sistemas — UNISUAM</b> · conclusão prevista dez. 2026', '<b>Piscine 42 Rio</b> · programa intensivo em Linux/C · concluído jul. 2025']
        courses = ['FIRJAN SENAI — Agentes de IA e Automações (40h) · Google AI Essentials · ENAP RPA (25h) · ENAP Mapeamento e Automação de Processos (20h)']
        languages = ['Português nativo · Inglês: leitura técnica independente; escrita e conversação básicas']
    else:
        path = OUT / 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf'
        name = 'MAYCON FERREIRA'
        title = 'AI, AUTOMATION & INTEGRATIONS ANALYST'
        contact = CONTACT_EN
        sections = {'summary':'PROFESSIONAL SUMMARY','skills':'CORE SKILLS','exp':'EXPERIENCE','projects':'SELECTED PROJECTS','edu':'EDUCATION','courses':'COURSES & CREDENTIALS','lang':'LANGUAGES'}
        summary = ('Automation, AI & Integrations Analyst. I turn operational processes into automations and internal systems, from discovery and requirements through deployment and support. I administer a self-hosted n8n environment with 10k+ production workflow executions and work with Python, FastAPI, REST APIs, PostgreSQL, Docker and applied AI.')
        skills = [
            '<b>Core:</b> self-hosted n8n · Python · FastAPI · REST APIs/webhooks · JSON/JSON Schema · OAuth 2.0 · SQL/PostgreSQL · Docker',
            '<b>Process & automation:</b> BPMN · AS-IS/TO-BE · requirements · business rules · Power Automate · Make/Zapier · CRM · traceability · documentation',
            '<b>Applied AI & engineering:</b> OpenAI · Gemini · Ollama · RAG/LangChain · MCP · LangGraph/CrewAI · human-in-the-loop · JavaScript/TypeScript · Linux · Git/GitHub Actions · testing · monitoring · logs · retries · idempotency · alerts · backups',
        ]
        vesper_role = 'GRUPO VESPER — Junior Process Automation Technician | Dec. 2025 – Present'
        vesper_meta = 'Vesper Equipamentos EX / Vent Rio · automation, applied AI, integrations and internal systems'
        vesper_bullets = [
            '<b>n8n:</b> administer self-hosted Windows/Docker environment with 10k+ production workflow executions, integrating APIs, webhooks, PostgreSQL and SMTP with logs, retries, alerts, backups and auditability.',
            '<b>Commercial Proposals:</b> built and support an ODT/PDF + IMAP/SMTP workflow with human review; simple proposals went from 2–4 min to &lt;30 sec and are used daily by 4 professionals.',
            '<b>Production & maintenance:</b> deployed Production Operations to 10+ PCs and 1 TV supporting 20+ professionals across 9 sectors; digitized maintenance for 40+ assets with checklists, evidence, history and Quality visibility.',
            '<b>Process & adoption:</b> gather requirements and map AS-IS/TO-BE/BPMN with users, Production, Quality and management; use n8n, Power Automate, Make/Zapier and CRM depending on context. Trained/guided 30+ people.',
        ]
        compass_role = 'COMPASS UOL — IT/Data Intern | Oct. 2024 – Mar. 2025'
        compass_meta = 'Data Engineering scholarship · 10 practical sprints'
        compass_bullets = ['Built a Python/SQL/Docker/AWS pipeline: CSV/TMDB API → S3 → Lambda/boto3 → Glue/PySpark → Raw/Trusted/Refined Parquet → Athena → QuickSight; practiced Linux, Git, ETL/Data Lake and data modeling.']
        projects = [
            '<b>Direct Mail:</b> 6 campaigns over a 1,020-contact base, one with 900+ recipients; 2 n8n workflows, main flow with 158 nodes and 9 Data Tables, queues, deduplication, cancellation and auditing.',
            '<b>CarreiraPessoal:</b> personal Windows product (FastAPI + React/TS + Tauri/Rust) for job discovery, deduplication, career-goal checks, evidence and resume routing; v12.5.2 with 283 passing Python tests.',
            '<b>Operational Catalog:</b> FastAPI + SQLite FTS5, 24 categories and 480+ codes, search without knowing item codes, price review/history, backups and daily use.',
            '<b>Social Publishing:</b> n8n + Meta Graph + OpenAI/Gemini/Ollama, RAG/grounding with LangChain, human review and idempotency; Facebook/Instagram validated in testing.',
        ]
        edu = ['<b>Systems Analysis and Development — UNISUAM</b> · expected Dec. 2026', '<b>42 Rio Piscine</b> · intensive Linux/C program · completed Jul. 2025']
        courses = ['FIRJAN SENAI — AI Agents & Automations (40h) · Google AI Essentials · ENAP RPA (25h) · ENAP Process Mapping & Automation (20h)']
        languages = ['Portuguese: native · English: independent technical reading; basic writing and conversation']

    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=10.5*mm, rightMargin=10.5*mm, topMargin=9.5*mm, bottomMargin=8.5*mm, title=name + ' - ' + title, author='Maycon Ferreira', subject='One-page resume for automation, applied AI, integrations, internal systems and process roles')
    story = [Paragraph(name, s['name']), Paragraph(title, s['title']), Paragraph(contact, s['contact'])]

    def sec(label):
        story.append(Paragraph(label, s['section']))

    sec(sections['summary']); story.append(Paragraph(summary, s['body']))
    sec(sections['skills'])
    for item in skills: story.append(Paragraph(item, s['small']))
    sec(sections['exp'])
    story.extend([Paragraph(vesper_role, s['role']), Paragraph(vesper_meta, s['meta'])])
    for item in vesper_bullets: story.append(bullet(item, s['small']))
    story.extend([Spacer(1,0.6*mm), Paragraph(compass_role, s['role']), Paragraph(compass_meta, s['meta'])])
    for item in compass_bullets: story.append(bullet(item, s['small']))
    sec(sections['projects'])
    for item in projects: story.append(bullet(item, s['small']))
    sec(sections['edu'])
    for item in edu: story.append(Paragraph(item, s['small']))
    sec(sections['courses'])
    for item in courses: story.append(Paragraph(item, s['small']))
    sec(sections['lang'])
    for item in languages: story.append(Paragraph(item, s['small']))

    doc.build(story, onFirstPage=line)
    return path


if __name__ == '__main__':
    print(build('pt'))
    print(build('en'))
