"""Check the four historical public CV URLs after deployment.

They remain stable links but now point to current profiles. This is a smoke test,
not a claim that external applicant tracking systems will accept the documents.
"""
from pathlib import Path
import sys
from pypdf import PdfReader

REQUIRED = {
    'pt-general':['SOLUÇÕES DIGITAIS', 'Produção Operacional', 'Belarc Inventory', 'Hubora', 'Compass UOL', 'Microsoft Applied Skills'],
    'en-general':['DIGITAL SOLUTIONS', 'Production Operations', 'Belarc Inventory', 'Hubora', 'Compass UOL'],
    'pt-ai':['IA APLICADA', 'AGENTES', 'Postagem Redes', 'ArsenalMind', 'Compass UOL'],
    'pt-bi':['ANÁLISE DE DADOS', 'Power BI', 'QuickSight', 'Catálogo Operacional', 'Compass UOL'],
}
BANNED = ('10 mil+', '10k+', '10+ computadores', '20+ profissionais', 'menos de 30', 'under 30 sec')

def norm(s):
    return ' '.join(s.split()).casefold()

def check(name,path):
    reader = PdfReader(str(path))
    if len(reader.pages)!=1:
        raise SystemExit(f'{path}: expected one-page PDF')
    text=norm(reader.pages[0].extract_text() or '')
    if len(text)<1500 or '\ufffd' in text:
        raise SystemExit(f'{path}: insufficient or invalid selectable text')
    for value in REQUIRED[name]:
        if norm(value) not in text:
            raise SystemExit(f'{path}: missing current phrase {value}')
    for value in BANNED:
        if norm(value) in text:
            raise SystemExit(f'{path}: unwanted operational number {value}')
    print('LIVE CV PASS:',name,Path(path).name)

def main():
    if len(sys.argv)!=5:
        raise SystemExit('usage: verify_live_resumes.py <general> <english> <ai> <bi>')
    for key,path in zip(REQUIRED.keys(),sys.argv[1:]):
        check(key,path)

if __name__=='__main__':main()
