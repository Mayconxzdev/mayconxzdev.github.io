from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATCHES = {
    "competencias/index.html": [
        (
            "A instância n8n que administro ultrapassou 10 mil execuções em produção.",
            "A instância n8n que administro ultrapassou 10 mil execuções de workflows em produção.",
        ),
    ],
    "en/skills/index.html": [
        (
            "The n8n environment I administer has surpassed 10,000 production executions.",
            "The n8n environment I administer has surpassed 10,000 workflow executions in production.",
        ),
    ],
    "cases/compras-vesper/index.html": [
        (
            "../../assets/evidence/compras-menu.webp",
            "https://raw.githubusercontent.com/Mayconxzdev/ComprasProducao/main/docs/assets/ui-dashboard-real.png",
        ),
        (
            "../../assets/evidence/compras-frete.webp",
            "https://raw.githubusercontent.com/Mayconxzdev/ComprasProducao/main/docs/assets/ui-freight-real.png",
        ),
        (
            "../../assets/evidence/compras-acompanhar.webp",
            "https://raw.githubusercontent.com/Mayconxzdev/ComprasProducao/main/docs/assets/ui-tracking-real.png",
        ),
    ],
    "cases/infinity-engine/index.html": [
        (
            "Aplicação privada: a material público é a arquitetura declarada, não uma captura de interface.",
            "Como a aplicação é privada, publico apenas a arquitetura e o fluxo — não capturas da interface interna.",
        ),
    ],
    "cases/vesper-manutencao/index.html": [
        (
            "../../assets/evidence/manutencao-dashboard.webp",
            "../../assets/evidence/manutencao-dashboard.svg",
        ),
        (
            "../../assets/evidence/manutencao-equipment.webp",
            "../../assets/evidence/manutencao-equipment.svg",
        ),
        (
            "../../assets/evidence/manutencao-document.webp",
            "../../assets/evidence/manutencao-document.svg",
        ),
        (
            "../../assets/evidence/manutencao-chat.webp",
            "../../assets/evidence/manutencao-chat.svg",
        ),
    ],
}


def main() -> None:
    for relative, replacements in PATCHES.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        for old, new in replacements:
            if old in text:
                text = text.replace(old, new)
            elif new not in text:
                raise RuntimeError(f"{relative}: expected content not found: {old}")
        path.write_text(text, encoding="utf-8")
        print(f"final quality patch current: {relative}")


if __name__ == "__main__":
    main()
