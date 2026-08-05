from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'/'cv'
PAGE_W,PAGE_H=A4; LEFT=48; RIGHT=48; CW=PAGE_W-LEFT-RIGHT
INK=HexColor('#111827'); MUTED=HexColor('#475569'); LINE=HexColor('#CBD5E1'); ACCENT=HexColor('#0F4C81')
FONT_CANDIDATES = [
    (Path(r'C:\\Windows\\Fonts\\arial.ttf'), Path(r'C:\\Windows\\Fonts\\arialbd.ttf')),
    (Path('/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf'), Path('/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf')),
    (Path('/usr/share/fonts/truetype/lato/Lato-Regular.ttf'), Path('/usr/share/fonts/truetype/lato/Lato-Bold.ttf')),
]
for REG, BOLD in FONT_CANDIDATES:
    if REG.exists() and BOLD.exists():
        break
else:
    raise FileNotFoundError('No supported resume font found')
pdfmetrics.registerFont(TTFont('ResumeSans', str(REG)))
pdfmetrics.registerFont(TTFont('ResumeSans-Bold', str(BOLD)))
pdfmetrics.registerFontFamily('ResumeSans',normal='ResumeSans',bold='ResumeSans-Bold')

PT={
'filename':'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf','title':'ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES','location':'Rio de Janeiro - RJ, Brasil','portfolio_label':'Portfólio','footer':'Portfólio público: mayconxzdev.github.io','summary_heading':'RESUMO PROFISSIONAL',
'summary':'Profissional de automação, IA generativa e aplicada e integração de sistemas e ferramentas, com atuação ponta a ponta em soluções internas: mapeamento e automação de processos, requisitos, arquitetura, desenvolvimento, implantação, treinamento, monitoramento e sustentação. Experiência com n8n self-hosted, Python, APIs REST, bancos de dados e fluxos com aprovação humana, filas, idempotência, auditoria e tratamento de falhas.',
'skills_heading':'COMPETÊNCIAS PRINCIPAIS','skills':[
'<b>Automação e mapeamento de processos:</b> n8n self-hosted, workflows, low-code, AS-IS/TO-BE, levantamento de requisitos, regras de negócio, documentação, treinamento, melhoria contínua e aprovação humana.',
'<b>IA generativa e aplicada:</b> OpenAI, Gemini, Ollama e OpenRouter; engenharia de prompts, assistentes e agentes com ferramentas, memória, recuperação de contexto, saída estruturada, fallback e revisão humana.',
'<b>Integração de sistemas e ferramentas:</b> APIs REST, webhooks, HTTP/JSON, OAuth 2.0, SMTP/IMAP, Meta Graph API, Evolution API/WPPConnect, Supabase, Firebase, Google Sheets e Postman.',
'<b>Engenharia e confiabilidade:</b> Python, JavaScript/TypeScript, FastAPI, SQL, PostgreSQL, SQLite, Docker, Git/GitHub Actions, testes, logs, backups, alertas, retries, idempotência e gestão de segredos.'
],
'experience_heading':'EXPERIÊNCIA PROFISSIONAL','vesper_org':'GRUPO VESPER - VESPER EQUIPAMENTOS EX E VENT RIO EQUIPAMENTOS','vesper_date':'dez. 2025 - atual','vesper_role':'Técnico Júnior em Automação de Processos (cargo formal) | automação, IA generativa/aplicada e integrações','vesper_points':[
'Conduzo o ciclo técnico de soluções internas: levantamento com gestão e usuários, mapeamento do processo, regras, arquitetura, desenvolvimento, testes, implantação, documentação, treinamento e sustentação.',
'Administro automações n8n self-hosted em Windows/Docker, integrando APIs, webhooks, bancos, e-mail e ferramentas operacionais com persistência, backups, alertas, retries, auditoria e diagnóstico.',
'Desenvolvi Vesper Propostas com geração ODT/PDF, IMAP/SMTP e revisão humana; o case documenta redução observada no tempo de propostas simples.',
'Implementei HelpDesk, Produção Operacional, ProcureFlow, ComprasVesper, Mala Direta e Postagem Redes para rotinas de TI, produção, compras e comunicação, com limites operacionais declarados.'
],
'compasso_org':'COMPASSO TECNOLOGIA LTDA','compasso_date':'out. 2024 - mar. 2025','compasso_role':'Estagiário de TI/Dados','compasso_point':'Automatizei rotina em Python/Pandas, reduzindo processamento observado de aproximadamente 3 horas para cerca de 5 minutos; atuei também com AWS S3/EC2, boto3, Pandas/Polars, SQL, Docker, suporte e documentação.',
'education_heading':'EVIDÊNCIAS, FORMAÇÃO E CERTIFICAÇÕES','education':[
'<b>Portfólio:</b> cases públicos e sanitizados com arquitetura, screenshots, testes e CI para automação n8n, IA generativa aplicada, integração de ferramentas, desktop, PWA e sistemas internos.',
'<b>Formação:</b> Tecnólogo em Análise e Desenvolvimento de Sistemas - UNISUAM | conclusão prevista: dez. 2026. Piscine 42 Rio concluída em jul. 2025.',
'<b>Certificações:</b> Ferramentas de IA: Agentes e Automações - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; RPA para Transformação Digital - ENAP (25h); Mapeamento e Automação de Processos - ENAP (20h); LGPD - ENAP (10h).',
'<b>Idiomas e disponibilidade:</b> inglês técnico para leitura; escrita e conversação básicas. Disponível para trabalho remoto, híbrido ou presencial; viagens e mudança.'
]}
EN={
'filename':'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf','title':'AI AUTOMATION & INTEGRATIONS ANALYST','location':'Rio de Janeiro - Brazil','portfolio_label':'Portfolio','footer':'Public portfolio: mayconxzdev.github.io','summary_heading':'PROFESSIONAL SUMMARY',
'summary':'Automation, generative and applied AI, and systems/tools integration professional working end to end on internal solutions: process mapping and automation, requirements, architecture, development, deployment, training, monitoring and support. Experience with self-hosted n8n, Python, REST APIs, databases and workflows with human approval, queues, idempotency, auditing and failure handling.',
'skills_heading':'CORE COMPETENCIES','skills':[
'<b>Process mapping and automation:</b> self-hosted n8n, workflows, low-code, AS-IS/TO-BE, requirements discovery, business rules, documentation, training, continuous improvement and human approval.',
'<b>Generative and applied AI:</b> OpenAI, Gemini, Ollama and OpenRouter; prompt engineering, assistants and agents with tools, memory, context retrieval, structured output, fallback and human review.',
'<b>Systems and tools integration:</b> REST APIs, webhooks, HTTP/JSON, OAuth 2.0, SMTP/IMAP, Meta Graph API, Evolution API/WPPConnect, Supabase, Firebase, Google Sheets and Postman.',
'<b>Engineering and reliability:</b> Python, JavaScript/TypeScript, FastAPI, SQL, PostgreSQL, SQLite, Docker, Git/GitHub Actions, tests, logs, backups, alerts, retries, idempotency and secrets management.'
],
'experience_heading':'PROFESSIONAL EXPERIENCE','vesper_org':'GRUPO VESPER - VESPER EQUIPAMENTOS EX AND VENT RIO EQUIPAMENTOS','vesper_date':'Dec. 2025 - Present','vesper_role':'Junior Process Automation Technician (formal title) | automation, generative/applied AI and integrations','vesper_points':[
'Lead the technical lifecycle of internal solutions: discovery with management and users, process mapping, rules, architecture, development, testing, deployment, documentation, training and support.',
'Administer self-hosted n8n automations in Windows/Docker, integrating APIs, webhooks, databases, e-mail and operational tools with persistence, backups, alerts, retries, auditing and diagnosis.',
'Developed Vesper Propostas with ODT/PDF generation, IMAP/SMTP and human review; the case documents an observed reduction in simple-proposal time.',
'Implemented HelpDesk, Produção Operacional, ProcureFlow, ComprasVesper, Mala Direta and Postagem Redes for IT, production, purchasing and communication routines, with declared operational limits.'
],
'compasso_org':'COMPASSO TECNOLOGIA LTDA','compasso_date':'Oct. 2024 - Mar. 2025','compasso_role':'IT/Data Intern','compasso_point':'Automated a Python/Pandas routine, reducing observed processing time from approximately three hours to around five minutes; also worked with AWS S3/EC2, boto3, Pandas/Polars, SQL, Docker, support and documentation.',
'education_heading':'EVIDENCE, EDUCATION & CERTIFICATIONS','education':[
'<b>Portfolio:</b> public and sanitized case studies with architecture, screenshots, tests and CI for n8n automation, applied generative AI, tools integration, desktop apps, PWA and internal systems.',
'<b>Education:</b> Associate Degree in Systems Analysis and Development - UNISUAM | expected completion: Dec. 2026. 42 Rio Piscine completed in Jul. 2025.',
'<b>Certifications:</b> AI Tools: Agents and Automations - FIRJAN SENAI (40h); Google AI Essentials - Google/Coursera; Process Automation by RPA - ENAP (25h); Process Mapping and Automation - ENAP (20h); LGPD - ENAP (10h).',
'<b>Languages and availability:</b> technical English for reading; basic writing and conversation. Available for remote, hybrid or on-site work; travel and relocation.'
]}

