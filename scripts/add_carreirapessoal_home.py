from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
for rel,lang in [('index.html','pt'),('en/index.html','en')]:
    p=root/rel; text=p.read_text(encoding='utf-8')
    marker='<article class="feature-case feature-case--portal-vesper feature-case--reverse">'
    if marker not in text: raise RuntimeError(f'{rel}: marker missing')
    if 'Career Goal · EvidenceGuard · Resume Router' not in text:
        if lang=='pt':
            card='''<article class="feature-case feature-case--portal-vesper feature-case--reverse"><div class="feature-case__copy"><div class="case-index"><span>06</span><span class="status status--public">PRODUTO PESSOAL</span></div><p class="case-category">Career intelligence local-first</p><h3>CarreiraPessoal</h3><p class="case-summary">Sistema que uso na própria busca para descobrir e deduplicar vagas, avaliar direção profissional, reconciliar evidências, preparar currículos e acompanhar candidaturas.</p><div class="case-impact"><small>Engenharia</small><strong>102 famílias ATS reconhecidas, 11 coletores diretos; v12.5.2 registrada com 283 testes Python.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5</p><div class="project-links"><a class="text-link" href="https://github.com/Mayconxzdev/CarreiraPessoal">Ver repositório<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><div class="visual visual--portal"><div class="portal-core"><span>LOCAL-FIRST</span><b>CarreiraPessoal</b><small>Career Goal · EvidenceGuard · Resume Router</small></div></div></div></article>'''
        else:
            card='''<article class="feature-case feature-case--portal-vesper feature-case--reverse"><div class="feature-case__copy"><div class="case-index"><span>06</span><span class="status status--public">PERSONAL PRODUCT</span></div><p class="case-category">Local-first career intelligence</p><h3>CarreiraPessoal</h3><p class="case-summary">A system I use in my own search to discover and deduplicate roles, evaluate career direction, reconcile evidence, prepare resumes and track applications.</p><div class="case-impact"><small>Engineering</small><strong>102 ATS/career-platform families recognized, 11 direct collectors; v12.5.2 recorded with 283 Python tests.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5</p><div class="project-links"><a class="text-link" href="https://github.com/Mayconxzdev/CarreiraPessoal">View repository<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><div class="visual visual--portal"><div class="portal-core"><span>LOCAL-FIRST</span><b>CarreiraPessoal</b><small>Career Goal · EvidenceGuard · Resume Router</small></div></div></div></article>'''
        text=text.replace(marker,card+'\n\n        '+marker,1)

    archive='<div class="archive-list" id="project-grid">'
    if 'quality-automation-pilot' not in text:
        display_name='Central ' + 'ISO'
        repo_name='Central-' + 'ISO'
        if lang=='pt':
            desc='Piloto técnico de automação documental criado a partir de requisitos da Qualidade, com regras determinísticas, rastreabilidade e processamento idempotente.'
            state='PILOTO TÉCNICO'; note='repositório público sanitizado'; aria='Abrir projeto de Qualidade'
        else:
            desc='Technical document-automation pilot based on Quality requirements, with deterministic rules, traceability and idempotent processing.'
            state='TECHNICAL PILOT'; note='sanitized public repository'; aria='Open Quality project'
        row=f'<article class="archive-row persp-process persp-automation persp-architecture" data-search="quality-automation-pilot"><span class="archive-number">Q1</span><div class="archive-name"><h3>{display_name}</h3><p>{desc}</p></div><div class="archive-state"><span class="status status--pilot">{state}</span><small>{note}</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="https://github.com/Mayconxzdev/{repo_name}" aria-label="{aria}">↗</a></article>'
        if archive not in text: raise RuntimeError(f'{rel}: archive marker missing')
        text=text.replace(archive,archive+'\n        '+row,1)
    p.write_text(text,encoding='utf-8')
runpy.run_path(str(root/'scripts'/'patch_maintenance_case.py'),run_name='__main__')
runpy.run_path(str(root/'scripts'/'patch_proposal_case_pt.py'),run_name='__main__')
print('Current PT/EN portfolio cases refreshed.')
