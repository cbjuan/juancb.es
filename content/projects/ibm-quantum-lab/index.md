---
title: IBM Quantum Lab
summary: Cloud Jupyter notebook platform (JupyterHub on Kubernetes) open to ~240K quantum computing users — retired in 2024
tags:
- Quantum Computing
- Jupyter
- Kubernetes
- Developer Tools
date: "2020-01-01T00:00:00Z"

# Former/archived marker: hides this card from the homepage (see layouts/_partials/project_status.html).
project_status: archived
project_status_since: 2024-05-15
project_status_note: "IBM retired the Lab to refocus the platform on [utility-scale computing](https://quantum.cloud.ibm.com/announcements/en/product-updates/2024-05-15-2024-sunset-final-lab-simulators)."

external_link: ""

image:
  caption: ""
  focal_point: Smart

links:
- icon: hero/presentation-chart-bar
  label: JupyterCon talk
  url: /events/2020_jupytercon/

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
---

Led development of IBM Quantum Lab, the cloud notebook environment where IBM Quantum users wrote and ran Qiskit code against real quantum hardware without installing anything. Built as a **JupyterHub deployment on Kubernetes** integrated with the IBM Quantum platform, open to **~240,000 enrolled users**.

**Engineering challenges solved:**
- Custom authentication against the IBM Quantum platform
- Persistent per-user storage and tailored user environments with Qiskit and tutorials pre-installed
- Automatic selection of hardware resources for different user profiles
- Abuse protection and performance at scale — peaks of **~800 concurrent user servers** during the IBM Quantum Challenge

Presented at JupyterCon 2020.
