from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {
    'en/cases/compass-automation/index.html',
    'en/cases/portal-vesper/index.html',
    'en/cases/procureflow/index.html',
}

replacements = {
    'href="/#overview"': 'href="/en/#overview"',
    'href="/#systems"': 'href="/en/#systems"',
    'href="/#experience"': 'href="/en/#experience"',
    'href="/#evidence"': 'href="/en/#evidence"',
    'href="/#contact"': 'href="/en/#contact"',
    '<a class="brand" href="/" aria-label="Maycon Ferreira">': '<a class="brand" href="/en/" aria-label="Maycon Ferreira">',
}

for path in (ROOT / 'en').rglob('*.html'):
    rel = path.relative_to(ROOT).as_posix()
    if rel in ALIASES:
        continue
    text = path.read_text(encoding='utf-8')
    if 'data-global-chrome="2026-08"' not in text:
        continue
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

print('English navigation targets now stay inside the English portfolio surface.')
