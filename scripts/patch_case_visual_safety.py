from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    'cases/producao-operacional/index.html': [
        ('<h1>Produção Operacional</h1>', '<h1>Produção<br>Operacional</h1>'),
    ],
    'en/cases/producao-operacional/index.html': [
        ('<h1>Production Operations</h1>', '<h1>Production<br>Operations</h1>'),
    ],
    'cases/carreira-pessoal/index.html': [
        ('<h1>CarreiraPessoal</h1>', '<h1>Carreira<wbr>Pessoal</h1>'),
    ],
    'en/cases/career-personal/index.html': [
        ('<h1>CarreiraPessoal</h1>', '<h1>Carreira<wbr>Pessoal</h1>'),
    ],
}

for relative, pairs in REPLACEMENTS.items():
    path = ROOT / relative
    text = path.read_text(encoding='utf-8')
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new, 1)
    path.write_text(text, encoding='utf-8')

css = ROOT / 'css' / 'layout-safety.css'
text = css.read_text(encoding='utf-8')
marker = '/* Case title wrapping: prefer semantic breaks over mid-word fragmentation. */'
block = '''\n/* Case title wrapping: prefer semantic breaks over mid-word fragmentation. */\n.case-identity h1{overflow-wrap:normal;word-break:normal;hyphens:none;text-wrap:balance}\n.case-identity h1 wbr{display:inline}\n'''
if marker not in text:
    css.write_text(text.rstrip() + '\n' + block, encoding='utf-8')

print('Case title wrapping normalized without arbitrary mid-word breaks.')
