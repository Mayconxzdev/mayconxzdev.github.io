from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[1]

for rel, lang in [('index.html', 'pt'), ('en/index.html', 'en')]:
    p = root / rel
    text = p.read_text(encoding='utf-8')
    marker = '<article class="feature-case feature-case--portal-vesper feature-case--reverse">'
    if marker not in text:
        raise RuntimeError(f'{rel}: marker missing')

    if 'data-project="carreira-pessoal"' not in text:
        if lang == 'pt':
            card = '''<article class="feature-case feature-case--portal-vesper feature-case--reverse" data-project="carreira-pessoal"><div class="feature-case__copy"><div class="case-index"><span>04</span><span class="status status--public">PRODUTO PESSOAL</span></div><p class="case-category">Produto Windows local-first</p><h3>CarreiraPessoal</h3><p class="case-summary">Eu criei este produto para parar de perder tempo com vagas duplicadas, versões de currículo e buscas espalhadas. Hoje uso o app para descobrir oportunidades, decidir o que vale meu tempo e acompanhar cada candidatura.</p><div class="case-impact"><small>Engenharia</small><strong>102 famílias ATS reconhecidas, 11 coletores diretos; v12.5.2 registrada com 283 testes Python.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5</p><div class="project-links"><a class="text-link" href="cases/carreira-pessoal/">Abrir case<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/CarreiraPessoal">Ver código<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><figure class="case-showcase"><div class="case-showcase__frame"><img src="assets/evidence/carreira-overview.webp" alt="Telas reais do CarreiraPessoal mostrando início, oportunidades, candidaturas e fontes" loading="lazy" decoding="async"></div><figcaption><span class="evidence-label">PRODUTO REAL</span><strong>O fluxo que eu uso para organizar minha própria busca.</strong></figcaption></figure></div></article>'''
        else:
            card = '''<article class="feature-case feature-case--portal-vesper feature-case--reverse" data-project="carreira-pessoal"><div class="feature-case__copy"><div class="case-index"><span>04</span><span class="status status--public">PERSONAL PRODUCT</span></div><p class="case-category">Local-first Windows product</p><h3>CarreiraPessoal</h3><p class="case-summary">I built this product to stop wasting time on duplicate roles, scattered searches and resume versions. I use it to discover opportunities, decide what is worth my time and track each application.</p><div class="case-impact"><small>Engineering</small><strong>102 ATS/career-platform families recognized, 11 direct collectors; v12.5.2 recorded with 283 Python tests.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5</p><div class="project-links"><a class="text-link" href="cases/career-personal/">Open case<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/CarreiraPessoal">View code<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><figure class="case-showcase"><div class="case-showcase__frame"><img src="../assets/evidence/carreira-overview.webp" alt="Real CarreiraPessoal screens showing home, opportunities, applications and sources" loading="lazy" decoding="async"></div><figcaption><span class="evidence-label">REAL PRODUCT</span><strong>The workflow I use for my own job search.</strong></figcaption></figure></div></article>'''
        text = text.replace(marker, card + '\n\n        ' + marker, 1)

    archive = '<div class="archive-list" id="project-grid">'
    if 'quality-automation-pilot' not in text:
        if lang == 'pt':
            row = '<article class="archive-row persp-process persp-automation persp-architecture" data-search="quality-automation-pilot"><span class="archive-number">08</span><div class="archive-name"><h3>Central ISO</h3><p>Piloto técnico criado com requisitos reais da Qualidade para organizar documentos, vencimentos e pendências sem alterar a fonte oficial.</p></div><div class="archive-state"><span class="status status--pilot">PILOTO TÉCNICO</span><small>regras determinísticas · revisão humana</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="cases/central-iso/" aria-label="Abrir case Central ISO">↗</a></article>'
        else:
            row = '<article class="archive-row persp-process persp-automation persp-architecture" data-search="quality-automation-pilot"><span class="archive-number">08</span><div class="archive-name"><h3>Central ISO</h3><p>Technical pilot based on real Quality requirements to organize documents, expiration dates and pending items without changing the official source.</p></div><div class="archive-state"><span class="status status--pilot">TECHNICAL PILOT</span><small>deterministic rules · human review</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="cases/central-iso/" aria-label="Open Central ISO case">↗</a></article>'
        if archive not in text:
            raise RuntimeError(f'{rel}: archive marker missing')
        text = text.replace(archive, archive + '\n        ' + row, 1)

    p.write_text(text, encoding='utf-8')

runpy.run_path(str(root / 'scripts' / 'patch_maintenance_case.py'), run_name='__main__')
runpy.run_path(str(root / 'scripts' / 'patch_proposal_case_pt.py'), run_name='__main__')
print('CarreiraPessoal and Central ISO presentation refreshed with real-state links and visual evidence.')
