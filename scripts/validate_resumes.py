"""Validate bilingual public resumes for ATS readability and release safety."""
from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / "assets" / "cv"

EXPECTED_URIS = {
    "https://wa.me/5521964810480",
    "mailto:mayconxz00dev@gmail.com",
    "https://www.linkedin.com/in/maycon-ferreira-7bb870231/",
    "https://github.com/Mayconxzdev",
    "https://mayconxzdev.github.io/",
}

FILES = {
    "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf": {
        "title": "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
        "headings": ["RESUMO PROFISSIONAL", "HABILIDADES TÉCNICAS", "EXPERIÊNCIA PROFISSIONAL", "FORMAÇÃO E CERTIFICAÇÕES"],
        "proof": ["mais de 10 mil", "mais de 900 destinatários", "11 computadores", "menos de 30 segundos", "cerca de 5 minutos"],
        "skills": ["n8n self-hosted", "AS-IS/TO-BE", "IA generativa", "engenharia de prompts", "JSON Schema", "APIs REST", "OAuth 2.0", "Python", "PostgreSQL", "Docker", "idempotência"],
        "dates": ["dez. 2025 - presente", "out. 2024 - mar. 2025"],
    },
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf": {
        "title": "AI AUTOMATION & SYSTEMS INTEGRATION ANALYST",
        "headings": ["PROFESSIONAL SUMMARY", "TECHNICAL SKILLS", "PROFESSIONAL EXPERIENCE", "EDUCATION & CERTIFICATIONS"],
        "proof": ["more than 10,000", "more than 900 recipients", "11 workstations", "under 30 seconds", "about five minutes"],
        "skills": ["self-hosted n8n", "AS-IS/TO-BE", "generative AI", "prompt engineering", "JSON Schema", "REST APIs", "OAuth 2.0", "Python", "PostgreSQL", "Docker", "idempotency"],
        "dates": ["Dec. 2025 - Present", "Oct. 2024 - Mar. 2025"],
    },
}

FORBIDDEN = [
    "fora. 2024",
    "EVENT RIO",
    "text-to-video tools are not presented",
    "ferramentas de conversão de texto em vídeo não são apresentadas",
    "currículo recomendado",
    "resume recommended",
]


def extract_links(reader: PdfReader) -> set[str]:
    links: set[str] = set()
    for page in reader.pages:
        for ref in page.get("/Annots", []):
            annotation = ref.get_object()
            action = annotation.get("/A")
            if action and action.get("/URI"):
                links.add(str(action["/URI"]))
    return links


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    errors: list[str] = []
    for filename, rules in FILES.items():
        path = CV / filename
        if not path.exists():
            errors.append(f"ausente: {filename}")
            continue

        reader = PdfReader(str(path))
        if len(reader.pages) != 1:
            errors.append(f"{filename}: esperado 1 página, encontrado {len(reader.pages)}")
            continue

        raw = reader.pages[0].extract_text() or ""
        text = normalized(raw)
        metadata = reader.metadata or {}

        if metadata.get("/Author") != "Maycon Ferreira":
            errors.append(f"{filename}: Author ausente ou incorreto")
        if not str(metadata.get("/Title") or "").startswith("Maycon Ferreira - "):
            errors.append(f"{filename}: Title ausente ou incorreto")
        if not str(metadata.get("/Subject") or "").strip():
            errors.append(f"{filename}: Subject ausente")
        if not str(metadata.get("/Keywords") or "").strip():
            errors.append(f"{filename}: Keywords ausentes")

        required = [rules["title"], *rules["headings"], *rules["proof"], *rules["skills"], *rules["dates"]]
        for phrase in required:
            if phrase not in text:
                errors.append(f"{filename}: texto obrigatório ausente: {phrase}")
        for phrase in FORBIDDEN:
            if phrase.casefold() in text.casefold():
                errors.append(f"{filename}: texto proibido encontrado: {phrase}")

        for contact in ["mayconxz00dev@gmail.com", "linkedin.com/in/maycon-ferreira-7bb870231", "github.com/Mayconxzdev", "mayconxzdev.github.io"]:
            if contact not in text:
                errors.append(f"{filename}: contato ausente no texto: {contact}")

        links = extract_links(reader)
        missing = EXPECTED_URIS - links
        unexpected = links - EXPECTED_URIS
        if missing:
            errors.append(f"{filename}: links ausentes: {sorted(missing)}")
        if unexpected:
            errors.append(f"{filename}: links inesperados: {sorted(unexpected)}")

        word_count = len(text.split())
        if not 400 <= word_count <= 720:
            errors.append(f"{filename}: contagem de palavras fora da faixa esperada: {word_count}")

        print(f"OK: {filename} | 1 página | {word_count} palavras | {len(links)} links")

    if errors:
        for error in errors:
            print(f"ERRO: {error}")
        return 1
    print("Validação dos currículos concluída sem erros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
