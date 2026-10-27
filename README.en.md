# Laboratório Vivo — Maycon Ferreira

My portfolio of systems, automation, integrations, data and applied AI. Each case explains the problem, my contribution, implementation decisions, evidence and project limits.

[Portfolio](https://mayconxzdev.github.io/) · [Six PT/EN resumes](https://mayconxzdev.github.io/assets/cv/) · [Português](README.md)

## Run locally

The application uses Vite, JavaScript, CSS and GSAP. Node.js 22.12 or later is required; CI uses Node 22.

    git clone https://github.com/Mayconxzdev/mayconxzdev.github.io.git
    cd mayconxzdev.github.io
    npm ci
    npm run dev

Development runs on http://127.0.0.1:8789. Build and preview:

    npm run build
    npm run preview

The build is self-contained and writes dist/. Preview uses http://127.0.0.1:4214. Edit source files rather than dist/.

## Source and content

- index.html and src/ contain the homepage, project data, motion and styles.
- scripts/evidence-map.mjs defines gallery images, captions, sources and stable IDs.
- scripts/generate-cases.mjs and templates/case.html generate 18 canonical case pages.
- public/ contains approved media, fonts, versioned PDFs and retained historical URLs.
- scripts/resumes-content.json contains the three Portuguese resumes and three English equivalents.

The site offers Automatic, Animation and Direct reading modes. The five featured projects remain accessible without animation; small screens use normal document flow. Screenshots, illustrative demos, co-authorship and private areas are identified.

## Validation

    npx playwright install chromium
    npm test
    npm run test:full

The runner manages the local preview and runs Playwright and axe-core. Full coverage includes the homepage and 18 cases at eight widths, galleries, keyboard, menus, filters, PDFs, browser back, reduced motion, fast scroll and historical URLs. Low-height layouts and a viewport approximation of 200% zoom are included.

These are Chromium laboratory checks, not certification, physical-device testing, ATS submission or user feedback.

## Resume generation

The web build preserves committed PDFs and needs no Python. Optional regeneration:

    python -m pip install -r requirements-resumes.txt
    npm run resumes:build
    npm run build
    npm run resumes:verify

The generator uses Arial when available, otherwise Helvetica. Inspect rendered pages after regeneration, especially across platforms.

## Delivery and rights

Pull requests run validation. Main publishes only the tested dist/ artifact through GitHub Actions. A final job compares the online commit and every file hash against the tested [build manifest](https://mayconxzdev.github.io/build.json).

See [architecture](docs/ARCHITECTURE.md), [deployment and rollback](docs/DEPLOYMENT.md), [asset permissions](ASSETS.md) and [security reporting](SECURITY.md). Historical deployment commits remain in Git history. Private audit packages, backups and client data are excluded.

Permission to display images in this portfolio does not grant a general reuse license for third-party photographs, brands or systems.
