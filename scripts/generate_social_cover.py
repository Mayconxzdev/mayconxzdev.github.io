from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "social" / "og-cover.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630
BG = (245, 242, 235)
BLACK = (20, 20, 18)
ORANGE = (209, 63, 26)
BLUE = (32, 92, 122)
MUTED = (98, 95, 87)
WHITE = (250, 250, 247)
LINE = (184, 180, 170)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(name: str, size: int):
    path = FONT_DIR / name
    if path.exists():
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


mono = font("DejaVuSansMono.ttf", 15)
mono_bold = font("DejaVuSansMono-Bold.ttf", 14)
name_font = font("DejaVuSansCondensed-Bold.ttf", 78)
title_font = font("DejaVuSans-Bold.ttf", 28)
tech_font = font("DejaVuSans.ttf", 24)
metric_font = font("DejaVuSans-Bold.ttf", 27)
label_font = font("DejaVuSans.ttf", 15)
footer_font = font("DejaVuSansMono.ttf", 16)
monogram_font = font("DejaVuSans-Bold.ttf", 78)

image = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(image)

# Brand frame.
draw.rectangle((0, 0, W, 18), fill=ORANGE)
split = 830
draw.line((split, 55, split, 535), fill=LINE, width=1)

# Positioning and stack. Keep these claims synchronized with CAREER_EVIDENCE.md.
draw.text((55, 78), "AUTOMAÇÃO · IA APLICADA · INTEGRAÇÕES · 2026", font=mono, fill=ORANGE)
draw.text((55, 145), "MAYCON", font=name_font, fill=BLACK)
draw.text((55, 225), "FERREIRA", font=name_font, fill=BLACK)
draw.text((55, 340), "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES", font=title_font, fill=BLACK)
draw.text((55, 388), "n8n · Python · FastAPI · APIs REST · RAG/grounding", font=tech_font, fill=BLUE)

# End-to-end delivery narrative.
items = ["PROCESSO", "INTEGRAÇÃO", "IMPLANTAÇÃO", "SUSTENTAÇÃO"]
x, y = 55, 478
for number, item in enumerate(items, 1):
    draw.text((x, y), f"{number:02d}", font=mono, fill=ORANGE)
    x += 30
    draw.text((x, y), item, font=mono_bold, fill=BLACK)
    x += draw.textlength(item, font=mono_bold) + 25
    if number < len(items):
        draw.line((x, y + 10, x + 20, y + 10), fill=LINE, width=2)
        x += 34

# Monogram card.
draw.rectangle((875, 95, 1120, 350), fill=BLACK)
draw.rectangle((875, 95, 889, 350), fill=ORANGE)
draw.text((924, 150), "MF", font=monogram_font, fill=WHITE)
draw.text((920, 285), "AUTOMAÇÃO / IA /", font=mono, fill=WHITE)
draw.text((920, 310), "INTEGRAÇÕES", font=mono_bold, fill=WHITE)

# Only canonical, evidenced metrics.
metrics = [
    ("10 mil+", "execuções n8n"),
    ("<30 s", "propostas simples"),
    ("20+", "profissionais"),
    ("9", "setores produtivos"),
]
positions = [(875, 385), (1010, 385), (875, 465), (1010, 465)]
for (value, label), (mx, my) in zip(metrics, positions):
    draw.text((mx, my), value, font=metric_font, fill=BLACK)
    draw.text((mx, my + 36), label, font=label_font, fill=MUTED)

# Evidence-first footer.
draw.line((55, 545, 1145, 545), fill=BLACK, width=2)
draw.text((55, 570), "EVIDÊNCIAS · ESTADOS DECLARADOS · LIMITES EXPLÍCITOS", font=footer_font, fill=BLACK)
draw.text((905, 570), "mayconxzdev.github.io", font=footer_font, fill=BLUE)

image.save(OUT, optimize=True)
print(f"Generated {OUT} ({W}x{H})")
