# CLAUDE.md

Plik opisuje strukturę, konwencje i architekturę projektu. Służy jako źródło prawdy dla Claude Code i każdego, kto pracuje z tym repozytorium.

## Project Overview

Strona internetowa **Bydgoskiego Towarzystwa Hipoterapeutycznego "Myślęcinek"** — organizacji prowadzącej hipoterapię w Bydgoszczy. Strona jest portalem informacyjnym: oferta, zespół, aktualności, galerie zdjęć, kontakt.

**Domena produkcyjna:** `https://nowa.hipoterapia.bydgoszcz.pl/`
**Hosting:** Netlify (statyczny build, CDN)
**GitHub:** `github.com/adamkempczynski/hipoterapia-bydgoszcz`

## Technology Stack

| Technologia | Rola | Konfiguracja |
|---|---|---|
| **Astro 5.x** | Generator stron statycznych | `astro.config.mjs` |
| **MDX** | Treści aktualności (Markdown + komponenty) | `@astrojs/mdx` |
| **Tailwind CSS 3.x** | System stylowania | `tailwind.config.mjs` |
| **TypeScript** | Typy w konfiguracji i komponentach | `tsconfig.json` |
| **GLightbox** | Lightbox do galerii zdjęć | CDN w `MainLayout.astro` |
| **Leaflet** | Mapy interaktywne (OpenStreetMap) | Dynamicznie w `LocationsMap.astro` |
| **Decap CMS** | Panel administracyjny do treści | `public/admin/config.yml` |
| **Netlify Identity** | Autentykacja użytkowników CMS | Widget w `MainLayout.astro` |

## Development Commands

```bash
npm run dev       # Serwer deweloperski — localhost:4321
npm run build     # Build produkcyjny → ./dist/
npm run preview   # Podgląd builda lokalnie
npm run astro     # Komendy CLI Astro
npm run cms       # Backend Decap CMS (port 8081) — wymagany do lokalnej edycji treści
```

**Lokalny CMS** wymaga dwóch terminali: `npm run dev` + `npm run cms`, panel pod `http://localhost:4321/admin/`.

## Project Architecture

### Directory Structure

