from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "Text-to-video": "Geração de mídia",
    "text-to-video": "geração de mídia",
    "11 computadores do escritório e na TV da fábrica": "10+ computadores e uma TV, apoiando 20+ profissionais em nove setores produtivos",
    "11 office computers and the factory TV": "10+ computers and one factory TV, supporting 20+ professionals across nine production areas",
    "11 computadores e uma TV": "10+ computadores e uma TV",
    "11 workstations and a factory TV": "10+ computers and one factory TV",
    "11 + TV": "10+ PCs · 1 TV",
    "PlanilhaCompras": "CatalogoOperacional",
    "https://github.com/Mayconxzdev/PlanilhaCompras": "https://github.com/Mayconxzdev/CatalogoOperacional",
    "Primeira campanha com mais de 900 destinatários.": "Seis campanhas sobre uma base de 1.020 contatos, incluindo uma para 900+ destinatários.",
    "First campaign with more than 900 recipients.": "Six campaigns over a 1,020-contact base, including one for 900+ recipients.",
    "Publicação multi-imagem confirmada no Facebook.": "Facebook e Instagram foram exercitados em teste; os limites externos estão documentados por canal.",
    "Multi-image Facebook publication confirmed.": "Facebook and Instagram were exercised in testing; external limits are documented by channel.",
    "Procurement e sourcing validados em sandbox; preparação para piloto interno.": "Procurement foi exercitado em sandbox; o head atual passa por revalidação antes do piloto interno.",
    "Procurement and sourcing validated in sandbox; preparation for an internal pilot.": "Procurement was exercised in sandbox; the current head is being revalidated before an internal pilot.",
    "Procurement validado em sandbox · pré-piloto": "Procurement exercitado em sandbox · revalidação pré-piloto",
    "Procurement validated in sandbox · pre-pilot": "Procurement exercised in sandbox · pre-pilot revalidation",
    "Estágio em TI / Dados": "Programa de Bolsas em Engenharia de Dados",
    "IT / Data Internship": "Data Engineering Scholarship Program",
    "uma rotina observada caiu de aproximadamente três horas para cinco minutos": "dez sprints práticas cobriram um pipeline analítico em AWS",
    "an observed routine went from approximately three hours to five minutes": "ten practical sprints covered an analytical AWS pipeline",
    "3h → 5min": "10 sprints em dados",
    "3 hours to 5 minutes": "10 data sprints",
    "cases/compass-automation/": "cases/compass/",
    "EM PRODUÇÃO · USO INTERNO": "USO INTERNO",
    "IN PRODUCTION · INTERNAL USE": "INTERNAL USE",
}


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if "artifacts" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in REPLACEMENTS.items():
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
            print(f"facts reconciled: {path.relative_to(ROOT)}")
    print(f"facts reconciled in {changed} public files")


if __name__ == "__main__":
    main()
