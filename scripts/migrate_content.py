#!/usr/bin/env python3
"""One-off Phase 2 migration: convert Academic-theme TOML content bundles to
the Hugo Blox Builder YAML schema confirmed against the `blox` module templates.

- content/post/*        -> content/blog/*        (pure move, no field changes)
- content/project/*      -> content/projects/*     (pure move, no field changes)
- content/talk/*         -> content/events/*       (TOML->YAML + field renames)
- content/publication/*  -> content/publications/* (TOML->YAML + field renames)

One-shot: each source folder is removed once its content has been moved/converted.
Re-running against a checkout where the source folders no longer exist will fail;
use `git checkout content/post content/project content/talk content/publication`
to restore the old layout first if you need to re-run.
"""
import json
import shutil
import tomllib
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

PUB_TYPE_MAP = {
    "1": "paper-conference",
    "2": "article-journal",
    "3": "article",
    "4": "report",
    "5": "book",
    "6": "chapter",
    "7": "thesis",
    "8": "patent",
    # "0" (Uncategorized) has no CSL/i18n equivalent -> field is dropped.
}

TALK_EXCLUDE = {"example"}


def parse_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("+++\n"), f"expected TOML front matter in {path}"
    end = text.index("\n+++", 4)
    toml_src = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    return tomllib.loads(toml_src), body


def clean(value):
    """Recursively drop empty strings/lists/dicts/None. Keep bools/numbers as-is."""
    if isinstance(value, dict):
        cleaned = {k: clean(v) for k, v in value.items()}
        return {k: v for k, v in cleaned.items() if not is_empty(v)}
    if isinstance(value, list):
        return [clean(v) for v in value]
    return value


def is_empty(value) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value == ""
    if isinstance(value, (list, dict)):
        return len(value) == 0
    return False


def yaml_scalar(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, (date, datetime)):
        return v.isoformat()
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    raise TypeError(f"unhandled scalar type: {type(v)!r}")


def emit_yaml(data: dict, indent: int = 0) -> list[str]:
    lines = []
    pad = "  " * indent
    for k, v in data.items():
        if isinstance(v, dict):
            lines.append(f"{pad}{k}:")
            lines.extend(emit_yaml(v, indent + 1))
        elif isinstance(v, list):
            lines.append(f"{pad}{k}:")
            for item in v:
                lines.append(f"{pad}  - {yaml_scalar(item)}")
        else:
            lines.append(f"{pad}{k}: {yaml_scalar(v)}")
    return lines


def write_page(dest_dir: Path, fields: dict, body: str) -> None:
    ordered = clean(fields)
    dest_dir.mkdir(parents=True, exist_ok=True)
    lines = ["---"] + emit_yaml(ordered) + ["---", ""]
    text = "\n".join(lines)
    if body.strip():
        text += body if body.endswith("\n") else body + "\n"
    (dest_dir / "index.md").write_text(text, encoding="utf-8")


def copy_assets(src_dir: Path, dest_dir: Path, skip: set[str] = frozenset()) -> None:
    for item in src_dir.iterdir():
        if item.name in skip or item.name in ("index.md", "cite.md"):
            continue
        dest = dest_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def migrate_plain(src_name: str, dest_name: str) -> None:
    """Pure move: content is already valid YAML matching the new schema."""
    src = CONTENT / src_name
    dest = CONTENT / dest_name
    reset_dir(dest)
    n = 0
    for entry in sorted(src.iterdir()):
        if not entry.is_dir():
            continue
        shutil.move(str(entry), str(dest / entry.name))
        n += 1
    shutil.rmtree(src)
    print(f"{src_name} -> {dest_name}: moved {n} bundles (no field changes)")