def para(text,style,c,y,indent=0):
 p=Paragraph(text,style); _,h=p.wrap(CW-indent,999); p.drawOn(c,LEFT+indent,y-h); return y-h

def section(c,title,y):
 y-=13;c.setFillColor(ACCENT);c.rect(LEFT,y-2,4,13,fill=1,stroke=0);c.setFillColor(INK);c.setFont('ResumeSans-Bold',10);c.drawString(LEFT+10,y,title);y-=6;c.setStrokeColor(LINE);c.setLineWidth(.6);c.line(LEFT,y,LEFT+CW,y);return y-11

def width(t,f,s): return pdfmetrics.stringWidth(t,f,s)
def linkline(c,y,items):
 x=LEFT;s=8.9;lead=13;c.setFont('ResumeSans',s)
 for label,url in items:
  txt=label+'  ';w=width(txt,'ResumeSans',s)
  if x!=LEFT and x+w>LEFT+CW:x=LEFT;y-=lead
  c.setFillColor(MUTED);c.drawString(x,y,txt);c.linkURL(url,(x,y-2,x+w,y+s+2),relative=0,thickness=0);x+=w+10
 return y-lead

def generate(d):
 path=OUT/d['filename'];c=Canvas(str(path),pagesize=A4,pageCompression=1);c.setTitle(f"Maycon Ferreira - {d['title']}");c.setAuthor('Maycon Ferreira');c.setSubject('Resume for process automation, generative and applied AI, and systems/tools integration roles');c.setKeywords('process mapping, process automation, generative AI, applied AI, systems integration, tools integration, n8n, Python, REST APIs, FastAPI, SQL, Docker');c.setCreator('Maycon Ferreira')
 y=PAGE_H-40;c.setFillColor(ACCENT);c.rect(0,PAGE_H-8,PAGE_W,8,fill=1,stroke=0);c.setFillColor(INK);c.setFont('ResumeSans-Bold',19);c.drawString(LEFT,y,'MAYCON FERREIRA');y-=17;c.setFillColor(ACCENT);c.setFont('ResumeSans-Bold',10.5);c.drawString(LEFT,y,d['title']);y-=15;c.setFillColor(MUTED);c.setFont('ResumeSans',9);c.drawString(LEFT,y,d['location']);y-=13
 y=linkline(c,y,[('WhatsApp: +55 (21) 96481-0480','https://wa.me/5521964810480'),('E-mail: mayconxz00dev@gmail.com','mailto:mayconxz00dev@gmail.com')]);y=linkline(c,y,[('LinkedIn: linkedin.com/in/maycon-ferreira-7bb870231/','https://www.linkedin.com/in/maycon-ferreira-7bb870231/'),('GitHub: github.com/Mayconxzdev','https://github.com/Mayconxzdev'),(f"{d['portfolio_label']}: mayconxzdev.github.io",'https://mayconxzdev.github.io/')]);c.setStrokeColor(LINE);c.line(LEFT,y-2,LEFT+CW,y-2);y-=9
 base=ParagraphStyle('base',fontName='ResumeSans',fontSize=9.25,leading=12.25,textColor=INK);skill=ParagraphStyle('skill',parent=base,fontSize=9.0,leading=11.75);role=ParagraphStyle('role',parent=base,fontSize=9.0,leading=11.5,textColor=MUTED);bullet=ParagraphStyle('bullet',parent=base,fontSize=8.9,leading=11.55,leftIndent=12,firstLineIndent=-8);evidence=ParagraphStyle('evidence',parent=base,fontSize=8.75,leading=11.35)
 y=section(c,d['summary_heading'],y);y=para(escape(d['summary']),base,c,y)
 y=section(c,d['skills_heading'],y)
 for i in d['skills']:y=para(i,skill,c,y);y-=2
 y=section(c,d['experience_heading'],y);c.setFont('ResumeSans-Bold',9.2);c.setFillColor(INK);c.drawString(LEFT,y,d['vesper_org']);c.setFont('ResumeSans',8.3);c.setFillColor(MUTED);c.drawRightString(LEFT+CW,y,d['vesper_date']);y-=13;y=para(escape(d['vesper_role']),role,c,y);y-=1
 for i in d['vesper_points']:y=para('- '+escape(i),bullet,c,y);y-=1
 y-=7;c.setFont('ResumeSans-Bold',9.2);c.setFillColor(INK);c.drawString(LEFT,y,d['compasso_org']);c.setFont('ResumeSans',8.3);c.setFillColor(MUTED);c.drawRightString(LEFT+CW,y,d['compasso_date']);y-=13;y=para(escape(d['compasso_role']),role,c,y);y=para('- '+escape(d['compasso_point']),bullet,c,y)
 y=section(c,d['education_heading'],y)
 for i in d['education']:y=para(i,evidence,c,y);y-=2
 if y<38: raise RuntimeError(f'overflow {d["filename"]}: {y}')
 c.setFillColor(MUTED);c.setFont('ResumeSans',7.2);f=d['footer'];fw=width(f,'ResumeSans',7.2);fx=LEFT+CW-fw;c.drawString(fx,26,f);c.linkURL('https://mayconxzdev.github.io/',(fx,24,fx+fw,36),relative=0,thickness=0);c.save();print(path,y)
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for d in (PT, EN):
        generate(d)

if __name__ == '__main__':
    main()
