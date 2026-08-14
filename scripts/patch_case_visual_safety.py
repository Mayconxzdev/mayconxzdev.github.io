from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    'cases/producao-operacional/index.html': [
        ('<h1>Produção Operacional</h1>', '<h1>Produção<br>Operacional</h1>'),
    ],
    'en/cases/producao-operacional/index.html': [
        ('<h1>Production Operations</h1>', '<h1>Production<br>Operations</h1>'),
    ],
    'cases/carreira-pessoal/index.html': [
        ('<h1>CarreiraPessoal</h1>', '<h1>Carreira<wbr>Pessoal</h1>'),
    ],
    'en/cases/career-personal/index.html': [
        ('<h1>CarreiraPessoal</h1>', '<h1>Carreira<wbr>Pessoal</h1>'),
    ],
    'cases/compras-vesper/index.html': [
        ('<h1>ComprasVesper</h1>', '<h1>Compras<wbr>Vesper</h1>'),
    ],
    'en/cases/compras-vesper/index.html': [
        ('<h1>ComprasVesper</h1>', '<h1>Compras<wbr>Vesper</h1>'),
    ],
    'cases/infinity-engine/index.html': [
        (
            '<div class="case-gallery-heading"><p>TELAS E FLUXOS</p><div><h2>Veja o sistema em uso</h2><span>Telas e fluxos que mostram como o sistema funciona na prática.</span></div></div>',
            '<div class="case-gallery-heading"><p>ARQUITETURA E FLUXO</p><div><h2>Como o sistema funciona</h2><span>Representações sanitizadas da arquitetura e dos pontos de controle — não são capturas da interface interna.</span></div></div>',
        ),
        (
            '<div><p class="eyebrow">Sobre as imagens</p><p>As imagens abaixo mostram o produto real ou reconstruções sanitizadas. Quando algo não é uma captura direta, isso fica indicado na própria legenda.</p></div>',
            '<div><p class="eyebrow">O que está representado</p><p>Os cards descrevem componentes, regras e pontos de controle do fluxo privado sem reproduzir a interface ou dados internos.</p></div>',
        ),
    ],
    'en/cases/infinity-engine/index.html': [
        (
            '<div class="case-gallery-heading"><p>SCREENS AND FLOWS</p><div><h2>See the system in use</h2><span>Screens and flows that show how the system works in practice.</span></div></div>',
            '<div class="case-gallery-heading"><p>ARCHITECTURE AND FLOW</p><div><h2>How the system works</h2><span>Sanitized representations of the architecture and control points — not screenshots of the private interface.</span></div></div>',
        ),
        (
            '<div><p class="eyebrow">About the images</p><p>The images below show the real product or sanitized reconstructions. When something is not a direct capture, the caption says so.</p></div>',
            '<div><p class="eyebrow">What is represented</p><p>The cards describe components, rules and control points in the private flow without reproducing the interface or internal data.</p></div>',
        ),
    ],
    'cases/whatsapp/index.html': [
        (
            '<div class="case-gallery-heading"><p>TELAS E FLUXOS</p><div><h2>Veja o sistema em uso</h2><span>Telas e fluxos que mostram como o sistema funciona na prática.</span></div></div>',
            '<div class="case-gallery-heading"><p>ARQUITETURA E FLUXO</p><div><h2>Como a integração opera</h2><span>Fluxos técnicos sanitizados da entrega e do fallback — não são capturas do aplicativo de mensagens.</span></div></div>',
        ),
        (
            '<div><p class="eyebrow">Sobre as imagens</p><p>As imagens abaixo mostram o produto real ou reconstruções sanitizadas. Quando algo não é uma captura direta, isso fica indicado na própria legenda.</p></div>',
            '<div><p class="eyebrow">O que está representado</p><p>Os cards mostram o encadeamento técnico da notificação e do fallback sem expor conversas, números, logs ou credenciais.</p></div>',
        ),
    ],
    'en/cases/whatsapp/index.html': [
        (
            '<div class="case-gallery-heading"><p>SCREENS AND FLOWS</p><div><h2>See the system in use</h2><span>Screens and flows that show how the system works in practice.</span></div></div>',
            '<div class="case-gallery-heading"><p>ARCHITECTURE AND FLOW</p><div><h2>How the integration operates</h2><span>Sanitized technical flows for delivery and fallback — not screenshots of the messaging application.</span></div></div>',
        ),
        (
            '<div><p class="eyebrow">About the images</p><p>The images below show the real product or sanitized reconstructions. When something is not a direct capture, the caption says so.</p></div>',
            '<div><p class="eyebrow">What is represented</p><p>The cards show the technical notification and fallback chain without exposing conversations, phone numbers, logs or credentials.</p></div>',
        ),
    ],
}

for relative, pairs in REPLACEMENTS.items():
    path = ROOT / relative
    text = path.read_text(encoding='utf-8')
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new, 1)
    path.write_text(text, encoding='utf-8')

css = ROOT / 'css' / 'layout-safety.css'
text = css.read_text(encoding='utf-8')
marker = '/* Case title wrapping: prefer semantic breaks over mid-word fragmentation. */'
block = '''\n/* Case title wrapping: prefer semantic breaks over mid-word fragmentation. */\n.case-identity h1{overflow-wrap:normal;word-break:normal;hyphens:none;text-wrap:balance}\n.case-identity h1 wbr{display:inline}\n'''
if marker not in text:
    css.write_text(text.rstrip() + '\n' + block, encoding='utf-8')

print('Case title wrapping and confidential evidence labels normalized.')
