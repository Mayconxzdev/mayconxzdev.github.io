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
    'Automação, IA, integrações e processos aplicados em projetos reais.',
    'BPMN',
    'RAG/grounding',
    'Power Automate/Make/Zapier/CRM (uso contextual)',
    'não as apresento no mesmo nível de profundidade do meu trabalho com n8n, Python e APIs',
    'RASTREABILIDADE, CONFIABILIDADE E SEGURANÇA',
])
for phrase in [
    'RASTREABILIDADE, RASTREABILIDADE',
    'CONFIABILIDADE, CONFIABILIDADE',
    'SEGURANÇA, SEGURANÇA',
    'Meu núcleo é n8n self-hosted, mas também uso Power Automate',
]:
    if phrase in pt_skills:
        errors.append(f'competencias/index.html: duplicated or depth-ambiguous phrase: {phrase}')

en_skills = require('en/skills/index.html', [
    'Automation, AI, integrations and processes applied in real projects.',
    'BPMN',
    'RAG/grounding',
    'Power Automate/Make/Zapier/CRM (contextual use)',
    'I do not present them at the same depth as my work with n8n, Python and APIs',
    'TRACEABILITY, RELIABILITY AND SECURITY',
])
for phrase in [
    'TRACEABILITY, TRACEABILITY',
    'RELIABILITY, RELIABILITY',
    'SECURITY, SECURITY',
    'My core platform is self-hosted n8n, but I also use Power Automate',
]:
    if phrase in en_skills:
        errors.append(f'en/skills/index.html: duplicated or depth-ambiguous phrase: {phrase}')


def check_featured(relative: str, expected_titles: list[str], architecture_phrase: str):
    text = require(relative, ['data-project="carreira-pessoal"', architecture_phrase])
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
    ['Mala Direta', 'Produção Operacional', 'Vesper Propostas', 'CarreiraPessoal', 'Catálogo Operacional de Compras', 'Postagem Redes'],
    'arquitetura de sistemas',
)
check_featured(
    'en/index.html',
    ['Mala Direta', 'Produção Operacional', 'Vesper Propostas', 'CarreiraPessoal', 'Operational Procurement Catalog', 'Postagem Redes'],
    'systems architecture',
)

career = require('docs/CAREER_EVIDENCE.md', [
    'Ferramentas complementares / contextuais',
    'Vocabulário de mercado — auditoria 16/08/2026',
    'Não reivindicar sem evidência suficiente',
    'Power Automate',
    'Process Mining',
])
if 'Portal** permanece' not in career:
    errors.append('docs/CAREER_EVIDENCE.md: Portal status boundary is missing')

if errors:
    raise SystemExit('\n'.join(errors))

print('Recruiter consistency guard passed across PT/EN skills, flagship order and canonical evidence.')
