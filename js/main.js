/* =========================================================================
   ASTRA — shared front-end behaviour (vanilla JS, no dependencies)
   ========================================================================= */
(function () {
  "use strict";

  /* ---------------------------------------------------------------------
     1. THEME TOGGLE (persisted in localStorage, respects OS preference)
     --------------------------------------------------------------------- */
  const THEME_KEY = "astra-theme";
  const root = document.documentElement;

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    document.querySelectorAll(".theme-toggle").forEach((btn) => {
      btn.setAttribute("aria-pressed", theme === "dark");
    });
  }

  function initTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    applyTheme(saved || (prefersDark ? "dark" : "light"));
  }

  function toggleTheme() {
    const current = root.getAttribute("data-theme") === "dark" ? "dark" : "light";
    const next = current === "dark" ? "light" : "dark";
    localStorage.setItem(THEME_KEY, next);
    applyTheme(next);
  }

  document.addEventListener("click", (e) => {
    if (e.target.closest(".theme-toggle")) toggleTheme();
  });
  initTheme();

  /* ---------------------------------------------------------------------
     2. MOBILE HAMBURGER MENU
     --------------------------------------------------------------------- */
  const hamburger = document.querySelector(".hamburger");
  const navLinks = document.querySelector(".nav-links");

  if (hamburger && navLinks) {
    hamburger.addEventListener("click", () => {
      const isOpen = navLinks.classList.toggle("open");
      hamburger.classList.toggle("open", isOpen);
      hamburger.setAttribute("aria-expanded", String(isOpen));
    });

    // Close the mobile menu after a link is chosen
    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        navLinks.classList.remove("open");
        hamburger.classList.remove("open");
        hamburger.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------------------------------------------------------------------
     3. SMOOTH SCROLL FOR IN-PAGE ANCHORS (accounts for fixed nav height)
     --------------------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach((link) => {
    link.addEventListener("click", (e) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (!target) return;
      e.preventDefault();
      const navH = document.querySelector(".site-header")?.offsetHeight || 0;
      const top = target.getBoundingClientRect().top + window.scrollY - navH - 16;
      window.scrollTo({ top, behavior: "smooth" });
    });
  });

  /* ---------------------------------------------------------------------
     4. BACK TO TOP BUTTON
     --------------------------------------------------------------------- */
  const backToTop = document.querySelector(".back-to-top");
  if (backToTop) {
    window.addEventListener("scroll", () => {
      backToTop.classList.toggle("show", window.scrollY > 480);
    }, { passive: true });
    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------------------------------------------------------------------
     5. STICKY HEADER SHADOW ON SCROLL
     --------------------------------------------------------------------- */
  const header = document.querySelector(".site-header");
  if (header) {
    const setShadow = () => {
      header.style.boxShadow = window.scrollY > 6 ? "0 6px 20px -12px rgba(1,32,78,0.35)" : "none";
    };
    window.addEventListener("scroll", setShadow, { passive: true });
    setShadow();
  }

  /* ---------------------------------------------------------------------
     6. FAQ ACCORDION
     --------------------------------------------------------------------- */
  document.querySelectorAll(".faq-item").forEach((item) => {
    const question = item.querySelector(".faq-q");
    const answer = item.querySelector(".faq-a");
    if (!question || !answer) return;

    question.addEventListener("click", () => {
      const isOpen = item.classList.contains("open");

      // Close sibling items within the same list for a single-open accordion
      const list = item.closest(".faq-list");
      if (list) {
        list.querySelectorAll(".faq-item.open").forEach((openItem) => {
          if (openItem !== item) {
            openItem.classList.remove("open");
            openItem.querySelector(".faq-a").style.maxHeight = null;
            openItem.querySelector(".faq-q").setAttribute("aria-expanded", "false");
          }
        });
      }

      item.classList.toggle("open", !isOpen);
      question.setAttribute("aria-expanded", String(!isOpen));
      answer.style.maxHeight = !isOpen ? answer.scrollHeight + "px" : null;
    });
  });

  /* ---------------------------------------------------------------------
     7. ANIMATED STATISTICS COUNTER (triggers once, on scroll into view)
     --------------------------------------------------------------------- */
  const counters = document.querySelectorAll("[data-count-to]");
  if (counters.length) {
    const animateCounter = (el) => {
      const target = parseFloat(el.getAttribute("data-count-to"));
      const suffix = el.getAttribute("data-suffix") || "";
      const duration = 1400;
      const start = performance.now();

      function tick(now) {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
        const value = target * eased;
        el.textContent = (target % 1 === 0 ? Math.round(value) : value.toFixed(1)).toLocaleString() + suffix;
        if (progress < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });

    counters.forEach((c) => observer.observe(c));
  }

  /* ---------------------------------------------------------------------
     8. FORM VALIDATION (contact form, newsletter, auth forms)
     --------------------------------------------------------------------- */
  function setFieldError(row, message) {
    row.classList.toggle("has-error", Boolean(message));
    const msgEl = row.querySelector(".error-msg");
    if (msgEl) msgEl.textContent = message || "";
  }

  function validateField(input) {
    const row = input.closest(".form-row");
    if (!row) return true;
    let message = "";

    if (input.hasAttribute("required") && !input.value.trim()) {
      message = "This field can't be empty.";
    } else if (input.type === "email" && input.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value)) {
      message = "Enter a valid email address.";
    } else if (input.type === "password" && input.value && input.value.length < 8) {
      message = "Use at least 8 characters.";
    } else if (input.dataset.match) {
      const other = document.getElementById(input.dataset.match);
      if (other && input.value !== other.value) message = "Passwords don't match.";
    }

    setFieldError(row, message);
    return !message;
  }

  document.querySelectorAll("form[data-validate]").forEach((form) => {
    const inputs = form.querySelectorAll("input, textarea, select");

    inputs.forEach((input) => {
      input.addEventListener("blur", () => validateField(input));
    });

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      let allValid = true;
      inputs.forEach((input) => {
        if (!validateField(input)) allValid = false;
      });

      if (allValid) {
        const successEl = form.querySelector(".form-success");
        if (successEl) {
          successEl.classList.add("show");
          successEl.setAttribute("role", "status");
        }
        form.reset();
        // Front-end only demo: no backend wired up yet.
        setTimeout(() => successEl && successEl.classList.remove("show"), 5000);
      }
    });
  });

  /* ---------------------------------------------------------------------
     9. YEAR STAMP IN FOOTER
     --------------------------------------------------------------------- */
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });

})();
