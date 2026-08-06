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
        "headings": ["RESUMO PROFISSIONAL", "HABILIDADES TÉCNICAS", "EXPERIÊNCIA PROFISSIONAL", "PROJETOS SELECIONADOS", "FORMAÇÃO", "CERTIFICAÇÕES", "IDIOMAS"],
        "required": [
            "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
            "n8n self-hosted", "automação low-code", "AS-IS/TO-BE", "IA generativa e agentes", "Codex", "APIs de LLM",
            "recuperação de contexto/grounding", "JSON Schema", "IA multimodal", "text-to-video", "APIs REST", "webhooks",
            "Node.js/Express", "FastAPI", "Git/GitHub Actions", "CI/CD",
            "mais de 10 mil execuções de workflows em produção", "menos de 30 segundos", "11 computadores", "11 usuários",
            "3 horas para cerca de 5 minutos", "GRUPO VESPER", "Técnico Júnior em Automação de Processos",
            "Mala Direta", "2 workflows", "fluxo principal com 158 nós", "9 Data Tables de domínio", "900+ destinatários",
            "Catálogo Operacional de Compras", "usado diariamente por 3 usuários", "SQLite FTS5", "controle de concorrência por revisão",
            "Postagem Redes", "3 workflows n8n", "workflow de ações com 58 nós", "Facebook validado em teste",
            "Portal - em desenvolvimento", "Business Operating Platform multiempresa", "tenant/RLS", "Action Envelope",
            "Procurement validado em sandbox", "preparação para piloto interno",
            "Tecnólogo em Análise e Desenvolvimento de Sistemas", "Ferramentas de IA: Agentes e Automações",
        ],
        "forbidden": [
            "5 workflows/158", "3 workflows/58", "ProcureFlow", "Portal Vesper", "RAG/grounding", "FastAPI/Flask",
            "Profissional de automação, IA generativa e aplicada", "EVIDÊNCIAS, FORMAÇÃO E CERTIFICAÇÕES",
        ],
        "date_patterns": [r"12/2025\s*-\s*presente", r"10/2024\s*-\s*03/2025"],
    },
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf": {
        "headings": ["PROFESSIONAL SUMMARY", "TECHNICAL SKILLS", "PROFESSIONAL EXPERIENCE", "SELECTED PROJECTS", "EDUCATION", "CERTIFICATIONS", "LANGUAGES"],
        "required": [
            "AI AUTOMATION & INTEGRATIONS ANALYST",
            "self-hosted n8n", "low-code automation", "AS-IS/TO-BE", "Generative AI and agents", "Codex", "LLM APIs",
            "context retrieval/grounding", "JSON Schema", "multimodal AI", "text-to-video", "REST APIs", "webhooks",
            "Node.js/Express", "FastAPI", "Git/GitHub Actions", "CI/CD",
            "more than 10,000 production workflow executions", "under 30 seconds", "11 workstations", "11 users",
            "3 hours to around 5 minutes", "GRUPO VESPER", "Junior Process Automation Technician",
            "Mala Direta", "2 workflows", "main workflow has 158 nodes", "9 domain Data Tables", "900+ recipient campaign",
            "Operational Procurement Catalog", "used daily by 3 users", "SQLite FTS5", "optimistic revision control",
            "Postagem Redes", "3 n8n workflows", "actions workflow has 58 nodes", "Facebook validated in testing",
            "Portal - in development", "multi-tenant Business Operating Platform", "tenant/RLS", "Action Envelopes",
            "Procurement validated in sandbox", "prepared for an internal pilot",
            "Technology Degree in Systems Analysis and Development", "AI Tools: Agents and Automations",
        ],
        "forbidden": [
            "5 workflows/158", "3 workflows/58", "ProcureFlow", "Portal Vesper", "RAG/grounding", "FastAPI/Flask",
            "EVIDENCE, EDUCATION & CERTIFICATIONS",
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
        if len(text) < 3300 or len(fitz_text) < 3300:
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
                errors.append(f"{filename}: stale, ambiguous or unsupported text found: {phrase}")
        for pattern in rules["date_patterns"]:
            if not re.search(pattern, text):
                errors.append(f"{filename}: inconsistent date pattern: {pattern}")

        metadata = reader.metadata or {}
        if metadata.get("/Author") != "Maycon Ferreira":
            errors.append(f"{filename}: invalid Author metadata")
        if not str(metadata.get("/Title") or "").startswith("Maycon Ferreira - "):
            errors.append(f"{filename}: invalid Title metadata")
        keywords = str(metadata.get("/Keywords") or "").lower()
        for keyword in ("automation", "n8n", "generative ai", "fastapi", "fts5", "rls", "action envelope"):
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
    print("Resume content and ATS validation completed without errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
