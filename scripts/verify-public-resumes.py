from pathlib import Path
from pypdf import PdfReader
import json,hashlib,pdfplumber
r=Path(__file__).resolve().parent.parent
m=json.loads((r/'scripts/public-release-manifest.json').read_text(encoding='utf-8'))
d=r/'dist/assets/cv'; results=[]
for c in m['curriculos']:
 f=d/c['file'];b=f.read_bytes();assert hashlib.sha256(b).hexdigest()==c['sha256']
 p=PdfReader(f);assert len(p.pages)==1;page=p.pages[0];t=page.extract_text()
 assert 'Maycon Ferreira' in t and 'UNISUAM' in t and len(t)>1100 and '\ufffd' not in t
 assert abs(float(page.mediabox.width)-595.28)<2
 assert abs(float(page.mediabox.height)-841.89)<2
 with pdfplumber.open(f) as pdf:
  chars=[x for x in pdf.pages[0].chars if x['text'].strip()]
  assert not [x for x in chars if x['x0']<31 or x['x1']>pdf.pages[0].width-31 or x['top']<20 or x['bottom']>pdf.pages[0].height-20]
 links=[str(x.get_object().get('/A',{}).get('/URI','')) for x in page.get('/Annots',[])]
 assert any(x.startswith('mailto:') for x in links) and any(x.startswith('https://github.com/') for x in links)
 results.append({'id':c['id'],'pages':1,'text':len(t),'links':len(links)})
for f,i in m['legacy'].items():
 assert (d/f).read_bytes()==(d/next(x['file'] for x in m['curriculos'] if x['id']==i)).read_bytes()
p=r/'evidence/production';p.mkdir(parents=True,exist_ok=True);(p/'resumes.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print('6 PDFs verified; 19 legacy aliases; selectable text, links and A4 bounds.')
