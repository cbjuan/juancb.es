+++
title = "IBM Quantum Experience Notebooks. Serving JupyterHub at scale for the Quantum Computing Community"
date = 2020-10-14T00:00:00  # Schedule page publish date.
draft = false

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
time_start = 2020-10-14T18:45:00
time_end = 2020-10-14T19:00:00

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = []

# Abstract and optional shortened version.
abstract = "How can we enable a complete online experience for IBM’s Quantum Experience (https://quantum-computing.ibm.com/) users to access all of our quantum devices and software libraries effortlessly? That question fired a research and engineering process at the core of the IBM Quantum cloud software team to provision, and integrate with our software, a JupyterHub deployment on Kubernetes available for ~240000 enrolled users. In this talk, we discuss how we have integrated JupyterHub with our already existing IBM Quantum Experience platform and how we are leveraging the power of the JupyterHub to provide the best experience to the users. Among other aspects, during the presentation, we cover how we have solved, and we're still addressing issues related to custom authentication with our platform, performance, look & feel, permanent storage per user, user environment tailoring, provision of pre-installed software like Qiskit (https://qiskit.org/) and other quantum-related software and tutorials, automation of the selection of custom hardware resources for different users, how we deal with malicious users, or how we handle ~800 concurrent user servers during our last May 4th challenge (https://www.ibm.com/blogs/research/2020/05/quantum-challenge-results/). To conclude the presentation, we will share some final reflections of our experience and plans we have to continue developing our platform and contributing to the Jupyter ecosystem."
abstract_short = "Since IBM put online the first cloud accessible quantum computer in 2016, there has been a surge of interest in accessing these systems. Among the different tools that IBM Quantum Experience provides to the quantum computing community, the cloud-based Jupyter Notebooks are a core part. This talk introduces how we enable ~240,000 users to use these notebooks via a JupyterHub deployed in Kubernetes."

# Name of event and optional event URL.
event = "JupyterCon 2020"
event_url = "https://cfp.jupytercon.com/2020/schedule/presentation/179/ibm-quantum-experience-notebooks-serving-jupyterhub-at-scale-for-the-quantum-computing-community/"

# Location of event.
location = "Online event"

# Is this a selected talk? (true/false)
selected = true

# Projects (optional).
#   Associate this talk with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["deep-learning"]` references 
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects = []

# Tags (optional).
#   Set `tags = []` for no tags, or use the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = []

# Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references 
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides = ""

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = ""
url_code = ""

# Does the content use math formatting?
math = true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = "Image credit: [**JupyterCon 2020**](https://jupytercon.com/)"

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Left"
+++

<!-- {{% alert note %}}
Click on the **Slides** button above to view the built-in slides feature.
{{% /alert %}}

Slides can be added in a few ways:

- **Create** slides using Academic's _Slides_ feature and link using `url_slides` parameter in the front matter of the talk file
- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://sourcethemes.com/academic/docs/writing-markdown-latex/).

Further talk details can easily be added to this page using _Markdown_ and $\rm \LaTeX$ math code. -->
