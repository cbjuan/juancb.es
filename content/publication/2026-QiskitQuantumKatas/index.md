+++
title = "Qiskit QuantumKatas: Adapting Microsoft's Quantum Computing exercises for LLM evaluation"
date = 2026-05-26
authors = ["Juan Cruz-Benito", "Ismael Faro"]
publication_types = ["3"]
abstract = "We adapt Microsoft's QuantumKatas - a well-established quantum computing curriculum - from Q# to Qiskit, the most widely-adopted quantum computing framework, and package it with an evaluation framework for systematic LLM assessment. The resulting benchmark comprises 350 tasks across 26 categories, spanning fundamental gates through advanced algorithms (Grover's, Simon's, Deutsch-Jozsa), error correction, key distribution, and quantum games. Each task includes a natural language prompt, canonical solution, and deterministic test verification via classical circuit simulation. By building on the QuantumKatas' proven pedagogical design rather than creating tasks from scratch, we inherit a principled difficulty progression and comprehensive concept coverage while contributing the framework adaptation, evaluation infrastructure, and empirical analysis. We evaluate 16 LLMs across 7 prompting configurations - a total of 39,200 model runs - to demonstrate the benchmark's utility. Three key findings emerge: (1) the benchmark effectively differentiates model capabilities, with best-configuration pass rates ranging from 32.3% to 83.1% and a 26.1 pp average gap between frontier and open-source models; (2) models perform well at implementing known algorithms (SimonsAlgorithm 82.1%, BasicGates 81.6%) but struggle with problem encoding (SolveSATWithGrover 34.4%, DistinguishUnitaries 40.0%); and (3) chain-of-thought prompting shows a modestly bimodal effect - it is the best strategy for three models (two of them explicitly reasoning-tuned per vendor documentation) but degrades performance for the rest, leaving it mid-pack in aggregate (56.3% mean) behind few-shot-5 (57.8%). We release the benchmark, evaluation framework, and baseline results to support research on LLM capabilities in quantum computing. "
selected = true
publication = "*arXiv preprint arXiv:2605.27210*"
tags = ["Qiskit", "Large Language Models", "Evaluation benchmarks", "QuantumKatas", "Quantum Computing"]
projects = ["qiskit-code-assistant"]
url_source = "https://arxiv.org/abs/2605.27210"
url_pdf = "https://arxiv.org/pdf/2605.27210"
doi = "10.48550/arXiv.2605.27210"
+++
