# juancb.es

Source for [juancb.es](https://juancb.es), the personal and academic website of Juan Cruz-Benito: blog posts, publications, projects and talks.

Built with [Hugo](https://gohugo.io) and [Hugo Blox Builder](https://hugoblox.com), styled with Tailwind CSS, with site search by [Pagefind](https://pagefind.app).

## Requirements

- [Hugo](https://gohugo.io/installation/) **extended**, version `0.161.1` (the version CI uses)
- [Go](https://go.dev/dl/), used by Hugo to fetch the Hugo Blox modules
- [Node.js](https://nodejs.org) and [pnpm](https://pnpm.io) `11.3.0`

## Local development

```sh
pnpm install     # install Tailwind and Pagefind
pnpm run dev     # start a local server at http://localhost:1313
```

Search only works in a full build, because the dev server doesn't generate the Pagefind index. To preview everything, including search:

```sh
hugo --minify --destination /tmp/juancb-preview
pnpm exec pagefind --site /tmp/juancb-preview
python3 -m http.server --directory /tmp/juancb-preview
```

## Project layout

| Path | What's there |
| --- | --- |
| `content/_index.md` | Homepage, built from Hugo Blox blocks |
| `content/blog/`, `publications/`, `projects/`, `events/` | One folder per item, with `index.md` and its images |
| `data/authors/juancb.yaml` | Bio, affiliations, education, experience and awards |
| `config/_default/` | Site configuration (`hugo.yaml`, `params.yaml`, menus, modules) |
| `layouts/` | Local overrides of Hugo Blox templates |
| `assets/css/custom.css` | Custom styles |
| `static/` | Files copied as-is, including `CNAME`, `robots.txt` and `llms.txt` |

## Deployment

Every push to `master` triggers [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml). It builds the site with Hugo and Pagefind and publishes it to [`cbjuan/cbjuan.github.io`](https://github.com/cbjuan/cbjuan.github.io), which serves `juancb.es` through GitHub Pages. The `public/` folder is a submodule pointing at that repository.

`./deploy-web.sh` does the same build and deploy manually, for when CI isn't available.

## License

- **Site content** (text, images and other material under `content/`): © Juan Cruz-Benito, licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
- **Template code**: started from the Academic Kickstart template, © George Cushen, under the [MIT License](LICENSE.md). The Hugo Blox modules are MIT-licensed too.
