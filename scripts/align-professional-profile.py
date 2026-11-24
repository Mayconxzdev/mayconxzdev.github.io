from pathlib import Path
import json,hashlib,subprocess
r=Path(__file__).resolve().parent.parent
src=r/'site-release';mfile=r/'scripts/public-release-manifest.json'
assert not subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],cwd=r,text=True).strip()
changed=[]
def edit(rel, pairs):
 p=src/rel; h=p.read_text(encoding='utf8')
 for old,new in pairs:
  assert old in h,(rel,old[:80])
  h=h.replace(old,new,1)
 p.write_text(h,encoding='utf8');changed.append(rel)
edit('sobre/index.html',[
 ('Sou técnico júnior em automação de processos e estudo Análise e Desenvolvimento de Sistemas. No dia a dia, uso IA para pesquisar, organizar demandas, construir soluções com agentes e revisar o resultado. Também produzo vídeos e materiais digitais.','Trabalho como técnico júnior em automação de processos e curso Análise e Desenvolvimento de Sistemas. Na indústria, converso com quem usa as ferramentas, organizo as demandas e acompanho a entrega. Também produzo conteúdo com IA e dou aulas de informática.'),
 ('<article><span>2025</span><h3>42 Rio</h3>','<article><span>Desde outubro de 2024</span><h3>Instrutor de informática · Freelance</h3><p>Aulas de Word, Excel, PowerPoint, Google Sheets, Power BI, Power Query, VBA introdutório e Windows/Linux. Também presto suporte técnico quando necessário.</p></article><article><span>2025</span><h3>VemSer</h3><p>Assistente de informática · atendimento, suporte a usuários e diagnóstico de computadores.</p></article><article><span>2025</span><h3>42 Rio</h3>'),
 ('<h3>UNISUAM</h3><p>Análise e Desenvolvimento de Sistemas.</p>','<h3>UNISUAM</h3><p>Tecnólogo em Análise e Desenvolvimento de Sistemas, em andamento · previsão de conclusão: dezembro de 2026.</p>'),
 ('<section class="p1-frame p2-section p3-ai-method">','<section class="p1-frame p2-section"><div class="p2-section-head"><h2>Ferramentas de negócio.</h2><p>Nem todo problema precisa de uma aplicação nova. Escolho as ferramentas a partir da rotina, dos dados e das pessoas que vão utilizá-las.</p></div><div class="p2-capabilities"><article><h3>Processos</h3><p>Mapeamento de rotinas, BPMN, AS-IS/TO-BE, requisitos, validação e implantação.</p></article><article><h3>Dados e produtividade</h3><p>Excel, Power Query, Power BI, Google Sheets, SQL e Office para organizar informações, relatórios e indicadores.</p></article><article><h3>Ensino e suporte</h3><p>Explico ferramentas, preparo orientações e acompanho dúvidas. Gosto de ver as pessoas conseguindo usar o que aprendem ou o que entrego.</p></article></div></section><section class="p1-frame p2-section p3-ai-method">')
])
edit('en/index.html',[
 ('I work on process automation in an industrial environment and use AI-assisted tools to build digital solutions and creative media.','I work as a junior process automation technician in an industrial environment. I build digital solutions and creative media with AI-assisted tools, and teach computer skills as a freelancer.'),
 ('<section class="p1-frame p2-section "><div class="p2-section-head"><h2>Selected work.','<section class="p1-frame p2-section"><div class="p2-context"><h2>Experience.</h2><div class="p2-timeline"><article><span>Current role</span><h3>Vesper</h3><p>Junior process automation technician: requirements, operational systems, integrations, deployment, training and support.</p></article><article><span>Since October 2024</span><h3>Freelance IT instructor</h3><p>Microsoft Office, Excel, Google Sheets, Power BI, Power Query, introductory VBA and Windows/Linux; technical support as needed.</p></article><article><span>2025</span><h3>VemSer</h3><p>IT assistant: user and computer support.</p></article><article><span>2024–2025</span><h3>Compass UOL</h3><p>Practical data engineering training, AWS and SQL.</p></article><article><span>In progress</span><h3>UNISUAM</h3><p>Systems Analysis and Development degree; expected December 2026.</p></article></div></div></section><section class="p1-frame p2-section"><div class="p2-section-head"><h2>Business tools.</h2></div><div class="p2-capabilities"><article><h3>Processes</h3><p>BPMN, AS-IS/TO-BE, requirements, testing and implementation.</p></article><article><h3>Data and productivity</h3><p>Excel, Power BI, Power Query, SQL, Office and Google Sheets.</p></article><article><h3>Applied AI</h3><p>AI agents, integrations, human review, generative visual tools and editing.</p></article></div></section><section class="p1-frame p2-section "><div class="p2-section-head"><h2>Selected work.')
])
edit('formacao/index.html',[('<h3>UNISUAM</h3><p>Análise e Desenvolvimento de Sistemas.</p>','<h3>UNISUAM</h3><p>Tecnólogo em Análise e Desenvolvimento de Sistemas, em andamento · previsão de conclusão: dezembro de 2026.</p>')])
# Replace vague historic redirects with explicit destination and status.
maps={'catalogo-operacional-compras':('Catálogo Operacional de Compras','Catálogo de materiais e categorias para consulta e organização de compras. O repositório apresenta uma edição demonstrativa; não é um dos estudos de caso principais.','CatalogoOperacional'),'studiocad':('StudioCad','Experiência com visualização de referências técnicas e apoio a projetos industriais. A edição pública é demonstrativa.','StudioCad'),'portal':('Portal','Referência pública de uma arquitetura anterior de plataforma modular. Não representa a versão atual de sistemas internos.','Portal'),'central-iso':('Central ISO','Piloto de conferência documental e rastreabilidade. Não apresentado como implantação em produção.','Central-ISO'),'compras-e-cotacoes':('Compras e Cotações','Ferramenta para organizar solicitações, cotações e acompanhamento de respostas. Consulte o escopo demonstrativo no repositório.','ComprasProducao'),'carreira-pessoal':('CarreiraPessoal','Protótipo pessoal de organização de candidaturas. O desenvolvimento está incompleto.','CarreiraPessoal')}
for slug,(title,desc,repo) in maps.items():
 rel=f'cases/{slug}/index.html';p=src/rel
 if not p.exists():continue
 h=p.read_text(encoding='utf8');a=h.index('<main');b=h.index('</main>',a)+7
 new=f'<main id="conteudo"><section class="p1-frame p1-page-intro"><h1>{title}.</h1><p>{desc}</p></section><section class="p1-frame p1-list"><a class="p1-arrowlink" href="https://github.com/Mayconxzdev/{repo}">Consultar o repositório ↗</a><br><a class="p1-arrowlink" href="/trabalhos/#outros-trabalhos">Voltar à seleção de trabalhos ↗</a></section></main>'
 h=h[:a]+new+h[b:];p.write_text(h,encoding='utf8');changed.append(rel)
m=json.loads(mfile.read_text(encoding='utf8'))
for entry in m['files']:
 if entry['path'] in changed:
  b=(src/entry['path']).read_bytes();entry.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
m['profileAlignment']='2026-11-24; freelance teaching, support, business tools and historical case destinations'
mfile.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf8')
print('Updated',changed)
