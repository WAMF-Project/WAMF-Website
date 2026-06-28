---
layout: post

title: "Building the WAMF Website"

description: "Why WAMF uses a lightweight static website, GitHub Pages and Jekyll to document the project and share development progress."

date: 2026-06-28 17:00:00 +0100

author: Ian Collins

category: Development

version: v0.4

tags:
  - Website
  - GitHub Pages
  - Jekyll
  - Open Source

published: true

excerpt: >
  The WAMF website has grown from a simple landing page into the public home of
  the project. This post explores the design decisions behind the site, why
  GitHub Pages was chosen, and how Jekyll provides a lightweight publishing
  workflow for development updates.
---

## Building the WAMF Website

When I first started WAMF, the website wasn't a priority. The focus was entirely on building the application itself. As the project matured, it became clear that WAMF needed more than a GitHub repository. It needed a place to explain the project, showcase its features and provide a central hub for documentation and future development updates.

## Keeping it simple

One of the first decisions was to avoid a large JavaScript framework.

There are some excellent website frameworks available today, but they also introduce additional tooling, dependencies and build processes. For WAMF, that complexity didn't feel necessary.

Instead, the website is built using straightforward HTML and CSS, hosted on GitHub Pages. The result is a site that's fast, lightweight and easy to maintain.

## Why Jekyll?

Although the website itself remains largely static, I wanted an easy way to publish development updates without manually creating HTML pages for every article.

GitHub Pages already supports Jekyll, making it a natural fit.

Adding Jekyll allows the website to keep its simple structure while providing a proper blog powered by Markdown. Writing a new article is now as simple as creating a file in the `_posts` directory, committing it to GitHub and letting GitHub Pages do the rest.

It keeps the workflow lightweight while making it much easier to share development progress.

## More than a homepage

The website is intended to become the public face of WAMF.

Today it includes:

- A landing page introducing the project.
- A roadmap outlining the current direction of development.
- A development blog sharing progress and design decisions.

Documentation will follow separately using MkDocs, allowing the website to focus on introducing the project while the documentation provides detailed installation and user guides.

## Building in public

One of the advantages of open source development is sharing not only the finished software, but also the journey behind it.

Future posts will cover architectural decisions, new features, experiments and lessons learned as WAMF continues to evolve.

Whether you're simply interested in wildlife monitoring or you're thinking about contributing to the project, I hope these updates provide a useful insight into how WAMF is growing.

Thanks for following the journey.
