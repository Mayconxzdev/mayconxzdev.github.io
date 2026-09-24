from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PT = [
    ('vesper-propostas', 'Proposta Comercial'),
    ('tradutor-documental', 'Tradutor documental offline'),
    ('belarc-inventory', 'Belarc Inventory'),
    ('postagem-redes', 'Postagem Redes'),
    ('producao-operacional', 'Produção Operacional'),
    ('compras-vesper', 'ComprasVesper'),
    ('hubora', 'Hubora'),
    ('mala-direta', 'Mala Direta'),
    ('helpdesk', 'HelpDesk'),
    ('central-iso', 'Central ISO'),
    ('carreira-pessoal', 'CarreiraPessoal'),
    ('catalogo-operacional-compras', 'Catálogo Operacional'),
    ('manutencao-campo', 'Manutenção em Campo'),
    ('studiocad', 'StudioCad'),
    ('sites-industriais', 'Vesper e Vent Rio'),
    ('compass', 'Programa Compass UOL'),
    ('portal', 'Portal'),
    ('vesper-manutencao', 'Vesper Manutenção'),
    ('infinity-engine', 'Vesper Infinity Engine'),
    ('whatsapp', 'Notificações por WhatsApp'),
    ('portfolio-2026', 'Este portfólio'),
    ('scanner-documentos', 'Scanner de documentos'),
    ('appscontrol', 'Controle de Aplicativos'),
]

EN = [
    ('vesper-propostas', 'Commercial Proposal'),
    ('offline-document-translator', 'Offline Document Translator'),
    ('belarc-inventory', 'Belarc Inventory'),
    ('postagem-redes', 'Postagem Redes'),
    ('producao-operacional', 'Production Operations'),
    ('compras-vesper', 'ComprasVesper'),
    ('hubora', 'Hubora'),
    ('mala-direta', 'Mala Direta'),
    ('helpdesk', 'HelpDesk'),
    ('central-iso', 'Central ISO'),
    ('career-personal', 'CarreiraPessoal'),
    ('operational-procurement-catalog', 'Operational Procurement Catalog'),
    ('manutencao-campo', 'Field Maintenance'),
    ('studiocad', 'StudioCad'),
    ('sites-industriais', 'Vesper and Vent Rio'),
    ('compass', 'Compass UOL Program'),
    ('portal', 'Portal'),
    ('vesper-manutencao', 'Vesper Maintenance'),
    ('infinity-engine', 'Vesper Infinity Engine'),
    ('whatsapp', 'WhatsApp Notifications'),
    ('portfolio-2026', 'This portfolio'),
    ('tablet-document-scanner', 'Tablet Document Scanner'),
    ('appscontrol', 'Application Control'),
]

# Case pages were created across several iterations, so the inner markup may use
# either a plain arrow or a nested aria-hidden span. The section boundary is the
# stable public contract and is safe to replace as a unit.
PATTERN = re.compile(r'<section class="case-next">.*?</section>', re.S)


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
