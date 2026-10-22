---
title: IBM Quantum Job Scheduling
summary: The fair-share queue that schedules every job on every IBM Quantum QPU, plus ML models that predict QPU processing time
tags:
- Quantum Computing
- Distributed Systems
- Machine Learning
- Production Systems
date: "2020-06-01T00:00:00Z"

# Former/archived marker: hides this card from the homepage (see layouts/_partials/project_status.html).
project_status: former
project_status_since: 2025-01-01
project_status_note: "The fair-share queue moved to another team in 2020; I kept working on QPU time prediction until 2025."

external_link: ""

image:
  caption: ""
  focal_point: Smart

links:
- icon: hero/book-open
  label: Fair-share docs
  url: https://quantum.cloud.ibm.com/docs/guides/fair-share-scheduler
- icon: hero/document-text
  label: QPU time paper
  url: https://arxiv.org/abs/2510.20630

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
---

Designed and implemented the **fair-share queue** that decides the order in which jobs run on IBM Quantum hardware. It balances access across users and organizations according to their allocations, and it schedules **every job run on every IBM Quantum QPU** — still in production today. I stopped working on the queueing system in 2020; another team owns it now.

Later, as Data & Intelligence Chapter Lead, I led work on **predicting QPU processing time** for user jobs, which has been deployed on production since 2023. Based on this experience, we published a paper at IEEE QCE 2025 in which we used a dataset of ~150,000 jobs following the IBM Quantum schema, gradient-boosting models (LightGBM) forecast how long each job will take on the hardware, giving scheduling and resource management a better signal than static estimates. I worked on this prediction effort until 2025.
