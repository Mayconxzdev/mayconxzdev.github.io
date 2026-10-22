"""Resume source of truth for mayconxzdev.github.io — 2026, AI-led delivery.

Reproducible with: pip install reportlab==4.4.9 ; python scripts/generate_resumes_general.py
All metrics are deliberately omitted at the candidate's request.
"""
from __future__ import annotations
from html import escape
from pathlib import Path
import shutil
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'cv'
OUT.mkdir(parents=True, exist_ok=True)
FONTS = Path(reportlab.__file__).parent / 'fonts'
for short, fullname in [('Vera','Vera'),('VeraBd','VeraBd'),('VeraIt','VeraIt'),('VeraBI','VeraBI')]:
    pdfmetrics.registerFont(TTFont(short, str(FONTS / (fullname+'.ttf'))))
pdfmetrics.registerFontFamily('Vera',normal='Vera',bold='VeraBd',italic='VeraIt',boldItalic='VeraBI')
NAVY = colors.HexColor('#17384F')
TEAL = colors.HexColor('#087E86')
GRAY = colors.HexColor('#435766')
LIGHT = colors.HexColor('#BCD6DA')

URLS = {
    'Belarc Inventory': 'https://github.com/Mayconxzdev/Belarc-Inventory',
    'Manutenção em Campo': 'https://github.com/Mayconxzdev/ManutencaoEmCampo',
    'Postagem Redes': 'https://github.com/Mayconxzdev/PostagemRedes',
    'Hubora': 'https://github.com/Mayconxzdev/Hubora',
    'Mala Direta': 'https://github.com/Mayconxzdev/MalaDireta',
    'Catálogo Operacional': 'https://github.com/Mayconxzdev/CatalogoOperacional',
    'CarreiraPessoal': 'https://github.com/Mayconxzdev/CarreiraPessoal',
    'Produção Operacional': 'https://github.com/Mayconxzdev/ProducaoOperacional',
    'Vesper + Vent Rio': 'https://vesper.ind.br/',
    'Compass UOL': 'https://github.com/Mayconxzdev/Estagio-CompassUOL',
}

COMMON_PT = {
    'city': 'Rio de Janeiro, RJ',
    'vesper': 'Vesper Equipamentos EX',
    'role': 'Técnico Júnior em Automação de Processos',
    'date': '2026 - atual',
    'vemser': 'VemSer  |  Assistente de Informática  |  2025',
    'vemser_text': 'Suporte a usuários e computadores, orientação em ferramentas digitais e apoio à operação de TI.',
    'compass': 'Compass UOL  |  Estágio de formação prática em Engenharia de Dados  |  out/2024 - mar/2025',
    'compass_text': 'Em sprints práticas, construí pipeline CSV/API, S3/Lambda, Glue/PySpark e Athena, com dashboard Amazon QuickSight.',
    'teacher': 'Atuação autônoma  |  Instrutor de Informática (desde 2024): aulas de informática e produtividade digital.',
    'education': [
        '<b>UNISUAM</b>  Tecnólogo em Análise e Desenvolvimento de Sistemas | conclusão prevista: dez/2026',
        '<b>42 Rio</b>  Piscine intensiva (2025): C, Linux, Git e resolução de problemas',
    ],
    'languages': 'Português nativo; inglês: leitura técnica intermediária, escrita e conversação básicas.',
}

