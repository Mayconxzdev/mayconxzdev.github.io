import { chromium } from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';

const baseURL = process.env.PORTFOLIO_BASE_URL || 'http://127.0.0.1:8000';
const outputRoot = path.resolve('artifacts/visual');
const routes = [
  {
    path: '/',
    slug: 'home-pt',
    expected: 'ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES',
    cv: 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
    anchors: ['#systems', '#experience', '#evidence'],
  },
  {
    path: '/en/',
    slug: 'home-en',
    expected: 'AI AUTOMATION & INTEGRATIONS ANALYST',
    cv: 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
    anchors: ['#systems', '#experience', '#evidence'],
  },
  {
    path: '/competencias/',
    slug: 'skills-pt',
    expected: 'Automação, IA e integrações com evidência.',
    cv: 'Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf',
    anchors: [],
  },
  {
    path: '/en/skills/',
    slug: 'skills-en',
    expected: 'Automation, AI and integrations backed by evidence.',
    cv: 'Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf',
    anchors: [],
  },
];
const viewports = [
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'mobile', width: 390, height: 844 },
];
const themes = ['light', 'dark'];

function assert(condition, message) {
  if (!condition) throw new Error(message);
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
        const context = await browser.newContext({
          viewport: { width: viewport.width, height: viewport.height },
          colorScheme: theme,
          reducedMotion: 'reduce',
          deviceScaleFactor: 1,
        });
        await context.addInitScript((selectedTheme) => {
          localStorage.setItem('mf-theme', selectedTheme);
        }, theme);
        const page = await context.newPage();
        const label = `${route.slug}-${viewport.name}-${theme}`;

        try {
          await page.goto(`${baseURL}${route.path}`, { waitUntil: 'networkidle', timeout: 45_000 });
          await page.addStyleTag({
            content: `*,*::before,*::after{animation-duration:0s!important;animation-delay:0s!important;transition:none!important;caret-color:transparent!important}`,
          });
          await page.waitForTimeout(100);

          const bodyText = await page.locator('body').innerText();
          assert(bodyText.includes(route.expected), `${label}: target positioning text is not visible`);

          const htmlTheme = await page.locator('html').getAttribute('data-theme');
          assert(htmlTheme === theme, `${label}: expected theme ${theme}, found ${htmlTheme}`);

          const overflow = await page.evaluate(() => ({
            scrollWidth: document.documentElement.scrollWidth,
            clientWidth: document.documentElement.clientWidth,
          }));
          assert(
            overflow.scrollWidth <= overflow.clientWidth + 1,
            `${label}: horizontal overflow ${overflow.scrollWidth}px > ${overflow.clientWidth}px`,
          );

          const brokenImages = await page.locator('img').evaluateAll((images) =>
            images
              .filter((img) => !img.complete || img.naturalWidth === 0)
              .map((img) => img.getAttribute('src') || '[missing src]'),
          );
          assert(brokenImages.length === 0, `${label}: broken images: ${brokenImages.join(', ')}`);

          const clippedText = await page.locator('main h1, main h2, main h3, main p, main li, main dt, main dd').evaluateAll((elements) =>
            elements.flatMap((element) => {
              const style = getComputedStyle(element);
              if (style.display === 'none' || style.visibility === 'hidden' || !element.textContent?.trim()) return [];
              const xClipped = ['hidden', 'clip'].includes(style.overflowX) && element.scrollWidth > element.clientWidth + 2;
              const yClipped = ['hidden', 'clip'].includes(style.overflowY) && element.scrollHeight > element.clientHeight + 2;
              return xClipped || yClipped
                ? [{ text: element.textContent.trim().slice(0, 90), xClipped, yClipped }]
                : [];
            }),
          );
          assert(clippedText.length === 0, `${label}: clipped text: ${JSON.stringify(clippedText.slice(0, 5))}`);

          const pdfLinks = await page.locator('a[href$=".pdf"]').evaluateAll((links) =>
            links.map((link) => link.getAttribute('href') || ''),
          );
          assert(pdfLinks.length > 0, `${label}: no resume link found`);
          assert(
            pdfLinks.every((href) => href.includes(route.cv)),
            `${label}: stale or incorrect resume link: ${pdfLinks.join(', ')}`,
          );

          for (const anchor of route.anchors) {
            assert((await page.locator(anchor).count()) === 1, `${label}: missing strategic section ${anchor}`);
          }

          if (viewport.name === 'mobile') {
            const menuButton = page.locator('.menu-button');
            assert((await menuButton.count()) === 1, `${label}: mobile menu button missing`);
            await menuButton.click();
            assert((await menuButton.getAttribute('aria-expanded')) === 'true', `${label}: mobile menu did not open`);
            await page.keyboard.press('Escape');
            assert((await menuButton.getAttribute('aria-expanded')) === 'false', `${label}: mobile menu did not close with Escape`);
          }

          const screenshotPath = path.join(outputRoot, `${label}.png`);
          await page.screenshot({ path: screenshotPath, fullPage: true, animations: 'disabled' });
          screenshots += 1;
          console.log(`OK: ${label}`);
        } catch (error) {
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

console.log(`Portfolio browser smoke completed: ${screenshots} screenshots, 4 strategic routes, 2 viewports and 2 themes.`);
