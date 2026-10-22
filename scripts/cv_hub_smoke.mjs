import { chromium } from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';

const base = (process.argv[2] || 'http://127.0.0.1:8000').replace(/\/$/, '');
const output = process.argv[3] || 'artifacts/visual';
await fs.mkdir(output, { recursive: true });
const browser = await chromium.launch({ headless: true });
const failures = [];
const expected = [
  'Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf',
  'Maycon_Ferreira_Automacao_Integracoes.pdf',
  'Maycon_Ferreira_Sistemas_Backend.pdf',
  'Maycon_Ferreira_Web_Produtos_Digitais.pdf',
  'Maycon_Ferreira_IA_Agentes_MCP.pdf',
  'Maycon_Ferreira_Dados_BI.pdf',
  'Maycon_Ferreira_Conteudo_Video_IA.pdf',
  'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
];
try {
  for (const route of ['/assets/cv/', '/en/resumes/']) {
  for (const viewport of [
    { width: 1440, height: 900 },
    { width: 768, height: 1024 },
    { width: 390, height: 844 },
    { width: 320, height: 640 },
  ]) {
    const ctx = await browser.newContext({ viewport });
    const page = await ctx.newPage();
    const errs = [];
    page.on('pageerror', e => errs.push(String(e)));
    const response = await page.goto(base + route, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response?.ok()) failures.push('hub failed to load: '+response?.status());
    if ((await page.locator('h1').innerText()).trim() !== (route.startsWith('/en/') ? 'Resumes by specialty.' : 'Currículos por área.'))
      failures.push('hub title not found');
    const hrefs = await page.locator('a[href$=".pdf"]').evaluateAll(links => links.map(el => el.getAttribute('href')));
    if (hrefs.length !== expected.length) failures.push('expected 8 PDF links; found ' + hrefs.length);
    for (const file of expected) {
      if (!hrefs.some(link => link.endsWith('/' + file) || link === file))
        failures.push('missing PDF link: ' + file);
    }
    const tooWide = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    if (tooWide) failures.push('horizontal overflow at width '+viewport.width);
    const link = page.locator('a[href$="Maycon_Ferreira_Solucoes_Digitais_Automacao_IA.pdf"]');
    if (!(await link.isVisible())) failures.push('general resume link invisible');
    if (viewport.width === 1440) {
      for (const file of expected) {
        const fileResponse = await page.request.get(base + '/assets/cv/' + file);
        const bytes = await fileResponse.body();
        if (!fileResponse.ok() || bytes.subarray(0,5).toString() !== '%PDF-')
          failures.push('PDF not reachable or invalid header: ' + file);
      }
    }
    if (errs.length) failures.push('browser errors: ' + errs.join(','));
    await page.screenshot({path:path.join(output, 'cv-hub-' + (route.includes('/en/')?'en':'pt') + '-' + viewport.width + '.png'),fullPage:true,animations:'disabled'});
    await ctx.close();
  }
  }
} finally {
  await browser.close();
}
if (failures.length) { console.error(failures.join('\n')); process.exit(1); }
console.log('CV hub smoke passed: 8 downloads x 2 languages x 4 viewports, no horizontal scroll or JS errors.');
