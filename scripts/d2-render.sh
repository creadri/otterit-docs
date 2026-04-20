#!/bin/bash
# Step 1: render d2 → svg
find . -type f -name "*.d2" -exec d2 --theme 3 {} \;

# Step 2: convert svg → png via Inkscape
find . -type f -name "*.svg" | while read -r f; do
  inkscape --export-type=png --export-dpi=192 "$f"
done
