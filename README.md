# Hipoterapia Bydgoszcz

Strona internetowa **Bydgoskiego Towarzystwa Hipoterapeutycznego "Myślęcinek"** — organizacji prowadzącej hipoterapię dla dzieci i dorosłych z niepełnosprawnościami w Bydgoszczy.

**Produkcja:** [nowa.hipoterapia.bydgoszcz.pl](https://nowa.hipoterapia.bydgoszcz.pl/)
**Repozytorium:** [github.com/adamkempczynski/hipoterapia-bydgoszcz](https://github.com/adamkempczynski/hipoterapia-bydgoszcz)

## Stack technologiczny

- [Astro 5](https://astro.build/) — generator stron statycznych
- [Tailwind CSS 3](https://tailwindcss.com/) — stylowanie
- [MDX](https://mdxjs.com/) — treści aktualności (Markdown + komponenty Astro)
- [Decap CMS](https://decapcms.org/) — panel administracyjny do zarządzania treścią
- [GLightbox](https://biati-digital.github.io/glightbox/) — lightbox do galerii zdjęć
- [Leaflet](https://leafletjs.com/) — mapy interaktywne

Hosting: **Netlify** (statyczny build + CDN + Identity)

## Szybki start

```bash
# Instalacja zależności
npm install

# Serwer deweloperski (localhost:4321)
npm run dev

# Lokalny panel CMS (wymaga osobnego terminala)
npm run cms
```

Panel administracyjny: [localhost:4321/admin/](http://localhost:4321/admin/) (w trybie lokalnym bez autentykacji)

## Komendy

| Komenda | Opis |
|---|---|
| `npm run dev` | Serwer deweloperski na `localhost:4321` |
| `npm run build` | Build produkcyjny do `./dist/` |
| `npm run preview` | Podgląd builda produkcyjnego |
| `npm run astro` | Komendy CLI Astro |
| `npm run cms` | Backend Decap CMS na porcie 8081 |

## Struktura projektu

```
src/
├── assets/          # Obrazy optymalizowane przy buildzie (hero, itp.)
├── components/      # Komponenty Astro (Navigation, Footer, Gallery, LocationsMap, Breadcrumbs)
├── content/         # Content Collections — aktualności w MDX + schemat Zod
├── layouts/         # Layouty stron (MainLayout.astro)
├── pages/           # Routing oparty na plikach (30 stron)
└── styles/          # Tailwind CSS (global.css)

public/
├── admin/           # Konfiguracja Decap CMS (config.yml)
└── uploads/         # Obrazy i pliki statyczne (galerie, logo)
```

Pełna dokumentacja architektury: [CLAUDE.md](CLAUDE.md)

## Zarządzanie treścią

Aktualności można dodawać na dwa sposoby:

1. **Przez panel CMS** (`/admin/`) — przyjazny interfejs, nie wymaga znajomości kodu
2. **Ręcznie** — nowy plik `.mdx` w `src/content/aktualnosci/` z frontmatter

Dokumentacja CMS:
- [CMS-README.md](CMS-README.md) — dokumentacja techniczna
- [CMS-INSTRUKCJA.md](CMS-INSTRUKCJA.md) — instrukcja obsługi dla redaktorów

## Konfiguracja

- [SETUP.md](SETUP.md) — formularz kontaktowy (Web3Forms), optymalizacja obrazów
- [CLAUDE.md](CLAUDE.md) — pełna dokumentacja architektury, komponentów, konwencji

## Deployment

Push do brancha `main` automatycznie uruchamia build na Netlify:

```
git push → Netlify build (npm run build) → deploy z dist/
```

Konfiguracja Netlify: `netlify.toml`

## Licencja

Projekt jest własnością Bydgoskiego Towarzystwa Hipoterapeutycznego "Myślęcinek".
