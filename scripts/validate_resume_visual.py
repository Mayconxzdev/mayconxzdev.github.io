"""PDF visual-integrity checks. Does not claim commercial ATS acceptance."""
from pathlib import Path
import fitz

ROOT=Path(__file__).resolve().parents[1]
CV=ROOT/'assets'/'cv'
FILES=[
 'Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf',
 'Maycon_Ferreira_Automacao_Integracoes.pdf',
 'Maycon_Ferreira_Sistemas_Backend.pdf',
 'Maycon_Ferreira_Web_Produtos_Digitais.pdf',
 'Maycon_Ferreira_IA_Agentes_MCP.pdf',
 'Maycon_Ferreira_Dados_BI.pdf',
 'Maycon_Ferreira_Conteudo_Video_IA.pdf',
 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
 'Maycon_Ferreira_Automacao_IA_n8n_Python_LLMs.pdf',
 'Maycon_Ferreira_Automacao_BI_Power_Automate_Power_BI.pdf',
]
for name in FILES:
    with fitz.open(CV/name) as doc:
        assert len(doc)==1,name
        p=doc[0]
        pix=p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False)
        assert pix.width>890 and pix.height>1250,name
        spans=[]
        for b in p.get_text('dict').get('blocks',[]):
            for line in b.get('lines',[]):
                spans+= [s for s in line.get('spans',[]) if s.get('text','').strip()]
        assert spans,name
        text=p.get_text('text')
        assert 'Maycon Ferreira' in text and len(text)>1500,name
        assert '\ufffd' not in text,name
        assert all(0 <= v <= p.rect.height for sp in spans for v in (sp['bbox'][1], sp['bbox'][3])),name
        assert min(s['size'] for s in spans)>=9.5, f'Font below reviewed minimum 9.5 pt: {name}'
        assert min(s['bbox'][0] for s in spans)>=35, f'Too close to left border {name}'
        assert max(s['bbox'][2] for s in spans)<=p.rect.width-35, f'Too close to right border {name}'
        bottom=p.rect.height-max(s['bbox'][3] for s in spans)
        assert 35<bottom<120, f'Unbalanced page or clipping {name}: {bottom:.1f}'
        print(f'VISUAL PASS: {name} minfont={min(s["size"] for s in spans):.1f} bottom={bottom:.0f}pt')