---
title: LLM-Guided Quantum Code Discovery
summary: Evolutionary program search guided by LLMs to discover quantum LDPC codes — 465 distinct bivariate-bicycle codes from ~200K candidates
tags:
- AI for Science
- Quantum Error Correction
- LLMs
- Open Source
date: "2026-06-01T00:00:00Z"

external_link: ""

image:
  caption: ""
  focal_point: Smart

links:
- icon: brands/github
  label: GitHub
  url: https://github.com/qiskit-community/qcode-discovery
- icon: hero/document-text
  label: Paper
  url: https://arxiv.org/abs/2606.02418
- icon: hero/document-text
  label: Weight-five paper
  url: https://arxiv.org/abs/2610.06623
- icon: hero/presentation-chart-bar
  label: Keynote
  url: /events/2026_ieee_qce_ai4qc/

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
---

An "AI for science" workflow that uses large language models to evolve Python programs generating quantum LDPC code designs: bivariate-bicycle (BB) and perturbed bivariate-bicycle (PBB) codes. Built on OpenEvolve with an ensemble of LLMs, and paired with an independent verification stack so every reported code is certified rather than just proposed.

**Results:**
- **465 distinct codes** (97 CSS, 368 non-CSS) at block length n ≤ 360, from ~200K candidates screened across five campaigns — about 140 hours and ~US$400 in LLM inference
- Notable finds include an indecomposable [[288,16,12]] code, higher-rate codes reaching k = 50 at d = 8, and non-CSS codes matching the gross-code benchmark at [[144,12,12]]
- Follow-up on **weight-five codes**: a 1,142-entry catalogue with exact distance certificates, structural analysis, and random-search controls

**Verification pipeline:** GF(2) rank computation, MILP-based distance bounds, BLISS Tanner-graph deduplication, decomposability analysis, and local-Clifford equivalence checks — designed to catch the search's own blind spots.

Presented as an invited keynote at the AI4QC workshop, IEEE Quantum Week 2026. Code, catalogues, and paper sources are open under Apache 2.0.
