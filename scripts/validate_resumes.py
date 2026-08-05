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
        "headings": [
            "RESUMO PROFISSIONAL",
            "HABILIDADES TÉCNICAS",
            "EXPERIÊNCIA PROFISSIONAL",
            "PROJETOS SELECIONADOS",
            "FORMAÇÃO",
            "CERTIFICAÇÕES",
            "IDIOMAS",
        ],
        "required": [
            "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
            "n8n self-hosted",
            "mapeamento AS-IS/TO-BE",
            "IA generativa e agentes de IA",
            "APIs de LLM",
            "RAG",
            "JSON Schema",
            "text-to-video",
            "Integração de sistemas e ferramentas",
            "APIs REST",
            "webhooks",
            "Python",
            "JavaScript/TypeScript",
            "Git/GitHub Actions",
            "CI/CD",
            "mais de 10 mil execuções em produção",
            "menos de 30 segundos",
            "11 computadores",
            "11 usuários",
            "mais de 900 destinatários",
            "3 horas para cerca de 5 minutos",
            "Técnico Júnior em Automação de Processos",
            "Tecnólogo em Análise e Desenvolvimento de Sistemas",
            "Ferramentas de IA: Agentes e Automações",
        ],
        "forbidden": [
            "EVIDÊNCIAS, FORMAÇÃO E CERTIFICAÇÕES",
            "Ferramentas de conversão de texto em vídeo não são apresentadas",
        ],
        "date_patterns": [r"12/2025\s*-\s*presente", r"10/2024\s*-\s*03/2025"],
    },
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf": {
        "headings": [
            "PROFESSIONAL SUMMARY",
            "TECHNICAL SKILLS",
            "PROFESSIONAL EXPERIENCE",
            "SELECTED PROJECTS",
            "EDUCATION",
            "CERTIFICATIONS",
            "LANGUAGES",
        ],
        "required": [
            "AI AUTOMATION & INTEGRATIONS ANALYST",
            "self-hosted n8n",
            "AS-IS/TO-BE process mapping",
            "Generative AI and AI agents",
            "LLM APIs",
            "RAG",
            "JSON Schema",
            "text-to-video",
            "Systems and tools integration",
            "REST APIs",
            "webhooks",
            "Python",
            "JavaScript/TypeScript",
            "Git/GitHub Actions",
            "CI/CD",
            "more than 10,000 production executions",
            "under 30 seconds",
            "11 workstations",
            "11 users",
            "more than 900 recipients",
            "3 hours to around 5 minutes",
            "Junior Process Automation Technician",
            "Systems Analysis and Development",
            "AI Tools: Agents and Automations",
        ],
        "forbidden": [
            "EVIDENCE, EDUCATION & CERTIFICATIONS",
            "Text-to-video tools are not presented",
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
    for filename, rules in FILES.items():
        path = CV / filename
        if not path.exists():
            errors.append(f"missing: {filename}")
            continue
        if path.stat().st_size > 400_000:
            errors.append(f"{filename}: file is unexpectedly large ({path.stat().st_size} bytes)")

        reader = PdfReader(str(path))
        if len(reader.pages) != 1:
            errors.append(f"{filename}: expected 1 page, found {len(reader.pages)}")
            continue

        page = reader.pages[0]
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - 595.2756) > 1 or abs(height - 841.8898) > 1:
            errors.append(f"{filename}: page is not A4 ({width:.1f} x {height:.1f})")

        raw = page.extract_text() or ""
        text = normalized(raw)
        if len(text) < 2500:
            errors.append(f"{filename}: extracted text is too short ({len(text)} chars)")

        metadata = reader.metadata or {}
        if metadata.get("/Author") != "Maycon Ferreira":
            errors.append(f"{filename}: invalid Author metadata")
        if not str(metadata.get("/Title") or "").startswith("Maycon Ferreira - "):
            errors.append(f"{filename}: invalid Title metadata")
        if "automation" not in str(metadata.get("/Keywords") or "").lower():
            errors.append(f"{filename}: Keywords metadata is incomplete")

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
                errors.append(f"{filename}: forbidden outdated text found: {phrase}")
        for pattern in rules["date_patterns"]:
            if not re.search(pattern, text):
                errors.append(f"{filename}: inconsistent or missing date pattern: {pattern}")

        found = annotations(reader)
        missing = EXPECTED_URIS - found
        extra = found - EXPECTED_URIS
        if missing:
            errors.append(f"{filename}: missing links: {sorted(missing)}")
        if extra:
            errors.append(f"{filename}: unexpected links: {sorted(extra)}")

        print(f"OK: {filename} | 1 A4 page | {len(text)} extracted chars | {len(found)} clickable links")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Resume validation completed without errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
