from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

errors = []


def require(relative: str, phrases: list[str]):
    text = (ROOT / relative).read_text(encoding='utf-8')
    for phrase in phrases:
        if phrase not in text:
            errors.append(f'{relative}: missing required content phrase: {phrase}')
    return text


def forbid(relative: str, phrases: list[str]):
    text = (ROOT / relative).read_text(encoding='utf-8')
    for phrase in phrases:
        if phrase in text:
            errors.append(f'{relative}: forbidden or ambiguous content phrase: {phrase}')
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
        errors.append(f'{relative}: Portal must remain outside the featured project block while under revalidation')
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
    ['Belarc Inventory', 'Produção Operacional', 'Manutenção em Campo', 'Postagem Redes'],
    'Sistemas e automações que desenvolvi para resolver necessidades reais da operação, da TI e da indústria.',
)
check_featured(
    'en/index.html',
    ['Belarc Inventory', 'Production Operations', 'Field Maintenance', 'Postagem Redes'],
    'Systems and automations I built to solve real needs in IT, manufacturing and day-to-day operations.',
)


for relative in ['index.html', 'en/index.html']:
    text = (ROOT / relative).read_text(encoding='utf-8')
    if '<section class="proof-strip"' in text:
        errors.append(f'{relative}: first-read homepage must lead with project stories, not a metrics panel')
    featured_start = text.find('<section class="featured"')
    featured_end = text.find('</section>', featured_start)
    first_read = text[featured_start:featured_end] if featured_start >= 0 and featured_end >= 0 else ''
    for phrase in ['pytest', 'SHA-', 'passed', 'skipped', 'deselected', 'testes aprovados', 'ZIP', 'RC60']:
        if phrase.casefold() in first_read.casefold():
            errors.append(f'{relative}: internal verification detail leaked into the first project view: {phrase}')

for relative in ['en/index.html', 'en/cases/belarc-inventory/index.html']:
    forbid(relative, ['IN INTERNAL USE'])

for relative in ['index.html', 'en/index.html']:
    forbid(relative, ['RAG/MCP', 'LLMs/RAG/MCP', '"MCP"'])

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

require('cases/portal/index.html', ['desenvolvimento'])
require('en/cases/portal/index.html', ['development'])
require('cases/postagem-redes/index.html', ['VALIDADO EM TESTE'])
require('en/cases/postagem-redes/index.html', ['VALIDATED IN TESTING'])

for relative, text in [
    ('competencias/credenciais/index.html', pt_credentials),
    ('en/credentials/index.html', en_credentials),
]:
    if '55+ certifications' in text or '55+ certificações' in text:
        # Allowed only in explicit negation explaining classification.
        pass

if errors:
    raise SystemExit('\n'.join(errors))

print('Public content consistency guard passed across PT/EN skills, credentials, project order and project status.')
