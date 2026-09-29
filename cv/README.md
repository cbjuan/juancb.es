# CV

LaTeX source of my CV. The layout is adapted from the
[NIT Warangal Resume](https://www.overleaf.com/latex/templates/nit-warangal-resume/gtsrbjvffcjn)
Overleaf template (CC BY 4.0).

- `cv.tex`: the CV source.
- `build.sh`: compiles it with `pdflatex`.
  - `./build.sh` builds the **public** PDF into `static/uploads/juan-cruz-benito-cv.pdf`, which the site serves at `/uploads/juan-cruz-benito-cv.pdf` and links from the "Download CV" button on the homepage. It refuses to publish if the PDF contains an email address or phone number.
  - `./build.sh private` builds a version with direct contact details into `cv/cv-private.pdf`. It needs a `contact.tex` file (copy `contact.tex.example`). Both `contact.tex` and `cv-private.pdf` are git-ignored, so they never reach the repo or the site.

The public PDF is committed rather than built in CI, so the site build doesn't need a TeX installation. After editing `cv.tex`, run `./build.sh` and commit both files.
