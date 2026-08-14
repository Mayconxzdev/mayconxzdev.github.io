import { chromium } from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';

const base = (process.argv[2] || 'http://127.0.0.1:4173').replace(/\/$/, '');
const out = process.argv[3] || 'artifacts/visual';

const routes = [
  ['home-pt', '/'],
  ['carreira-pt', '/cases/carreira-pessoal/'],
  ['central-iso-pt', '/cases/central-iso/'],
  ['skills-pt', '/competencias/'],
  ['home-en', '/en/'],
  ['carreira-en', '/en/cases/career-personal/'],
  ['central-iso-en', '/en/cases/central-iso/'],
];

const viewports = [
  ['desktop', { width: 1440, height: 1000 }],
  ['mobile', { width: 390, height: 844 }],
];

const themes = ['light', 'dark'];
await fs.mkdir(out, { recursive: true });
const browser = await chromium.launch({ headless: true });
const failures = [];

try {
  for (const [routeName, route] of routes) {
    for (const [viewName, viewport] of viewports) {
      for (const theme of themes) {
        const context = await browser.newContext({ viewport });
        await context.addInitScript((selected) => {
          try { localStorage.setItem('mf-theme', selected); } catch {}
        }, theme);
        const page = await context.newPage();
        const consoleErrors = [];
        page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
        page.on('pageerror', err => consoleErrors.push(String(err)));

        const response = await page.goto(base + route, { waitUntil: 'networkidle' });
        if (!response || !response.ok()) failures.push(`${route} returned ${response?.status?.()}`);

        const result = await page.evaluate(() => {
          const root = document.documentElement;
          const broken = [...document.images].filter(img => img.complete && img.naturalWidth === 0).map(img => img.src);
          const text = document.body.innerText || '';
          return {
            overflow: Math.max(0, root.scrollWidth - root.clientWidth),
            broken,
            text,
          };
        });

        if (result.overflow > 2) failures.push(`${route} ${viewName}/${theme}: horizontal overflow ${result.overflow}px`);
        if (result.broken.length) failures.push(`${route} ${viewName}/${theme}: broken images: ${result.broken.join(', ')}`);
        for (const bad of ['PermissionError', 'Traceback (most recent call last)', 'Internal Server Error']) {
          if (result.text.includes(bad)) failures.push(`${route} ${viewName}/${theme}: leaked error text: ${bad}`);
        }
        if (consoleErrors.length) failures.push(`${route} ${viewName}/${theme}: console/page errors: ${consoleErrors.join(' | ')}`);

        const file = path.join(out, `${routeName}-${viewName}-${theme}.png`);
        await page.screenshot({ path: file, fullPage: true });
        await context.close();
      }
    }
  }
} finally {
  await browser.close();
}

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Visual smoke passed: ${routes.length * viewports.length * themes.length} captures`);
