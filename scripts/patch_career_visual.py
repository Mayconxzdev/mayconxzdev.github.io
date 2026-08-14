from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    ROOT / "index.html",
    ROOT / "en" / "index.html",
    ROOT / "cases" / "carreira-pessoal" / "index.html",
    ROOT / "en" / "cases" / "career-personal" / "index.html",
]

PAIRS = [
    ("assets/evidence/carreira-overview.webp", "assets/evidence/carreira-product-overview.svg"),
    ("../assets/evidence/carreira-overview.webp", "../assets/evidence/carreira-product-overview.svg"),
    ("../../assets/evidence/carreira-overview.webp", "../../assets/evidence/carreira-product-overview.svg"),
    ("../../../assets/evidence/carreira-overview.webp", "../../../assets/evidence/carreira-product-overview.svg"),
    ('alt="Telas reais do CarreiraPessoal"', 'alt="Mapa visual sanitizado do CarreiraPessoal"'),
    ('alt="Real CarreiraPessoal screens"', 'alt="Sanitized visual map of CarreiraPessoal"'),
    ('alt="Conjunto de telas reais do CarreiraPessoal mostrando início, oportunidades, candidaturas, perfil, fontes e recursos"', 'alt="Mapa visual sanitizado do CarreiraPessoal mostrando Hoje, Oportunidades, Candidaturas, Perfil, Fontes e Recursos"'),
    ('alt="Real CarreiraPessoal screens showing Today, Opportunities, Applications, Profile, Sources and Resources"', 'alt="Sanitized CarreiraPessoal visual map showing Today, Opportunities, Applications, Profile, Sources and Resources"'),
    ("Telas reais da v12.5.2. O material público evita expor candidaturas, dados pessoais e credenciais.", "Mapa visual sanitizado da v12.5.2. Não é screenshot da interface e não expõe candidaturas, dados pessoais ou credenciais."),
    ("Real v12.5.2 screens. The public material avoids exposing applications, personal data and credentials.", "Sanitized v12.5.2 product map. It is not a UI screenshot and does not expose applications, personal data or credentials."),
    ("Telas reais da v12.5.2.", "Mapa visual sanitizado da v12.5.2."),
    ("Real v12.5.2 product screens.", "Sanitized v12.5.2 product map."),
]

for path in FILES:
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    for old, new in PAIRS:
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

print("CarreiraPessoal visual evidence now uses a valid, explicitly sanitized product map.")
