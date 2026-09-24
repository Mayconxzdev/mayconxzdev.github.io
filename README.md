# Portfólio — Maycon Ferreira

Trabalho com automação, IA aplicada, integrações e Python. Converso com as pessoas que usam os processos, entendo suas regras e construo soluções que possam ser usadas e mantidas no contexto real.

O [portfólio publicado](https://mayconxzdev.github.io/) reúne projetos de automação, documentação, operação industrial e sistemas internos. Os cases começam pelo problema e pelo uso; cada página também traz detalhes técnicos para quem quiser conhecer as decisões e a implementação.

## Por onde começar

- [Proposta Comercial](cases/proposta-comercial/) — um aplicativo que reúne pedidos, modelos, documentos, revisão e envio de propostas.
- [Tradutor documental offline](cases/tradutor-documental/) — aplicativo desktop para preparar versões em português e inglês de documentos Word e ODT, mantendo sua estrutura.
- [Postagem Redes](cases/postagem-redes/) — automação que prepara rascunhos com contexto aprovado e inclui revisão humana antes da publicação.
- [Produção Operacional](cases/producao-operacional/) — aplicação Windows usada para acompanhar ordens entre escritório, fábrica e painel de produção.

Outros projetos estão no [arquivo do portfólio](https://mayconxzdev.github.io/#archive), incluindo inventário de estações, compras, suporte e consulta documental. Cases de sistemas internos explicam o funcionamento sem publicar código ou informações empresariais.

## Currículos

O site mantém quatro currículos em PDF, cada um com uma página e direcionado a um foco profissional. Os PDFs são gerados pela fonte Python em [`scripts/generate_resumes_general.py`](scripts/generate_resumes_general.py) e não devem ser editados manualmente.

## Estrutura do site

- `index.html`, `en/` — páginas em português e inglês;
- `cases/`, `en/cases/` — histórias dos projetos e detalhes técnicos;
- `assets/` — elementos visuais, materiais fictícios e currículos;
- `css/`, `js/` — estilos e interações;
- `scripts/` — geração de PDFs, materialização do conteúdo e verificações.

O portfólio é um site estático no GitHub Pages. Os repositórios públicos contêm somente código e materiais preparados para publicação; projetos internos são apresentados por meio de descrições e demonstrações sem dados reais.

## Executar localmente

Requer Python 3.10+. Para conferir o site no navegador:

```powershell
python -m http.server 8000
```

Abra `http://127.0.0.1:8000/`. Para regenerar os currículos:

```powershell
python scripts/generate_resumes_general.py
```

## Verificações

O workflow de CI executa os validadores de conteúdo, navegação, currículos, acessibilidade, layout e publicação. Os comandos de manutenção estão em [`docs/VALIDATION.md`](docs/VALIDATION.md) e no arquivo de workflow.

## Publicação

Pull requests executam o CI sem publicar. A integração na branch `main` inicia a publicação no GitHub Pages; depois, o workflow verifica o build publicado e os links do site.
