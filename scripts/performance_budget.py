from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPLOY_PATHS = ['index.html', '404.html', 'assets', 'cases', 'competencias', 'en', 'css', 'js', 'robots.txt', 'sitemap.xml']
TOTAL_BUDGET = 7 * 1024 * 1024
ASSET_BUDGET = 512 * 1024
HTML_BUDGET = 300 * 1024

files = []
for entry in DEPLOY_PATHS:
    path = ROOT / entry
    if path.is_file():
        files.append(path)
    elif path.is_dir():
        files.extend(item for item in path.rglob('*') if item.is_file())

total = sum(item.stat().st_size for item in files)
errors = []
for item in files:
    size = item.stat().st_size
    rel = item.relative_to(ROOT)
    if item.suffix.lower() == '.html' and size > HTML_BUDGET:
        errors.append(f'{rel}: HTML {size / 1024:.1f} KiB exceeds {HTML_BUDGET / 1024:.0f} KiB')
    if item.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.pdf'} and size > ASSET_BUDGET:
        errors.append(f'{rel}: asset {size / 1024:.1f} KiB exceeds {ASSET_BUDGET / 1024:.0f} KiB')
if total > TOTAL_BUDGET:
    errors.append(f'deployable site: {total / 1024 / 1024:.2f} MiB exceeds {TOTAL_BUDGET / 1024 / 1024:.0f} MiB')

largest = sorted(files, key=lambda item: item.stat().st_size, reverse=True)[:8]
print(f'Deployable size: {total / 1024 / 1024:.2f} MiB across {len(files)} files')
for item in largest:
    print(f'  {item.relative_to(ROOT)}: {item.stat().st_size / 1024:.1f} KiB')

if errors:
    raise SystemExit('\n'.join(f'ERROR: {error}' for error in errors))
print('Static performance budgets passed.')
