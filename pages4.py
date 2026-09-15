# -*- coding: utf-8 -*-
from scripts.build import head, header, footer, page, write, icon

# ===========================================================================
# CONTACT — contact.html
# ===========================================================================
contact_main = f"""<main>
  <div class="page-header">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Contact</div>
      <h1 style="color:var(--peach);">Talk to us</h1>
      <p style="max-width:58ch;">Account issues, a broken test case, a problem you'd like to contribute, or just something on your mind &mdash; we read every message.</p>
    </div>
  </div>

  <section class="section" style="padding-top:2.5rem;">
    <div class="container two-col" style="align-items:start;">
      <div class="form-panel">
        <div class="form-success">{icon('check-shield')} Message sent &mdash; we'll reply within two business days.</div>
        <form data-validate novalidate>
          <div class="form-two-col">
            <div class="form-row">
              <label for="fname">First name</label>
              <input type="text" id="fname" required />
              <span class="error-msg"></span>
            </div>
            <div class="form-row">
              <label for="lname">Last name</label>
              <input type="text" id="lname" required />
              <span class="error-msg"></span>
            </div>
          </div>
          <div class="form-row">
            <label for="cemail">Email address</label>
            <input type="email" id="cemail" required />
            <span class="error-msg"></span>
          </div>
          <div class="form-row">
            <label for="ctopic">Topic</label>
            <select id="ctopic">
              <option>Account issue</option>
              <option>Report a test case</option>
              <option>Propose a problem</option>
              <option>Team &amp; coaching plans</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="form-row">
            <label for="cmessage">Message</label>
            <textarea id="cmessage" required placeholder="Tell us what's going on&hellip;"></textarea>
            <span class="error-msg"></span>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Send message</button>
        </form>
      </div>

      <div>
        <h3>Other ways to reach us</h3>
        <div class="card" style="margin-bottom:1rem;">
          <h4 style="margin-bottom:0.3rem;">Email</h4>
          <p style="margin-bottom:0;">hello@astra.dev &mdash; general questions and partnerships.</p>
        </div>
        <div class="card" style="margin-bottom:1rem;">
          <h4 style="margin-bottom:0.3rem;">Discord</h4>
          <p style="margin-bottom:0;">The fastest way to get help from setters and the community directly.</p>
        </div>
        <div class="card">
          <h4 style="margin-bottom:0.6rem;">Find us</h4>
          <div class="footer-map" style="filter:none;">
            <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=106.62%2C10.75%2C106.72%2C10.82&amp;layer=mapnik" title="Astra HQ location map" loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>"""

write("contact.html", page(
    "Contact",
    "Contact Astra: report an issue, propose a problem, or reach the team about coaching and team plans.",
    "", contact_main
))

# ===========================================================================
# LOGIN — login.html
# ===========================================================================
def auth_visual():
    return """<div class="hero-visual" aria-hidden="true">
        <div class="orbit-ring r1"></div>
        <div class="orbit-ring r2"></div>
        <div class="orbit-ring r3"></div>
        <div class="planet-core"></div>
        <div class="orbit-node n1">AC</div>
        <div class="orbit-node n2">2100</div>
        <div class="orbit-node n3">#12</div>
        <div class="orbit-node n4">WA</div>
      </div>"""

login_main = f"""<main>
  <div class="auth-shell">
    <div class="auth-visual">
      {auth_visual()}
    </div>
    <div class="auth-form-side">
      <div class="auth-box">
        <span class="eyebrow">Welcome back</span>
        <h1 style="font-size:2rem;">Log in to Astra</h1>
        <p>Pick up your streak where you left off.</p>

        <div class="form-success">{icon('check-shield')} Logged in &mdash; redirecting to your dashboard.</div>
        <form data-validate novalidate>
          <div class="form-row">
            <label for="lemail">Handle or email</label>
            <input type="text" id="lemail" required />
            <span class="error-msg"></span>
          </div>
          <div class="form-row">
            <label for="lpass">Password</label>
            <input type="password" id="lpass" required />
            <span class="error-msg"></span>
          </div>
          <div class="flex-between" style="margin-bottom:1.4rem;font-size:0.85rem;">
            <label style="display:flex;align-items:center;gap:0.5em;font-weight:400;"><input type="checkbox" style="width:auto;" /> Remember me</label>
            <a href="#" style="color:var(--accent-2);">Forgot password?</a>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Log in</button>
        </form>

        <div class="divider-or">or continue with</div>
        <div class="oauth-row">
          <button class="oauth-btn" type="button">GitHub</button>
          <button class="oauth-btn" type="button">Google</button>
        </div>

        <p class="auth-switch">New to Astra? <a href="register.html">Create a free account</a></p>
      </div>
    </div>
  </div>
</main>"""

