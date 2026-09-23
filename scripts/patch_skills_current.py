from pathlib import Path

root = Path(__file__).resolve().parents[1]

PAGES = {
    'competencias/index.html': [
        'Power Automate Cloud/Desktop',
        'Power BI',
        'DAX',
        'Power Query',
        'WhatsApp Cloud API',
        'Redis',
        'Prompt Engineering',
        'RAG/grounding',
        'MCP Tools with Agents',
        'DADOS, BI E PRODUTIVIDADE',
        'RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA',
    ],
    'en/skills/index.html': [
        'Power Automate Cloud/Desktop',
        'Power BI',
        'DAX',
        'Power Query',
        'WhatsApp Cloud API',
        'Redis',
        'Prompt Engineering',
        'RAG/grounding',
        'MCP Tools with Agents',
        'DATA, BI AND PRODUCTIVITY',
        'TRACEABILITY, RELIABILITY AND SECURITY',
    ],
}

NORMALIZATIONS = {
    'RASTREABILIDADE, RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA': 'RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA',
    'TRACEABILITY, TRACEABILITY, RELIABILITY AND SECURITY': 'TRACEABILITY, RELIABILITY AND SECURITY',
}

for rel, required in PAGES.items():
    path = root / rel
    text = path.read_text(encoding='utf-8')
    for broken, fixed in NORMALIZATIONS.items():
        text = text.replace(broken, fixed)
    missing = [phrase for phrase in required if phrase not in text]
    if missing:
        raise RuntimeError(f'{rel}: missing current skills evidence: {missing}')
    path.write_text(text, encoding='utf-8')

print('Current PT/EN skills evidence verified idempotently.')
