"""Independently validate canonical V15 resumes and retained legacy URLs."""
from pathlib import Path
import hashlib, html.parser, json, re
import pdfplumber
from pypdf import PdfReader

site = Path(__file__).resolve().parent.parent
studio = site.parent
content = json.loads((site / 'scripts/resumes-content.json').read_text(encoding='utf8'))
expected = {
    'general_pt': 'Maycon_Ferreira_Geral_Automacao_IA_PT.pdf',
    'agents_pt': 'Maycon_Ferreira_Agentes_Automacao_n8n_PT.pdf',
    'creative_pt': 'Maycon_Ferreira_Produtos_Conteudo_IA_PT.pdf',
    'general_en': 'Maycon_Ferreira_General_Automation_AI_EN.pdf',
    'agents_en': 'Maycon_Ferreira_AI_Agents_Automation_n8n_EN.pdf',
    'creative_en': 'Maycon_Ferreira_AI_Digital_Products_Content_EN.pdf',
}
assert len(content['resumes']) == 6
assert {x['id']: x['file'] for x in content['resumes']} == expected
listed = set(re.findall(r'file:\s*"([^"]+\.pdf)"', (site / 'src/data.js').read_text(encoding='utf8')))
assert listed == {expected[x] for x in ('general_pt','agents_pt','creative_pt')}, 'Homepage cards must link to the three current PT resumes'

class PdfLinks(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.hrefs=[]
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href=dict(attrs).get('href','')
            if href.lower().endswith('.pdf'): self.hrefs.append(Path(href).name)

catalog = site / 'public/assets/cv/index.html'
parser=PdfLinks(); parser.feed(catalog.read_text(encoding='utf8'))
assert set(parser.hrefs) == set(expected.values()) and len(parser.hrefs) == 6, 'Static public catalog must expose exactly six canonical files'

alias_targets = {
    'Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf': expected['general_pt'],
    'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf': expected['agents_pt'],
    'Maycon_Ferreira_IA_Agentes_MCP.pdf': expected['agents_pt'],
    'Maycon_Ferreira_Automacao_Integracoes.pdf': expected['agents_pt'],
    'Maycon_Ferreira_Dados_BI.pdf': expected['general_pt'],
    'Maycon_Ferreira_Sistemas_Backend.pdf': expected['general_pt'],
    'Maycon_Ferreira_Web_Produtos_Digitais.pdf': expected['creative_pt'],
    'Maycon_Ferreira_Conteudo_Video_IA.pdf': expected['creative_pt'],
    'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf': expected['general_en'],
}
old_path=studio.parent/'REVISAO_REFERENCIAS_20261024/curriculos.json'
old={x['file']:x for x in json.loads(old_path.read_text(encoding='utf8'))} if old_path.exists() else {}
results=[]
for item in content['resumes']:
    p=site/'public/assets/cv'/item['file']
    reader=PdfReader(p); assert len(reader.pages)==1, (item['id'],'PDF must be one A4 page')
    page=reader.pages[0]
    assert abs(float(page.mediabox.width)-595.276)<1 and abs(float(page.mediabox.height)-841.89)<1, (item['id'],'not A4')
    text=page.extract_text(); assert '\ufffd' not in text
    assert 'Maycon Ferreira' in text and 'UNISUAM' in text
    if item['lang']=='en': assert 'expected completion Dec 2026' in text and '+55 21 96481-0480' in text
    else: assert 'conclusão prevista: dez/2026' in text
    with pdfplumber.open(p) as pdf:
        chars=[c for c in pdf.pages[0].chars if c['text'].strip()]
        assert chars
        outside=[c['text'] for c in chars if c['x0']<34 or c['x1']>pdf.pages[0].width-34 or c['top']<24 or c['bottom']>pdf.pages[0].height-24]
        assert not outside,(item['id'],'characters outside safe margins',outside[:20])
        min_font=min(c['size'] for c in chars)
        body_sizes=[c['size'] for c in chars if c['size']>=10]
        assert min_font>=9 and body_sizes and min(body_sizes)>=10.5,(item['id'],min_font)
        extent={'top':round(min(c['top'] for c in chars),2),'bottom':round(max(c['bottom'] for c in chars),2),'left':round(min(c['x0'] for c in chars),2),'right':round(max(c['x1'] for c in chars),2)}
    links=[]
    for annot in page.get('/Annots',[]):
        uri=annot.get_object().get('/A',{}).get('/URI')
        if uri: links.append(str(uri))
    assert any(x.startswith('mailto:') for x in links) and any(x.startswith('https://github.com/') for x in links)
    aliases=[name for name,target in alias_targets.items() if target==item['file']]
    for alias in aliases: assert (p.parent/alias).read_bytes()==p.read_bytes(), (item['id'],alias,'alias differs from canonical PDF')
    words=len(re.findall(r'\S+',text))
    old_item=old.get(item['file'])
    old_words=len(re.findall(r'\S+',old_item.get('text',''))) if old_item else None
    results.append({'id':item['id'],'file':item['file'],'pages':1,'a4':True,'textSelectable':True,'textSafeMargins':True,'minimumFontPt':round(min_font,2),'bodyFontMinimumPt':round(min(body_sizes),2),'textBoundsPt':extent,'wordsBefore':old_words,'wordsAfter':words,'legacyAliasesIdentical':aliases,'links':links,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})

out=site/'evidence/refinement/cv/independent-checks.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'method':'Independent pypdf/pdfplumber structural validation of six current V15 PDFs: page size/count, extracted text, character bounds, font sizes, hyperlinks, six-item static catalog and byte-identical legacy PDF aliases. No commercial ATS submission and no PDF/UA certification.','canonicalCount':6,'catalogCanonicalFiles':parser.hrefs,'legacyAliasCount':len(alias_targets),'results':results,'failures':[]},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'checked':len(results),'aliases':len(alias_targets),'failures':0,'words':[{k:x[k] for k in ('id','wordsBefore','wordsAfter')} for x in results]},ensure_ascii=True))
