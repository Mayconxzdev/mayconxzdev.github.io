from __future__ import annotations

import html
from pathlib import Path
import re
import subprocess

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
        "Catálogo Operacional",
        "produto atual permanece em revalidação",
    ],
    "en/index.html": [
        "RESULTS IN USE",
        "FEATURED PROJECTS",
        "A few results from my current work.",
        "10+ PCs · 1 TV · 9 departments",
        "1,020-contact base",
        "Operational Procurement Catalog",
        "current product remains under revalidation",
    ],
    "competencias/index.html": [
        "COMPETÊNCIAS E EXPERIÊNCIA PRÁTICA",
        "ONDE APLICO NA ROTINA",
        "multimodalidade",
        "10 mil execuções de workflows em produção",
        "AWS",
    ],
    "en/skills/index.html": [
        "SKILLS AND PRACTICAL EXPERIENCE",
        "WHERE I USE IT IN PRACTICE",
        "multimodal workflows",
        "10,000 workflow executions in production",
        "AWS",
    ],
}

ENGLISH_CASE_METADATA = {
    "en/cases/vesper-propostas/index.html": "Commercial Proposal | Maycon Ferreira",
    "en/cases/manutencao-campo/index.html": "Field Maintenance | Maycon Ferreira",
    "en/cases/whatsapp/index.html": "WhatsApp Notifications | Maycon Ferreira",
    "en/cases/portfolio-2026/index.html": "Systems in Operation — Portfolio | Maycon Ferreira",
}


def main() -> int:
    errors: list[str] = []
    tracked = subprocess.run(
        [
            "git",
            "-C",
            str(ROOT),
            "ls-files",
            "-z",
            "--",
            "README.md",
            "index.html",
            "404.html",
            "cases",
            "competencias",
            "en",
        ],
        check=True,
        capture_output=True,
    )
    tracked_files = [
        ROOT / item.decode("utf-8")
        for item in tracked.stdout.split(b"\0")
        if item
    ]
    public_files = sorted(
        path
        for path in tracked_files
        if path.name == "README.md" or path.suffix.lower() == ".html"
    )

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

    for relative, expected_title in ENGLISH_CASE_METADATA.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        lang = re.search(r"<html\b[^>]*\blang=[\"']([^\"']+)", text, re.IGNORECASE)
        title = re.search(r"<title>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
        og_title = re.search(
            r"<meta\b(?=[^>]*\bproperty=[\"']og:title[\"'])(?=[^>]*\bcontent=[\"']([^\"']*)[\"'])[^>]*>",
            text,
            re.IGNORECASE,
        )
        heading = re.search(r"<h1\b[^>]*>(.*?)</h1>", text, re.IGNORECASE | re.DOTALL)
        plain_heading = html.unescape(re.sub(r"<[^>]+>", "", heading.group(1))).strip() if heading else ""
        if not lang or lang.group(1).lower() != "en":
            errors.append(f"{relative}: page language must be English")
        if not title or html.unescape(title.group(1)).strip() != expected_title:
            errors.append(f"{relative}: page title must match approved English title")
        if not og_title or html.unescape(og_title.group(1)).strip() != expected_title:
            errors.append(f"{relative}: Open Graph title must match approved English title")
        if plain_heading != expected_title.split(" | ", 1)[0]:
            errors.append(f"{relative}: H1 must match approved English title")

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