TRACKS = {
 'general': {
    'file':'Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf',
    'title':'SOLUÇÕES DIGITAIS | AUTOMAÇÃO DE PROCESSOS E IA APLICADA',
    'summary':'Concebo e entrego soluções digitais para operações, TI e comunicação. Transformo necessidades em requisitos, arquitetura e critérios de aceitação; utilizo agentes de IA para acelerar a execução, com revisão técnica, testes e validação humana até a implantação.',
    'vesper_bullets':[
      'Concebi e implantei <b>Produção Operacional</b>, aplicativo Windows para ordens de produção, importação validada, prevenção de duplicidades e acompanhamento fabril.',
      'Defino arquitetura e contratos de dados; orquestro agentes de IA por especificações versionadas, reviso diffs e valido regras, testes e segurança antes de entregar.',
      'Automatizei propostas e documentos com Python, n8n e APIs; criei sites, catálogos industriais e vídeos técnicos com apoio de IA.'
    ],
    'projects':[
      ('Belarc Inventory','Co-desenvolvimento de agente Windows e sistema de inventário de computadores para suporte e operação de TI.'),
      ('Manutenção em Campo','Full-stack React/FastAPI para ordens, QR Code, checklists, evidências e histórico auditável.'),
      ('Postagem Redes','Produção de conteúdo com IA, fontes verificáveis, aprovação humana, APIs e tratamento de falhas.'),
      ('Hubora','Projeto final apresentado na Casa Firjan: aplicação web/PWA com APIs e persistência, na formação de IA de 40h.')
    ],
    'skills':'Especificações e engenharia de contexto; agentes/MCP; revisão de código e testes. Python, SQL, React/TypeScript, n8n, Power Automate, APIs, Excel/Power Query, AWS, Git e Docker.',
    'education_extra':[],
    'credentials':'Microsoft Applied Skills (2026): agentes Microsoft Foundry, integração MCP e Power Apps. SENAI Casa Firjan: Ferramentas de IA, Agentes e Automações (40h).',
 },
 'automation':{
    'file':'Maycon_Ferreira_Automacao_Integracoes.pdf',
    'title':'AUTOMAÇÃO DE PROCESSOS | INTEGRAÇÕES E IA',
    'summary':'Transformo processos em automações confiáveis. Especifico regras, exceções e critérios de aceitação antes de orientar agentes de IA; verifico dados, falhas e resultados com testes e revisão humana.',
    'vesper_bullets':[
      'Estruturei fluxos de propostas, documentos e mensagens com Python, n8n e APIs, validação de entradas, revisão humana e recuperação de falhas.',
      'Especifiquei e implantei Produção Operacional, conectando atividades do escritório ao acompanhamento fabril com prevenção de duplicidades.',
      'Levanto requisitos, orquestro agentes e acompanho testes, implantação, treinamento e sustentação de soluções.'
    ],
    'projects':[
      ('Mala Direta','Campanhas em n8n com fila, deduplicação, revalidação de cancelamento e auditoria por destinatário.'),
      ('Catálogo Operacional','FastAPI e SQLite FTS5 com busca, histórico, revisão otimista, conflitos de edição e backups.'),
      ('Postagem Redes','n8n, APIs Meta e IA com revisão humana, idempotência e isolamento de falhas por rede.')
    ],
    'skills':'Requisitos, especificações, testes, revisão de agentes, logs e tratamento de falhas. n8n, Power Automate, Python, APIs REST, webhooks, OAuth, SQL, Excel/Power Query, Docker e Git.',
    'education_extra':[],
    'credentials':'Microsoft Applied Skills: Power Apps e ferramentas MCP (2026). n8n Academy (N8N102/N8N103); UiPath Automation Business Analyst.'
 },
 'systems':{
    'file':'Maycon_Ferreira_Sistemas_Backend.pdf',
    'title':'DESENVOLVIMENTO DE SISTEMAS | BACKEND E APLICAÇÕES',
    'summary':'Concebo sistemas internos e produtos digitais com arquitetura modular, modelos de dados, APIs e interfaces. Trabalho por especificações e coordeno agentes de IA, preservando revisão de código, testes e responsabilidade técnica.',
    'vesper_bullets':[
      'Arquitetei e implantei Produção Operacional para Windows, com persistência, importação validada e prevenção de duplicidades.',
      'Defino componentes, contratos de API e esquemas de dados; reviso diffs, regras de negócio e testes automatizados.',
      'Desenvolvo ferramentas para manutenção, propostas e suporte, acompanhando a implantação com usuários.'
    ],
    'projects':[
      ('Manutenção em Campo','React e FastAPI com ordens, QR Code, checklists versionados, evidências, histórico e PDFs.'),
      ('Belarc Inventory','Co-desenvolvimento de inventário de estações Windows, agentes e interface de operação de TI.'),
      ('CarreiraPessoal','Aplicação local-first com FastAPI, React e Tauri para oportunidades, evidências e currículos.')
    ],
    'skills':'Arquitetura modular, modelos de dados, APIs, revisão de diffs, testes e CI. Python, FastAPI, SQL/SQLite/PostgreSQL, React/TypeScript, Rust/Tauri, Docker e Git.',
    'education_extra':[],
    'credentials':'Microsoft Applied Skills (2026): agentes Microsoft Foundry, integração MCP e Power Apps.'
 },
 'web':{
    'file':'Maycon_Ferreira_Web_Produtos_Digitais.pdf',
    'title':'DESENVOLVIMENTO WEB | PRODUTOS DIGITAIS E INTERFACES',
    'summary':'Planejo experiências web responsivas, dos requisitos à arquitetura de componentes, publicação e manutenção. Utilizo agentes de IA para acelerar implementação, com revisão técnica, testes e atenção à experiência do usuário.',
    'vesper_bullets':[
      'Planejei, desenvolvi e publiquei os sites Vesper e Vent Rio, com catálogos técnicos, páginas de produtos, responsividade e conteúdo PT/EN.',
      'Estruturei componentes reutilizáveis em React/Vite e interfaces orientadas por dados, com critérios de aceitação e validação técnica.',
      'Integrei interfaces, APIs e serviços; acompanhei deploy, domínio, testes de navegação e manutenção.'
    ],
    'projects':[
      ('Vesper + Vent Rio','Sites industriais publicados, React/Vite, i18n, catálogos orientados a dados e mobile.'),
      ('Hubora','Projeto final Casa Firjan: React/TypeScript/PWA, APIs, Supabase e demonstração pública.'),
      ('Manutenção em Campo','Checklists e QR Code em interface responsiva, com backend FastAPI e histórico auditável.')
    ],
    'skills':'Arquitetura de componentes, UX responsiva, testes e revisão de agentes. React, TypeScript, HTML/CSS, Vite, APIs REST, Supabase, PWA, i18n e Git.',
    'education_extra':[],
    'credentials':'SENAI Casa Firjan: Ferramentas de IA, Agentes e Automações (40h). Microsoft Applied Skills: Power Apps.'
 },
 'ai':{
    'file':'Maycon_Ferreira_IA_Agentes_MCP.pdf',
    'title':'IA APLICADA | AGENTES, MCP, INTEGRAÇÕES E AVALIAÇÃO',
    'summary':'Projeto soluções com IA generativa e agentes, definindo contexto, contratos de saída, integração de ferramentas e critérios de avaliação. Combino inferência local ou em nuvem com governança, testes e revisão humana.',
    'vesper_bullets':[
      'Especifico aplicações de IA para documentos, conteúdo e processos, com saídas estruturadas e revisão humana.',
      'Integro APIs, ferramentas MCP e workflows; avalio modelos locais e em nuvem segundo custo, contexto e privacidade.',
      'Conduzo desenvolvimento assistido por agentes com arquitetura e especificações versionadas, revisão de diffs e testes.'
    ],
    'projects':[
      ('Postagem Redes','IA com grounding, avaliação, revisão humana e integrações para publicação.'),
      ('ArsenalMind','Projeto local de orquestração modular, ferramentas MCP e testes de componentes.'),
      ('CarreiraPessoal','IA opcional para apoio à análise de vagas, com revisão humana de candidaturas.')
    ],
    'skills':'Engenharia de contexto, desenvolvimento orientado por especificações, agentes/MCP, RAG, saídas estruturadas, avaliação, roteamento local/nuvem e revisão humana. Python, Pydantic, n8n, Ollama, APIs de LLMs e Docker.',
    'education_extra':[],
    'credentials':'Microsoft Applied Skills: agentes Microsoft Foundry, ferramentas MCP e Power Apps (2026). Make Academy: AI Agent Builder; SENAI Casa Firjan (40h).'
 },
 'data':{
    'file':'Maycon_Ferreira_Dados_BI.pdf',
    'title':'ANÁLISE DE DADOS E AUTOMAÇÃO | PYTHON, SQL, AWS E BI',
    'summary':'Conecto dados e processos por extração, tratamento, modelagem e análise. Utilizo Python, SQL, AWS e ferramentas de IA para acelerar a entrega, com validação, rastreabilidade e revisão dos resultados.',
    'vesper_bullets':[
      'Desenvolvi sistemas para organizar ordens e informações operacionais, com consultas, histórico e relatórios.',
      'Criei catálogo pesquisável para materiais e compras com FastAPI, SQLite FTS5, prevenção de conflitos e backups.',
      'Automatizo o tratamento de planilhas, documentos e dados com Python, verificando regras e resultados antes da adoção.'
    ],
    'projects':[
      ('Compass UOL','Pipeline de dados AWS: CSV/API, S3/Lambda, Glue/PySpark, modelo dimensional, Athena e dashboard QuickSight.'),
      ('Catálogo Operacional','Busca em SQLite FTS5, histórico de materiais, revisão concorrente e exportação.'),
      ('Brasil às Claras','Protótipo local com APIs públicas oficiais, dados e visualizações informativas.')
    ],
    'skills':'ETL, modelagem, validação de dados, documentação e revisão com IA. Python, Pandas, SQL, AWS S3/Lambda/Glue/Athena/QuickSight, PySpark, Excel/Power Query e Power BI.',
    'education_extra':[],
    'credentials':'Compass UOL: Programa de Bolsas em Engenharia de Dados. Microsoft Applied Skills (2026): agentes Foundry, MCP e Power Apps.'
 },
 'content':{
    'file':'Maycon_Ferreira_Conteudo_Video_IA.pdf',
    'title':'CONTEÚDO DIGITAL E IA | VÍDEO, DESIGN E AUTOMAÇÃO',
    'summary':'Planejo e produzo conteúdo técnico de produtos: pesquisa, roteiro, composição, edição e revisão. Utilizo IA generativa e automação na criação audiovisual e digital, com consistência técnica e visual.',
    'vesper_bullets':[
      'Crio e edito vídeos técnicos industriais, da pesquisa ao roteiro, cenas, edição e revisão assistidas por IA.',
      'Desenvolvi sites e catálogos para Vesper e Vent Rio, convertendo especificações em conteúdo visual e navegação comercial.',
      'Estruturei processos de publicação com IA, fontes verificáveis, revisão humana, APIs e validação de conteúdo.'
    ],
    'projects':[
      ('Conteúdo audiovisual industrial','Vídeos demonstrativos e materiais promocionais para produtos e divulgação técnica.'),
      ('Vesper + Vent Rio','Sites publicados, catálogos digitais, páginas de produto e conteúdo responsivo.'),
      ('Postagem Redes','Painel e workflows de produção, revisão, agendamento e distribuição de conteúdo digital.')
    ],
    'skills':'Roteiro, edição e composição de vídeo, IA generativa visual, revisão técnica, consistência visual e automação editorial. Criação web, catálogos digitais, n8n e APIs.',
    'education_extra':[],
    'credentials':'SENAI Casa Firjan: Ferramentas de IA, Agentes e Automações (40h). Make Academy: AI Agent Builder.'
 }
}

