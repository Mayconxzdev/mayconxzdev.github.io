from __future__ import annotations
from pathlib import Path
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"assets"/"cv"
OUT.mkdir(parents=True,exist_ok=True)
W,H=A4; L=42; R=42; CW=W-L-R
FONT='Helvetica'; BOLD='Helvetica-Bold'
INK=HexColor('#101828'); MUTED=HexColor('#475467'); LINE=HexColor('#C7D3E0'); ACCENT=HexColor('#0F4C81')

PT={
'filename':'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
'title':'ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES',
'location':'Rio de Janeiro - RJ | remoto, híbrido ou presencial | viagens e mudança',
'headings':['RESUMO PROFISSIONAL','HABILIDADES TÉCNICAS','EXPERIÊNCIA PROFISSIONAL','PROJETOS SELECIONADOS','FORMAÇÃO','CERTIFICAÇÕES','IDIOMAS'],
'summary':'Analista de Automação, IA e Integrações com atuação ponta a ponta na transformação de processos operacionais em automações e sistemas internos. Administro n8n self-hosted com 10 mil+ execuções de workflows em produção e desenvolvo e sustento soluções com Python, FastAPI, APIs REST, PostgreSQL, Docker e IA generativa, do levantamento de requisitos à implantação, monitoramento, treinamento e melhoria contínua.',
'skills':[
'<b>Automação, integrações e processos:</b> n8n self-hosted, Python, APIs REST, webhooks, JSON/JSON Schema, OAuth 2.0, SQL/PostgreSQL, AS-IS/TO-BE, requisitos, regras de negócio, rastreabilidade, auditoria, qualidade/conformidade e documentação.',
'<b>IA aplicada:</b> OpenAI, Gemini e Ollama, APIs de LLM, engenharia de prompts, RAG/grounding com LangChain, recuperação de contexto, respostas estruturadas e revisão humana (human-in-the-loop).',
'<b>Engenharia e confiabilidade:</b> FastAPI, JavaScript/TypeScript, Docker, Linux, Git/GitHub Actions, testes automatizados, monitoramento, logs, retries, idempotência, alertas, backups e gestão de segredos.'
],
'vesper_role':'Técnico Júnior em Automação de Processos (cargo formal) | automação, IA aplicada e integrações',
'vesper_points':[
'Administro uma instância n8n self-hosted em Windows/Docker com 10 mil+ execuções de workflows em produção, integrando APIs REST, webhooks, PostgreSQL e SMTP com monitoramento, logs, retries, alertas, backups e auditoria.',
'Desenvolvi o Proposta Comercial, com ODT/PDF, IMAP/SMTP, revisão humana e rastreabilidade; propostas simples passaram de 2-4 minutos para menos de 30 segundos, com uso diário por 4 profissionais.',
'Implantei o Produção Operacional em 10+ computadores e 1 TV, apoiando 20+ profissionais em 9 setores, e uma solução de manutenção com 40+ ativos, checklists, evidências, histórico e rastreabilidade usada por manutenção e Qualidade.',
'Levanto requisitos diretamente com usuários, Produção, Qualidade e gestão em ambiente industrial com requisitos de qualidade/Ex, transformando rotinas de planilhas, papel e pastas de rede em processos digitais com aprovações, versionamento e auditoria; treinei/orientei 30+ pessoas.'
],
'compass_role':'Estagiário de TI/Dados | Programa de Bolsas em Engenharia de Dados',
'compass':'Concluí 10 sprints práticas com Linux, Git, Python, SQL e Docker e construí pipeline ETL/Data Lake em AWS: CSV/API TMDB, S3, Lambda/boto3, Glue/PySpark, Parquet, camadas Raw/Trusted/Refined, Athena e QuickSight.',
'projects':[
'<b>Mala Direta:</b> 6 campanhas sobre base de 1.020 contatos, incluindo uma com 900+ destinatários; n8n, filas, 158 nós no workflow principal, 9 Data Tables, deduplicação, envio de teste, cancelamento revalidado e auditoria.',
'<b>CarreiraPessoal:</b> produto pessoal local-first usado na própria busca, com FastAPI, React/TypeScript, Tauri/Rust, SQLite/FTS5, Career Goal Gate, EvidenceGuard, Resume Router e 102 famílias ATS reconhecidas; versão 12.5.2 validada com 283 testes Python.',
'<b>Central ISO:</b> piloto técnico criado a partir de requisitos da Qualidade para rastrear documentos, certificados e não conformidades; FastAPI, n8n, Docker, regras determinísticas, SHA-256, acesso read-only e testes automatizados.',
'<b>Postagem Redes:</b> RAG/grounding com LangChain, Supabase e n8n/Docker para reduzir alucinações, integrado a Meta Graph API e LLMs com aprovação humana; canais exercitados em teste.'
],
'education':['<b>Tecnólogo em Análise e Desenvolvimento de Sistemas - UNISUAM</b> | conclusão prevista: dez. 2026','Piscine 42 Rio | programa intensivo em Linux/C concluído em jul. 2025'],
'certs':'Ferramentas de IA: Agentes e Automações - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; Automação de Processos através da RPA - ENAP (25h); Mapeamento e Automação de Processos - ENAP (20h).',
'language':'Português nativo | Inglês: leitura técnica independente; escrita e conversação básicas.'
}

