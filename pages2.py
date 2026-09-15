# -*- coding: utf-8 -*-
from scripts.build import head, header, footer, page, write, icon

# ===========================================================================
# PROBLEMS — problems.html
# ===========================================================================
def diff_pill(v):
    v = int(v)
    if v < 1400: return f'<span class="pill pill-easy">{v}</span>'
    if v < 2100: return f'<span class="pill pill-medium">{v}</span>'
    return f'<span class="pill pill-hard">{v}</span>'

PROBLEMS = [
    ("2264F", "Deranged Calculator", ["math", "constructive"], 1900, "62.4%"),
    ("2264E2", "A Prime Flood (Hard Version)", ["combinatorics", "dp"], 2600, "8.1%"),
    ("2264E1", "A Prime Flood (Easy Version)", ["combinatorics", "dp"], 2100, "21.7%"),
    ("2264D", "Dr. Agos's Dark Mode", ["brute force", "strings"], 1400, "58.9%"),
    ("2264C", "Madamant's Skating Dynasty", ["combinatorics", "sortings"], 1600, "44.2%"),
    ("2264B", "Knife's Pill Farm", ["data structures", "greedy"], 1300, "67.0%"),
    ("2264A", "Rumb Needs a Hand", ["implementation", "two pointers"], 900, "88.4%"),
    ("2263B", "Min Matrices", ["constructive algorithms"], 1700, "39.6%"),
    ("2263A", "Min Max Game", ["greedy"], 1100, "74.3%"),
    ("2262F", "Rank Removal", ["math"], 2500, "6.4%"),
    ("2262E", "Paired Bracket Sequences", ["combinatorics", "math"], 2200, "12.9%"),
    ("2262D", "PLUSworld", ["graphs", "greedy"], 2000, "18.5%"),
    ("2262C", "Traveling the World", ["graphs", "math"], 1800, "31.2%"),
    ("2262B", "Culling Game", ["binary search", "two pointers"], 1500, "49.8%"),
    ("2262A2", "Floor of MEX (Hard Version)", ["dp", "implementation"], 1600, "27.6%"),
    ("2262A1", "Floor of MEX (Easy Version)", ["constructive", "greedy"], 1200, "63.1%"),
    ("499", "Loop", ["basic", "for loops"], 800, "97.6%"),
    ("500", "Even Numbers", ["basic", "math"], 800, "93.4%"),
    ("501", "Factorial", ["math", "recursion"], 800, "89.7%"),
    ("502", "Star Triangle", ["implementation"], 800, "91.2%"),
]

rows = []
for pid, name, tags, diff, solve in PROBLEMS:
    tagstr = "".join(f'<span class="tag">{t}</span>' for t in tags)
    rows.append(f'<tr><td>{pid}</td><td><a class="problem-link" href="problem-detail.html">{name}</a></td><td>{tagstr}</td><td>{diff_pill(diff)}</td><td>{solve}</td></tr>')
rows_html = "\n            ".join(rows)

problems_main = f"""<main>
  <div class="page-header">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Problemset</div>
      <h1 style="color:var(--peach);">Problemset</h1>
      <p style="max-width:60ch;">Every problem Astra has ever run, searchable by topic and difficulty. Solve them rated, inside the Gym, or just for the satisfaction of a clean accepted verdict.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container">
      <form class="filters-bar" data-validate novalidate>
        <input type="text" placeholder="Search by name or number&hellip;" aria-label="Search problems" />
        <select aria-label="Filter by topic">
          <option value="">All topics</option>
          <option>Math</option>
          <option>Dynamic Programming</option>
          <option>Graphs</option>
          <option>Data Structures</option>
          <option>Greedy</option>
          <option>Strings</option>
        </select>
        <input type="number" placeholder="Min rating" style="max-width:120px;" aria-label="Minimum difficulty" />
        <input type="number" placeholder="Max rating" style="max-width:120px;" aria-label="Maximum difficulty" />
        <button class="btn btn-primary btn-sm" type="submit">Apply filters</button>
      </form>

      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>#</th><th>Name</th><th>Topics</th><th>Difficulty</th><th>Solve rate</th></tr></thead>
          <tbody>
            {rows_html}
          </tbody>
        </table>
      </div>

      <div class="flex-between" style="margin-top:1.6rem;">
        <p style="margin:0;font-size:0.85rem;">Showing 20 of 2,634 problems</p>
        <div style="display:flex;gap:0.5rem;">
          <button class="btn btn-secondary btn-sm" type="button" disabled>&larr; Previous</button>
          <button class="btn btn-secondary btn-sm" type="button">Next &rarr;</button>
        </div>
      </div>
    </div>
  </section>
</main>"""

