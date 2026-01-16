---
title: Qiskit Gym
summary: Reinforcement learning environments for quantum circuit synthesis — powers the AI transpiler passes
tags:
- Reinforcement Learning
- Quantum Computing
- AI
- Open Source
date: "2025-02-01T00:00:00Z"

external_link: ""

image:
  caption: ""
  focal_point: Smart

links:
- icon: github
  icon_pack: fab
  name: GitHub
  url: https://github.com/AI4quantum/qiskit-gym

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
---

Gymnasium-compatible RL environments for training AI agents to synthesize quantum circuits. The framework that powers the AI transpiler passes achieving state-of-the-art results in qiskit-ibm-transpiler.

**Three synthesis environments:**
- **Permutation Synthesis** — Minimal SWAP gate implementations respecting hardware coupling
- **Linear Function Synthesis** — CNOT-optimal decomposition of Boolean linear functions
- **Clifford Synthesis** — Hardware-efficient implementations of Clifford group elements

Hardware-aware design matches real quantum device coupling maps. High-performance Rust backend enables fast training. Supports PPO, AlphaZero, and custom policies with built-in TensorBoard visualization.

The agents trained with this framework achieve near-optimal synthesis up to 65 qubits—orders of magnitude faster than SAT solvers.
