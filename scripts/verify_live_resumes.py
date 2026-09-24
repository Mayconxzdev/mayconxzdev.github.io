from __future__ import annotations

from pathlib import Path
import sys
from pypdf import PdfReader

REQUIRED = {
    'pt-general': [
        'ANALISTA DE AUTOMAÇÃO E IA | n8n · Power Automate · Python',
        'Power Automate', 'APIs', 'Tradutor documental offline',
        'Postagem Redes', 'Produção Operacional', 'Belarc Inventory',
    ],
    'en-general': [
        'AUTOMATION & AI ANALYST | n8n · Power Automate · Python',
        'Power Automate', 'APIs', 'Offline Document Translator',
        'Production Operations', 'IT operations', 'Belarc Inventory',
    ],
    'pt-ai': [
        'ANALISTA DE AUTOMAÇÃO E IA | n8n · Python · LLMs/RAG',
        'Power Automate', 'RAG/LangChain', 'Supabase/Qdrant',
        'Plataforma SaaS B2B', 'Postagem Redes',
    ],
    'pt-bi': [
        'ANALISTA DE AUTOMAÇÃO E BI | Power Automate · Power BI · Python',
        'Power Automate Cloud/Desktop', 'Power BI', 'DAX', 'Power Query',
        'Excel/Google Sheets', 'Catálogo Operacional',
    ],
}

FORBIDDEN = [
    '12 dias', '12 days', 'menos de 4 horas', 'less than 4 hours',
    '55 certificações', '55 certifications',
    'UiPath Certified Automation Business Analyst Professional',
]

def normalized(value: str) -> str:
    return ' '.join(value.split())

def check(key: str, path: Path) -> None:
    reader = PdfReader(str(path))
    if len(reader.pages) != 1:
        raise SystemExit(f'{path.name}: live resume must be one page, got {len(reader.pages)}')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    flat = normalized(text)
    for phrase in REQUIRED[key]:
        if normalized(phrase) not in flat:
            raise SystemExit(f'{path.name}: stale/incomplete live resume; missing {phrase!r}')
    for phrase in FORBIDDEN:
        if normalized(phrase) in flat:
            raise SystemExit(f'{path.name}: stale/forbidden live resume text found: {phrase!r}')
    print(f'OK live {key} resume: one page and current candidature-ready content verified.')

def main() -> None:
    if len(sys.argv) != 5:
        raise SystemExit('usage: verify_live_resumes.py <pt-general> <en-general> <pt-ai> <pt-bi>')
    check('pt-general', Path(sys.argv[1]))
    check('en-general', Path(sys.argv[2]))
    check('pt-ai', Path(sys.argv[3]))
    check('pt-bi', Path(sys.argv[4]))

if __name__ == '__main__':
    main()
