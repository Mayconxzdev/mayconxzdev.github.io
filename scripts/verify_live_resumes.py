from __future__ import annotations

from pathlib import Path
import sys
from pypdf import PdfReader

REQUIRED = {
    'pt': [
        'ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES',
        'low-code/no-code',
        'UAT/homologação',
        'IA generativa/LLMs',
        'evals offline reproduzíveis',
        'Automation Business Analyst Professional Training',
        'N8N102/N8N103',
    ],
    'en': [
        'AI, AUTOMATION & INTEGRATIONS ANALYST',
        'low-code/no-code',
        'generative AI/LLMs',
        'reproducible offline evals',
        'Automation Business Analyst Professional Training',
        'N8N102/N8N103',
    ],
}

FORBIDDEN = {
    'pt': [
        'Automation Business Analyst Associate Training',
        'Portal:',
        '158 nós',
        'CERTIFICAÇÕES',
        'OpenAI/Gemini/Ollama/OpenRouter',
    ],
    'en': [
        'Automation Business Analyst Associate Training',
        'Portal:',
        '158 nodes',
        'CERTIFICATIONS',
        'OpenAI/Gemini/Ollama/OpenRouter',
    ],
}


def normalized(value: str) -> str:
    return ' '.join(value.split())


def check(lang: str, path: Path) -> None:
    reader = PdfReader(str(path))
    if len(reader.pages) != 1:
        raise SystemExit(f'{path.name}: live resume must be one page, got {len(reader.pages)}')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    flat = normalized(text)
    for phrase in REQUIRED[lang]:
        if normalized(phrase) not in flat:
            raise SystemExit(f'{path.name}: stale/incomplete live resume; missing {phrase!r}')
    for phrase in FORBIDDEN[lang]:
        if normalized(phrase) in flat:
            raise SystemExit(f'{path.name}: stale/forbidden live resume text found: {phrase!r}')
    print(f'OK live {lang} resume: one page, current August 2026 content verified.')


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit('usage: verify_live_resumes.py <pt-pdf> <en-pdf>')
    check('pt', Path(sys.argv[1]))
    check('en', Path(sys.argv[2]))


if __name__ == '__main__':
    main()
