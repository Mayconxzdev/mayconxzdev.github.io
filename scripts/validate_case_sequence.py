from __future__ import annotations

from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]

PT = [
    ('proposta-comercial', 'Proposta Comercial'),
    ('tradutor-documental', 'Tradutor documental offline'),
    ('belarc-inventory', 'Belarc Inventory'),
    ('postagem-redes', 'Postagem Redes'),
    ('producao-operacional', 'Produção Operacional'),
    ('compras-e-cotacoes', 'Compras e Cotações'),
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
    ('commercial-proposal', 'Commercial Proposal'),
    ('offline-document-translator', 'Offline Document Translator'),
    ('belarc-inventory', 'Belarc Inventory'),
    ('postagem-redes', 'Postagem Redes'),
    ('producao-operacional', 'Production Operations'),
    ('purchasing-and-quotes', 'Purchasing and Quotes'),
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


class NextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_next = False
        self.href = ''
        self.text_parts: list[str] = []
        self.capture = False

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == 'section' and 'case-next' in (data.get('class') or '').split():
            self.in_next = True
        elif self.in_next and tag == 'a' and not self.href:
            self.href = data.get('href', '')
            self.capture = True

    def handle_endtag(self, tag):
        if tag == 'a' and self.capture:
            self.capture = False
        elif tag == 'section' and self.in_next:
            self.in_next = False

    def handle_data(self, data):
        if self.capture:
            self.text_parts.append(data)


def check(root: Path, sequence: list[tuple[str, str]], label: str) -> list[str]:
    errors: list[str] = []
    for index, (slug, _name) in enumerate(sequence):
        next_slug, next_name = sequence[(index + 1) % len(sequence)]
        path = root / slug / 'index.html'
        if not path.exists():
            errors.append(f'{label}: missing {slug}')
            continue
        parser = NextParser()
        parser.feed(path.read_text(encoding='utf-8'))
        expected_href = f'../{next_slug}/'
        actual_text = ' '.join(''.join(parser.text_parts).split()).removesuffix(' →').strip()
        if parser.href != expected_href:
            errors.append(f'{label}/{slug}: next href {parser.href!r} != {expected_href!r}')
        if actual_text != next_name:
            errors.append(f'{label}/{slug}: next label {actual_text!r} != {next_name!r}')
    return errors


errors = check(ROOT / 'cases', PT, 'PT') + check(ROOT / 'en' / 'cases', EN, 'EN')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Case browsing sequence validated: {len(PT)} PT + {len(EN)} EN canonical cases in one complete cycle.')
