from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN = [
    "Leitura rápida para recrutadores",
    "Projetos recomendados para avaliação",
    "Evidências atualmente confirmadas",
    "PROVAS EM CONTEXTO",
    "PROVA OPERACIONAL",
    "PROVA DE AMPLITUDE",
    "O que este repositório comprova",
    "Seis entregas para entender meu valor",
    "Para uma avaliação rápida",
    "Recruiter overview",
    "Technical review summary",
    "Five-minute review path",
    "EVIDENCE IN CONTEXT",
    "OPERATIONAL EVIDENCE",
    "BREADTH EVIDENCE",
    "What this project demonstrates",
    "What this repository demonstrates",
    "Skills demonstrated",
    "Two-minute evaluation",
    "For a quick evaluation",
    "Text-to-video",
    "text-to-video",
]

STALE_CLAIMS = [
    "11 computadores do escritório",
    "11 office computers",
    "11 + TV",
    "3h → 5min",
    "3 hours to 5 minutes",
    "cases/compass-automation/",
    "Procurement do Portal validado em sandbox",
    "Portal Procurement validated in sandbox",
]

PUBLIC_FILES = [
    ROOT / "README.md",
    ROOT / "index.html",
    ROOT / "en" / "index.html",
    ROOT / "competencias" / "index.html",
    ROOT / "en" / "skills" / "index.html",
]
PUBLIC_FILES.extend(
    path
    for path in ROOT.rglob("*.html")
    if "artifacts" not in path.parts and path not in PUBLIC_FILES
)


def main() -> int:
    errors: list[str] = []
    for path in sorted(set(PUBLIC_FILES)):
        if not path.exists():
            errors.append(f"missing public file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in FORBIDDEN:
            if phrase in text:
                errors.append(f"{path.relative_to(ROOT)}: external-review or AI-like wording remains: {phrase}")
        if path in {
            ROOT / "index.html",
            ROOT / "en" / "index.html",
            ROOT / "competencias" / "index.html",
            ROOT / "en" / "skills" / "index.html",
        }:
            for phrase in STALE_CLAIMS:
                if phrase in text:
                    errors.append(f"{path.relative_to(ROOT)}: stale or unsupported claim remains: {phrase}")

    required = {
        ROOT / "index.html": [
            "RESULTADOS EM USO",
            "PROJETOS PRINCIPAIS",
            "Alguns números da minha atuação atual.",
            "10+ PCs · 1 TV · 9 setores",
            "base de 1.020 contatos",
        ],
        ROOT / "en" / "index.html": [
            "RESULTS IN USE",
            "MAIN PROJECTS",
            "A few numbers from my current work.",
            "10+ PCs · 1 TV · 9 areas",
            "1,020-contact base",
        ],
        ROOT / "competencias" / "index.html": [
            "COMPETÊNCIAS E EXPERIÊNCIA PRÁTICA",
            "ONDE APLIQUEI NA ROTINA",
            "geração de mídia",
        ],
        ROOT / "en" / "skills" / "index.html": [
            "SKILLS AND PRACTICAL EXPERIENCE",
            "WHERE I USE IT IN PRACTICE",
            "media generation",
        ],
    }
    for path, phrases in required.items():
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{path.relative_to(ROOT)}: required natural/current wording missing: {phrase}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Public voice validated across {len(set(PUBLIC_FILES))} public files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
