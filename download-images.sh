#!/bin/bash

# Script to download all images from old hipoterapia website
# Run this from project root directory

echo "🐴 Starting image download from hipoterapia.bydgoszcz.pl..."

# Base URL of the old website
BASE_URL="https://hipoterapia.bydgoszcz.pl"

# Create directory structure
echo "📁 Creating directory structure..."
mkdir -p public/uploads/{aktualnosci,galeria,wydarzenia,logos,konie,biwak_06_2025,splyw_2025,bal_jubileuszowy_2025}

# Function to download image with error handling
download_image() {
    local url="$1"
    local output_path="$2"

    echo "⬇️  Downloading: $url"

    if curl -f -s -o "$output_path" "$url"; then
        echo "✅ Downloaded: $(basename "$output_path")"
        return 0
    else
        echo "❌ Failed: $(basename "$output_path")"
        return 1
    fi
}

# Function to download image with fallback attempts
download_with_fallback() {
    local filename="$1"
    local output_path="$2"
    local base_paths=("" "images/" "img/" "obrazy/" "galeria/")

    for path in "${base_paths[@]}"; do
        local url="${BASE_URL}/${path}${filename}"
        if download_image "$url" "$output_path"; then
            return 0
        fi
    done

    echo "⚠️  Could not find: $filename"
    return 1
}

echo "🖼️  Downloading logos and main images..."

# Download logos
download_with_fallback "logo.jpg" "public/uploads/logos/logo.jpg"
download_with_fallback "logo_bw.gif" "public/uploads/logos/logo_bw.gif"
download_with_fallback "logo_opp_150.png" "public/uploads/logos/logo_opp_150.png"
download_with_fallback "logo_opp_1,5.png" "public/uploads/logos/logo_opp_15.png"

# Download main page images
download_with_fallback "index_na_koniu.jpg" "public/uploads/index_na_koniu.jpg"
download_with_fallback "wielkanoc2022.png" "public/uploads/wydarzenia/wielkanoc2022.png"
download_with_fallback "balony.png" "public/uploads/wydarzenia/balony.png"
download_with_fallback "wojewodztwo_kujawko_pomorskie.jpg" "public/uploads/logos/wojewodztwo_kujawko_pomorskie.jpg"

echo "📸 Downloading Biwak 2025 gallery (20 images)..."

# Download Biwak 2025 images (00 to 19)
for i in {0..19}; do
    # Format number with leading zero for single digits
    num=$(printf "%02d" $i)
    filename="biwak - ${num}.jpg"
    url="${BASE_URL}/obrazy/biwak_06_2025/${filename}"
    output_path="public/uploads/biwak_06_2025/biwak-${num}.jpg"

    download_image "$url" "$output_path"
done

echo "🛶 Downloading Spływ 2025 gallery (8 images)..."

# Download Spływ 2025 images (01 to 08)
for i in {1..8}; do
    num=$(printf "%02d" $i)
    filename="splyw_2025_${num}.jpg"
    url="${BASE_URL}/obrazy/splyw_2025/${filename}"
    output_path="public/uploads/splyw_2025/splyw_2025_${num}.jpg"

    download_image "$url" "$output_path"
done

echo "🎭 Downloading Bal Jubileuszowy 2025 gallery (11 images)..."

# Download Bal Jubileuszowy 2025 images (01 to 11)
for i in {1..11}; do
    num=$(printf "%02d" $i)
    filename="bal_jubileuszowy_2025_${num}.jpg"
    url="${BASE_URL}/obrazy/bal_jubileuszowy_2025/${filename}"
    output_path="public/uploads/bal_jubileuszowy_2025/bal_jubileuszowy_2025_${num}.jpg"

    download_image "$url" "$output_path"
done

echo "⚽ Downloading Mecz 2024 gallery (5 images)..."

# Create directory for mecz 2024
mkdir -p public/uploads/mecz_28_09_2024

# Download Mecz images (1 to 5)
for i in {1..5}; do
    filename="mecz2024-${i}.jpg"
    url="${BASE_URL}/galeria/mecz_28.09.2024/${filename}"
    output_path="public/uploads/mecz_28_09_2024/${filename}"

    download_image "$url" "$output_path"
done

echo "🏕️ Downloading Biwak Jarużyn 2024 gallery (8 images)..."

# Create directory for biwak Jaruzyn
mkdir -p public/uploads/biwak_jaruzyn_2024

# Download Biwak Jaruzyn images (1 to 8)
for i in {1..8}; do
    filename="biwak${i}.jpg"
    url="${BASE_URL}/galeria/biwakJaruzyn2024/${filename}"
    output_path="public/uploads/biwak_jaruzyn_2024/biwak${i}.jpg"

    download_image "$url" "$output_path"
done

echo "🛶 Downloading Spływ 9.06.2024 gallery (7 images)..."

# Create directory for splyw 2024
mkdir -p public/uploads/splyw_09_06_2024

# Download Spływ 9.06.2024 images (1 to 7)
for i in {1..7}; do
    filename="${i}splyw9.06.2024.jpg"
    url="${BASE_URL}/galeria/splyw9.06.2024/${filename}"
    output_path="public/uploads/splyw_09_06_2024/splyw${i}_09_06_2024.jpg"

    download_image "$url" "$output_path"
done

echo "🏕️ Downloading Biwak 09.2024 gallery (trying various patterns)..."

# Create directory for biwak 09.2024
mkdir -p public/uploads/biwak_09_2024

# Download various biwak 09.2024 images with different naming patterns
biwak_files=(
    "biwak6.09.2024-1.jpg"
    "biwak7.09.2024-1.jpg"
    "biwak7.09.2024-2.jpg"
    "biwak7.09.2024-3.jpg"
    "biwak7.09.2024-4.jpg"
    "biwak7.09.2024-5.jpg"
    "biwak8.09.2024-1.jpg"
    "biwak8.09.2024-2.jpg"
    "biwak8.09.2024-3.jpg"
    "biwak8.09.2024-4.jpg"
)

for filename in "${biwak_files[@]}"; do
    url="${BASE_URL}/galeria/biwak_09_2024/${filename}"
    output_path="public/uploads/biwak_09_2024/${filename}"

    download_image "$url" "$output_path"
done

echo "🔍 Trying to download additional common images..."

# Try to download some common image filenames that might exist
common_images=(
    "hero.jpg"
    "hero-image.jpg"
    "konie.jpg"
    "hipoterapia.jpg"
    "terapia.jpg"
    "kon.jpg"
    "dzieci.jpg"
    "zajecia.jpg"
    "nepal.jpg"
    "tofik.jpg"
)

for img in "${common_images[@]}"; do
    download_with_fallback "$img" "public/uploads/konie/$img"
done

echo "📊 Download summary:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Count downloaded files
total_files=$(find public/uploads -type f | wc -l)
total_size=$(du -sh public/uploads 2>/dev/null | cut -f1)

echo "📁 Total files downloaded: $total_files"
echo "💾 Total size: ${total_size:-"Unable to calculate"}"
echo "📂 Files saved in: public/uploads/"

echo ""
echo "🎯 Next steps:"
echo "1. Check public/uploads/ directory for downloaded images"
echo "2. Run 'npm run build' to verify everything works"
echo "3. Images are now ready to use in galleries and content"

echo ""
echo "✨ Image download completed!"
echo "🐴 Ready to gallop with your new images! 🏇"