def migrate_talks() -> None:
    src = CONTENT / "talk"
    dest = CONTENT / "events"
    reset_dir(dest)
    count = 0
    for entry in sorted(src.iterdir()):
        if not entry.is_dir() or entry.name in TALK_EXCLUDE:
            continue
        fm, _body = parse_front_matter(entry / "index.md")

        fields = {}
        fields["title"] = fm["title"]
        fields["date"] = fm["date"]
        if "draft" in fm:
            fields["draft"] = fm["draft"]
        if fm.get("time_start") is not None:
            fields["event_start"] = fm["time_start"]
        if fm.get("time_end") is not None:
            fields["event_end"] = fm["time_end"]
        fields["authors"] = fm.get("authors", [])
        fields["abstract"] = fm.get("abstract", "")
        if fm.get("abstract_short"):
            fields["summary"] = fm["abstract_short"]
        fields["event_name"] = fm.get("event", "")
        fields["event_url"] = fm.get("event_url", "")
        fields["location"] = fm.get("location", "")
        if "selected" in fm:
            fields["selected"] = fm["selected"]
        fields["projects"] = fm.get("projects", [])
        fields["tags"] = fm.get("tags", [])
        fields["slides"] = fm.get("slides", "")
        fields["url_pdf"] = fm.get("url_pdf", "")
        fields["url_slides"] = fm.get("url_slides", "")
        fields["url_video"] = fm.get("url_video", "")
        fields["url_code"] = fm.get("url_code", "")
        if "math" in fm:
            fields["math"] = fm["math"]
        image = {}
        if fm.get("image"):
            image["caption"] = fm["image"].get("caption", "")
            image["focal_point"] = fm["image"].get("focal_point", "")
        fields["image"] = image

        dest_dir = dest / entry.name
        # Boilerplate HTML-comment instructional body (Academic theme default,
        # invisible when rendered) is not real content -- dropped, not carried over.
        write_page(dest_dir, fields, "")
        copy_assets(entry, dest_dir)
        count += 1
    shutil.rmtree(src)
    print(f"talk -> events: converted {count} bundles (excluded: {sorted(TALK_EXCLUDE)})")


def migrate_publications() -> None:
    src = CONTENT / "publication"
    dest = CONTENT / "publications"
    reset_dir(dest)
    count = 0
    special_case_handled = False
    for entry in sorted(src.iterdir()):
        if not entry.is_dir():
            continue
        fm_path = entry / "index.md"
        is_special = not fm_path.exists()
        if is_special:
            fm_path = entry / "cite.md"
        fm, _body = parse_front_matter(fm_path)

        fields = {}
        fields["title"] = fm["title"]
        fields["date"] = fm["date"]
        if "draft" in fm:
            fields["draft"] = fm["draft"]
        fields["authors"] = fm.get("authors", [])
        fields["abstract"] = fm.get("abstract", "")
        if fm.get("abstract_short"):
            fields["summary"] = fm["abstract_short"]

        pub_types_raw = fm.get("publication_types", [])
        pub_types = [PUB_TYPE_MAP[c] for c in pub_types_raw if c in PUB_TYPE_MAP]
        fields["publication_types"] = pub_types

        if "selected" in fm:
            fields["selected"] = fm["selected"]
        if "featured" in fm:
            fields["featured"] = fm["featured"]
        fields["publication"] = fm.get("publication", "")
        if fm.get("publication_short"):
            fields["publication_short"] = fm["publication_short"]
        fields["tags"] = fm.get("tags", [])
        fields["projects"] = fm.get("projects", [])
        if "math" in fm:
            fields["math"] = fm["math"]

        fields["url_pdf"] = fm.get("url_pdf") or fm.get("pdf_source", "")
        fields["url_preprint"] = fm.get("url_preprint", "")
        fields["url_code"] = fm.get("url_code", "")
        fields["url_source"] = fm.get("url_source") or fm.get("source_url", "")
        fields["url_dataset"] = fm.get("url_dataset", "")
        fields["url_poster"] = fm.get("url_poster", "")
        fields["url_project"] = fm.get("url_project", "")
        fields["url_slides"] = fm.get("url_slides", "")
        fields["url_video"] = fm.get("url_video", "")

        doi = fm.get("doi", "")
        if doi:
            fields["hugoblox"] = {"ids": {"doi": doi}}

        image = {}
        if fm.get("image"):
            image["caption"] = fm["image"].get("caption", "")
            image["focal_point"] = fm["image"].get("focal_point", "")
        fields["image"] = image

        dest_dir = dest / entry.name
        write_page(dest_dir, fields, "")
        skip = {fm_path.name}
        copy_assets(entry, dest_dir, skip=skip)

        if is_special:
            old_bib = next(dest_dir.glob("*.bib"))
            old_bib.rename(dest_dir / "cite.bib")
            special_case_handled = True

        count += 1
    shutil.rmtree(src)
    print(f"publication -> publications: converted {count} bundles")
    assert special_case_handled, "expected to handle the 2015_michavila cite.md special case"


def main() -> None:
    migrate_plain("post", "blog")
    migrate_plain("project", "projects")
    migrate_talks()
    migrate_publications()


if __name__ == "__main__":
    main()
