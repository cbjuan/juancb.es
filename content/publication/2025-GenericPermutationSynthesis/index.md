+++
title = "AI Methods for Permutation Circuit Synthesis Across Generic Topologies"
date = 2025-09-19
authors = ["Victor Villar", "Juan Cruz-Benito", "Ismael Faro", "David Kremer"]
publication_types = ["3"]
abstract = "This paper investigates artificial intelligence (AI) methodologies for the synthesis and transpilation of permutation circuits across generic topologies. Our approach uses Reinforcement Learning (RL) techniques to achieve near-optimal synthesis of permutation circuits up to 25 qubits. Rather than developing specialized models for individual topologies, we train a foundational model on a generic rectangular lattice, and employ masking mechanisms to dynamically select subsets of topologies during the synthesis. This enables the synthesis of permutation circuits on any topology that can be embedded within the rectangular lattice, without the need to re-train the model. In this paper we show results for 5x5 lattice and compare them to previous AI topology-oriented models and classical methods, showing that they outperform classical heuristics, and match previous specialized AI models, and performs synthesis even for topologies that were not seen during training. We further show that the model can be fine tuned to strengthen the performance for selected topologies of interest. This methodology allows a single trained model to efficiently synthesize circuits across diverse topologies, allowing its practical integration into transpilation workflows."
selected = true
publication = "*arXiv preprint arXiv:2509.16020*"
tags = ["Quantum Computing","Machine Learning", "Artificial Intelligence", "Reinforcement Learning", "Circuit Synthesis", "Permutation Circuit"]
url_source = "https://arxiv.org/abs/2509.16020"
doi = "10.48550/arXiv.2509.16020"
+++