write("problems.html", page(
    "Problemset",
    "Browse Astra's full problemset: 2,600+ algorithmic problems filterable by topic and difficulty rating.",
    "problems.html", problems_main
))

# ===========================================================================
# PROBLEM DETAIL — problem-detail.html
# ===========================================================================
problem_detail_main = f"""<main>
  <div class="page-header" style="padding-bottom:2rem;">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / <a href="problems.html">Problemset</a> / 2264F</div>
      <div class="flex-between">
        <h1 style="color:var(--peach);margin-bottom:0.2rem;">Deranged Calculator</h1>
        <div style="display:flex;gap:0.6rem;flex-wrap:wrap;">
          <span class="pill pill-medium">1900</span>
        </div>
      </div>
      <div style="display:flex;gap:1.6rem;flex-wrap:wrap;margin-top:0.6rem;color:rgba(246,220,172,0.75);font-size:0.9rem;">
        <span>{icon('clock')} Time limit: 2 s</span>
        <span>Memory limit: 256 MB</span>
        <span>62.4% solve rate</span>
      </div>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container two-col" style="align-items:start;">
      <div>
        <div style="display:flex;gap:0.5rem;margin-bottom:1.6rem;border-bottom:1px solid var(--border);">
          <a href="problem-detail.html" class="btn btn-sm" style="border-radius:0;border-bottom:2px solid var(--accent);">Statement</a>
          <a href="#" class="btn btn-sm btn-secondary" style="border:none;">Submit</a>
          <a href="#" class="btn btn-sm btn-secondary" style="border:none;">Submissions</a>
          <a href="#" class="btn btn-sm btn-secondary" style="border:none;">Editorial</a>
        </div>

        <p>Kohaku found an old calculator that has been struck by a strange curse: every button still lights up, but the digits it prints come out in a <strong>deranged</strong> order &mdash; no digit ever lands in its original position.</p>
        <p>You are given two integers <em>l</em> and <em>r</em>. For every integer <em>x</em> with <em>l &le; x &le; r</em>, the calculator prints a permutation of <em>x</em>'s digits with no fixed point, choosing the lexicographically smallest such permutation when one exists. If no valid derangement of the digits exists, the calculator prints <code>-1</code> for that value instead.</p>

        <h3>Input</h3>
        <p>The only line contains two integers <em>l</em> and <em>r</em> (1 &le; <em>l</em> &le; <em>r</em> &le; 10<sup>9</sup>).</p>

        <h3>Output</h3>
        <p>Print <em>r &minus; l + 1</em> lines. The <em>i</em>-th line should contain the calculator's output for <em>x = l + i &minus; 1</em>.</p>

        <h3>Example</h3>
        <div class="code-window">
          <div class="code-bar"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
          <pre>Input:
21 24

Output:
12
-1
32
-1</pre>
        </div>

        <h3 style="margin-top:2rem;">Note</h3>
        <p>For <em>x = 21</em>, swapping the two digits gives <em>12</em>, and neither digit stays in place. For <em>x = 22</em>, every permutation of its digits keeps both 2s fixed, so the answer is <code>-1</code>.</p>
      </div>

      <aside>
        <div class="card" style="margin-bottom:1.2rem;">
          <h4>Submit a solution</h4>
          <form data-validate novalidate>
            <div class="form-row">
              <label for="lang">Language</label>
              <select id="lang">
                <option>C++20</option>
                <option>Python 3</option>
                <option>Java 21</option>
                <option>Rust</option>
              </select>
            </div>
            <div class="form-row">
              <label for="src">Source code</label>
              <textarea id="src" placeholder="Paste your solution&hellip;" required style="min-height:160px;font-family:var(--font-mono);"></textarea>
              <span class="error-msg"></span>
            </div>
            <button type="submit" class="btn btn-primary btn-block">Submit solution</button>
          </form>
          <div class="form-success">{icon('check-shield')} Queued for judging.</div>
        </div>

        <div class="card">
          <h4>Topic tags</h4>
          <div>
            <span class="tag tag-teal">math</span>
            <span class="tag">constructive algorithms</span>
            <span class="tag">implementation</span>
          </div>
          <hr class="divider" style="margin-block:1.2rem;" />
          <h4>Recent AC</h4>
          <p style="font-size:0.85rem;">jiangly &middot; Kevin114514 &middot; Benq &middot; strapple &middot; heuristica</p>
        </div>
      </aside>
    </div>
  </section>
</main>"""

