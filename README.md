# Portfólio — Maycon Ferreira

Atuo com soluções digitais, automação e IA aplicada em operações, TI e comunicação. Defino requisitos, arquitetura e critérios de aceitação, conduzo agentes por especificações versionadas e valido as entregas com revisão de código, testes e feedback de usuários.

O [portfólio publicado](https://mayconxzdev.github.io/) reúne projetos de automação, documentação, operação industrial e sistemas internos. Os cases começam pelo problema e pelo uso; cada página também traz detalhes técnicos para quem quiser conhecer as decisões e a implementação.

## Por onde começar

- [Belarc Inventory](cases/belarc-inventory/) — sistema de inventário de estações Windows com contexto para apoiar suporte e manutenção.
- [Produção Operacional](cases/producao-operacional/) — aplicação Windows usada para acompanhar ordens entre escritório, fábrica e painel de produção.
- [Manutenção em Campo](cases/manutencao-campo/) — sistema usado na empresa para registrar manutenções em máquinas e equipamentos. O código público é uma demonstração independente com dados fictícios.
- [Postagem Redes](cases/postagem-redes/) — automação que prepara rascunhos com contexto aprovado e inclui revisão humana antes da publicação.

Também desenvolvi o [Tradutor documental offline](cases/tradutor-documental/) para preparar versões em português e inglês de documentos Word e ODT mantendo sua estrutura, e a [Proposta Comercial](cases/proposta-comercial/), que reúne pedidos, modelos, documentos, revisão e envio. Outros projetos estão no [arquivo do portfólio](https://mayconxzdev.github.io/#archive). Cases de sistemas internos explicam o trabalho sem publicar código ou informações empresariais.

## Currículos

O portfólio mantém **sete currículos temáticos em português e uma versão geral em inglês**, gerados de forma reprodutível pelo código em [`scripts/generate_resumes_general.py`](scripts/generate_resumes_general.py).

- [Escolher currículo por área](https://mayconxzdev.github.io/assets/cv/)
- [Currículo geral — Soluções Digitais, Automação e IA](assets/cv/Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf)
- [General Resume (EN)](assets/cv/Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf)

Os três nomes históricos em português continuam disponíveis e apontam para a versão principal, IA/agentes e Dados/BI, preservando links de candidaturas antigas. As fontes estão no repositório e os PDFs são testados quanto a extração, links e legibilidade; esses testes não simulam a pontuação de ATS comerciais.

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

O workflow de CI executa os validadores de conteúdo, navegação, currículos, acessibilidade, layout e publicação, incluindo equivalência entre PDFs rastreados e PDFs regenerados. Os comandos de manutenção estão em [`docs/VALIDATION.md`](docs/VALIDATION.md) e no arquivo de workflow.

## Publicação

Pull requests executam o CI sem publicar. A integração na branch `main` inicia a publicação no GitHub Pages; depois, o workflow verifica o build publicado e os links do site.
