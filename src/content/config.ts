import { defineCollection, z } from 'astro:content';

// Definiujemy kolekcję dla naszych aktualności
const aktualnosciCollection = defineCollection({
  type: 'content', // Oznacza, że treść będzie pisana np. w Markdown
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string().optional(), // Krótki opis, opcjonalny
    image: z.string().optional(),       // Ścieżka do obrazka, opcjonalna
    category: z.enum(['biwaki-wycieczki', 'wydarzenia-sportowe', 'zebrania-organizacyjne', 'wydarzenia-spoleczne', 'programy-dotacyjne']).optional(), // Kategoria wydarzenia
    gallery: z.array(z.string()).optional(), // Galeria zdjęć
  }),
});

// Eksportujemy kolekcje, aby Astro o nich wiedział
export const collections = {
  'aktualnosci': aktualnosciCollection,
};