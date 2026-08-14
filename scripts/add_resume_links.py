from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / "assets" / "cv"

FILES = [
    CV / "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    CV / "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
]

LINKS = [
    ("+55 (21) 96481-0480", "tel:+5521964810480"),
    ("mayconxz00dev@gmail.com", "mailto:mayconxz00dev@gmail.com"),
    ("linkedin.com/in/maycon-ferreira-7bb870231/", "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"),
    ("github.com/Mayconxzdev", "https://github.com/Mayconxzdev"),
    ("mayconxzdev.github.io", "https://mayconxzdev.github.io/"),
]

for path in FILES:
    if not path.exists():
        raise SystemExit(f"Missing generated resume: {path}")
    doc = fitz.open(path)
    if len(doc) != 1:
        doc.close()
        raise SystemExit(f"{path.name}: expected one page before adding links")
    page = doc[0]
    for visible_text, uri in LINKS:
        matches = page.search_for(visible_text)
        if not matches:
            doc.close()
            raise SystemExit(f"{path.name}: could not locate contact text for link: {visible_text}")
        page.insert_link({"kind": fitz.LINK_URI, "from": matches[0], "uri": uri})
    temp = path.with_name(path.stem + ".linked.pdf")
    doc.save(temp, garbage=4, deflate=True)
    doc.close()
    temp.replace(path)
    print(f"Clickable contact links added: {path.name}")
