from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

# Keep this order identical to the recruiter-facing transformation block in
# .github/workflows/pages.yml. The materialized source must match what Pages
# validates and publishes; otherwise the repository can drift from the live site.
TRANSFORMATIONS = [
    'scripts/add_carreirapessoal_home.py',
    'scripts/patch_career_visual.py',
    'scripts/patch_skills_current.py',
    'scripts/patch_portfolio_consistency.py',
    'scripts/normalize_site_chrome.py',
    'scripts/patch_navigation_targets.py',
    'scripts/patch_404_language.py',
    'scripts/normalize_case_sequence.py',
]

for relative in TRANSFORMATIONS:
    print(f'+ {sys.executable} {relative}')
    subprocess.run([sys.executable, relative], cwd=ROOT, check=True)

css = ROOT / 'css' / 'layout-safety.css'
text = css.read_text(encoding='utf-8')
marker = 'Real product evidence used in flagship cards.'
block = '''\n/* Real product evidence used in flagship cards. */\n.portfolio-proof{margin:0;width:100%;display:grid;gap:.55rem}.portfolio-proof img{display:block;width:100%;height:auto;border-radius:16px;border:1px solid rgba(127,127,127,.22);box-shadow:0 18px 54px rgba(0,0,0,.10)}.portfolio-proof figcaption{font-size:.76rem;line-height:1.4;opacity:.72}\n'''
if marker not in text:
    css.write_text(text + block, encoding='utf-8')

print('Portfolio source materialization completed with the same canonical transformations used by Pages.')
