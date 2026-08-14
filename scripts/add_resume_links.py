from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / "assets" / "cv"

FILES = [
    CV / "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    CV / "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
]

# The generator now embeds these annotations directly. This pass remains as a
# defensive fallback for older/generated PDFs and is intentionally idempotent.
LINKS = [
    (["+55 (21) 96481-0480"], "tel:+5521964810480"),
    (["E-mail", "Email", "mayconxz00dev@gmail.com"], "mailto:mayconxz00dev@gmail.com"),
    (["LinkedIn", "linkedin.com/in/maycon-ferreira-7bb870231/"], "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"),
    (["GitHub", "github.com/Mayconxzdev"], "https://github.com/Mayconxzdev"),
    (["Portfólio", "Portfolio", "mayconxzdev.github.io"], "https://mayconxzdev.github.io/"),
]

for path in FILES:
    if not path.exists():
        raise SystemExit(f"Missing generated resume: {path}")
    doc = fitz.open(path)
    if len(doc) != 1:
        doc.close()
        raise SystemExit(f"{path.name}: expected one page before adding links")
    page = doc[0]
    existing = {item.get("uri") for item in page.get_links() if item.get("uri")}
    changed = False

    for visible_candidates, uri in LINKS:
        if uri in existing:
            continue
        match = None
        for visible_text in visible_candidates:
            matches = page.search_for(visible_text)
            if matches:
                match = matches[0]
                break
        if match is None:
            doc.close()
            raise SystemExit(f"{path.name}: could not locate contact label for link: {uri}")
        page.insert_link({"kind": fitz.LINK_URI, "from": match, "uri": uri})
        existing.add(uri)
        changed = True

    if changed:
        temp = path.with_name(path.stem + ".linked.pdf")
        doc.save(temp, garbage=4, deflate=True)
        doc.close()
        temp.replace(path)
        print(f"Clickable contact fallback applied: {path.name}")
    else:
        doc.close()
        print(f"Clickable contact links already embedded: {path.name}")
