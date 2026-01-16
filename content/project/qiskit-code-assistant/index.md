---
title: Qiskit Code Assistant
summary: Family of open-source LLMs (8B–24B) for quantum code generation, plus the Qiskit HumanEval* benchmarks
tags:
- AI
- Quantum Computing
- LLMs
- Open Source
date: "2025-04-01T00:00:00Z"

external_link: ""

image:
  caption: ""
  focal_point: Smart

links:
- icon: blog
  icon_pack: fas
  name: Blog
  url: https://www.ibm.com/quantum/blog/qiskit-code-assistant
- icon: robot
  icon_pack: fas
  name: Models
  url: https://huggingface.co/collections/Qiskit/qiskit-llms-67337b513e8718191b0a6ff6
- icon: database
  icon_pack: fas
  name: HumanEval
  url: https://huggingface.co/datasets/Qiskit/qiskit_humaneval
- icon: database
  icon_pack: fas
  name: HumanEval Hard
  url: https://huggingface.co/datasets/Qiskit/qiskit_humaneval_hard

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
---

A family of LLMs (8B–24B parameters) specialized for quantum code generation. Models built on IBM Granite, Mistral, and Qwen foundations, fine-tuned on curated Qiskit datasets including Python scripts, Jupyter notebooks, and synthetic Q&A pairs.

**Open-source model family:**
- **Mistral Small 24B** — Largest model, highest accuracy
- **Qwen2.5 Coder 14B** — Strong coding foundation
- **Granite 3.x 8B** — Efficient, multiple versions
- GGUF quantized versions available for local deployment

Achieves **46.53% on Qiskit HumanEval**—significantly outperforming competing models (24.75%–39.6%). Supports natural language to code ("define a Bell circuit and run it on ibm_brisbane") and intelligent autocomplete.

We created and open-sourced **Qiskit HumanEval** and **Qiskit HumanEval Hard**—benchmarks with 150+ tasks each, now used industry-wide for evaluating quantum code LLMs. Integrated into VS Code and JupyterLab.
