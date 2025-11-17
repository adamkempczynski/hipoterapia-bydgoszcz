# Konfiguracja Strony

## Formularz Kontaktowy

Formularz kontaktowy używa [Web3Forms](https://web3forms.com/) - darmowego serwisu do obsługi formularzy.

### Krok 1: Uzyskaj Access Key

1. Odwiedź [https://web3forms.com/](https://web3forms.com/)
2. Wpisz swój adres email
3. Otrzymasz wiadomość z access key

### Krok 2: Skonfiguruj Formularz

W pliku `src/pages/kontakt/index.astro` znajdź linię:

```html
<input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
```

Zamień `YOUR_ACCESS_KEY_HERE` na otrzymany klucz.

### Krok 3: Testuj

Po wdrożeniu na produkcji, przetestuj formularz wysyłając wiadomość testową.

---

## Optymalizacja Obrazów

### Uruchomienie Skryptu Optymalizacji

Aby zoptymalizować wszystkie obrazy w `public/uploads/`:

```bash
# Zainstaluj sharp (już dodany do package.json)
npm install

# Uruchom skrypt optymalizacji
node optimize-images.js
```

Skrypt:
- Konwertuje JPG/PNG do WebP
- Zmniejsza rozmiar do max 1920x1080px
- Kompresuje do jakości 80%
- Tworzy backup oryginałów w folderze `originals/`

**Uwaga**: Po optymalizacji zaktualizuj ścieżki w plikach MDX z `.jpg` na `.webp`

---

## Rozwój

```bash
npm run dev        # Start serwera deweloperskiego
npm run build      # Build produkcyjny
npm run preview    # Podgląd buildu
```
