# Guia de leitura para recrutadores

## Posicionamento

**Analista de Automação e IA**, com foco em automação de processos, integrações e sistemas internos em Python. A tecnologia é mostrada como meio para reduzir trabalho manual e tornar a operação mais clara e sustentável.

## Comece por estes quatro cases

| Ordem | Case | O que comprova | Estado |
| ---: | --- | --- | --- |
| 1 | [Vesper Propostas](../cases/vesper-propostas/) | melhoria mensurável de um processo documental; revisão humana antes de e-mail | uso interno, código privado e case sanitizado |
| 2 | [Belarc Inventory](../cases/belarc-inventory/) | co-desenvolvimento de arquitetura Windows distribuída e contexto de suporte | uso interno; imagens e dados sanitizados |
| 3 | [Postagem Redes](../cases/postagem-redes/) | grounding/RAG, guardrails, revisão humana e evals | validado em teste; não é produção |
| 4 | [Produção Operacional](../cases/producao-operacional/) | implantação e adoção em operação produtiva | produção |

O arquivo inclui [ComprasVesper](../cases/compras-vesper/) para e-mail e filas persistentes, [Mala Direta](../cases/mala-direta/) para automação n8n em produção, e [Central ISO](../cases/central-iso/) como piloto determinístico/read-only. Eles complementam os quatro cases principais sem competir pela mesma primeira leitura.

## Currículos

- **Geral PT-BR:** automação de processos, integrações, n8n, Power Automate e Python. Use para Automação, Integrações e Python Automation júnior.
- **Automação + IA PT-BR:** use quando a vaga pedir LLMs, conteúdo assistido, RAG ou avaliação de IA. Os cases de IA estão marcados como teste/experimental.
- **Power Platform/BI PT-BR:** use para automação low-code, Power Automate, dados e BI.
- **Geral EN:** versão semanticamente equivalente ao currículo geral PT-BR; inglês de escrita e conversação é básico.

Os quatro PDFs têm uma página. A validação verifica texto com **pypdf e PyMuPDF**, ordem de seções/projetos, links de contato e renderização visual. Isso é uma verificação de extração e legibilidade, não uma garantia para todo ATS proprietário.

## Estado de competências sensíveis

- **MCP:** Microsoft Applied Skill — MCP Tools with Agents. Não há evidência encontrada de servidor/cliente MCP próprio; não apresentar como projeto implementado.
- **IA/RAG:** Postagem Redes validado em teste, com evals reproduzíveis. Não há claim de agente/RAG em produção.
- **Métricas:** cada número pertence ao contexto indicado no case e no registro canônico [`CAREER_EVIDENCE.md`](CAREER_EVIDENCE.md).
- **Código corporativo:** não está no portfólio. Casos internos usam arquitetura e capturas sanitizadas.

## Protocolo de conversa

Ao apresentar um projeto, explicar nesta ordem: problema e usuário; meu papel; fluxo e decisões; integração e tratamento de falha; estado atual; resultado; limite conhecido. Para IA, acrescentar contexto/fontes, validação e revisão humana. Separar o que foi feito por mim do que foi co-desenvolvido ou é parte do ambiente da equipe.
