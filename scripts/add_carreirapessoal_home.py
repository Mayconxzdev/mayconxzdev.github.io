from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
for rel,lang in [('index.html','pt'),('en/index.html','en')]:
    p=root/rel; text=p.read_text(encoding='utf-8')
    marker='<article class="feature-case feature-case--portal-vesper feature-case--reverse">'
    if marker not in text: raise RuntimeError(f'{rel}: marker missing')
    if 'Career Goal · EvidenceGuard · Resume Router' in text: continue
    if lang=='pt':
        card='''<article class="feature-case feature-case--portal-vesper feature-case--reverse"><div class="feature-case__copy"><div class="case-index"><span>06</span><span class="status status--public">PRODUTO PESSOAL</span></div><p class="case-category">Career intelligence local-first</p><h3>CarreiraPessoal</h3><p class="case-summary">Sistema que uso na própria busca para descobrir e deduplicar vagas, avaliar direção profissional, reconciliar evidências, preparar currículos e acompanhar candidaturas.</p><div class="case-impact"><small>Engenharia</small><strong>102 famílias ATS reconhecidas, 11 coletores diretos; v12.5.2 registrada com 283 testes Python.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5</p><div class="project-links"><a class="text-link" href="https://github.com/Mayconxzdev/CarreiraPessoal">Ver repositório<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><div class="visual visual--portal"><div class="portal-core"><span>LOCAL-FIRST</span><b>CarreiraPessoal</b><small>Career Goal · EvidenceGuard · Resume Router</small></div></div></div></article>'''
    else:
        card='''<article class="feature-case feature-case--portal-vesper feature-case--reverse"><div class="feature-case__copy"><div class="case-index"><span>06</span><span class="status status--public">PERSONAL PRODUCT</span></div><p class="case-category">Local-first career intelligence</p><h3>CarreiraPessoal</h3><p class="case-summary">A system I use in my own search to discover and deduplicate roles, evaluate career direction, reconcile evidence, prepare resumes and track applications.</p><div class="case-impact"><small>Engineering</small><strong>102 ATS/career-platform families recognized, 11 direct collectors; v12.5.2 recorded with 283 Python tests.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5</p><div class="project-links"><a class="text-link" href="https://github.com/Mayconxzdev/CarreiraPessoal">View repository<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><div class="visual visual--portal"><div class="portal-core"><span>LOCAL-FIRST</span><b>CarreiraPessoal</b><small>Career Goal · EvidenceGuard · Resume Router</small></div></div></div></article>'''
    text=text.replace(marker,card+'\n\n        '+marker,1)
    p.write_text(text,encoding='utf-8')
runpy.run_path(str(root/'scripts'/'patch_maintenance_case.py'),run_name='__main__')
runpy.run_path(str(root/'scripts'/'patch_proposal_case_pt.py'),run_name='__main__')
print('Current PT/EN portfolio cases refreshed.')
