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

# Keep every recruiter contact route both visible to text parsers and clickable for humans.
# Two compact lines are more robust than hyperlink-only labels and remain readable in one page.
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
        'name': ParagraphStyle('name', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=19.0, leading=20.3, textColor=BLACK, spaceAfter=1.6*mm),
        'title': ParagraphStyle('title', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=11.0, leading=12.3, textColor=BLACK, spaceAfter=1.25*mm),
        'contact': ParagraphStyle('contact', parent=base['Normal'], fontName='Helvetica', fontSize=8.3, leading=10.0, textColor=GRAY, spaceAfter=3.25*mm),
        'section': ParagraphStyle('section', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=9.6, leading=11.2, textColor=BLACK, spaceBefore=3.4*mm, spaceAfter=1.65*mm),
        'body': ParagraphStyle('body', parent=base['Normal'], fontName='Helvetica', fontSize=9.25, leading=11.85, textColor=BLACK, spaceAfter=1.35*mm),
        'small': ParagraphStyle('small', parent=base['Normal'], fontName='Helvetica', fontSize=8.85, leading=11.75, textColor=BLACK, spaceAfter=1.0*mm),
        'role': ParagraphStyle('role', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=9.2, leading=11.5, textColor=BLACK, spaceAfter=0.8*mm),
        'meta': ParagraphStyle('meta', parent=base['Normal'], fontName='Helvetica', fontSize=8.2, leading=10.2, textColor=GRAY, spaceAfter=1.0*mm),
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
        sections = {'summary':'RESUMO PROFISSIONAL','skills':'COMPETÊNCIAS','exp':'EXPERIÊNCIA','projects':'PROJETOS SELECIONADOS','edu':'FORMAÇÃO','courses':'CREDENCIAIS E FORMAÇÃO COMPLEMENTAR','lang':'IDIOMAS'}
        summary = ('Analista de Automação, IA e Integrações com atuação ponta a ponta em automação de processos, integrações, APIs e sistemas internos. Administro n8n self-hosted com 10 mil+ execuções em produção e transformo necessidades operacionais em soluções com Python, FastAPI, SQL/PostgreSQL e IA aplicada, do mapeamento BPMN/AS-IS/TO-BE e requisitos à implantação, treinamento e sustentação.')
        skills = [
            '<b>Automação e integrações:</b> n8n self-hosted · low-code/no-code · Python · FastAPI · APIs REST/JSON · webhooks · OAuth 2.0 · SQL/PostgreSQL · Docker · Power Platform/Make/Zapier/CRM (uso contextual)',
            '<b>Processos e entrega:</b> BPMN · AS-IS/TO-BE · levantamento de requisitos · stakeholders · regras de negócio · testes · UAT/homologação · documentação · implantação · treinamento · melhoria contínua',
            '<b>IA aplicada e engenharia:</b> IA generativa/LLMs · agentes de IA · RAG/grounding · human-in-the-loop · JavaScript/TypeScript · Git/GitHub Actions · CI/CD · logs/monitoramento · troubleshooting · tratamento de erros · retries · idempotência · segurança de integrações · gestão de segredos',
        ]
        vesper_role = 'GRUPO VESPER — Técnico Júnior em Automação de Processos | dez. 2025 – atual'
        vesper_meta = 'Vesper Equipamentos EX / Vent Rio · automação, IA aplicada, integrações e sistemas internos'
        vesper_bullets = [
            '<b>n8n e integrações:</b> administro ambiente self-hosted Windows/Docker com 10 mil+ execuções de workflows em produção, integrando APIs, webhooks, PostgreSQL e SMTP com logs, retries, alertas, backups e auditoria.',
            '<b>Proposta Comercial:</b> desenvolvi e sustento o fluxo com ODT/PDF, IMAP/SMTP e revisão humana; propostas simples passaram de 2–4 min para &lt;30 s, com uso diário por 4 profissionais.',
            '<b>Produção e manutenção:</b> implantei a Produção Operacional em 10+ PCs e 1 TV para 20+ profissionais em 9 setores e digitalizei manutenção de 40+ ativos com checklists, fotos/evidências, histórico e consulta da Qualidade.',
            '<b>HelpDesk e adoção:</b> sistema interno em uso por 11 pessoas; levanto requisitos, modelo AS-IS/TO-BE/BPMN, testo/homologo e implanto soluções com usuários, stakeholders e gestão; já treinei/orientei 30+ pessoas e acompanho sustentação e melhoria contínua.',
        ]
        compass_role = 'COMPASS UOL — Estagiário TI/Dados | out. 2024 – mar. 2025'
        compass_meta = 'Programa de bolsas em Engenharia de Dados · 10 sprints práticas'
        compass_bullets = ['Construí pipeline em Python/SQL/Docker/AWS: ingestão CSV/TMDB API → S3 → Lambda/boto3 → Glue/PySpark → Parquet Raw/Trusted/Refined → Athena → QuickSight; pratiquei Linux, Git, ETL/Data Lake e modelagem.']
        projects = [
            '<b>Mala Direta:</b> 6 campanhas sobre base de 1.020 contatos, uma com 900+; 2 workflows n8n com fila por destinatário, deduplicação, cancelamento revalidado, retry e auditoria.',
            '<b>CarreiraPessoal:</b> produto Windows em uso próprio (FastAPI + React/TS + Tauri/Rust) para descoberta, deduplicação, Career Goal, evidências e roteamento de currículo; v12.5.2 com 283 testes Python aprovados.',
            '<b>Catálogo Operacional:</b> FastAPI + SQLite FTS5, 24 categorias e 480+ códigos, busca unificada, controle de revisão, histórico de preço e backups; uso diário por 3 pessoas.',
            '<b>Postagem Redes:</b> n8n + Meta Graph API com IA aplicada, RAG/grounding, human-in-the-loop, evals offline reproduzíveis, idempotência e isolamento de falhas por canal; Facebook/Instagram validados em teste.',
        ]
        edu = ['<b>Análise e Desenvolvimento de Sistemas — UNISUAM</b> · conclusão prevista dez. 2026', '<b>Piscine 42 Rio</b> · programa intensivo em Linux/C · concluído jul. 2025']
        courses = [
            '<b>Selecionadas:</b> Microsoft Applied Skills (3) — Microsoft Foundry Agents · MCP Tools with Agents · Power Apps Canvas Apps; UiPath Academy — Automation Business Analyst Professional Training; n8n Academy — N8N102/N8N103; Make Academy — AI Agent Builder; FIRJAN SENAI — Agentes e Automações (40h).',
        ]
        languages = ['Português nativo · Inglês: leitura técnica independente; escrita e conversação básicas']
    else:
        path = OUT / 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf'
        name = 'MAYCON FERREIRA'
        title = 'AI, AUTOMATION & INTEGRATIONS ANALYST'
        contact = CONTACT_EN
        sections = {'summary':'PROFESSIONAL SUMMARY','skills':'CORE SKILLS','exp':'EXPERIENCE','projects':'SELECTED PROJECTS','edu':'EDUCATION','courses':'CREDENTIALS & ADDITIONAL TRAINING','lang':'LANGUAGES'}
        summary = ('Automation, AI & Integrations Analyst working end to end across process automation, integrations, APIs and internal systems. I administer a self-hosted n8n environment with 10k+ production workflow executions and turn operational needs into solutions with Python, FastAPI, SQL/PostgreSQL and applied AI, from BPMN/AS-IS/TO-BE mapping and requirements through deployment, training and support.')
        skills = [
            '<b>Automation & integrations:</b> self-hosted n8n · low-code/no-code · Python · FastAPI · REST/JSON APIs · webhooks · OAuth 2.0 · SQL/PostgreSQL · Docker · Power Platform/Make/Zapier/CRM (contextual use)',
            '<b>Process & delivery:</b> BPMN · AS-IS/TO-BE · requirements discovery · stakeholders · business rules · testing · UAT · documentation · deployment · training · continuous improvement',
            '<b>Applied AI & engineering:</b> generative AI/LLMs · AI agents · RAG/grounding · human-in-the-loop · JavaScript/TypeScript · Git/GitHub Actions · CI/CD · logs/monitoring · troubleshooting · error handling · retries · idempotency · integration security · secret management',
        ]
        vesper_role = 'GRUPO VESPER — Junior Process Automation Technician | Dec. 2025 – Present'
        vesper_meta = 'Vesper Equipamentos EX / Vent Rio · automation, applied AI, integrations and internal systems'
        vesper_bullets = [
            '<b>n8n & integrations:</b> administer a self-hosted Windows/Docker environment with 10k+ production workflow executions, integrating APIs, webhooks, PostgreSQL and SMTP with logs, retries, alerts, backups and auditability.',
            '<b>Commercial Proposals:</b> built and support an ODT/PDF + IMAP/SMTP workflow with human review; simple proposals went from 2–4 min to &lt;30 sec and are used daily by 4 professionals.',
            '<b>Production & maintenance:</b> deployed Production Operations to 10+ PCs and 1 TV supporting 20+ professionals across 9 sectors; digitized maintenance for 40+ assets with checklists, evidence, history and Quality visibility.',
            '<b>HelpDesk & adoption:</b> internal system used by 11 people; gather requirements, map AS-IS/TO-BE/BPMN, test/UAT and deploy solutions with users, stakeholders and management; trained/guided 30+ people and follow support and continuous improvement.',
        ]
        compass_role = 'COMPASS UOL — IT/Data Intern | Oct. 2024 – Mar. 2025'
        compass_meta = 'Data Engineering scholarship · 10 practical sprints'
        compass_bullets = ['Built a Python/SQL/Docker/AWS pipeline: CSV/TMDB API → S3 → Lambda/boto3 → Glue/PySpark → Raw/Trusted/Refined Parquet → Athena → QuickSight; practiced Linux, Git, ETL/Data Lake and data modeling.']
        projects = [
            '<b>Direct Mail:</b> 6 campaigns over a 1,020-contact base, one with 900+ recipients; 2 n8n workflows with per-recipient queues, deduplication, revalidated cancellation, retry and auditing.',
            '<b>CarreiraPessoal:</b> personal Windows product in active personal use (FastAPI + React/TS + Tauri/Rust) for job discovery, deduplication, career-goal checks, evidence and resume routing; v12.5.2 with 283 passing Python tests.',
            '<b>Operational Catalog:</b> FastAPI + SQLite FTS5, 24 categories and 480+ codes, unified search, revision control, price history and backups; used daily by 3 people.',
            '<b>Social Publishing:</b> n8n + Meta Graph API with applied AI, RAG/grounding, human-in-the-loop, reproducible offline evals, idempotency and per-channel failure isolation; Facebook/Instagram validated in testing.',
        ]
        edu = ['<b>Systems Analysis and Development — UNISUAM</b> · expected Dec. 2026', '<b>42 Rio Piscine</b> · intensive Linux/C program · completed Jul. 2025']
        courses = [
            '<b>Selected:</b> Microsoft Applied Skills (3) — Microsoft Foundry Agents · MCP Tools with Agents · Power Apps Canvas Apps; UiPath Academy — Automation Business Analyst Professional Training; n8n Academy — N8N102/N8N103; Make Academy — AI Agent Builder; FIRJAN SENAI — AI Agents & Automations (40h).',
        ]
        languages = ['Portuguese: native · English: independent technical reading; basic writing and conversation']

    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=11*mm, rightMargin=11*mm, topMargin=10*mm, bottomMargin=10*mm, title=name + ' - ' + title, author='Maycon Ferreira', subject='One-page resume for automation, applied AI, integrations, internal systems and process roles')
    story = [Paragraph(name, s['name']), Paragraph(title, s['title']), Paragraph(contact, s['contact'])]

    def sec(label):
        story.append(Paragraph(label, s['section']))

    sec(sections['summary']); story.append(Paragraph(summary, s['body']))
    sec(sections['skills'])
    for item in skills: story.append(Paragraph(item, s['small']))
    sec(sections['exp'])
    story.extend([Paragraph(vesper_role, s['role']), Paragraph(vesper_meta, s['meta'])])
    for item in vesper_bullets: story.append(bullet(item, s['small']))
    story.extend([Spacer(1,1.4*mm), Paragraph(compass_role, s['role']), Paragraph(compass_meta, s['meta'])])
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