#!/usr/bin/env bash
# Build the CV with pdflatex.
#   ./build.sh           public build -> ../static/uploads/juan-cruz-benito-cv.pdf
#   ./build.sh private   private build (needs contact.tex) -> ./cv-private.pdf, never published
set -euo pipefail
cd "$(dirname "$0")"

mode="${1:-public}"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
cp cv.tex "$tmp/"

if [[ "$mode" == "private" ]]; then
  [[ -f contact.tex ]] || { echo "contact.tex not found (see contact.tex.example)"; exit 1; }
  cp contact.tex "$tmp/"
  out="cv-private.pdf"
else
  out="../static/uploads/juan-cruz-benito-cv.pdf"
fi

(cd "$tmp" && pdflatex -interaction=nonstopmode -halt-on-error cv.tex >/dev/null && pdflatex -interaction=nonstopmode -halt-on-error cv.tex >/dev/null)
mkdir -p "$(dirname "$out")"
cp "$tmp/cv.pdf" "$out"

if [[ "$mode" != "private" ]] && command -v pdftotext >/dev/null; then
  if pdftotext "$out" - | grep -Eq '@[a-z0-9.-]+\.[a-z]{2,}|\+34 ?[0-9]'; then
    echo "Refusing to publish: email or phone number found in the public PDF" >&2
    rm -f "$out"; exit 1
  fi
fi
echo "Built $out"
