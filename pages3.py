# -*- coding: utf-8 -*-
from scripts.build import head, header, footer, page, write, icon

# ===========================================================================
# RANKINGS — rankings.html
# ===========================================================================
RANKS = [
    ("jiangly", "VN", 3810, 198),
    ("Kevin114514", "VN", 3655, 114),
    ("Benq", "US", 3650, 168),
    ("maroonrk", "JP", 3427, 216),
    ("strapple", "VN", 3413, 69),
    ("Um_nik", "GB", 3387, 308),
    ("heuristica", "FI", 3322, 69),
    ("tourist", "BY", 3301, 307),
    ("turmax", "VN", 3297, 124),
    ("squareOf105", "VN", 3262, 20),
]
rank_rows = []
for i, (name, cc, rating, wins) in enumerate(RANKS, start=1):
    rc = f" rank-{i}" if i <= 3 else ""
    rank_rows.append(f'<tr><td class="rank-cell{rc}">{i}</td><td><a class="problem-link" href="#">{name}</a></td><td>{cc}</td><td>{rating}</td><td>{wins}</td></tr>')
rank_rows_html = "\n            ".join(rank_rows)

rankings_main = f"""<main>
  <div class="page-header">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Rankings</div>
      <h1 style="color:var(--peach);">Rankings</h1>
      <p style="max-width:60ch;">Live ratings across every coder active in the last six months. Ratings update within minutes of a round's system tests finishing.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container">
      <div class="filters-bar">
        <select aria-label="Filter by country"><option>Any country</option><option>Vietnam</option><option>Japan</option><option>United States</option></select>
        <select aria-label="Filter by organization"><option>Any organization</option><option>UIT</option><option>MIT</option><option>Tokyo Univ.</option></select>
        <input type="text" placeholder="Search handle&hellip;" />
        <button class="btn btn-primary btn-sm" type="button">Filter</button>
      </div>
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>Rank</th><th>Handle</th><th>Country</th><th>Rating</th><th>Contests</th></tr></thead>
          <tbody>
            {rank_rows_html}
          </tbody>
        </table>
      </div>

      <div class="grid grid-3" style="margin-top:3rem;">
        <div class="card">
          <h4>Rating bands</h4>
          <p style="font-size:0.9rem;margin-bottom:0.6rem;"><span class="pill pill-easy">&lt;1600</span> Pupil &ndash; Specialist</p>
          <p style="font-size:0.9rem;margin-bottom:0.6rem;"><span class="pill pill-medium">1600&ndash;2400</span> Expert &ndash; Master</p>
          <p style="font-size:0.9rem;margin-bottom:0;"><span class="pill pill-hard">2400+</span> Grandmaster &amp; above</p>
        </div>
        <div class="card">
          <h4>How rating changes</h4>
          <p style="font-size:0.9rem;margin-bottom:0;">Astra uses an Elo-derived system: your expected performance is compared against everyone else in the round, then rating shifts toward the result.</p>
        </div>
        <div class="card">
          <h4>Top contributors</h4>
          <p style="font-size:0.9rem;margin-bottom:0;">Contribution points reward problem-setting, editorial writing, and helpful forum answers &mdash; separate from rating entirely.</p>
        </div>
      </div>
    </div>
  </section>
</main>"""

write("rankings.html", page(
    "Rankings",
    "Astra's live rating leaderboard: top coders ranked by rating across the last six months of contests.",
    "rankings.html", rankings_main
))

# ===========================================================================
# PRICING — pricing.html
# ===========================================================================
pricing_main = f"""<main>
  <div class="page-header">
    <div class="container center-text">
      <div class="breadcrumb" style="justify-content:center;display:flex;"><a href="index.html">Home</a>&nbsp;/&nbsp;Pricing</div>
      <h1 style="color:var(--peach);">Simple, honest pricing</h1>
      <p style="max-width:56ch;margin-inline:auto;">Every problem, every contest, and every rating point is free, forever. Orbit is for teams and coaches who want more structure.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container">
      <div class="pricing-grid">
        <div class="price-card">
          <span class="eyebrow">Cadet</span>
          <h3>Free</h3>
          <p class="price-amount">$0<span>/forever</span></p>
          <ul class="price-list">
            <li>Full problemset access</li>
            <li>Weekly rated contests</li>
            <li>Public rating &amp; standings</li>
            <li>Unlimited Gym practice</li>
            <li>Community forum access</li>
          </ul>
          <a href="register.html" class="btn btn-secondary btn-block">Start for free</a>
        </div>

        <div class="price-card featured">
          <span class="price-badge">Most popular</span>
          <span class="eyebrow">Orbit</span>
          <h3>For serious training</h3>
          <p class="price-amount">$6<span>/month</span></p>
          <ul class="price-list">
            <li>Everything in Cadet</li>
            <li>Personalised problem recommendations</li>
            <li>Submission analytics &amp; heatmaps</li>
            <li>Early access to new rounds</li>
            <li>Priority judge queue</li>
            <li>Ad-free interface</li>
          </ul>
          <a href="register.html" class="btn btn-primary btn-block">Start 14-day trial</a>
        </div>

        <div class="price-card">
          <span class="eyebrow">Mission Control</span>
          <h3>For teams &amp; coaches</h3>
          <p class="price-amount">$24<span>/month</span></p>
          <ul class="price-list">
            <li>Everything in Orbit</li>
            <li>Private mashups for your team</li>
            <li>Coach dashboard &amp; progress tracking</li>
            <li>Custom contest hosting</li>
            <li>Dedicated support channel</li>
          </ul>
          <a href="contact.html" class="btn btn-secondary btn-block">Talk to us</a>
        </div>
      </div>

      <p class="center-text" style="margin-top:2.2rem;font-size:0.85rem;">All plans include the same judge, the same problems, and the same ratings. Paid tiers fund servers and new problem development &mdash; nothing here is pay-to-win.</p>
    </div>
  </section>
</main>"""

