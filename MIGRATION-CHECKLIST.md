# 🚀 Checklist Migracji na Produkcję

## Przed przełączeniem na `hipoterapia.bydgoszcz.pl`

### 1. ✅ **Zaktualizuj robots.txt**
**Plik:** `public/robots.txt`

Zmień z:
```txt
User-agent: *
Disallow: /
```

Na:
```txt
User-agent: *
Allow: /

Sitemap: https://hipoterapia.bydgoszcz.pl/sitemap.xml
```

---

### 2. ✅ **Zaktualizuj astro.config.mjs**
**Plik:** `astro.config.mjs`

Zmień:
```js
site: 'https://nowa.hipoterapia.bydgoszcz.pl',
```

Na:
```js
site: 'https://hipoterapia.bydgoszcz.pl',
```

---

### 3. ✅ **Zaktualizuj Schema.org URLs**
**Plik:** `src/components/StructuredData.astro`

Znajdź wszystkie wystąpienia `nowa.hipoterapia.bydgoszcz.pl` i zamień na `hipoterapia.bydgoszcz.pl`:

```astro
"@id": "https://hipoterapia.bydgoszcz.pl/#localbusiness",
"url": "https://hipoterapia.bydgoszcz.pl",
"logo": "https://hipoterapia.bydgoszcz.pl/uploads/logos/logo_bw.webp",
// ... etc
```

**Szybka zamiana:**
```bash
# W terminalu (z głównego katalogu projektu):
find src/components -name "*.astro" -type f -exec sed -i 's/nowa\.hipoterapia\.bydgoszcz\.pl/hipoterapia.bydgoszcz.pl/g' {} +
```

---

### 4. ✅ **Zaktualizuj MainLayout.astro**
**Plik:** `src/layouts/MainLayout.astro`

Znajdź i zamień wszystkie Open Graph / canonical URLs:

```astro
<meta property="og:url" content="https://hipoterapia.bydgoszcz.pl/" />
<link rel="canonical" href={`https://hipoterapia.bydgoszcz.pl${Astro.url.pathname}`} />
```

**Szybka zamiana:**
```bash
sed -i 's/nowa\.hipoterapia\.bydgoszcz\.pl/hipoterapia.bydgoszcz.pl/g' src/layouts/MainLayout.astro
```

---

### 5. ✅ **Rebuild i Deploy**

```bash
npm run build
git add .
git commit -m "Migracja na domenę produkcyjną hipoterapia.bydgoszcz.pl"
git push origin main
```

Netlify automatycznie zbuduje i wdroży nową wersję.

---

### 6. ✅ **Konfiguracja Netlify (ręcznie w panelu)**

1. Wejdź do Netlify Dashboard → Twój projekt
2. **Domain settings** → Dodaj `hipoterapia.bydgoszcz.pl` jako primary domain
3. **DNS:** Ustaw rekord DNS u rejestratora domeny:
   - Typ: `CNAME` lub `A`
   - Host: `@` lub `hipoterapia`
   - Value: Netlify domain (np. `hipoterapiabydgoszcz.netlify.app`)
4. Zaczekaj na propagację DNS (5-30 min)
5. Włącz SSL certificate (automatycznie w Netlify)

---

### 7. ✅ **Redirect starej strony (opcjonalnie)**

Jeśli chcesz przekierować ruch ze starej strony:

**Plik:** `netlify.toml` (dodaj na końcu)

```toml
# Redirect old domain to new
[[redirects]]
  from = "https://nowa.hipoterapia.bydgoszcz.pl/*"
  to = "https://hipoterapia.bydgoszcz.pl/:splat"
  status = 301
  force = true
```

---

### 8. ✅ **Google Search Console**

Po migracji:

1. Dodaj `hipoterapia.bydgoszcz.pl` do Google Search Console
2. Wyślij sitemap: `https://hipoterapia.bydgoszcz.pl/sitemap-0.xml`
3. Zgłoś zmianę adresu (jeśli stara domena była w GSC):
   - GSC → Settings → Change of address
   - Wybierz nową domenę

---

### 9. ✅ **Google Business Profile**

Zaktualizuj URL strony w profilu Google Business:
1. Wejdź: https://business.google.com
2. Twój profil → Edytuj → Strona internetowa
3. Zmień na: `https://hipoterapia.bydgoszcz.pl`

---

### 10. ✅ **Testowanie po migracji**

Sprawdź:
- ✅ Czy strona ładuje się poprawnie na nowej domenie
- ✅ Czy wszystkie linki wewnętrzne działają
- ✅ Czy obrazy się ładują
- ✅ Czy formularz kontaktowy działa (Netlify Forms)
- ✅ Czy sitemap jest dostępny: `/sitemap-0.xml`
- ✅ Czy robots.txt jest poprawny: `/robots.txt`
- ✅ Czy Schema.org się waliduje: https://search.google.com/test/rich-results
- ✅ Czy SSL certificate jest aktywny (zielona kłódka)

---

## 🎯 **Quick Commands (wszystko w jednym)**

```bash
# 1. Zaktualizuj wszystkie URLe w plikach
find src -name "*.astro" -type f -exec sed -i 's/nowa\.hipoterapia\.bydgoszcz\.pl/hipoterapia.bydgoszcz.pl/g' {} +
find public -name "robots.txt" -type f -exec sed -i 's/nowa\.hipoterapia\.bydgoszcz\.pl/hipoterapia.bydgoszcz.pl/g' {} +

# 2. Zaktualizuj astro.config.mjs (ręcznie)
# 3. Zaktualizuj robots.txt (usuń Disallow: /, dodaj Sitemap)

# 4. Build i deploy
npm run build
git add .
git commit -m "Migracja na domenę produkcyjną hipoterapia.bydgoszcz.pl"
git push origin main
```

---

## ⚠️ **Ważne uwagi:**

1. **Backup:** Przed migracją zrób backup obecnej strony produkcyjnej (jeśli istnieje)
2. **Downtime:** Migracja może zająć 5-30 minut (propagacja DNS)
3. **SEO:** Po migracji Google może potrzebować 2-4 tygodni na pełną reindeksację
4. **301 Redirects:** Jeśli stara strona miała pozycje w Google, skonfiguruj 301 redirects
5. **Testing:** Testuj wszystko dokładnie na testowej domenie przed migracją!

---

## 📞 **Support:**

- Netlify Docs: https://docs.netlify.com/domains-https/custom-domains/
- Astro Docs: https://docs.astro.build/en/guides/deploy/netlify/
- Google Search Console: https://support.google.com/webmasters

---

**Powodzenia z migracją! 🚀**
