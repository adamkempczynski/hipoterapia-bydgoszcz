#!/usr/bin/env python3
"""
Ekstrakcja postów ze starej strony hipoterapia.bydgoszcz.pl.

Każdy post to blok: <tr> ... <td class="tabela" ...> TREŚĆ </td> ... </tr>
Skrypt wyciąga treść każdego takiego bloku i próbuje wyekstrahować tytuł/datę.
"""

import re
import html
from pathlib import Path


def strip_tags(text: str) -> str:
    """Usuń tagi HTML i oczyść tekst."""
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n+', '\n', text)
    return text.strip()


def extract_title(content: str) -> str:
    """Próbuj wyekstrahować tytuł z treści posta."""
    # Szukaj w <h3>, <h2>, <h1>
    for tag in ['h3', 'h2', 'h1']:
        match = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', content, re.DOTALL | re.IGNORECASE)
        if match:
            title = strip_tags(match.group(1)).strip()
            if title and len(title) > 3:
                return title[:120]

    # Szukaj w <p> z bold/underline (częsty wzorzec na starej stronie)
    match = re.search(
        r'<p[^>]*(?:text-decoration:\s*underline|font-weight:\s*bold)[^>]*>(.*?)</p>',
        content, re.DOTALL | re.IGNORECASE
    )
    if match:
        title = strip_tags(match.group(1)).strip()
        if title and len(title) > 3:
            return title[:120]

    # Szukaj w <em> lub <b> na początku
    match = re.search(r'<(?:em|b|strong)[^>]*>(.*?)</(?:em|b|strong)>', content, re.DOTALL | re.IGNORECASE)
    if match:
        title = strip_tags(match.group(1)).strip()
        if title and len(title) > 3:
            return title[:120]

    # Fallback: pierwsze zdanie tekstu
    plain = strip_tags(content)
    first_line = plain.split('\n')[0].strip()
    if first_line:
        return first_line[:120]

    return "(brak tytułu)"


def extract_date(content: str) -> str:
    """Próbuj wyekstrahować datę z treści posta."""
    # Wzorce dat: DD.MM.YYYY, DD.MM.YY, DD/MM/YYYY, YYYY
    patterns = [
        r'(\d{1,2}\.\d{1,2}\.\d{4})',       # 28.11.2025
        r'(\d{1,2}\.\d{1,2}\.\d{2})(?!\d)',  # 28.11.25
        r'(\d{1,2}/\d{1,2}/\d{4})',          # 28/11/2025
    ]
    for pat in patterns:
        match = re.search(pat, content)
        if match:
            return match.group(1)
    return ""


def extract_images(content: str) -> list[str]:
    """Wyekstrahuj ścieżki do obrazów."""
    # img src
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    # lightbox href
    lightbox = re.findall(r'<a[^>]+href=["\']([^"\']+\.(?:jpg|jpeg|png|gif|webp))["\']', content, re.IGNORECASE)
    all_imgs = list(dict.fromkeys(imgs + lightbox))  # deduplikacja z zachowaniem kolejności
    return all_imgs


def extract_posts(filepath: str) -> list[dict]:
    """Główna funkcja: wyekstrahuj wszystkie posty z pliku HTML."""
    text = Path(filepath).read_text(encoding='utf-8')

    # Znajdź wszystkie bloki <tr>...<td class="tabela"...>TREŚĆ</td>...</tr>
    # Regex: szukaj <tr>, potem <td class="tabela", potem treść do </td>, potem </tr>
    pattern = re.compile(
        r'<tr[^>]*>\s*'                           # <tr>
        r'<td\s+class="tabela"[^>]*>'             # <td class="tabela" ...>
        r'(.*?)'                                   # TREŚĆ (lazy)
        r'</td>\s*'                                # </td>
        r'</tr>',                                  # </tr>
        re.DOTALL | re.IGNORECASE
    )

    posts = []
    for i, match in enumerate(pattern.finditer(text)):
        content = match.group(1).strip()

        # Pomiń bardzo krótkie bloki (np. puste komórki)
        plain_text = strip_tags(content)
        if len(plain_text) < 20:
            continue

        title = extract_title(content)
        date = extract_date(content)
        images = extract_images(content)

        posts.append({
            'nr': len(posts) + 1,
            'title': title,
            'date': date,
            'images_count': len(images),
            'images': images,
            'text_length': len(plain_text),
            'text_preview': plain_text[:200],
            'raw_html': content,
            'start_pos': match.start(),
        })

    return posts


def main():
    filepath = Path(__file__).parent / 'stary_index.txt'

    if not filepath.exists():
        print(f"Nie znaleziono pliku: {filepath}")
        return

    posts = extract_posts(str(filepath))

    print(f"{'='*80}")
    print(f"POSTY ZE STAREJ STRONY hipoterapia.bydgoszcz.pl")
    print(f"Znaleziono: {len(posts)} postów")
    print(f"{'='*80}\n")

    for post in posts:
        date_str = f" | Data: {post['date']}" if post['date'] else ""
        img_str = f" | Obrazy: {post['images_count']}" if post['images_count'] > 0 else ""
        print(f"[{post['nr']:3d}] {post['title']}")
        print(f"      {date_str}{img_str} | Długość tekstu: {post['text_length']} znaków")
        if post['images_count'] > 0:
            for img in post['images'][:5]:  # max 5 obrazów w podglądzie
                print(f"        📷 {img}")
            if post['images_count'] > 5:
                print(f"        ... i {post['images_count'] - 5} więcej")
        print()

    # Podsumowanie
    print(f"{'='*80}")
    print(f"PODSUMOWANIE")
    print(f"{'='*80}")
    print(f"Łącznie postów: {len(posts)}")
    with_dates = sum(1 for p in posts if p['date'])
    with_images = sum(1 for p in posts if p['images_count'] > 0)
    total_images = sum(p['images_count'] for p in posts)
    print(f"Postów z datą: {with_dates}")
    print(f"Postów z obrazami: {with_images} (łącznie {total_images} obrazów)")

    # Zapisz surowe dane do pliku
    output = filepath.parent / 'extracted_posts.txt'
    with open(output, 'w', encoding='utf-8') as f:
        for post in posts:
            f.write(f"{'='*80}\n")
            f.write(f"POST #{post['nr']}\n")
            f.write(f"Tytuł: {post['title']}\n")
            f.write(f"Data: {post['date'] or '(brak)'}\n")
            f.write(f"Obrazów: {post['images_count']}\n")
            if post['images']:
                f.write(f"Obrazy: {', '.join(post['images'])}\n")
            f.write(f"{'─'*80}\n")
            f.write(f"{strip_tags(post['raw_html'])}\n\n")

    print(f"\nSzczegóły zapisane do: {output}")

    # Zapisz listę tytułów do osobnego pliku
    titles_output = filepath.parent / 'extracted_titles.txt'
    with open(titles_output, 'w', encoding='utf-8') as f:
        f.write(f"TYTUŁY POSTÓW ZE STAREJ STRONY ({len(posts)} postów)\n")
        f.write(f"{'='*80}\n\n")
        for post in posts:
            date_str = f"  [{post['date']}]" if post['date'] else ""
            title_clean = post['title'].replace('\n', ' ')
            f.write(f"{post['nr']:3d}. {title_clean}{date_str}\n")

    print(f"Lista tytułów zapisana do: {titles_output}")


if __name__ == '__main__':
    main()
