# -*- coding: utf-8 -*-
from scripts.build import head, header, footer, page, write, icon

# ===========================================================================
# HOME — index.html
# ===========================================================================
home_main = f"""<main>
  <!-- HERO ================================================================= -->
  <section class="hero">
    <div class="container hero-grid">
      <div class="hero-content">
        <span class="hero-kicker">{icon('star')} Season 4 rating reset &mdash; now live</span>
        <h1>May the system<br/>test be <em>with</em> you.</h1>
        <p class="hero-tagline">For the benefit of all.</p>
        <p class="hero-lede">Astra is a free training ground for algorithmic thinking: a deep problemset, timed rated contests, and a rating that actually reflects how you solve &mdash; not just what you memorised.</p>
        <div class="hero-actions">
          <a href="register.html" class="btn btn-primary">Start solving &mdash; it's free</a>
          <a href="contests.html" class="btn btn-ghost">See upcoming contests</a>
        </div>
        <div class="hero-meta">
          <div><strong data-count-to="14200" data-suffix="+">0</strong><span>Problems solved today</span></div>
          <div><strong data-count-to="382" data-suffix="">0</strong><span>Rated contests run</span></div>
          <div><strong data-count-to="61" data-suffix="k">0</strong><span>Registered coders</span></div>
        </div>
      </div>

      <div class="hero-visual" aria-hidden="true">
        <div class="orbit-ring r1"></div>
        <div class="orbit-ring r2"></div>
        <div class="orbit-ring r3"></div>
        <div class="planet-core"></div>
        <div class="orbit-node n1">DP</div>
        <div class="orbit-node n2">1900</div>
        <div class="orbit-node n3">A+B</div>
        <div class="orbit-node n4">#4</div>
      </div>
    </div>
  </section>

  <!-- FEATURE CARDS ========================================================= -->
  <section class="section">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">Why Astra</span>
        <h2>Everything a training ground needs, nothing it doesn't</h2>
        <p style="margin-inline:auto;">No clutter, no paywalled editorials, no dark patterns. Just a clean judge, honest ratings, and problems worth your time.</p>
      </div>
      <div class="grid grid-4">
        <div class="card">
          <div class="card-icon">{icon('code')}</div>
          <h3>2,600+ problems</h3>
          <p>Sorted by difficulty and topic, from your first loop to segment trees with lazy propagation.</p>
        </div>
        <div class="card">
          <div class="card-icon">{icon('trophy')}</div>
          <h3>Weekly rated rounds</h3>
          <p>Div. 1 and Div. 2 rounds every week, ICPC and OI formats, real-time standings and hacks.</p>
        </div>
        <div class="card">
          <div class="card-icon">{icon('chart')}</div>
          <h3>A rating worth earning</h3>
          <p>Astra's rating system rewards consistent solving over lucky guesses &mdash; and it's public.</p>
        </div>
        <div class="card">
          <div class="card-icon">{icon('dumbbell')}</div>
          <h3>Gym &amp; mashups</h3>
          <p>Build your own practice sets from past rounds, or drop into an unrated virtual contest any time.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FEATURED CONTEST ====================================================== -->
  <section class="section section-oxford">
    <div class="container two-col">
      <div>
        <span class="eyebrow" style="color:var(--sandy)">Featured contest</span>
        <h2 style="color:var(--peach)">Astra Round 118 (Div. 1 + Div. 2)</h2>
        <p>Six problems, two hours, one shared standings page. Div. 2 problems double as the tail of Div. 1, so everyone lands on a fair curve regardless of rating.</p>
        <div class="hero-meta" style="margin-top:1.6rem;">
          <div><strong style="color:var(--peach)">Oct 17</strong><span>Starts 21:35 ICT</span></div>
          <div><strong style="color:var(--peach)">02:00</strong><span>Duration</span></div>
          <div><strong style="color:var(--peach)">Rated</strong><span>Up to 3000</span></div>
        </div>
        <div class="hero-actions">
          <a href="contest.html" class="btn btn-primary">Register for round</a>
          <a href="contests.html" class="btn btn-ghost">View all contests</a>
        </div>
      </div>
      <div class="code-window">
        <div class="code-bar"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
        <pre><span class="c-com">// C. Deranged Calculator &mdash; 1900</span>
<span class="c-kw">#include</span> <span class="c-str">&lt;bits/stdc++.h&gt;</span>
<span class="c-kw">using namespace</span> std;

<span class="c-kw">int</span> main() {{
    <span class="c-kw">int</span> l, r; cin &gt;&gt; l &gt;&gt; r;
    <span class="c-kw">for</span> (<span class="c-kw">int</span> i = l; i &lt;= r; i++)
        cout &lt;&lt; i &lt;&lt; <span class="c-str">" "</span>;
    <span class="c-kw">return</span> 0;
}}</pre>
      </div>
    </div>
  </section>

  <!-- PROBLEM PREVIEW ======================================================= -->
  <section class="section">
    <div class="container">
      <div class="flex-between section-head" style="margin-bottom:1.6rem;">
        <div>
          <span class="eyebrow">Fresh off the queue</span>
          <h2 class="mt-0">Recently added problems</h2>
        </div>
        <a href="problems.html" class="btn btn-secondary btn-sm">Browse full problemset</a>
      </div>
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>#</th><th>Problem</th><th>Topics</th><th>Difficulty</th><th>Solved</th></tr></thead>
          <tbody>
            <tr><td>2264F</td><td><a class="problem-link" href="problem-detail.html">Deranged Calculator</a></td><td><span class="tag">math</span><span class="tag">implementation</span></td><td><span class="pill pill-medium">1900</span></td><td>1,112</td></tr>
            <tr><td>2264D</td><td><a class="problem-link" href="problem-detail.html">Dr. Agos's Dark Mode</a></td><td><span class="tag">brute force</span><span class="tag">strings</span></td><td><span class="pill pill-easy">1400</span></td><td>4,027</td></tr>
            <tr><td>2263B</td><td><a class="problem-link" href="problem-detail.html">Min Matrices</a></td><td><span class="tag">constructive</span></td><td><span class="pill pill-medium">1700</span></td><td>10,410</td></tr>
            <tr><td>2262E</td><td><a class="problem-link" href="problem-detail.html">Paired Bracket Sequences</a></td><td><span class="tag">combinatorics</span><span class="tag">math</span></td><td><span class="pill pill-hard">2200</span></td><td>72</td></tr>
            <tr><td>2260G</td><td><a class="problem-link" href="problem-detail.html">Sortable Permutations</a></td><td><span class="tag">number theory</span></td><td><span class="pill pill-hard">2400</span></td><td>172</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- STATS STRIP ============================================================ -->
  <section class="section section-oxford">
    <div class="container">
      <div class="stats-strip">
        <div><span class="stat-num" data-count-to="2634">0</span><span class="stat-label">Problems in the archive</span></div>
        <div><span class="stat-num" data-count-to="61400" data-suffix="+">0</span><span class="stat-label">Registered accounts</span></div>
        <div><span class="stat-num" data-count-to="382">0</span><span class="stat-label">Rated rounds hosted</span></div>
        <div><span class="stat-num" data-count-to="3810">0</span><span class="stat-label">Highest live rating</span></div>
      </div>
    </div>
  </section>

  <!-- HOW IT WORKS =========================================================== -->
  <section class="section">
    <div class="container two-col">
      <div>
        <span class="eyebrow">How it works</span>
        <h2>From account to first accepted verdict in four steps</h2>
        <p>No setup fees, no credit card. Just a judge, a queue, and your next submission.</p>
        <div class="hero-actions">
          <a href="guide.html" class="btn btn-secondary">Read the full guide</a>
        </div>
      </div>
      <div class="step-list">
        <div class="step-item">
          <div class="step-num">1</div>
          <div><h4>Create your account</h4><p>Pick a handle &mdash; it's how the whole community will know you on standings pages.</p></div>
        </div>
        <div class="step-item">
          <div class="step-num">2</div>
          <div><h4>Warm up in the Gym</h4><p>Unrated practice sets and past-round mashups let you calibrate before you compete.</p></div>
        </div>
        <div class="step-item">
          <div class="step-num">3</div>
          <div><h4>Register for a round</h4><p>Div. 1, Div. 2, or combined &mdash; rounds run weekly, and registration takes ten seconds.</p></div>
        </div>
        <div class="step-item">
          <div class="step-num">4</div>
          <div><h4>Submit &amp; climb</h4><p>Get instant verdicts, read editorials afterward, and watch your rating move.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- TESTIMONIAL / SOCIAL PROOF ============================================= -->
  <section class="section section-alt">
    <div class="container">
      <div class="grid grid-3">
        <div class="card">
          <p style="font-family:var(--font-display);font-style:italic;font-size:1.05rem;color:var(--text);">&ldquo;Astra's editorials are the first ones I've read all the way through. They explain the <em>why</em>, not just the code.&rdquo;</p>
          <div class="flex-between" style="margin-top:1.2rem;">
            <strong style="font-size:0.9rem;">@heuristica</strong><span class="pill pill-hard">3322</span>
          </div>
        </div>
        <div class="card">
          <p style="font-family:var(--font-display);font-style:italic;font-size:1.05rem;color:var(--text);">&ldquo;I moved from Div. 2 to Div. 1 in four months of weekly rounds. The Gym practice sets made the difference.&rdquo;</p>
          <div class="flex-between" style="margin-top:1.2rem;">
            <strong style="font-size:0.9rem;">@maroonrk</strong><span class="pill pill-medium">1780</span>
          </div>
        </div>
        <div class="card">
          <p style="font-family:var(--font-display);font-style:italic;font-size:1.05rem;color:var(--text);">&ldquo;It's rare to find a judge this fast and this uncluttered. Submissions come back in under a second.&rdquo;</p>
          <div class="flex-between" style="margin-top:1.2rem;">
            <strong style="font-size:0.9rem;">@turmax</strong><span class="pill pill-hard">2950</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA ===================================================================== -->
  <section class="section">
    <div class="container center-text" style="max-width:640px;">
      <h2>Your first accepted verdict is a few clicks away.</h2>
      <p style="margin-inline:auto;">Join for free and get a starting problem set matched to your first placement round.</p>
      <div class="hero-actions" style="justify-content:center;">
        <a href="register.html" class="btn btn-primary">Create free account</a>
        <a href="pricing.html" class="btn btn-secondary">Compare plans</a>
      </div>
    </div>
  </section>
</main>"""

write("index.html", page(
    "Home",
    "Astra is a free competitive programming platform: problems, rated contests, and rankings for training algorithmic thinking.",
    "", home_main
))
