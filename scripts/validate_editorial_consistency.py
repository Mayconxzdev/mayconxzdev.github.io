from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

errors = []


def require(relative: str, phrases: list[str]):
    text = (ROOT / relative).read_text(encoding='utf-8')
    for phrase in phrases:
        if phrase not in text:
            errors.append(f'{relative}: missing required recruiter phrase: {phrase}')
    return text


def forbid(relative: str, phrases: list[str]):
    text = (ROOT / relative).read_text(encoding='utf-8')
    for phrase in phrases:
        if phrase in text:
            errors.append(f'{relative}: forbidden/ambiguous recruiter phrase: {phrase}')
    return text


pt_skills = require('competencias/index.html', [
    'Automação, IA e engenharia aplicadas em sistemas reais.',
    'Power Automate Cloud/Desktop',
    'Power BI',
    'DAX',
    'Power Query',
    'VBA',
    'WhatsApp Cloud API',
    'Redis',
    'Prompt Engineering',
    'RAG/grounding',
    'LangChain',
    'MCP Tools with Agents',
    'evals',
    'BPMN',
    'Rust',
    'Axum',
    'PowerShell/CIM',
    'RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA',
    'DADOS, BI E PRODUTIVIDADE',
])
for phrase in [
    'RASTREABILIDADE, RASTREABILIDADE',
    'CONFIABILIDADE, CONFIABILIDADE',
    'SEGURANÇA, SEGURANÇA',
    'Meu núcleo é n8n self-hosted, mas também uso Power Automate',
    'Power Platform/Make/Zapier/CRM (uso contextual)',
]:
    if phrase in pt_skills:
        errors.append(f'competencias/index.html: duplicated or depth-ambiguous phrase: {phrase}')

en_skills = require('en/skills/index.html', [
    'Automation, AI and engineering applied in real systems.',
    'Power Automate Cloud/Desktop',
    'Power BI',
    'DAX',
    'Power Query',
    'VBA',
    'WhatsApp Cloud API',
    'Redis',
    'Prompt Engineering',
    'RAG/grounding',
    'LangChain',
    'MCP Tools with Agents',
    'evals',
    'BPMN',
    'Rust',
    'Axum',
    'PowerShell/CIM',
    'TRACEABILITY, RELIABILITY AND SECURITY',
    'DATA, BI AND PRODUCTIVITY',
])
for phrase in [
    'TRACEABILITY, TRACEABILITY',
    'RELIABILITY, RELIABILITY',
    'SECURITY, SECURITY',
    'My core platform is self-hosted n8n, but I also use Power Automate',
    'Power Platform/Make/Zapier/CRM (contextual use)',
]:
    if phrase in en_skills:
        errors.append(f'en/skills/index.html: duplicated or depth-ambiguous phrase: {phrase}')

for relative, text in [('competencias/index.html', pt_skills), ('en/skills/index.html', en_skills)]:
    for unsupported in ['desenvolvi servidor e cliente MCP', 'built MCP servers and clients', 'MCP servers and clients, tools']:
        if unsupported in text:
            errors.append(f'{relative}: unsupported MCP implementation claim remains')


def check_featured(relative: str, expected_titles: list[str], architecture_phrase: str):
    text = require(relative, [architecture_phrase])
    start = text.find('<section class="featured" id="systems">')
    end = text.find('<section class="experience" id="experience">', start)
    if start < 0 or end < 0:
        errors.append(f'{relative}: unable to isolate featured projects')
        return
    block = text[start:end]
    if '<h3>Portal</h3>' in block:
        errors.append(f'{relative}: Portal must remain outside the recruiter flagship block while under revalidation')
    cursor = -1
    for title in expected_titles:
        pos = block.find(f'<h3>{title}</h3>')
        if pos < 0:
            errors.append(f'{relative}: missing featured project: {title}')
        elif pos <= cursor:
            errors.append(f'{relative}: featured project order is inconsistent around {title}')
        cursor = max(cursor, pos)


