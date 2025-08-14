#!/bin/bash
# Linux file search örnek scripti

# 1. Mevcut dizinde .txt dosyalarını bul ve listele
echo "TXT dosyaları:"
find . -type f -name "*.txt"

# 2. .log dosyalarında "error" kelimesini ara
echo "Log dosyalarında error arama:"
find . -type f -name "*.log" | xargs grep -i "error"

# 3. Dosya adında tek haneli sayı olanları bul
echo "Dosya adında tek haneli sayı olanlar:"
find . -regex ".*[0-9]\.txt"

# 4. Her adımı açıklama ile göster
echo "Arama tamamlandı."
