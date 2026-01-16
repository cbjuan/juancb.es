+++
title = "Pauli Network Circuit Synthesis with Reinforcement Learning"
date = 2025-03-18
authors = ["Ayushi Dubal", "David Kremer", "Simon Martiel", "Victor Villar", "Derek Wang", "Juan Cruz-Benito"]
publication_types = ["3"]
abstract = "We introduce a Reinforcement Learning (RL)-based method for re-synthesis of quantum circuits containing arbitrary Pauli rotations alongside Clifford operations. By collapsing each sub-block to a compact representation and then synthesizing it step-by-step through a learned heuristic, we obtain circuits that are both shorter and compliant with hardware connectivity constraints. We find that the method is fast enough and good enough to work as an optimization procedure: in direct comparisons on 6-qubit random Pauli Networks against state-of-the-art heuristic methods, our RL approach yields over 2x reduction in two-qubit gate count, while executing in under 10 milliseconds per circuit. We further integrate the method into a collect-and-re-synthesize pipeline, applied as a Qiskit transpiler pass, where we observe average improvements of 20% in two-qubit gate count and depth, reaching up to 60% for many instances, across the Benchpress benchmark. These results highlight the potential of RL-driven synthesis to significantly improve circuit quality in realistic, large-scale quantum transpilation workloads"
selected = true
publication = "*arXiv preprint arXiv:2503.14448*"
tags = ["Quantum Computing","Machine Learning", "Artificial Intelligence", "Reinforcement Learning", "Circuit Synthesis", "Pauli Networks", "Clifford Circuits", "Transpiling"]
projects = ["qiskit-ibm-transpiler", "qiskit-gym"]
url_source = "https://arxiv.org/abs/2503.14448"
doi = "10.48550/arXiv.2503.14448"
+++