EN = {
  'title': 'DIGITAL SOLUTIONS | PROCESS AUTOMATION AND APPLIED AI',
  'summary': 'I design and deliver digital solutions for operations, IT and communication. I translate needs into requirements, architecture and acceptance criteria; I guide AI agents to accelerate implementation while retaining technical review, testing and human validation.',
  'vesper_bullets': [
    'Designed and rolled out Production Operations, a Windows system for work orders, validated imports, duplicate prevention and factory tracking.',
    'Define architecture and data contracts; guide AI agents through versioned specifications and review diffs, business rules, tests and security.',
    'Automated proposals and documents with Python, n8n and APIs; built industrial websites, catalogs and AI-assisted technical content.'
  ],
  'projects': [
    ('Belarc Inventory', 'Co-development of Windows inventory and IT support application.'),
    ('Field Maintenance', 'React/FastAPI solution for maintenance orders, QR codes, checklists, evidence and history.'),
    ('Social Publishing', 'AI-assisted content workflows, human review, APIs and failure recovery.'),
    ('Hubora', 'Web/PWA project presented at Casa Firjan as part of AI and automation training.')
  ],
  'skills': 'Specification-driven development, context engineering, agents/MCP, code review and tests. Python, SQL, React/TypeScript, n8n, Power Automate, APIs, Excel/Power Query, AWS, Git and Docker.',
  'credentials': 'Microsoft Applied Skills: Foundry agents, MCP integration and Power Apps. SENAI Casa Firjan: AI Tools, Agents and Automation (40h).'
}


