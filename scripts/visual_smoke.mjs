import { chromium } from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';

const base = (process.argv[2] || 'http://127.0.0.1:4173').replace(/\/$/, '');
const out = process.argv[3] || 'artifacts/visual';

const aliases = new Set([
  '/cases/compass-automation/',
  '/cases/portal-vesper/',
  '/cases/procureflow/',
  '/en/cases/compass-automation/',
  '/en/cases/portal-vesper/',
  '/en/cases/procureflow/',
]);

const routes = [
  ['home-pt', '/'],
  ['skills-pt', '/competencias/'],
  ['home-en', '/en/'],
  ['skills-en', '/en/skills/'],
  ['not-found-pt', '/404.html'],
  ['not-found-en', '/en/404.html'],
];

async function addCaseRoutes(root, prefix, labelPrefix) {
  const entries = await fs.readdir(root, { withFileTypes: true });
  for (const entry of entries.filter(item => item.isDirectory()).sort((a, b) => a.name.localeCompare(b.name))) {
    try {
      await fs.access(path.join(root, entry.name, 'index.html'));
      routes.push([`${labelPrefix}-${entry.name}`, `${prefix}${entry.name}/`]);
    } catch {}
  }
}

await addCaseRoutes('cases', '/cases/', 'case-pt');
await addCaseRoutes('en/cases', '/en/cases/', 'case-en');

const profiles = [
  ['desktop-light', { width: 1440, height: 1000 }, 'light'],
  ['desktop-dark', { width: 1440, height: 1000 }, 'dark'],
  ['mobile-light', { width: 390, height: 844 }, 'light'],
];

const PT_NAV = ['Visão geral', 'Projetos', 'Experiência', 'Resultados', 'Competências', 'Contato', 'Currículo', 'EN'];
const EN_NAV = ['Overview', 'Projects', 'Experience', 'Results', 'Skills', 'Contact', 'Resume', 'PT'];

await fs.mkdir(out, { recursive: true });
const browser = await chromium.launch({ headless: true });
const failures = [];
let captures = 0;
let interactionChecks = 0;

