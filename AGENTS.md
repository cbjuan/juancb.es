# AGENTS.md

This file provides guidance to AI coding agents (including Claude Code, claude.ai/code) when working with code in this repository.

## What this is

A static personal/academic website for Juan Cruz-Benito, built with [Hugo](https://gohugo.io) using the `hugo-academic` ("Academic Kickstart") theme. There is no application code, no package manager, and no test suite — this is content (Markdown + TOML front matter) plus Hugo templates.

## Commands

Hugo is not preinstalled in a fresh environment; install it first (`apt-get install -y hugo` gets a working `v0.123.x extended` build, or use `apt-cache policy hugo` to check what's available).

- **Build the site**: `hugo` (outputs to `public/`, which is a *separate git repo*, see below). Use `hugo --minify --destination /tmp/some_dir` to build into a scratch directory instead, so you don't dirty `public/` while testing.
- **Local dev server**: `./view.sh` (runs `hugo server --disableFastRender`)
- **Deploy is automatic**: `.github/workflows/deploy.yml` builds with Hugo (`hugo --gc --minify`) and pushes `public/` to `cbjuan/cbjuan.github.io` (`master` branch) on every push to this repo's `master`. Don't try to "deploy" as a manual step for a normal PR — merging to `master` is the deploy trigger. `./deploy-web.sh` (runs `hugo`, then commits/pushes the `public/` submodule directly) still works as a manual/local fallback, but is no longer the primary path — only reach for it if explicitly asked to deploy outside of CI.
- There is no lint/test command, but CI *does* run a real `hugo --gc --minify` build on every push to `master` and will fail loudly if a template breaks — validate changes the same way locally before pushing: run a real `hugo` build and check it completes with no errors/warnings, then inspect the generated HTML in the output directory for the specific page(s) you changed (e.g. `grep`/`python -m json.tool` on any JSON-LD you touched).
- After a local test build, clean up `resources/_gen/` if new cache entries were added under it that aren't already tracked by git (`git status` will show them as untracked) — don't leave build cache lying around, and never blindly `rm -rf resources/_gen`: some of it **is** tracked/committed in this repo, so check `git status` before deleting anything under `resources/`.

## Repository structure

- **`public/`** is a **git submodule** pointing at a *different* repo (`cbjuan/cbjuan.github.io`) — that's the actual GitHub Pages deployment target. This repo (`juancb.es`) is the Hugo *source*; editing anything under `public/` directly is almost never what you want.
- **`themes/academic/`** is the `hugo-academic` theme, but it is **vendored directly into this repo as regular tracked files, not a git submodule** (`.gitmodules` only declares `public`). This means theme templates can and should be edited in place here when a fix or feature requires it — there is no upstream sync step. (`update_academic.sh` assumes the theme is still a submodule and runs `git submodule update --remote --merge` for it; that call is a no-op today since the theme isn't a submodule — don't rely on it to actually pull theme updates.)
- **`content/`** — the actual site content, one directory per content type: `authors/` (author profile(s), including the primary/`superuser` bio used site-wide), `post/`, `publication/`, `project/`, `talk/`, `home/` (front-page widgets like `about.md`, `experience.md`, `publications.md` — these compose the homepage), plus standalone `privacy.md`/`terms.md`. Most content types use Hugo "leaf bundles" (a folder with an `index.md`, e.g. `content/publication/2025-foo/index.md`), not flat `.md` files.
- **`config/_default/`** holds the real configuration (`config.toml`, `params.toml`, `languages.toml`, `menus.toml`); the root `config.toml` is just a compatibility stub pointing here.
- Site config: `site_type = "Person"` in `params.toml` — this matters because several theme templates (notably JSON-LD generation) branch on `site_type`.
- `static/CNAME` sets the deployed site's custom domain (`juancb.es`), but `baseurl` in `config/_default/config.toml` is still `https://cbjuan.github.io/` — they don't currently agree. Every absolute URL Hugo generates (canonical links, sitemap, OG tags, and the `robots.txt`/`llms.txt`/JSON-LD described below) is built from `baseurl`, so it's currently `cbjuan.github.io`-rooted even though the site serves at `juancb.es`. Don't "fix" this unprompted — it may be an intentional in-progress migration — but flag it if working on anything URL-related.

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
