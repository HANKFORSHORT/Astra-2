# -*- coding: utf-8 -*-
"""
Build script for the Astra static site.
Generates every HTML page from shared header/footer/nav partials so the
markup stays consistent across pages while remaining plain, dependency-free
HTML once written to disk (no server-side includes involved at runtime).
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Icons (inline SVG, stroke-based, tiny footprint, theme-aware via currentColor)
# ---------------------------------------------------------------------------
ICONS = {
    "sun": '<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2.5M12 19.5V22M4.2 4.2l1.8 1.8M18 18l1.8 1.8M2 12h2.5M19.5 12H22M4.2 19.8L6 18M18 6l1.8-1.8"/></svg>',
    "moon": '<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a6.8 6.8 0 0 0 10.5 10.5Z"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="8 6 2 12 8 18"/><polyline points="16 6 22 12 16 18"/></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 4h8v4a4 4 0 0 1-8 0V4Z"/><path d="M8 5H4v1a4 4 0 0 0 4 4"/><path d="M16 5h4v1a4 4 0 0 1-4 4"/><path d="M10 14v3M14 14v3"/><path d="M8 21h8M9 17h6l1 4H8l1-4Z"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M12 20V4M20 20v-7"/></svg>',
    "dumbbell": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 7v10M18 7v10M2 10v4M22 10v4M6 12h12"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.1 6.5L12 17.6 6.2 20.5l1.1-6.5L2.5 9.4l6.6-.9L12 2.5Z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17.5" cy="9" r="2.6"/><path d="M15.7 12.4A5.2 5.2 0 0 1 21.5 17.5"/></svg>',
    "check-shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6l7-3Z"/><path d="M9 12l2 2 4-4"/></svg>',
    "arrow-up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
    "discord": '<svg viewBox="0 0 24 24"><path d="M20 5.6c-1.5-.7-3-1.2-4.7-1.4l-.3.6c1.5.4 2.8 1 4 1.7-2.2-1-4.6-1.6-7-1.6s-4.8.6-7 1.6c1.2-.8 2.6-1.3 4-1.7l-.3-.6C7 4.4 5.5 4.9 4 5.6 1.7 9 1 12.3 1.3 15.5c1.7 1.3 3.4 2 5 2.5l.7-1.3c-.8-.3-1.6-.7-2.3-1.2l.5-.4c3.5 1.6 7.3 1.6 10.8 0l.5.4c-.7.5-1.5.9-2.3 1.2l.7 1.3c1.6-.5 3.3-1.2 5-2.5.4-3.7-.5-7-2.9-9.9ZM8.7 13.4c-.8 0-1.5-.8-1.5-1.7s.7-1.7 1.5-1.7 1.5.8 1.5 1.7-.7 1.7-1.5 1.7Zm6.6 0c-.8 0-1.5-.8-1.5-1.7s.7-1.7 1.5-1.7 1.5.8 1.5 1.7-.6 1.7-1.5 1.7Z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24"><path d="M22 12s0-3.2-.4-4.7a2.8 2.8 0 0 0-2-2C17.9 5 12 5 12 5s-5.9 0-7.6.3a2.8 2.8 0 0 0-2 2C2 8.8 2 12 2 12s0 3.2.4 4.7a2.8 2.8 0 0 0 2 2C6.1 19 12 19 12 19s5.9 0 7.6-.3a2.8 2.8 0 0 0 2-2C22 15.2 22 12 22 12ZM10 15.3V8.7L15.8 12 10 15.3Z"/></svg>',
    "github": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.3-3.4-1.3-.4-1.2-1.1-1.5-1.1-1.5-1-.6.1-.6.1-.6 1 .1 1.6 1.1 1.6 1.1.9 1.6 2.4 1.1 3 .8.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5 0-1.1.4-2 1-2.7-.1-.3-.5-1.3.1-2.7 0 0 .9-.3 2.9 1a10 10 0 0 1 5.2 0c2-1.3 2.9-1 2.9-1 .6 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.9-2.4 4.7-4.6 5 .4.3.7 1 .7 2v3c0 .3.2.6.7.5A10 10 0 0 0 12 2Z"/></svg>',
    "x": '<svg viewBox="0 0 24 24"><path d="M4 4l7.3 9.6L4.4 20h1.9l6-6.6 4.6 6.6H21l-7.6-10L20 4h-1.9l-5.6 6-4.2-6H4Z"/></svg>',
}

def icon(name):
    return ICONS[name]

# ---------------------------------------------------------------------------
# <head> template
# ---------------------------------------------------------------------------
def head(title, description, path_prefix=""):
    return f"""<meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} · Astra</title>
  <meta name="description" content="{description}" />
  <link rel="icon" href="{path_prefix}images/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{path_prefix}css/style.css" />"""

# ---------------------------------------------------------------------------
# Header / nav (path_prefix lets pages in the same root reference assets;
# every page lives at site root so path_prefix stays "" throughout)
# ---------------------------------------------------------------------------
NAV_ITEMS = [
    ("problems.html", "Problems"),
    ("contests.html", "Contests"),
    ("gym.html", "Gym"),
    ("rankings.html", "Rankings"),
    ("guide.html", "Guide"),
    ("about.html", "About"),
]

def header(active=""):
    links = []
    for href, label in NAV_ITEMS:
        cls = " active" if href == active else ""
        links.append(f'<li><a href="{href}" class="{cls.strip()}">{label}</a></li>')
    links_html = "\n        ".join(links)
    return f"""<header class="site-header">
    <nav class="navbar container">
      <a href="index.html" class="brand">
        <span class="brand-mark" aria-hidden="true"></span>
        Astra
      </a>

      <ul class="nav-links" id="navLinks">
        {links_html}
        <li class="nav-only-mobile"><a href="login.html">Log in</a></li>
        <li class="nav-only-mobile"><a href="register.html">Sign up</a></li>
      </ul>

      <div class="nav-actions">
        <button class="theme-toggle" type="button" aria-label="Toggle dark mode" aria-pressed="false">
          {icon('sun')}
          {icon('moon')}
        </button>
        <a href="login.html" class="btn btn-secondary btn-sm hide-mobile">Log in</a>
        <a href="register.html" class="btn btn-primary btn-sm hide-mobile">Sign up</a>
        <button class="hamburger" type="button" aria-label="Open menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </nav>
  </header>"""

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
def footer():
    return f"""<footer class="site-footer">
    <div class="container footer-top">
      <div class="footer-brand">
        <a href="index.html" class="brand" style="color:var(--peach);margin-bottom:1rem;">
          <span class="brand-mark" aria-hidden="true"></span> Astra
        </a>
        <p>A calm, focused place to train algorithmic thinking &mdash; problems, timed contests, and ratings that track real progress.</p>
        <div class="social-row">
          <a href="https://discord.com" target="_blank" rel="noopener" aria-label="Astra on Discord">{icon('discord')}</a>
          <a href="https://github.com" target="_blank" rel="noopener" aria-label="Astra on GitHub">{icon('github')}</a>
          <a href="https://youtube.com" target="_blank" rel="noopener" aria-label="Astra on YouTube">{icon('youtube')}</a>
          <a href="https://x.com" target="_blank" rel="noopener" aria-label="Astra on X">{icon('x')}</a>
        </div>
      </div>

      <div>
        <h4>Platform</h4>
        <ul>
          <li><a href="problems.html">Problemset</a></li>
          <li><a href="contests.html">Contests</a></li>
          <li><a href="gym.html">Gym &amp; practice</a></li>
          <li><a href="rankings.html">Rankings</a></li>
        </ul>
      </div>

      <div>
        <h4>Resources</h4>
        <ul>
          <li><a href="guide.html">Guide</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="about.html">About Astra</a></li>
        </ul>
      </div>

      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">Our mission</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="contact.html">Report an issue</a></li>
          <li><a href="contact.html">Propose a problem</a></li>
        </ul>
      </div>

      <div>
        <h4>Mission control</h4>
        <p style="font-size:0.85rem;">Get one email a week: new problems, contest reminders, editorial highlights.</p>
        <form class="newsletter-form" data-validate novalidate>
          <div class="form-row" style="flex:1;min-width:180px;margin-bottom:0;">
            <input type="email" placeholder="you@domain.com" required aria-label="Email address" />
            <span class="error-msg"></span>
          </div>
          <button class="btn btn-primary btn-sm" type="submit">Subscribe</button>
        </form>
        <div class="form-success" style="margin-top:0.8rem;">{icon('check-shield')} You're on the list.</div>
        <div class="footer-map" style="margin-top:1.2rem;">
          <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=106.62%2C10.75%2C106.72%2C10.82&amp;layer=mapnik" title="Astra HQ location map" loading="lazy"></iframe>
        </div>
      </div>
    </div>

    <div class="container footer-bottom">
      <span>&copy; <span data-year>2026</span> Astra. All systems nominal.</span>
      <div class="footer-bottom-links">
        <a href="faq.html">Privacy</a>
        <a href="faq.html">Terms</a>
        <a href="contact.html">Contact</a>
      </div>
    </div>
  </footer>

  <button class="back-to-top" type="button" aria-label="Back to top">{icon('arrow-up')}</button>
  <script src="js/main.js"></script>"""

def page(title, description, active, main_html, extra_head="", body_class=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  {head(title, description)}
  {extra_head}
</head>
<body class="{body_class}">
  {header(active)}
  {main_html}
  {footer()}
</body>
</html>"""

def write(filename, content):
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", filename)

print("build.py helpers loaded")