```
src/
├── assets/                          # Obrazy importowane przez Astro (optymalizacja build-time)
│   ├── hero-image-v2.webp           # Główny obraz hero na stronie głównej
│   └── ATAMAN_Asia.jpg              # Zdjęcie konia
│
├── components/                      # Komponenty Astro (wielokrotnego użytku)
│   ├── Navigation.astro             # Nawigacja — sticky, responsywna, mobile hamburger
│   ├── Footer.astro                 # Stopka — 3 kolumny: o nas, kontakt, szybkie linki
│   ├── Gallery.astro                # Galeria zdjęć — siatka + GLightbox + skeleton loader
│   ├── LocationsMap.astro           # Mapa Leaflet — 2 lokalizacje (siedziba + Jarużyn)
│   └── Breadcrumbs.astro            # Okruszki nawigacyjne + schema.org BreadcrumbList
│
├── content/                         # Content Collections (Astro)
│   ├── aktualnosci/                 # ~37 plików MDX z aktualnościami
│   └── config.ts                    # Schemat Zod dla kolekcji
│
├── layouts/
│   ├── MainLayout.astro             # Główny layout — Navigation, Footer, SEO, GLightbox, Netlify Identity
│   └── Layout.astro                 # Bazowy layout (legacy, minimalny)
│
├── pages/                           # Routing oparty na plikach
│   ├── index.astro                  # Strona główna — hero, cechy, aktualności, CTA
│   ├── 404.astro                    # Strona błędu 404
│   ├── linki.astro                  # Strona z linkami
│   │
│   ├── oferta/
│   │   ├── index.astro              # Oferta — cennik, harmonogram, usługi
│   │   ├── kadra.astro              # Kadra / zespół
│   │   ├── konie.astro              # Konie terapeutyczne
│   │   ├── regulamin.astro          # Regulamin
│   │   ├── dokumenty-rozliczeniowe.astro  # Dokumenty finansowe
│   │   └── wolontariusze.astro      # Informacje dla wolontariuszy
│   │
│   ├── o-hipoterapii/
│   │   └── index.astro              # Czym jest hipoterapia
│   │
│   ├── aktualnosci/
│   │   ├── index.astro              # Archiwum — nawigacja po latach i kategoriach
│   │   ├── [year].astro             # Filtr po roku (dynamiczny routing)
│   │   ├── [...slug].astro          # Fallback catch-all
│   │   ├── wpis/
│   │   │   └── [slug].astro         # Pojedynczy wpis aktualności
│   │   └── kategoria/
│   │       └── [category].astro     # Filtr po kategorii
│   │
│   ├── galeria/
│   │   └── index.astro              # Galerie zdjęć z wielu wydarzeń
│   │
│   ├── towarzystwo/
│   │   ├── index.astro              # Przegląd organizacji — misja, historia, wartości
│   │   ├── zarzad.astro             # Zarząd
│   │   ├── historia.astro           # Historia organizacji
│   │   ├── statut.astro             # Statut
│   │   ├── kalendarium.astro        # Kalendarium wydarzeń
│   │   ├── sprawozdania-opp.astro   # Sprawozdania OPP
│   │   ├── druki-do-pobrania.astro  # Dokumenty do pobrania
│   │   └── numer-konta.astro        # Dane do wpłat / darowizn
│   │
│   ├── kontakt/
│   │   └── index.astro              # Kontakt — formularz (Web3Forms), mapa, godziny
│   │
│   ├── onas/
│   │   └── index.astro              # O nas
│   │
│   ├── faq/
│   │   └── index.astro              # Najczęściej zadawane pytania
│   │
│   ├── rodo/
│   │   └── index.astro              # Polityka prywatności RODO
│   │
│   ├── standardy-ochrony-maloletnich/
│   │   └── index.astro              # Standardy ochrony małoletnich
│   │
│   └── admin/
│       └── index.astro              # Panel Decap CMS
│
└── styles/
    └── global.css                   # Tailwind directives + klasy komponentów (.btn, .card, .gradient-bg)

public/
├── admin/
│   ├── config.yml                   # Konfiguracja Decap CMS
│   └── index.html                   # Entry point panelu CMS
├── uploads/                         # Obrazy i pliki statyczne
│   ├── logos/                       # Logo organizacji (logo_bw.webp)
│   ├── bal_jubileuszowy_2025/       # Galerie pogrupowane wg wydarzeń
│   ├── splyw_2025/
│   ├── mecz_28_09_2024/
│   ├── biwak_09_2024/
│   ├── biwak_jaruzyn_2024/
│   ├── splyw_09_06_2024/
│   ├── konie/
│   └── ...                          # Pojedyncze obrazy (hero, plakaty)
├── favicon.svg
└── netlify.toml                     # Konfiguracja Netlify (build, headers, redirects)
```

### Content Collections

Kolekcja `aktualnosci` — pliki MDX w `src/content/aktualnosci/`.

**Schemat** (zdefiniowany w `src/content/config.ts`):

| Pole | Typ | Wymagane | Opis |
|---|---|---|---|
| `title` | `string` | tak | Tytuł aktualności |
| `pubDate` | `date` | tak | Data publikacji (YYYY-MM-DD) |
| `description` | `string` | nie | Krótki opis na listach |
| `image` | `string` | nie | Ścieżka do obrazka głównego |
| `category` | `enum` | nie | Kategoria wydarzenia |
| `gallery` | `string[]` | nie | Lista ścieżek do zdjęć galerii |

**Kategorie** (wartości enum w `category`):
- `biwaki-wycieczki` — Biwaki i wycieczki
- `wydarzenia-sportowe` — Wydarzenia sportowe
- `zebrania-organizacyjne` — Zebrania i sprawy organizacyjne
- `wydarzenia-spoleczne` — Wydarzenia społeczne
- `programy-dotacyjne` — Programy dotacyjne

### Key Components

#### Navigation.astro
- Sticky navbar z logo (`/uploads/logos/logo_bw.webp`) i menu desktopowym/mobilnym
- Pozycje menu: Strona Główna, Oferta, O Hipoterapii, Aktualności, Galeria, Towarzystwo, Kontakt
- Mobile: hamburger button z toggle menu

#### Footer.astro
- 3-kolumnowy layout: Opis organizacji | Kontakt (adres, KRS) | Szybkie linki + 1.5% podatku
- Link do Facebook: `https://www.facebook.com/bthip.myslecinek/`
- Copyright z dynamicznym rokiem
- Oficjalna nazwa: **Bydgoskie Towarzystwo Hipoterapeutyczne "Myślęcinek"**

