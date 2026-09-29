---
title: 'Juan Cruz-Benito'
type: 'landing'

sections:
  - block: resume-biography-3
    id: about
    content:
      username: juancb
    design:
      name:
        size: sm

  - block: content-collection
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - projects
        featured_only: false
      count: 0
    design:
      view: card
      columns: 2
      show_date: false
      show_read_time: false

  - block: content-collection
    id: posts
    content:
      title: Recent Posts
      filters:
        folders:
          - blog
      count: 5
      archive:
        text: See all posts
        url: /blog/
    design:
      view: date-title-summary

  - block: content-collection
    id: publications
    content:
      title: Recent Publications
      filters:
        folders:
          - publications
      count: 10
      archive:
        text: See all publications
        url: /publications/
    design:
      view: citation

  - block: resume-experience
    id: experience
    content:
      username: juancb

  - block: content-collection
    id: talks
    content:
      title: Recent Talks
      filters:
        folders:
          - events
      count: 5
      archive:
        text: See all talks
        url: /events/
    design:
      view: date-title-summary

  - block: resume-awards
    id: accomplishments
    content:
      title: Awards & Accomplishments
      username: juancb

  - block: contact-info
    id: contact
    content:
      title: Contact
      connect_title: Get in touch
      text: "Happy to talk about research collaborations, open source, Quantum+AI, or speaking opportunities. Use the form below or reach me on any of these networks."
      social:
        - icon: brands/x
          url: 'https://twitter.com/_juancb'
        - icon: brands/github
          url: 'https://github.com/cbjuan'
        - icon: brands/linkedin
          url: 'https://www.linkedin.com/in/juancb/'
      show_form: true
      form_action: 'https://formspree.io/cruzbenitojuan@gmail.com'
---
