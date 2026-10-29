---
layout: post
title: "WAMF Development Update: From v0.4.1 to v0.4.3"
description: "Three WAMF maintenance releases focused on security, reliability, safer setup and strengthening the foundations for Kingfisher."
date: 2026-10-29 18:00:00 +0000
author: Ian Collins
category: Release
version: v0.4.3
tags:
  - Release
  - Security
  - Docker
  - Wildlife Monitoring
  - Open Source
published: true
excerpt: >
  Since the release of WAMF v0.4.0, three maintenance updates have focused
  on security, dependency management, safer first-run setup and regression
  testing. Here's what changed in v0.4.1, v0.4.2 and v0.4.3, and where the
  project is heading next.
---

## WAMF Development Update: From v0.4.1 to v0.4.3

It's been a busy few weeks for WAMF.

Following the release of [v0.4.0](/blog/2026/09/18/wamf-v0.4.0-released/), development has continued with three maintenance releases, culminating in **WAMF v0.4.3**, published on 28 October 2026.

None of these releases introduces a major new wildlife monitoring feature. Instead, they've concentrated on something equally important: making the existing platform more secure, reliable and maintainable.

A project that processes camera events, downloads media, runs classification models and stores observations needs more than an attractive interface. It also needs to handle unexpected input, protect credentials, survive upgrades and behave predictably when things go wrong.

That's where much of the recent work has been focused.

## v0.4.1: Strengthening the Foundations

The first maintenance release concentrated primarily on dependencies and deployment security.

WAMF relies on several Python libraries for its web interface, image processing, networking and species classification. Keeping those dependencies current is important, but updates also need to preserve compatibility with the existing application.

For v0.4.1, compatible dependencies were updated and constrained, including Flask, Werkzeug, Requests, Pillow, certifi and urllib3.

The Docker image also received attention.

Unused multimedia and OpenCV components were removed from the runtime, along with unnecessary packaging tools. The Python and Debian runtime base was updated, reducing the amount of software included in the container.

Less unnecessary software means fewer components to maintain and a smaller potential attack surface.

However, dependency updates are only useful if the application still works afterwards.

The release was tested against the existing configuration and database formats, administrator credentials, API authentication and session handling.

Importantly, it was also validated on Bird-Watcher, a separate test machine running the complete Frigate-to-WAMF pipeline.

That included real MQTT events, CPU-based bird classification, observation storage, media archiving and persistence across container restarts.

The goal was to improve security without breaking existing installations.

