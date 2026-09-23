"""Compatibility entry point for resume validation.

The canonical resume checks for the published portfolio live in:
- validate_general_resumes.py (text, links and one-page content)
- validate_resume_visual.py (rendering/readability/layout)

Keeping this lightweight entry point avoids a second, stale source of truth.
"""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parent

if __name__ == "__main__":
    runpy.run_path(str(ROOT / "validate_general_resumes.py"), run_name="__main__")
    runpy.run_path(str(ROOT / "validate_resume_visual.py"), run_name="__main__")
