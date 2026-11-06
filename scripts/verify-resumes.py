"""Verify the four current resume PDFs and historical URLs after site build."""
from pathlib import Path
import hashlib, html.parser, json, re
from pypdf import PdfReader
import pdfplumber

site=Path(__file__).resolve().parent.parent
content=json.loads((site/"scripts/resumes-content.json").read_text(encoding="utf8"))
expected={
 "pt_ai":"Maycon_Ferreira_IA_Aplicada_Agentes_PT_2026_V2.pdf",
 "pt_sw":"Maycon_Ferreira_Backend_Integracoes_PT_2026_V2.pdf",
 "en_ai":"Maycon_Ferreira_Applied_AI_Agents_EN_2026_V2.pdf",
 "en_sw":"Maycon_Ferreira_Backend_Integrations_EN_2026_V2.pdf",
}
assert len(content["resumes"])==4 and {x["id"]:x["file"] for x in content["resumes"]}==expected
source=(site/"src/data.js").read_text(encoding="utf8")
listed=set(re.findall('file:' + '\\s*' + '"([^"]+\\.pdf)"', source))
assert listed=={expected["pt_ai"],expected["pt_sw"]}, "Homepage must expose two current PT resumes"
class Links(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.hrefs=[]
 def handle_starttag(self,tag,attrs):
  if tag=="a":
   href=dict(attrs).get("href","")
   if href.lower().endswith(".pdf"):self.hrefs.append(Path(href).name)
catalog=Links()
catalog.feed((site/"public/assets/cv/index.html").read_text(encoding="utf8"))
assert len(catalog.hrefs)==4 and set(catalog.hrefs)==set(expected.values())
english=Links()
english.feed((site/"public/en/resumes/index.html").read_text(encoding="utf8"))
assert len(english.hrefs)==2 and set(english.hrefs)=={expected["en_ai"],expected["en_sw"]}
legacy={
 "Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf":"pt_sw",
 "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf":"pt_ai",
 "Maycon_Ferreira_IA_Agentes_MCP.pdf":"pt_ai",
 "Maycon_Ferreira_Automacao_Integracoes.pdf":"pt_sw",
 "Maycon_Ferreira_Dados_BI.pdf":"pt_sw",
 "Maycon_Ferreira_Sistemas_Backend.pdf":"pt_sw",
 "Maycon_Ferreira_Web_Produtos_Digitais.pdf":"pt_sw",
 "Maycon_Ferreira_Conteudo_Video_IA.pdf":"pt_sw",
 "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf":"en_ai",
 "Maycon_Ferreira_Geral_Automacao_IA_PT.pdf":"pt_sw",
 "Maycon_Ferreira_Agentes_Automacao_n8n_PT.pdf":"pt_ai",
 "Maycon_Ferreira_Produtos_Conteudo_IA_PT.pdf":"pt_sw",
 "Maycon_Ferreira_General_Automation_AI_EN.pdf":"en_sw",
 "Maycon_Ferreira_AI_Agents_Automation_n8n_EN.pdf":"en_ai",
 "Maycon_Ferreira_AI_Digital_Products_Content_EN.pdf":"en_sw",
}
folder=site/"public/assets/cv"
results=[]
for item in content["resumes"]:
 path=folder/item["file"]
 reader=PdfReader(path)
 assert len(reader.pages)==1,(item["id"],"pages")
 p=reader.pages[0]
 assert abs(float(p.mediabox.width)-595.28)<2 and abs(float(p.mediabox.height)-841.89)<2
 text=p.extract_text()
 assert "Maycon Ferreira" in text and "UNISUAM" in text and len(text)>1100
 assert "\ufffd" not in text
 if item["lang"]=="en":assert "Expected" in text or "expected" in text
 else:assert "prevista" in text
 links=[]
 for annot in p.get("/Annots",[]):
  uri=annot.get_object().get("/A",{}).get("/URI")
  if uri:links.append(str(uri))
 assert any(x.startswith("https://github.com/") for x in links)
 assert any(x.startswith("mailto:") for x in links)
 with pdfplumber.open(path) as pdf:
  chars=[c for c in pdf.pages[0].chars if c["text"].strip()]
  outside=[c["text"] for c in chars if c["x0"]<31 or c["x1"]>pdf.pages[0].width-31 or c["top"]<20 or c["bottom"]>pdf.pages[0].height-20]
  assert not outside,(item["id"],"page margin",outside[:10])
  min_font=min(x["size"] for x in chars)
  assert min_font>=8.9,(item["id"],min_font)
 aliases=[name for name,target in legacy.items() if target==item["id"]]
 for name in aliases:assert (folder/name).read_bytes()==path.read_bytes(),(item["id"],name)
 results.append({"id":item["id"],"file":item["file"],"pages":1,"a4":True,"bytes":path.stat().st_size,"fontMinPt":round(min_font,2),"links":len(links),"legacyAliases":aliases,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
out=site/"evidence/refinement/cv/independent-checks.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"method":"Local PDF structure, links, text and bounds; not commercial ATS or WCAG certification","checked":len(results),"legacyCount":len(legacy),"results":results},ensure_ascii=False,indent=2),encoding="utf8")
print(json.dumps({"checked":len(results),"aliases":len(legacy),"issues":0},ensure_ascii=False))
