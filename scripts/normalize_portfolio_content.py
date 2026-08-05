from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    ROOT / "index.html": {
        "<strong>Automação de Processos por RPA</strong><span>ENAP · 25h</span>": "<strong>Automação de Processos através da RPA</strong><span>ENAP · 25h</span>",
        "<strong>Mapeamento e Automação de Processos</strong><span>ENAP · 20h</span>": "<strong>Fundamentos da Transformação Digital: Mapeamento e Automação de Processos</strong><span>ENAP · 20h</span>",
        "<strong>Trilha n8n e Workflows</strong><span>DIO · 8h / 4 cursos</span>": "<strong>Trilha n8n e Workflows</strong><span>DIO · 4h / 4 cursos</span>",
    },
    ROOT / "en" / "index.html": {
        "<strong>Ferramentas de IA: Agentes e Automações</strong><span>FIRJAN SENAI · 40h</span>": "<strong>AI Tools: Agents and Automations</strong><span>FIRJAN SENAI · 40h</span>",
        "<strong>Automação de Processos por RPA</strong><span>ENAP · 25h</span>": "<strong>Process Automation through RPA</strong><span>ENAP · 25h</span>",
        "<strong>Mapeamento e Automação de Processos</strong><span>ENAP · 20h</span>": "<strong>Digital Transformation Fundamentals: Process Mapping and Automation</strong><span>ENAP · 20h</span>",
        "<strong>IA no Contexto do Serviço Público</strong><span>ENAP · 20h</span>": "<strong>AI in the Public Service Context</strong><span>ENAP · 20h</span>",
        "<strong>Introdução à LGPD</strong><span>ENAP · 10h</span>": "<strong>Introduction to Brazil's Data Protection Law</strong><span>ENAP · 10h</span>",
        "<strong>Trilha n8n e Workflows</strong><span>DIO · 8h / 4 cursos</span>": "<strong>n8n and Workflows Learning Path</strong><span>DIO · 4h / 4 courses</span>",
    },
}


def normalize(path: Path, replacements: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
        elif new not in text:
            raise RuntimeError(f"Expected portfolio text not found in {path.relative_to(ROOT)}: {old}")
    if text == original:
        print(f"unchanged: {path.relative_to(ROOT)}")
        return False
    path.write_text(text, encoding="utf-8")
    print(f"normalized: {path.relative_to(ROOT)}")
    return True


def main() -> None:
    for path, replacements in REPLACEMENTS.items():
        normalize(path, replacements)


if __name__ == "__main__":
    main()
