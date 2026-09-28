#!/usr/bin/env python3
"""
Migrate deprecated flat link front-matter fields (url_pdf, url_source, url_video,
url_code, url_preprint, external_link) into the new `links: [{type, url}]` array
schema expected by Hugo Blox Builder's build_links.html.

Scoped to content/publications, content/events, content/media - the directories
flagged by the build's deprecation warnings. Text-based (not a full YAML
round-trip) so untouched front-matter lines keep their exact original formatting.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_DIRS = ["content/publications", "content/events", "content/media"]

# Order mirrors the legacy field dict in the blox module's build_links.html.
LEGACY_ORDER = [
    "url_pdf",
    "url_preprint",
    "url_code",
    "url_dataset",
    "url_poster",
    "url_project",
    "url_slides",
    "url_source",
    "url_video",
    "external_link",
]
TYPE_MAP = {
    "url_pdf": "pdf",
    "url_preprint": "preprint",
    "url_code": "code",
    "url_dataset": "dataset",
    "url_poster": "poster",
    "url_project": "project",
    "url_slides": "slides",
    "url_source": "source",
    "url_video": "video",
    "external_link": "site",
}

FIELD_RE = re.compile(r'^(' + "|".join(LEGACY_ORDER) + r'):\s*"(.*)"\s*$')


def migrate_file(path: Path) -> bool:
    lines = path.read_text().splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return False
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return False

    found = {}  # key -> url value
    kept_lines = []
    insert_at = None
    for i in range(1, end):
        m = FIELD_RE.match(lines[i])
        if m:
            key, url = m.group(1), m.group(2)
            if url:  # skip empty legacy fields; they don't warn or need migrating
                found[key] = url
                if insert_at is None:
                    insert_at = len(kept_lines)
            continue
        kept_lines.append(lines[i])

    if not found:
        return False

    links_block = ["links:\n"]
    for key in LEGACY_ORDER:
        if key in found:
            links_block.append(f'- type: {TYPE_MAP[key]}\n')
            links_block.append(f'  url: "{found[key]}"\n')

    new_front_matter = kept_lines[:insert_at] + links_block + kept_lines[insert_at:]
    new_lines = [lines[0]] + new_front_matter + lines[end:]
    path.write_text("".join(new_lines))
    return True


def main():
    changed = []
    for d in TARGET_DIRS:
        for path in sorted((ROOT / d).glob("*/index.md")):
            if migrate_file(path):
                changed.append(path.relative_to(ROOT))
    print(f"Migrated {len(changed)} files")
    for p in changed:
        print(f"  {p}")


if __name__ == "__main__":
    main()
