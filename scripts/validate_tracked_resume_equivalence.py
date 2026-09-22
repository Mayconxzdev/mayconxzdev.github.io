from __future__ import annotations

from pathlib import Path
import sys
import fitz

FILES = [
    "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    "Maycon_Ferreira_Automacao_IA_n8n_Python_LLMs.pdf",
    "Maycon_Ferreira_Automacao_BI_Power_Automate_Power_BI.pdf",
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
]


def page_signature(page: fitz.Page):
    spans = []
    data = page.get_text("dict")
    for block in data.get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = " ".join(str(span.get("text", "")).split())
                if not text:
                    continue
                bbox = tuple(round(float(v), 1) for v in span.get("bbox", (0, 0, 0, 0)))
                spans.append((
                    text,
                    round(float(span.get("size", 0.0)), 2),
                    str(span.get("font", "")),
                    bbox,
                ))
    links = sorted(
        link.get("uri")
        for link in page.get_links()
        if link.get("uri")
    )
    return spans, links


def signature(path: Path):
    doc = fitz.open(path)
    try:
        return [
            (
                round(page.rect.width, 1),
                round(page.rect.height, 1),
                *page_signature(page),
            )
            for page in doc
        ]
    finally:
        doc.close()


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: validate_tracked_resume_equivalence.py <tracked_dir> <generated_dir>")

    tracked_dir = Path(sys.argv[1])
    generated_dir = Path(sys.argv[2])
    failures = []

    for name in FILES:
        tracked = tracked_dir / name
        generated = generated_dir / name
        if not tracked.exists() or not generated.exists():
            failures.append(f"{name}: missing tracked or generated file")
            continue
        if signature(tracked) != signature(generated):
            failures.append(f"{name}: tracked PDF content/layout/links differ from freshly generated PDF")
        else:
            print(f"OK tracked resume equivalent: {name}")

    if failures:
        for failure in failures:
            print(f"ERROR {failure}")
        return 1

    print("Tracked resume PDFs are semantically and visually equivalent to freshly generated output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
