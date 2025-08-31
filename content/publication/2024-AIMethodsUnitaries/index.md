+++
title = "AI methods for approximate compiling of unitaries"
date = 2024-09-15
authors = ["David Kremer", "Victor Villar", "Sanjay Vishwakarma", "Ismael Faro", "Juan Cruz-Benito"]
publication_types = ["1"]
abstract = "This paper explores artificial intelligence (AI) methods for the approximate compiling of unitaries, focusing on the use of fixed two-qubit gates and arbitrary single-qubit rotations typical in superconducting hardware. Our approach involves three main stages: identifying an initial template that approximates the target unitary, predicting initial parameters for this template, and refining these parameters to maximize the fidelity of the circuit. We propose AI-driven approaches for the first two stages, with a deep learning model that suggests initial templates and an autoencoder-like model that suggests parameter values, which are refined through gradient descent to achieve the desired fidelity. We demonstrate the method on 2 and 3-qubit unitaries, showcasing promising improvements over exhaustive search and random parameter initialization. The results highlight the potential of AI to enhance the transpiling process, supporting more efficient quantum computations on current and future quantum hardware."
selected = false
publication = "In _2024 IEEE International Conference on Quantum Computing and Engineering (QCE)_ Vol. 1, pp. 1163-1168"
tags = ["Quantum Computing","Machine Learning", "Artificial Intelligence", "Unitary synthesis", "Approximate compiling"]
url_source = "https://ieeexplore.ieee.org/abstract/document/10821333/"
url_pdf= "https://arxiv.org/pdf/2407.21225"
doi = "10.1109/QCE60285.2024.00136"
+++
