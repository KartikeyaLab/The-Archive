# *the* Archive

> **Moments, Made To Keep.**

A personal portfolio and showcase site by **Kartikeya** — a dark, glass-morphism aesthetic built with pure HTML, Tailwind CSS, and vanilla JavaScript. No frameworks, no build steps.

---

## Live Site

**[kartikeyalab.github.io/the-archive](https://kartikeyalab.github.io/the-archive/)** *(update with your actual URL)*

---

## What's Inside

| Section | Description |
|---|---|
| **Hero** | Animated header with social dock (Email, YouTube, GitHub, Portfolio) |
| **Tribute** | Embedded YouTube video dedicated to the artists who inspired this work |
| **Creations** | Showcase of two computer vision projects with image/GIF carousels |
| **In Kindness** | A personal closing note |
| **Footer** | About + contact |

### Featured Projects

**Program 01 — Computer Camera**
An ASCII art camera that renders the world through the language of characters. Inspired by a YouTube Short watched years ago, it was exhibited live to people who loved seeing themselves through a screen of text.
[Download Source](https://github.com/KartikeyaLab/Computer-Camera/archive/refs/heads/main.zip) · [GitHub Repo](https://github.com/KartikeyaLab/Computer-Camera)

**Program 02 — Air Drawing**
Draw on screen using mid-air finger gestures — the camera tracks your hand to register color, stroke, and position. Born from an idea about innovating outside your own industry.
[Download Source](https://github.com/KartikeyaLab/Air-Drawing/archive/refs/heads/main.zip) · [GitHub Repo](https://github.com/KartikeyaLab/Air-Drawing)

---

## Tech Stack

- **HTML5** — semantic, single-file structure
- **[Tailwind CSS](https://tailwindcss.com/)** (CDN) — utility-first styling
- **Vanilla JavaScript** — carousels, scroll effects, mobile nav, fade animations
- **[Font Awesome](https://fontawesome.com/)** — icons
- **[Google Fonts — Montserrat](https://fonts.google.com/specimen/Montserrat)** — typography
- **[Lottie Player](https://lottiefiles.com/web-player)** — animation support

---

## Design Details

- **Dark background** `#10121b` with glass-morphism cards
- **Shimmer animation** on feature cards (`@keyframes shimmer`)
- **Scroll-aware fade** on hero elements
- **Auto-advancing carousel** (3.5s interval) with dot indicators and prev/next arrows
- **Responsive nav** with mobile slide-in menu
- **Scroll progress bar** on the navbar

---

## File Structure

```
/
├── index.html          # Main page
├── style.css           # Custom styles (nav, mobile menu, layout)
├── Favicon/            # All favicon sizes (iOS, Android, Windows)
├── Pictures/           # Computer Camera carousel images (img_001–019, vid_001–003)
└── Drawing/            # Air Drawing carousel images (img_001–015)
```

> **Carousel convention:** Images are named `img_001.png`, `img_002.png`, … and GIFs are named `vid_001.gif`, `vid_002.gif`, …

---

## Local Development

No build step needed. Just open the file:

```bash
git clone https://github.com/KartikeyaLab/the-archive.git
cd the-archive
open index.html   # or use Live Server in VS Code
```

---

## Connect

| | |
|---|---|
| **Email** | kartikeya30062009@gmail.com |
| **YouTube** | [@clever-ways](https://www.youtube.com/@clever-ways) |
| **GitHub** | [KartikeyaLab](https://github.com/KartikeyaLab) |
| **Portfolio** | [kartikeyalab.github.io/kartikeya](https://kartikeyalab.github.io/kartikeya/) |

---

© *the* Archive. Made with euphoria.
