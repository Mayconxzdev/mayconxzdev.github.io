from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / "assets" / "cv"
FILES = {
    "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf": [
        "RESUMO PROFISSIONAL",
        "COMPETÊNCIAS",
        "EXPERIÊNCIA",
        "PROJETOS SELECIONADOS",
        "FORMAÇÃO",
        "CURSOS E CERTIFICAÇÕES",
        "IDIOMAS",
    ],
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf": [
        "PROFESSIONAL SUMMARY",
        "CORE SKILLS",
        "EXPERIENCE",
        "SELECTED PROJECTS",
        "EDUCATION",
        "COURSES & CREDENTIALS",
        "LANGUAGES",
    ],
}


@dataclass
class TextLine:
    text: str
    x0: float
    y0: float
    x1: float
    y1: float
    min_size: float
    baseline: float


def extract_lines(page: fitz.Page) -> list[TextLine]:
    lines: list[TextLine] = []
    data = page.get_text("dict", flags=fitz.TEXTFLAGS_TEXT)
    for block in data.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = [span for span in line.get("spans", []) if span.get("text", "").strip()]
            if not spans:
                continue
            text = "".join(span["text"] for span in spans).strip()
            x0 = min(float(span["bbox"][0]) for span in spans)
            y0 = min(float(span["bbox"][1]) for span in spans)
            x1 = max(float(span["bbox"][2]) for span in spans)
            y1 = max(float(span["bbox"][3]) for span in spans)
            min_size = min(float(span["size"]) for span in spans)
            baseline = sum(float(span["origin"][1]) for span in spans) / len(spans)
            lines.append(TextLine(text, x0, y0, x1, y1, min_size, baseline))
    return sorted(lines, key=lambda item: (item.y0, item.x0))


def merge_same_rows(lines: list[TextLine]) -> list[TextLine]:
    rows: list[TextLine] = []
    for line in lines:
        if rows and abs(rows[-1].baseline - line.baseline) < 0.8:
            previous = rows[-1]
            rows[-1] = TextLine(
                text=f"{previous.text} {line.text}".strip(),
                x0=min(previous.x0, line.x0),
                y0=min(previous.y0, line.y0),
                x1=max(previous.x1, line.x1),
                y1=max(previous.y1, line.y1),
                min_size=min(previous.min_size, line.min_size),
                baseline=(previous.baseline + line.baseline) / 2,
            )
        else:
            rows.append(line)
    return rows


def main() -> int:
    errors: list[str] = []
    for filename, headings in FILES.items():
        path = CV / filename
        doc = fitz.open(path)
        if doc.page_count != 1:
            errors.append(f"{filename}: expected one page")
            continue
        page = doc[0]
        rows = merge_same_rows(extract_lines(page))
        if not rows:
            errors.append(f"{filename}: no text lines found")
            continue

        pixmap = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
        if pixmap.width < 890 or pixmap.height < 1260 or len(pixmap.samples) == 0:
            errors.append(f"{filename}: raster render is invalid")

        for row in rows:
            if row.min_size < 7.9:
                errors.append(f"{filename}: text smaller than 7.9 pt: {row.min_size:.2f} in {row.text[:60]!r}")
            if row.x0 < 28 or row.x1 > page.rect.width - 28:
                errors.append(f"{filename}: text leaves horizontal safe area: {row.text[:60]!r}")

        for previous, current in zip(rows, rows[1:]):
            overlap = previous.y1 - current.y0
            if overlap > 2.0:
                errors.append(
                    f"{filename}: overlapping text rows ({overlap:.2f} pt): {previous.text[:42]!r} / {current.text[:42]!r}"
                )

        for heading in headings:
            index = next((i for i, row in enumerate(rows) if heading in row.text), None)
            if index is None:
                errors.append(f"{filename}: heading not found visually: {heading}")
                continue
            if index > 0:
                before = rows[index].y0 - rows[index - 1].y1
                if before < 4.0:
                    errors.append(f"{filename}: insufficient spacing before {heading}: {before:.2f} pt")
            if index + 1 < len(rows):
                after = rows[index + 1].y0 - rows[index].y1
                if after < 2.0:
                    errors.append(f"{filename}: insufficient spacing after {heading}: {after:.2f} pt")

        bottom_margin = page.rect.height - max(row.y1 for row in rows)
        if bottom_margin < 34:
            errors.append(f"{filename}: bottom margin too small: {bottom_margin:.1f} pt")
        if bottom_margin > 110:
            errors.append(f"{filename}: page is underused: bottom margin {bottom_margin:.1f} pt")

        print(
            f"OK: {filename} | {len(rows)} visual rows | min font {min(row.min_size for row in rows):.2f} pt | "
            f"bottom margin {bottom_margin:.1f} pt"
        )

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Resume visual-layout validation completed without errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