write("problem-detail.html", page(
    "Deranged Calculator &middot; 2264F",
    "Problem 2264F, Deranged Calculator: statement, constraints, and submission panel on Astra.",
    "problems.html", problem_detail_main
))

# ===========================================================================
# CONTESTS — contests.html
# ===========================================================================
past_rounds = [
    ("Astra Round 117 (Div. 2)", "Sep 14, 2026", "02:00", "12,406"),
    ("Astra Round 116 (Div. 1)", "Sep 12, 2026", "03:00", "3,981"),
    ("Educational Round 94", "Sep 08, 2026", "02:00", "9,204"),
    ("Astra Round 115 (Div. 3)", "Sep 05, 2026", "02:15", "18,772"),
    ("Astra Round 114 (Div. 2)", "Aug 29, 2026", "02:00", "13,050"),
    ("Astra Round 113 (Div. 2)", "Aug 17, 2026", "02:00", "11,893"),
]
past_rows = "\n            ".join(
    f'<tr><td><a class="problem-link" href="contest.html">{n}</a></td><td>{d}</td><td>{l}</td><td>{p}</td><td><a href="rankings.html" class="btn btn-sm btn-secondary">Standings</a></td></tr>'
    for n, d, l, p in past_rounds
)

contests_main = f"""<main>
  <div class="page-header">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Contests</div>
      <h1 style="color:var(--peach);">Contests</h1>
      <p style="max-width:60ch;">Rated rounds run weekly. Register ahead of time, or drop in for virtual participation once a round has ended.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container">
      <div class="card" style="border-color:var(--orange);margin-bottom:2.5rem;">
        <div class="flex-between">
          <div>
            <span class="eyebrow">Next up</span>
            <h3 class="mt-0">Astra Round 118 (Div. 1 + Div. 2)</h3>
            <p style="margin-bottom:0;">Starts Oct 17, 2026 &middot; 21:35 ICT &middot; Duration 02:00 &middot; Rated for everyone</p>
          </div>
          <a href="contest.html" class="btn btn-primary">Register</a>
        </div>
      </div>

      <div class="section-head">
        <span class="eyebrow">Archive</span>
        <h2 class="mt-0">Past contests</h2>
      </div>
      <div class="filters-bar">
        <select aria-label="Filter by type"><option>Any format</option><option>Div. 1</option><option>Div. 2</option><option>Div. 3</option><option>Educational</option></select>
        <select aria-label="Filter by rated status"><option>Rated: doesn't matter</option><option>Rated only</option><option>Unrated only</option></select>
        <input type="text" placeholder="Search contest name&hellip;" />
        <button class="btn btn-primary btn-sm" type="button">Filter</button>
      </div>
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>Name</th><th>Date</th><th>Length</th><th>Participants</th><th></th></tr></thead>
          <tbody>
            {past_rows}
          </tbody>
        </table>
      </div>
    </div>
  </section>
</main>"""

write("contests.html", page(
    "Contests",
    "See upcoming rated rounds and browse past Astra contests with standings and participation counts.",
    "contests.html", contests_main
))

# ===========================================================================
# CONTEST DETAIL — contest.html
# ===========================================================================
contest_problems = [
    ("A", "Warm-Up Signal", 800, "18,204"),
    ("B", "Orbit Pairs", 1100, "14,551"),
    ("C", "Deranged Calculator", 1900, "6,204"),
    ("D", "Star Chart Reassembly", 2200, "2,118"),
    ("E", "Meteor Shower DP", 2600, "540"),
    ("F", "Nebula Segment Tree", 3000, "88"),
]
cp_rows = "\n            ".join(
    f'<tr><td class="rank-cell">{i}</td><td><a class="problem-link" href="problem-detail.html">{name}</a></td><td>{diff_pill(d)}</td><td>{s}</td></tr>'
    for i, name, d, s in contest_problems
)

