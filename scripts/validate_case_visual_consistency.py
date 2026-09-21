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

errors = []
checked = 0

for base in (ROOT / 'cases', ROOT / 'en' / 'cases'):
    for page in sorted(base.glob('*/index.html')):
        rel = page.relative_to(ROOT).as_posix()
        if rel in ALIASES:
            continue
        checked += 1
        text = page.read_text(encoding='utf-8')

        required = [
            'class="case-body',
            'class="site-header"',
            'data-global-chrome="2026-08"',
            'id="main"',
            'class="case-page"',
            'class="case-hero"',
            'class="case-identity"',
            'class="site-footer"',
            'data-global-footer="2026-08"',
            'css/styles.css',
            'css/layout-safety.css',
            'js/site.js',
        ]
        for needle in required:
            if needle not in text:
                errors.append(f'{rel}: missing shared visual primitive: {needle}')

        # Case pages should inherit the single portfolio design system. Large local
        # style blocks are a regression because they can silently change theme,
        # spacing, navigation behavior and mobile layout for one project only.
        if re.search(r'<style\b', text, flags=re.I):
            errors.append(f'{rel}: contains a page-local <style> block; move styling to the shared design system')

        # A project hero must expose either a visual or an explicit text-only proof
        # block. Empty framed media is treated as a visual failure.
        image_tags = re.findall(r'<img\b[^>]*>', text, flags=re.I)
        for tag in image_tags:
            if not re.search(r'\bsrc=["\'][^"\']+["\']', tag, flags=re.I):
                errors.append(f'{rel}: image without src: {tag[:120]}')
            if not re.search(r'\balt=["\'][^"\']+["\']', tag, flags=re.I):
                errors.append(f'{rel}: image without meaningful alt text: {tag[:120]}')

if checked < 20:
    errors.append(f'Expected a broad case audit; only {checked} canonical cases were checked')

if errors:
    raise SystemExit('\n'.join(errors))

print(f'Case visual consistency passed for {checked} canonical PT/EN case pages.')
