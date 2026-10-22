"""One-page, ATS-readability, content and link validations for published CVs."""
from pathlib import Path
import fitz
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / 'assets' / 'cv'
FILES = {
  'Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf': ('PERFIL PROFISSIONAL','Belarc Inventory','Hubora','Compass UOL'),
  'Maycon_Ferreira_Automacao_Integracoes.pdf': ('PERFIL PROFISSIONAL','Mala Direta','Catálogo Operacional','Compass UOL'),
  'Maycon_Ferreira_Sistemas_Backend.pdf': ('PERFIL PROFISSIONAL','Manutenção em Campo','CarreiraPessoal','Compass UOL'),
  'Maycon_Ferreira_Web_Produtos_Digitais.pdf': ('PERFIL PROFISSIONAL','Vesper + Vent Rio','Hubora','Compass UOL'),
  'Maycon_Ferreira_IA_Agentes_MCP.pdf': ('PERFIL PROFISSIONAL','Postagem Redes','ArsenalMind','Compass UOL'),
  'Maycon_Ferreira_Dados_BI.pdf': ('PERFIL PROFISSIONAL','QuickSight','Catálogo Operacional','Compass UOL'),
  'Maycon_Ferreira_Conteudo_Video_IA.pdf': ('PERFIL PROFISSIONAL','Conteúdo audiovisual industrial','Postagem Redes','Compass UOL'),
  'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf': ('PROFESSIONAL SUMMARY','Belarc Inventory','Hubora','Compass UOL'),
  'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf': ('PERFIL PROFISSIONAL','Belarc Inventory','Hubora','Compass UOL'),
  'Maycon_Ferreira_Automacao_IA_n8n_Python_LLMs.pdf': ('PERFIL PROFISSIONAL','Postagem Redes','ArsenalMind','Compass UOL'),
  'Maycon_Ferreira_Automacao_BI_Power_Automate_Power_BI.pdf': ('PERFIL PROFISSIONAL','QuickSight','Catálogo Operacional','Compass UOL'),
}
CONTACTS=('mayconxz00dev@gmail.com','github.com/Mayconxzdev','mayconxzdev.github.io','linkedin.com/in/maycon-ferreira-7bb870231')
MANDATORY_LINKS=('https://github.com/Mayconxzdev','https://mayconxzdev.github.io/','https://www.linkedin.com/in/maycon-ferreira-7bb870231/')
FORBIDDEN=('10 mil+', '10k+', '10+ computadores', '20+ profissionais', 'menos de 30', 'under 30 sec')

def normal(s):return ' '.join(s.split()).casefold()

for name, phrases in FILES.items():
    path=CV/name
    assert path.exists(), f'Missing PDF: {path}'
    a=PdfReader(str(path))
    with fitz.open(path) as d:
        assert len(a.pages)==len(d)==1, f'Must be 1 page: {name}'
        txt1=a.pages[0].extract_text() or ''
        txt2=d[0].get_text()
        assert len(txt1)>1600 and len(txt2)>1600, f'Unexpectedly little selectable text: {name}'
        assert '\ufffd' not in txt1+txt2, f'Encoding error: {name}'
        for phrase in phrases+CONTACTS:
            assert normal(phrase) in normal(txt1) and normal(phrase) in normal(txt2), f'Missing {phrase}: {name}'
        for phrase in FORBIDDEN:
            assert normal(phrase) not in normal(txt2), f'Disallowed operational numbers: {phrase} in {name}'
        links={link.get('uri') for link in d[0].get_links() if link.get('uri')}
        for required in MANDATORY_LINKS:
            assert required in links, f'Absent link {required}: {name}'
        rect=d[0].rect
        assert abs(rect.width-595.3)<2 and abs(rect.height-841.9)<2
        print('PASS:',name, 'chars=',len(txt2),'links=',len(links))
print(f'Validated {len(FILES)} published PDFs')