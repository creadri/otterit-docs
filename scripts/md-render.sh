#!/bin/bash
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
THEMES_DIR="$SCRIPT_DIR/../static/themes"

find . -type f -name "*.md" | while read -r f; do
  dir=$(dirname "$f")
  base=$(basename "$f" .md)
  out="$dir/$base.pdf"

  if grep -q "^marp: true" "$f"; then
    marp "$f" --pdf --allow-local-files --theme-set "$THEMES_DIR" -o "$out"
  else
    (cd "$dir" && pandoc "$base.md" -o "$base.pdf" --pdf-engine=pdflatex -V geometry:margin=1in)
    (cd "$dir" && pandoc "$base.md" -o "$base.epub")
  fi
done
