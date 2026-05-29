---
title: "Qiskit QuantumKatas: A Benchmark for Evaluating LLMs on Quantum Code"
subtitle: ""
summary: "We adapted Microsoft's QuantumKatas from Q# to Qiskit and turned them into a 350-task benchmark for evaluating how well LLMs write quantum code. We ran 16 models across 7 prompting setups — 39,200 runs — and the results say a lot about where these models are strong and where they still fall short."
authors:
  - juancb
tags:
  - Quantum Computing
  - Artificial Intelligence
  - Open Source
categories:
  - Quantum Computing
  - Artificial Intelligence
  - Open Source
date: 2026-05-27T00:00:00+00:00
lastmod: 2026-05-27T00:00:00+00:00
featured: false
draft: false
projects:
  - qiskit-code-assistant

image:
  placement: 2
  caption: "Qiskit QuantumKatas: a benchmark for evaluating LLMs on quantum code"
  focal_point: "Smart"
  preview_only: false
---

Together with [Ismael Faro](https://www.linkedin.com/in/ismaelfaro/), I've just put a new preprint on arXiv: `Qiskit QuantumKatas, a benchmark for measuring how well large language models write quantum computing code`.

The starting point was [Microsoft's QuantumKatas](https://github.com/microsoft/QuantumKatas/) — a well-established, self-paced curriculum for learning quantum computing through programming exercises. The catch is that the originals are written in Q#. We translated them to Qiskit, the most widely-used quantum framework, and packaged the result with an evaluation pipeline built for systematic LLM assessment.

## What's in it

The benchmark has 350 tasks across 26 categories, spanning the full pedagogical arc the QuantumKatas were designed around: fundamental gates and superposition, through canonical algorithms like Deutsch–Jozsa, Simon's, and Grover's, up to error correction, key distribution, and quantum games. Each task ships with a natural-language prompt, a canonical solution, and a deterministic test that verifies correctness via classical circuit simulation — so a solution either reproduces the expected statevector or it doesn't. No approximate matching, no ambiguity.

Building on the QuantumKatas' existing structure rather than inventing tasks from scratch meant we inherited a principled difficulty progression and broad concept coverage. Our work sits on top of that: the Qiskit translation, the evaluation infrastructure, and the empirical analysis.

## What we found

To show the benchmark does its job, we evaluated 16 models across 7 prompting configurations — 39,200 runs in total. A few things stood out.

**It separates models cleanly.** Best-configuration pass rates run from 32.3% to 83.1%, with frontier models averaging about 26 points above open-source ones. That's a wide enough spread to be useful, with no ceiling or floor effects crowding the results together.

**Implementing a known algorithm is very different from encoding a problem.** Models do well when the task is to implement something documented — Simon's algorithm sits at 82.1%, basic gates at 81.6%. They struggle when they have to cast a classical problem into quantum terms — encoding SAT for Grover's search drops to 34.4%. The dominant failure mode across the board is logic errors, not syntax: the code runs and uses Qiskit correctly but produces the wrong quantum state.

**Chain-of-thought is not a free win.** It helped a few models — notably the reasoning-tuned ones — but degraded performance for the majority, leaving it mid-pack on average and behind simple few-shot prompting. The practical takeaway is that prompting strategy should track a model's provenance rather than defaulting to "more reasoning is better."

## Get it

Everything is open. The dataset, the evaluation framework, and all the baseline results are released so anyone can reproduce the numbers or run their own models against the benchmark.

- **Paper:** [arXiv:2605.27210](https://arxiv.org/abs/2605.27210)
- **Dataset:** [Qiskit/Qiskit-QuantumKatas on HuggingFace](https://huggingface.co/datasets/Qiskit/Qiskit-QuantumKatas)
- **Code:** [qiskit-community/Qiskit-QuantumKatas on GitHub](https://github.com/qiskit-community/Qiskit-QuantumKatas/)

If you work on quantum code generation, model evaluation, or quantum education tooling, I'd be glad to hear what you make of it.