#### Gallery.astro
- Props: `imagePaths: string[]`, `galleryId: string`
- Siatka responsywna (auto-fit, minmax 300px / 250px mobile)
- Skeleton loader z animacją shimmer → płynne przejście po załadowaniu obrazu
- IntersectionObserver do lazy loading (rootMargin 50px)
- Hover: zoom obrazu + gradient overlay + licznik zdjęć
- Integracja z GLightbox (data-gallery, data-title)

#### LocationsMap.astro
- Mapa Leaflet z 2 lokalizacjami:
  - **Siedziba**: ul. Gdańska 188, Bydgoszcz (53.140474, 18.018722)
  - **Miejsce zajęć**: Jarużyn, ul. Kolonia 33 (53.202965, 18.131769)
- Dynamiczne ładowanie Leaflet CSS/JS (nie blokuje renderowania)
- Noscript fallback z adresami tekstowymi

#### Breadcrumbs.astro
- Props: `items: { label: string; href?: string }[]`
- Generuje schema.org `BreadcrumbList` JSON-LD
- Responsywne z truncation i ukrytym scrollbarem

#### MainLayout.astro
- Props: `title: string`, `description?: string`
- Importuje Navigation + Footer + `global.css`
- SEO: Open Graph, Twitter Card, canonical URL, keywords
- Ładuje GLightbox (CSS + JS z CDN), inicjalizuje na `DOMContentLoaded`
- Netlify Identity Widget z obsługą invite/recovery tokenów z hash URL

### Styling System

Projekt używa **Tailwind CSS** — konfiguracja w `tailwind.config.mjs`.

**Fonty:**
- `font-sans` → **Inter** (ciało tekstu) — ładowany z Google Fonts w `global.css`
- `font-display` → **Cal Sans** (nagłówki dekoracyjne)

