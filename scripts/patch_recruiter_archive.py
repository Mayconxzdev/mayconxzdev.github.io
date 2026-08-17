from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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
    path.write_text(text, encoding='utf-8')


for page, config in PAGES.items():
    patch(page, config)

print('Recruiter archive patch applied to PT/EN homepages.')
