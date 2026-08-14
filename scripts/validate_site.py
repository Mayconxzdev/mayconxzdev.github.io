from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from PIL import Image
import xml.etree.ElementTree as ET
import re

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {'.git', '.github', '.venv', 'node_modules', 'artifacts', '__pycache__', '.site'}
ALIASES = {
    'cases/compass-automation/index.html',
    'cases/portal-vesper/index.html',
    'cases/procureflow/index.html',
    'en/cases/compass-automation/index.html',
    'en/cases/portal-vesper/index.html',
    'en/cases/procureflow/index.html',
}

PT_NAV = ['Visão geral', 'Projetos', 'Experiência', 'Resultados', 'Competências', 'Contato', 'Currículo', 'EN']
EN_NAV = ['Overview', 'Projects', 'Experience', 'Results', 'Skills', 'Contact', 'Resume', 'PT']

CASE_EN_SLUG = {
    'carreira-pessoal': 'career-personal',
    'catalogo-operacional-compras': 'operational-procurement-catalog',
}
CASE_PT_SLUG = {v: k for k, v in CASE_EN_SLUG.items()}


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


def route_for(page: Path) -> str:
    rel = page.relative_to(ROOT).as_posix()
    if rel == 'index.html':
        return '/'
    if rel.endswith('/index.html'):
        return '/' + rel[:-10]
    return '/' + rel


def expected_lang_target(route: str, english: bool) -> str:
    if english:
        if route == '/en/':
            return '/'
        if route == '/en/skills/':
            return '/competencias/'
        match = re.fullmatch(r'/en/cases/([^/]+)/', route)
        if match:
            return f"/cases/{CASE_PT_SLUG.get(match.group(1), match.group(1))}/"
        return route.removeprefix('/en') or '/'
    if route == '/':
        return '/en/'
    if route == '/competencias/':
        return '/en/skills/'
    match = re.fullmatch(r'/cases/([^/]+)/', route)
    if match:
        return f"/en/cases/{CASE_EN_SLUG.get(match.group(1), match.group(1))}/"
    return '/en' + route


def resolve_local(page: Path, ref: str) -> Path | None:
    if not ref or ref.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:')):
        return None
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc:
        return None
    clean = parts.path
    if not clean:
        return None
    if clean.startswith('/'):
        target = (ROOT / clean.lstrip('/')).resolve()
    else:
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