**Kolory** (zdefiniowane w Tailwind config):
- `primary-*` — odcienie zieleni (#f0f9f4 → #14532d) — główny kolor organizacji
- `secondary-*` — odcienie fioletu (#fdf4ff → #581c87) — akcenty

**Klasy komponentów** (zdefiniowane w `src/styles/global.css` w `@layer components`):
- `.btn` / `.btn-primary` / `.btn-secondary` — przyciski z trzema rozmiarami (sm/md/lg)
- `.card` — karta z cieniem, zaokrągleniem, hover: shadow + translate
- `.gradient-bg` — gradient primary 500→600→700
- `.text-gradient` — gradient primary→secondary na tekście

**Animacje** (Tailwind keyframes):
- `fade-in` — opacity 0→1, 0.5s
- `slide-up` — translateY(10px)→0 + opacity, 0.5s
- `bounce-gentle` — translateY ±5px, 2s infinite

### Decap CMS

Panel administracyjny pod `/admin/` do zarządzania aktualnościami bez znajomości kodu.

- **Konfiguracja:** `public/admin/config.yml`
- **Backend:** Git Gateway (produkcja), local backend (development)
- **Editorial workflow:** obecnie wyłączony (zakomentowany w config.yml)
- **Locale:** polski (pl)
- **Media:** upload do `public/uploads/`, publiczna ścieżka `/uploads/`

Szczegółowa dokumentacja CMS: `CMS-README.md` (techniczna), `CMS-INSTRUKCJA.md` (dla użytkowników).

### Image Management

- **Statyczne obrazy:** `public/uploads/` — serwowane bezpośrednio, cache 1 rok (netlify.toml)
- **Obrazy importowane przez Astro:** `src/assets/` — optymalizacja build-time (np. hero image)
- **Galerie w MDX:** ścieżki w frontmatter `gallery`, wyświetlane przez komponent `Gallery.astro`
- **Konwencja nazw folderów:** `nazwazdarzenia_rok/` (np. `bal_jubileuszowy_2025/`)
- **Preferowany format:** WebP; skrypt optymalizacji: `node optimize-images.js`

## Development Guidelines

### Adding New News Articles

1. Utwórz plik `.mdx` w `src/content/aktualnosci/` (nazwa pliku = slug URL)
2. Dodaj frontmatter z wymaganymi polami (`title`, `pubDate`)
3. Opcjonalnie dodaj `category`, `description`, `gallery`
4. Obrazy galerii umieść w `public/uploads/nazwa_wydarzenia/`
5. Jeśli artykuł ma galerię, zaimportuj i użyj komponentu Gallery:

```mdx
---
title: "Tytuł wydarzenia"
pubDate: 2025-01-15
description: "Krótki opis."
category: "wydarzenia-spoleczne"
gallery:
  - /uploads/nazwa_wydarzenia/foto1.webp
  - /uploads/nazwa_wydarzenia/foto2.webp
---

import Gallery from '../../components/Gallery.astro';

Treść artykułu w Markdown...

<Gallery imagePaths={frontmatter.gallery} galleryId="nazwa-wydarzenia" />
```

**Uwaga:** Artykuły bez galerii (np. `nowy-kon.mdx`) nie muszą importować Gallery — pole `gallery` w frontmatter jest opcjonalne, komponent też.

### Alternatywnie: Decap CMS

Nowe aktualności można dodawać przez panel CMS (`/admin/`), który automatycznie tworzy pliki MDX z poprawnym frontmatter. Wymaga konfiguracji Netlify Identity w produkcji lub `npm run cms` lokalnie.

### Page Structure

Wszystkie strony używają `MainLayout.astro` z prop `title`. Layout zapewnia nawigację, stopkę, SEO i skrypty.

### Configuration Notes

- **Astro Config** (`astro.config.mjs`): integracje MDX + Tailwind, alias `@` → `/src`
- **Tailwind** (`tailwind.config.mjs`): custom fonty, kolory, animacje, plugin `@tailwindcss/typography`
- **Netlify** (`netlify.toml`): build command, cache na uploads, redirect
- **TypeScript** (`tsconfig.json`): alias `@` → `/src`
- **Brak lintingu/testów**: projekt nie używa ESLint, Prettier ani frameworka testowego
- **Formularz kontaktowy**: Web3Forms (wymaga klucza API — aktualnie placeholder `YOUR_ACCESS_KEY_HERE` w `kontakt/index.astro`)

## File-based Routing

| Plik | URL |
|---|---|
| `pages/index.astro` | `/` |
| `pages/oferta/index.astro` | `/oferta/` |
| `pages/oferta/kadra.astro` | `/oferta/kadra/` |
| `pages/aktualnosci/index.astro` | `/aktualnosci/` |
| `pages/aktualnosci/wpis/[slug].astro` | `/aktualnosci/wpis/nazwa-wpisu/` |
| `pages/aktualnosci/[year].astro` | `/aktualnosci/2025/` |
| `pages/aktualnosci/kategoria/[category].astro` | `/aktualnosci/kategoria/biwaki-wycieczki/` |
| `pages/towarzystwo/index.astro` | `/towarzystwo/` |
| `pages/towarzystwo/zarzad.astro` | `/towarzystwo/zarzad/` |
| `pages/kontakt/index.astro` | `/kontakt/` |
| `pages/galeria/index.astro` | `/galeria/` |
| `pages/o-hipoterapii/index.astro` | `/o-hipoterapii/` |
| `pages/faq/index.astro` | `/faq/` |
| `pages/rodo/index.astro` | `/rodo/` |
| `pages/admin/index.astro` | `/admin/` |

## Deployment

### Netlify

| Parametr | Wartość |
|---|---|
| **Domena** | `nowa.hipoterapia.bydgoszcz.pl` |
| **Projekt Netlify** | `hipoterapiabydgoszcz` |
| **Project ID** | `c95f510d-057f-43d8-bb6c-e1ca9b937fd0` |
| **Team** | `hipoterapia-bydgoszcz` |
| **Repo GitHub** | `adamkempczynski/hipoterapia-bydgoszcz` |
| **Branch** | `main` (auto publishing ON) |
| **Build command** | `npm run build` |
| **Publish directory** | `dist/` |

**Flow:** `git push main` → Netlify webhook → `npm run build` → deploy z `dist/`

**Netlify Identity:**
- Włączone, rejestracja invite-only (max 5 użytkowników na darmowym planie)
- Endpoint: `https://nowa.hipoterapia.bydgoszcz.pl/.netlify/identity`
- Wymagane do logowania w panelu CMS na produkcji (`/admin/`)
- Aktualnie 0 zaproszonych użytkowników — aby ktoś mógł korzystać z CMS, trzeba go zaprosić z panelu Netlify (Identity → Invite users)

**Konfiguracja Netlify** (`netlify.toml`):
- Cache na `/uploads/*`: `max-age=31536000` (1 rok)
- Statyczne pliki z `public/` kopiowane do `dist/` bez zmian

### Kontekst

Ta strona (`nowa.hipoterapia.bydgoszcz.pl`) jest nową wersją portalu `hipoterapia.bydgoszcz.pl`. Główna różnica: możliwość dodawania i edycji aktualności przez panel CMS (Decap CMS + Netlify Identity).
