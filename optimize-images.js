import sharp from 'sharp';
import { readdir, stat, mkdir } from 'fs/promises';
import { join, dirname, basename, extname } from 'path';
import { existsSync } from 'fs';

const UPLOADS_DIR = './public/uploads';
const MAX_WIDTH = 1920;
const MAX_HEIGHT = 1080;
const QUALITY = 80;
const MAX_SIZE_MB = 0.2; // 200KB target

async function getAllImages(dir) {
  const files = await readdir(dir);
  const images = [];

  for (const file of files) {
    const fullPath = join(dir, file);
    const stats = await stat(fullPath);

    if (stats.isDirectory()) {
      const subImages = await getAllImages(fullPath);
      images.push(...subImages);
    } else if (/\.(jpg|jpeg|png)$/i.test(file)) {
      images.push(fullPath);
    }
  }

  return images;
}

async function optimizeImage(imagePath) {
  const stats = await stat(imagePath);
  const sizeMB = stats.size / (1024 * 1024);

  const ext = extname(imagePath).toLowerCase();
  const dir = dirname(imagePath);
  const base = basename(imagePath, ext);
  const webpPath = join(dir, `${base}.webp`);

  // Check if WebP already exists
  if (existsSync(webpPath)) {
    console.log(`\n⏭️  ${imagePath} - WebP już istnieje`);
    return;
  }

  console.log(`\n📸 ${imagePath}`);
  console.log(`   Rozmiar przed: ${sizeMB.toFixed(2)}MB`);

  try {
    const image = sharp(imagePath);
    const metadata = await image.metadata();

    // Resize if too large
    let pipeline = image;
    if (metadata.width > MAX_WIDTH || metadata.height > MAX_HEIGHT) {
      pipeline = pipeline.resize(MAX_WIDTH, MAX_HEIGHT, {
        fit: 'inside',
        withoutEnlargement: true
      });
    }

    // Convert to WebP
    await pipeline
      .webp({ quality: QUALITY })
      .toFile(webpPath);

    const newStats = await stat(webpPath);
    const newSizeMB = newStats.size / (1024 * 1024);
    const savings = ((sizeMB - newSizeMB) / sizeMB * 100).toFixed(1);

    console.log(`   ✨ Rozmiar po: ${newSizeMB.toFixed(2)}MB`);
    console.log(`   💾 Oszczędność: ${savings}%`);
    console.log(`   📁 WebP: ${webpPath}`);

  } catch (error) {
    console.error(`   ❌ Błąd: ${error.message}`);
  }
}

async function main() {
  console.log('🚀 Rozpoczynam optymalizację obrazów...\n');

  const images = await getAllImages(UPLOADS_DIR);
  console.log(`📊 Znaleziono ${images.length} obrazów\n`);

  for (const imagePath of images) {
    await optimizeImage(imagePath);
  }

  console.log('\n✅ Optymalizacja zakończona!');
}

main().catch(console.error);