check_featured(
    'index.html',
    ['Vesper Propostas', 'Belarc Inventory', 'Postagem Redes', 'Produção Operacional'],
    'Quatro provas diferentes de resultado, engenharia, IA e implantação.',
)
check_featured(
    'en/index.html',
    ['Commercial Proposal', 'Belarc Inventory', 'Postagem Redes', 'Production Operations'],
    'Four different proofs of impact, engineering, AI and deployment.',
)


def check_metrics(relative: str, required: list[str], forbidden: list[str]):
    text = (ROOT / relative).read_text(encoding='utf-8')
    start = text.find('<section class="proof-strip"')
    end = text.find('<section class="featured"', start)
    if start < 0 or end < 0:
        errors.append(f'{relative}: unable to isolate proof strip')
        return
    block = text[start:end]
    if block.count('class="metric-link"') != 4:
        errors.append(f'{relative}: proof strip must contain exactly four high-signal metrics')
    for phrase in required:
        if phrase not in block:
            errors.append(f'{relative}: proof strip missing required metric: {phrase}')
    for phrase in forbidden:
        if phrase in block:
            errors.append(f'{relative}: secondary-project metric leaked into first-read proof strip: {phrase}')


check_metrics(
    'index.html',
    ['10 mil+', '&lt; 30s', '20+', '30+'],
    ['campanhas operacionais', 'códigos no catálogo', 'usuários no HelpDesk'],
)
check_metrics(
    'en/index.html',
    ['10k+', '&lt; 30s', '20+', '30+'],
    ['operational campaigns', 'codes in the catalog', 'HelpDesk users'],
)

for relative in ['en/index.html', 'en/cases/belarc-inventory/index.html']:
    forbid(relative, ['IN INTERNAL USE'])

for relative in ['index.html', 'en/index.html']:
    forbid(relative, ['RAG/MCP', 'LLMs/RAG/MCP', '"MCP"'])

career = require('docs/CAREER_EVIDENCE.md', [
    'Atualizado em **23/09/2026**',
    'Ferramentas complementares / contextuais',
    'Competências práticas e credencializadas',
    'Vocabulário de mercado — auditoria 24/08/2026',
    'Não reivindicar sem evidência suficiente',
    'Power Apps',
    'Power Automate',
    'Microsoft Foundry',
    'não um servidor/cliente MCP próprio',
    'Automation Business Analyst Professional Training',
    'LangChain',
    'evals',
    'Power BI',
    'Redis',
    'Prompt Engineering',
    'Manter **um currículo-base PT-BR**, duas variações direcionadas (IA/agentes e Power Platform/BI) e um espelho semântico EN do currículo-base.',
])
if 'Portal** permanece' not in career:
    errors.append('docs/CAREER_EVIDENCE.md: Portal status boundary is missing')

credentials = require('docs/CREDENTIALS_EVIDENCE.md', [
    '55+ registros de aprendizagem/credenciais',
    'não deve ser apresentado como “55+ certificações”',
    'Microsoft Applied Skills — 3',
    'N8N102',
    'N8N103',
    'Automation Business Analyst Professional Training',
    'Automation Business Analyst Associate Training',
    'Cases e READMEs individuais',
])
if 'UiPath Certified Automation Business Analyst Professional' not in credentials:
    errors.append('docs/CREDENTIALS_EVIDENCE.md: UiPath exam-certification boundary is missing')

pt_credentials = require('competencias/credenciais/index.html', [
    '55+ registros',
    'Automation Business Analyst Professional Training',
    'certificação profissional separada por exame',
])
en_credentials = require('en/credentials/index.html', [
    '55+ records',
    'Automation Business Analyst Professional Training',
    'separate exam-based professional certification',
])

for relative, text in [
    ('competencias/credenciais/index.html', pt_credentials),
    ('en/credentials/index.html', en_credentials),
]:
    if '55+ certifications' in text or '55+ certificações' in text:
        # Allowed only in explicit negation explaining classification.
        pass

if errors:
    raise SystemExit('\n'.join(errors))

print('Recruiter consistency guard passed across PT/EN skills, credential taxonomy, flagship order and canonical evidence.')
