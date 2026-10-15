---
aliases:
  - '/project/qiskit-mcp-servers/'
title: Qiskit MCP Servers
summary: Model Context Protocol servers connecting AI assistants to IBM Quantum services
tags:
- AI
- Quantum Computing
- MCP
- Developer Tools
date: "2025-01-01T00:00:00Z"

external_link: ""

image:
  caption: ""
  focal_point: Smart

links:
- icon: brands/github
  label: GitHub
  url: https://github.com/Qiskit/mcp-servers

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
---

Production-ready Model Context Protocol servers that give AI assistants direct access to quantum computing infrastructure. Built on FastMCP with async-first architecture, full type safety, and 65%+ test coverage.

**Five specialized servers:**
- **Qiskit Server** — Circuit creation, manipulation, and transpilation
- **Code Assistant Server** — AI-assisted quantum programming via Granite models
- **IBM Runtime Server** — Hardware access, job execution, and backend selection
- **AI Transpiler Server** — RL-powered circuit optimization
- **Qiskit Gym Server** — Lets AI agents train RL models for circuit synthesis on their own: create environments, launch PPO or AlphaZero training, and synthesize circuits ([announcement](/blog/2026-qiskit-gym-mcp-server/))

Enables AI systems to autonomously generate quantum code, select optimal backends, execute circuits on real hardware, train their own circuit-synthesis models, and provide expert quantum computing guidance—all through a standardized protocol.