write("pricing.html", page(
    "Pricing",
    "Astra pricing: a free tier with full access to problems and contests, plus optional Orbit and Mission Control plans.",
    "pricing.html", pricing_main
))

# ===========================================================================
# ABOUT — about.html
# ===========================================================================
about_main = f"""<main>
  <div class="page-header">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / About</div>
      <h1 style="color:var(--peach);">Built by people who missed their own bus stop debugging a segment tree.</h1>
      <p style="max-width:62ch;">Astra started as a study group's shared problemset and grew into a full judge because we couldn't find one that felt this calm.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container two-col">
      <div>
        <span class="eyebrow">Our mission</span>
        <h2>For the benefit of all</h2>
        <p>Astra exists so that anyone &mdash; regardless of where they study or whether they can afford a bootcamp &mdash; has a free, reliable place to build real algorithmic intuition. The roadmap is deliberately narrow: master the fundamentals before chasing exotic techniques, because that's what actually shows up in contests.</p>
        <p>We keep the judge fast, the interface quiet, and the editorials honest about why a solution works, not just that it does.</p>
      </div>
      <div class="code-window">
        <div class="code-bar"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
        <pre><span class="c-com">// Astra's founding principle</span>
<span class="c-kw">while</span> (coder.keeps_trying()) {{
    judge.give_instant_feedback();
    community.share_what_it_learned();
}}
<span class="c-com">// &mdash; for the benefit of all</span></pre>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">What we stand for</span>
        <h2>Three things we won't compromise on</h2>
      </div>
      <div class="grid grid-3">
        <div class="card">
          <div class="card-icon">{icon('check-shield')}</div>
          <h3>Fair judging</h3>
          <p>Same compiler flags, same time limits, same queue for everyone &mdash; rating means the same thing whoever earned it.</p>
        </div>
        <div class="card">
          <div class="card-icon">{icon('users')}</div>
          <h3>Open to everyone</h3>
          <p>Statements ship in multiple languages, the core problemset stays free, and volunteer setters come from every skill level.</p>
        </div>
        <div class="card">
          <div class="card-icon">{icon('trophy')}</div>
          <h3>Fundamentals first</h3>
          <p>We'd rather teach one technique ten thousand times than ten techniques once. That's what actually improves contest performance.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">The crew</span>
        <h2>A small, mostly-nocturnal team</h2>
      </div>
      <div class="grid grid-4">
        <div class="card center-text">
          <img src="https://i.pravatar.cc/120?img=13" alt="Portrait of Astra founder" style="border-radius:50%;width:80px;margin-inline:auto 0.8rem;" />
          <h4 style="margin-bottom:0.1rem;">letterc67</h4>
          <p style="font-size:0.82rem;">Founder &amp; problem setter</p>
        </div>
        <div class="card center-text">
          <img src="https://i.pravatar.cc/120?img=33" alt="Portrait of a team member" style="border-radius:50%;width:80px;margin-inline:auto 0.8rem;" />
          <h4 style="margin-bottom:0.1rem;">Legoshi</h4>
          <p style="font-size:0.82rem;">Judge infrastructure</p>
        </div>
        <div class="card center-text">
          <img src="https://i.pravatar.cc/120?img=48" alt="Portrait of a team member" style="border-radius:50%;width:80px;margin-inline:auto 0.8rem;" />
          <h4 style="margin-bottom:0.1rem;">Sherwin</h4>
          <p style="font-size:0.82rem;">Editorials &amp; content</p>
        </div>
        <div class="card center-text">
          <img src="https://i.pravatar.cc/120?img=21" alt="Portrait of a team member" style="border-radius:50%;width:80px;margin-inline:auto 0.8rem;" />
          <h4 style="margin-bottom:0.1rem;">Cerq</h4>
          <p style="font-size:0.82rem;">Community &amp; moderation</p>
        </div>
      </div>
    </div>
  </section>
</main>"""

write("about.html", page(
    "About",
    "About Astra: our mission to provide a free, fair competitive programming platform for everyone.",
    "about.html", about_main
))