try {
  for (const [routeName, route] of routes) {
    const routeProfiles = aliases.has(route) ? profiles.slice(0, 1) : profiles;
    for (const [profileName, viewport, theme] of routeProfiles) {
      const context = await browser.newContext({ viewport });
      await context.addInitScript((selected) => {
        try { localStorage.setItem('mf-theme', selected); } catch {}
      }, theme);
      const page = await context.newPage();
      page.setDefaultTimeout(6000);
      page.setDefaultNavigationTimeout(10000);
      const consoleErrors = [];
      page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
      page.on('pageerror', err => consoleErrors.push(String(err)));

      const response = await page.goto(base + route, { waitUntil: 'domcontentloaded', timeout: 10000 });
      if (!response || !response.ok()) failures.push(`${route} returned ${response?.status?.()}`);
      await page.waitForLoadState('networkidle', { timeout: 4000 }).catch(() => {});

      // Trigger browser lazy-loading before judging image health. The static validator
      // already parses/decodes the underlying files; here we verify that the page can load them.
      await page.evaluate(async () => {
        const step = Math.max(500, Math.floor(window.innerHeight * 0.85));
        for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
          window.scrollTo(0, y);
          await new Promise(resolve => setTimeout(resolve, 25));
        }
        window.scrollTo(0, 0);
        await new Promise(resolve => setTimeout(resolve, 80));
      });

      const result = await page.evaluate(async ({ theme, alias }) => {
        const root = document.documentElement;
        const waitForImage = img => new Promise(resolve => {
          if (img.complete) return resolve();
          const finish = () => resolve();
          img.addEventListener('load', finish, { once: true });
          img.addEventListener('error', finish, { once: true });
          setTimeout(finish, 5000);
        });
        const imageResults = await Promise.all([...document.images].map(async img => {
          await waitForImage(img);
          if (!img.complete || !img.naturalWidth || !img.naturalHeight) {
            return {
              src: img.currentSrc || img.src,
              error: `browser load state complete=${img.complete} natural=${img.naturalWidth}x${img.naturalHeight}`,
            };
          }
          return null;
        }));
        const nav = document.querySelector('#main-nav');
        const navLabels = nav ? [...nav.querySelectorAll('a')].map(a => a.textContent.trim().replace(/\s+/g, ' ')) : [];
        const text = document.body.innerText || '';
        return {
          overflow: Math.max(0, root.scrollWidth - root.clientWidth),
          broken: imageResults.filter(Boolean),
          text,
          theme: root.dataset.theme || '',
          chrome: alias ? true : Boolean(document.querySelector('[data-global-chrome="2026-08"]')),
          footer: alias ? true : Boolean(document.querySelector('[data-global-footer="2026-08"]')),
          themeToggle: alias ? true : Boolean(document.querySelector('.theme-toggle')),
          menuButton: alias ? true : Boolean(document.querySelector('.menu-button')),
          navLabels,
        };
      }, { theme, alias: aliases.has(route) });

      if (result.overflow > 2) failures.push(`${route} ${profileName}: horizontal overflow ${result.overflow}px`);
      if (result.broken.length) failures.push(`${route} ${profileName}: broken images: ${result.broken.map(x => `${x.src} (${x.error})`).join(', ')}`);
      for (const bad of ['PermissionError', 'Traceback (most recent call last)', 'Internal Server Error']) {
        if (result.text.includes(bad)) failures.push(`${route} ${profileName}: leaked error text: ${bad}`);
      }
      if (consoleErrors.length) failures.push(`${route} ${profileName}: console/page errors: ${consoleErrors.join(' | ')}`);

      if (!aliases.has(route)) {
        if (result.theme !== theme) failures.push(`${route} ${profileName}: requested ${theme} theme but got ${result.theme}`);
        if (!result.chrome || !result.footer || !result.themeToggle || !result.menuButton) failures.push(`${route} ${profileName}: shared chrome incomplete`);
        const expectedNav = route.startsWith('/en/') ? EN_NAV : PT_NAV;
        if (JSON.stringify(result.navLabels) !== JSON.stringify(expectedNav)) {
          failures.push(`${route} ${profileName}: nav labels drifted: ${JSON.stringify(result.navLabels)}`);
        }

        // Verify the visible controls are functional, not merely present in markup.
        const initialTheme = await page.locator('html').getAttribute('data-theme');
        await page.locator('.theme-toggle').click({ timeout: 3000 });
        const toggledTheme = await page.locator('html').getAttribute('data-theme');
        if (!initialTheme || !toggledTheme || toggledTheme === initialTheme) {
          failures.push(`${route} ${profileName}: theme toggle is not functional`);
        }
        await page.locator('.theme-toggle').click({ timeout: 3000 });
        const restoredTheme = await page.locator('html').getAttribute('data-theme');
        if (restoredTheme !== initialTheme) {
          failures.push(`${route} ${profileName}: theme toggle did not restore the original theme`);
        }
        interactionChecks += 1;

        if (viewport.width <= 500) {
          const menu = page.locator('.menu-button');
          const nav = page.locator('#main-nav');
          await menu.click({ timeout: 3000 });
          const opened = await menu.getAttribute('aria-expanded');
          const openClass = await nav.evaluate(node => node.classList.contains('open'));
          if (opened !== 'true' || !openClass) {
            failures.push(`${route} ${profileName}: mobile menu did not open`);
          }
          await menu.click({ timeout: 3000 });
          const closed = await menu.getAttribute('aria-expanded');
          const closedClass = await nav.evaluate(node => node.classList.contains('open'));
          if (closed !== 'false' || closedClass) {
            failures.push(`${route} ${profileName}: mobile menu did not close`);
          }
          interactionChecks += 1;
        }
      }

      const file = path.join(out, `${routeName}-${profileName}.png`);
      await page.screenshot({ path: file, fullPage: true, timeout: 10000 });
      captures += 1;
      await context.close();
    }
  }
} finally {
  await browser.close();
}

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Visual smoke passed: ${captures} captures across ${routes.length} routes; ${interactionChecks} theme/menu interaction checks`);
