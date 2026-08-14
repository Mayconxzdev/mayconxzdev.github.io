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


def assert_order(text: str, labels: list[str], surface: str, errors: list[str]) -> None:
    positions = []
    for label in labels:
        pos = text.find(f'<h3>{label}</h3>')
        if pos < 0:
            errors.append(f'{surface}: missing curated flagship: {label}')
        positions.append(pos)
    if all(pos >= 0 for pos in positions) and positions != sorted(positions):
        errors.append(f'{surface}: flagship order drifted: {labels}')


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

pt_flagships = [
    'Mala Direta',
    'Produção Operacional',
    'Vesper Propostas',
    'CarreiraPessoal',
    'Catálogo Operacional de Compras',
    'Postagem Redes',
]
en_flagships = [
    'Mala Direta',
    'Production Operations',
    'Vesper Propostas',
    'CarreiraPessoal',
    'Operational Procurement Catalog',
    'Postagem Redes',
]
assert_order(home, pt_flagships, 'PT home', errors)
assert_order(en_home, en_flagships, 'EN home', errors)

for text, surface in [(home, 'PT home'), (en_home, 'EN home')]:
    featured_start = text.find('<section class="featured"')
    featured_end = text.find('</section>', featured_start)
    featured = text[featured_start:featured_end] if featured_start >= 0 and featured_end >= 0 else ''
    if '<h3>Portal</h3>' in featured:
        errors.append(f'{surface}: Portal must stay out of the flagship section while in revalidation')
    if 'data-project="portal-archive"' not in text:
        errors.append(f'{surface}: Portal archive status is missing')
    if 'data-project="central-iso"' not in text:
        errors.append(f'{surface}: Central ISO archive status is missing')
    if 'data-project="carreira-pessoal"' not in text:
        errors.append(f'{surface}: CarreiraPessoal flagship marker is missing')

if 'RAG/grounding' not in home or 'RAG/grounding' not in en_home:
    errors.append('home pages must expose RAG/grounding as applied AI evidence')
if 'FastAPI · APIs REST · SQL/PostgreSQL' not in home:
    errors.append('PT home core positioning drifted')
if 'FastAPI · REST APIs · SQL/PostgreSQL' not in en_home:
    errors.append('EN home core positioning drifted')

required_routes = [
    ROOT / 'cases/carreira-pessoal/index.html',
    ROOT / 'en/cases/career-personal/index.html',
    ROOT / 'cases/central-iso/index.html',
    ROOT / 'en/cases/central-iso/index.html',
    ROOT / 'assets/evidence/carreira-overview.webp',
    ROOT / 'assets/evidence/central-iso-overview.webp',
    ROOT / 'assets/cv/Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
    ROOT / 'assets/cv/Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
    ROOT / 'docs/CAREER_EVIDENCE.md',
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

print(
    f'HTML={len(pages)} | active cases PT/EN={len(pt_cases)}/{len(en_cases)} | '
    f'local refs={ref_count} | resume links={resume_links} | curated flagships=6'
)
