from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = {
    'competencias/index.html': [
        'RASTREABILIDADE, RASTREABILIDADE',
        'CONFIABILIDADE, CONFIABILIDADE',
        'SEGURANÇA, SEGURANÇA',
    ],
    'en/skills/index.html': [
        'TRACEABILITY, TRACEABILITY',
        'RELIABILITY, RELIABILITY',
        'SECURITY, SECURITY',
    ],
}

errors = []
for relative, forbidden in CHECKS.items():
    path = ROOT / relative
    text = path.read_text(encoding='utf-8')
    for phrase in forbidden:
        if phrase in text:
            errors.append(f'{relative}: duplicated editorial phrase: {phrase}')

if errors:
    raise SystemExit('\n'.join(errors))

print('Editorial repetition guard passed for PT/EN skills pages.')
