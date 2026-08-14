from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {'.git', '.github', '.venv', 'node_modules', 'artifacts', '__pycache__'}


class RefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag in {'a', 'link'} and data.get('href'):
            self.refs.append(('href', data['href']))
        if tag in {'img', 'script', 'source'} and data.get('src'):
            self.refs.append(('src', data['src']))


def html_files():
    for path in ROOT.rglob('*.html'):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        yield path


def resolve_local(page: Path, ref: str) -> Path | None:
    if not ref or ref.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:')):
        return None
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc:
        return None
    clean = parts.path
    if not clean:
        return None
    target = (page.parent / clean).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        raise AssertionError(f'{page.relative_to(ROOT)} escapes repository root: {ref}')
    if clean.endswith('/'):
        target = target / 'index.html'
    elif target.is_dir():
        target = target / 'index.html'
    return target


pages = list(html_files())
assert pages, 'No HTML pages found'

errors: list[str] = []
ref_count = 0
resume_links = 0
for page in pages:
    text = page.read_text(encoding='utf-8')
    parser = RefParser()
    try:
        parser.feed(text)
    except Exception as exc:
        errors.append(f'{page.relative_to(ROOT)}: HTML parse error: {exc}')
        continue
    for _, ref in parser.refs:
        ref_count += 1
        if 'assets/cv/' in ref:
            resume_links += 1
        try:
            target = resolve_local(page, ref)
        except AssertionError as exc:
            errors.append(str(exc))
            continue
        if target is not None and not target.exists():
            errors.append(f'{page.relative_to(ROOT)} -> missing local reference: {ref}')

home = (ROOT / 'index.html').read_text(encoding='utf-8')
en_home = (ROOT / 'en' / 'index.html').read_text(encoding='utf-8')
for required in ['Mala Direta', 'Produção Operacional', 'CarreiraPessoal', 'Catálogo Operacional', 'Postagem Redes']:
    if required not in home:
        errors.append(f'PT home missing strategic project: {required}')
for required in ['CarreiraPessoal', 'Production Operations', 'Operational Procurement Catalog']:
    if required not in en_home:
        errors.append(f'EN home missing strategic content: {required}')

required_routes = [
    ROOT / 'cases/carreira-pessoal/index.html',
    ROOT / 'en/cases/career-personal/index.html',
    ROOT / 'cases/central-iso/index.html',
    ROOT / 'en/cases/central-iso/index.html',
    ROOT / 'assets/evidence/carreira-overview.webp',
    ROOT / 'assets/evidence/central-iso-overview.webp',
    ROOT / 'assets/cv/Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
    ROOT / 'assets/cv/Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
]
for route in required_routes:
    if not route.exists():
        errors.append(f'missing strategic route: {route.relative_to(ROOT)}')

pt_cases = list((ROOT / 'cases').glob('*/index.html'))
en_cases = list((ROOT / 'en/cases').glob('*/index.html'))
if len(pt_cases) < 15 or len(en_cases) < 15:
    errors.append(f'unexpectedly low case count: PT={len(pt_cases)}, EN={len(en_cases)}')
if resume_links < 2:
    errors.append('resume links unexpectedly missing')

if errors:
    raise SystemExit('\n'.join(errors[:100]))

print(f'HTML={len(pages)} | active cases PT/EN={len(pt_cases)}/{len(en_cases)} | local refs={ref_count} | resume links={resume_links}')
