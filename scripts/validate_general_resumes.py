from pathlib import Path

import fitz
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / 'assets' / 'cv'

FILES = {
    'pt-general': CV / 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
    'pt-ai': CV / 'Maycon_Ferreira_Automacao_IA_n8n_Python_LLMs.pdf',
    'pt-bi': CV / 'Maycon_Ferreira_Automacao_BI_Power_Automate_Power_BI.pdf',
    'en-general': CV / 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
}

REQUIRED = {
    'pt-general': [
        'ANALISTA DE AUTOMAÇÃO E IA | n8n · Power Automate · Python',
        '10 mil+', 'Power BI', 'Power Query', 'Prompt Engineering', 'RAG/LangChain',
        'WhatsApp Cloud API', 'PostgreSQL/Redis', 'Mala Direta', 'HelpDesk & IT Operations',
        'INSTRUTOR DE INFORMÁTICA (FREELANCER)', 'Técnico Júnior em Automação de Processos',
        'leitura técnica intermediária',
    ],
    'pt-ai': [
        'ANALISTA DE AUTOMAÇÃO E IA | n8n · Python · LLMs/RAG',
        'Prompt Engineering', 'RAG/LangChain', 'MCP', 'Supabase/Qdrant',
        'HelpDesk & IT Operations', 'Postagem Redes', '10 mil+',
    ],
    'pt-bi': [
        'ANALISTA DE AUTOMAÇÃO E BI | Power Automate · Power BI · Python',
        'Power Automate Cloud/Desktop', 'Power BI', 'DAX', 'Power Query',
        'Excel/Google Sheets', 'VBA', 'ETL/Data Lake', 'Mala Direta', 'Catálogo Operacional',
    ],
    'en-general': [
        'AUTOMATION & AI ANALYST | n8n · Power Automate · Python',
        '10k+', 'Power BI', 'Power Query', 'Prompt Engineering', 'RAG/LangChain',
        'WhatsApp Cloud API', 'PostgreSQL/Redis', 'Mala Direta', 'HelpDesk & IT Operations',
        'IT INSTRUCTOR (FREELANCE)', 'Junior Process Automation Technician',
        'intermediate technical reading',
    ],
}

FORBIDDEN = [
    '(cargo formal)', '(formal role)', '55 certificações', '55 certifications',
    'Automation Business Analyst Associate Training',
    'UiPath Certified Automation Business Analyst Professional',
    'LangGraph/CrewAI', 'Kafka', 'RabbitMQ', 'ROI',
    '12 dias', '12 days', 'menos de 4 horas', 'less than 4 hours',
]

VISIBLE_CONTACTS = {
    'mayconxz00dev@gmail.com',
    'linkedin.com/in/maycon-ferreira-7bb870231',
    'github.com/Mayconxzdev',
    'mayconxzdev.github.io',
}

EXPECTED_URIS = {
    'tel:+5521964810480',
    'mailto:mayconxz00dev@gmail.com',
    'https://www.linkedin.com/in/maycon-ferreira-7bb870231/',
    'https://github.com/Mayconxzdev',
    'https://mayconxzdev.github.io/',
}


def normalize(value: str) -> str:
    return ' '.join(value.split())


def check(key: str, path: Path) -> None:
    if not path.exists():
        raise SystemExit(f'Missing resume: {path}')
    reader = PdfReader(str(path))
    if len(reader.pages) != 1:
        raise SystemExit(f'{path.name}: expected 1 page, got {len(reader.pages)}')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    flat = normalize(text)
    for phrase in REQUIRED[key]:
        if normalize(phrase) not in flat:
            raise SystemExit(f'{path.name}: missing required text: {phrase}')
    for phrase in FORBIDDEN:
        if normalize(phrase) in flat:
            raise SystemExit(f'{path.name}: forbidden text found: {phrase}')
    for contact in VISIBLE_CONTACTS:
        if contact not in flat:
            raise SystemExit(f'{path.name}: ATS-visible contact missing: {contact}')
    if len(text.strip()) < 2200:
        raise SystemExit(f'{path.name}: extracted text unexpectedly short')

    doc = fitz.open(path)
    links = {item.get('uri') for item in doc[0].get_links() if item.get('uri')}
    doc.close()
    missing = EXPECTED_URIS - links
    if missing:
        raise SystemExit(f'{path.name}: missing clickable contact links: {sorted(missing)}')

    print(f'OK {path.name}: one page, {len(text)} chars, ATS contacts and links verified')


for key, path in FILES.items():
    check(key, path)
