from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PT = [
    ('mala-direta', 'Mala Direta'),
    ('producao-operacional', 'Produção Operacional'),
    ('vesper-propostas', 'Proposta Comercial'),
    ('carreira-pessoal', 'CarreiraPessoal'),
    ('catalogo-operacional-compras', 'Catálogo Operacional'),
    ('postagem-redes', 'Postagem Redes'),
    ('helpdesk', 'HelpDesk'),
    ('compras-vesper', 'ComprasVesper'),
    ('vesper-manutencao', 'Vesper Manutenção'),
    ('manutencao-campo', 'Manutenção em Campo'),
    ('sites-industriais', 'Vesper e Vent Rio'),
    ('studiocad', 'StudioCad'),
    ('portal', 'Portal'),
    ('central-iso', 'Central ISO'),
    ('compass', 'Programa Compass UOL'),
    ('portfolio-2026', 'Este portfólio'),
    ('hubora', 'Hubora'),
    ('infinity-engine', 'Vesper Infinity Engine'),
    ('whatsapp', 'Notificações por WhatsApp'),
]

EN = [
    ('mala-direta', 'Mala Direta'),
    ('producao-operacional', 'Production Operations'),
    ('vesper-propostas', 'Commercial Proposal'),
    ('career-personal', 'CarreiraPessoal'),
    ('operational-procurement-catalog', 'Operational Procurement Catalog'),
    ('postagem-redes', 'Social Publishing'),
    ('helpdesk', 'HelpDesk'),
    ('compras-vesper', 'ComprasVesper'),
    ('vesper-manutencao', 'Vesper Maintenance'),
    ('manutencao-campo', 'Field Maintenance'),
    ('sites-industriais', 'Vesper and Vent Rio'),
    ('studiocad', 'StudioCad'),
    ('portal', 'Portal'),
    ('central-iso', 'Central ISO'),
    ('compass', 'Compass UOL Program'),
    ('portfolio-2026', 'This portfolio'),
    ('hubora', 'Hubora'),
    ('infinity-engine', 'Vesper Infinity Engine'),
    ('whatsapp', 'WhatsApp Notifications'),
]

PATTERN = re.compile(
    r'<section class="case-next"><div><span>.*?</span><a href="[^"]+">.*?<span aria-hidden="true">→</span></a></div>'
    r'<a class="button button--primary" href="mailto:mayconxz00dev@gmail.com">(.*?)</a></section>',
    re.S,
)


def normalize(root: Path, sequence: list[tuple[str, str]], english: bool) -> int:
    changed = 0
    for index, (slug, _label) in enumerate(sequence):
        path = root / slug / 'index.html'
        if not path.exists():
            raise RuntimeError(f'Missing canonical case: {path.relative_to(ROOT)}')
        next_slug, next_label = sequence[(index + 1) % len(sequence)]
        text = path.read_text(encoding='utf-8')
        match = PATTERN.search(text)
        if not match:
            raise RuntimeError(f'Missing case-next block: {path.relative_to(ROOT)}')
        contact_label = 'Contact' if english else 'Contato'
        heading = 'Next project' if english else 'Próximo projeto'
        replacement = (
            f'<section class="case-next"><div><span>{heading}</span>'
            f'<a href="../{next_slug}/">{next_label} <span aria-hidden="true">→</span></a></div>'
            f'<a class="button button--primary" href="mailto:mayconxz00dev@gmail.com">{contact_label}</a></section>'
        )
        updated = text[:match.start()] + replacement + text[match.end():]
        if updated != text:
            path.write_text(updated, encoding='utf-8')
            changed += 1
    return changed


pt_changed = normalize(ROOT / 'cases', PT, False)
en_changed = normalize(ROOT / 'en' / 'cases', EN, True)
print(f'Canonical case sequence normalized: PT={pt_changed}, EN={en_changed}, cases={len(PT)} per language.')
