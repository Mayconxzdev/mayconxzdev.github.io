from __future__ import annotations

import re
from pathlib import Path

import fitz
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
        "headings": [
            "RESUMO PROFISSIONAL", "HABILIDADES TÉCNICAS", "EXPERIÊNCIA PROFISSIONAL",
            "PROJETOS SELECIONADOS", "FORMAÇÃO", "CERTIFICAÇÕES", "IDIOMAS",
        ],
        "required": [
            "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
            "viagens e mudança",
            "uma instância n8n self-hosted",
            "10 mil+ execuções de workflows em produção",
            "automação low-code/no-code",
            "AS-IS/TO-BE",
            "Ollama e OpenRouter",
            "APIs de LLM",
            "recuperação de contexto/grounding",
            "JSON Schema",
            "IA multimodal e geração de mídia",
            "APIs REST",
            "Node.js/Express",
            "FastAPI",
            "AWS S3/EC2/Lambda/Glue/Athena/QuickSight",
            "menos de 30 segundos",
            "10+ computadores",
            "1 TV",
            "20+ profissionais",
            "9 setores",
            "11 usuários",
            "30+ pessoas",
            "Estagiário de TI/Dados",
            "Programa de Bolsas em Engenharia de Dados",
            "10 sprints práticas",
            "CSV/API TMDB",
            "Glue/PySpark",
            "Raw/Trusted/Refined",
            "Mala Direta",
            "6 campanhas",
            "1.020 contatos",
            "900+ destinatários",
            "158 nós no principal",
            "9 Data Tables",
            "Catálogo Operacional de Compras",
            "24 categorias",
            "480+ códigos",
            "Postagem Redes",
            "Facebook e Instagram exercitados em teste",
            "Portal - em desenvolvimento",
            "tenant/RLS",
            "Action Envelope",
            "revalidação técnica em andamento",
            "Tecnólogo em Análise e Desenvolvimento de Sistemas",
            "Inglês: leitura técnica independente",
        ],
        "forbidden": [
            "3 horas para cerca de 5 minutos", "3h", "text-to-video", "11 computadores",
            "PlanilhaCompras", "ProcureFlow", "Portal Vesper", "Procurement validado em sandbox",
            "Facebook e Instagram validados em teste", "10 mil+ execuções em produção",
            "Inglês básico", "Ollama/OpenRouter", "FastAPI/Flask",
        ],
        "date_patterns": [r"12/2025\s*-\s*presente", r"10/2024\s*-\s*03/2025"],
    },
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf": {
        "headings": [
            "PROFESSIONAL SUMMARY", "TECHNICAL SKILLS", "PROFESSIONAL EXPERIENCE",
            "SELECTED PROJECTS", "EDUCATION", "CERTIFICATIONS", "LANGUAGES",
        ],
        "required": [
            "AI AUTOMATION & INTEGRATIONS ANALYST",
            "available to travel and relocate",
            "10,000+ workflow executions in production",
            "low-code/no-code automation",
            "AS-IS/TO-BE",
            "Ollama and OpenRouter",
            "LLM APIs",
            "context retrieval/grounding",
            "JSON Schema",
            "multimodal AI and media generation",
            "REST APIs",
            "Node.js/Express",
            "FastAPI",
            "AWS S3/EC2/Lambda/Glue/Athena/QuickSight",
            "under 30 seconds",
            "10+ workstations",
            "1 factory TV",
            "20+ professionals",
            "9 production areas",
            "11 users",
            "30+ people",
            "Data Engineering Intern",
            "Scholarship Program",
            "10 practical sprints",
            "CSV/TMDB API",
            "Glue/PySpark",
            "Raw/Trusted/Refined",
            "Mala Direta",
            "6 campaigns",
            "1,020-contact base",
            "900+ recipients",
            "158 nodes in the main flow",
            "9 Data Tables",
            "Operational Procurement Catalog",
            "24 categories",
            "480+ material codes",
            "Postagem Redes",
            "Facebook and Instagram exercised in testing",
            "Portal - in development",
            "tenant/RLS",
            "Action Envelopes",
            "technical revalidation underway",
            "Technology Degree (Tecnólogo) in Systems Analysis and Development",
            "Process Automation with RPA",
            "English: independent technical reading",
        ],
        "forbidden": [
            "3 hours to around 5 minutes", "text-to-video", "11 workstations", "PlanilhaCompras",
            "ProcureFlow", "Portal Vesper", "Procurement validated in sandbox",
            "Facebook and Instagram validated in testing", "10,000+ production executions",
            "English: basic", "Ollama/OpenRouter", "FastAPI/Flask",
        ],
        "date_patterns": [r"12/2025\s*-\s*Present", r"10/2024\s*-\s*03/2025"],
    },
}