EN={
'filename':'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
'title':'AI AUTOMATION & INTEGRATIONS ANALYST',
'location':'Rio de Janeiro, Brazil | remote, hybrid or on-site | available to travel and relocate',
'headings':['PROFESSIONAL SUMMARY','TECHNICAL SKILLS','PROFESSIONAL EXPERIENCE','SELECTED PROJECTS','EDUCATION','CERTIFICATIONS','LANGUAGES'],
'summary':'AI Automation & Integrations Analyst with end-to-end experience turning operational processes into automations and internal systems. I administer a self-hosted n8n environment with 10,000+ workflow executions in production and build and support solutions with Python, FastAPI, REST APIs, PostgreSQL, Docker and generative AI, from requirements discovery through deployment, monitoring, training and continuous improvement.',
'skills':[
'<b>Automation, integrations and processes:</b> self-hosted n8n, Python, REST APIs, webhooks, JSON/JSON Schema, OAuth 2.0, SQL/PostgreSQL, AS-IS/TO-BE, requirements, business rules, traceability, auditing, quality/compliance and documentation.',
'<b>Applied AI:</b> OpenAI, Gemini and Ollama, LLM APIs, prompt engineering, RAG/grounding with LangChain, context retrieval, structured outputs and human-in-the-loop review.',
'<b>Engineering and reliability:</b> FastAPI, JavaScript/TypeScript, Docker, Linux, Git/GitHub Actions, automated tests, monitoring, logs, retries, idempotency, alerts, backups and secrets management.'
],
'vesper_role':'Junior Process Automation Technician (formal title) | automation, applied AI and integrations',
'vesper_points':[
'Administer a self-hosted n8n environment on Windows/Docker with 10,000+ workflow executions in production, integrating REST APIs, webhooks, PostgreSQL and SMTP with monitoring, logs, retries, alerts, backups and auditing.',
'Developed Proposta Comercial with ODT/PDF, IMAP/SMTP, human review and traceability; simple proposals went from 2-4 minutes to under 30 seconds and are used daily by 4 professionals.',
'Deployed Produção Operacional to 10+ workstations and 1 factory TV, supporting 20+ professionals across 9 production areas, plus a maintenance solution covering 40+ assets with checklists, evidence, history and traceability used by Maintenance and Quality.',
'Gather requirements directly with users, Production, Quality and management in an industrial environment with quality/Ex requirements, turning spreadsheet, paper and network-folder routines into digital processes with approvals, versioning and auditability; trained/guided 30+ people.'
],
'compass_role':'Data Engineering Intern | Scholarship Program',
'compass':'Completed 10 practical sprints with Linux, Git, Python, SQL and Docker and built an AWS ETL/Data Lake pipeline: CSV/TMDB API, S3, Lambda/boto3, Glue/PySpark, Parquet, Raw/Trusted/Refined layers, Athena and QuickSight.',
'projects':[
'<b>Mala Direta:</b> 6 campaigns over a 1,020-contact base, including one with 900+ recipients; n8n, queues, 158 nodes in the main workflow, 9 Data Tables, deduplication, test send, revalidated cancellation and auditing.',
'<b>CarreiraPessoal:</b> local-first personal product used in my own job search, built with FastAPI, React/TypeScript, Tauri/Rust and SQLite/FTS5; Career Goal Gate, EvidenceGuard, Resume Router and 102 ATS families recognized; v12.5.2 validated with 283 Python tests.',
'<b>Central ISO:</b> technical pilot based on Quality requirements to track documents, certificates and nonconformities; FastAPI, n8n, Docker, deterministic rules, SHA-256, read-only access and automated tests.',
'<b>Postagem Redes:</b> RAG/grounding with LangChain, Supabase and n8n/Docker to reduce hallucinations, integrated with Meta Graph API and LLMs with human approval; channels exercised in testing.'
],
'education':['<b>Technology Degree (Tecnólogo) in Systems Analysis and Development - UNISUAM</b> | expected completion: Dec. 2026','42 Rio Piscine | intensive Linux/C program completed in Jul. 2025'],
'certs':'AI Tools: Agents and Automations - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; Process Automation with RPA - ENAP (25h); Process Mapping and Automation - ENAP (20h).',
'language':'Portuguese: native | English: independent technical reading; basic writing and conversation.'
}

class Audit:
    def __init__(self): self.prev=None
    def add(self,name,top,bottom):
        if self.prev and self.prev[1]-top < -0.4: raise RuntimeError(f'overlap {self.prev[0]} -> {name}: {top-self.prev[1]:.2f}')
        self.prev=(name,bottom)

def pstyle(size=8.65,leading=10.65,color=INK,bold=False):
    return ParagraphStyle('x',fontName=BOLD if bold else FONT,fontSize=size,leading=leading,textColor=color,spaceAfter=0)

