from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {
    'cases/compass-automation/index.html',
    'cases/portal-vesper/index.html',
    'cases/procureflow/index.html',
    'en/cases/compass-automation/index.html',
    'en/cases/portal-vesper/index.html',
    'en/cases/procureflow/index.html',
}

PT = [
    ('Visão geral', '/#overview'),
    ('Projetos', '/#systems'),
    ('Experiência', '/#experience'),
    ('Resultados', '/#evidence'),
    ('Competências', '/competencias/'),
    ('Contato', '/#contact'),
    ('Currículo', '/assets/cv/Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf'),
]
EN = [
    ('Overview', '/en/#overview'),
    ('Projects', '/en/#systems'),
    ('Experience', '/en/#experience'),
    ('Results', '/en/#evidence'),
    ('Skills', '/en/skills/'),
    ('Contact', '/en/#contact'),
    ('Resume', '/assets/cv/Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf'),
]
GLOBAL_ANCHORS = ['overview', 'systems', 'experience', 'evidence', 'contact']


class NavParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_nav = False
        self.current_href = None
        self.current_text = []
        self.links = []
        self.brand_href = None

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == 'nav' and data.get('id') == 'main-nav':
            self.in_nav = True
        if tag == 'a' and 'brand' in data.get('class', '').split():
            self.brand_href = data.get('href')
        if self.in_nav and tag == 'a':
            self.current_href = data.get('href')
            self.current_text = []

    def handle_data(self, data):
        if self.current_href is not None:
            self.current_text.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.current_href is not None:
            text = ' '.join(''.join(self.current_text).split())
            self.links.append((text, self.current_href))
            self.current_href = None
            self.current_text = []
        if tag == 'nav' and self.in_nav:
            self.in_nav = False


def route_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == 'index.html':
        return '/'
    if rel.endswith('/index.html'):
        return '/' + rel[:-10]
    return '/' + rel


errors = []
checked = 0

# A correct-looking href is not enough: every global hash target must actually
# exist in both language homes or the navigation still fails after clicking.
for surface, home in [('PT', ROOT / 'index.html'), ('EN', ROOT / 'en/index.html')]:
    text = home.read_text(encoding='utf-8')
    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', text, flags=re.I))
    for anchor in GLOBAL_ANCHORS:
        if anchor not in ids:
            errors.append(f'{surface} home: global navigation anchor missing: #{anchor}')

# The 404 pair has its own language route and should advertise that route in
# hreflang metadata as well as in the visible switch.
pt404 = (ROOT / '404.html').read_text(encoding='utf-8')
en404 = (ROOT / 'en/404.html').read_text(encoding='utf-8')
if 'hreflang="en" href="https://mayconxzdev.github.io/en/404.html"' not in pt404:
    errors.append('PT 404: EN hreflang does not point to /en/404.html')
if 'hreflang="pt-BR" href="https://mayconxzdev.github.io/404.html"' not in en404:
    errors.append('EN 404: PT hreflang does not point to /404.html')

for path in ROOT.rglob('*.html'):
    if any(part in {'.git', '.github', 'node_modules', 'artifacts', '.site'} for part in path.parts):
        continue
    rel = path.relative_to(ROOT).as_posix()
    if rel in ALIASES:
        continue
    text = path.read_text(encoding='utf-8')
    if 'data-global-chrome="2026-08"' not in text:
        continue
    route = route_for(path)
    english = route.startswith('/en/')
    parser = NavParser()
    parser.feed(text)
    expected = list(EN if english else PT)
    if english:
        lang = ('PT', '/404.html' if route == '/en/404.html' else ('/' if route == '/en/' else None))
    else:
        lang = ('EN', '/en/404.html' if route == '/404.html' else ('/en/' if route == '/' else None))

    # The language path for case/skills pages is page-specific and validated by validate_site.py.
    if not parser.links:
        errors.append(f'{rel}: navigation links missing')
        continue
    if parser.links[:7] != expected:
        errors.append(f'{rel}: navigation href drift: {parser.links[:7]} != {expected}')
    expected_brand = '/en/' if english else '/'
    if parser.brand_href != expected_brand:
        errors.append(f'{rel}: brand target {parser.brand_href!r} != {expected_brand!r}')
    if lang[1] is not None and (len(parser.links) < 8 or parser.links[7] != lang):
        errors.append(f'{rel}: language switch {parser.links[7] if len(parser.links) > 7 else None} != {lang}')
    checked += 1

if errors:
    raise SystemExit('\n'.join(errors[:100]))
print(f'Navigation labels, href targets, global anchors and 404 hreflang validated on {checked} canonical pages.')
