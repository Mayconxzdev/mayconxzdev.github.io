from pathlib import Path
from pypdf import PdfReader
import fitz

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
        'uso contextual',
        'BPMN',
        'REST/JSON',
        'RAG/grounding',
        'agentes de IA',
        'gestão de segredos',
        'HelpDesk',
        '11 pessoas',
        'CarreiraPessoal',
        '283 testes Python',
        'Catálogo Operacional',
        'uso diário por 3 pessoas',
        'Postagem Redes',
        'Microsoft Applied Skills',
        'Microsoft Foundry',
        'MCP',
        'Power Apps',
        'N8N102',
        'N8N103',
        'AI Agent Builder',
        'Automation Business Analyst Associate Training',
        'Introdução à LGPD',
        'CREDENCIAIS E FORMAÇÃO COMPLEMENTAR',
        'Técnico Júnior em Automação de Processos',
    ],
    'en': [
        'AI, AUTOMATION & INTEGRATIONS ANALYST',
        '10k+',
        'Power Automate',
        'contextual use',
        'BPMN',
        'REST/JSON',
        'RAG/grounding',
        'AI agents',
        'secret management',
        'HelpDesk',
        '11 people',
        'CarreiraPessoal',
        '283 passing Python tests',
        'Operational Catalog',
        'used daily by 3 people',
        'Social Publishing',
        'Microsoft Applied Skills',
        'Microsoft Foundry',
        'MCP',
        'Power Apps',
        'N8N102',
        'N8N103',
        'AI Agent Builder',
        'Automation Business Analyst Associate Training',
        'LGPD / Data Protection',
        'CREDENTIALS & ADDITIONAL TRAINING',
        'Junior Process Automation Technician',
    ],
}

FORBIDDEN = {
    'pt': [
        '(cargo formal)',
        'Central ISO:</b>',
        'Portal:</b>',
        'LangGraph/CrewAI',
        'IA multimodal',
        'Geração de mídia',
        '158 nós',
        '55 certificações',
    ],
    'en': [
        '(formal role)',
        'Central ISO:</b>',
        'Portal:</b>',
        'LangGraph/CrewAI',
        'multimodal AI',
        'media generation',
        '158 nodes',
        '55 certifications',
    ],
}

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
    for contact in VISIBLE_CONTACTS:
        if contact not in text:
            raise SystemExit(f'{path.name}: ATS-visible contact missing from extracted text: {contact}')
    if len(text.strip()) < 3600:
        raise SystemExit(f'{path.name}: extracted text unexpectedly short')

    doc = fitz.open(path)
    links = {item.get('uri') for item in doc[0].get_links() if item.get('uri')}
    doc.close()
    missing_links = EXPECTED_URIS - links
    if missing_links:
        raise SystemExit(f'{path.name}: missing clickable contact links: {sorted(missing_links)}')

    print(
        f'OK {path.name}: 1 page, {len(text)} extracted chars, '
        f'{len(VISIBLE_CONTACTS)} ATS-visible contacts, {len(EXPECTED_URIS)} clickable contact links'
    )


for lang, path in FILES.items():
    check(lang, path)