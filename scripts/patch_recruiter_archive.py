import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_JOURNEY = '''<section class="journey">
      <div class="section-heading"><p>FORMAÇÃO E CREDENCIAIS</p><h2>Base acadêmica e validações práticas alinhadas ao trabalho.</h2><span>Projetos e experiência continuam sendo a prova principal. Aqui aparecem apenas credenciais de maior sinal; o inventário completo separa avaliações práticas, certificados de conclusão, badges e módulos.</span></div>
      <div class="journey-grid"><div class="journey-facts"><p>Tecnólogo em Análise e Desenvolvimento de Sistemas · UNISUAM · conclusão prevista dez. 2026</p><p>Piscine 42 Rio · programa intensivo concluído em jul. 2025</p><p>Inglês básico · leitura independente de documentação técnica</p><p><a class="text-link" href="/competencias/credenciais/">Ver inventário e critérios de credenciais ↗</a></p></div><ol class="cert-list"><li><strong>Microsoft Applied Skills — Agents & MCP</strong><span>2 credenciais · avaliação prática em laboratório</span></li><li><strong>Microsoft Applied Skills — Power Apps</strong><span>1 credencial · Canvas Apps</span></li><li><strong>UiPath Academy — Automation Business Analyst Professional Training</strong><span>business analysis · BPMN · UAT · deployment · hypercare</span></li><li><strong>n8n Academy — N8N102 + N8N103</strong><span>APIs · connected workflows · AI · testing · best practices</span></li><li><strong>Make Academy — AI Agent Builder</strong><span>MCP · segurança · context engineering · assessment</span></li><li><strong>FIRJAN SENAI — Agentes e Automações</strong><span>40h</span></li></ol></div>
    </section>'''

EN_JOURNEY = '''<section class="journey">
      <div class="section-heading"><p>EDUCATION AND CREDENTIALS</p><h2>Academic foundation and practical validation aligned with the work.</h2><span>Projects and experience remain the primary evidence. Only higher-signal credentials appear here; the full inventory separates practical assessments, completion certificates, badges and modules.</span></div>
      <div class="journey-grid"><div class="journey-facts"><p>Technology Degree in Systems Analysis and Development · UNISUAM · expected Dec. 2026</p><p>42 Rio Piscine · intensive program completed Jul. 2025</p><p>Basic English · independently reads technical documentation</p><p><a class="text-link" href="/en/credentials/">View credential inventory and criteria ↗</a></p></div><ol class="cert-list"><li><strong>Microsoft Applied Skills — Agents & MCP</strong><span>2 credentials · hands-on lab assessment</span></li><li><strong>Microsoft Applied Skills — Power Apps</strong><span>1 credential · Canvas Apps</span></li><li><strong>UiPath Academy — Automation Business Analyst Professional Training</strong><span>business analysis · BPMN · UAT · deployment · hypercare</span></li><li><strong>n8n Academy — N8N102 + N8N103</strong><span>APIs · connected workflows · AI · testing · best practices</span></li><li><strong>Make Academy — AI Agent Builder</strong><span>MCP · security · context engineering · assessment</span></li><li><strong>FIRJAN SENAI — AI Agents & Automations</strong><span>40h</span></li></ol></div>
    </section>'''

PAGES = {
    ROOT / 'index.html': {
        'button': (
            '      <button class="archive-expand" type="button" aria-expanded="false" '
            'aria-controls="project-grid" data-collapsed-label="Ver todos os projetos" '
            'data-expanded-label="Mostrar menos projetos">'
            '<span>Ver todos os projetos</span><span aria-hidden="true">↓</span></button>\n'
        ),
        'empty_anchor': '      </div>\n      <p class="empty-state" id="empty-state" hidden>',
        'maintenance_public_old': '<h3>Manutenção em Campo</h3><p>Checklists, evidências, QR Code, histórico e PDF com dados fictícios.</p>',
        'maintenance_public_new': '<h3>Manutenção em Campo</h3><p>Versão pública funcional e sanitizada do domínio de manutenção, com checklists, evidências, QR Code, histórico e PDF usando dados fictícios.</p>',
        'maintenance_private_old': '<h3>Vesper Manutenção</h3><p>Ativos, checklists, evidências e histórico rastreável para a manutenção de 40+ equipamentos.</p>',
        'maintenance_private_new': '<h3>Vesper Manutenção</h3><p>Ativos, checklists, evidências e histórico rastreável para 40+ equipamentos; o laboratório público demonstra o mesmo domínio sem expor dados reais.</p>',
        'journey': PT_JOURNEY,
    },
    ROOT / 'en' / 'index.html': {
        'button': (
            '      <button class="archive-expand" type="button" aria-expanded="false" '
            'aria-controls="project-grid" data-collapsed-label="View all projects" '
            'data-expanded-label="Show fewer projects">'
            '<span>View all projects</span><span aria-hidden="true">↓</span></button>\n'
        ),
        'empty_anchor': '      </div><p class="empty-state" id="empty-state" hidden>',
        'maintenance_public_old': '<h3>Field Maintenance</h3><p>Checklists, evidence, QR codes, history and PDF generation with fictional data.</p>',
        'maintenance_public_new': '<h3>Field Maintenance</h3><p>Functional sanitized public version of the maintenance domain, with checklists, evidence, QR codes, history and PDF generation using fictional data.</p>',
        'maintenance_private_old': '<h3>Vesper Maintenance</h3><p>Assets, checklists, evidence and traceable history for maintenance across 40+ pieces of equipment.</p>',
        'maintenance_private_new': '<h3>Vesper Maintenance</h3><p>Assets, checklists, evidence and traceable history across 40+ pieces of equipment; the public lab demonstrates the same domain without exposing real data.</p>',
        'journey': EN_JOURNEY,
    },
}

STYLE = '<link rel="stylesheet" href="{prefix}css/recruiter-audit.css">'
SCRIPT = '<script defer src="{prefix}js/recruiter-audit.js"></script>'


def patch(path: Path, cfg: dict[str, str]) -> None:
    text = path.read_text(encoding='utf-8')
    prefix = '../' if path.parent.name == 'en' else ''

    style = STYLE.format(prefix=prefix)
    if style not in text:
        text = text.replace('</head>', f'  {style}\n</head>', 1)

    script = SCRIPT.format(prefix=prefix)
    if script not in text:
        text = text.replace('</body>', f'  {script}\n</body>', 1)

    if 'class="archive-expand"' not in text:
        anchor = cfg['empty_anchor']
        if anchor not in text:
            raise SystemExit(f'{path}: archive insertion anchor not found')
        text = text.replace(anchor, f"      </div>\n{cfg['button']}      <p class=\"empty-state\" id=\"empty-state\" hidden>", 1)

    text = text.replace(cfg['maintenance_public_old'], cfg['maintenance_public_new'])
    text = text.replace(cfg['maintenance_private_old'], cfg['maintenance_private_new'])

    text, count = re.subn(r'<section class="journey">.*?</section>', cfg['journey'], text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f'{path}: journey section not found')

    path.write_text(text, encoding='utf-8')


for page, config in PAGES.items():
    patch(page, config)

print('Recruiter archive and selected credentials applied to PT/EN homepages.')