[Read the v0.4.1 release notes](https://github.com/WAMF-Project/WAMF/releases/tag/v0.4.1).

## v0.4.2: Hardening the Application

While v0.4.1 focused largely on dependencies and deployment, v0.4.2 turned attention towards the application itself.

Several areas were reviewed and hardened, particularly where external information enters WAMF.

Detection values are now handled as data rather than executable HTML, and Frigate event identifiers receive additional validation.

Media proxy handling was also tightened, including URL paths, redirects and streaming behaviour.

Login protection received improvements to prevent spoofed forwarding headers from influencing rate limiting, while diagnostic responses and logs were reviewed to reduce the risk of exposing sensitive information.

These changes aren't especially visible during normal use, which is precisely the point.

A security improvement is often something that prevents an unexpected situation from becoming a problem.

### A Safer First-Run Experience

One of the more noticeable changes in v0.4.2 was the administrator setup process.

Previously, a fresh installation generated a temporary administrator password.

Now, WAMF generates a private, single-use setup link, allowing the administrator to choose their own password during initial configuration.

The link expires after 15 minutes, and restarting an installation that hasn't completed setup invalidates the previous link.

This makes the initial setup process more deliberate, although administrators still need to protect startup logs and use a secure connection when configuring WAMF remotely.

Operational workers also wait until administrator setup is complete before proceeding.

### Interface and Browser Improvements

The release restored mobile navigation controls and changed how the Monaco configuration editor is delivered.

Rather than relying on an external service for the editor, WAMF now serves its Monaco assets locally.

Remaining external Bootstrap and jQuery assets use integrity checks to help ensure the browser receives the expected files.

Together, these changes improve both the security and predictability of the web interface.

[Read the v0.4.2 release notes](https://github.com/WAMF-Project/WAMF/releases/tag/v0.4.2).

## v0.4.3: Closing the Remaining Navigation Issue

The latest maintenance release, **v0.4.3**, addresses a security issue involving navigation within the WAMF interface.

When WAMF is embedded in another interface, such as a Home Assistant dashboard, navigation requires some additional handling.

That handling now uses the browser's URL parser to validate destinations and permits only HTTP and HTTPS URLs.

Malformed or unsafe destinations are rejected, while normal internal links, external websites, page fragments and Home Assistant embedded navigation continue to work.

The change also prompted additional regression testing.

Tests now cover permitted and rejected URL formats, login redirects, date navigation, embedded links and browser history behaviour.

The browser-testing environment was improved too, making automated Chromium tests more reliable in continuous integration.

Some of the security tests were also updated to use Python's built-in HTML parser rather than relying on regular expressions to extract HTML content.

### Testing Before Release

By the time v0.4.3 was ready, the complete Python 3.11 test suite contained **1,860 passing tests, with none skipped**.

The release candidate Docker image was also built and tested on Linux/AMD64.

Those checks confirmed application startup, version reporting, authenticated health access and database and archive health.

The isolated Docker smoke test didn't repeat the full live Frigate and MQTT integration testing, so it's important not to confuse the two.

The aim was to validate the specific maintenance changes while retaining the previously established application behaviour.

[Read the v0.4.3 release notes](https://github.com/WAMF-Project/WAMF/releases/tag/v0.4.3).

## Security Is an Ongoing Process

One lesson from these releases is that security maintenance isn't a single task that can simply be marked complete.

Reviewing dependencies and application code can reveal problems that need fixing immediately, alongside others that require a longer-term solution.

For example, WAMF currently retains protobuf 3.20.3 because of compatibility requirements in its existing TensorFlow Lite support stack.

Two known protobuf vulnerabilities remain documented as accepted risks rather than patched issues.

That distinction matters.

Passing automated tests or closing security alerts doesn't mean that an application has no remaining vulnerabilities.

For WAMF, the approach is to document those limitations, understand their exposure and address them as the underlying architecture and dependencies evolve.

The updated [security documentation](https://docs.wamf.uk/reference/security/) provides further information.

## What Does This Mean for Existing Users?

For anyone already running WAMF v0.4.x, these maintenance releases are intended to strengthen the existing installation without changing the underlying wildlife monitoring workflow.

WAMF still receives bird detections from Frigate over MQTT, retrieves the associated media, performs species classification and stores observations for browsing and review.

The releases retain the existing database and media formats, and v0.4.3 introduces no configuration migration.

Docker remains the recommended deployment method.

The current published image is:

`ghcr.io/wamf-project/wamf:0.4.3`

WAMF v0.4.3 supports Linux/AMD64 and continues to use CPU-based TensorFlow Lite species classification.

As always, stop WAMF cleanly and back up configuration, database and media before upgrading.

The [installation](https://docs.wamf.uk/getting-started/installation/) and [Docker deployment](https://docs.wamf.uk/deployment/docker/) guides have been updated to reflect the current stable release.

## Looking Ahead: Kingfisher

With the v0.4.x maintenance work completed, attention can return to the next major stage of WAMF development.

**WAMF v0.5.0, codenamed Kingfisher**, is a much broader development effort.

Kingfisher is focused on modernising the application, improving administration and configuration, refining the user interface and making WAMF easier to extend.

Work includes moving to Python 3.12, modernising species classification, improving system health information and giving administrators better tools for managing the application.

There's also considerable work happening behind the scenes to make WAMF's components more reusable and easier to maintain.

Kingfisher remains in development. These capabilities should not be confused with features available in the current stable v0.4.3 release.

Beyond Kingfisher, the planned Raven development phase will explore a more fundamental change: allowing WAMF to receive wildlife observations from detection sources other than Frigate.

That could eventually include direct camera processing, alternative inference hardware and dedicated edge devices.

For now, those remain future plans.

## A Stronger Place to Build From

Three maintenance releases in three days might not sound particularly exciting compared with announcing new detection models or an entirely redesigned interface.

But they've addressed important parts of the application that are easy to overlook when concentrating on new features.

Dependency management, secure setup, input validation, authentication, regression testing and reliable deployments all contribute to making WAMF something people can run with confidence.

There will undoubtedly be more issues to discover and improvements to make. That's part of developing and maintaining an open-source project.

For now, **v0.4.3 is the recommended stable release**, and Kingfisher is the next chapter.

Hopefully, the birds will continue providing enough test data to keep development interesting.

They've certainly never shown much interest in following the roadmap.

Thanks for following the project.