from __future__ import annotations

from pathlib import Path
import re
import sys

PT = 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf'
EN = 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf'


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit('usage: version_resume_links.py <site-root> <release-token>')
    root = Path(sys.argv[1]).resolve()
    token = re.sub(r'[^A-Za-z0-9._-]+', '', sys.argv[2])
    if not root.is_dir() or not token:
        raise SystemExit('valid site root and release token are required')

    changed = 0
    for path in root.rglob('*.html'):
        text = path.read_text(encoding='utf-8')
        original = text
        for name in (PT, EN):
            # Replace stable or previously versioned references with the current release token.
            pattern = rf'(/assets/cv/{re.escape(name)})(?:\?v=[A-Za-z0-9._-]+)?'
            text = re.sub(pattern, rf'\1?v={token}', text)
        if text != original:
            path.write_text(text, encoding='utf-8')
            changed += 1

    print(f'Versioned resume links in {changed} HTML files with token {token}.')


if __name__ == '__main__':
    main()
