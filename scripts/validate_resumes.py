"""Static checks for the public one-page resume PDFs.

Run with the same Python environment used by generate_resumes.py:
    C:\\Users\\Projeto3\\cv_env\\Scripts\\python.exe scripts\\validate_resumes.py
"""

from __future__ import annotations

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
    "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf": [
        "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES",
        "Técnico Júnior em Automação de Processos",
        "RESUMO PROFISSIONAL",
    ],
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf": [
        "AI AUTOMATION & INTEGRATIONS ANALYST",
        "Junior Process Automation Technician",
        "PROFESSIONAL SUMMARY",
    ],
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


def main() -> int:
    errors: list[str] = []
    for filename, required_text in FILES.items():
        path = CV / filename
        if not path.exists():
            errors.append(f"ausente: {filename}")
            continue
        reader = PdfReader(str(path))
        if len(reader.pages) != 1:
            errors.append(f"{filename}: esperado 1 página, encontrado {len(reader.pages)}")
            continue
        content = reader.pages[0].extract_text() or ""
        for phrase in required_text:
            if phrase not in content:
                errors.append(f"{filename}: texto obrigatório ausente: {phrase}")
        found = annotations(reader)
        missing = EXPECTED_URIS - found
        extra = found - EXPECTED_URIS
        if missing:
            errors.append(f"{filename}: links ausentes: {sorted(missing)}")
        if extra:
            errors.append(f"{filename}: links inesperados: {sorted(extra)}")
        print(f"OK: {filename} | 1 página | {len(found)} links clicáveis")
    if errors:
        print("\n".join(f"ERRO: {error}" for error in errors))
        return 1
    print("Validação de currículo concluída sem erros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