def para(c,text,y,a,name,size=8.65,leading=10.65):
    p=Paragraph(text,pstyle(size,leading)); _,h=p.wrap(CW,999); p.drawOn(c,L,y-h); a.add(name,y,y-h); return y-h

def sec(c,title,y,a):
    top=y-5; baseline=top-9.6; liney=baseline-4.8; bottom=liney-6.6
    c.setFillColor(ACCENT); c.rect(L,baseline-1,4,11,fill=1,stroke=0)
    c.setFillColor(INK); c.setFont(BOLD,9.8); c.drawString(L+10,baseline,title)
    c.setStrokeColor(LINE); c.setLineWidth(.55); c.line(L,liney,L+CW,liney)
    a.add('sec '+title,top,bottom); return bottom

def bullet(c,text,y,a,name):
    return para(c,'• '+text,y,a,name,8.35,10.25)-1.7

def draw(data):
    path=OUT/data['filename']; c=Canvas(str(path),pagesize=A4)
    c.setTitle('Maycon Ferreira - '+data['title']); c.setAuthor('Maycon Ferreira'); c.setSubject('One-page resume for automation, applied AI, integrations, internal systems and process roles')
    c.setKeywords('automation, n8n, Python, REST APIs, webhooks, JSON, FastAPI, PostgreSQL, Docker, Linux, applied AI, generative AI, RAG, LangChain, process automation, AS-IS, TO-BE, requirements, traceability, auditing, testing, monitoring, data engineering')
    a=Audit(); y=H-37
    c.setFillColor(INK); c.setFont(BOLD,20); c.drawString(L,y,'MAYCON FERREIRA'); y-=20
    c.setFillColor(ACCENT); c.setFont(BOLD,10.7); c.drawString(L,y,data['title']); y-=15
    c.setFillColor(MUTED); c.setFont(FONT,8.25); c.drawString(L,y,data['location']); y-=13
    links=[('Telefone/WhatsApp: +55 (21) 96481-0480','https://wa.me/5521964810480'),('E-mail: mayconxz00dev@gmail.com','mailto:mayconxz00dev@gmail.com'),('LinkedIn','https://www.linkedin.com/in/maycon-ferreira-7bb870231/'),('GitHub','https://github.com/Mayconxzdev'),('Portfólio' if data is PT else 'Portfolio','https://mayconxzdev.github.io/')]
    x=L; size=8.05; lead=10.8
    for label,url in links:
        text=label+'  '; width=pdfmetrics.stringWidth(text,FONT,size)
        if x!=L and x+width>L+CW:
            y-=lead; x=L
        c.setFont(FONT,size); c.setFillColor(MUTED); c.drawString(x,y,text); c.linkURL(url,(x,y-2,x+width,y+size+2),relative=0,thickness=0); x+=width+8
    y-=15

    y=sec(c,data['headings'][0],y,a); y=para(c,data['summary'],y,a,'summary',8.7,10.8)-2.5
    y=sec(c,data['headings'][1],y,a)
    for i,s in enumerate(data['skills']): y=para(c,s,y,a,f'skill{i}',8.35,10.25)-1.3
    y=sec(c,data['headings'][2],y,a)
    c.setFillColor(INK); c.setFont(BOLD,8.9); c.drawString(L,y-8.5,'GRUPO VESPER')
    c.setFillColor(MUTED); c.setFont(FONT,8); c.drawRightString(L+CW,y-8.5,'12/2025 - presente' if data is PT else '12/2025 - Present'); y-=13
    y=para(c,'Vesper Equipamentos EX e Vent Rio Equipamentos',y,a,'company',8.25,10)-.6
    y=para(c,data['vesper_role'],y,a,'role',8.3,10.1)-1
    for i,b in enumerate(data['vesper_points']): y=bullet(c,b,y,a,f'vb{i}')
    y-=1
    c.setFillColor(INK); c.setFont(BOLD,8.9); c.drawString(L,y-8.5,'COMPASS UOL'); c.setFillColor(MUTED); c.setFont(FONT,8); c.drawRightString(L+CW,y-8.5,'10/2024 - 03/2025'); y-=13
    y=para(c,data['compass_role'],y,a,'compassrole',8.3,10.1)-1
    y=bullet(c,data['compass'],y,a,'compass')
    y=sec(c,data['headings'][3],y,a)
    for i,b in enumerate(data['projects']): y=bullet(c,b,y,a,f'proj{i}')
    y=sec(c,data['headings'][4],y,a)
    for i,e in enumerate(data['education']): y=para(c,e,y,a,f'edu{i}',8.35,10.15)-.9
    y=sec(c,data['headings'][5],y,a); y=para(c,data['certs'],y,a,'certs',8.3,10.1)-1
    y=sec(c,data['headings'][6],y,a); y=para(c,data['language'],y,a,'lang',8.35,10.15)
    if y<34: raise RuntimeError(f'overflow {data["filename"]}: {y}')
    c.showPage(); c.save(); print(path, 'bottom', y)

for d in (PT,EN): draw(d)
