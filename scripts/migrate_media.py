#!/usr/bin/env python3
"""One-off: normalize content/media/* (press mentions) to the trimmed Hugo
Blox Builder schema. Unlike the other content types, these bundles already
use YAML front matter (Academic theme's "project" widget, used generically
for press items) -- this just strips theme boilerplate comments and drops
fields that are empty for every item except one.

Kept fields: title, date, authors, summary, tags, categories, external_link.
image{caption,focal_point,preview_only} is kept only for the one bundle
(2020-la-razon) that has a real featured.jpg asset -- for the other two
bundles that carry the same placeholder image block but no actual image
file, the block is dropped (nothing to render).

In place: rewrites content/media/*/index.md, does not move/rename anything.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEDIA = ROOT / "content" / "media"

FIELD_RE = re.compile(r'^([a-z_]+):\s*(.*)$')

HAS_REAL_IMAGE = {"2020-la-razon"}


def strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def parse_front_matter(text: str) -> dict:
    assert text.startswith("---\n")
    end = text.index("\n---", 4)
    body = text[4:end]

    fields: dict = {}
    in_image = False
    for line in body.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("image:"):
            in_image = True
            fields["image"] = {}
            continue
        m = FIELD_RE.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        if in_image and key in ("caption", "focal_point", "preview_only"):
            fields["image"][key] = val
            continue
        in_image = False
        fields[key] = val
    return fields


def yaml_str(v: str) -> str:
    return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_page(dest: Path, fm: dict, slug: str) -> None:
    lines = ["---"]
    lines.append(f"title: {yaml_str(strip_quotes(fm['title']))}")
    lines.append(f"date: {strip_quotes(fm['date'])}")
    lines.append("authors: []")
    lines.append(f"summary: {yaml_str(strip_quotes(fm['summary']))}")
    lines.append('tags: ["media"]')
    categories = strip_quotes(fm.get("categories", "[]").strip("[]"))
    lines.append(f"categories: [{categories}]")
    lines.append(f"external_link: {yaml_str(strip_quotes(fm['external_link']))}")
    if slug in HAS_REAL_IMAGE:
        image = fm.get("image", {})
        lines.append("image:")
        lines.append(f"  caption: {yaml_str(strip_quotes(image.get('caption', '')))}")
        lines.append(f"  focal_point: {yaml_str(strip_quotes(image.get('focal_point', 'Center')))}")
        lines.append(f"  preview_only: {strip_quotes(image.get('preview_only', 'false'))}")
    lines.append("---")
    lines.append("")
    dest.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    count = 0
    for entry in sorted(MEDIA.iterdir()):
        if not entry.is_dir():
            continue
        index = entry / "index.md"
        fm = parse_front_matter(index.read_text(encoding="utf-8"))
        write_page(index, fm, entry.name)
        count += 1
    print(f"media: normalized {count} bundles in place")


if __name__ == "__main__":
    main()
