# Astra

**May the system test be with you. For the benefit of all.**

Astra is a marketing/product site for a competitive programming platform:
problems, rated contests, rankings, and community pages. Built with plain
HTML, CSS, and vanilla JavaScript — no build step, no framework, no
dependencies.

## Structure

```
.
├── index.html            Home
├── problems.html          Problemset (browse + filter)
├── problem-detail.html    Single problem statement + submit panel
├── contests.html          Contest list (upcoming + archive)
├── contest.html           Single contest detail
├── gym.html                Practice / mashups
├── rankings.html           Rating leaderboard
├── pricing.html            Pricing tiers
├── about.html               About / mission / team
├── guide.html                Onboarding guide
├── faq.html                   FAQ accordion
├── contact.html              Contact form
├── login.html                 Log in
├── register.html              Sign up
├── 404.html                    Not-found page
├── css/style.css              Design tokens + all styles
├── js/main.js                  Shared interactivity
├── images/favicon.svg          Site icon
└── build.py, pages*.py         Python generator used to produce the HTML
                                 (not needed at runtime — the .html files
                                 are already generated and self-contained)
```

## Running locally

Any static file server works:

```bash
npx serve .
# or
python3 -m http.server 3000
```

Then open `http://localhost:3000`.

## Deploying to Vercel

This is a zero-config static site.

1. Push this folder to a GitHub repository.
2. Import the repo in Vercel.
3. Framework preset: **Other** (no build command, no output directory
   override needed — Vercel serves the root as static files).
4. Deploy.

`vercel.json` adds basic security headers and long-cache headers for
`/css`, `/js`, and `/images`.

## Notes

- All data (problems, contests, rankings, testimonials) is realistic
  placeholder content — there is no backend wired up yet. Forms validate
  on the client and show a success state, but do not submit anywhere.
- Images use `i.pravatar.cc` and `picsum.photos`/inline SVG placeholders.
- Dark/light theme preference is stored in `localStorage` under the key
  `astra-theme` and falls back to the OS preference on first visit.
- Regenerating pages: edit `pages*.py` / `build.py` and re-run
  `python3 pages.py && python3 pages2.py && python3 pages3.py && python3 pages4.py`
  from inside this folder. This regenerates the `.html` files in place.
