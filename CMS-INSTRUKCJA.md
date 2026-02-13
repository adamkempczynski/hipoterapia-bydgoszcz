# Panel Administracyjny - Instrukcja Obsługi

## Spis treści
- [Co to jest Decap CMS?](#co-to-jest-decap-cms)
- [Dostęp do panelu](#dostęp-do-panelu)
- [Testowanie lokalne](#testowanie-lokalne)
- [Konfiguracja produkcyjna](#konfiguracja-produkcyjna)
- [Jak dodać nową aktualność](#jak-dodać-nową-aktualność)
- [Jak edytować istniejącą aktualność](#jak-edytować-istniejącą-aktualność)
- [Jak dodać zdjęcia do galerii](#jak-dodać-zdjęcia-do-galerii)
- [Wskazówki dotyczące formatowania](#wskazówki-dotyczące-formatowania)
- [Rozwiązywanie problemów](#rozwiązywanie-problemów)

---

## Co to jest Decap CMS?

Decap CMS to nowoczesny system zarządzania treścią, który:
- Zapisuje zmiany bezpośrednio do repozytorium Git
- Pozwala na edycję treści bez znajomości kodu
- Oferuje przyjazny interfejs WYSIWYG (podobny do Worda)
- Nie wymaga osobnej bazy danych

---

## Dostęp do panelu

### Wersja produkcyjna (po wdrożeniu)
Panel administracyjny będzie dostępny pod adresem:
```
https://nowa.hipoterapia.bydgoszcz.pl/admin/
```

### Wymagania
- Konto GitHub z dostępem do repozytorium projektu
- Konfiguracja Netlify Identity lub GitHub OAuth

---

## Testowanie lokalne

### Krok 1: Uruchom serwer deweloperski
Otwórz **dwa** terminale:

**Terminal 1** - Uruchom stronę Astro:
```bash
npm run dev
```

**Terminal 2** - Uruchom backend CMS:
```bash
npm run cms
```

### Krok 2: Otwórz panel w przeglądarce
```
http://localhost:4321/admin/
```

### Uwaga
W trybie lokalnym (`local_backend: true`) nie potrzebujesz autentykacji. Panel będzie działał bezpośrednio z plikami na dysku.

---

## Konfiguracja produkcyjna

### Opcja 1: Netlify Identity (Zalecane)

#### 1. Zaloguj się do Netlify
Przejdź do [app.netlify.com](https://app.netlify.com/) i znajdź swoją stronę.

#### 2. Włącz Netlify Identity
- Settings → Identity → Enable Identity
- Services → Git Gateway → Enable Git Gateway

#### 3. Zaproś użytkowników
- Identity → Invite users
- Wpisz adresy email osób, które będą dodawać aktualności

#### 4. Wyłącz rejestrację publiczną
- Settings → Identity → Registration → Invite only

#### 5. Gotowe!
Użytkownicy otrzymają email z linkiem aktywacyjnym.

---

### Opcja 2: GitHub OAuth (dla zaawansowanych)

Jeśli nie korzystasz z Netlify, możesz skonfigurować GitHub OAuth:

#### 1. Utwórz GitHub OAuth App
- GitHub → Settings → Developer settings → OAuth Apps → New OAuth App
- **Application name**: Hipoterapia CMS
- **Homepage URL**: `https://nowa.hipoterapia.bydgoszcz.pl`
- **Authorization callback URL**: `https://nowa.hipoterapia.bydgoszcz.pl/admin/`

#### 2. Zapisz Client ID i Client Secret

#### 3. Zaktualizuj konfigurację CMS
Edytuj `public/admin/config.yml`:
```yaml
backend:
  name: github
  repo: adamkempczynski/hipoterapia-bydgoszcz
  branch: main
```

#### 4. Dodaj backend OAuth
Będziesz potrzebować serwera OAuth (np. [netlify-cms-github-oauth-provider](https://github.com/vencax/netlify-cms-github-oauth-provider))

---

## Jak dodać nową aktualność

### Krok po kroku

1. **Zaloguj się do panelu** pod adresem `/admin/`

2. **Kliknij "Aktualności"** w menu bocznym

3. **Kliknij "New Aktualność"**

4. **Wypełnij formularz:**
   - **Tytuł**: Wpisz tytuł aktualności (np. "Biwak w Biskupinie 2025")
   - **Data publikacji**: Wybierz datę z kalendarza
   - **Krótki opis**: Wpisz jedno-dwa zdania podsumowania (opcjonalne)
   - **Kategoria**: Wybierz z listy rozwijanej:
     - Biwaki i wycieczki
     - Wydarzenia sportowe
     - Zebrania i sprawy organizacyjne
     - Wydarzenia społeczne
     - Programy dotacyjne
   - **Galeria zdjęć**: Zobacz sekcję poniżej
   - **Treść**: Wpisz główną treść wpisu

5. **Zapisz zmiany:**
   - **"Save"** - zapisuje szkic (draft)
   - **"Publish"** - publikuje od razu
   - **"Set status → Ready"** - oznacza jako gotowe do recenzji

6. **Gotowe!** Aktualność pojawi się na stronie po przebudowaniu.

---

## Jak edytować istniejącą aktualność

1. Zaloguj się do panelu (`/admin/`)
2. Kliknij "Aktualności" w menu
3. Znajdź aktualność na liście i kliknij w nią
4. Edytuj potrzebne pola
5. Kliknij "Save" lub "Publish"

---

## Jak dodać zdjęcia do galerii

### Sposób 1: Przeciągnij i upuść

1. W formularzu aktualności znajdź sekcję **"Galeria zdjęć"**
2. Kliknij **"Add Zdjęcie"**
3. **Przeciągnij zdjęcie** z explorera plików na pole "Zdjęcie"
4. Zdjęcie zostanie automatycznie przesłane
5. Powtórz dla każdego zdjęcia

### Sposób 2: Wybierz z dysku

1. Kliknij **"Add Zdjęcie"**
2. Kliknij pole "Zdjęcie"
3. Kliknij **"Choose an image"**
4. Wybierz plik z dysku
5. Poczekaj na upload

### Zmiana kolejności zdjęć

1. Każde zdjęcie w galerii ma ikonę "trzech kresek" ☰
2. Kliknij i przeciągnij zdjęcie na nową pozycję
3. Pierwsze zdjęcie będzie wyświetlane jako główne

### Usuwanie zdjęć

1. Najedź na zdjęcie w galerii
2. Kliknij ikonę kosza (🗑️)
3. Potwierdź usunięcie

---

## Wskazówki dotyczące formatowania

Panel CMS oferuje edytor Markdown z przyciskami formatowania:

### Podstawowe formatowanie

| Element | Jak to zrobić |
|---------|---------------|
| **Pogrubienie** | Zaznacz tekst i kliknij **B** lub użyj `**tekst**` |
| *Kursywa* | Zaznacz tekst i kliknij *I* lub użyj `*tekst*` |
| Link | Zaznacz tekst, kliknij 🔗 i wklej URL |

### Nagłówki

```markdown
## Duży nagłówek (Heading 2)
### Mniejszy nagłówek (Heading 3)
```

Kliknij przycisk **H2** lub **H3** na pasku narzędzi.

### Listy

**Lista punktowana:**
```markdown
- Pierwszy punkt
- Drugi punkt
- Trzeci punkt
```

**Lista numerowana:**
```markdown
1. Pierwszy punkt
2. Drugi punkt
3. Trzeci punkt
```

### Cytaty

```markdown
> To jest cytat
```

Kliknij przycisk **"** na pasku narzędzi.

### Przykład dobrze sformatowanego wpisu

```markdown
Witamy na biegu przełajowym! Wydarzenie było wspaniałe.

## Przebieg wydarzenia

Rozpoczęliśmy o godzinie 10:00 rozgrzewką. Następnie:

- Losowanie numerów startowych
- Instruktaż bezpieczeństwa
- Start biegu

### Wyniki

Gratulujemy wszystkim uczestnikom!

**Pierwsze miejsce**: Jan Kowalski
**Drugie miejsce**: Anna Nowak

## Podziękowania

Dziękujemy sponsorom i wolontariuszom za wsparcie!
```

---

## Rozwiązywanie problemów

### Nie mogę się zalogować

**Problem**: Panel wyświetla błąd logowania

**Rozwiązanie**:
- Sprawdź czy masz dostęp do repozytorium GitHub
- Sprawdź czy Netlify Identity jest włączone
- Sprawdź czy otrzymałeś email z zaproszeniem

---

### Zdjęcia nie wczytują się

**Problem**: Upload zdjęcia nie działa

**Rozwiązanie**:
- Sprawdź połączenie internetowe
- Upewnij się że plik to obraz (JPG, PNG, WebP)
- Spróbuj zmniejszyć rozmiar zdjęcia (max 5MB zalecane)
- Odśwież stronę i spróbuj ponownie

---

### Zmiany nie pojawiają się na stronie

**Problem**: Zapisałem aktualność ale jej nie widać

**Możliwe przyczyny**:
1. **Wpis jest w trybie Draft** - kliknij "Publish" aby opublikować
2. **Strona nie została przebudowana** - poczekaj 2-3 minuty na automatyczne przebudowanie
3. **Cache przeglądarki** - odśwież stronę kombinacją Ctrl+Shift+R (Windows) lub Cmd+Shift+R (Mac)

---

### Galeria nie wyświetla się prawidłowo

**Problem**: Zdjęcia w galerii się nie pokazują

**Rozwiązanie**:
- Sprawdź czy pole "Galeria zdjęć" zawiera ścieżki zdjęć
- Upewnij się że zdjęcia zostały prawidłowo przesłane
- Sprawdź czy ścieżki zaczynają się od `/uploads/`

---

### Formatowanie Markdown nie działa

**Problem**: Nagłówki lub listy wyświetlają się jako zwykły tekst

**Rozwiązanie**:
- Użyj przycisków na pasku narzędzi zamiast ręcznego wpisywania
- Upewnij się że są puste linie przed i po nagłówkach
- Sprawdź czy nie ma spacji przed znakami formatowania

---

## Potrzebujesz pomocy?

Jeśli masz problemy z panelem CMS, skontaktuj się z administratorem technicznym.

**Przydatne linki:**
- [Dokumentacja Decap CMS](https://decapcms.org/docs/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [Repozytorium projektu](https://github.com/adamkempczynski/hipoterapia-bydgoszcz)

---

*Ostatnia aktualizacja: 2026-02-13*
