from pathlib import Path

import fitz
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / 'assets' / 'cv'

FILES = {
    'pt': CV / 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
    'en': CV / 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
}

REQUIRED = {
    'pt': [
        'ANALISTA DE AUTOMAÇÃO E IA | n8n · Python · APIs',
        'RESUMO PROFISSIONAL',
        'COMPETÊNCIAS TÉCNICAS',
        'EXPERIÊNCIA PROFISSIONAL',
        'CREDENCIAIS SELECIONADAS',
        '10 mil+',
        'n8n self-hosted',
        'Python',
        'FastAPI',
        'APIs REST',
        'SMTP/IMAP',
        'JSON',
        'webhooks',
        'OAuth 2.0',
        'SQL',
        'PostgreSQL',
        'Docker',
        'Power Automate/Power Apps',
        'BPMN',
        'AS-IS/TO-BE',
        'levantamento de requisitos',
        'testes/UAT',
        'IA generativa/LLMs',
        'APIs de LLM',
        'agentes de IA',
        'RAG/grounding',
        'LangChain',
        'human-in-the-loop',
        'evals',
        'tratamento de erros',
        'retries',
        'idempotência',
        'HelpDesk',
        '11 usuários',
        'CarreiraPessoal',
        '283 testes Python',
        '102 famílias ATS',
        '11 coletores diretos',
        'Postagem Redes',
        'Tecnólogo em Análise e Desenvolvimento de Sistemas',
        'Microsoft Applied Skills',
        'Microsoft Foundry',
        'MCP',
        'Automation Business Analyst Professional Training',
        'N8N102',
        'N8N103',
        'AI Agent Builder',
        'Técnico Júnior em Automação de Processos',
    ],
    'en': [
        'AUTOMATION & AI ANALYST | n8n · Python · APIs',
        'PROFESSIONAL SUMMARY',
        'TECHNICAL SKILLS',
        'PROFESSIONAL EXPERIENCE',
        'SELECTED CREDENTIALS',
        '10k+',
        'self-hosted n8n',
        'Python',
        'FastAPI',
        'REST/JSON APIs',
        'SMTP/IMAP',
        'JSON',
        'webhooks',
        'OAuth 2.0',
        'SQL',
        'PostgreSQL',
        'Docker',
        'Power Automate/Power Apps',
        'BPMN',
        'AS-IS/TO-BE',
        'requirements discovery',
        'testing/UAT',
        'generative AI/LLMs',
        'LLM APIs',
        'AI agents',
        'RAG/grounding',
        'LangChain',
        'human-in-the-loop',
        'evals',
        'error handling',
        'retries',
        'idempotency',
        'HelpDesk',
        '11 users',
        'CarreiraPessoal',
        '283 Python tests',
        '102 ATS role families',
        '11 direct collectors',
        'Postagem Redes',
        'Technology Degree in Systems Analysis and Development',
        'Microsoft Applied Skills',
        'Microsoft Foundry',
        'MCP',
        'Automation Business Analyst Professional Training',
        'N8N102',
        'N8N103',
        'AI Agent Builder',
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
        'Automation Business Analyst Associate Training',
        'UiPath Certified Automation Business Analyst Professional',
        'Process Mining',
        'Kafka',
        'RabbitMQ',
        'ROI',
        'CRM (uso contextual)',
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
        'Automation Business Analyst Associate Training',
        'UiPath Certified Automation Business Analyst Professional',
        'Process Mining',
        'Kafka',
        'RabbitMQ',
        'ROI',
        'CRM (contextual use)',
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


def normalize_text(value: str) -> str:
    return ' '.join(value.split())


def check(lang, path):
    if not path.exists():
        raise SystemExit(f'Missing resume: {path}')
    reader = PdfReader(str(path))
    if len(reader.pages) != 1:
        raise SystemExit(f'{path.name}: expected 1 page, got {len(reader.pages)}')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    normalized = normalize_text(text)
    for needle in REQUIRED[lang]:
        if normalize_text(needle) not in normalized:
            raise SystemExit(f'{path.name}: missing required text: {needle}')
    for needle in FORBIDDEN[lang]:
        if normalize_text(needle) in normalized:
            raise SystemExit(f'{path.name}: forbidden general-resume text: {needle}')
    for contact in VISIBLE_CONTACTS:
        if contact not in normalized:
            raise SystemExit(f'{path.name}: ATS-visible contact missing from extracted text: {contact}')
    if len(text.strip()) < 2600:
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
