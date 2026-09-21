# Focused visual audit — 2026-08-14

This pass follows the full PT/EN browser screenshot audit and records concrete recruiter-facing regressions found after the first consistency pass.

## Fixed in this branch

- `ComprasVesper` receives a semantic word-break opportunity so the brand no longer clips on 390 px mobile layouts.
- `Infinity Engine` and `WhatsApp` no longer label architecture-only cards as “system in use” or “screens”. Their headings now state that the material is a sanitized architecture/flow representation.
- Central ISO validation evidence is synchronized with the current successful repository CI: 32 passing tests.
- Browser smoke now fails when a `.case-identity h1` has horizontal clipping, in addition to the existing whole-page overflow check.

## Audit rule

A visually successful page must not only render without broken assets. Its title must fit, evidence labels must describe what is actually shown, visible links must be actionable, and PT/EN surfaces must keep the same evidence boundary.