contest_main = f"""<main>
  <div class="page-header">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / <a href="contests.html">Contests</a> / Round 118</div>
      <h1 style="color:var(--peach);">Astra Round 118 (Div. 1 + Div. 2)</h1>
      <div style="display:flex;gap:1.6rem;flex-wrap:wrap;margin-top:0.6rem;color:rgba(246,220,172,0.75);font-size:0.9rem;">
        <span>{icon('clock')} Starts Oct 17, 2026 &middot; 21:35 ICT</span>
        <span>Duration 02:00</span>
        <span>Rated, up to 3000</span>
      </div>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container two-col" style="align-items:start;">
      <div>
        <h3>About this round</h3>
        <p>Six problems shared between Div. 1 and Div. 2: A&ndash;C count toward Div. 2 only, C&ndash;F carry into Div. 1. Standard ICPC scoring, 10-minute penalty per wrong submission, hacks open after the round.</p>

        <h3 style="margin-top:2rem;">Problems</h3>
        <div class="table-wrap">
          <table class="data-table">
            <thead><tr><th>#</th><th>Name</th><th>Difficulty</th><th>Attempts</th></tr></thead>
            <tbody>{cp_rows}</tbody>
          </table>
        </div>

        <h3 style="margin-top:2rem;">Rules</h3>
        <ul style="display:flex;flex-direction:column;gap:0.6rem;color:var(--text-muted);font-size:0.94rem;">
          <li>&mdash; Registration closes 5 minutes before the round starts.</li>
          <li>&mdash; Discussing problems publicly during the round results in disqualification.</li>
          <li>&mdash; Virtual participation opens automatically once the round ends.</li>
        </ul>
      </div>

      <aside>
        <div class="card">
          <h4>Registration</h4>
          <p style="font-size:0.9rem;">4,208 coders registered so far.</p>
          <div class="avatar-stack" style="margin-bottom:1.2rem;">
            <img src="https://i.pravatar.cc/64?img=12" alt="" />
            <img src="https://i.pravatar.cc/64?img=32" alt="" />
            <img src="https://i.pravatar.cc/64?img=45" alt="" />
            <img src="https://i.pravatar.cc/64?img=8" alt="" />
          </div>
          <a href="register.html" class="btn btn-primary btn-block">Register for round</a>
          <a href="gym.html" class="btn btn-secondary btn-block" style="margin-top:0.7rem;">Practice similar problems</a>
        </div>
      </aside>
    </div>
  </section>
</main>"""

write("contest.html", page(
    "Astra Round 118",
    "Astra Round 118 (Div. 1 + Div. 2): schedule, problem list, and registration.",
    "contests.html", contest_main
))

# ===========================================================================
# GYM — gym.html
# ===========================================================================
gym_items = [
    ("ICPC Regional Training Camp Vol. 3", "10 problems", "5:00:00", "Prepared by NHQ0914"),
    ("Div. 2 Warm-Up Mashup", "6 problems", "2:00:00", "Prepared by Sherwin"),
    ("Segment Trees Deep Dive", "8 problems", "3:30:00", "Prepared by Cerq"),
    ("Beginner Bootcamp Week 1", "12 problems", "4:00:00", "Prepared by harryleee"),
    ("Number Theory Sprint", "7 problems", "2:30:00", "Prepared by tuongll"),
    ("Graph Theory Marathon", "9 problems", "4:30:00", "Prepared by lenhanbo"),
]
gym_cards = "\n        ".join(
    f'''<div class="card">
          <h3 style="font-size:1.05rem;">{n}</h3>
          <p style="font-size:0.88rem;">{c} &middot; {t} duration</p>
          <p style="font-size:0.8rem;color:var(--text-muted);margin-bottom:1.1rem;">{p}</p>
          <a href="contest.html" class="btn btn-secondary btn-sm">Start virtual run</a>
        </div>'''
    for n, c, t, p in gym_items
)

gym_main = f"""<main>
  <div class="page-header">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Gym</div>
      <h1 style="color:var(--peach);">Gym &amp; practice</h1>
      <p style="max-width:60ch;">Unrated training sets built from retired rounds and community mashups. Run them solo or race a friend &mdash; nothing here touches your rating.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container">
      <div class="filters-bar">
        <input type="text" placeholder="Search trainings&hellip;" />
        <select aria-label="Filter by difficulty"><option>Any difficulty</option><option>Beginner</option><option>Intermediate</option><option>Advanced</option></select>
        <select aria-label="Filter by duration"><option>Any duration</option><option>Under 2 hours</option><option>2&ndash;4 hours</option><option>4+ hours</option></select>
        <button class="btn btn-primary btn-sm" type="button">Filter</button>
      </div>

      <div class="grid grid-3">
        {gym_cards}
      </div>

      <div class="section-head center" style="margin-top:3.5rem;">
        <span class="eyebrow">Your own mashup</span>
        <h2>Build a custom practice set</h2>
        <p style="margin-inline:auto;">Pick your own problems, set your own clock, and get a private mashup contest for you and your team.</p>
        <a href="register.html" class="btn btn-primary" style="margin-top:1rem;">Create a mashup</a>
      </div>
    </div>
  </section>
</main>"""

write("gym.html", page(
    "Gym",
    "Astra Gym: unrated practice sets and community mashups built from retired contest problems.",
    "gym.html", gym_main
))
