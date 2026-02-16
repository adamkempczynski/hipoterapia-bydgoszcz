import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://nowa.hipoterapia.bydgoszcz.pl',
  integrations: [
    mdx(),
    tailwind(),
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
      // Custom configuration for different page types
      customPages: [],
      i18n: {
        defaultLocale: 'pl',
        locales: {
          pl: 'pl-PL',
        },
      },
    })
  ],
  vite: {
    resolve: {
      alias: {
        '@': '/src'
      }
    }
  }
});