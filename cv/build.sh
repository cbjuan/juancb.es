#!/usr/bin/env bash
# Build the CV with XeLaTeX.
#   ./build.sh           public build -> ../static/uploads/juan-cruz-benito-cv.pdf
#   ./build.sh private   private build (needs contact.tex) -> ./cv-private.pdf, never published
#
# Requires: xelatex (TeX Live, with the Carlito font) and python3 with fonttools + brotli
# (pip install fonttools brotli), used to cut static Montserrat weights from the site's
# variable font so the CV and the website share a single font file.
set -euo pipefail
cd "$(dirname "$0")"

mode="${1:-public}"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
cp cv.tex "$tmp/"

python3 - "$tmp/fonts" <<'PY'
import sys, os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
src = os.path.join("..", "assets", "dist", "font", "Montserrat.var.woff2")
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for style, weight in [("Medium", 500), ("Bold", 700)]:
    font = TTFont(src)
    font.flavor = None
    font = instancer.instantiateVariableFont(font, {"wght": weight}, updateFontNames=True)
    font.save(os.path.join(out, f"Montserrat-{style}.ttf"))
PY

if [[ "$mode" == "private" ]]; then
  [[ -f contact.tex ]] || { echo "contact.tex not found (see contact.tex.example)"; exit 1; }
  cp contact.tex "$tmp/"
  out="cv-private.pdf"
else
  out="../static/uploads/juan-cruz-benito-cv.pdf"
fi

(cd "$tmp" && xelatex -interaction=nonstopmode -halt-on-error cv.tex >/dev/null && xelatex -interaction=nonstopmode -halt-on-error cv.tex >/dev/null) \
  || { echo "xelatex failed; see the log by running it manually in cv/" >&2; exit 1; }
mkdir -p "$(dirname "$out")"
cp "$tmp/cv.pdf" "$out"

if [[ "$mode" != "private" ]] && command -v pdftotext >/dev/null; then
  if pdftotext "$out" - | grep -Eq '@[a-z0-9.-]+\.[a-z]{2,}|\+34 ?[0-9]'; then
    echo "Refusing to publish: email or phone number found in the public PDF" >&2
    rm -f "$out"; exit 1
  fi
fi
echo "Built $out"
