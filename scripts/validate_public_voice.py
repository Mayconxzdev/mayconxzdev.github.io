from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN = [
    "Leitura rápida para recrutadores",
    "Resumo para avaliação técnica",
    "Caminho de revisão em cinco minutos",
    "Como avaliar sem depender de dados reais",
    "Projetos recomendados para avaliação",
    "Evidências atualmente confirmadas",
    "O que este repositório comprova",
    "O que este projeto demonstra",
    "O que ficou comprovado",
    "Competências demonstradas",
    "PROVAS EM CONTEXTO",
    "PROVA OPERACIONAL",
    "PROVA DE AMPLITUDE",
    "PROVAS VISUAIS",
    "SISTEMAS PRIORITÁRIOS",
    "COMPETÊNCIA → PROVA",
    "Seis entregas para entender meu valor",
    "Para uma avaliação rápida",
    "avaliação rápida de RH",
    "Tipo de prova",
    "tipo de prova",
    "evidência pública",
    "material público é a arquitetura declarada",
    "A material público",
    "a material público",
    "Imagem selecionada como evidência visual do case.",
    "O que este case não mostra",
    "Se a operação crescesse",
    "Recruiter overview",
    "Technical review summary",
    "Five-minute review path",
    "Two-minute evaluation",
    "Projects recommended for evaluation",
    "Currently verified evidence",
    "What this project demonstrates",
    "What this repository demonstrates",
    "What is demonstrated",
    "What was demonstrated",
    "Skills demonstrated",
    "EVIDENCE IN CONTEXT",
    "OPERATIONAL EVIDENCE",
    "BREADTH EVIDENCE",
    "VISUAL EVIDENCE",
    "PRIORITY SYSTEMS",
    "SKILL → EVIDENCE",
    "For a quick evaluation",
    "quick HR evaluation",
    "Evidence type",
    "evidence type",
    "public evidence",
    "Image selected as visual evidence for this case.",
    "What this case does not show",
    "If the operation grew",
    "Text-to-video",
    "text-to-video",
]

STALE = [
    "11 computadores do escritório",
    "11 office computers",
    "11 + TV",
    "3h → 5min",
    "3 hours to 5 minutes",
    "PlanilhaCompras",
    "ProcureFlow",
    "Portal Vesper",
    "Procurement e sourcing validados em sandbox",
    "Procurement and sourcing validated in sandbox",
    "Facebook e Instagram validados em teste",
    "Facebook and Instagram validated in testing",
    "ultrapassou 10 mil execuções em produção",
    "surpassed 10,000 production executions",
    "portal-dev-only",
    "vesper_admin",
]

REQUIRED = {
    "index.html": [
        "RESULTADOS EM USO",
        "PROJETOS PRINCIPAIS",
        "Alguns números da minha atuação atual.",
        "10+ PCs · 1 TV · 9 setores",
        "base de 1.020 contatos",
        "Catálogo Operacional de Compras",
        "revalidação técnica antes do piloto interno",
    ],
    "en/index.html": [
        "RESULTS IN USE",
        "MAIN PROJECTS",
        "A few numbers from my current work.",
        "10+ PCs · 1 TV · 9 areas",
        "1,020-contact base",
        "Operational Procurement Catalog",
        "technical revalidation before an internal pilot",
    ],
    "competencias/index.html": [
        "COMPETÊNCIAS E EXPERIÊNCIA PRÁTICA",
        "ONDE APLICO NA ROTINA",
        "IA multimodal",
        "10 mil execuções de workflows em produção",
        "AWS",
    ],
    "en/skills/index.html": [
        "SKILLS AND PRACTICAL EXPERIENCE",
        "WHERE I USE IT IN PRACTICE",
        "multimodal AI",
        "10,000 workflow executions in production",
        "AWS",
    ],
}


def main() -> int:
    errors: list[str] = []
    public_files = [ROOT / "README.md"] + [
        path for path in ROOT.rglob("*.html") if "artifacts" not in path.parts
    ]

    for path in sorted(public_files):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        for phrase in FORBIDDEN:
            if phrase in text:
                errors.append(f"{relative}: external-review or artificial wording remains: {phrase}")
        for phrase in STALE:
            if phrase in text:
                errors.append(f"{relative}: stale wording, metric, status or credential remains: {phrase}")

    for relative, phrases in REQUIRED.items():
        path = ROOT / relative
        if not path.exists():
            errors.append(f"missing strategic page: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{relative}: required current wording missing: {phrase}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        "Natural first-person public voice, current claims and public-secret hygiene "
        f"validated across {len(public_files)} public files."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
