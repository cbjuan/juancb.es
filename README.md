# github.com/cbjuan/juancb.es

This repository contains the files to generate a website using [Hugo.io](https://gohugo.io/) and the [Academic theme](https://sourcethemes.com/academic/).

## Running the website in local

Install Hugo

```shell
brew install hugo
```

and from the website folder, run

```shell
hugo server
```

## Updating the website

Make the changes following the templates and different instructions placed as comments in the different files.

### Adding publications automatically

To create automatically publications from bibtex, we use the [Academic's admin tool](https://github.com/sourcethemes/academic-admin).

To [use it](https://sourcethemes.com/academic/docs/managing-content/#create-a-publication), you should install the admin tool using pip: `pip3 install -U academic`. Later, use the command `academic import --bibtex <path_to_your/publications.bib>` to create the publications folder with the new publications to include them under `/content/publication` directory.

## Deploying the website

The automatic deployment using [GitHub Pages](https://pages.github.com/) has been implemented using [these instructions](https://gohugo.io/hosting-and-deployment/hosting-on-github/#github-user-or-organization-pages).

The folder `public` is a Git submodule which is pushed to the repository <https://github.com/cbjuan/cbjuan.github.io.> This folder is populated using the `deploy-web.sh` script. Execute the script using the bash: `./deploy-web.sh`
