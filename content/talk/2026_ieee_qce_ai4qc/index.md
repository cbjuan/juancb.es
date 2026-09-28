+++
title = "Quantum Error Correction Meets AI for Science: Lessons from LLM-Guided Code Discovery"
date = 2026-09-17T15:15:00  # Schedule page publish date.
draft = false

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
time_start = 2026-09-17T15:15:00
time_end = 2026-09-17T16:00:00

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = []

# Abstract and optional shortened version.
abstract = "Invited keynote at the AI for Circuit Synthesis, Optimization, and Discovery (AI4QC) workshop, held alongside IEEE Quantum Week 2026 in Toronto. The talk places LLM-guided program evolution within the broader 'AI for science' landscape (AlphaFold, GNoME, FunSearch, AlphaEvolve) and walks through a verifier-guided evolutionary pipeline, built on OpenEvolve, that mutates Python programs generating bivariate-bicycle and perturbed bivariate-bicycle quantum LDPC codes. Screening roughly 2×10^5 candidates across five campaigns surfaced 465 BLISS-distinct codes (97 CSS, 368 non-CSS) at block length n ≤ 360, backed by an independent verification stack — GF(2) rank computation, MILP-based distance bounds, BLISS Tanner-graph deduplication, and local-Clifford equivalence checks — built to expose and correct the search's own blind spots. The talk closes with transferable lessons on where LLM-guided evolution complements, rather than replaces, reinforcement-learning approaches to quantum error-correcting code discovery."
abstract_short = "Keynote on using LLM-guided evolutionary program search (built on OpenEvolve) to discover 465 new bivariate-bicycle quantum LDPC codes, and what that stress test teaches about applying 'AI for science' methods to quantum error correction."

# Name of event and optional event URL.
event = "AI for Circuit Synthesis, Optimization, and Discovery Workshop (AI4QC) — IEEE Quantum Week 2026 (QCE26)"
event_url = "https://sites.google.com/view/qce-workshop-ai4qc/"

# Location of event.
location = "Metro Toronto Convention Centre, Toronto, Ontario, Canada"

# Is this a selected talk? (true/false)
selected = false

# Projects (optional).
#   Associate this talk with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["deep-learning"]` references
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects = []

# Tags (optional).
#   Set `tags = []` for no tags, or use the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["AI", "Quantum Computing", "Quantum Error Correction", "Quantum LDPC Codes", "Large Language Models"]

# Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides = ""

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = ""
url_code = "https://github.com/qiskit-community/qcode-discovery"

# Additional links (optional).
#   Icons: https://sourcethemes.com/academic/docs/page-builder/#icons
[[links]]
  icon = "globe"
  icon_pack = "fas"
  name = "IEEE Quantum Week 2026 (QCE26)"
  url = "https://qce.quantum.ieee.org/2026"

# Does the content use math formatting?
math = false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
[image]
  # Caption (optional)
  caption = "Image credit: [**IEEE Quantum Week 2026**](https://qce.quantum.ieee.org/2026)"

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Smart"
+++

Related paper: [Evolutionary Discovery of Bivariate Bicycle Codes with LLM-Guided Search](https://arxiv.org/abs/2606.02418) (arXiv:2606.02418).
