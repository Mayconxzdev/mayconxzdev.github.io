import { chromium } from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';

const baseURL = process.env.PORTFOLIO_BASE_URL || 'http://127.0.0.1:8000';
const outputRoot = path.resolve('artifacts/visual');
const routes = [
  { path: '/', slug: 'home-pt', expected: 'ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES', cv: 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf', anchors: ['#systems', '#experience', '#evidence'] },
  { path: '/en/', slug: 'home-en', expected: 'AI AUTOMATION & INTEGRATIONS ANALYST', cv: 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf', anchors: ['#systems', '#experience', '#evidence'] },
  { path: '/competencias/', slug: 'skills-pt', expected: 'Automação, IA, dados e governança com evidência.', cv: 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf', anchors: [] },
  { path: '/en/skills/', slug: 'skills-en', expected: 'Automation, AI, data and governance backed by evidence.', cv: 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf', anchors: [] },
  { path: '/cases/catalogo-operacional-compras/', slug: 'catalog-pt', expected: 'Catálogo Operacional de Compras', cv: 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf', anchors: [] },
  { path: '/en/cases/operational-procurement-catalog/', slug: 'catalog-en', expected: 'Operational Procurement Catalog', cv: 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf', anchors: [] },
  { path: '/cases/portal/', slug: 'portal-pt', expected: 'Business Operating Platform multiempresa', cv: 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf', anchors: [] },
  { path: '/en/cases/portal/', slug: 'portal-en', expected: 'Multi-tenant Business Operating Platform', cv: 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf', anchors: [] },
];
const viewports = [
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'mobile', width: 390, height: 844 },
];
const themes = ['light', 'dark'];

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

async function loadAllImages(page) {
  await page.locator('img').evaluateAll((images) => {
    for (const image of images) image.loading = 'eager';
  });
  await page.evaluate(async () => {
    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
    const step = Math.max(window.innerHeight * 0.8, 500);
    for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
      window.scrollTo(0, y);
      await sleep(25);
    }
    window.scrollTo(0, 0);
  });
  await page.waitForFunction(() => Array.from(document.images).every((image) => image.complete), { timeout: 30_000 });
}

async function horizontalOverflowDetails(page) {
  return page.evaluate(() => {
    const viewport = document.documentElement.clientWidth;
    return Array.from(document.querySelectorAll('body *'))
      .map((element) => {
        const rect = element.getBoundingClientRect();
        return {
          tag: element.tagName.toLowerCase(),
          className: typeof element.className === 'string' ? element.className : '',
          text: (element.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 80),
          left: Math.round(rect.left), right: Math.round(rect.right), width: Math.round(rect.width),
        };
      })
      .filter((item) => item.right > viewport + 1 || item.left < -1)
      .sort((a, b) => Math.max(b.right - viewport, -b.left) - Math.max(a.right - viewport, -a.left))
      .slice(0, 8);
  });
}

await fs.rm(outputRoot, { recursive: true, force: true });
await fs.mkdir(outputRoot, { recursive: true });

const browser = await chromium.launch({ headless: true });
const failures = [];
let screenshots = 0;

try {
  for (const route of routes) {
    for (const viewport of viewports) {
      for (const theme of themes) {
        const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height }, colorScheme: theme, reducedMotion: 'reduce', deviceScaleFactor: 1 });
        await context.addInitScript((selectedTheme) => localStorage.setItem('mf-theme', selectedTheme), theme);
        const page = await context.newPage();
        const label = `${route.slug}-${viewport.name}-${theme}`;
        const screenshotPath = path.join(outputRoot, `${label}.png`);
        try {
          await page.goto(`${baseURL}${route.path}`, { waitUntil: 'networkidle', timeout: 45_000 });
          await page.addStyleTag({ content: '*,*::before,*::after{animation-duration:0s!important;animation-delay:0s!important;transition:none!important;caret-color:transparent!important}' });
          await loadAllImages(page);
          await page.waitForTimeout(100);

          const bodyText = (await page.locator('body').innerText()).toLocaleLowerCase();
          assert(bodyText.includes(route.expected.toLocaleLowerCase()), `${label}: target positioning text is not visible`);
          const htmlTheme = await page.locator('html').getAttribute('data-theme');
          assert(htmlTheme === theme, `${label}: expected theme ${theme}, found ${htmlTheme}`);

          const overflow = await page.evaluate(() => ({ scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth }));
          if (overflow.scrollWidth > overflow.clientWidth + 1) {
            const details = await horizontalOverflowDetails(page);
            throw new Error(`${label}: horizontal overflow ${overflow.scrollWidth}px > ${overflow.clientWidth}px; offenders=${JSON.stringify(details)}`);
          }

          const brokenImages = await page.locator('img').evaluateAll((images) => images.filter((img) => !img.complete || img.naturalWidth === 0).map((img) => img.getAttribute('src') || '[missing src]'));
          assert(brokenImages.length === 0, `${label}: broken images: ${brokenImages.join(', ')}`);

          const clippedText = await page.locator('main h1, main h2, main h3, main p, main li, main dt, main dd').evaluateAll((elements) => elements.flatMap((element) => {
            const style = getComputedStyle(element);
            if (style.display === 'none' || style.visibility === 'hidden' || !element.textContent?.trim()) return [];
            const xClipped = ['hidden', 'clip'].includes(style.overflowX) && element.scrollWidth > element.clientWidth + 2;
            const yClipped = ['hidden', 'clip'].includes(style.overflowY) && element.scrollHeight > element.clientHeight + 2;
            return xClipped || yClipped ? [{ text: element.textContent.trim().slice(0, 90), xClipped, yClipped }] : [];
          }));
          assert(clippedText.length === 0, `${label}: clipped text: ${JSON.stringify(clippedText.slice(0, 5))}`);

          const pdfLinks = await page.locator('a[href$=".pdf"]').evaluateAll((links) => links.map((link) => link.getAttribute('href') || ''));
          assert(pdfLinks.length > 0, `${label}: no resume link found`);
          assert(pdfLinks.every((href) => href.includes(route.cv)), `${label}: stale or incorrect resume link: ${pdfLinks.join(', ')}`);
          for (const anchor of route.anchors) assert((await page.locator(anchor).count()) === 1, `${label}: missing strategic section ${anchor}`);

          if (viewport.name === 'mobile') {
            const menuButton = page.locator('.menu-button');
            assert((await menuButton.count()) === 1, `${label}: mobile menu button missing`);
            await menuButton.click();
            assert((await menuButton.getAttribute('aria-expanded')) === 'true', `${label}: mobile menu did not open`);
            await page.keyboard.press('Escape');
            assert((await menuButton.getAttribute('aria-expanded')) === 'false', `${label}: mobile menu did not close with Escape`);
          }

          await page.screenshot({ path: screenshotPath, fullPage: true, animations: 'disabled' });
          screenshots += 1;
          console.log(`OK: ${label}`);
        } catch (error) {
          await page.screenshot({ path: screenshotPath, fullPage: true, animations: 'disabled' }).catch(() => {});
          failures.push(`${label}: ${error instanceof Error ? error.message : String(error)}`);
        } finally {
          await context.close();
        }
      }
    }
  }
} finally {
  await browser.close();
}

if (failures.length) {
  console.error(failures.map((failure) => `ERROR: ${failure}`).join('\n'));
  process.exit(1);
}
console.log(`Portfolio browser smoke completed: ${screenshots} screenshots, ${routes.length} strategic routes, 2 viewports and 2 themes.`);
