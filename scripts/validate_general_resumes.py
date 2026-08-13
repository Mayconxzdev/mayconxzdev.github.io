from pathlib import Path
import fitz
from pypdf import PdfReader

root=Path(__file__).resolve().parents[1]
cv=root/'assets'/'cv'
files={
'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf':['ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES','APIs REST','Linux','RAG/grounding com LangChain','CarreiraPessoal','Central ISO','40+ ativos','283 testes Python'],
'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf':['AI AUTOMATION & INTEGRATIONS ANALYST','REST APIs','Linux','RAG/grounding with LangChain','CarreiraPessoal','Central ISO','40+ assets','283 Python tests'],
}
for name,required in files.items():
    path=cv/name
    reader=PdfReader(str(path))
    assert len(reader.pages)==1, f'{name}: expected one page'
    page=reader.pages[0]
    assert abs(float(page.mediabox.width)-595.3)<2 and abs(float(page.mediabox.height)-841.9)<2, f'{name}: expected A4'
    text=' '.join((page.extract_text() or '').split())
    for phrase in required: assert phrase in text, f'{name}: missing {phrase}'
    doc=fitz.open(path); spans=[]
    for block in doc[0].get_text('dict').get('blocks',[]):
        if block.get('type')==0:
            for line in block.get('lines',[]): spans += [s for s in line.get('spans',[]) if s.get('text','').strip()]
    assert spans and min(float(s['size']) for s in spans)>=7.9, f'{name}: font too small'
    assert doc[0].rect.height-max(float(s['bbox'][3]) for s in spans)>=34, f'{name}: bottom margin too small'
    print(f'OK: {name} | one A4 page | {len(text)} chars')
print('General resume validation passed.')