write("login.html", page(
    "Log in",
    "Log in to your Astra account to submit solutions, join contests, and track your rating.",
    "", login_main
))

# ===========================================================================
# REGISTER — register.html
# ===========================================================================
register_main = f"""<main>
  <div class="auth-shell">
    <div class="auth-visual">
      {auth_visual()}
    </div>
    <div class="auth-form-side">
      <div class="auth-box">
        <span class="eyebrow">Join for free</span>
        <h1 style="font-size:2rem;">Create your account</h1>
        <p>No credit card. Just pick a handle and start solving.</p>

        <div class="form-success">{icon('check-shield')} Account created &mdash; check your inbox to verify.</div>
        <form data-validate novalidate>
          <div class="form-row">
            <label for="rhandle">Handle</label>
            <input type="text" id="rhandle" required placeholder="e.g. star_hunter" />
            <span class="error-msg"></span>
          </div>
          <div class="form-row">
            <label for="remail">Email address</label>
            <input type="email" id="remail" required />
            <span class="error-msg"></span>
          </div>
          <div class="form-two-col">
            <div class="form-row">
              <label for="rpass">Password</label>
              <input type="password" id="rpass" required />
              <span class="error-msg"></span>
            </div>
            <div class="form-row">
              <label for="rpass2">Confirm password</label>
              <input type="password" id="rpass2" required data-match="rpass" />
              <span class="error-msg"></span>
            </div>
          </div>
          <div class="form-row" style="flex-direction:row;align-items:flex-start;gap:0.6em;">
            <input type="checkbox" id="rterms" required style="width:auto;margin-top:0.2em;" />
            <label for="rterms" style="font-weight:400;">I agree to the <a href="faq.html" style="color:var(--accent-2);">Terms</a> and <a href="faq.html" style="color:var(--accent-2);">Privacy Policy</a>.</label>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Create free account</button>
        </form>

        <div class="divider-or">or continue with</div>
        <div class="oauth-row">
          <button class="oauth-btn" type="button">GitHub</button>
          <button class="oauth-btn" type="button">Google</button>
        </div>

        <p class="auth-switch">Already have an account? <a href="login.html">Log in</a></p>
      </div>
    </div>
  </div>
</main>"""

write("register.html", page(
    "Sign up",
    "Create a free Astra account to access the full problemset, rated contests, and rankings.",
    "", register_main
))

# ===========================================================================
# 404 — 404.html
# ===========================================================================
notfound_main = f"""<main>
  <section class="hero" style="min-height:80svh;">
    <div class="container center-text" style="max-width:560px;margin-inline:auto;">
      <span class="hero-kicker">{icon('star')} Signal lost</span>
      <h1 style="color:var(--peach);font-size:clamp(2.4rem,7vw,4rem);">404: out of orbit</h1>
      <p class="hero-lede" style="margin-inline:auto;">This page drifted off the map, or the link was never quite right. Let's get you back to solid ground.</p>
      <div class="hero-actions" style="justify-content:center;">
        <a href="index.html" class="btn btn-primary">Back to home</a>
        <a href="problems.html" class="btn btn-ghost">Browse problems</a>
      </div>
    </div>
  </section>
</main>"""

write("404.html", page(
    "Page not found",
    "This page could not be found on Astra.",
    "", notfound_main
))
