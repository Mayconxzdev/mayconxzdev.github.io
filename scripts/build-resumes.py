"""Build six factual, single-column V15 resumes and their historical aliases.

Use the installed document-toolkit Python environment. No office conversion,
network calls or source-repository mutation. Requires reportlab/pypdf/pypdfium2.
"""
from pathlib import Path
import argparse,hashlib,json,os,shutil
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
import pypdfium2 as pdfium

SITE=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser()
parser.add_argument('--content',type=Path,default=Path(__file__).with_name('resumes-content.json'))
parser.add_argument('--evidence',type=Path,default=SITE/'evidence/refinement/cv')
parser.add_argument('--output-dir',type=Path,default=SITE/'public/assets/cv')
args=parser.parse_args()
data=json.loads(args.content.read_text(encoding='utf8'))
evidence=args.evidence.resolve();evidence.mkdir(parents=True,exist_ok=True)
target=args.output_dir.resolve();target.mkdir(parents=True,exist_ok=True);stage=evidence/'staged';stage.mkdir(exist_ok=True)
fontdir=Path(os.environ.get('RESUME_FONT_DIR','C:/Windows/Fonts'))
regular,bold=fontdir/'arial.ttf',fontdir/'arialbd.ttf'
if regular.exists() and bold.exists():
 pdfmetrics.registerFont(TTFont('ResumeSans',str(regular)))
 pdfmetrics.registerFont(TTFont('ResumeSans-Bold',str(bold)))
 pdfmetrics.registerFontFamily('ResumeSans',normal='ResumeSans',bold='ResumeSans-Bold',italic='ResumeSans',boldItalic='ResumeSans-Bold')
 face='ResumeSans';heavy='ResumeSans-Bold'
else:face='Helvetica';heavy='Helvetica-Bold'
ink=HexColor('#172832');blue=HexColor('#174fca');muted=HexColor('#405460')
body=ParagraphStyle('body',fontName=face,fontSize=10.55,leading=14.25,textColor=ink,spaceAfter=6)
small=ParagraphStyle('small',parent=body,fontSize=9.3,leading=12.4,textColor=muted,spaceAfter=4)
section=ParagraphStyle('section',parent=body,fontName=heavy,fontSize=10.75,leading=14.2,textColor=blue,spaceBefore=11,spaceAfter=6)
name=ParagraphStyle('name',parent=body,fontName=heavy,fontSize=23,leading=26,spaceAfter=3)
title=ParagraphStyle('title',parent=body,fontName=heavy,fontSize=10.5,leading=13.2,textColor=blue,spaceAfter=5)
bullet=ParagraphStyle('bullet',parent=body,leftIndent=11,firstLineIndent=-10,spaceAfter=5)
def para(s,style=body):return Paragraph(s,style)
def link(text,url):return f'<link href="{escape(url)}" color="#174fca">{escape(text)}</link>'
def project(p):
 label=link(p['name'],p['url']) if p.get('url') else '<b>'+escape(p['name'])+'</b>'
 return para(label+' — '+escape(p['text']))
person=data['person'];shared=data['shared'];role=shared['currentRole'];results=[]
for cv in data['resumes']:
 en=cv.get('lang')=='en';flow=[]
 flow.extend([para(escape(person['name']),name),para(escape(cv['title']),title)])
 contact=(person['locationEn'] if en else person['location'])+' · '+link(person['phoneEn'] if en else person['phone'],person['phoneLink'])+' · '+link(person['email'],'mailto:'+person['email'])
 flow.append(para(contact,small))
 # Visible URLs remain useful when a parser ignores link annotations.
 profile_links=[link(person[k].removeprefix('https://').removeprefix('www.').rstrip('/'),person[k]) for k in ['github','portfolio','linkedin']]
 flow.append(para('  ·  '.join(profile_links),small))
 def heading(pt,english):flow.append(para(english if en else pt,section))
 heading('PERFIL','SUMMARY');flow.append(para(escape(cv['summary'])))
 heading('EXPERIÊNCIA','EXPERIENCE')
 current='<b>'+escape(role['organization'])+' · '+escape(role['titleEn'] if en else role['titlePt'])+'</b> | '+escape(role['periodEn'] if en else role['periodPt'])
 flow.append(para(current))
 for text in cv['current']:flow.append(para('• '+text,bullet))
 if en:
  for key in ['supportEn','compassEn','instructorEn']:flow.append(para(shared[key]))
 else:
  for key in ['support','compass','instructor']:flow.append(para(shared[key]))
 heading('PROJETOS SELECIONADOS','SELECTED PROJECTS')
 for p in cv['projects']:flow.append(project(p))
 heading('COMPETÊNCIAS','SKILLS');flow.append(para(cv['skills']))
 heading('FORMAÇÃO','EDUCATION')
 for s in cv.get('education',shared['education']):flow.append(para(s))
 flow.append(para(cv['credentials']))
 flow.append(para(cv.get('languages',shared['languages'])))
 output=stage/cv['file']
 document=SimpleDocTemplate(str(output),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=38,bottomMargin=32,title=person['name']+' — '+cv['title'],author=person['name'],subject=cv['title'],pageCompression=1)
 document.build(flow)
 reader=PdfReader(output);assert len(reader.pages)==1,(cv['id'],len(reader.pages),'Resume overflow; edit content, do not shrink indiscriminately')
 text=reader.pages[0].extract_text();assert 'Maycon Ferreira' in text and len(text)>1200
 links=[]
 for annot in reader.pages[0].get('/Annots',[]):
  uri=annot.get_object().get('/A',{}).get('/URI')
  if uri:links.append(str(uri))
 if cv['id'] in ['general_pt','creative_pt','general_en','creative_en']:
  assert 'ZERO21FOTOS' in text and 'https://zero21fotos.com.br/' in links
 if cv['id'] in ['agents_pt','agents_en']:
  assert 'Postagem Redes' in text and 'https://github.com/Mayconxzdev/PostagemRedes' in links
  assert 'Mala Direta' in text and 'https://github.com/Mayconxzdev/MalaDireta' in links
  assert 'n8n' in text and 'MCP' in text
 if en:assert '+55 21 96481-0480' in text
 render=evidence/cv['id'];render.mkdir(exist_ok=True)
 pdfium.PdfDocument(output)[0].render(scale=1.6).to_pil().save(render/'page-1.png')
 (render/'text.txt').write_text(text,encoding='utf8')
 results.append({'id':cv['id'],'file':cv['file'],'pages':1,'bytes':output.stat().st_size,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'links':links,'aliases':cv.get('aliases',[]),'textCharacters':len(text),'tagged':bool(reader.trailer['/Root'].get('/StructTreeRoot'))})
# Only replace current files after every generated version passed structural checks.
for row in results:
 shutil.copy2(stage/row['file'],target/row['file'])
 for alias in row['aliases']:shutil.copy2(stage/row['file'],target/alias)
(evidence/'verification.json').write_text(json.dumps({'version':data['version'],'method':'ReportLab generation; pypdf page/text/link assertions; pypdfium2 render. Visual inspection must be recorded separately. Not an ATS submission or PDF/UA certificate.','font':face,'resumes':results,'uniqueResumes':len(results),'currentPlusAliases':sum(1+len(r['aliases']) for r in results)},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'resumes':len(results),'pages':sum(x['pages'] for x in results),'filesWithAliases':sum(1+len(r['aliases']) for r in results),'evidence':str(evidence)},ensure_ascii=True))
