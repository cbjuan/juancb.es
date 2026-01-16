+++
title = "AI Methods for Permutation Circuit Synthesis Across Generic Topologies"
date = 2025-11-23
authors = ["Victor Villar", "Juan Cruz-Benito", "Ismael Faro", "David Kremer"]
publication_types = ["1"]
abstract = "This paper investigates artificial intelligence (AI) methodologies for the synthesis and transpilation of permutation circuits across generic topologies. Our approach uses Reinforcement Learning (RL) techniques to achieve near-optimal synthesis of permutation circuits up to 25 qubits. Rather than developing specialized models for individual topologies, we train a foundational model on a generic rectangular lattice, and employ masking mechanisms to dynamically select subsets of topologies during the synthesis. This enables the synthesis of permutation circuits on any topology that can be embedded within the rectangular lattice, without the need to re-train the model. In this paper we show results for 5x5 lattice and compare them to previous AI topology-oriented models and classical methods, showing that they outperform classical heuristics, and match previous specialized AI models, and performs synthesis even for topologies that were not seen during training. We further show that the model can be fine tuned to strengthen the performance for selected topologies of interest. This methodology allows a single trained model to efficiently synthesize circuits across diverse topologies, allowing its practical integration into transpilation workflows."
selected = true
publication = "*Proceedings of the AAAI Fall Symposium Series, 7(1)*"
tags = ["Quantum Computing","Machine Learning", "Artificial Intelligence", "Reinforcement Learning", "Circuit Synthesis", "Permutation Circuit"]
projects = ["qiskit-ibm-transpiler", "qiskit-gym"]
url_source = "https://ojs.aaai.org/index.php/AAAI-SS/article/view/36912"
url_pdf = "https://ojs.aaai.org/index.php/AAAI-SS/article/view/36912/39050"
doi = "10.1609/aaaiss.v7i1.36912"
+++