def annotations(reader: PdfReader) -> set[str]:
    links: set[str] = set()
    for page in reader.pages:
        for annotation in page.get("/Annots", []):
            item = annotation.get_object()
            action = item.get("/A")
            if action and action.get("/URI"):
                links.add(str(action["/URI"]))
    return links


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    errors: list[str] = []
    actual = sorted(path.name for path in CV.glob("*.pdf"))
    expected = sorted(FILES)
    if actual != expected:
        errors.append(f"assets/cv must contain only current resumes: found {actual}, expected {expected}")

    for filename, rules in FILES.items():
        path = CV / filename
        if not path.exists():
            errors.append(f"missing: {filename}")
            continue
        if path.stat().st_size > 250_000:
            errors.append(f"{filename}: unexpectedly large ({path.stat().st_size} bytes)")

        reader = PdfReader(str(path))
        if len(reader.pages) != 1:
            errors.append(f"{filename}: expected 1 page, found {len(reader.pages)}")
            continue
        page = reader.pages[0]
        width, height = float(page.mediabox.width), float(page.mediabox.height)
        if abs(width - 595.2756) > 1 or abs(height - 841.8898) > 1:
            errors.append(f"{filename}: page is not A4 ({width:.1f} x {height:.1f})")

        text = normalized(page.extract_text() or "")
        fitz_doc = fitz.open(path)
        fitz_text = normalized(fitz_doc[0].get_text("text"))
        if len(text) < 3000 or len(fitz_text) < 3000:
            errors.append(f"{filename}: extracted text is unexpectedly short ({len(text)} / {len(fitz_text)} chars)")

        previous = -1
        for heading in rules["headings"]:
            position = text.find(heading)
            if position == -1:
                errors.append(f"{filename}: missing standard heading: {heading}")
            elif position <= previous:
                errors.append(f"{filename}: heading out of order: {heading}")
            previous = max(previous, position)

        for phrase in rules["required"]:
            if phrase not in text:
                errors.append(f"{filename}: missing required evidence/keyword: {phrase}")
        for phrase in rules["forbidden"]:
            if phrase in text:
                errors.append(f"{filename}: stale, awkward or unsupported text found: {phrase}")
        for pattern in rules["date_patterns"]:
            if not re.search(pattern, text):
                errors.append(f"{filename}: inconsistent date pattern: {pattern}")

        metadata = reader.metadata or {}
        if metadata.get("/Author") != "Maycon Ferreira":
            errors.append(f"{filename}: invalid Author metadata")
        if not str(metadata.get("/Title") or "").startswith("Maycon Ferreira - "):
            errors.append(f"{filename}: invalid Title metadata")
        keywords = str(metadata.get("/Keywords") or "").lower()
        for keyword in ("automation", "n8n", "generative ai", "media generation", "fastapi", "fts5", "aws", "data engineering", "rls", "action envelope"):
            if keyword not in keywords:
                errors.append(f"{filename}: Keywords metadata is missing {keyword}")

        found = annotations(reader)
        if missing := EXPECTED_URIS - found:
            errors.append(f"{filename}: missing links: {sorted(missing)}")
        if extra := found - EXPECTED_URIS:
            errors.append(f"{filename}: unexpected links: {sorted(extra)}")
        print(f"OK: {filename} | one A4 page | {len(text)} chars | {len(found)} links")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Resume content, evidence and ATS parsing validated without errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