def para(style, txt):
    return Paragraph(txt, style)


def styles():
    def ps(name,size,leading,bold=False,color=NAVY,before=0,after=0):
        return ParagraphStyle(name, fontName='VeraBd' if bold else 'Vera',fontSize=size,leading=leading,textColor=color,spaceBefore=before,spaceAfter=after,allowWidows=0,allowOrphans=0)
    return {
      'name':ps('name',20.0,23,True,after=2),
      'title':ps('title',10.35,12,True,TEAL,after=4),
      'contact':ps('contact',8.9,11,color=GRAY,after=4),
      'section':ps('section',10.0,12.0,True,TEAL,before=8,after=2.8),
      'body':ps('body',10.05,13.35,after=3.3),
      'job':ps('job',9.8,12.5,after=3),
      'project':ps('project',9.8,13.0,after=3),
      'footer':ps('footer',9.6,12.65,after=2.1),
    }


def link_text(label,url):
    return f'<link href="{escape(url, quote=True)}" color="#087E86">{escape(label)}</link>'


def build(track='general', lang='pt'):
    data = EN if lang=='en' else TRACKS[track]
    name = ('Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf' if lang=='en' else data['file'])
    s=styles()
    dest=OUT/name
    doc=SimpleDocTemplate(str(dest),pagesize=A4,leftMargin=17*mm,rightMargin=17*mm,topMargin=15*mm,bottomMargin=14*mm, title='Maycon Ferreira - '+data['title'],author='Maycon Ferreira')
    contact_city='Rio de Janeiro, Brazil' if lang=='en' else COMMON_PT['city']
    contact = f'{contact_city}  |  <link href="tel:+5521964810480">(21) 96481-0480</link>  |  <link href="mailto:mayconxz00dev@gmail.com">mayconxz00dev@gmail.com</link><br/>'
    contact += link_text('github.com/Mayconxzdev','https://github.com/Mayconxzdev')+'  |  '+link_text('mayconxzdev.github.io','https://mayconxzdev.github.io/')+'  |  '+link_text('linkedin.com/in/maycon-ferreira-7bb870231','https://www.linkedin.com/in/maycon-ferreira-7bb870231/')
    story=[para(s['name'],'Maycon Ferreira'),para(s['title'],data['title']),para(s['contact'],contact)]
    def sec(pt,en=None):
        story.append(para(s['section'],en if lang=='en' else pt))
        story.append(HRFlowable(width='100%',thickness=0.35,color=LIGHT,spaceBefore=0,spaceAfter=4))
    sec('PERFIL PROFISSIONAL','PROFESSIONAL SUMMARY')
    story.append(para(s['body'],data['summary']))
    sec('EXPERIÊNCIA PROFISSIONAL','EXPERIENCE')
    if lang=='en':
        story.append(para(s['job'],'<b>Vesper Equipamentos EX</b>  |  Junior Process Automation Technician  |  2026 - Present'))
    else:
        story.append(para(s['job'],f'<b>{COMMON_PT["vesper"]}</b>  |  {COMMON_PT["role"]}  |  {COMMON_PT["date"]}'))
    for item in data['vesper_bullets']:
        story.append(para(s['body'],'&#8226;  '+item))
    if lang=='en':
        story.extend([
          para(s['job'],'<b>VemSer</b>  |  IT Assistant  |  2025'),
          para(s['body'],'&#8226;  Provided user support and hands-on assistance with computers and digital tools.'),
          para(s['job'],'<b>Compass UOL</b>  |  Practical Data Engineering Internship/Training  |  Oct/2024 - Mar/2025'),
          para(s['body'],'&#8226;  Built a CSV/API, S3/Lambda, Glue/PySpark and Athena pipeline, with an Amazon QuickSight dashboard.'),
          para(s['body'],'<b>Freelance IT Instructor</b> (since 2024): practical computer and digital productivity lessons.'),
        ])
    else:
        story.extend([
          para(s['job'],'<b>VemSer</b>  |  Assistente de Informática  |  2025'),
          para(s['body'],'&#8226;  '+COMMON_PT['vemser_text']),
          para(s['job'],'<b>Compass UOL</b>  |  Estágio de formação prática em Engenharia de Dados  |  out/2024 - mar/2025'),
          para(s['body'],'&#8226;  '+COMMON_PT['compass_text']),
          para(s['body'],'<b>Atuação autônoma</b>  |  Instrutor de Informática (desde 2024): aulas práticas de informática e produtividade digital.'),
        ])
    sec('PROJETOS SELECIONADOS','SELECTED PROJECTS')
    for label,descr in data['projects']:
        link=URLS.get(label)
        txt=(link_text(label,link) if link else '<b>'+escape(label)+'</b>')+' — '+escape(descr)
        story.append(para(s['project'],txt))
    sec('COMPETÊNCIAS','SKILLS')
    story.append(para(s['body'],data['skills']))
    sec('FORMAÇÃO E CREDENCIAIS','EDUCATION & CREDENTIALS')
    if lang=='en':
        rows=[
          '<b>UNISUAM</b>  Technology Degree in Systems Analysis and Development | expected Dec/2026',
          '<b>42 Rio</b>  Intensive Piscine: C, Linux, Git (2025)',
          '<b>Credentials</b>  '+data['credentials'],
          '<b>Languages</b>  Portuguese native; English intermediate technical reading, basic speaking and writing.'
        ]
    else:
        rows=COMMON_PT['education']+['<b>Certificações</b>  '+data['credentials'],'<b>Idiomas</b>  '+COMMON_PT['languages']]
    for row in rows:story.append(para(s['footer'],row))
    doc.build(story)
    return dest


def run():
    files=[]
    for track in TRACKS:
        files.append(build(track))
    files.append(build('general','en'))
    # Existing inbound links must remain valid and point to current versions.
    aliases={
        'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf':TRACKS['general']['file'],
        'Maycon_Ferreira_Automacao_IA_n8n_Python_LLMs.pdf':TRACKS['ai']['file'],
        'Maycon_Ferreira_Automacao_BI_Power_Automate_Power_BI.pdf':TRACKS['data']['file'],
    }
    for old,source in aliases.items():
        shutil.copy2(OUT/source,OUT/old)
        files.append(OUT/old)
    for p in files:print('RESUME',p.name, p.stat().st_size)


if __name__ == '__main__': run()