# AGENTS.md

This file provides guidance to AI coding agents (including Claude Code, claude.ai/code) when working with code in this repository.

## What this is

A static personal/academic website for Juan Cruz-Benito, built with [Hugo](https://gohugo.io) and [Hugo Blox Builder](https://hugoblox.com) (the successor to the old `hugo-academic` theme, which this site used until 2026). The theme is pulled in as **Hugo Modules** (`github.com/HugoBlox/kit/modules/{blox,slides}`, see `go.mod`), not vendored. Styling is Tailwind v4 and site search is [Pagefind](https://pagefind.app), both installed via pnpm. There is no application code and no test suite: this is content (Markdown + YAML front matter), config, and a few Hugo template overrides.

## Commands

Required tooling: Hugo **extended** `0.161.1` (pinned in `hugoblox.yaml` and CI), Go (needed to resolve Hugo Modules), Node + pnpm `11.3.0` (pinned via `packageManager` in `package.json`).

- **Install JS deps**: `pnpm install` (the `postinstall` script, `scripts/fix-tailwindcss-bin.mjs`, fixes up the Tailwind CLI binary). pnpm 11 fails the install with `ERR_PNPM_IGNORED_BUILDS` unless every dependency with a build script has an explicit `true`/`false` under `allowBuilds` in `pnpm-workspace.yaml`. If a new dependency adds one, set it there. Never leave pnpm's `set this to true or false` placeholder: that broke the first deploy.
- **Local dev server**: `pnpm run dev` or `./view.sh` (both run `hugo server --disableFastRender`). Search doesn't work in the dev server because the Pagefind index is only built by `pnpm run pagefind`.
- **Test build**: `hugo --minify --destination /tmp/some_dir` builds into a scratch directory without touching `public/` (see below). It must finish with no errors or warnings.
- **Deploy is automatic**: `.github/workflows/deploy.yml` runs on every push to `master`. It sets up Go, pnpm and Node, runs `pnpm install --frozen-lockfile`, installs Hugo, runs `hugo --gc --minify` and then `pnpm run pagefind`, and pushes `public/` to `cbjuan/cbjuan.github.io` (`master` branch). Merging to `master` is the deploy, so don't deploy manually for a normal PR.
  - The deploy step authenticates with an SSH deploy key stored as the `PAGES_DEPLOY_KEY` secret in this repo, paired with a write-access deploy key on `cbjuan/cbjuan.github.io`. If a run fails with `Permission ... denied to deploy key`, that pairing is broken. Fix it in the settings of both repos; a code change here can't fix it.
  - The deploy mirrors `public/` onto the target branch, replacing the whole branch rather than syncing incrementally. Anything that exists only in `cbjuan.github.io` and isn't produced from this repo gets deleted on the next deploy. `static/CNAME` exists so the custom domain survives this.
  - `./deploy-web.sh` is a manual fallback. It runs the same build as CI, then commits and pushes the `public/` submodule directly. Only use it if explicitly asked to deploy outside CI. CI force-pushes `cbjuan.github.io`, so the local `public/` checkout must first be synced to `origin/master` or the push will be rejected.
- There is no lint or test command. CI runs a real build and fails loudly if a template breaks, so validate locally the same way before pushing:
  - Run a scratch `hugo` build and check it finishes with no errors or warnings.
  - Inspect the generated HTML for the specific pages you changed, e.g. `grep`, or `python -m json.tool` on any JSON-LD you touched.
  - For visual changes, take a screenshot of the built output. Serve the scratch dir with `python3 -m http.server`, then capture it with headless Chrome.
- `resources/` (Hugo's build cache, including processed images) is git-ignored and never committed, so it's safe to delete.

## Repository structure

- **`public/`** is a **git submodule** pointing at a *different* repo (`cbjuan/cbjuan.github.io`), the GitHub Pages deployment target. This repo (`juancb.es`) is the Hugo *source*. CI builds and publishes `public/` on its own, so the local checkout of the submodule is usually stale or dirty. Don't edit, commit or clean it unless explicitly asked.
- **`config/_default/`** holds all configuration as YAML:
  - `hugo.yaml`: Hugo core settings, cascades, permalinks and taxonomies.
  - `params.yaml`: the `hugoblox:` settings (identity, theme, header/footer, analytics, repository, …).
  - `module.yaml`: module imports and mounts.
  - `menus.yaml` and `languages.yaml`.
- **`content/`** is the site content, one folder per section, mostly as leaf bundles (`<section>/<slug>/index.md` plus a `featured.*` image and other assets):
  - `blog/`
  - `publications/`
  - `projects/`
  - `events/` (talks)
  - `authors/`: `_index.md` only, render disabled. Author *data* lives in `data/authors/`.
  - `privacy.md` and `terms.md`
  - `_index.md`: the homepage.
- **The homepage** (`content/_index.md`) is a list of Hugo Blox `sections:` blocks, not separate widget files:
  - `resume-biography-3`
  - four `content-collection` blocks (projects, posts, publications, talks)
  - `resume-experience`
  - `resume-awards`
  - `contact-info`

  Each block has its own `content:` and `design:` options (view, columns, `show_date`, …).
- **`data/authors/juancb.yaml`** (schema `hugoblox/author/v1`, `is_owner: true`) is the single source of truth for site-wide Person data: name, role, affiliations, links, education, experience and awards. It feeds the biography, experience and awards blocks and the Person JSON-LD. Update it there, not by hardcoding values in templates.
- **`layouts/`** holds project-level **overrides** of module templates. A file here at the same path as one in the blox module replaces it. To override something:
  1. Copy the upstream file from the module cache (`hugo config mounts` shows where it is, typically `~/go/pkg/mod/github.com/!hugo!blox/kit/modules/blox@<version>/layouts/…`).
  2. Edit the copy.
  3. Start the copy with a comment explaining why it differs from upstream, as the existing overrides do.

  Keep overrides minimal: every override is a file that won't pick up upstream fixes when the module is updated.
- `assets/css/custom.css` holds site CSS on top of the Tailwind theme, including the homepage type scale.
- `i18n/en.yaml` overrides specific UI strings from the module.
- `scripts/migrate_*.py` are one-shot scripts from the Academic → Hugo Blox content migration. They're kept for reference and aren't part of the build.
- The files in `data/` besides `authors/` (`fonts/`, `themes/`, `page_sharer.toml`) are read by the module for font packs, theme packs and share buttons. They aren't leftovers.

## Hugo Blox gotcha: `false | default true`

In Hugo, `false | default true` evaluates to `true`, because `default` treats `false` as "unset". Several upstream templates read boolean options as `.Params.show_x | default true`, so setting `show_date: false`, `show_read_time: false` etc. silently does nothing. When a `false` option is ignored, this is almost always why. The fix is an override that uses `ne .Params.show_x false` or `isset` instead. `layouts/single.html`, `layouts/list.html` and `layouts/_partials/views/card.html` exist for exactly this reason.

## Analytics and cookie consent

Hugo Blox has no consent feature (`privacy.enable` in `params.yaml` is read by nothing), so GA4 is gated locally to comply with GDPR/LSSI:

- `layouts/_partials/blox-analytics/services/google_analytics.html` overrides the analytics module so gtag.js is only injected after consent. It exposes `window.hbxConsent` (`status`/`grant`/`deny`), stores the choice in `localStorage` under `cookie-consent` for 12 months, and treats Global Privacy Control as a rejection.
- `layouts/_partials/hooks/body-end/cookie-consent.html` is the banner (styles in `assets/css/custom.css`). Any link to `#cookie-settings`, such as the footer menu entry, reopens it.
- Both render whenever a measurement ID is set, so the banner works under `hugo server`, but gtag.js is only loaded in production builds. If you add another tracker or third-party embed, gate it the same way and update `content/privacy.md`.

## Content conventions worth knowing

- Front matter is YAML (`---` delimiters).
- Publications store their DOI under `hugoblox: ids: doi:`. When present, it flows into that page's JSON-LD (`identifier`/`sameAs`) automatically, so don't add DOI handling elsewhere. Publication types are CSL-style strings (e.g. `paper-conference`, `article-journal`).
- Page links (`links:` in front matter) take an `icon` as `pack/name`, e.g. `brands/github` or `hero/book-open`. There's no separate `icon_pack` field. `emoji/<name>` is also accepted (e.g. `emoji/hugs` for 🤗, used for Hugging Face links).
- Per-section defaults are set with `cascade:` in `config/_default/hugo.yaml` (e.g. projects and events hide reading time), rather than repeated in every file's front matter.
- **Old URLs**: the Academic site used `/post/`, `/publication/`, `/project/` and `/talk/`. The current sections are `blog`, `publications`, `projects` and `events`.
  - Items that existed on the old site carry an `aliases:` entry with their old path, so the old URL redirects.
  - The section roots redirect via static pages in `static/{post,publication,project,talk}/index.html`.
  - New content needs no alias.
  - If you rename or move an existing item, add its previous URL to `aliases` so links don't break.
- `baseURL` in `config/_default/hugo.yaml` is `https://juancb.es/`, matching `static/CNAME`. Every absolute URL (canonical links, sitemap, OG tags, JSON-LD) is built from it.

## Structured data / agent- and SEO-readiness

The site has had explicit work done to make it legible to search engines and AI agents/crawlers. Know this before touching related templates:

- `static/robots.txt` and `static/llms.txt` are hand-maintained static files, not generated. `enableRobotsTXT: false` in `hugo.yaml` is deliberate: turning it on would replace our `robots.txt` (with its explicit AI-crawler allowlist) with the module's generic one. `llms.txt` follows the [llmstxt.org](https://llmstxt.org) convention and is a *curated* summary (bio, key pages, featured projects). It doesn't update when new content is added, so it needs manual edits when something worth surfacing ships.
- JSON-LD is produced by the blox module's `jsonld/main.html` (article, event, breadcrumbs, website, etc.), plus two local additions:
  - `layouts/_partials/hooks/head-end/person-jsonld.html`: the site owner's `Person` schema on the homepage. The module has no Person schema, so this fills the gap when `identity.type` is `person`.
  - `layouts/_partials/jsonld/article.html`: overrides the module's version to add DOI `identifier`/`sameAs` and full multi-author support for publications.
- `layouts/_partials/hooks/head-end/markdown-alternate.html` emits `<link rel="alternate" type="text/markdown">` on blog/publication/project/event pages. It points at the raw Markdown source on GitHub, built from `hugoblox.repository.url`, `branch` and `content_dir` in `params.yaml`. GitHub Pages is static hosting with no real Accept-header content negotiation, so this is the practical equivalent for agents that want the raw source. If this repo is renamed or moved, update `repository.url`.
- Files under `layouts/_partials/hooks/<hook-name>/` are picked up automatically by the module's `get_hook` calls (e.g. `head-end`, rendered at the end of `<head>`). Prefer a hook over overriding `site_head.html` when you only need to add markup.
- All of the above is generated at build time from existing front matter and author data, so new content gets it for free. `llms.txt` is the one exception that needs manual upkeep.
