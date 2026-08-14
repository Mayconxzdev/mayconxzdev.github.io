from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pt = ROOT / '404.html'
text = pt.read_text(encoding='utf-8')
text = text.replace('class="lang-link" href="/en/"', 'class="lang-link" href="/en/404.html"')
pt.write_text(text, encoding='utf-8')
print('PT/EN 404 language routing synchronized.')
