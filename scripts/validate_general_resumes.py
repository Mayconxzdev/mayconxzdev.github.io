from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / 'assets' / 'cv'

FILES = {
    'pt': CV / 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
    'en': CV / 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
}

REQUIRED = {
    'pt': [
        'ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES',
        '10 mil+',
        'Power Automate',
        'BPMN',
        'MCP',
        'LangGraph/CrewAI',
        'CarreiraPessoal',
        'Catálogo Operacional',
        'CURSOS E CERTIFICAÇÕES',
        'Técnico Júnior em Automação de Processos',
    ],
    'en': [
        'AI, AUTOMATION & INTEGRATIONS ANALYST',
        '10k+',
        'Power Automate',
        'BPMN',
        'MCP',
        'LangGraph/CrewAI',
        'CarreiraPessoal',
        'Operational Catalog',
        'COURSES & CREDENTIALS',
        'Junior Process Automation Technician',
    ],
}

FORBIDDEN = {
    'pt': ['(cargo formal)', 'Central ISO:</b>'],
    'en': ['(formal role)', 'Central ISO:</b>'],
}


def check(lang, path):
    if not path.exists():
        raise SystemExit(f'Missing resume: {path}')
    reader = PdfReader(str(path))
    if len(reader.pages) != 1:
        raise SystemExit(f'{path.name}: expected 1 page, got {len(reader.pages)}')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    for needle in REQUIRED[lang]:
        if needle not in text:
            raise SystemExit(f'{path.name}: missing required text: {needle}')
    for needle in FORBIDDEN[lang]:
        if needle in text:
            raise SystemExit(f'{path.name}: forbidden stale text: {needle}')
    if len(text.strip()) < 2500:
        raise SystemExit(f'{path.name}: extracted text unexpectedly short')
    print(f'OK {path.name}: 1 page, {len(text)} extracted chars')


for lang, path in FILES.items():
    check(lang, path)
