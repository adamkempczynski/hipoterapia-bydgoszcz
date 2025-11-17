import playwright from 'playwright';

(async () => {
  const browser = await playwright.chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 }
  });
  const page = await context.newPage();

  const pages = [
    { url: 'http://localhost:4321/oferta/', name: 'oferta' },
    { url: 'http://localhost:4321/galeria/', name: 'galeria' },
    { url: 'http://localhost:4321/kontakt/', name: 'kontakt' },
    { url: 'http://localhost:4321/aktualnosci/', name: 'aktualnosci' },
    { url: 'http://localhost:4321/o-hipoterapii/', name: 'o-hipoterapii' },
    { url: 'http://localhost:4321/towarzystwo/', name: 'towarzystwo' }
  ];

  for (const pageInfo of pages) {
    console.log(`Otwieranie strony ${pageInfo.name}...`);
    await page.goto(pageInfo.url, { waitUntil: 'networkidle' });
    await page.screenshot({ path: `screenshots/${pageInfo.name}-desktop.png`, fullPage: true });
    console.log(`✓ Screenshot ${pageInfo.name} zapisany`);
  }

  await browser.close();
  console.log('Gotowe!');
})();
