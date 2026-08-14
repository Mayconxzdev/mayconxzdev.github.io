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
        'RAG/grounding',
        'agentes de IA',
        'HelpDesk',
        '11 pessoas',
        'CarreiraPessoal',
        '283 testes Python',
        'Catálogo Operacional',
        'Postagem Redes',
        'CURSOS E CERTIFICAÇÕES',
        'Técnico Júnior em Automação de Processos',
    ],
    'en': [
        'AI, AUTOMATION & INTEGRATIONS ANALYST',
        '10k+',
        'Power Automate',
        'BPMN',
        'RAG/grounding',
        'AI agents',
        'HelpDesk',
        '11 people',
        'CarreiraPessoal',
        '283 passing Python tests',
        'Operational Catalog',
        'Social Publishing',
        'COURSES & CREDENTIALS',
        'Junior Process Automation Technician',
    ],
}

FORBIDDEN = {
    'pt': [
        '(cargo formal)',
        'Central ISO:</b>',
        'Portal:</b>',
        'MCP',
        'LangGraph/CrewAI',
        'IA multimodal',
        'Geração de mídia',
    ],
    'en': [
        '(formal role)',
        'Central ISO:</b>',
        'Portal:</b>',
        'MCP',
        'LangGraph/CrewAI',
        'multimodal AI',
        'media generation',
    ],
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
            raise SystemExit(f'{path.name}: forbidden general-resume text: {needle}')
    if len(text.strip()) < 3400:
        raise SystemExit(f'{path.name}: extracted text unexpectedly short')
    print(f'OK {path.name}: 1 page, {len(text)} extracted chars')


for lang, path in FILES.items():
    check(lang, path)
