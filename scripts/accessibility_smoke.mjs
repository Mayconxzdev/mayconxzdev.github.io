import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import fs from 'node:fs/promises';
import path from 'node:path';

const base = (process.argv[2] || 'http://127.0.0.1:8000').replace(/\/$/, '');
const aliases = new Set([
  '/cases/compass-automation/', '/cases/portal-vesper/', '/cases/procureflow/',
  '/en/cases/compass-automation/', '/en/cases/portal-vesper/', '/en/cases/procureflow/',
]);
const routeSet = new Set([
  '/', '/competencias/', '/competencias/credenciais/', '/en/', '/en/skills/', '/en/credentials/',
  '/404.html', '/en/404.html',
]);

async function addCaseRoutes(root, prefix) {
  const entries = await fs.readdir(root, { withFileTypes: true });
  for (const entry of entries.filter(item => item.isDirectory())) {
    try {
      await fs.access(path.join(root, entry.name, 'index.html'));
      const route = `${prefix}${entry.name}/`;
      if (!aliases.has(route)) routeSet.add(route);
    } catch {}
  }
}

await addCaseRoutes('cases', '/cases/');
await addCaseRoutes('en/cases', '/en/cases/');
const routes = [...routeSet].sort();
const mobileRoutes = new Set([
  '/', '/competencias/', '/competencias/credenciais/',
  '/cases/proposta-comercial/', '/cases/compras-e-cotacoes/', '/cases/tradutor-documental/', '/cases/belarc-inventory/', '/cases/postagem-redes/', '/cases/producao-operacional/',
  '/en/', '/en/skills/', '/en/credentials/',
  '/en/cases/commercial-proposal/', '/en/cases/purchasing-and-quotes/', '/en/cases/offline-document-translator/', '/en/cases/belarc-inventory/', '/en/cases/postagem-redes/', '/en/cases/producao-operacional/',
]);
const launchOptions = { headless: true };
if (process.env.PORTFOLIO_CHROMIUM_PATH) launchOptions.executablePath = process.env.PORTFOLIO_CHROMIUM_PATH;
const browser = await chromium.launch(launchOptions);
const failures = [];
let scans = 0;

try {
  for (const route of routes) {
    const viewports = [{ name: 'desktop', viewport: { width: 1440, height: 1000 } }];
    if (mobileRoutes.has(route)) viewports.push({ name: 'mobile', viewport: { width: 390, height: 844 } });
    for (const { name, viewport } of viewports) {
      const context = await browser.newContext({ viewport });
      const page = await context.newPage();
      try {
        const response = await page.goto(base + route, { waitUntil: 'networkidle', timeout: 15000 });
        if (!response?.ok()) {
          failures.push(`${route} ${name}: HTTP ${response?.status()}`);
          continue;
        }
        const results = await new AxeBuilder({ page }).analyze();
        const blocking = results.violations.filter(item => ['serious', 'critical', 'moderate'].includes(item.impact || ''));
        if (blocking.length) {
          failures.push(`${route} ${name}: ${blocking.map(item => `${item.id}(${item.impact}) x${item.nodes.length}`).join(', ')}`);
        }
        const severe = results.violations.filter(item => ['serious', 'critical'].includes(item.impact || '')).length;
        const moderate = results.violations.filter(item => item.impact === 'moderate').length;
        console.log(`${route} ${name}: ${severe} serious/critical; ${moderate} moderate violations`);
        scans += 1;
      } finally {
        await context.close();
      }
    }
  }
} finally {
  await browser.close();
}

if (failures.length) {
  console.error('Accessibility gate failed:\n' + failures.join('\n'));
  process.exit(1);
}
console.log(`Accessibility gate passed: ${scans} axe scans across ${routes.length} canonical PT/EN pages; all cases desktop and selected key routes also mobile; no moderate-or-higher violations.`);
