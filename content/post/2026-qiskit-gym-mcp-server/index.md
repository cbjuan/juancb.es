---
title: 'We Got AI Agents to Train RL Models for Quantum Transpilation'
subtitle: 'Introducing qiskit-gym-mcp-server: autonomous reinforcement learning training for quantum circuit synthesis'
summary: 'A new MCP server that enables AI agents to autonomously train reinforcement learning models for quantum circuit synthesis - including permutation, linear function, and Clifford circuits.'
authors:
- juancb
tags:
- Quantum Computing
- AI
- Machine Learning
- Qiskit
- MCP
- Reinforcement Learning
- AI for Quantum
categories:
- Quantum Computing
- Artificial Intelligence
date: "2026-01-22T00:00:00Z"
lastmod: "2026-01-22T00:00:00Z"
featured: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Placement options: 1 = Full column width, 2 = Out-set, 3 = Screen-width
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
image:
  placement: 2
  caption: 'Qiskit Gym MCP Server - AI Agents Training RL Models for Quantum Transpilation'
  focal_point: "Smart"
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
- qiskit-gym
- qiskit-mcp-servers
- qiskit-ibm-transpiler
---

What if you could tell an AI assistant: `train a model of X qubits to synthesize linear function circuits using the topology YYYY and 100 million steps` - and it just does it? That's now possible with the new **qiskit-gym-mcp-server**.

Inspired by the work Hugging Face has done with [HF Skills Training](https://huggingface.co/blog/hf-skills-training) - where Claude and other agents can submit fine-tuning jobs through natural language - we've built something similar for quantum circuit synthesis. The key difference: instead of fine-tuning LLMs, we're training RL agents that learn to synthesize quantum circuits optimized for real hardware.

<video controls width="100%">
  <source src="demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## What Is qiskit-gym-mcp-server?

The [qiskit-gym-mcp-server](https://github.com/Qiskit/mcp-servers/tree/main/qiskit-gym-mcp-server) is a community MCP (Model Context Protocol) server that integrates the [qiskit-gym](https://github.com/AI4quantum/qiskit-gym) library. It exposes reinforcement learning-based quantum circuit synthesis as tools that AI agents can invoke autonomously.

The server enables three main synthesis capabilities:

- **Permutation synthesis**: Uses SWAP gate routing to handle qubit permutations on constrained topologies
- **LinearFunction synthesis**: Synthesizes CNOT circuits for linear boolean functions
- **Clifford synthesis**: Generates Clifford circuits using H, S, and CNOT gates

## How It Works

The workflow is straightforward. An AI assistant connected via MCP can:

1. **Create environments** for different quantum circuit problems, supporting various hardware topologies including linear arrays, grid layouts, and layouts from real IBM backends
2. **Train models** asynchronously using PPO or AlphaZero algorithms with real-time progress monitoring via TensorBoard
3. **Save and manage** trained models for later use
4. **Synthesize circuits** using the trained models

```
AI Assistant → MCP Client → create_*_env_tool → start_training_tool
                ↓                ↓
            gym_core.py (envs)  training.py (RLSynthesis)
                ↓
            synthesize_*_tool
                ↓
            Optimized circuit (QPY format)
```

## The Agentic Example

To demonstrate the full potential, we've included a LangChain-based agent example in the [MCP server](https://github.com/Qiskit/mcp-servers/tree/main/qiskit-gym-mcp-server/examples). The agent can:

- Create RL environments for specific synthesis tasks
- Configure and launch training runs
- Monitor progress and adjust hyperparameters
- Use trained models to synthesize optimized circuits
- Save models for deployment

This isn't a toy demo - it's a proof of concept of how we envision training our AI-based transpilation models that can outperform most existing heuristic methods, as demonstrated in [Benchpress](https://www.nature.com/articles/s43588-025-00792-y) (*Nature Computational Science*, 2025).

## Getting Started

Install with pip:

```bash
# Full installation with all servers
pip install qiskit-mcp-servers[all]

# Or just the gym server
pip install qiskit-mcp-servers[gym]
```

Configure your MCP client (Claude Code, Cursor, etc.) to connect to the server, and you're ready to start training RL models through conversation.

## Why This Matters

The intersection of AI agents and quantum computing opens up new possibilities for automating complex optimization tasks. Instead of manually configuring training runs and tuning hyperparameters, you can describe what you want in natural language and let the agent handle the details.

This is just the beginning. The same pattern can extend to other quantum computing tasks and other fields.

---

**Links:**
- Pull Request: https://github.com/Qiskit/mcp-servers/pull/100
- qiskit-gym-mcp-server: https://github.com/Qiskit/mcp-servers/tree/main/qiskit-gym-mcp-server/
- PyPI: https://pypi.org/project/qiskit-gym-mcp-server/
- qiskit-gym: https://github.com/AI4quantum/qiskit-gym
- HF Skills Training (inspiration): https://huggingface.co/blog/hf-skills-training
