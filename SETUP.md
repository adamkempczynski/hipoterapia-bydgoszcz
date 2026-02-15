# Konfiguracja Strony

## Formularz Kontaktowy

Formularz kontaktowy używa **Netlify Forms** — wbudowanej funkcji Netlify, bez zewnętrznych serwisów.

Zgłoszenia są zapisywane w panelu Netlify (Forms) i mogą być wysyłane jako powiadomienia e-mail.

### Konfiguracja powiadomień e-mail

1. Wejdź na [app.netlify.com](https://app.netlify.com/) → projekt **hipoterapiabydgoszcz**
2. **Site configuration** → **Forms** → **Form notifications**
3. **Add notification** → **Email notification**
4. Wpisz adres e-mail, na który mają przychodzić wiadomości

### Limity

- Darmowy plan: **100 zgłoszeń/miesiąc**
- Ochrona przed spamem: honeypot (`bot-field`)

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
