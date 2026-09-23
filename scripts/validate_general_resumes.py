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
        'Rust/Axum', 'PowerShell/CIM', 'Git/GitHub Actions', 'Postagem Redes', 'ComprasVesper', 'MCP Tools with Agents',
        'INSTRUTOR DE INFORMÁTICA (FREELANCER)', 'Técnico Júnior em Automação de Processos',
        'Belarc Inventory', 'leitura técnica intermediária',
        'presto suporte a usuários, endpoints Windows e sistemas internos em ambiente industrial',
    ],
    'pt-ai': [
        'ANALISTA DE AUTOMAÇÃO E IA | n8n · Python · LLMs/RAG',
        'Prompt Engineering', 'RAG/LangChain', 'MCP Tools with Agents', 'Supabase/Qdrant',
        'HelpDesk & IT Operations', 'Postagem Redes', '10 mil+',
        'presto suporte a usuários, endpoints Windows e sistemas internos',
    ],
    'pt-bi': [
        'ANALISTA DE AUTOMAÇÃO E BI | Power Automate · Power BI · Python',
        'Power Automate Cloud/Desktop', 'Power BI', 'DAX', 'Power Query',
        'Excel/Google Sheets', 'VBA', 'ETL/Data Lake', 'Catálogo Operacional', 'ComprasVesper',
        'dou suporte a usuários, endpoints Windows e sistemas internos em ambiente industrial',
    ],
    'en-general': [
        'AUTOMATION & AI ANALYST | n8n · Power Automate · Python',
        '10k+', 'Power BI', 'Power Query', 'Prompt Engineering', 'RAG/LangChain',
        'Rust/Axum', 'PowerShell/CIM', 'Git/GitHub Actions', 'Postagem Redes', 'ComprasVesper', 'MCP Tools with Agents',
        'IT INSTRUCTOR (FREELANCE)', 'Junior Process Automation Technician',
        'Belarc Inventory', 'intermediate technical reading',
        'provide hands-on support for users, Windows endpoints and internal systems in an industrial environment',
    ],
}

PARSER_REQUIRED = {
    'pt-general': ['MAYCON FERREIRA', 'Técnico Júnior em Automação de Processos', 'PROPOSTA COMERCIAL', 'presto suporte a usuários, endpoints Windows e sistemas internos em ambiente industrial', 'Postagem Redes', 'ComprasVesper', 'FORMAÇÃO', 'IDIOMAS'],
    'pt-ai': ['MAYCON FERREIRA', 'Técnico Júnior em Automação de Processos', 'presto suporte a usuários, endpoints Windows e sistemas internos', 'HelpDesk & IT Operations', 'Postagem Redes', 'FORMAÇÃO', 'IDIOMAS'],
    'pt-bi': ['MAYCON FERREIRA', 'Técnico Júnior em Automação de Processos', 'dou suporte a usuários, endpoints Windows e sistemas internos em ambiente industrial', 'Catálogo Operacional', 'ComprasVesper', 'FORMAÇÃO', 'IDIOMAS'],
    'en-general': ['MAYCON FERREIRA', 'Junior Process Automation Technician', 'provide hands-on support for users, Windows endpoints and internal systems in an industrial environment', 'Postagem Redes', 'ComprasVesper', 'EDUCATION', 'LANGUAGES'],
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
    return ' '.join(value.split()).casefold()


def check(key: str, path: Path) -> None:
    if not path.exists():
        raise SystemExit(f'Missing resume: {path}')
    reader = PdfReader(str(path))
    if len(reader.pages) != 1:
        raise SystemExit(f'{path.name}: expected 1 page, got {len(reader.pages)}')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    flat = normalize(text)
    if '\ufffd' in text:
        raise SystemExit(f'{path.name}: pypdf extraction contains Unicode replacement characters')
    for phrase in REQUIRED[key]:
        if normalize(phrase) not in flat:
            raise SystemExit(f'{path.name}: missing required text: {phrase}')

    # Check semantic extraction with a second independent PDF parser and ensure
    # that ATS-relevant sections and project names remain present and ordered.
    doc = fitz.open(path)
    fitz_text = '\n'.join(page.get_text('text') for page in doc)
    doc.close()
    fitz_flat = normalize(fitz_text)
    if '\ufffd' in fitz_text:
        raise SystemExit(f'{path.name}: PyMuPDF extraction contains Unicode replacement characters')
    for phrase in PARSER_REQUIRED[key]:
        if normalize(phrase) not in fitz_flat:
            raise SystemExit(f'{path.name}: PyMuPDF extraction is missing required text: {phrase}')
    for before, after in zip(PARSER_REQUIRED[key], PARSER_REQUIRED[key][1:]):
        if fitz_flat.index(normalize(before)) > fitz_flat.index(normalize(after)):
            raise SystemExit(f'{path.name}: PyMuPDF extraction order drifted: {before} before {after}')
    if len(fitz_text.strip()) < 2200:
        raise SystemExit(f'{path.name}: PyMuPDF extracted text unexpectedly short')
    for phrase in FORBIDDEN:
        if normalize(phrase) in flat:
            raise SystemExit(f'{path.name}: forbidden text found: {phrase}')
    for contact in VISIBLE_CONTACTS:
        if normalize(contact) not in flat:
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
