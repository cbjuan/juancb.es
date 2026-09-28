+++
title = "AI Methods for Quantum Circuit Optimization"
date = 2025-09-01T10:00:00  # Schedule page publish date.
draft = false

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
time_start = 2025-09-01T10:00:00
time_end = 2025-09-01T14:30:00

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["David Kremer", "Juan Cruz-Benito", "Victor Villar"]

# Abstract and optional shortened version.
abstract = "Full-day tutorial (TUT13) at IEEE Quantum Week 2025 (QCE25), co-presented with David Kremer and Victor Villar (IBM Quantum). Quantum circuit optimization is essential for getting the most out of current quantum hardware, and AI methods have emerged as a practical tool for circuit optimization and transpilation, striking a balance between output quality and computational effort. The first session gives an overview of the AI-powered transpiler passes available in Qiskit, with hands-on exercises applying them to produce optimized circuits and guidelines for using them effectively. The second session goes under the hood, covering the methods behind these passes and walking through training custom models for specific problems, including how to integrate them into Qiskit as transpiler passes. Hands-on material drew on the Qiskit Gym reinforcement-learning environments for quantum circuit synthesis. Aimed at beginner and intermediate users looking to leverage AI models for circuit optimization, as well as advanced practitioners interested in building their own AI-based optimization passes; foundational Python and quantum computing knowledge were assumed, with AI/ML and Qiskit experience helpful but not required."
abstract_short = "Full-day tutorial at IEEE Quantum Week 2025 (QCE25) on using and training AI-powered transpiler passes in Qiskit for quantum circuit optimization, co-presented with David Kremer and Victor Villar."

# Name of event and optional event URL.
event = "IEEE Quantum Week 2025 (QCE25)"
event_url = "https://qce.quantum.ieee.org/2025/"

# Location of event.
location = "Albuquerque Convention Center, Albuquerque, New Mexico, USA"

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
tags = ["AI", "Qiskit", "Quantum Computing", "Transpiler", "Circuit Optimization", "Tutorial"]

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
url_code = "https://github.com/AI4quantum/qiskit-gym"

# Additional links (optional).
#   Icons: https://sourcethemes.com/academic/docs/page-builder/#icons
[[links]]
  icon = "globe"
  icon_pack = "fas"
  name = "IEEE Quantum Week 2025 (QCE25)"
  url = "https://qce.quantum.ieee.org/2025/"

# Does the content use math formatting?
math = false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Smart"
+++

Tutorial materials built on [Qiskit Gym](https://github.com/AI4quantum/qiskit-gym), including the [intro notebook](https://github.com/AI4quantum/qiskit-gym/blob/main/examples/intro.ipynb).
