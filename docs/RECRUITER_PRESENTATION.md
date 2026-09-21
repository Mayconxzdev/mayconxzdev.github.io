# Como organizei a apresentação profissional

Este documento registra a lógica de curadoria do portfólio para evitar três problemas: **repetir a mesma competência em todos os projetos, transformar a apresentação em uma lista de tecnologias e criar divergências entre currículo, portfólio e GitHub**.

## Posicionamento central

**Analista de Automação, IA e Integrações**

A narrativa principal é: **processo → regras → solução → integração → implantação → adoção → confiabilidade → sustentação**.

Isso permite mostrar amplitude técnica sem me posicionar artificialmente como desenvolvedor full-stack puro, especialista de segurança, cientista de dados ou engenheiro de ML.

## Projetos principais

| Ordem | Projeto | Evidência principal |
| ---: | --- | --- |
| 1 | Mala Direta | automação/n8n em produção e confiabilidade |
| 2 | Produção Operacional | implantação, adoção e operação |
| 3 | Proposta Comercial | processo, documentos/e-mail e impacto mensurável |
| 4 | CarreiraPessoal | produto, arquitetura, evidências e QA |
| 5 | Catálogo Operacional | backend, busca e integridade de dados operacionais |
| 6 | Postagem Redes | IA aplicada, RAG/grounding, APIs externas e revisão humana |

A ordem não representa “melhor código”. Ela oferece ao recrutador seis provas complementares de capacidade profissional.

## Recortes complementares

- HelpDesk: sistema interno, adoção, tempo real e segurança;
- ComprasVesper: integração de e-mail, fila durável e operação desktop;
- Central ISO: Qualidade, regras determinísticas, rastreabilidade e piloto técnico;
- StudioCad: IA aplicada, processamento seguro de arquivos e revisão humana;
- Compass UOL: dados/cloud;
- Manutenção em Campo: ativos, checklists, evidências e histórico;
- Hubora/sites: produto, UX e web;
- Portal: arquitetura empresarial e modularidade, **em desenvolvimento/revalidação**.

O Portal permanece fora dos projetos principais até que uma nova etapa de maturidade tenha evidência suficiente para mudar seu estado.

## Currículo geral de uma página

O currículo não deve repetir o portfólio. A experiência do Grupo Vesper já prova:

- n8n e integrações em produção;
- Proposta Comercial e resultado mensurável;
- Produção Operacional e manutenção;
- HelpDesk e adoção;
- levantamento de requisitos, BPMN/AS-IS/TO-BE, implantação, treinamento e sustentação.

Por isso, a seção **Projetos Selecionados** complementa a experiência com:

1. Mala Direta;
2. CarreiraPessoal;
3. Catálogo Operacional;
4. Postagem Redes.

O currículo geral prioriza termos de mercado sustentados por evidência — automação de processos, n8n, Python, FastAPI, APIs REST/webhooks, SQL/PostgreSQL, Docker, BPMN, AS-IS/TO-BE, IA generativa, RAG/grounding, agentes de IA, testes/homologação, monitoramento, retries e idempotência — sem colocar cada framework contextual no mesmo nível.

## Regra editorial dos cases

Cada case deve seguir, sempre que possível, a ordem:

**problema → decisão → implementação → resultado → confiabilidade/risco → limite real**.

A tecnologia aparece como resposta ao problema, não como o assunto principal.

Quando existe tela real que pode ser publicada com segurança, ela tem prioridade sobre mockup ou ilustração. Quando o ambiente é confidencial, uso dados sintéticos, referência autorizada ou arquitetura sanitizada.

## Estados e claims

O registro canônico de números, estados e wording aprovado está em [`CAREER_EVIDENCE.md`](CAREER_EVIDENCE.md).

As superfícies públicas não podem divergir em:

- cargo e posicionamento;
- métricas;
- estado do projeto;
- tecnologia atribuída ao projeto;
- produção versus teste/piloto/desenvolvimento;
- profundidade declarada de uma competência.

## Função de cada superfície

- **Currículo:** síntese de uma página para ATS e decisão inicial.
- **Portfólio:** contexto, resultado, processo e evidências visuais.
- **GitHub:** código, arquitetura, testes, decisões e limites técnicos.
- **LinkedIn:** descoberta, narrativa profissional e prova social; deve reutilizar os mesmos claims canônicos sem copiar o currículo palavra por palavra.
