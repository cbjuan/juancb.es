---
title: "Quantum Error Correction Meets AI for Science: Lessons from LLM-Guided Code Discovery"
date: 2026-09-17T15:15:00
draft: false
event_start: 2026-09-17T15:15:00
event_end: 2026-09-17T16:00:00
abstract: "Invited keynote at the AI for Circuit Synthesis, Optimization, and Discovery (AI4QC) workshop, held alongside IEEE Quantum Week 2026 in Toronto. The talk places LLM-guided program evolution within the broader 'AI for science' landscape (AlphaFold, GNoME, FunSearch, AlphaEvolve) and walks through a verifier-guided evolutionary pipeline, built on OpenEvolve, that mutates Python programs generating bivariate-bicycle and perturbed bivariate-bicycle quantum LDPC codes. Screening roughly 2×10^5 candidates across five campaigns surfaced 465 BLISS-distinct codes (97 CSS, 368 non-CSS) at block length n ≤ 360, backed by an independent verification stack — GF(2) rank computation, MILP-based distance bounds, BLISS Tanner-graph deduplication, and local-Clifford equivalence checks — built to expose and correct the search's own blind spots. The talk closes with transferable lessons on where LLM-guided evolution complements, rather than replaces, reinforcement-learning approaches to quantum error-correcting code discovery."
summary: "Keynote on using LLM-guided evolutionary program search (built on OpenEvolve) to discover 465 new bivariate-bicycle quantum LDPC codes, and what that stress test teaches about applying 'AI for science' methods to quantum error correction."
event_name: "AI for Circuit Synthesis, Optimization, and Discovery Workshop (AI4QC) — IEEE Quantum Week 2026 (QCE26)"
event_url: "https://sites.google.com/view/qce-workshop-ai4qc/"
location: "Metro Toronto Convention Centre, Toronto, Ontario, Canada"
selected: false
tags:
  - "AI"
  - "Quantum Computing"
  - "Quantum Error Correction"
  - "Quantum LDPC Codes"
  - "Large Language Models"
links:
- type: code
  url: "https://github.com/qiskit-community/qcode-discovery"
math: false
image:
  caption: "Image credit: [**AILAB-Udine**](https://www.linkedin.com/posts/ieeequantumweek-qce2026-quantumcomputing-ugcPost-7510625105777950720-dfFU/)"
  focal_point: "Smart"
---

Related paper: [Evolutionary Discovery of Bivariate Bicycle Codes with LLM-Guided Search](https://arxiv.org/abs/2606.02418) (arXiv:2606.02418).