def heading_position(text: str, label: str) -> int:
    match = re.search(
        r'<h3\b[^>]*>\s*' + re.escape(label) + r'\s*</h3>',
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return match.start() if match else -1


def has_data_project(text: str, name: str) -> bool:
    return bool(
        re.search(
            r'data-project\s*=\s*["\']' + re.escape(name) + r'["\']',
            text,
            flags=re.IGNORECASE,
        )
    )


def assert_order(text: str, labels: list[str], surface: str, errors: list[str]) -> None:
    positions = []
    for label in labels:
        pos = heading_position(text, label)
        if pos < 0:
            errors.append(f'{surface}: missing curated flagship: {label}')
        positions.append(pos)
    if all(pos >= 0 for pos in positions) and positions != sorted(positions):
        errors.append(f'{surface}: flagship order drifted: {labels}')


def strip_tags(value: str) -> str:
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', value)).strip()


def validate_chrome(page: Path, text: str, errors: list[str]) -> None:
    rel = page.relative_to(ROOT).as_posix()
    if rel in ALIASES:
        return
    route = route_for(page)
    english = route.startswith('/en/')
    expected_nav = EN_NAV if english else PT_NAV

    if 'data-global-chrome="2026-08"' not in text:
        errors.append(f'{rel}: global header marker missing')
    if 'data-global-footer="2026-08"' not in text:
        errors.append(f'{rel}: global footer marker missing')
    for needle in ['id="main-nav"', 'class="menu-button"', 'class="theme-toggle"', 'layout-safety.css', 'js/site.js', 'mf-theme']:
        if needle not in text:
            errors.append(f'{rel}: shared chrome dependency missing: {needle}')

    nav_match = re.search(r'<nav\b[^>]*id=["\']main-nav["\'][^>]*>(.*?)</nav>', text, flags=re.I | re.S)
    if not nav_match:
        errors.append(f'{rel}: #main-nav missing')
        return
    labels = [strip_tags(item) for item in re.findall(r'<a\b[^>]*>(.*?)</a>', nav_match.group(1), flags=re.I | re.S)]
    if labels != expected_nav:
        errors.append(f'{rel}: nav mismatch: {labels} != {expected_nav}')

    lang_match = re.search(r'<a\b[^>]*class=["\'][^"\']*lang-link[^"\']*["\'][^>]*href=["\']([^"\']+)', nav_match.group(1), flags=re.I | re.S)
    if not lang_match:
        lang_match = re.search(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*class=["\'][^"\']*lang-link', nav_match.group(1), flags=re.I | re.S)
    if not lang_match:
        errors.append(f'{rel}: language link missing')
    else:
        expected = expected_lang_target(route, english)
        if lang_match.group(1) != expected:
            errors.append(f'{rel}: language target {lang_match.group(1)} != {expected}')


def validate_visual_asset(path: Path, errors: list[str], checked: set[Path]) -> None:
    if path in checked:
        return
    checked.add(path)
    suffix = path.suffix.lower()
    try:
        if suffix in {'.png', '.jpg', '.jpeg', '.webp'}:
            with Image.open(path) as image:
                image.load()
                if image.width < 2 or image.height < 2:
                    raise ValueError(f'invalid dimensions {image.size}')
        elif suffix == '.svg':
            ET.parse(path)
    except Exception as exc:
        errors.append(f'corrupt or undecodable visual asset {path.relative_to(ROOT)}: {exc}')


pages = list(html_files())
assert pages, 'No HTML pages found'

errors: list[str] = []
ref_count = 0
resume_links = 0
checked_visuals: set[Path] = set()
for page in pages:
    text = page.read_text(encoding='utf-8')
    validate_chrome(page, text, errors)
    parser = RefParser()
    try:
        parser.feed(text)
    except Exception as exc:
        errors.append(f'{page.relative_to(ROOT)}: HTML parse error: {exc}')
        continue
    for kind, ref in parser.refs:
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
        elif target is not None and kind == 'src':
            validate_visual_asset(target, errors, checked_visuals)

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
    if heading_position(featured, 'Portal') >= 0:
        errors.append(f'{surface}: Portal must stay out of the flagship section while in revalidation')
    if not has_data_project(text, 'portal-archive'):
        errors.append(f'{surface}: Portal archive status is missing')
    if not has_data_project(text, 'central-iso'):
        errors.append(f'{surface}: Central ISO archive status is missing')
    if not has_data_project(text, 'carreira-pessoal'):
        errors.append(f'{surface}: CarreiraPessoal flagship marker is missing')

if 'RAG/grounding' not in home or 'RAG/grounding' not in en_home:
    errors.append('home pages must expose RAG/grounding as applied AI evidence')
if 'FastAPI · APIs REST · SQL/PostgreSQL' not in home:
    errors.append('PT home core positioning drifted')
if 'FastAPI · REST APIs · SQL/PostgreSQL' not in en_home:
    errors.append('EN home core positioning drifted')
if 'carreira-overview.webp' in home or 'carreira-overview.webp' in en_home:
    errors.append('home pages still reference the known corrupt CarreiraPessoal WebP')

required_routes = [
    ROOT / 'cases/carreira-pessoal/index.html',
    ROOT / 'en/cases/career-personal/index.html',
    ROOT / 'cases/central-iso/index.html',
    ROOT / 'en/cases/central-iso/index.html',
    ROOT / 'assets/evidence/carreira-product-overview.svg',
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
    raise SystemExit('\n'.join(errors[:150]))

print(
    f'HTML={len(pages)} | active cases PT/EN={len(pt_cases)}/{len(en_cases)} | '
    f'local refs={ref_count} | decoded visuals={len(checked_visuals)} | resume links={resume_links} | '
    f'global chrome consistent on {len(pages)-len(ALIASES)} canonical pages'
)
