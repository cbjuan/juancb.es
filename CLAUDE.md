# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static personal/academic website for Juan Cruz-Benito, built with [Hugo](https://gohugo.io) using the `hugo-academic` ("Academic Kickstart") theme. There is no application code, no package manager, and no test suite — this is content (Markdown + TOML front matter) plus Hugo templates.

## Commands

Hugo is not preinstalled in a fresh environment; install it first (`apt-get install -y hugo` gets a working `v0.123.x extended` build, or use `apt-cache policy hugo` to check what's available).

- **Build the site**: `hugo` (outputs to `public/`, which is a *separate git repo*, see below). Use `hugo --minify --destination /tmp/some_dir` to build into a scratch directory instead, so you don't dirty `public/` while testing.
- **Local dev server**: `./view.sh` (runs `hugo server --disableFastRender`)
- **Deploy**: `./deploy-web.sh` — runs `hugo`, then commits and pushes the generated `public/` submodule to its own remote (`cbjuan.github.io`), then commits the submodule pointer bump here. Only run this when actually asked to deploy.
- There is no lint/test command — validate changes by running a real `hugo` build and checking it completes with no errors/warnings, then inspect the generated HTML in the output directory for the specific page(s) you changed (e.g. `grep`/`python -m json.tool` on any JSON-LD you touched).
- After a local test build, clean up `resources/_gen/` if new cache entries were added under it that aren't already tracked by git (`git status` will show them as untracked) — don't leave build cache lying around, and never blindly `rm -rf resources/_gen`: some of it **is** tracked/committed in this repo, so check `git status` before deleting anything under `resources/`.

## Repository structure

- **`public/`** is a **git submodule** pointing at a *different* repo (`cbjuan/cbjuan.github.io`) — that's the actual GitHub Pages deployment target. This repo (`juancb.es`) is the Hugo *source*; editing anything under `public/` directly is almost never what you want.
- **`themes/academic/`** is the `hugo-academic` theme, but it is **vendored directly into this repo as regular tracked files, not a git submodule** (`.gitmodules` only declares `public`). This means theme templates can and should be edited in place here when a fix or feature requires it — there is no upstream sync step. (`update_academic.sh` assumes the theme is still a submodule and runs `git submodule update --remote --merge` for it; that call is a no-op today since the theme isn't a submodule — don't rely on it to actually pull theme updates.)
- **`content/`** — the actual site content, one directory per content type: `authors/` (author profile(s), including the primary/`superuser` bio used site-wide), `post/`, `publication/`, `project/`, `talk/`, `home/` (front-page widgets like `about.md`, `experience.md`, `publications.md` — these compose the homepage), plus standalone `privacy.md`/`terms.md`. Most content types use Hugo "leaf bundles" (a folder with an `index.md`, e.g. `content/publication/2025-foo/index.md`), not flat `.md` files.
- **`config/_default/`** holds the real configuration (`config.toml`, `params.toml`, `languages.toml`, `menus.toml`); the root `config.toml` is just a compatibility stub pointing here.
- Site config: `site_type = "Person"` in `params.toml` — this matters because several theme templates (notably JSON-LD generation) branch on `site_type`.

## Content conventions worth knowing

- Publication front matter is TOML (`+++` delimiters), e.g. `content/publication/<slug>/index.md`, and commonly includes `doi = "10.xxxx/..."` — when present, this automatically flows into that page's JSON-LD (`identifier`/`sameAs` fields). Don't add DOI handling elsewhere; it's already wired.
- The "superuser" author page (`content/authors/juancb/_index.md`, `superuser: true` in front matter) is the source of truth for site-wide Person data (name, role, organizations, education, social links) — it feeds the homepage `Person` JSON-LD and several other partials (`functions/get_author_name.html`, etc.). Update it there, not by hardcoding values in templates.
- `edit_page.repo_url` in `params.toml` points at this repo (`https://github.com/cbjuan/juancb.es`) and is reused by more than just the human-facing "Edit this page" link — e.g. the per-page `<link rel="alternate" type="text/markdown">` tags that point agents/crawlers at the raw Markdown source are built from it too. If this repo is ever renamed/moved, that value needs updating.

## Structured data / agent- and SEO-readiness

This site has had explicit work done to make it legible to search engines and AI agents/crawlers — worth knowing before touching related templates:

- `static/robots.txt` and `static/llms.txt` are hand-maintained static files (not generated). `llms.txt` in particular follows the [llmstxt.org](https://llmstxt.org) convention and is a *curated* summary (bio, key pages, featured projects) — it does not auto-update when new content is added, so it can go stale and needs manual edits when something worth surfacing ships.
- `themes/academic/layouts/partials/jsonld/` contains the JSON-LD templates: `person.html` (site owner, only used when `site_type = "Person"`), `article.html` (posts/publications/projects, includes DOI when present), `event.html` (talks), `business.html` (non-Person site types), wired together in `main.html`.
- `themes/academic/layouts/partials/site_head.html` emits the per-page `<link rel="alternate" type="text/markdown">` tag for `post`/`publication`/`project`/`talk` pages, pointing at the raw GitHub Markdown source — this exists because GitHub Pages is static hosting with no real Accept-header content negotiation, so this is the practical equivalent for agents that want the raw source instead of parsed HTML.
- These three things (Person schema, DOI JSON-LD, Markdown alternate links) are all generated automatically from existing front matter/content at build time — new content gets them for free. `llms.txt` is the one exception requiring manual upkeep.