# ===========================================================================
# GUIDE — guide.html
# ===========================================================================
guide_main = f"""<main>
  <div class="page-header">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Guide</div>
      <h1 style="color:var(--peach);">The Astra guide</h1>
      <p style="max-width:60ch;">Everything you need before your first contest: setting up your environment, understanding the roadmap, and reading a problem statement properly.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container two-col" style="align-items:start;">
      <aside>
        <div class="card">
          <h4>On this page</h4>
          <ul style="display:flex;flex-direction:column;gap:0.7rem;font-size:0.9rem;">
            <li><a href="#environment" style="color:var(--accent-2);">Setting up your environment</a></li>
            <li><a href="#account" style="color:var(--accent-2);">Your account &amp; handle</a></li>
            <li><a href="#roadmap" style="color:var(--accent-2);">Following the roadmap</a></li>
            <li><a href="#reading" style="color:var(--accent-2);">Reading a problem statement</a></li>
            <li><a href="#submit" style="color:var(--accent-2);">Submitting &amp; verdicts</a></li>
          </ul>
        </div>
      </aside>

      <div>
        <h3 id="environment">Setting up your environment</h3>
        <p>Astra's judge supports C++20, Python 3.12, Java 21, and Rust. You can write directly in the browser editor, or set up a local environment and paste your solution in before submitting &mdash; both are equally valid.</p>

        <h3 id="account">Your account &amp; handle</h3>
        <p>Your handle is permanent and public: it appears on every standings page you ever compete in. Pick something you won't mind explaining to a future interviewer.</p>

        <h3 id="roadmap">Following the roadmap</h3>
        <p>The Roadmap orders topics by how often they appear in real contests, not by how interesting they are to teach. Work through Basic, Sorting, and Two Pointers before touching Segment Trees &mdash; the fundamentals compound.</p>

        <h3 id="reading">Reading a problem statement</h3>
        <div class="step-list">
          <div class="step-item">
            <div class="step-num">1</div>
            <div><h4>Read the constraints first</h4><p>Input size tells you the expected time complexity before you've even understood the problem.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num">2</div>
            <div><h4>Work the example by hand</h4><p>If you can't reproduce the sample output manually, you don't understand the problem yet.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num">3</div>
            <div><h4>Write pseudocode before code</h4><p>Ten minutes of planning saves an hour of debugging a wrong approach.</p></div>
          </div>
        </div>

        <h3 id="submit" style="margin-top:2rem;">Submitting &amp; verdicts</h3>
        <p>Every submission runs against the full test set before you see a verdict &mdash; no partial hints, no peeking at which test failed during a rated round. After the round ends, failed submissions show exactly which test broke them.</p>
      </div>
    </div>
  </section>
</main>"""

write("guide.html", page(
    "Guide",
    "The Astra guide: environment setup, account basics, the learning roadmap, and how to read a problem statement.",
    "guide.html", guide_main
))

# ===========================================================================
# FAQ — faq.html
# ===========================================================================
FAQS = [
    ("Is Astra really free?", "Yes. Every problem, every rated contest, and your rating history are free permanently. Orbit and Mission Control are optional paid tiers for extra tooling, not a paywall on the core judge."),
    ("What languages can I submit in?", "C++20, Python 3.12, Java 21, and Rust are supported today, with the same time and memory limits applied fairly across languages after standard scaling."),
    ("How is my rating calculated?", "Astra uses an Elo-derived system similar to other major judges: your performance in a round is compared to your rating-implied expectation, and your rating shifts toward the gap."),
    ("Can I participate after a contest ends?", "Yes, through Virtual Participation. You get the original problems and time limit, but the run is unrated and doesn't affect your public standing."),
    ("How do I report a wrong test case?", "Open the problem page and use the report link, or email us directly from the Contact page. Setters review reports within a few days."),
    ("Can I propose my own problems?", "We welcome community-authored problems. Reach out via Contact with a draft statement and we'll walk you through the review process."),
]
faq_items = "\n        ".join(
    f'''<div class="faq-item">
          <button class="faq-q" aria-expanded="false">{q}<span class="plus" aria-hidden="true"></span></button>
          <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
        </div>'''
    for q, a in FAQS
)

faq_main = f"""<main>
  <div class="page-header">
    <div class="container center-text">
      <div class="breadcrumb" style="justify-content:center;display:flex;"><a href="index.html">Home</a>&nbsp;/&nbsp;FAQ</div>
      <h1 style="color:var(--peach);">Frequently asked questions</h1>
      <p style="max-width:56ch;margin-inline:auto;">Can't find your answer here? The <a href="contact.html" style="color:var(--sandy);">Contact page</a> reaches us directly.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container">
      <div class="faq-list">
        {faq_items}
      </div>
    </div>
  </section>
</main>"""

write("faq.html", page(
    "FAQ",
    "Frequently asked questions about Astra: pricing, supported languages, rating calculation, and problem reports.",
    "faq.html", faq_main
))
