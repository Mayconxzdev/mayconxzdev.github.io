from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATCHES = {
    "index.html": [
        ("sustentação. Treinei e orientei 30+ pessoas", "sustentação; treinei e orientei 30+ pessoas"),
    ],
    "en/cases/compass/index.html": [
        ("A six-month, ten-sprint program progressing", "A six-month program with ten sprints, progressing"),
    ],
}

for relative, replacements in PATCHES.items():
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
        elif new not in text:
            raise RuntimeError(f"{relative}: expected wording not found: {old}")
    path.write_text(text, encoding="utf-8")
    print(f"wording normalized: {relative}")
