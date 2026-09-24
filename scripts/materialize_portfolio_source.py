from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

# This is the canonical materialization order for published source.
# Keep it synchronized with .github/workflows/pages.yml; the source-drift guard relies on this exact sequence.
COMMANDS = [
    "scripts/generate_resumes_general.py",
    "scripts/add_resume_links.py",
    "scripts/generate_social_cover.py",
    "scripts/add_carreirapessoal_home.py",
    "scripts/patch_career_visual.py",
    "scripts/patch_skills_current.py",
    "scripts/patch_portfolio_consistency.py",
    "scripts/patch_case_visual_safety.py",
    "scripts/patch_human_project_stories.py",
    "scripts/normalize_site_chrome.py",
    "scripts/patch_navigation_targets.py",
    "scripts/patch_404_language.py",
    "scripts/normalize_case_sequence.py",
    "scripts/patch_project_archive.py",
    # Run idempotent materializers twice intentionally so source and CI prove
    # that these transformations do not duplicate controls or copy.
    "scripts/patch_skills_current.py",
    "scripts/patch_project_archive.py",
    "scripts/curate_featured_projects.py",
]

for relative in COMMANDS:
    print(f"+ {sys.executable} {relative}")
    subprocess.run([sys.executable, relative], cwd=ROOT, check=True)

print("Portfolio source materialized to the same pre-release state validated by Pages.")
