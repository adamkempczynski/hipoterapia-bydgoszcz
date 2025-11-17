import playwright from 'playwright';
import { playAudit } from 'playwright-lighthouse';
import { writeFileSync } from 'fs';

(async () => {
  const browser = await playwright.chromium.launch({ args: ['--remote-debugging-port=9222'] });
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('http://localhost:4321');

  try {
    await playAudit({
      page,
      port: 9222,
      thresholds: {
        performance: 50,
        accessibility: 50,
        'best-practices': 50,
        seo: 50,
      },
      reports: {
        formats: {
          html: true,
        },
        name: 'lighthouse-report',
        directory: './lighthouse-reports',
      },
    });
    console.log('✓ Lighthouse audit completed');
  } catch (error) {
    console.error('Lighthouse error:', error.message);
  }

  await browser.close();
})();
