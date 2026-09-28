#!/usr/bin/env python3
"""Generate the Career Skills Center inner pages.

Reads index.html, lifts the shared <header>, <footer> and <dialog> out of it so
every page stays byte-identical to the home page, then writes each inner page.
Re-run after changing the header/footer/dialog on index.html.
"""
import re
import json
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
home = (ROOT / "index.html").read_text(encoding="utf-8")


def block(pattern):
    m = re.search(pattern, home, re.S)
    if not m:
        raise SystemExit("could not find block: " + pattern)
    return m.group(0)


HEADER = block(r'<header class="site-header".*?</header>')
FOOTER = block(r'<footer class="site-footer".*?</footer>')
DIALOG = block(r'<dialog class="contact-dialog".*?</dialog>')

# Cache-busting: stamp css/js links with each asset's mtime so browsers always
# fetch the current version after a change (no hard-refresh needed).
CSS_VER = str(int((ROOT / "css" / "style.css").stat().st_mtime))
JS_VER = str(int((ROOT / "js" / "main.js").stat().st_mtime))
CFG_VER = str(int((ROOT / "js" / "site-config.js").stat().st_mtime))

# index.html isn't regenerated, so keep its own asset links stamped here.
_stamped = re.sub(r'(href="css/style\.css)(\?v=\d+)?"', r'\1?v=%s"' % CSS_VER, home)
_stamped = re.sub(r'(src="js/main\.js)(\?v=\d+)?"', r'\1?v=%s"' % JS_VER, _stamped)
_stamped = re.sub(r'(src="js/site-config\.js)(\?v=\d+)?"', r'\1?v=%s"' % CFG_VER, _stamped)
if _stamped != home:
    (ROOT / "index.html").write_text(_stamped, encoding="utf-8")
    home = _stamped
    HEADER = block(r'<header class="site-header".*?</header>')
    FOOTER = block(r'<footer class="site-footer".*?</footer>')
    DIALOG = block(r'<dialog class="contact-dialog".*?</dialog>')

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Google Analytics (GA4) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0XDE7E7RGQ"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-0XDE7E7RGQ');
  </script>

  <title>@@TITLE@@</title>
  <meta name="description" content="@@DESC@@">
  <link rel="canonical" href="https://careerskillscenter.com/@@SLUG@@">

  <!-- Open Graph / social -->
  <meta property="og:title" content="@@OGTITLE@@">
  <meta property="og:description" content="@@DESC@@">
  <meta property="og:url" content="https://careerskillscenter.com/@@SLUG@@">
  <meta property="og:image" content="https://careerskillscenter.com/images/Hero.webp">
  <meta property="og:type" content="website">

  <!-- Fonts: Poppins (display) + Roboto (everything else) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/style.css?v=@@CSSVER@@">
@@EXTRAHEAD@@
</head>
<body>

  <a class="skip-link" href="#main">Skip to content</a>

@@HEADER@@

  <main id="main">

@@MAIN@@

  </main>

@@FOOTER@@

@@DIALOG@@

  <script src="js/site-config.js?v=@@CFGVER@@" defer></script>
  <script src="js/main.js?v=@@JSVER@@" defer></script>
</body>
</html>
"""

# --- shared fragments -------------------------------------------------------

ICON_TRADES = """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M10 40h44"/>
                <path d="M14 40v-6a18 18 0 0 1 36 0v6"/>
                <path d="M26 18v-4h12v4"/>
                <path d="M32 16v10"/>
                <path d="M8 40h48v4H8z"/>
                <path d="M20 52l6-6 4 4-6 6z"/>
                <path d="M30 46l10-10a5 5 0 1 1 6 6l-10 10"/>
              </svg>"""

ICON_IT = """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="6" y="10" width="52" height="34" rx="3"/>
                <path d="M6 38h52"/>
                <path d="M24 54h16M32 44v10"/>
                <path d="M24 20l-6 6 6 6"/>
                <path d="M40 20l6 6-6 6"/>
                <path d="M35 18l-6 16"/>
              </svg>"""

ICON_MED = """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 8v18a10 10 0 0 0 20 0V8"/>
                <path d="M12 8h8M32 8h8"/>
                <path d="M26 36v8a10 10 0 0 0 20 0v-6"/>
                <circle cx="46" cy="32" r="6"/>
                <path d="M46 29v6M43 32h6"/>
              </svg>"""


def program_cards():
    """The three navy program cards, same markup/behaviour as the home page.
    NOTE: the hover-reveal effect is still deferred (see index.html)."""
    return f"""        <div class="program-grid">
          <a class="program-card" href="skilled-trades.html" data-hover-image="images/Todaybanner2.webp">
            <span class="program-icon" aria-hidden="true">{ICON_TRADES}</span>
            <span class="program-name">Skilled Trades</span>
            <span class="program-more">Read more</span>
          </a>
          <a class="program-card" href="it-support-specialist.html" data-hover-image="">
            <span class="program-icon" aria-hidden="true">{ICON_IT}</span>
            <span class="program-name">Information Technology</span>
            <span class="program-more">Read more</span>
          </a>
          <a class="program-card" href="our-programs.html#medical" data-hover-image="">
            <span class="program-icon" aria-hidden="true">{ICON_MED}</span>
            <span class="program-name">Medical</span>
            <span class="program-more">Read more</span>
          </a>
        </div>"""


def hero(label, title, lede, img="images/Hero.webp", btn2=("Career Paths", "career-paths.html")):
    bg = (f'\n      <div class="page-hero-bg"><img src="{img}" alt="" fetchpriority="high" decoding="async"></div>'
          if img else "")
    return f"""    <section class="page-hero">{bg}
      <div class="container">
        <p class="eyebrow eyebrow--light"><span class="eyebrow-line" aria-hidden="true"></span>{label}</p>
        <h1>{title}<span class="dot">.</span></h1>
        <p class="page-hero-lede">{lede}</p>
        <div class="hero-actions">
          <button class="btn btn-yellow js-open-contact" type="button">Get in Touch</button>
          <a class="btn btn-outline" href="{btn2[1]}">{btn2[0]}</a>
        </div>
      </div>
    </section>"""


def cta(title, label="Yes, Let’s Get in Touch"):
    return f"""    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container text-center">
        <h2 class="cta-title" id="cta-title">{title}</h2>
        <button class="btn btn-yellow js-open-contact" type="button">{label}</button>
      </div>
    </section>"""


# --- Pre-launch ("Program in development") building blocks -------------------
# The school has no programs, students or graduates live yet, so pages must not
# state program length, hours, price, credential/exam, certificate, start date,
# VA status or any outcome. See docs/PRE_LAUNCH_SITE_SPEC.md and CLAUDE.md.

DEV_STATUS = ('    <section class="section section--tight">\n'
              '      <div class="container">\n'
              '        <p class="note"><strong>Program in development.</strong> Details, pricing and start '
              'dates will be announced before enrollment opens. Join the interest list below and we will email '
              'you first.</p>\n'
              '      </div>\n'
              '    </section>')


def dev_hero(label, title, lede):
    """Hero for a pre-launch page: 'Join the interest list' as the primary CTA."""
    return f"""    <section class="page-hero">
      <div class="container">
        <p class="eyebrow eyebrow--light"><span class="eyebrow-line" aria-hidden="true"></span>{label}</p>
        <h1>{title}<span class="dot">.</span></h1>
        <p class="page-hero-lede">{lede}</p>
        <div class="hero-actions">
          <a class="btn btn-yellow" href="#interest">Join the interest list</a>
          <a class="btn btn-outline" href="our-programs.html">All programs</a>
        </div>
      </div>
    </section>"""


def interest_form(preselect="unsure", program_label="our programs"):
    """Site-wide interest-list form (spec §16). Reuses the .contact-form fetch
    handler; posts to submit.php with source=interest-list. `preselect` is one of
    it / medical / trades / unsure. Doubles as market research (pay method)."""
    opts = [("it", "Information Technology"), ("medical", "Healthcare"),
            ("trades", "Skilled Trades"), ("unsure", "Not sure yet")]
    sel = preselect or "unsure"
    options = "\n".join(
        f'              <option value="{v}"{" selected" if v == sel else ""}>{label}</option>'
        for v, label in opts)
    return f"""    <!-- COURSE-DEPENDENT: R-IFORM — interest list. In course mode, live fields swap
         this for an enroll/apply form (COURSES_LIVE.*). -->
    <section class="section section--alt" id="interest">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Join the interest list</p>
        <h2 class="section-title left">Be first to know</h2>
        <div class="section-intro"><p>Enrollment isn’t open yet. Leave your details and we’ll email you the
        moment {program_label} details, dates and pricing are ready. No spam, no pressure.</p></div>
        <form class="contact-form interest-form" action="submit.php" method="post" novalidate
              data-success="You’re on the list. We’ll email you when the details are ready.">
          <input type="hidden" name="source" value="interest-list">
          <input type="text" class="hp-field" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
          <label class="sr-only" for="il-name">First name</label>
          <input id="il-name" name="name" type="text" placeholder="First name" autocomplete="given-name" required>
          <label class="sr-only" for="il-email">Email address</label>
          <input id="il-email" name="email" type="email" placeholder="Email address" autocomplete="email" required>
          <label class="sr-only" for="il-phone">Mobile phone (optional)</label>
          <input id="il-phone" name="phone" type="tel" placeholder="Mobile phone (optional)" autocomplete="tel">
          <label class="sr-only" for="il-program">Program of interest</label>
          <select id="il-program" name="program" required>
{options}
          </select>
          <label class="sr-only" for="il-language">Preferred language</label>
          <select id="il-language" name="language">
            <option value="" selected disabled>Preferred language</option>
            <option value="English">English</option>
            <option value="Español">Español</option>
            <option value="Português">Português</option>
          </select>
          <label class="sr-only" for="il-pay">How would you likely pay?</label>
          <select id="il-pay" name="pay_method">
            <option value="" selected disabled>How would you likely pay?</option>
            <option value="self">Self-pay</option>
            <option value="employer">My employer</option>
            <option value="state">State or grant funding</option>
            <option value="unsure">Not sure</option>
          </select>
          <label class="consent-row"><input type="checkbox" name="consent" value="yes"> It’s OK to text me about
          programs. Message and data rates may apply.</label>
          <button class="btn btn-yellow" type="submit">Join the interest list</button>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>"""


def employer_form(source, heading="Talk to us about training your team",
                  intro="Tell us what you need and we&rsquo;ll follow up. No obligation.",
                  topic_options=None, show_team_size=True, show_timeline=False,
                  submit_label="Send inquiry", eyebrow="For employers"):
    """Employer inquiry form (Site Structure Spec v1.5). Reuses the .contact-form
    fetch handler in main.js; posts to submit.php with a distinct hidden `source`.
    Each employer page passes its own source (employer / employer-express /
    employer-apprenticeship / corporate)."""
    sid = source.replace("-", "_")
    team = ("" if not show_team_size else f"""
          <label class="sr-only" for="{sid}-team">Team size</label>
          <select id="{sid}-team" name="team_size">
            <option value="" selected disabled>How many people to train?</option>
            <option value="1-5">1&ndash;5</option>
            <option value="6-20">6&ndash;20</option>
            <option value="21-100">21&ndash;100</option>
            <option value="100+">More than 100</option>
          </select>""")
    if topic_options is not None:
        opts = "\n".join(f'            <option value="{v}">{lbl}</option>' for v, lbl in topic_options)
        topic = f"""
          <label class="sr-only" for="{sid}-topic">Training topic</label>
          <select id="{sid}-topic" name="topic">
            <option value="" selected disabled>What training do you need?</option>
{opts}
          </select>"""
    else:
        topic = ""
    timeline = ("" if not show_timeline else f"""
          <label class="sr-only" for="{sid}-timeline">Timeline</label>
          <select id="{sid}-timeline" name="timeline">
            <option value="" selected disabled>When do you want to start?</option>
            <option value="asap">As soon as possible</option>
            <option value="1-3-months">In 1&ndash;3 months</option>
            <option value="3-6-months">In 3&ndash;6 months</option>
            <option value="exploring">Just exploring</option>
          </select>""")
    return f"""    <section class="section section--alt" id="employer-inquiry">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>{eyebrow}</p>
        <h2 class="section-title left">{heading}</h2>
        <div class="section-intro"><p>{intro}</p></div>
        <form class="contact-form employer-form" action="submit.php" method="post" novalidate
              data-success="Thanks &mdash; we&rsquo;ve got your details and will be in touch.">
          <input type="hidden" name="source" value="{source}">
          <input type="text" class="hp-field" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
          <label class="sr-only" for="{sid}-company">Company name</label>
          <input id="{sid}-company" name="company" type="text" placeholder="Company name" autocomplete="organization" required>
          <label class="sr-only" for="{sid}-name">Your name</label>
          <input id="{sid}-name" name="name" type="text" placeholder="Your name" autocomplete="name" required>
          <label class="sr-only" for="{sid}-email">Work email</label>
          <input id="{sid}-email" name="email" type="email" placeholder="Work email" autocomplete="email" required>
          <label class="sr-only" for="{sid}-phone">Phone (optional)</label>
          <input id="{sid}-phone" name="phone" type="tel" placeholder="Phone (optional)" autocomplete="tel">{team}{topic}{timeline}
          <label class="sr-only" for="{sid}-message">Anything else?</label>
          <textarea id="{sid}-message" name="message" rows="4" placeholder="Anything else we should know?"></textarea>
          <button class="btn btn-yellow" type="submit">{submit_label}</button>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>"""


SITE_URL = "https://careerskillscenter.com/"


def article(category, title, dek, date, read, body, author="Career Skills Center Team"):
    """Blog article: navy hero (category eyebrow, H1, meta line) + prose body.
    `body` is the inner HTML of the .prose container. Image-free by design.
    No "Updated" line — added only when a real update happens (see VERIFICATION_LOG F2)."""
    return f"""    <section class="page-hero">
      <div class="container">
        <p class="eyebrow eyebrow--light"><span class="eyebrow-line" aria-hidden="true"></span>{category}</p>
        <h1 class="article-title">{title}</h1>
        <p class="page-hero-lede">{dek}</p>
        <p class="article-meta">Published {date}<span class="dot-sep"></span>{read}<span class="dot-sep"></span>By {author}</p>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
{body}
      </div>
    </section>"""


def post_cta(title, lede, label, href):
    """In-article call-to-action box (link version, not the dialog band)."""
    return f"""        <div class="post-cta">
          <h2>{title}</h2>
          <p>{lede}</p>
          <a class="btn btn-yellow" href="{href}">{label}</a>
        </div>"""


def related(*cards):
    """`cards` are (title, href) tuples rendered as a small related-articles grid."""
    items = "\n".join(
        f'          <a class="post-card" href="{href}"><h3>{t}</h3><span class="read-link">Read article</span></a>'
        for t, href in cards)
    return f"""        <h2 class="related-title">Related articles</h2>
        <div class="post-grid post-grid--related">
{items}
        </div>"""


def faq_ld(pairs):
    """FAQPage JSON-LD from a list of (question, answer-plaintext) tuples."""
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }
    return ('  <script type="application/ld+json">\n  '
            + json.dumps(data, ensure_ascii=False, indent=2).replace("\n", "\n  ")
            + "\n  </script>")


def article_ld(slug, title, desc, date, updated, author="Career Skills Center Team"):
    """BlogPosting JSON-LD for a blog article."""
    data = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "datePublished": date,
        "dateModified": updated,
        "author": {"@type": "Organization", "name": author},
        "publisher": {"@type": "Organization", "name": "Career Skills Center"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": SITE_URL + slug},
    }
    return ('  <script type="application/ld+json">\n  '
            + json.dumps(data, ensure_ascii=False, indent=2).replace("\n", "\n  ")
            + "\n  </script>")


def prog_item(name, desc, credential, length="TBD"):
    return f"""          <article class="program-item">
            <h4>{name}</h4>
            <p>{desc}</p>
            <div class="program-meta">
              <span><strong>Credential:</strong> {credential}</span>
              <span><strong>Length:</strong> <span class="tbd">{length}</span></span>
            </div>
          </article>"""


# The steps section, reused from the home page on admissions.html
STEPS = """    <section class="steps section" id="steps">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Step by Step</p>
        <h2 class="section-title left">Ready to Start?</h2>

        <ol class="step-list">
          <li class="step-card">
            <div class="step-num"><span class="num">1</span><span class="lbl">Step</span></div>
            <div class="step-body">
              <h3>Call to get qualified</h3>
              <p>Speak with our enrollment team to discover your career interests. Choose from trade, IT, and medical courses. Get qualified to become a student.</p>
            </div>
          </li>
          <li class="step-card">
            <div class="step-num"><span class="num">2</span><span class="lbl">Step</span></div>
            <div class="step-body">
              <h3>Enroll in a program</h3>
              <p>Choose the course that fits you best. Complete forms for school and funding. Attend the “Welcome” meeting and ask questions. We’re here to help you succeed!</p>
            </div>
          </li>
          <li class="step-card">
            <div class="step-num"><span class="num">3</span><span class="lbl">Step</span></div>
            <div class="step-body">
              <h3>Get started</h3>
              <p>Participate in orientation to understand expectations. We’re serious about your success. Your future starts now.</p>
            </div>
          </li>
        </ol>

        <div class="steps-cta">
          <button class="btn btn-navy btn-block js-open-contact" type="button">Get Started Today</button>
        </div>
      </div>
    </section>"""

DRAFT_NOTE = ('<p class="note"><strong>Draft content.</strong> Program names, credentials, lengths and '
              'prices below are a working list. Confirm the final catalog, licensing and approvals with '
              'the Massachusetts Department of Professional Licensure before publishing.</p>')


# --- Guide-mode helpers: career-field guides (GUIDE_MODE_SPEC step 3) --------
# Each guide is a reference to a whole field in Massachusetts, NOT a course page.
# All pay = BLS OEWS May 2025, Massachusetts (docs/VERIFICATION_LOG.md H1).
# Licensing facts are sourced (VERIFICATION_LOG H2). No Course schema.

MASSHIRE_URL = "https://www.mass.gov/info-details/masshire-career-center-locations"
JOBQUEST_URL = "https://jobquest.mass.gov"


def role_card(name, blurb, training, certs, online, license_note):
    """Career-path role card (Site Structure Spec v1.5): location-neutral, no pay.
    Pay figures are intentionally omitted until sourced entry-level data is ready
    (R-PAY-DATA); each card carries a hidden PAY-DATA slot to drop them into."""
    return f"""          <article class="role-card">
            <h3 class="role-name">{name}</h3>
            <p class="role-blurb">{blurb}</p>
            <dl class="role-facts">
              <div><dt>Typical training</dt><dd>{training}</dd></div>
              <div><dt>Certifications</dt><dd>{certs}</dd></div>
              <div><dt>License</dt><dd>{license_note}</dd></div>
              <div><dt>Can you train online?</dt><dd>{online}</dd></div>
            </dl>
            <!-- PAY-DATA: pending — R-PAY-DATA. Typical-pay figures omitted until sourced;
                 add a <div><dt>Typical pay</dt><dd>…</dd></div> here when ready. -->
          </article>"""


def role_grid(*cards):
    return '        <div class="role-grid">\n' + "\n".join(cards) + "\n        </div>"


def pay_for_training_block():
    """Shared 'How to pay for training in MA' summary → blog + qualify."""
    return """    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Paying for it</p>
        <h2 class="section-title left">How to pay for training in Massachusetts</h2>
        <p>Most people combine more than one source. Massachusetts residents who are unemployed, laid off, or
        working in a low-wage job may qualify for state-funded training through a MassHire career center. If you
        get unemployment benefits, ask about Section 30. Employers can be reimbursed for training their staff
        through the state Workforce Training Fund. Only a MassHire career center can approve funding &mdash;
        we&rsquo;ll help you understand your options.</p>
        <ul class="check-list">
          <li><a class="link-yellow" href="blog/free-job-training-massachusetts.html">Free job training in Massachusetts</a> &mdash; the full funding guide</li>
          <li><a class="link-yellow" href="blog/wioa-eligibility-massachusetts.html">Who qualifies for WIOA training in Massachusetts</a></li>
          <li><a class="link-yellow" href="blog/masshire-training-voucher.html">How to get a MassHire training voucher (ITA)</a></li>
          <li><a class="link-yellow" href="student-financing.html">Ways to Pay</a> &mdash; every option in one place</li>
        </ul>
        <p><a class="btn btn-yellow" href="qualify.html">Check your funding options</a></p>
      </div>
    </section>"""


def outward_next_step(field_label):
    """Shared outward 'next step' → MassHire + JobQuest (verified URLs)."""
    return f"""    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Your next step</p>
        <h2 class="section-title left">Start with the state</h2>
        <p>Massachusetts runs the system that pays for most career training. Two free steps get you moving
        toward {field_label}:</p>
        <ol class="check-list check-list--num">
          <li><strong>Find your MassHire Career Center.</strong> <a class="link-yellow" href="{MASSHIRE_URL}" target="_blank" rel="noopener">See the list of locations</a> and contact the one nearest you.</li>
          <li><strong>Register on JobQuest.</strong> You need a JobQuest account before you can get training funding. <a class="link-yellow" href="{JOBQUEST_URL}" target="_blank" rel="noopener">Register at jobquest.mass.gov</a>, then ask about a Training Information Meeting.</li>
        </ol>
        <p>From there, a career counselor helps you check your eligibility and pick a state-approved training
        program in this field.</p>
      </div>
    </section>"""


FUNDING_NOTE = """        <div class="note"><strong>About Career Skills Center and state funding:</strong> Massachusetts offers
        free training to eligible residents through MassHire Career Centers. Career Skills Center is working
        toward approval to accept these funds. In the meantime, <a href="contact.html">join our interest
        list</a>, and we will keep you posted as our programs and funding status develop. We will help you check
        what you may qualify for — but only your MassHire career center can approve funding.</div>"""


def career_pay_block():
    """Location-neutral 'how to pay' + next step for the Career Paths pages
    (Site Structure Spec v1.5: no location framing on career pages). Points to the
    funding guides, which carry the Massachusetts-specific detail."""
    return """    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Paying for it</p>
        <h2 class="section-title left">You may not have to pay out of pocket</h2>
        <p>Training costs money, but you may not have to cover it yourself. Public workforce funding can pay
        tuition for people who qualify, and employers can often get reimbursed for training their staff. Our
        funding guides explain how these programs work and how to check what you may qualify for.</p>
        <ul class="check-list">
          <li><a class="link-yellow" href="wioa-explained.html">WIOA Explained</a> &mdash; how the main public training fund works and who qualifies</li>
          <li><a class="link-yellow" href="express-program-explained.html">Express Program Explained</a> &mdash; how employers get staff training reimbursed</li>
          <li><a class="link-yellow" href="qualify.html">Do I Qualify?</a> &mdash; a quick check of your options</li>
        </ul>
        <p><a class="btn btn-yellow" href="qualify.html">Check what you may qualify for</a></p>
      </div>
    </section>"""


def field_interest(field, field_name, human_field):
    """COURSE-DEPENDENT secondary CTA for a field guide (interest list).
    `field` is one of healthcare/it/trades/hub; the register IDs are R-HC/R-IT/R-TR/R-HUB."""
    rid = {"healthcare": "HC", "it": "IT", "trades": "TR", "hub": "HUB"}.get(field, field.upper())
    live = {"healthcare": "healthcare", "it": "it", "trades": "trades", "hub": "*"}.get(field, field)
    return (f"""    <!-- COURSE-DEPENDENT: R-{rid} — guide mode routes outward (MassHire/JobQuest)
         and offers the interest list. In course mode (COURSES_LIVE.{live}) replace this
         with a "Train with Career Skills Center" block: course name, details, enroll/apply CTA. -->
"""
            + interest_form(field_name, human_field))

# ---------------------------------------------------------------------------
# PAGES
# ---------------------------------------------------------------------------
PAGES = []

# Pages defined below but withheld from the live site until certification is in
# hand. Their definitions stay intact so they can be restored by removing the
# slug here; the last-built copies are kept in _archive/. WIOA and the
# superseded financial-aid page advertise WIOA funding, which must not be
# published until Career Skills Center is an approved Eligible Training
# Provider on the Massachusetts ETPL.
ARCHIVED = {"wioa.html", "financial-aid.html"}

# STEP 6 — pages retired in guide mode. Each is emitted as a small 301-style
# redirect stub (meta refresh + canonical), and .htaccess does the real server
# 301 (SEO-correct). They're kept out of the sitemap. Their full PAGES entries
# stay in this file (unused) so the content can be restored if a page returns in
# course mode. See docs/GUIDE_MODE_SPEC.md step 6 + COURSE_CONTENT_REGISTER.
REDIRECTS = {
    # Old program pages -> the new location-neutral career-field guides (v1.5 renamed
    # the guides and re-points these here).
    "medical-billing-coding.html": "healthcare-careers.html",
    "it-support-specialist.html":  "it-careers.html",
    "skilled-trades.html":         "skilled-trades-careers.html",
    # The v1.4 Massachusetts-named guides -> the v1.5 location-neutral URLs.
    "healthcare-careers-massachusetts.html":     "healthcare-careers.html",
    "it-careers-massachusetts.html":             "it-careers.html",
    "skilled-trades-careers-massachusetts.html": "skilled-trades-careers.html",
    "our-programs.html":           "career-paths.html",
    "programs.html":               "career-paths.html",
    "tuition.html":                "student-financing.html",
    "admissions.html":             "career-paths.html",
    "career-services.html":        "about.html",
    "team.html":                   "about.html",
    "media.html":                  "about.html",
    # Legal page rename (v1.5: terms.html).
    "terms-of-use.html":           "terms.html",
}


# Pages built but held back from the sitemap and search indexing (not redirected).
# Post #5 is on hold until the pay-data work is done (Site Structure Spec v1.5 §6).
HOLD = {"blog/highest-paying-certifications-massachusetts.html"}


def redirect_html(slug, target):
    """A minimal 301-style stub: canonical + meta refresh to `target`.
    .htaccess also serves a real 301 for the path; this is the belt-and-suspenders
    fallback if .htaccess is ever not honored."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page moved | Career Skills Center</title>
  <link rel="canonical" href="https://careerskillscenter.com/{target}">
  <meta name="robots" content="noindex, follow">
  <meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
  <p>This page has moved. If you are not redirected, <a href="{target}">continue here</a>.</p>
  <script>location.replace({target!r});</script>
</body>
</html>
"""


# ---- redirect-only slugs (v1.5) -------------------------------------------
# These have no page body of their own; they exist only so the build emits a
# redirect stub (and overwrites any stale file on disk). The real 301 is served
# by .htaccess. Targets live in the REDIRECTS map above.
for _rslug in ("healthcare-careers-massachusetts.html",
               "it-careers-massachusetts.html",
               "skilled-trades-careers-massachusetts.html",
               "terms-of-use.html"):
    PAGES.append(dict(slug=_rslug, nav=None, title="", ogtitle="", desc="", main=""))


# ---- programs.html --------------------------------------------------------
# Deprecated and unlinked. Redirects to our-programs.html so it carries no
# stale program details (see docs/PRE_LAUNCH_SITE_SPEC.md §6).
PAGES.append(dict(
    slug="programs.html", nav="our-programs.html",
    title="Our Programs | Career Skills Center — Massachusetts",
    ogtitle="Our Programs",
    desc="This page has moved to Our Programs.",
    extrahead='  <meta http-equiv="refresh" content="0; url=our-programs.html">',
    main=hero("Our Programs", "Our Programs", "This page has moved.", None) + """

    <section class="section">
      <div class="container narrow text-center">
        <p class="lede">This page has moved to
        <a class="link-yellow" href="our-programs.html">Our Programs</a>.</p>
      </div>
    </section>
"""))


# ---- our-programs.html ----------------------------------------------------
# Card-grid overview linked from the homepage "Our Programs" button. The image
# areas are intentional placeholders until program photos are chosen.
PAGES.append(dict(
    slug="our-programs.html", nav="our-programs.html",
    title="Our Programs | Career Skills Center — Massachusetts",
    ogtitle="Our Programs",
    desc="Explore Career Skills Center training in the skilled trades, information technology and the medical field in Massachusetts.",
    main=hero("Our Programs", "Our Programs",
              "We&rsquo;re building online career training for Massachusetts adults. Explore the fields below "
              "and join the interest list for the program you want.",
              "images/programs-hero.webp", ("Join the Interest List", "#interest")) + """

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Explore the fields</p>
        <h2 class="section-title left">Choose Your Field</h2>
        <div class="pcard-grid">

          <article class="pcard" id="it">
            <img src="images/comptia.webp" alt="IT support technician at work" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <span class="pcard-badge">In development</span>
              <h3 class="pcard-title">Information Technology</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Help-desk and IT support &mdash; the most common way into a tech career, hiring across Massachusetts. No four-year degree required.</p>
              <a class="btn btn-outline-navy" href="it-support-specialist.html">Read more</a>
            </div>
          </article>

          <article class="pcard" id="medical">
            <img src="images/medicalbilling.webp" alt="Medical billing and coding specialist" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <span class="pcard-badge">In development</span>
              <h3 class="pcard-title">Medical Billing &amp; Coding</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Turn doctor visits into codes and claims &mdash; detailed, office-based healthcare work, often remote once you have experience.</p>
              <a class="btn btn-outline-navy" href="medical-billing-coding.html">Read more</a>
            </div>
          </article>

          <article class="pcard" id="trades">
            <img src="images/electrician.webp" alt="Electrician at work" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <span class="pcard-badge">Coming soon</span>
              <h3 class="pcard-title">Skilled Trades</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Electrical, HVAC/R and plumbing &mdash; licensed trades that pay well in Massachusetts and can&rsquo;t be shipped overseas.</p>
              <a class="btn btn-outline-navy" href="skilled-trades.html">Read more</a>
            </div>
          </article>

        </div>
      </div>
    </section>

""" + interest_form("unsure", "our programs")))


# ---- it-support-specialist.html (pre-launch: program in development) --------
PAGES.append(dict(
    slug="it-support-specialist.html", nav="our-programs.html",
    title="IT Support Training in Massachusetts (Coming Soon) | Career Skills Center",
    ogtitle="IT Support Training in Massachusetts (Coming Soon)",
    desc="Career Skills Center is developing an online IT support program for Massachusetts adults. Learn about the career and join the interest list to hear when it opens.",
    main=dev_hero("Information Technology", "IT Support Training, Coming Soon",
              "We&rsquo;re building an online IT support program for Massachusetts adults. Get on the list and "
              "we&rsquo;ll tell you the moment it&rsquo;s ready.") + DEV_STATUS + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>About the career</p>
        <h2 class="section-title left">What IT support is</h2>
        <p class="lede">IT support (the help desk) is the most common way into a technology career. Support
        technicians set up computers, fix everyday problems, and help people use software and networks. It is
        part technical skill, part customer service.</p>
        <p>In Massachusetts, computer user support specialists earn a median of about <strong>$75,070</strong> a
        year (U.S. Bureau of Labor Statistics, OEWS, May 2025). Nationally, these roles are expected to hold
        steady, with thousands of openings each year as people move up or retire.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>What we&rsquo;re planning</p>
        <h2 class="section-title left">An online program for Massachusetts adults</h2>
        <p>We&rsquo;re designing a beginner-friendly, online IT support program. The plan is to cover the
        fundamentals employers look for:</p>
        <ul class="check-list">
          <li>Computer hardware and operating systems</li>
          <li>Networking basics</li>
          <li>Security basics</li>
          <li>Troubleshooting and customer support</li>
        </ul>
        <p>We plan to align the program with an industry-recognized certification. The exact credential, length,
        schedule and cost will be confirmed before enrollment opens.</p>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Before enrollment opens</p>
        <h2 class="section-title left">What we&rsquo;ll tell you</h2>
        <ul class="check-list">
          <li>Length and schedule</li>
          <li>Cost and payment options</li>
          <li>Which certification it prepares you for</li>
          <li>Whether state or employer funding can be used</li>
        </ul>
        <p>Curious whether this path fits you? Read
        <a class="link-yellow" href="blog/can-you-learn-it-support-online.html">Can you learn IT support
        online?</a> and our guide to
        <a class="link-yellow" href="blog/free-job-training-massachusetts.html">free job training in
        Massachusetts</a>.</p>
      </div>
    </section>

""" + interest_form("it", "IT support program") + """

    <section class="section">
      <div class="container">
        <h2 class="related-title">Learn more</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="blog/can-you-learn-it-support-online.html"><h3>Can You Learn IT Support Online?</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="blog/highest-paying-certifications-massachusetts.html"><h3>Highest-Paying Certifications in Massachusetts</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="blog/free-job-training-massachusetts.html"><h3>Free Job Training in Massachusetts</h3><span class="read-link">Read article</span></a>
        </div>
      </div>
    </section>
"""))


# ---- medical-billing-coding.html (pre-launch: program in development) -------
PAGES.append(dict(
    slug="medical-billing-coding.html", nav="our-programs.html",
    title="Medical Billing &amp; Coding Training in Massachusetts (Coming Soon) | Career Skills Center",
    ogtitle="Medical Billing & Coding Training in Massachusetts (Coming Soon)",
    desc="Career Skills Center is developing an online Medical Billing & Coding program for Massachusetts adults. Learn about the career and join the interest list to hear when it opens.",
    main=dev_hero("Medical", "Medical Billing &amp; Coding Training, Coming Soon",
              "We&rsquo;re building an online medical billing and coding program for Massachusetts adults. Join "
              "the list and we&rsquo;ll tell you when it opens.") + DEV_STATUS + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>About the career</p>
        <h2 class="section-title left">What medical billing and coding is</h2>
        <p class="lede">Medical coders and billers turn doctor visits into standard codes and insurance claims.
        It is detailed, office-based work &mdash; often remote or hybrid once you have experience &mdash; and a
        common way into healthcare without hands-on patient care.</p>
        <p>In Massachusetts, medical records specialists earn a median of about <strong>$60,350</strong> a year
        (U.S. Bureau of Labor Statistics, OEWS, May 2025).</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>What we&rsquo;re planning</p>
        <h2 class="section-title left">An online program for Massachusetts adults</h2>
        <p>We&rsquo;re designing an online medical billing and coding program. The plan is to cover:</p>
        <ul class="check-list">
          <li>Medical terminology and anatomy basics</li>
          <li>Coding systems like ICD-10-CM and CPT</li>
          <li>The claims and billing process</li>
          <li>Privacy and compliance (HIPAA)</li>
        </ul>
        <p>We plan to align the program with an industry-recognized certification. The exact credential, length,
        schedule and cost will be confirmed before enrollment opens.</p>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Before enrollment opens</p>
        <h2 class="section-title left">What we&rsquo;ll tell you</h2>
        <ul class="check-list">
          <li>Length and schedule</li>
          <li>Cost and payment options</li>
          <li>Which certification it prepares you for</li>
          <li>Whether state or employer funding can be used</li>
        </ul>
        <p>Wondering if you can learn it online? Read
        <a class="link-yellow" href="blog/can-medical-billing-coding-be-learned-online.html">Can medical billing
        and coding be learned online?</a></p>
      </div>
    </section>

""" + interest_form("medical", "Medical Billing & Coding program") + """

    <section class="section">
      <div class="container">
        <h2 class="related-title">Learn more</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="blog/can-medical-billing-coding-be-learned-online.html"><h3>Can Medical Billing &amp; Coding Be Learned Online?</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="blog/highest-paying-certifications-massachusetts.html"><h3>Highest-Paying Certifications in Massachusetts</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="blog/free-job-training-massachusetts.html"><h3>Free Job Training in Massachusetts</h3><span class="read-link">Read article</span></a>
        </div>
      </div>
    </section>
"""))


# ---- skilled-trades.html (pre-launch: program in development) ---------------
PAGES.append(dict(
    slug="skilled-trades.html", nav="our-programs.html",
    title="Skilled Trades Training in Massachusetts (Coming Soon) | Career Skills Center",
    ogtitle="Skilled Trades Training in Massachusetts (Coming Soon)",
    desc="Career Skills Center plans to add skilled trades training in Massachusetts. Learn how the trades and licensing work, and join the interest list.",
    main=dev_hero("Skilled Trades", "Skilled Trades Training, Coming Soon",
              "The trades are hiring across Massachusetts. We plan to add skilled trades training &mdash; join "
              "the list and we&rsquo;ll tell you when it opens.") + DEV_STATUS + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>About the careers</p>
        <h2 class="section-title left">Trades that pay, close to home</h2>
        <p class="lede">Electricians, plumbers, and HVAC and refrigeration technicians do work that cannot be
        shipped overseas, and they earn solid middle-class wages in Massachusetts. The trade-off: the trades are
        hands-on and licensed by the state.</p>
        <p>Licensing takes classroom hours (some can be online) plus supervised on-the-job hours. For example, a
        Massachusetts journeyman electrician needs 600 classroom hours and 8,000 hours of supervised work over
        at least four years. HVAC work with refrigerant also needs federal EPA 608 certification.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>What we&rsquo;re planning</p>
        <h2 class="section-title left">Training built around the real path</h2>
        <p>We&rsquo;re developing skilled trades training for Massachusetts. Because a license needs supervised,
        in-person hours, the honest path pairs online coursework (theory, code, safety, exam prep) with an
        apprenticeship or hands-on hours. Program details, format, length and cost will be announced before
        enrollment opens.</p>
        <p>Want the full picture first? Read
        <a class="link-yellow" href="blog/can-you-learn-a-trade-online.html">Can you learn a skilled trade
        online?</a></p>
      </div>
    </section>

""" + interest_form("trades", "skilled trades training") + """

    <section class="section">
      <div class="container">
        <h2 class="related-title">Learn more</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="blog/can-you-learn-a-trade-online.html"><h3>Can You Learn a Skilled Trade Online?</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="blog/highest-paying-certifications-massachusetts.html"><h3>Highest-Paying Certifications in Massachusetts</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="blog/free-job-training-massachusetts.html"><h3>Free Job Training in Massachusetts</h3><span class="read-link">Read article</span></a>
        </div>
      </div>
    </section>
"""))


# ===========================================================================
# STEP 3 — Career field guides (guide mode). Reference guides to whole fields
# in Massachusetts. They 301-replace the old program pages. No Course schema.
# ===========================================================================

# ---- healthcare-careers.html ----------------------------------------------
# Location-neutral career reference (Site Structure Spec v1.5): no "Massachusetts"
# framing, no pay figures (hidden PAY-DATA slot, R-PAY-DATA). Licensing is a general
# note with a clearly labeled Massachusetts example.
_HC_FAQ = [
    ("Do I need a college degree to work in healthcare?",
     "No, not for many roles. Jobs like medical billing and coding, medical assistant, phlebotomy technician, nurse aide (CNA) and home health aide are open to people without a four-year degree, and several can be trained for in a matter of months."),
    ("Which healthcare jobs can I train for online?",
     "Office-based roles like medical billing and coding and medical administrative assistant are the most online-friendly. Hands-on roles such as medical assistant, phlebotomy, nurse aide and EKG technician can start online but require in-person clinical practice."),
    ("Do I need a license to work in healthcare?",
     "It depends on the role and your state. Some roles, like nurse aide (CNA) and pharmacy technician, are regulated. Others, like medical billing and coding, medical assistant and phlebotomy, usually have no license; employers often prefer a voluntary national certification. Always check the rules in your state. Example (Massachusetts): CNAs must complete a state-approved program and pass a competency exam, and pharmacy technicians must be licensed by the state Board of Registration in Pharmacy."),
    ("How long does healthcare training take?",
     "Many entry-level healthcare roles are short, postsecondary certificate paths that take a matter of months rather than years. Hands-on roles add supervised clinical hours; office-based roles like billing and coding can often be finished faster and online."),
    ("How do I pay for healthcare training?",
     "You may not have to pay out of pocket. Public workforce funding can cover tuition for people who qualify, and employers can be reimbursed for training staff. See our funding guides and use the Do I Qualify? check."),
    ("Does Career Skills Center offer healthcare training?",
     "Not yet. Career Skills Center plans to offer training in healthcare, IT and the skilled trades. Join the interest list to get updates when we launch."),
]

PAGES.append(dict(
    slug="healthcare-careers.html", nav="healthcare-careers.html",
    title="Healthcare Careers: Jobs, Training &amp; Certifications | Career Skills Center",
    ogtitle="Healthcare Careers: Jobs, Training & Certifications",
    desc="A plain guide to entry-level healthcare careers: what each job is, how to train, the certifications employers look for, whether you can train online, and how to pay for it.",
    extrahead=faq_ld(_HC_FAQ),
    main=hero("Career Paths &middot; Healthcare",
              "Healthcare Careers: Jobs, Training and How to Get In",
              "Healthcare is one of the largest and steadiest parts of the economy. Many roles don&rsquo;t need "
              "a four-year degree, and several can be trained for in months. Here&rsquo;s what the jobs are, how "
              "to train, and how to get help paying for it.",
              "images/medicalbilling.webp", ("Do I Qualify?", "qualify.html")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The field</p>
        <h2 class="section-title left">Is healthcare right for you?</h2>
        <p class="lede">Healthcare isn&rsquo;t only doctors and nurses. Behind every clinic and hospital is a
        team of billers, coders, assistants, aides and technicians &mdash; roles you can often train for
        quickly. This field suits people who are reliable, detail-oriented, and want steady work that helps
        others. Some jobs are hands-on with patients; others are office-based and can be done partly or fully
        online.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Common roles</p>
        <h2 class="section-title left">Healthcare roles you can train for</h2>
        <div class="section-intro"><p>For each role: what the job is, the typical training path, the
        certifications employers look for, and whether you can train online. Licensing rules vary by state
        &mdash; check yours before you start.</p></div>
""" + role_grid(
        role_card("Medical Billing &amp; Coding",
                  "Turn doctor visits into standard codes and insurance claims. Detailed, office-based work, often remote once you have experience.",
                  "Short certificate or online course, often a few months.",
                  "Voluntary but employer-preferred: AAPC (CPC/CPB) or AHIMA (CCA).",
                  "Yes &mdash; one of the most online-friendly healthcare paths.",
                  "No state license typically required."),
        role_card("Medical Assistant",
                  "Work alongside doctors and nurses: rooming patients, taking vital signs, and handling front-office tasks.",
                  "Postsecondary certificate, often under a year, plus a clinical externship.",
                  "Voluntary: CMA (AAMA) or RMA (AMT).",
                  "Partly. Classroom work can be online, but you need an in-person clinical externship.",
                  "No state license typically required; certification is voluntary."),
        role_card("Phlebotomy Technician",
                  "Draw blood for tests, donations and research. A focused role you can train for quickly.",
                  "Short certificate plus supervised, hands-on draws.",
                  "Voluntary: ASCP or NHA.",
                  "Partly. Theory can be online, but you must practice real blood draws in person.",
                  "Most states don&rsquo;t license phlebotomists; a few require certification. Check your state."),
        role_card("Pharmacy Technician",
                  "Help pharmacists prepare and dispense medications in pharmacies and hospitals.",
                  "Short training program, plus hands-on experience on the job.",
                  "PTCB or ExCPT (widely expected by employers).",
                  "Partly. Coursework can be online; you gain hands-on experience on the job.",
                  "Licensing varies by state. Example (Massachusetts): a state Pharmacy Technician license is required even if you&rsquo;re nationally certified, and you must be 18 or older."),
        role_card("EKG Technician",
                  "Run electrocardiogram (EKG/ECG) tests that record the heart&rsquo;s activity for doctors to read.",
                  "Short certificate plus hands-on practice with the equipment.",
                  "Voluntary: CET (CCI or NHA).",
                  "Partly. Theory can be online, but you need hands-on practice with the equipment.",
                  "No state license typically required; certification is voluntary."),
        role_card("Nurse Aide (CNA)",
                  "Provide hands-on daily care to patients and residents in nursing homes, hospitals and home care.",
                  "A state-approved Nurse Aide Training Program plus a competency exam.",
                  "State competency exam and registry listing (required to work).",
                  "Partly. Some classroom hours may be online, but clinical hours must be done in person.",
                  "Regulated in every state. Example (Massachusetts): complete a Department of Public Health&ndash;approved program and pass the state competency exam to be listed on the Nurse Aide Registry."),
        role_card("Home Health Aide",
                  "Help older adults and people with disabilities live safely and independently at home.",
                  "Usually provided by the employing agency; Medicare-certified agencies follow federal training standards.",
                  "Agency training; federal standards apply at Medicare-certified agencies.",
                  "Partly. Some training is online, but hands-on care skills are practiced in person.",
                  "No license for the role in most states; agencies set training requirements."),
        role_card("Medical Administrative Assistant",
                  "Run the front office of a clinic or practice: scheduling, records, insurance and patient intake.",
                  "Short certificate.",
                  "Voluntary: CMAA.",
                  "Yes &mdash; this office-based role is well suited to online training.",
                  "No state license typically required; certification is voluntary."),
    ) + """
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Choosing a path</p>
        <h2 class="section-title left">Pick your path by where you want to work</h2>
        <div class="section-intro"><p>Healthcare roles differ most by the setting and the kind of day you want.
        A good first question isn&rsquo;t &ldquo;which pays most?&rdquo; but &ldquo;where do I picture myself
        working?&rdquo;</p></div>
        <div class="program-items">
          <article class="program-item">
            <h4>In someone&rsquo;s home or the community</h4>
            <p>One-on-one caregiving in people&rsquo;s homes &mdash; helping older adults and people with
            disabilities live safely and independently. Personal, relationship-based work, often on a schedule
            that fits your life.</p>
            <div class="program-meta"><span><strong>Roles:</strong> Home Health Aide, CNA (home care)</span></div>
          </article>
          <article class="program-item">
            <h4>In a hospital or nursing facility</h4>
            <p>Fast-paced, hands-on work with many patients across a shift. A good fit if you want to be on your
            feet, part of a care team, and in the middle of things.</p>
            <div class="program-meta"><span><strong>Roles:</strong> CNA, Phlebotomy Technician, EKG Technician</span></div>
          </article>
          <article class="program-item">
            <h4>In a clinic or doctor&rsquo;s office</h4>
            <p>A mix of patient contact and front-office work &mdash; rooming patients, taking vital signs,
            scheduling and records &mdash; usually on regular daytime hours.</p>
            <div class="program-meta"><span><strong>Roles:</strong> Medical Assistant, Medical Administrative Assistant, Phlebotomy</span></div>
          </article>
          <article class="program-item">
            <h4>Behind the scenes, often from home</h4>
            <p>Detail work with records, codes and insurance claims, with little or no patient contact &mdash;
            the most remote-friendly healthcare path once you have some experience.</p>
            <div class="program-meta"><span><strong>Roles:</strong> Medical Billing &amp; Coding, Medical Administrative Assistant</span></div>
          </article>
        </div>
        <p class="note"><strong>License vs. certification &mdash; an important difference.</strong> A
        <em>license</em> is government permission you must have before you can work; a <em>certification</em> is
        a voluntary credential that shows employers you&rsquo;re qualified. Some healthcare roles are licensed
        or regulated (nurse aide and pharmacy technician are common examples), while many others &mdash; billing
        and coding, medical assistant, phlebotomy, EKG and medical admin &mdash; usually have no license, so a
        voluntary national certification is what employers look for. The exact rules depend on your state.</p>
      </div>
    </section>
""" + career_pay_block() + """

    <section class="section section--tight">
      <div class="container">
        <div class="faq">
          <p class="faq-group-title">Healthcare careers FAQ</p>
""" + "\n".join(f'''          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>''' for q, a in _HC_FAQ) + """
        </div>
      </div>
    </section>

""" + field_interest("healthcare", "medical", "healthcare training") + """

    <section class="section">
      <div class="container">
        <h2 class="related-title">Related guides</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="blog/can-medical-billing-coding-be-learned-online.html"><h3>Can Medical Billing &amp; Coding Be Learned Online?</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="wioa-explained.html"><h3>WIOA Training Funds Explained</h3><span class="read-link">Read the guide</span></a>
          <a class="post-card" href="qualify.html"><h3>Do I Qualify for Training Funding?</h3><span class="read-link">Check your options</span></a>
        </div>
      </div>
    </section>
"""))


# ---- it-careers.html ------------------------------------------------------
# Location-neutral career reference (Site Structure Spec v1.5): no "Massachusetts"
# framing, no pay figures (hidden PAY-DATA slot, R-PAY-DATA).
_IT_FAQ = [
    ("Can I get an IT job without a degree?",
     "Often yes. Many employers hire for entry-level help desk and support roles based on skills and certifications rather than a four-year degree. A certification like CompTIA A+ or Tech+ plus some hands-on practice is a common way in."),
    ("What IT certification should I start with?",
     "Most people start with CompTIA A+ or Tech+ for help desk work, then add Network+ for networking or Security+ for cybersecurity. Cloud roles use vendor certifications such as AWS, Microsoft Azure or Google Cloud fundamentals."),
    ("Can I learn IT online?",
     "Yes. IT is one of the most online-friendly fields. You can study the material and build a free home lab on your own computer to practice the skills employers test for."),
    ("Which IT job should I aim for first?",
     "Almost everyone starts on the help desk or in user support. It gets you in the door with a short certificate, and it&rsquo;s the foundation for networking, security and cloud roles later. The higher-paying roles assume you already know the basics."),
    ("Is IT support still a good field with AI around?",
     "Demand for user support is steady rather than booming, with thousands of openings each year as people move up or retire. The work is shifting toward troubleshooting, security and cloud tools, so keeping your skills current matters."),
    ("Does Career Skills Center offer IT training?",
     "Not yet. Career Skills Center plans to offer training in healthcare, IT and the skilled trades. Join the interest list to get updates when we launch."),
]

PAGES.append(dict(
    slug="it-careers.html", nav="it-careers.html",
    title="IT Careers: Jobs, Certifications &amp; How to Get Started | Career Skills Center",
    ogtitle="IT Careers: Jobs, Certifications & How to Get Started",
    desc="A plain guide to IT careers: help desk, networking, cybersecurity and cloud. Which certifications to start with, whether you can train online, and how to pay for training.",
    extrahead=faq_ld(_IT_FAQ),
    main=hero("Career Paths &middot; Information Technology",
              "IT Careers: Jobs, Certifications and How to Get Started",
              "Information technology is a common way into a stable, well-paid career without a four-year "
              "degree. Most people start on the help desk. Here&rsquo;s what the roles are, which certifications "
              "to start with, and how to pay for training.",
              "images/comptia.webp", ("Do I Qualify?", "qualify.html")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The field</p>
        <h2 class="section-title left">Is IT right for you?</h2>
        <p class="lede">IT suits people who like solving problems, are patient with others, and enjoy learning
        new tools. Most careers start with help desk or user support &mdash; setting up computers, fixing
        everyday problems and helping people &mdash; and grow from there into networking, security or cloud.
        You can learn most of it online, and certifications matter more than a degree for getting your first
        job.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Common roles</p>
        <h2 class="section-title left">IT roles you can train for</h2>
        <div class="section-intro"><p>For each role: what the job is, the typical training path, the
        certifications employers look for, and whether you can train online. IT roles generally don&rsquo;t
        require a government license &mdash; certifications are how you show you&rsquo;re ready.</p></div>
""" + role_grid(
        role_card("Help Desk / User Support",
                  "The most common way into tech. Set up computers, fix everyday problems and help people use software and networks.",
                  "Short online course; a free home lab to practice.",
                  "CompTIA A+ or Tech+ (voluntary but employer-preferred).",
                  "Yes &mdash; fully online-friendly. A free home lab helps you practice.",
                  "No license required; certifications are voluntary."),
        role_card("Network Support Technician",
                  "Keep an organization&rsquo;s networks running: routers, switches, Wi-Fi and connections between systems.",
                  "Online coursework plus hands-on labs; usually after A+.",
                  "CompTIA Network+.",
                  "Yes, with virtual or home labs to practice on.",
                  "No license required; certifications are voluntary."),
        role_card("Entry-Level Cybersecurity",
                  "Help protect systems and data from attacks: monitoring, access, and following security procedures.",
                  "Usually after some help desk or networking experience.",
                  "CompTIA Security+ (a common starting security cert).",
                  "Yes for coursework; expect to build lab and hands-on experience.",
                  "No license required; certifications are voluntary."),
        role_card("Cloud Support",
                  "Help run services on cloud platforms like AWS, Microsoft Azure and Google Cloud.",
                  "Online coursework plus vendor certifications; often after help-desk or networking.",
                  "AWS Cloud Practitioner, Microsoft Azure AZ-900, or Google Cloud Digital Leader.",
                  "Yes &mdash; cloud work is inherently online.",
                  "No license required; certifications are voluntary."),
    ) + """
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The training ladder</p>
        <h2 class="section-title left">Where you start and where it leads</h2>
        <div class="section-intro"><p>IT is built in rungs. The entry courses assume you know nothing; the
        higher-paying ones assume you already know the basics. Certifications &mdash; not a four-year degree
        &mdash; are how you show an employer you&rsquo;re ready for the next step. Almost everyone starts on the
        help desk and climbs from there.</p></div>
        <div class="ladder">
          <article class="ladder-step is-entry">
            <p class="ladder-rank">Start here &middot; no experience needed</p>
            <h3>Help desk &amp; user support</h3>
            <p>Where almost everyone begins. You learn to set up computers, fix everyday problems, and help
            people use software and networks. State-funded IT courses are short certificate programs aimed at
            this rung &mdash; they get you in the door, not straight to a senior salary.</p>
            <div class="ladder-meta"><span><strong>Train for:</strong> CompTIA Tech+ (FC0-U71), then CompTIA A+</span><span><strong>Leads to:</strong> networking, security and cloud roles</span></div>
          </article>
          <article class="ladder-step">
            <p class="ladder-rank">Next step &middot; builds on the basics</p>
            <h3>Network support</h3>
            <p>Once you understand hardware and operating systems, networking is the natural next move:
            routers, switches, Wi-Fi, and how machines talk to each other.</p>
            <div class="ladder-meta"><span><strong>Train for:</strong> CompTIA Network+ (A+ first)</span><span><strong>Grows toward:</strong> network administration</span></div>
          </article>
          <article class="ladder-step">
            <p class="ladder-rank">Higher pay &middot; needs prior knowledge</p>
            <h3>Cybersecurity</h3>
            <p>Security roles pay well but are rarely a first job. Employers expect you to already understand
            systems and networks. Security+ is the common starting certification once you have help-desk or
            networking experience behind you.</p>
            <div class="ladder-meta"><span><strong>Train for:</strong> CompTIA Security+ (after A+/Network+ or work experience)</span></div>
          </article>
          <article class="ladder-step">
            <p class="ladder-rank">Higher pay &middot; needs prior knowledge</p>
            <h3>Cloud support</h3>
            <p>Cloud platforms &mdash; Amazon AWS, Microsoft Azure and Google Cloud &mdash; run much of today&rsquo;s
            software. Cloud roles usually come after some help-desk or networking experience.</p>
            <div class="ladder-meta"><span><strong>Train for:</strong> AWS Cloud Practitioner, Microsoft Azure AZ-900, or Google Cloud Digital Leader</span></div>
          </article>
          <article class="ladder-step">
            <p class="ladder-rank">A separate path</p>
            <h3>Programming &amp; software</h3>
            <p>Writing code is its own track rather than a step up from the help desk. Certifications matter
            less here than a portfolio of real projects and knowing a language such as Python or JavaScript. It
            can pay very well, but the learning curve is steeper and longer than an entry IT certificate.</p>
            <div class="ladder-meta"><span><strong>Train through:</strong> a bootcamp or structured self-study, plus a project portfolio</span></div>
          </article>
        </div>
        <p class="note"><strong>Start on the ladder, then climb.</strong> A short certificate is a real way in,
        but it prepares you for the entry rung &mdash; usually help desk or user support &mdash; not a senior
        salary on day one. The higher-paying IT roles (security, cloud, software) assume you already know the
        basics and often expect prior experience or a degree. Plan to start on the help desk and add
        certifications and experience to move up. Certifications, not a four-year degree, are how you show
        you&rsquo;re ready for the next step.</p>
      </div>
    </section>
""" + career_pay_block() + """

    <section class="section section--tight">
      <div class="container">
        <div class="faq">
          <p class="faq-group-title">IT careers FAQ</p>
""" + "\n".join(f'''          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>''' for q, a in _IT_FAQ) + """
        </div>
      </div>
    </section>

""" + field_interest("it", "it", "IT training") + """

    <section class="section">
      <div class="container">
        <h2 class="related-title">Related guides</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="blog/can-you-learn-it-support-online.html"><h3>Can You Learn IT Support Online?</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="wioa-explained.html"><h3>WIOA Training Funds Explained</h3><span class="read-link">Read the guide</span></a>
          <a class="post-card" href="qualify.html"><h3>Do I Qualify for Training Funding?</h3><span class="read-link">Check your options</span></a>
        </div>
      </div>
    </section>
"""))


# ---- it-careers-massachusetts-draft.html (WORKING DRAFT - course-focused) --
def course_card(course, blurb, trains_for, length, cert, online, note=""):
    extra = ('\n              <div><dt>Good to know</dt><dd>%s</dd></div>' % note) if note else ""
    return """          <article class="role-card">
            <h3 class="role-name">%s</h3>
            <p class="role-blurb">%s</p>
            <dl class="role-facts">
              <div><dt>Trains you for</dt><dd>%s</dd></div>
              <div><dt>Typical length</dt><dd>%s</dd></div>
              <div><dt>Certification</dt><dd>%s</dd></div>
              <div><dt>Typical starting pay</dt><dd><span class="tbd">Entry-level &mdash; sourcing current figures</span></dd></div>
              <div><dt>Can you train online?</dt><dd>%s</dd></div>%s
            </dl>
          </article>""" % (course, blurb, trains_for, length, cert, online, extra)

_ITD_FAQ = [
    ("Do I need a college degree to get an IT job in Massachusetts?",
     "Often no. Many employers hire for entry-level help desk and support roles based on skills and a certification like CompTIA A+, rather than a four-year degree."),
    ("How long do these courses take?",
     "Most are short &mdash; a few weeks to about four months &mdash; and prepare you for a certification exam. They are not two- or four-year college degrees."),
    ("Which course should I start with?",
     "Most people start with CompTIA A+ (or the more basic CompTIA Tech+) for help desk work, then add Network+ for networking or Security+ for security later."),
    ("Can I learn IT online?",
     "Yes. IT is one of the most online-friendly fields. You can study the material and build a free home lab on your own computer to practice."),
    ("How much will I earn?",
     "These courses lead to entry-level jobs, so expect entry-level pay to start &mdash; it rises with experience and added certifications. We are sourcing accurate Massachusetts starting-wage figures and will add them per course."),
    ("Does Career Skills Center offer these courses?",
     "Not yet. Career Skills Center plans to offer training in healthcare, IT and the skilled trades. Join the interest list to get updates when we launch."),
]

PAGES.append(dict(
    slug="it-careers-massachusetts-draft.html", nav="",
    title="DRAFT - IT Courses You Can Train For in Massachusetts | Career Skills Center",
    ogtitle="IT Courses You Can Train For in Massachusetts (DRAFT)",
    desc="Working draft: short IT courses a Massachusetts training voucher can cover, the job each trains you for, and how funding works.",
    extrahead='  <meta name="robots" content="noindex">\n' + faq_ld(_ITD_FAQ),
    main=hero("Career Paths &middot; Information Technology",
              "IT Courses You Can Train For in Massachusetts",
              "A Massachusetts training voucher can pay for short IT courses that prepare you for a "
              "certification and an entry-level job &mdash; no four-year degree required. Here are the courses a "
              "voucher commonly covers, what each one trains you for, and how to get funding.",
              "images/comptia.webp", ("Check Your Options", "qualify.html")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The field in Massachusetts</p>
        <h2 class="section-title left">Is IT right for you?</h2>
        <p class="lede">IT suits people who like solving problems, are patient with others, and enjoy learning
        new tools. Most careers start with help desk or user support &mdash; setting up computers, fixing
        everyday problems and helping people &mdash; and grow from there into networking, security or cloud.
        You can learn most of it online, and a certification matters more than a degree for getting your first
        job.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Courses &amp; pay</p>
        <h2 class="section-title left">IT courses a training voucher can pay for</h2>
        <div class="section-intro"><p>These are the short IT courses a MassHire training voucher (an
        Individual Training Account, or ITA) commonly covers. Each one prepares you for an industry
        certification and an entry-level job &mdash; they are <strong>not</strong> two- or four-year college
        degrees. Most run only a few weeks to about four months, so the pay to expect is entry-level: what
        people earn starting out, which grows with experience and added certifications.</p></div>
""" + role_grid(
        course_card("IT Support (CompTIA A+)",
                    "The core entry course for tech. Learn to set up computers, fix everyday problems, and support people using software and networks.",
                    "Help Desk / User Support Specialist",
                    "Short &mdash; a few weeks to a few months",
                    "CompTIA A+ (some begin with the more basic CompTIA Tech+)",
                    "Yes &mdash; fully online-friendly; a free home lab helps you practice."),
        course_card("Networking (CompTIA Network+)",
                    "Builds on A+. Learn how routers, switches, Wi-Fi and the connections between systems work.",
                    "Network Support Technician",
                    "Short &mdash; a few weeks to a few months",
                    "CompTIA Network+",
                    "Yes, with virtual or home labs to practice on.",
                    note="Usually taken after CompTIA A+ or some help-desk experience."),
        course_card("Cybersecurity (CompTIA Security+)",
                    "An introduction to protecting systems and data: monitoring, access, and security procedures.",
                    "Entry security / IT support with a security focus",
                    "Short &mdash; a few weeks to a few months",
                    "CompTIA Security+",
                    "Yes for coursework; expect to build hands-on lab experience.",
                    note="Security+ is usually taken after A+/Network+ or IT experience &mdash; it is rarely a first job. The six-figure &lsquo;security analyst&rsquo; salaries advertised elsewhere generally require a bachelor&rsquo;s degree and years of experience."),
        course_card("Cloud fundamentals (AWS / Azure / Google Cloud)",
                    "An introduction to running services on cloud platforms.",
                    "Junior cloud or IT support",
                    "Short &mdash; a few weeks to a few months",
                    "AWS Cloud Practitioner, Microsoft Azure AZ-900, or Google Cloud Digital Leader",
                    "Yes &mdash; cloud work is inherently online.",
                    note="Usually taken after some help-desk or networking experience."),
    ) + """
        <p class="note"><strong>Why we don&rsquo;t show a single salary yet.</strong> Pay for these jobs
        varies, and the career-wide &ldquo;median&rdquo; figures you see elsewhere overstate what a new
        certificate-holder earns. We&rsquo;re sourcing accurate <em>entry-level</em> Massachusetts wage data and
        will add it to each course.</p>
        <p>Longer paths such as software development or programming also exist and can pay well, but they
        usually take more than a few months and aren&rsquo;t typically short voucher courses.</p>
      </div>
    </section>

""" + pay_for_training_block() + outward_next_step("an IT career") + """

    <section class="section section--tight">
      <div class="container">
        <div class="faq">
          <p class="faq-group-title">IT courses FAQ</p>
""" + "\n".join('''          <details class="faq-item">
            <summary>%s</summary>
            <div class="faq-body"><p>%s</p></div>
          </details>''' % (q, a) for q, a in _ITD_FAQ) + """
        </div>
      </div>
    </section>

""" + field_interest("it", "it", "IT training") + """

    <section class="section">
      <div class="container">
        <h2 class="related-title">Related guides</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="blog/can-you-learn-it-support-online.html"><h3>Can You Learn IT Support Online?</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="blog/free-job-training-massachusetts.html"><h3>Free Job Training in Massachusetts</h3><span class="read-link">Read article</span></a>
        </div>
      </div>
    </section>
"""))


# ---- skilled-trades-careers-massachusetts.html ----------------------------
# Location-neutral career reference (Site Structure Spec v1.5): no "Massachusetts"
# framing except the clearly labeled licensing example; no pay figures (R-PAY-DATA).
_TR_FAQ = [
    ("Can I learn a skilled trade online?",
     "Only partly. You can study theory, code and safety online, but the trades are hands-on and licenses require supervised, in-person work hours. The honest path pairs online or classroom coursework with an apprenticeship."),
    ("How long does it take to get licensed in a trade?",
     "It varies by trade and by state. Licensed trades typically require a mix of classroom hours and thousands of supervised, on-the-job hours &mdash; often a 4- to 5-year apprenticeship &mdash; before you sit for a state exam. Always check the rules where you plan to work."),
    ("Do I need a license for every trade?",
     "No. Electricians, plumbers and refrigeration/HVAC technicians are licensed in most states, with requirements set by state boards. Welding generally has no statewide license &mdash; employers use hands-on weld tests and voluntary AWS certification."),
    ("How do I pay for trade training?",
     "Registered apprenticeships let you earn while you learn. You may also qualify for publicly funded training. See our funding guides and use the Do I Qualify? check."),
    ("Does Career Skills Center offer skilled trades training?",
     "Not yet. Career Skills Center plans to offer training in healthcare, IT and the skilled trades. Join the interest list to get updates when we launch."),
]

PAGES.append(dict(
    slug="skilled-trades-careers.html", nav="skilled-trades-careers.html",
    title="Skilled Trades Careers: Jobs, Licensing &amp; Apprenticeships | Career Skills Center",
    ogtitle="Skilled Trades Careers: Jobs, Licensing & Apprenticeships",
    desc="A plain guide to skilled trades careers: electrician, HVAC/R, plumber and welder. How licensing and apprenticeships work, whether you can train online, and how to pay for training.",
    extrahead=faq_ld(_TR_FAQ),
    main=hero("Career Paths &middot; Skilled Trades",
              "Skilled Trades Careers: Jobs, Licensing and Apprenticeships",
              "The trades pay well, can&rsquo;t be shipped overseas, and are hiring. They are also hands-on and, "
              "in most states, licensed. Here&rsquo;s what the work is, how licensing and apprenticeships work, "
              "and how to pay for training.",
              "images/electrician.webp", ("Do I Qualify?", "qualify.html")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The field</p>
        <h2 class="section-title left">Are the trades right for you?</h2>
        <p class="lede">The trades suit people who like working with their hands, solving physical problems, and
        seeing the result of a day&rsquo;s work. The trade-off compared with office jobs: the work is physical,
        and most licensed trades combine classroom hours with thousands of supervised, on-the-job hours. That
        path takes time, but you can earn while you learn.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Common roles</p>
        <h2 class="section-title left">Skilled trades you can train for</h2>
        <div class="section-intro"><p>For each trade: what the work is, the typical training path, the
        certifications involved, and whether you can train online. Licensing rules vary by state &mdash; the
        example table further down uses Massachusetts; check the rules where you plan to work.</p></div>
""" + role_grid(
        role_card("Electrician",
                  "Install and maintain wiring, power, lighting and control systems in homes and businesses.",
                  "An apprenticeship: classroom hours plus supervised on-the-job hours over about four years.",
                  "State journeyman license (via exam); no national certificate required.",
                  "Partly. Some related theory can be online, but licensing requires supervised in-person hours.",
                  "Licensed in most states. Example (Massachusetts): journeyman (Class B) needs 8,000 supervised hours over at least four years plus a 600-hour course, then the state exam."),
        role_card("HVAC/R Technician",
                  "Install and service heating, air conditioning and refrigeration systems.",
                  "An apprenticeship or approved study, plus federal EPA 608 certification to handle refrigerant.",
                  "Federal EPA 608 (required to handle refrigerant); plus a state license where required.",
                  "Partly. Theory and EPA 608 exam prep can be online; hands-on hours are in person.",
                  "Licensing varies by state. Example (Massachusetts): a refrigeration technician license (6,000 apprentice hours, or 450 hours of approved study) plus federal EPA 608."),
        role_card("Plumber",
                  "Install and repair pipes, fixtures and systems that carry water and gas.",
                  "An apprenticeship: practical hours plus theory over about three years, then the journeyman exam.",
                  "State journeyman license (via exam); gas fitting is often licensed separately.",
                  "Partly. Some theory can be online; supervised hours are in person.",
                  "Licensed in most states. Example (Massachusetts): apprentices need at least 5,100 practical hours plus 300 hours of theory before the journeyman exam."),
        role_card("Welder",
                  "Join metal parts for construction, manufacturing and repair using heat and specialized tools.",
                  "A short technical program plus a lot of hands-on practice.",
                  "Voluntary AWS (American Welding Society) certification; employer weld tests.",
                  "Mostly no &mdash; welding is a hands-on skill you build in a shop.",
                  "Generally no statewide license; employers rely on weld tests and AWS certification."),
    ) + """
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Getting in</p>
        <h2 class="section-title left">How you actually get into a trade</h2>
        <div class="section-intro"><p>The trades work differently from healthcare or IT. You can&rsquo;t certify
        your way in from a laptop &mdash; but you also don&rsquo;t pay for years of school up front. You learn
        the theory and get paid to do the hands-on work at the same time.</p></div>
        <ol class="check-list check-list--num">
          <li><strong>Learn the theory.</strong> Code, safety, math and how systems work &mdash; this part can
          be online or in a classroom. Many people also do OSHA 10 or 30 safety training here, and, for
          HVAC/refrigeration, prep for the federal EPA 608 certification.</li>
          <li><strong>Get into a registered apprenticeship.</strong> You work under a licensed tradesperson and earn a paid wage while you build the supervised hours your state requires. BLS describes trade apprenticeships as 4- to 5-year programs with about 2,000 hours of paid on-the-job training each year.</li>
          <li><strong>Log your hours and classroom time.</strong> Each trade sets its own mix of on-the-job
          hours and classroom hours.</li>
          <li><strong>Pass the state exam and get licensed.</strong> Once you meet the hours and pass the exam
          you become a journeyman &mdash; and your pay steps up.</li>
        </ol>
        <h3 class="mt-lg">Example: how licensing works in Massachusetts</h3>
        <p>Licensing is set state by state. The table below is a <strong>Massachusetts example</strong> to show
        the shape of the requirements &mdash; the specific hours and boards differ where you live, so always
        check your own state.</p>
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr><th>Trade</th><th>Classroom / theory</th><th>Supervised work hours</th><th>License (MA example)</th><th>Also required</th></tr>
            </thead>
            <tbody>
              <tr><th>Electrician</th><td>600-hour Journeyman&rsquo;s Course</td><td>8,000 hours over at least 4 years</td><td>Journeyman (Class B) exam &mdash; Board of State Examiners of Electricians</td><td>&mdash;</td></tr>
              <tr><th>HVAC/R Technician</th><td>450 hours approved study (or 6,000 apprentice hours)</td><td>Included in the apprentice route</td><td>Refrigeration Technician license</td><td>Federal EPA 608 to handle refrigerant</td></tr>
              <tr><th>Plumber</th><td>300 hours of theory</td><td>5,100 practical hours (about 3 years)</td><td>Journeyman exam &mdash; Board of Plumbers &amp; Gas Fitters</td><td>Gas fitting is licensed separately</td></tr>
              <tr><th>Welder</th><td>Short technical program</td><td>Plenty of hands-on shop practice</td><td>No statewide license</td><td>Voluntary AWS certification; employer weld tests</td></tr>
            </tbody>
          </table>
        </div>
        <p class="role-src">Massachusetts example sources: mass.gov licensing boards (237 CMR 13 electricians; 248 CMR 11 plumbers), Massachusetts Refrigeration Technician licensing, and federal EPA 608. Checked 2026.</p>
        <p class="note"><strong>What online learning can and can&rsquo;t do.</strong> You can genuinely learn the
        theory, code and safety online, and do OSHA and EPA 608 exam prep on a screen. What you cannot do online
        is the supervised, hands-on hours a license requires &mdash; those happen on real job sites under a
        licensed tradesperson. Treat online study as the classroom half of an apprenticeship, not a replacement
        for it.</p>
      </div>
    </section>
""" + career_pay_block() + """

    <section class="section section--tight">
      <div class="container">
        <div class="faq">
          <p class="faq-group-title">Skilled trades FAQ</p>
""" + "\n".join(f'''          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>''' for q, a in _TR_FAQ) + """
        </div>
      </div>
    </section>

""" + field_interest("trades", "trades", "skilled trades training") + """

    <section class="section">
      <div class="container">
        <h2 class="related-title">Related guides</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="blog/can-you-learn-a-trade-online.html"><h3>Can You Learn a Skilled Trade Online?</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="apprenticeships.html"><h3>Apprenticeship Programs (for Employers)</h3><span class="read-link">Read more</span></a>
          <a class="post-card" href="qualify.html"><h3>Do I Qualify for Training Funding?</h3><span class="read-link">Check your options</span></a>
        </div>
      </div>
    </section>
"""))


# ---- career-paths.html (STEP 4 — hub; 301 target for our-programs/programs) --
PAGES.append(dict(
    slug="career-paths.html", nav="career-paths.html",
    title="Career Paths: Explore Fields You Can Train For | Career Skills Center",
    ogtitle="Career Paths",
    desc="Explore careers you can train for — healthcare, information technology and the skilled trades. See what each field involves, how to train, and how to get help paying for it.",
    main=hero("Career Paths", "Explore Careers You Can Train For",
              "Three fields with clear ways in and no four-year degree required. Each guide covers what the "
              "jobs are, how to train, and how to get help paying for it.",
              None, ("Do I Qualify?", "qualify.html")) + """

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Explore the fields</p>
        <h2 class="section-title left">Choose a field</h2>
        <!-- COURSE-DEPENDENT: R-HUB — guide mode: cards link to field guides. In
             course mode, show a "Now enrolling" badge + course link for live fields
             (COURSES_LIVE.*). -->
        <div class="pcard-grid">

          <article class="pcard">
            <img src="images/medicalbilling.webp" alt="Healthcare worker" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <h3 class="pcard-title">Healthcare</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Billing and coding, medical assistant, phlebotomy, pharmacy tech, CNA and more &mdash; steady work, often trainable in months, some fully online.</p>
              <a class="btn btn-outline-navy" href="healthcare-careers.html">Explore healthcare</a>
            </div>
          </article>

          <article class="pcard">
            <img src="images/comptia.webp" alt="IT support technician at work" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <h3 class="pcard-title">Information Technology</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Help desk, networking, cybersecurity and cloud &mdash; a common way into a well-paid tech career without a four-year degree.</p>
              <a class="btn btn-outline-navy" href="it-careers.html">Explore IT</a>
            </div>
          </article>

          <article class="pcard">
            <img src="images/electrician.webp" alt="Electrician at work" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <h3 class="pcard-title">Skilled Trades</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Electrician, HVAC/R, plumber and welder &mdash; licensed trades that pay well and can&rsquo;t be shipped overseas. Earn while you learn through an apprenticeship.</p>
              <a class="btn btn-outline-navy" href="skilled-trades-careers.html">Explore the trades</a>
            </div>
          </article>

        </div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How training works</p>
        <h2 class="section-title left">How training differs by field</h2>
        <div class="section-intro"><p>The three fields ask for very different things. Here&rsquo;s the honest
        shape of each before you pick one.</p></div>
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr><th>Field</th><th>Time to first job</th><th>Where you learn</th><th>Credential</th><th>Pay while training</th></tr>
            </thead>
            <tbody>
              <tr><th>Healthcare</th><td>A few months to about a year for entry roles</td><td>Mostly online, plus short in-person clinical practice</td><td>State registry (CNA) or a voluntary national certification</td><td>You usually pay for the course; may qualify for state funding</td></tr>
              <tr><th>Information Technology</th><td>Weeks to a few months per certification</td><td>Mostly online, with a free home lab to practice</td><td>CompTIA and vendor certifications &mdash; not a four-year degree</td><td>You usually pay for the course; may qualify for state funding</td></tr>
              <tr><th>Skilled Trades</th><td>Several years to a full license</td><td>Online or classroom theory, plus on-the-job apprenticeship</td><td>A state license after supervised hours and an exam</td><td>You earn a wage as an apprentice</td></tr>
            </tbody>
          </table>
        </div>
        <p class="note">State-funded short courses open the <em>entry-level</em> doors in each field. They&rsquo;re
        certificates, not degrees, so the first job is usually an entry role &mdash; help desk in IT, a nurse aide
        or phlebotomist in healthcare, an apprentice in the trades &mdash; and pay grows from there with
        experience and further training. Each guide below is honest about where a field starts and where it can
        lead.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Not sure yet?</p>
        <h2 class="section-title left">See what help you may qualify for</h2>
        <p>Answer a few quick questions and we&rsquo;ll point you to the right next steps for publicly funded
        training &mdash; no cost, no obligation.</p>
        <p><a class="btn btn-yellow" href="qualify.html">Do I Qualify?</a></p>
      </div>
    </section>

""" + field_interest("hub", "unsure", "training in these fields")))


# ===========================================================================
# v1.5 NEW PAGES — Funding Guides + For Employers (Site Structure Spec v1.5)
# ===========================================================================

# ---- wioa-explained.html (Funding Guides) ---------------------------------
# Reference page. WIOA structure and Massachusetts process facts are sourced in
# docs/VERIFICATION_LOG.md (B1, B2, B5, B6, B7, B8, B10, B11, B12). Do NOT state
# statewide ITA dollar caps — the FY27 ETPL policy sets none (B12).
_WIOA_FAQ = [
    ("What is WIOA?",
     "WIOA stands for the Workforce Innovation and Opportunity Act, the main federal law that pays for job training in the United States. Each state runs it locally. In Massachusetts, you access it through a MassHire career center."),
    ("Who qualifies for WIOA training funds?",
     "WIOA serves three groups: Adults, Dislocated Workers (people laid off or whose jobs ended), and Youth (ages 14–24). Within the adult program, people who receive public assistance, are low income, or are basic-skills deficient get priority of service, and veterans and eligible spouses get priority across all programs. Your local career center makes the final decision."),
    ("How much does WIOA pay for training?",
     "It pays tuition for training programs that are on the state Eligible Training Provider List (ETPL). There is no single statewide dollar cap in Massachusetts — the amount is set locally, and some career centers also help with related costs like books or exam fees. Ask your counselor exactly what yours covers."),
    ("What is an ITA?",
     "An Individual Training Account (ITA) is the WIOA voucher that pays your tuition at an approved training provider. You choose an eligible program with your career counselor, and the ITA covers the approved cost."),
    ("Can I get paid while I train?",
     "If you are collecting unemployment, ask about Section 30 (the Training Opportunities Program). It can keep your unemployment checks coming while you train full time and add up to 26 extra weeks of benefits. It does not pay tuition — you pair it with an ITA. You generally must apply by your 20th compensable week of benefits."),
    ("Does Career Skills Center accept WIOA funding?",
     "Not yet. Career Skills Center is working toward approval to accept these funds and plans to offer training in healthcare, IT and the skilled trades. Only your MassHire career center can approve funding. Join the interest list for updates."),
]

PAGES.append(dict(
    slug="wioa-explained.html", nav="wioa-explained.html",
    title="WIOA Training Funds Explained: Who Qualifies and How to Apply in Massachusetts | Career Skills Center",
    ogtitle="WIOA Training Funds Explained: Who Qualifies and How to Apply",
    desc="A plain-language guide to WIOA training funds: the three eligibility groups, priority of service, the ITA voucher, the ETPL, and the step-by-step process to apply in Massachusetts.",
    extrahead=faq_ld(_WIOA_FAQ),
    main=hero("Funding Guides &middot; WIOA",
              "WIOA Training Funds Explained",
              "WIOA is the main public program that pays for job training in the United States. Here&rsquo;s who "
              "qualifies, what it covers, and the exact steps to apply through a MassHire career center in "
              "Massachusetts.",
              None, ("Do I Qualify?", "qualify.html")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The basics</p>
        <h2 class="section-title left">What WIOA is</h2>
        <p class="lede">WIOA stands for the <strong>Workforce Innovation and Opportunity Act</strong> &mdash; the
        main federal law that funds job training across the country. The money is federal, but each state runs
        the program through local offices. In Massachusetts, those offices are the <strong>MassHire career
        centers</strong>, and the training you can pay for must be on the state&rsquo;s approved list.</p>
        <p>WIOA is not a loan and not a scholarship you apply to online. It works through a career counselor who
        checks your eligibility, helps you build a plan, and approves a voucher for an approved program.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Who it&rsquo;s for</p>
        <h2 class="section-title left">The three groups WIOA serves</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Adults</h3>
            <p>Adults 18 and over who want training for a better job. Priority goes to people on public
            assistance, with low income, or who need to build basic skills.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Dislocated Workers</h3>
            <p>People who were laid off, whose job or plant closed, or who otherwise lost work through no fault
            of their own &mdash; including some who received a layoff notice.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Youth</h3>
            <p>Young people ages 14–24, with services aimed at education, skills and a first career step.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Priority of service</p>
        <h2 class="section-title left">Who gets served first</h2>
        <p>Funds are limited, so the adult program serves some people ahead of others. Priority of service goes
        to:</p>
        <ul class="check-list">
          <li>People who receive public assistance (such as SNAP or TAFDC)</li>
          <li>Other low-income individuals</li>
          <li>People who are &ldquo;basic skills deficient&rdquo; (need to build reading, writing or math skills)</li>
        </ul>
        <p><strong>Veterans and eligible spouses</strong> receive priority of service across all U.S. Department
        of Labor–funded programs. You do not have to be in one of these groups to qualify &mdash; but if you
        are, you move toward the front of the line.</p>
        <p class="role-src">Source: U.S. Department of Labor, WIOA Adult program (priority of service);
        veterans&rsquo; priority under the Jobs for Veterans Act.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The voucher</p>
        <h2 class="section-title left">The ITA: what it covers and what it doesn&rsquo;t</h2>
        <p>The voucher is called an <strong>Individual Training Account (ITA)</strong>. Here&rsquo;s the honest
        picture:</p>
        <ul class="check-list">
          <li><strong>It pays tuition</strong> for an approved training program you choose with your counselor.</li>
          <li><strong>It may cover related costs</strong> like books, fees or exam vouchers &mdash; this depends
          on your career center, so ask.</li>
          <li><strong>There is no single statewide dollar cap</strong> in Massachusetts; the amount is set
          locally.</li>
          <li><strong>It does not pay your living expenses.</strong> If you collect unemployment, Section 30
          (below) can keep those checks coming while you train.</li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The approved list</p>
        <h2 class="section-title left">Why the program must be on the ETPL</h2>
        <p>WIOA money can only pay for training that is on the state&rsquo;s <strong>Eligible Training Provider
        List (ETPL)</strong>. The ETPL is the state&rsquo;s vetted list of schools and programs that have shown
        they lead to real jobs. If a program isn&rsquo;t on the list, an ITA can&rsquo;t pay for it &mdash; so
        one of the first things to check is whether the training you want is listed. Your career counselor can
        confirm this with you.</p>
        <p class="role-src">Source: Massachusetts ETPL policy (100 DCS 14.106.2, FY27).</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How to apply</p>
        <h2 class="section-title left">Step by step in Massachusetts</h2>
        <p>Exact steps vary by career center, but the path usually looks like this &mdash; and it takes roughly
        <strong>six to eight weeks</strong> from your first visit to an approved voucher:</p>
        <ol class="check-list check-list--num">
          <li><strong>Register.</strong> Create a MyMassGov account and register on <a class="link-yellow" href="https://jobquest.mass.gov" target="_blank" rel="noopener">JobQuest</a>. You need a JobQuest account before you can get training funding.</li>
          <li><strong>Connect with a MassHire career center.</strong> <a class="link-yellow" href="https://www.mass.gov/info-details/masshire-career-center-locations" target="_blank" rel="noopener">Find your nearest location</a> and attend a Training Information Meeting (some centers use a required video).</li>
          <li><strong>Take a basic-skills assessment</strong> (often the TABE) so your counselor can build the right plan with you.</li>
          <li><strong>Build a career plan and gather documents</strong> with your counselor (ID, income, work history).</li>
          <li><strong>Pick an ETPL-approved program</strong> in your field.</li>
          <li><strong>Get your ITA approved</strong> and start training.</li>
        </ol>
        <p><strong>Collecting unemployment?</strong> Ask about <strong>Section 30 (the Training Opportunities
        Program)</strong>. If you train at least 20 hours a week, it can keep your unemployment checks coming and
        add up to 26 extra weeks of benefits. You generally must apply by your <strong>20th compensable
        week</strong>. Section 30 doesn&rsquo;t pay tuition &mdash; you pair it with an ITA.</p>
        <p class="role-src">Sources: MassHire career center process pages; mass.gov Training Opportunities
        Program (Section 30).</p>
      </div>
    </section>

    <!-- COURSE-DEPENDENT: R-WIOA — the "working toward approval / plans to offer"
         line about CSC changes once CSC is an approved provider / has live courses. -->
    <section class="section">
      <div class="container narrow">
""" + FUNDING_NOTE + """
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Your next step</p>
        <h2 class="section-title left">See where you may fit</h2>
        <p>The quickest way to understand your options is our free check. It never gives a yes/no verdict &mdash;
        only your career center can do that &mdash; but it shows which WIOA group you may fit and what to do
        next.</p>
        <p><a class="btn btn-yellow" href="qualify.html">Do I Qualify?</a></p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="faq">
          <p class="faq-group-title">WIOA FAQ</p>
""" + "\n".join(f'''          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>''' for q, a in _WIOA_FAQ) + """
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="related-title">Related guides</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="blog/free-job-training-massachusetts.html"><h3>Free Job Training in Massachusetts</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="blog/masshire-training-voucher.html"><h3>How to Get a MassHire Training Voucher (ITA)</h3><span class="read-link">Read article</span></a>
          <a class="post-card" href="express-program-explained.html"><h3>Express Program Explained (Employers)</h3><span class="read-link">Read the guide</span></a>
        </div>
      </div>
    </section>
"""))


# ---- express-program-explained.html (Funding Guides) ----------------------
# Reference page for employers. All rates/caps come from js/site-config.js via
# [data-cfg] spans (hard rule: funding numbers live only in the config), and each
# renders "[VERIFY]" until the figures are confirmed with express@commcorp.org.
_EXPRESS_FAQ = [
    ("What is the Workforce Training Fund Express Program?",
     "It&rsquo;s a Massachusetts program that reimburses employers for training their current staff. The employer pays for approved training up front and the state pays part of it back. It is run by Commonwealth Corporation (CommCorp)."),
    ("Which employers can apply?",
     "Massachusetts businesses that contribute to the Workforce Training Fund can apply. Smaller employers get a higher reimbursement rate than larger ones. Check current eligibility with CommCorp before you plan."),
    ("What does Express cover?",
     "It reimburses the cost of eligible, instructor-led training. It is for live instruction — it does not cover things like equipment, travel, or wages during training. The exact list of eligible courses and costs is set by the program."),
    ("How much does it pay back?",
     "Reimbursement rates and per-person and per-company caps are set by the program and change over time. This page shows the current figures we have on file, but confirm them with CommCorp before you budget."),
    ("How do I apply?",
     "The employer applies directly with the state: you choose eligible training, submit an application/agreement to CommCorp, run the training, and then request reimbursement. You manage this yourself &mdash; a training provider does not apply on your behalf."),
    ("What is Career Skills Center's role?",
     "Career Skills Center provides training for employer teams. It does not apply for Express grants, handle the paperwork, or take payment for the grant process &mdash; the employer applies to the state directly. Career Skills Center is working toward becoming a listed Express provider."),
]

PAGES.append(dict(
    slug="express-program-explained.html", nav="express-program-explained.html",
    title="Express Program Explained: Massachusetts Workforce Training Fund | Career Skills Center",
    ogtitle="Express Program Explained: MA Workforce Training Fund",
    desc="A plain-language guide to the Massachusetts Workforce Training Fund Express Program: who can apply, what it covers, reimbursement rates and caps, how to apply, and the timeline.",
    extrahead=faq_ld(_EXPRESS_FAQ),
    main=hero("Funding Guides &middot; Express Program",
              "The Express Program, Explained",
              "The Workforce Training Fund Express Program helps Massachusetts employers pay for training their "
              "staff &mdash; the state reimburses part of the cost. Here&rsquo;s who can apply, what&rsquo;s "
              "covered, the rates and caps, and how to apply.",
              None, ("Staff Training Grants", "staff-training-grants.html")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The basics</p>
        <h2 class="section-title left">What the Workforce Training Fund is</h2>
        <p class="lede">The <strong>Workforce Training Fund</strong> is a Massachusetts program that helps
        employers pay to train the people they already employ. The <strong>Express Program</strong> is its
        simplest track: you pick eligible training, pay for it, and the state reimburses part of the cost. It is
        administered by <strong>Commonwealth Corporation (CommCorp)</strong>.</p>
        <p>It exists because trained workers are good for the whole state economy &mdash; so Massachusetts shares
        the cost of upskilling with employers who contribute to the fund.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Who &amp; what</p>
        <h2 class="section-title left">Who can apply, and what&rsquo;s covered</h2>
        <p><strong>Who can apply:</strong> Massachusetts businesses that contribute to the Workforce Training
        Fund. Smaller employers (up to <span data-cfg="EXPRESS_SMALL_EMPLOYER_MAX" data-cfg-format="number">[VERIFY]</span>
        employees) get the highest reimbursement rate; larger employers can also participate at a lower rate.</p>
        <p><strong>What&rsquo;s covered:</strong> the cost of eligible, <strong>instructor-led (live)
        training</strong>. It is not for equipment, travel, or paying wages during training. The specific
        eligible courses and costs are set by the program.</p>
        <p class="note"><strong>Please confirm the current figures.</strong> Reimbursement rates, caps and
        timelines change. The numbers below are what we have on file and are being verified with CommCorp
        &mdash; treat them as a guide, not a guarantee. [VERIFY]</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Rates &amp; caps</p>
        <h2 class="section-title left">What Express pays back</h2>
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr><th>What</th><th>Amount</th></tr>
            </thead>
            <tbody>
              <tr><th>Reimbursement rate &mdash; small employers</th><td>up to <span data-cfg="EXPRESS_RATE_SMALL" data-cfg-format="percent">[VERIFY]</span> of eligible cost</td></tr>
              <tr><th>Reimbursement rate &mdash; larger employers</th><td>up to <span data-cfg="EXPRESS_RATE_LARGE" data-cfg-format="percent">[VERIFY]</span> of eligible cost</td></tr>
              <tr><th>Cap per person, per course</th><td>up to <span data-cfg="EXPRESS_MAX_PER_PERSON_PER_COURSE" data-cfg-format="money">[VERIFY]</span></td></tr>
              <tr><th>Cap per instructional hour</th><td>up to <span data-cfg="EXPRESS_MAX_PER_INSTRUCTIONAL_HOUR" data-cfg-format="money">[VERIFY]</span></td></tr>
              <tr><th>Annual cap per company</th><td>up to <span data-cfg="EXPRESS_ANNUAL_CAP_PER_COMPANY" data-cfg-format="money">[VERIFY]</span></td></tr>
            </tbody>
          </table>
        </div>
        <p><a class="btn btn-yellow" href="staff-training-grants.html">Estimate your reimbursement</a></p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How &amp; when</p>
        <h2 class="section-title left">How to apply, and the timeline</h2>
        <ol class="check-list check-list--num">
          <li><strong>Choose eligible training</strong> for your staff.</li>
          <li><strong>Submit an application/agreement</strong> to CommCorp before training starts.</li>
          <li><strong>Run the training</strong> once your agreement is in place. Smaller requests can be approved
          quickly &mdash; some agreements start automatically after about
          <span data-cfg="EXPRESS_AGREEMENT_AUTOSTART_DAYS" data-cfg-format="number">[VERIFY]</span> days if not
          otherwise decided. [VERIFY]</li>
          <li><strong>Request reimbursement</strong> after the training is complete.</li>
        </ol>
        <p>The employer manages this application directly with the state. Career Skills Center&rsquo;s role is to
        provide the training. <a class="link-yellow" href="staff-training-grants.html">See the training we offer
        employers</a>.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="faq">
          <p class="faq-group-title">Express Program FAQ</p>
""" + "\n".join(f'''          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>''' for q, a in _EXPRESS_FAQ) + """
        </div>
      </div>
    </section>

    <section class="cta-band" aria-labelledby="ex-cta">
      <div class="container text-center">
        <h2 class="cta-title" id="ex-cta">Thinking about training your team?</h2>
        <a class="btn btn-yellow" href="staff-training-grants.html">See the training we offer employers</a>
      </div>
    </section>
"""))


# ---- employers.html (For Employers — overview) ----------------------------
PAGES.append(dict(
    slug="employers.html", nav="employers.html",
    title="For Employers: Staff Training Grants, Apprenticeships &amp; Corporate Training | Career Skills Center",
    ogtitle="For Employers: Training for Your Team",
    desc="Career Skills Center trains your team — and eligible Massachusetts employers can be reimbursed for the cost through the Express Program. Plus apprenticeships and custom corporate training.",
    main=hero("For Employers",
              "Training for Your Team",
              "Career Skills Center trains your team. Through the Massachusetts Express Program, eligible "
              "employers can be reimbursed for much of the cost &mdash; you apply to the state, we deliver the "
              "training. We also support apprenticeships and custom corporate training.",
              None, ("Do I Qualify?", "qualify.html")) + """

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How we help</p>
        <h2 class="section-title left">Three ways we support employers</h2>
        <div class="pcard-grid">
          <article class="pcard">
            <div class="pcard-body">
              <h3 class="pcard-title">Staff Training Grants</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>We provide the training. Through the Express Program, eligible employers can be reimbursed for
              much of the cost &mdash; you apply to the state directly.</p>
              <a class="btn btn-outline-navy" href="staff-training-grants.html">See staff training grants</a>
            </div>
          </article>
          <article class="pcard">
            <div class="pcard-body">
              <h3 class="pcard-title">Apprenticeships</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Build a trained, loyal pipeline with a Registered Apprenticeship &mdash; earn-while-you-learn
              roles supported by grants and tax credits.</p>
              <a class="btn btn-outline-navy" href="apprenticeships.html">Explore apprenticeships</a>
            </div>
          </article>
          <article class="pcard">
            <div class="pcard-body">
              <h3 class="pcard-title">Corporate Training</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Tell us what your team needs to learn. We&rsquo;re building training for employers, whether or
              not state funding is involved.</p>
              <a class="btn btn-outline-navy" href="corporate-training.html">See corporate training</a>
            </div>
          </article>
        </div>
      </div>
    </section>

""" + employer_form("employer",
                    heading="Tell us about your training needs",
                    intro="Tell us what you&rsquo;d like your team to learn &mdash; staff training, "
                          "apprenticeships or custom corporate training &mdash; and we&rsquo;ll follow up.",
                    show_team_size=True) + """
"""))


# ---- staff-training-grants.html (For Employers — service + calculator) -----
# Service page. CSC PROVIDES THE TRAINING only. It does NOT apply for grants,
# handle Express paperwork, or get paid to help employers apply — the employer
# applies to the state directly. Never "our course"; follow EXPRESS_PROVIDER_LISTED
# (false). Calculator logic lives in js/main.js (calcExpress); figures from config.
PAGES.append(dict(
    slug="staff-training-grants.html", nav="staff-training-grants.html",
    title="Staff Training Grants: Train Your Team, the State Can Reimburse You | Career Skills Center",
    ogtitle="Staff Training Grants for Massachusetts Employers",
    desc="Career Skills Center trains your team. Through the Massachusetts Workforce Training Fund Express Program, eligible employers can be reimbursed for much of the cost. Estimate the reimbursement.",
    main=hero('<span>For Massachusetts businesses &middot; <span data-cfg="EXPRESS_SMALL_EMPLOYER_MAX" data-cfg-format="number">100</span> or fewer W-2 employees</span>',
              "We Train Your Team. The State Can Reimburse the Cost",
              'Hands-on training that makes your people genuinely productive, taught by experts in each field. '
              'Massachusetts reimburses up to <span data-cfg="EXPRESS_RATE_SMALL" data-cfg-format="percent">100%</span> '
              'of the cost for eligible companies with <span data-cfg="EXPRESS_SMALL_EMPLOYER_MAX" data-cfg-format="number">100</span> '
              'or fewer employees, through the Workforce Training Fund Express Program.',
              None, ("How Express works", "express-program-explained.html")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>What we do</p>
        <h2 class="section-title left">We provide the training</h2>
        <p class="lede">Our role is simple: we train your team. We&rsquo;re building training for employers in
        healthcare, IT and the skilled trades. The Massachusetts Express Program can then reimburse eligible
        employers for a large share of what that training costs.</p>
        <p class="note"><strong>How the funding works &mdash; and our role in it:</strong> the Express Program is
        between you and the state. <strong>The employer applies for the grant directly</strong> and receives the
        reimbursement. Career Skills Center does <strong>not</strong> apply on your behalf, handle the paperwork,
        or take any payment for the grant process &mdash; we simply provide the training. Only the state approves
        reimbursement.</p>
        <p><a class="btn btn-yellow" href="express-program-explained.html">See how the Express Program works</a></p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How the reimbursement works</p>
        <h2 class="section-title left">Up to 100%, up to <span data-cfg="EXPRESS_ANNUAL_CAP_PER_COMPANY" data-cfg-format="money">$15,000</span> a year</h2>
        <p class="lede">For eligible Massachusetts companies with <span data-cfg="EXPRESS_SMALL_EMPLOYER_MAX" data-cfg-format="number">100</span> or fewer W-2 employees, the Express Program can cover the full cost of training your staff.</p>
        <ul class="check-list check-list--num">
          <li><strong>Up to <span data-cfg="EXPRESS_RATE_SMALL" data-cfg-format="percent">100%</span> reimbursed.</strong> Eligible small employers can get back up to the full cost of approved training.</li>
          <li><strong>Up to <span data-cfg="EXPRESS_ANNUAL_CAP_PER_COMPANY" data-cfg-format="money">$15,000</span> a year.</strong> Each company can be reimbursed up to this amount per year, and you can use it across different trainings.</li>
          <li><strong>About <span data-cfg="EXPRESS_APPLICATION_WEEKS" data-cfg-format="number">3</span> weeks.</strong> From application to acceptance typically takes about three weeks.</li>
          <li><strong>The state sends you a check.</strong> You pay for the training, then Massachusetts reimburses you directly.</li>
        </ul>
      </div>
    </section>

    <section class="section" id="calculator">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Estimate</p>
        <h2 class="section-title left">Estimate the reimbursement</h2>
        <div class="section-intro"><p>A rough estimate of what an eligible employer could be reimbursed, based on
        the current program figures. Final amounts are set by the state &mdash; treat this as a guide, not a
        guarantee. [VERIFY]</p></div>
        <div class="express-calc">
          <div class="calc-grid">
            <div class="calc-field">
              <label for="calc-emp">Employees to train</label>
              <input id="calc-emp" type="number" min="1" step="1" value="5" inputmode="numeric">
            </div>
            <div class="calc-field">
              <label for="calc-cost">Training cost per employee</label>
              <input id="calc-cost" type="number" min="0" step="50" value="2000" inputmode="numeric">
            </div>
          </div>
          <fieldset class="calc-size">
            <legend>Company size</legend>
            <label><input type="radio" name="calc_size" value="small" checked> Up to <span data-cfg="EXPRESS_SMALL_EMPLOYER_MAX" data-cfg-format="number">100</span> employees</label>
            <label><input type="radio" name="calc_size" value="large"> More than <span data-cfg="EXPRESS_SMALL_EMPLOYER_MAX" data-cfg-format="number">100</span> employees</label>
          </fieldset>
          <div class="calc-output" aria-live="polite">
            <p class="calc-result-line">Estimated reimbursement: <strong class="calc-total">&mdash;</strong></p>
            <p class="calc-detail"></p>
          </div>
          <p class="calc-note">Estimate uses the reimbursement rate for your company size, capped per person and
          per company. It doesn&rsquo;t apply the per-instructional-hour cap (that depends on course hours). All
          figures come from the program and are being verified. [VERIFY]</p>
        </div>
      </div>
    </section>

""" + employer_form("employer-express",
                    heading="Tell us about training your team",
                    intro="Tell us what you&rsquo;d like your team to learn and we&rsquo;ll follow up about the "
                          "training we can provide.",
                    show_team_size=True) + """

    <section class="section">
      <div class="container">
        <h2 class="related-title">Related</h2>
        <div class="post-grid post-grid--related">
          <a class="post-card" href="express-program-explained.html"><h3>Express Program Explained</h3><span class="read-link">Read the guide</span></a>
          <a class="post-card" href="apprenticeships.html"><h3>Apprenticeship Programs</h3><span class="read-link">Read more</span></a>
          <a class="post-card" href="corporate-training.html"><h3>Corporate Training</h3><span class="read-link">Read more</span></a>
        </div>
      </div>
    </section>
"""))


# ---- apprenticeships.html (For Employers) ---------------------------------
_APPR_FAQ = [
    ("What is a Registered Apprenticeship?",
     "It&rsquo;s an &ldquo;earn while you learn&rdquo; job. The apprentice is your employee from day one and is trained on the job by a mentor, plus related classroom instruction, over a program that ends in a nationally recognized credential. Programs are registered with the state (Division of Apprentice Standards) or the federal apprenticeship agency."),
    ("Do I train the person first and then they become an apprentice?",
     "No &mdash; that&rsquo;s a common mix-up. An apprenticeship flips the usual order: you hire the person first and they learn on the job while they work. It&rsquo;s not a subsidy for hiring someone who is already fully trained. (Separately, a pre-apprenticeship can prepare someone to enter an apprenticeship.)"),
    ("How is this different from an ITA / WIOA training voucher?",
     "They&rsquo;re two different paths. An ITA voucher pays for classroom training before a job, at a state-approved school. An apprenticeship is a paid job where training happens during employment. The apprentice tax credit only applies to registered apprentices &mdash; not to someone you hire after they finish ITA-funded training."),
    ("How much can an employer get back?",
     "Massachusetts offers a Registered Apprentice Tax Credit worth 50% of an apprentice&rsquo;s wages, up to $4,800 per apprentice per year and up to $100,000 per employer per year, for up to two consecutive tax years. GROW grants can also help fund the classroom (related instruction) side. Amounts and rules are set by the state."),
    ("Which apprentices qualify for the tax credit?",
     "Per the state: you must be registered with the Division of Apprentice Standards as a sponsor with an approved apprenticeship agreement, the apprentice must work at least 180 days in the tax year with their main workplace in Massachusetts, and the occupation must be on the state&rsquo;s eligible list (technology, healthcare, advanced manufacturing, life sciences, clean energy and other in-demand fields)."),
    ("What is Career Skills Center's role in apprenticeships?",
     "Career Skills Center provides training. We can deliver the related classroom instruction a Registered Apprenticeship requires. We don't register or administer your apprenticeship program or claim the tax credit &mdash; you do that with the state as the sponsor. Career Skills Center plans to offer training in healthcare, IT and the skilled trades; as our programs launch, our graduates will become a hiring pipeline for partner employers."),
]

PAGES.append(dict(
    slug="apprenticeships.html", nav="apprenticeships.html",
    title="Apprenticeship Programs for Employers: Tax Credit &amp; Grants | Career Skills Center",
    ogtitle="Apprenticeship Programs for Employers",
    desc="How Registered Apprenticeships work in Massachusetts: earn-while-you-learn hiring, the Registered Apprentice Tax Credit (up to $4,800/apprentice), GROW grants for the classroom side, and who qualifies.",
    extrahead=faq_ld(_APPR_FAQ),
    main=hero("For Employers &middot; Apprenticeships",
              "Build a Trained Pipeline with Apprenticeships",
              "A Registered Apprenticeship lets you hire and train workers to your standards while they earn "
              "&mdash; with a state tax credit on their wages and grants that can fund the classroom side. "
              "Career Skills Center provides that classroom training.",
              None, ("Talk to us", "#employer-inquiry")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The basics</p>
        <h2 class="section-title left">What a Registered Apprenticeship is</h2>
        <p class="lede">A Registered Apprenticeship is an <strong>&ldquo;earn while you learn&rdquo;</strong> job.
        The apprentice is your <strong>employee from day one</strong>, learns on the job from a mentor, takes
        <strong>related classroom instruction</strong> alongside the work, and moves up a defined
        <strong>wage-progression</strong> schedule to a nationally recognized credential.</p>
        <p class="note"><strong>It flips the usual order.</strong> Instead of &ldquo;train first, then get
        hired,&rdquo; the apprentice is hired first and trained during the job. So an apprenticeship isn&rsquo;t a
        way to get a credit for hiring someone who&rsquo;s already fully trained &mdash; the training <em>is</em>
        the job. (A separate ITA/WIOA voucher is the classroom-first path; see
        <a class="link-yellow" href="wioa-explained.html">WIOA explained</a>.)</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How it works</p>
        <h2 class="section-title left">The four building blocks</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">A sponsor</h3>
            <p>You (or an intermediary) register the program with the state and define the skills the apprentice will master.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">On-the-job learning</h3>
            <p>Apprentices work and learn under experienced staff, building real skills from day one.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Related instruction</h3>
            <p>Classroom or online coursework runs alongside the job &mdash; the part Career Skills Center can provide.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Wage progression</h3>
            <p>Pay rises on a set schedule as the apprentice hits skill milestones &mdash; earn while you learn.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Funding</p>
        <h2 class="section-title left">How much it costs an employer &mdash; and what you get back</h2>
        <p class="lede">Because the apprentice is your employee, you pay their wages. Two things bring the real
        cost down: a state tax credit on those wages, and grants that can fund the classroom instruction.</p>

        <h3>Registered Apprentice Tax Credit</h3>
        <p>If you register as a program sponsor, Massachusetts offers a tax credit worth
        <strong><span data-cfg="APPRENTICE_TAX_CREDIT_WAGE_SHARE" data-cfg-format="percent">50%</span> of an
        apprentice&rsquo;s wages</strong>, up to
        <strong><span data-cfg="APPRENTICE_TAX_CREDIT_MAX_PER_APPRENTICE" data-cfg-format="money">$4,800</span>
        per apprentice</strong> per year, and up to
        <strong><span data-cfg="APPRENTICE_TAX_CREDIT_MAX_PER_EMPLOYER" data-cfg-format="money">$100,000</span>
        per employer</strong> per year &mdash; for up to
        <strong><span data-cfg="APPRENTICE_TAX_CREDIT_YEARS" data-cfg-format="number">2</span> consecutive tax
        years</strong> per apprentice.</p>
        <p><strong>To qualify</strong> (per the state): you must be registered with the Division of Apprentice
        Standards (DAS) as a sponsor with an approved apprenticeship agreement; the apprentice must work at least
        <span data-cfg="APPRENTICE_MIN_DAYS" data-cfg-format="number">180</span> days in the tax year with their
        main workplace in Massachusetts; and the occupation must be on the state&rsquo;s eligible list
        (technology, healthcare, advanced manufacturing, life sciences, clean energy and other in-demand fields).</p>

        <h3>Grants for the classroom side</h3>
        <p>Massachusetts <strong>GROW</strong> grants (and related technical instruction grants) can help fund the
        classroom portion of an apprenticeship. Award amounts are set per grant round, and the rules require that
        the cost of related instruction <strong>not</strong> be passed on to the apprentice. This classroom piece
        is exactly what Career Skills Center can provide.</p>
        <p class="role-src">Sources: mass.gov &mdash; Apply for a Registered Apprentice Tax Credit (DAS Issuance
        TY2026); Registered Apprenticeship funding opportunities / GROW grants; apprenticeship.gov (earn-while-you-learn model). Checked 2026-09-28.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Why it pays off</p>
        <h2 class="section-title left">Benefits for employers</h2>
        <ul class="check-list">
          <li><strong>Better retention.</strong> Workers you train and invest in tend to stay longer.</li>
          <li><strong>A trained pipeline.</strong> You grow the exact skills your business needs, to your standards.</li>
          <li><strong>Real cost offsets.</strong> The state tax credit on wages plus grants for the classroom side lower what the apprenticeship costs you.</li>
        </ul>
        <!-- COURSE-DEPENDENT: R-APPR — future graduate-pipeline line; present tense only in course mode. -->
        <p>As our programs launch, our graduates will become a hiring pipeline for partner employers.</p>
      </div>
    </section>

""" + employer_form("employer-apprenticeship",
                    heading="Interested in apprenticeships?",
                    intro="Tell us about your team and the classroom training you need for an apprenticeship, "
                          "and we&rsquo;ll follow up.",
                    show_team_size=True) + """

    <section class="section section--tight">
      <div class="container">
        <div class="faq">
          <p class="faq-group-title">Apprenticeship FAQ</p>
""" + "\n".join(f'''          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>''' for q, a in _APPR_FAQ) + """
        </div>
      </div>
    </section>
"""))


# ---- corporate-training.html (For Employers) ------------------------------
# COURSE-DEPENDENT: R-CORP. No location wording, no prices/formats/course names.
PAGES.append(dict(
    slug="corporate-training.html", nav="corporate-training.html",
    title="Corporate Training: Custom Training for Your Team | Career Skills Center",
    ogtitle="Corporate Training for Your Team",
    desc="Career Skills Center is building custom training for employers. Tell us what your team needs to learn and we'll follow up.",
    main=hero("For Employers &middot; Corporate Training",
              "Custom Training for Your Team",
              "Every team has skills it needs to build. We&rsquo;re building training that employers can bring "
              "to their people &mdash; with or without state funding.",
              None, ("Tell us your needs", "#employer-inquiry")) + """

    <!-- COURSE-DEPENDENT: R-CORP — corporate-training copy is future tense in guide
         mode. In course mode, describe live offerings, formats and enrollment. -->
    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>What we&rsquo;re building</p>
        <h2 class="section-title left">Training built around your team</h2>
        <p class="lede">We&rsquo;re building training for employers. Tell us what your team needs, and
        we&rsquo;ll work with you to shape it. Eligible employers may be able to offset the cost through the
        state Express Program, which the employer applies for directly.</p>
        <ul class="check-list">
          <li>Skills your team needs, not off-the-shelf filler</li>
          <li>Options whether or not you use state funding</li>
          <li>Training built to be eligible for reimbursement where it applies</li>
        </ul>
        <p>Career Skills Center plans to offer training in healthcare, IT and the skilled trades. Corporate
        training details will follow as our programs launch.</p>
      </div>
    </section>

""" + employer_form("corporate",
                    heading="Tell us what your team needs",
                    intro="Share a few details and we&rsquo;ll be in touch to talk it through.",
                    topic_options=[("healthcare", "Healthcare skills"),
                                   ("it", "IT / technology skills"),
                                   ("trades", "Skilled trades"),
                                   ("safety-compliance", "Safety / compliance"),
                                   ("other", "Something else")],
                    show_team_size=True, show_timeline=True,
                    submit_label="Send request") + """
"""))


# ---- admissions.html ------------------------------------------------------
PAGES.append(dict(
    slug="admissions.html", nav="admissions.html",
    title="Admissions | Career Skills Center — Massachusetts",
    ogtitle="Admissions",
    desc="Enrollment isn't open yet at Career Skills Center. Here's how admissions will work and how to join the interest list to hear first.",
    main=hero("Admissions", "Admissions",
              "Enrollment isn&rsquo;t open yet. Here&rsquo;s how it will work &mdash; and how to get on the "
              "list so you&rsquo;re first to know.",
              None) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How it will work</p>
        <h2 class="section-title left">Three simple steps</h2>
        <ul class="check-list">
          <li><strong>Join the interest list</strong>Tell us the program you want, and we&rsquo;ll email you the moment enrollment opens.</li>
          <li><strong>Talk with us</strong>A short conversation about your goals, schedule and how you&rsquo;ll pay &mdash; no pressure.</li>
          <li><strong>Enroll</strong>Once programs launch, we&rsquo;ll walk you through signing up and getting started.</li>
        </ul>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Requirements</p>
        <h2 class="section-title left">Who will be able to enroll</h2>
        <p>We&rsquo;re keeping requirements straightforward. When enrollment opens, we expect you&rsquo;ll need:</p>
        <ul class="check-list">
          <li><strong>To be 18 or older</strong>(17 with a parent or guardian signature).</li>
          <li><strong>A high school diploma or GED</strong>for most programs &mdash; ask us about options if you don&rsquo;t have one yet.</li>
          <li><strong>A valid photo ID</strong>(driver&rsquo;s license, state ID or passport).</li>
          <li><strong>A short enrollment conversation</strong>about your goals, schedule and funding.</li>
        </ul>
        <p>Final requirements will be confirmed before enrollment opens.</p>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Paying for it</p>
        <h2 class="section-title left">How you might pay</h2>
        <p>Most people combine sources. We plan to offer payment plans, and you may qualify for state or
        employer funding. Start with our
        <a class="link-yellow" href="blog/free-job-training-massachusetts.html">guide to free job training in
        Massachusetts</a>, and see <a class="link-yellow" href="student-financing.html">Ways to Pay</a>.</p>
      </div>
    </section>

""" + interest_form("unsure", "program")))


# ---- tuition.html ---------------------------------------------------------
PAGES.append(dict(
    slug="tuition.html", nav="tuition.html",
    title="Tuition | Career Skills Center — Massachusetts",
    ogtitle="Tuition",
    desc="Pricing for Career Skills Center programs will be published before enrollment opens, including books and exam fees, with no hidden fees. Join the interest list.",
    main=hero("Tuition", "Tuition",
              "Clear, upfront pricing is coming. We&rsquo;ll publish full costs before enrollment opens, and "
              "help you find every funding source you may qualify for.",
              "images/tuition-hero.webp") + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Pricing</p>
        <h2 class="section-title left">Pricing coming soon</h2>
        <p class="lede">Career Skills Center&rsquo;s programs are in development, so we haven&rsquo;t set final
        tuition yet. When we do, we&rsquo;ll publish the full cost of each program &mdash; including books and
        exam fees &mdash; right here, with no hidden fees.</p>
        <p>Affordability is a core goal: short, focused programs mean you stop paying sooner and start earning
        sooner. Join the interest list and we&rsquo;ll send pricing the moment it&rsquo;s ready.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Find your fit</p>
        <h2 class="section-title left">Ways we plan to help you pay</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Payment plans</h3>
            <p>We plan to offer a monthly payment option so you can spread the cost out. Terms will be published with pricing.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Employer-paid</h3>
            <p>Massachusetts employers may be reimbursed for training their staff through the state Workforce Training Fund.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">State &amp; grant funding</h3>
            <p>You may qualify for funded training. See our <a class="link-yellow" href="blog/free-job-training-massachusetts.html">guide to free job training in Massachusetts</a>.</p>
          </article>
        </div>
        <p class="note">Career Skills Center is working toward approval to accept state training funds. We&rsquo;ll help you check what you may qualify for &mdash; but only your MassHire career center can approve funding.</p>
      </div>
    </section>

""" + interest_form("unsure", "pricing and program")))


# ---- qualify.html ---------------------------------------------------------
# Lead-magnet #1 (brief §3.2). A 6-step, one-question-per-screen wizard with a
# progress bar. It CAPTURES A LEAD and shows a soft-routing message — it never
# renders a yes/no eligibility verdict (only a MassHire career center decides).
# The wizard behaviour lives in js/main.js (feature-detected by .qualify-form);
# it posts to the live submit.php mailer with a hidden source=qualify.
#
# FUNDING_ETPL_APPROVED is false (js/site-config.js doesn't exist yet), so the
# result copy uses the not-yet-approved wording ("...options to start now").
# When the config lands, the result strings in main.js can be flag-driven.


def _q_opts(name, opts, autoadvance=True):
    """Radio-button option cards for one wizard question.
    `opts` is a list of (value, label). First step gets no pre-selection."""
    rows = "\n".join(
        f'''          <div class="qualify-option">
            <input type="radio" id="{name}-{v}" name="{name}" value="{v}">
            <label for="{name}-{v}">{lbl}</label>
          </div>'''
        for v, lbl in opts)
    return rows


PAGES.append(dict(
    slug="qualify.html", nav="",
    title="Do I Qualify for WIOA Training? Free Eligibility Check | Career Skills Center",
    ogtitle="Do I Qualify for WIOA Training? Free Eligibility Check",
    desc="Answer a few quick questions to see which WIOA group you may fit and your next steps for publicly funded training. Free, about 60 seconds, and never a yes/no verdict.",
    main="""    <section class="page-hero">
      <div class="container">
        <p class="eyebrow eyebrow--light"><span class="eyebrow-line" aria-hidden="true"></span>Do I Qualify?</p>
        <h1>See what training help you may qualify for<span class="dot">.</span></h1>
        <p class="page-hero-lede">Answer a few quick questions and we&rsquo;ll show which WIOA group you may fit
        and what to do next. This isn&rsquo;t an application, it&rsquo;s free, and it never gives a yes/no verdict
        &mdash; only a MassHire career center can approve funding.</p>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <div class="qualify-wrap">
          <form class="qualify-form" action="submit.php" method="post" novalidate>
            <input type="hidden" name="source" value="qualify">
            <input type="text" class="hp-field" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">

            <div class="qualify-progress" aria-hidden="true">
              <div class="qualify-progress-track"><div class="qualify-progress-fill"></div></div>
              <p class="qualify-progress-label">Step 1 of 8</p>
            </div>

            <button type="button" class="qualify-back" hidden>&larr; Back</button>

            <fieldset class="qualify-step" data-autoadvance="1">
              <legend>Do you live in Massachusetts?</legend>
              <p class="qualify-help">This check covers Massachusetts. WIOA exists in every state, though.</p>
              <div class="qualify-options">
""" + _q_opts("live_ma", [("yes", "Yes"), ("no", "No")]) + """
              </div>
            </fieldset>

            <fieldset class="qualify-step" data-autoadvance="1">
              <legend>How old are you?</legend>
              <p class="qualify-help">WIOA has a separate track for young people.</p>
              <div class="qualify-options">
""" + _q_opts("age", [
        ("under18", "Under 18"),
        ("18-24", "18 to 24"),
        ("25plus", "25 or older")]) + """
              </div>
            </fieldset>

            <fieldset class="qualify-step" data-autoadvance="1">
              <legend>What&rsquo;s your current work situation?</legend>
              <p class="qualify-help">Pick the closest one.</p>
              <div class="qualify-options">
""" + _q_opts("situation", [
        ("unemployed", "Unemployed"),
        ("laid-off", "Laid off, or I got a layoff notice"),
        ("on-ui", "Collecting unemployment benefits"),
        ("part-low", "Working part-time or low wage"),
        ("full-time", "Employed full-time"),
        ("self-closed", "Self-employed and my business closed")]) + """
              </div>
            </fieldset>

            <fieldset class="qualify-step" data-autoadvance="1">
              <legend>Does your household receive public assistance?</legend>
              <p class="qualify-help">For example SNAP, TAFDC, SSI or similar. This can move you up the priority list.</p>
              <div class="qualify-options">
""" + _q_opts("assistance", [
        ("yes", "Yes"),
        ("no", "No"),
        ("prefer-not", "Prefer not to say")]) + """
              </div>
            </fieldset>

            <fieldset class="qualify-step" data-autoadvance="1">
              <legend>Is your household income low?</legend>
              <p class="qualify-help">&ldquo;Low income&rdquo; depends on household size. As a rough example, one
              Massachusetts career center in <span data-cfg="INCOME_EXAMPLE_YEAR" data-cfg-format="raw">[VERIFY]</span>
              used thresholds from about <span data-cfg="INCOME_EXAMPLE_MIN" data-cfg-format="money">[VERIFY]</span>
              for one person up to <span data-cfg="INCOME_EXAMPLE_MAX" data-cfg-format="money">[VERIFY]</span>+ for
              larger families &mdash; but this varies by center and year, so it&rsquo;s only a guide.</p>
              <div class="qualify-options">
""" + _q_opts("income_low", [
        ("yes", "Yes, or close to it"),
        ("no", "No"),
        ("unsure", "Not sure")]) + """
              </div>
            </fieldset>

            <fieldset class="qualify-step" data-autoadvance="1">
              <legend>Are you a veteran or the spouse of a veteran?</legend>
              <p class="qualify-help">Veterans and eligible spouses get priority in these programs.</p>
              <div class="qualify-options">
""" + _q_opts("veteran", [("yes", "Yes"), ("no", "No")]) + """
              </div>
            </fieldset>

            <fieldset class="qualify-step" data-autoadvance="1">
              <legend>Are you legally allowed to work in the US?</legend>
              <p class="qualify-help">Work authorization is generally required for WIOA-funded training.</p>
              <div class="qualify-options">
""" + _q_opts("work_auth", [("yes", "Yes"), ("no", "No"), ("unsure", "Not sure")]) + """
              </div>
            </fieldset>

            <fieldset class="qualify-step" data-autoadvance="1">
              <legend>Which field interests you?</legend>
              <p class="qualify-help">You can change your mind later.</p>
              <div class="qualify-options">
""" + _q_opts("field", [
        ("healthcare", "Healthcare"),
        ("it", "Information Technology"),
        ("trades", "Skilled Trades"),
        ("unsure", "Not sure")]) + """
              </div>
            </fieldset>

            <!-- Result screen = which WIOA group you MAY fit + priority flags + outward
                 next steps. NEVER a yes/no verdict. js/main.js fills it (see classifyQualify).
                 COURSE-DEPENDENT: R-QUALIFY — in course mode the result also routes inward
                 (matching CSC course + funding help), pre-written behind SITE_MODE. -->
            <div class="qualify-result" role="status" aria-live="polite">
              <svg class="result-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
              <h2 class="result-head">Here&rsquo;s what your answers suggest.</h2>
              <p class="result-body"></p>

              <div class="result-groups" hidden>
                <h3 class="result-subhead">You may fit:</h3>
                <ul class="result-group-list check-list"></ul>
              </div>

              <div class="result-priority" hidden>
                <h3 class="result-subhead">Things that may move you up the priority list:</h3>
                <ul class="result-priority-list check-list"></ul>
              </div>

              <div class="result-steps-wrap" hidden>
                <h3 class="result-subhead">Your next steps:</h3>
                <ol class="result-steps check-list check-list--num"></ol>
              </div>

              <p class="result-selective note" hidden>Note: men born on or after January 1, 1960 must be
              registered with Selective Service to receive WIOA funds. [VERIFY]</p>

              <p class="result-workauth note" hidden>Work authorization is generally required for WIOA-funded
              training. A MassHire career center can explain your options.</p>

              <p class="result-notma note" hidden>WIOA exists in every state, but this check covers Massachusetts.
              Find your local American Job Center at <a class="link-yellow" href="https://www.careeronestop.org/LocalHelp/AmericanJobCenters/find-american-job-centers.aspx" target="_blank" rel="noopener">CareerOneStop</a>. [VERIFY]</p>

              <p class="result-employer" hidden>Already working? Your employer may be able to get training costs
              reimbursed through the state. <a class="link-yellow" href="staff-training-grants.html">See staff
              training grants</a>.</p>

              <p class="result-readmore">Read more: <a class="link-yellow" href="wioa-explained.html">WIOA explained</a> &middot; <a class="link-yellow" href="blog/free-job-training-massachusetts.html">Free job training in Massachusetts</a> &middot; <a class="link-yellow" href="blog/masshire-training-voucher.html">How to get a MassHire voucher (ITA)</a>.</p>

              <div class="result-actions">
                <a class="btn btn-navy result-guide" href="career-paths.html">Explore your field</a>
                <a class="btn btn-outline-navy" href="wioa-explained.html">How WIOA works</a>
              </div>

              <!-- COURSE-DEPENDENT: R-QUALIFY — guide mode: interest-list line.
                   Course mode: replace with the matching CSC course + enroll CTA. -->
              <p class="result-field-note"></p>

              <p class="qualify-disclaimer">This tool doesn&rsquo;t decide your funding. Only a MassHire career
              center can approve state training funds. We&rsquo;ll help you understand what you may qualify for.</p>

              <!-- Optional: email these steps. Not required to see results. -->
              <div class="qualify-email">
                <h3 class="result-subhead">Want these steps emailed to you?</h3>
                <p class="qualify-help">Optional. Leave your details and we&rsquo;ll send a copy and keep you
                posted. No spam, no pressure.</p>
                <div class="qualify-fields">
                  <label class="sr-only" for="q-name">First name</label>
                  <input id="q-name" name="name" type="text" placeholder="First name" autocomplete="given-name">
                  <label class="sr-only" for="q-email">Email address</label>
                  <input id="q-email" name="email" type="email" placeholder="Email address" autocomplete="email">
                  <label class="sr-only" for="q-phone">Mobile phone (optional)</label>
                  <input id="q-phone" name="phone" type="tel" placeholder="Mobile phone (optional)" autocomplete="tel">
                  <label class="sr-only" for="q-language">Preferred language</label>
                  <select id="q-language" name="language">
                    <option value="" selected disabled>Preferred language</option>
                    <option value="English">English</option>
                    <option value="Espa&ntilde;ol">Espa&ntilde;ol</option>
                    <option value="Portugu&ecirc;s">Portugu&ecirc;s</option>
                  </select>
                  <label class="consent-row"><input type="checkbox" name="consent" value="yes"> Send me updates from
                  Career Skills Center (email/SMS). Message and data rates may apply.</label>
                </div>
                <div class="qualify-nav">
                  <button class="btn btn-yellow" type="submit">Email me these steps</button>
                </div>
                <p class="form-status" role="status" aria-live="polite"></p>
              </div>
            </div>
          </form>
        </div>
      </div>
    </section>"""))


# ---- wioa.html ------------------------------------------------------------
# Section order and layout follow the reference site's WIOA page; the copy is
# written for Career Skills Center and Massachusetts (MassHire, not Texas).
# Images are intentionally left as empty placeholders for now.
PAGES.append(dict(
    slug="wioa.html", nav="wioa.html",
    title="WIOA Program | Career Skills Center — Massachusetts",
    ogtitle="WIOA Program: Free Career Training",
    desc="A Workforce Innovation and Opportunity Act grant may cover the full cost of trade, IT or medical training at Career Skills Center in Massachusetts.",
    main=hero("WIOA Program", "Free Career Training",
              "A Workforce Innovation and Opportunity Act grant can cover the cost of short-term training "
              "that leads to a recognized certification in the skilled trades, information technology or "
              "the medical field. Read on to see whether you qualify.",
              "images/wioa-hero.webp") + """

    <section class="section">
      <div class="container">
        <div class="split-grid reverse">
          <div class="split-media">
            <!-- PLACEHOLDER: image to be added later (NTI shows a student at a computer here) -->
            <div class="img-placeholder">Image placeholder</div>
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>WIOA Program Grants</p>
            <h2 class="section-title left">Career Training at No Cost to You</h2>
            <p>The Workforce Innovation and Opportunity Act was created by the U.S. Department of Labor
            together with the Department of Education to lower the barriers that keep people out of good
            careers. It is built for adults entering the workforce for the first time and for those returning
            to it, and it pays for the skills and credentials that lead to in-demand jobs rather than
            short-term work.</p>
            <p>In Massachusetts the money is administered locally. MassHire career centers take applications,
            decide who qualifies, and set how much each approved applicant receives. The school does not make
            that determination, but we help you prepare for it and we know what the career centers ask for.</p>
            <p class="note"><strong>Before publishing:</strong> confirm that Career Skills Center is listed
            as an Eligible Training Provider on the Massachusetts ETPL. Advertising WIOA-funded training,
            including the phrase “free career training,” requires that approval in writing first.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split-grid">
          <div class="split-media">
            <!-- PLACEHOLDER: image to be added later -->
            <div class="img-placeholder">Image placeholder</div>
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>WIOA Funding</p>
            <h2 class="section-title left">The Basics</h2>
            <div class="faq">
              <details class="faq-item">
                <summary>Who funds the WIOA grant?</summary>
                <div class="faq-body"><p>The U.S. Department of Labor, in partnership with the Department of
                Education. Money flows to the states and is distributed through local career centers, which
                in Massachusetts are the MassHire centers.</p></div>
              </details>
              <details class="faq-item">
                <summary>How do I find out if I am eligible?</summary>
                <div class="faq-body"><p>Eligibility is decided by your local career center rather than by
                the school. Begin an intake with MassHire, or call us at
                <a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a> and we will point you to
                the right office and tell you what to bring.</p></div>
              </details>
              <details class="faq-item">
                <summary>How much is available per person?</summary>
                <div class="faq-body"><p>It varies. Award amounts depend on where you live, how much funding
                your career center has been allocated, the program you choose, and your own circumstances.</p></div>
              </details>
              <details class="faq-item">
                <summary>How long before I can begin training?</summary>
                <div class="faq-body"><p>Once you are found eligible and your paperwork, assessments and
                evaluations are complete, we work to place you in the next available cohort.</p></div>
              </details>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="split-grid reverse">
          <div class="split-media">
            <!-- PLACEHOLDER: image to be added later -->
            <div class="img-placeholder">Image placeholder</div>
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Career Skills Center WIOA Programs</p>
            <h2 class="section-title left">Get Started on Your Journey</h2>
            <p>Our certificate programs are built around entry-level roles in fields that are still growing:
            the skilled trades, information technology and allied health. Each one is short, hands-on, and
            ends in a credential an employer recognizes.</p>
            <p>For students whose training is covered by a workforce grant, that credential comes without
            out-of-pocket tuition. You finish with the certification, the practice hours and the job search
            support, and without the debt.</p>
            <p><a class="btn btn-navy" href="our-programs.html">Explore Programs</a></p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split-grid split-grid--top">
          <div class="split-media">
            <!-- PLACEHOLDER: image to be added later (NTI shows a portrait photo here) -->
            <div class="img-placeholder">Image placeholder</div>
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>WIOA Eligibility</p>
            <h2 class="section-title left">You May Be Eligible If…</h2>
            <p>Career centers weigh several factors, and meeting one of the conditions below is often enough
            to start a conversation. You do not need to meet all of them.</p>
            <ul class="check-list">
              <li><strong>You are 18 or older</strong>Applicants who are 17 may still have options; ask us.</li>
              <li><strong>You are authorized to work in the United States</strong>Documentation is verified by the career center during intake.</li>
              <li><strong>You have a high school diploma or a GED</strong>Required for most approved programs.</li>
              <li><strong>You are eligible for government benefits</strong>Receiving assistance often supports a funding determination.</li>
              <li><strong>You are a dislocated worker</strong>Plant or facility closures, layoffs, and homemakers who have lost the income they depended on.</li>
              <li><strong>You have been terminated or laid off</strong>Including anyone who has received notice and is eligible for, or has exhausted, unemployment compensation, or who works at a facility scheduled to close within 180 days.</li>
              <li><strong>You are self-employed but not working</strong>Including people whose work has stopped because of economic conditions or a natural disaster.</li>
            </ul>
            <p class="note">Final eligibility is always determined by your MassHire career center, not by the
            school. Nothing on this page is a guarantee of funding.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="split-grid">
          <div class="split-media">
            <!-- PLACEHOLDER: image to be added later -->
            <div class="img-placeholder">Image placeholder</div>
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Find Your Fit</p>
            <h2 class="section-title left">Talk With an Enrollment Advisor</h2>
            <p>When you are choosing a school, fit matters as much as the subject. You need the right
            program, funding you actually qualify for, and enough support to finish what you start.</p>
            <p>Our advisors know how the funding process works and what the career centers ask for, and our
            schedules are built around people who are working or raising a family while they train. Call
            <a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a> to talk it through. There is no
            cost and no obligation.</p>
            <p><button class="btn btn-navy js-open-contact" type="button">Talk to an Advisor</button></p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>WIOA Approved Programs</p>
        <h2 class="section-title left">Career Opportunities for a Better Future</h2>
        <div class="section-intro">
          <p><strong>More than career training. Training for a better future.</strong></p>
          <p>The point of a workforce grant is to break a cycle, not to fill a seat. That is why the industry
          you pick matters as much as the funding. Fields with steady demand and room to advance give you
          somewhere to go after the first job, instead of leaving you looking again in a year.</p>
          <p>Certificates fit that well. Most take months rather than years, and they stack: each credential
          you earn builds on the last, so you can keep moving up without starting over.</p>
        </div>

        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Skilled Trades</h3>
            <p>Electrical, HVAC/R, plumbing, welding and construction roles that contractors across the South
            Shore are hiring for now.</p>
            <a class="read-more" href="skilled-trades.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
          <article class="feature">
            <h3 class="feature-title">Information Technology</h3>
            <p>Help desk, networking, security and cloud roles where employers hire on certification rather
            than a four-year degree.</p>
            <a class="read-more" href="it-support-specialist.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
          <article class="feature">
            <h3 class="feature-title">Medical</h3>
            <p>Clinical and administrative support roles across one of the largest healthcare employment
            markets in the country.</p>
            <a class="read-more" href="our-programs.html#medical"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container narrow text-center">
        <h2 class="section-title">Approved to Accept WIOA Funding</h2>
        <p class="lede">To accept workforce funding, a school has to be listed as an Eligible Training
        Provider with the state. <span class="tbd">Our current listing status is TBD.</span> Our advisors can
        tell you exactly where that stands and what it means for your start date, so you are never guessing
        about whether your training will be covered.</p>
        <p class="note">Replace the status sentence above with the school’s actual ETPL listing once it is
        granted, worded the way the state words it.</p>
      </div>
    </section>

""" + cta("Ready to find out if you qualify?", "Talk to an Advisor")))


# ---- financial-aid.html ---------------------------------------------------
PAGES.append(dict(
    slug="financial-aid.html", nav="financial-aid.html",
    title="Financial Aid &amp; WIOA Grants | Career Skills Center — Massachusetts",
    ogtitle="Financial Aid",
    desc="Workforce grants, veterans benefits and other funding that may cover your training at Career Skills Center in Massachusetts.",
    main=hero("Financial Aid", "Financial Aid",
              "You may qualify for funding that covers some or all of your training. Find out in a single "
              "phone call.",
              "images/Todaybanner.webp") + f"""

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Workforce Grants</p>
        <h2 class="section-title left">Career Training at Little or No Cost</h2>
        <div class="section-intro">
          <p>The Workforce Innovation and Opportunity Act, known as WIOA, was created by the Department of
          Labor and the Department of Education to remove barriers for people who have trouble finding
          quality work. It helps those entering or re-entering the workforce get the skills and credentials
          needed for in-demand jobs that turn into long-term careers.</p>
          <p>In Massachusetts, WIOA funds are distributed through MassHire career centers. The MassHire
          South Shore Career Center serves Quincy and the surrounding towns. Eligibility, award amounts and
          approved program lists are set by the career center, not by the school.</p>
        </div>

        <p class="note"><strong>Before publishing:</strong> confirm whether Career Skills Center is an
        approved Eligible Training Provider on the Massachusetts ETPL. Do not advertise WIOA funding for our
        programs until that approval is in writing.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split-grid">
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Eligibility</p>
            <h2 class="section-title left">You May Qualify If…</h2>
            <ul class="check-list">
              <li><strong>You are 18 or older</strong>Some programs accept 17-year-olds with guardian consent.</li>
              <li><strong>You are authorized to work in the United States</strong>Documentation is verified by the career center.</li>
              <li><strong>You have a high school diploma or GED</strong>Required for most approved programs.</li>
              <li><strong>You are unemployed or underemployed</strong>Including anyone not earning a self-sufficient wage.</li>
              <li><strong>You are a dislocated worker</strong>Plant or facility closures, layoffs, or homemakers who have lost a primary income.</li>
              <li><strong>You were terminated or laid off</strong>Or received notice, and are eligible for or have exhausted unemployment compensation.</li>
            </ul>
          </div>
          <div class="split-media">
            <img src="images/hero3.webp" alt="Adult learners in a Career Skills Center classroom" loading="lazy" decoding="async">
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>The Basics</p>
        <h2 class="section-title left">Common Questions</h2>
        <div class="faq">
          <details class="faq-item">
            <summary>Who funds the grant?</summary>
            <div class="faq-body"><p>The U.S. Department of Labor, in partnership with the Department of
            Education. Funds are administered locally through MassHire career centers.</p></div>
          </details>
          <details class="faq-item">
            <summary>How do I find out if I am eligible?</summary>
            <div class="faq-body"><p>Eligibility is determined by your local career center, not by the
            school. Contact the MassHire South Shore Career Center, or call us at
            <a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a> and we will point you to the
            right intake process.</p></div>
          </details>
          <details class="faq-item">
            <summary>How much funding is available per person?</summary>
            <div class="faq-body"><p>It depends on your region, how much funding is allocated to your career
            center, your program of choice and other factors. Award amounts are set case by case.</p></div>
          </details>
          <details class="faq-item">
            <summary>How long before I can start training?</summary>
            <div class="faq-body"><p>After you are found eligible and finish the required paperwork,
            evaluations and assessments, we work to place you in the next available cohort.</p></div>
          </details>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Other Options</p>
        <h2 class="section-title left">Additional Funding Sources</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Veterans Benefits</h3>
            <p>If you served, you may have education benefits available. <span class="tbd">Approval status
            for VA benefits: TBD.</span></p>
            <a class="read-more" href="contact.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
          <article class="feature">
            <h3 class="feature-title">Employer Sponsorship</h3>
            <p>Many employers reimburse training that upgrades their workforce. We can provide documentation
            for your employer.</p>
            <a class="read-more" href="contact.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
          <article class="feature">
            <h3 class="feature-title">Scholarships</h3>
            <p><span class="tbd">Placeholder — list any school or community scholarships once they are
            established.</span></p>
            <a class="read-more" href="contact.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
        </div>
      </div>
    </section>

    <section class="steps section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How to Apply</p>
        <h2 class="section-title left">Three Steps to Funding</h2>
        <ol class="step-list">
          <li class="step-card">
            <div class="step-num"><span class="num">1</span><span class="lbl">Step</span></div>
            <div class="step-body">
              <h3>Call us first</h3>
              <p>We will review your situation, tell you which programs are a fit, and explain which funding sources you are likely to qualify for.</p>
            </div>
          </li>
          <li class="step-card">
            <div class="step-num"><span class="num">2</span><span class="lbl">Step</span></div>
            <div class="step-body">
              <h3>Open a file with the career center</h3>
              <p>Complete intake with MassHire, bring your documents, and finish the required assessments. We will tell you exactly what to bring.</p>
            </div>
          </li>
          <li class="step-card">
            <div class="step-num"><span class="num">3</span><span class="lbl">Step</span></div>
            <div class="step-body">
              <h3>Enroll and start</h3>
              <p>Once your funding is approved, we reserve your seat in the next cohort and get you into orientation.</p>
            </div>
          </li>
        </ol>
        <div class="steps-cta">
          <button class="btn btn-navy btn-block js-open-contact" type="button">Find Out If You Qualify</button>
        </div>
      </div>
    </section>

""" + cta("Want to know what we can do for you?")))


# ---- student-financing.html -----------------------------------------------
PAGES.append(dict(
    slug="student-financing.html", nav="student-financing.html",
    title="Ways to Pay for Training in Massachusetts | Career Skills Center",
    ogtitle="Ways to Pay for Training in Massachusetts",
    desc="A plain guide to paying for career training in Massachusetts: WIOA/ITA vouchers, Section 30, Donnelly grants, employer-paid training and payment plans. See what you may qualify for.",
    main=hero("Ways to Pay", "Ways to Pay for Training in Massachusetts",
              "Cost shouldn&rsquo;t be the thing that stops you. Most people combine more than one source. "
              "Here&rsquo;s how paying for training works in Massachusetts, and how to check what you may "
              "qualify for.",
              None, ("Check Your Options", "qualify.html")) + """

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>State-funded training</p>
        <h2 class="section-title left">Massachusetts may pay for your training</h2>
        <p class="lede">Massachusetts runs the system that pays for most career training, through your local
        MassHire career center. You have to apply and qualify, and only a career center can approve funding
        &mdash; but many people don&rsquo;t realize they may be eligible.</p>
        <ul class="check-list">
          <li><strong>WIOA / Individual Training Account (ITA)</strong>A voucher from your MassHire career center that pays for approved training. Register on JobQuest first, then work with a counselor.</li>
          <li><strong>Section 30 (for people on unemployment)</strong>If you get unemployment benefits, Section 30 can let you keep collecting while you train full-time. Apply early &mdash; there are deadlines.</li>
          <li><strong>Donnelly and other state grants</strong>Massachusetts funds training programs through grants like the Senator Kenneth J. Donnelly Workforce Success Grants. These go to organizations, so look for a program funded by one.</li>
        </ul>
        <p><a class="btn btn-yellow" href="qualify.html">Check your options</a>
        <a class="btn btn-outline-navy" href="blog/free-job-training-massachusetts.html">Read the full funding guide</a></p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Other ways to pay</p>
        <h2 class="section-title left">Beyond state funding</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Employer-paid training</h3>
            <p>Ask your employer. Massachusetts employers can be reimbursed for training their staff through the state Workforce Training Fund (including the Express Program).</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Payment plans</h3>
            <p>Many training providers offer monthly payment plans so you can spread the cost out. Ask any provider about terms, interest and whether there&rsquo;s a prepayment penalty before you sign.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Private lenders</h3>
            <p>Some students use a career-training loan. Compare the interest rate, total cost and repayment terms carefully, and treat borrowing as a last resort after grants and vouchers.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Start here</p>
        <h2 class="section-title left">How to begin</h2>
        <ol class="check-list check-list--num">
          <li>Find your MassHire Career Center at <a class="link-yellow" href="https://www.mass.gov/info-details/masshire-career-center-locations" target="_blank" rel="noopener">mass.gov</a> and contact the nearest one.</li>
          <li>Register on JobQuest at <a class="link-yellow" href="https://jobquest.mass.gov" target="_blank" rel="noopener">jobquest.mass.gov</a>.</li>
          <li>Read our guides: <a class="link-yellow" href="blog/free-job-training-massachusetts.html">Free job training in Massachusetts</a> and <a class="link-yellow" href="blog/masshire-training-voucher.html">how to get a MassHire voucher (ITA)</a>.</li>
        </ol>
        <!-- COURSE-DEPENDENT: R-PAY — guide mode: no CSC tuition/terms; "working toward
             approval" disclosure. Course mode: add CSC tuition, payment-plan terms and
             lenders; flip ETPL copy only if FUNDING_ETPL_APPROVED. -->
        <p class="note"><strong>About Career Skills Center and state funding:</strong> Career Skills Center is
        working toward approval to accept state training funds and doesn&rsquo;t have its own courses yet. We can
        help you understand what you may qualify for &mdash; but only your MassHire career center can approve
        funding.</p>
      </div>
    </section>

""" + interest_form("unsure", "training and funding")))


# ---- about.html -----------------------------------------------------------
PAGES.append(dict(
    slug="about.html", nav="about.html",
    title="About Us | Career Skills Center",
    ogtitle="About Career Skills Center",
    desc="Career Skills Center is a Quincy, Massachusetts company building career training and helping workers and employers navigate training funding.",
    main=hero("About Us", "About Us",
              "A Quincy, Massachusetts company building career training &mdash; and helping workers and "
              "employers make sense of how to pay for it. Our focus is your potential.",
              "images/aboutus.webp") + f"""

    <section class="section">
      <div class="container narrow text-center">
        <h2 class="section-title">Our Focus: Your Potential</h2>
        <p class="lede">Our goal isn’t just to help you achieve your potential. It’s to <strong>activate your
        potential</strong>. Career Skills Center is being built to prepare committed adults for rewarding
        careers through practical, job-focused training and real support.</p>
        <p class="lede">Employers today expect more than technical skill. They look for discipline, integrity,
        teamwork and professionalism. We intend to build those habits alongside the skills themselves.</p>
      </div>
      <div class="container narrow">
        <blockquote class="quote-block">
          <p>It is better to be prepared for an opportunity and not have one than to have an opportunity and
          not be prepared.</p>
          <cite>Les Brown</cite>
        </blockquote>
      </div>
    </section>

    <!-- COURSE-DEPENDENT: R-ABOUT — "what we're building" is future tense in guide mode.
         In course mode (SITE_MODE=courses) switch to present tense and add real program
         details. -->
    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>What we&rsquo;re building</p>
        <h2 class="section-title left">Three ways we help</h2>
        <p>Career Skills Center is a new company, and we&rsquo;re building in three directions:</p>
        <ul class="arrow-list">
          <li><strong>Clear funding guidance.</strong> We explain how funding like WIOA and the state Express
          Program works, so workers and employers understand their options and where to go.</li>
          <li><strong>Training for employers and apprenticeships.</strong> We provide training for employer
          teams and support Registered Apprenticeships. Eligible employers can be reimbursed for training
          through the state &mdash; they apply directly; we deliver the training.</li>
          <li><strong>Corporate training.</strong> As we grow, we&rsquo;re building training that companies
          can bring to their teams, funded or self-paid.</li>
        </ul>
        <p>Career Skills Center plans to offer training in healthcare, IT and the skilled trades.
        <a class="link-yellow" href="career-paths.html#interest">Get updates when we launch.</a></p>
      </div>
    </section>

    <!-- PLACEHOLDER: founder name, title, photo and short bio to be supplied by Emilio.
         Keep future/neutral tense until confirmed. -->
    <section class="section" id="founder">
      <div class="container about-grid">
        <div class="about-media">
          <div class="deco-dots deco-dots--about" aria-hidden="true"></div>
          <img src="images/aboutus.webp" alt="" loading="lazy" decoding="async">
        </div>
        <div class="about-copy">
          <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Who we are</p>
          <h2 class="section-title left">Founded in Quincy</h2>
          <p>Career Skills Center is based in Quincy, Massachusetts. We started it because too many capable
          people never get a fair shot at good training &mdash; either they can&rsquo;t find the funding or
          no one explains how it works.</p>
          <p><span class="tbd">[Founder name and short bio &mdash; to be supplied.]</span></p>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>What We Stand For</p>
        <h2 class="section-title left">Our Values</h2>
        <div class="section-intro">
          <p>We&rsquo;re building this company around a few simple commitments.</p>
        </div>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Practical, skills-first</h3>
            <p>Training built around what the job actually requires, not just theory.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Honest guidance</h3>
            <p>Straight answers about cost, funding and what a credential really gets you. No pressure and no surprises.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Industry relevance</h3>
            <p>Focused on the credentials and skills employers actually hire for.</p>
          </article>
        </div>
        <div class="feature-grid" style="margin-top: 40px;">
          <article class="feature">
            <h3 class="feature-title">Access</h3>
            <p>We help people find the funding that makes training possible, not just the training itself.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Growth mindset</h3>
            <p>Everyone starts somewhere. Effort and coaching close the gap faster than talent alone.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Community</h3>
            <p>Rooted in Quincy, we want to strengthen the workforce and the employers around us.</p>
          </article>
        </div>
      </div>
    </section>

    <!-- COURSE-DEPENDENT: R-ABOUT — career-support copy is future tense in guide mode.
         In course mode switch to present tense and add real details. -->
    <section class="section">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Career support</p>
        <h2 class="section-title left">Support that continues after training</h2>
        <p>Training is only worth it if it leads to a job. As our programs launch, career support &mdash; help
        with your resume, interview practice and connections to employers &mdash; will be built into every
        program, not treated as an afterthought.</p>
      </div>
    </section>

    <section class="section section--alt section--tight">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Get in touch</p>
        <h2 class="section-title left">Talk to us</h2>
        <p>Career Skills Center &middot; Quincy, MA 02171<br>
        <a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a> &middot;
        <a class="link-yellow" href="mailto:info@careerskillscenter.com">info@careerskillscenter.com</a></p>
        <p><a class="btn btn-yellow" href="contact.html">Contact us</a></p>
      </div>
    </section>

""" + interest_form("unsure", "our programs")))


# ---- team.html ------------------------------------------------------------
# ---- team.html ------------------------------------------------------------
def team_card(name, role, bio):
    return f"""          <article class="team-card">
            <div class="team-photo">Headshot placeholder</div>
            <div class="team-body">
              <h3>{name}</h3>
              <p class="team-role">{role}</p>
              <p>{bio}</p>
            </div>
          </article>"""


PAGES.append(dict(
    slug="team.html", nav="team.html",
    title="Meet the Team | Career Skills Center — Massachusetts",
    ogtitle="Meet the Team",
    desc="The leadership and instructors behind Career Skills Center in Massachusetts.",
    main=hero("Leadership", "Meet the Team",
              "The people behind the programs. Our instructors have worked in the fields they teach, and our "
              "staff is here from your first call through your first job.",
              "images/person2.webp") + f"""

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Leadership &amp; Staff</p>
        <h2 class="section-title left">Leadership</h2>
        <div class="section-intro">
          <p>Names, titles, biographies and headshots below are placeholders. Replace each card with a real
          team member before publishing.</p>
        </div>
        <div class="team-grid">
{team_card("[Name]", "Chief Executive Officer", "Two to four sentences on background, years of experience, and what they are responsible for at Career Skills Center.")}
{team_card("[Name]", "Director of Operations", "Two to four sentences on background, years of experience, and what they are responsible for at Career Skills Center.")}
{team_card("[Name]", "Director of Admissions", "Two to four sentences on background, years of experience, and what they are responsible for at Career Skills Center.")}
{team_card("[Name]", "Director of Career Services", "Two to four sentences on background, years of experience, and what they are responsible for at Career Skills Center.")}
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Instructors</p>
        <h2 class="section-title left">Skilled Trades Faculty</h2>
        <div class="team-grid">
{team_card("[Name]", "Electrical Instructor", "Years in the field, licenses held, and what students say about their teaching.")}
{team_card("[Name]", "HVAC/R Instructor", "Years in the field, licenses held, and what students say about their teaching.")}
{team_card("[Name]", "Plumbing Instructor", "Years in the field, licenses held, and what students say about their teaching.")}
        </div>

        <h2 class="section-title left" style="margin-top: 64px;">Information Technology Faculty</h2>
        <div class="team-grid">
{team_card("[Name]", "IT Support Instructor", "Certifications held, industry background, and teaching focus.")}
{team_card("[Name]", "Networking &amp; Security Instructor", "Certifications held, industry background, and teaching focus.")}
        </div>

        <h2 class="section-title left" style="margin-top: 64px;">Medical Faculty</h2>
        <div class="team-grid">
{team_card("[Name]", "Medical Assistant Instructor", "Clinical background, credentials held, and teaching focus.")}
{team_card("[Name]", "Phlebotomy &amp; EKG Instructor", "Clinical background, credentials held, and teaching focus.")}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container narrow text-center">
        <h2 class="section-title">Join Our Team</h2>
        <p class="lede">We are always interested in hearing from experienced tradespeople, IT professionals
        and clinicians who want to teach. If that is you, send us a note and tell us what you would want to
        teach.</p>
        <p><a class="btn btn-navy" href="mailto:info@careerskillscenter.com">Email Us</a></p>
      </div>
    </section>

""" + cta("Want to know what we can do for you?")))


# ---- career-services.html -------------------------------------------------
PAGES.append(dict(
    slug="career-services.html", nav="career-services.html",
    title="Career Services | Career Skills Center — Massachusetts",
    ogtitle="Career Services",
    desc="The career support Career Skills Center is building into every program: resume help, interview practice and employer connections for Massachusetts students.",
    main=hero("Career Services", "Career Services",
              "Training is only worth it if it leads to a job. Career support will be built into every program "
              "we offer.",
              None) + """

    <section class="section">
      <div class="container narrow text-center">
        <h2 class="section-title">Support we&rsquo;re building in</h2>
        <p class="lede">Career Skills Center&rsquo;s programs are in development, and career support is part of
        the plan from day one &mdash; not an afterthought. Here&rsquo;s what we intend to offer every student.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Resume &amp; application help</h3>
            <p>Help writing a resume that puts your new credential first, and a review of applications before you send them.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Interview practice</h3>
            <p>Mock interviews, tips on presentation, and guidance on following up after an interview.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Employer connections</h3>
            <p>Introductions to Massachusetts employers &mdash; clinics, IT departments and contractors &mdash; who hire for these roles.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Certification exam prep</h3>
            <p>Practice and review so you&rsquo;re ready to sit for your credential while the material is fresh.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Our approach</p>
        <h2 class="section-title left">Real support, not a waiting list</h2>
        <p>The plan is simple: work with every student through completion and stay available afterward, so you
        feel supported, prepared, and ready for the next step. As programs launch, we&rsquo;ll share exactly how
        career services works and what it includes.</p>
      </div>
    </section>

""" + interest_form("unsure", "career services and program")))


# ---- faq.html -------------------------------------------------------------
def faq(q, a):
    return f"""          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>"""


PAGES.append(dict(
    slug="faq.html", nav="faq.html",
    title="FAQ | Career Skills Center — Massachusetts",
    ogtitle="Frequently Asked Questions",
    desc="Answers about career training and funding in Massachusetts: how state funding works, how to find your MassHire career center, and when Career Skills Center will launch training.",
    main=hero("FAQ", "Find Answers",
              "The questions we hear most about training and funding, answered plainly. If "
              "yours is not here, call us at (617) 544-7155.",
              None, ("Do I Qualify?", "qualify.html")) + f"""

    <section class="section">
      <div class="container">
        <div class="faq">

          <p class="faq-group-title">Careers &amp; training</p>
{faq("Do I need a college degree to get a good job?", 'Not always. Many jobs in healthcare, IT and the skilled trades are open to people without a four-year degree, and several can be trained for in months. See our <a class="link-yellow" href="career-paths.html">career paths</a> for what each field pays and how to train.')}
{faq("Can I train online?", 'It depends on the field. Office-based roles like medical billing and IT support are very online-friendly. Hands-on roles &mdash; medical assistant, phlebotomy, and the licensed trades &mdash; can start online but need in-person practice or supervised hours.')}
{faq("How long does training take?", 'It varies. Some healthcare and IT certificates take a few months, while licensed trades take years of apprenticeship. Each <a class="link-yellow" href="career-paths.html">career guide</a> explains the typical path.')}

          <p class="faq-group-title">Paying for training</p>
{faq("How much does training cost, and how do people pay?", 'It varies by program and provider. Most people combine sources &mdash; state funding, employer help, and sometimes a payment plan. See <a class="link-yellow" href="student-financing.html">Ways to Pay</a>.')}
{faq("Can Massachusetts pay for my training?", 'You may qualify for funded training through a MassHire career center (a WIOA/ITA voucher). If you get unemployment benefits, ask about Section 30. Only your career center can approve funding. Start with our <a class="link-yellow" href="blog/wioa-eligibility-massachusetts.html">WIOA eligibility guide</a>.')}
{faq("Where do I actually start?", 'Two free steps: find your MassHire Career Center at <a class="link-yellow" href="https://www.mass.gov/info-details/masshire-career-center-locations" target="_blank" rel="noopener">mass.gov</a>, and register on <a class="link-yellow" href="https://jobquest.mass.gov" target="_blank" rel="noopener">JobQuest</a>. Or take our quick <a class="link-yellow" href="qualify.html">Check Your Options</a> quiz.')}
{faq("Do you accept VA benefits?", 'Career Skills Center does not have its own courses yet. If you served, you may have education benefits like the GI Bill &mdash; the VA&rsquo;s GI Bill Comparison Tool shows which schools are approved.')}

          <p class="faq-group-title">For employers</p>
{faq("Can my company get training reimbursed?", 'We provide the training; the reimbursement comes from the state. Through the Workforce Training Fund Express Program, eligible Massachusetts employers can be reimbursed for much of what they spend on training &mdash; you apply directly to the state. See <a class="link-yellow" href="staff-training-grants.html">Staff Training Grants</a> and <a class="link-yellow" href="express-program-explained.html">how Express works</a>.')}
{faq("Do you run apprenticeships?", 'Career Skills Center provides the training side &mdash; we can deliver the related classroom instruction a Registered Apprenticeship requires. Employers register and run the apprenticeship with the state. See <a class="link-yellow" href="apprenticeships.html">Apprenticeship Programs</a>.')}
{faq("Can you train my team on something specific?", 'Tell us what your team needs. We&rsquo;re building <a class="link-yellow" href="corporate-training.html">corporate training</a> for employers, with or without state funding.')}

          <p class="faq-group-title">About Career Skills Center</p>
{faq("Does Career Skills Center offer courses right now?", 'Not yet. Career Skills Center plans to offer training in healthcare, IT and the skilled trades. For now, this site is an honest guide to careers and funding. <!-- COURSE-DEPENDENT: R-FAQ --> Join an interest list on any <a class="link-yellow" href="career-paths.html">career guide</a> and we&rsquo;ll let you know when we launch.')}
{faq("When will training launch?", 'We don&rsquo;t have a public date yet. The best way to hear first is to join an interest list on a <a class="link-yellow" href="career-paths.html">career guide</a>. In the meantime, our guides help you start now through the state.')}
{faq("Where are you located?", "Career Skills Center is based in Quincy, Massachusetts.")}
{faq("How can I reach you?", 'Call <a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a> or email <a class="link-yellow" href="mailto:info@careerskillscenter.com">info@careerskillscenter.com</a>, or use our <a class="link-yellow" href="contact.html">contact form</a>.')}

        </div>
      </div>
    </section>

""" + cta("Still have questions? Call (617) 544-7155.")))


# ---- media.html -----------------------------------------------------------
# ---- media.html -----------------------------------------------------------
def media_card(date, title, body):
    return f"""          <article class="media-card">
            <div class="media-thumb">Image placeholder</div>
            <div class="media-body">
              <p class="media-date">{date}</p>
              <h3>{title}</h3>
              <p>{body}</p>
            </div>
          </article>"""


PAGES.append(dict(
    slug="media.html", nav="media.html",
    title="Media | Career Skills Center — Massachusetts",
    ogtitle="Media",
    desc="News, press and media resources from Career Skills Center in Massachusetts.",
    main=hero("Media", "In the News",
              "Announcements, student stories and press resources from Career Skills Center.",
              "images/Todaybanner2.webp") + f"""

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Featured</p>
        <h2 class="section-title left">News &amp; Updates</h2>
        <div class="section-intro">
          <p>Placeholder entries. Replace each card with a real announcement, article or student story as
          they happen.</p>
        </div>
        <div class="media-grid">
{media_card("Month DD, YYYY", "[Headline placeholder]", "One or two sentences summarizing the announcement, with a link to the full article or release.")}
{media_card("Month DD, YYYY", "[Headline placeholder]", "One or two sentences summarizing the announcement, with a link to the full article or release.")}
{media_card("Month DD, YYYY", "[Headline placeholder]", "One or two sentences summarizing the announcement, with a link to the full article or release.")}
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Gallery</p>
        <h2 class="section-title left">Photos &amp; Video</h2>
        <div class="gallery-grid">
          <div class="gallery-slot">Photo</div>
          <div class="gallery-slot">Photo</div>
          <div class="gallery-slot">Photo</div>
          <div class="gallery-slot">Photo</div>
          <div class="gallery-slot">Photo</div>
          <div class="gallery-slot">Photo</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="split-grid">
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Press Kit</p>
            <h2 class="section-title left">For Journalists</h2>
            <p>Career Skills Center is a career training school based in Quincy, Massachusetts, offering
            hands-on programs in the skilled trades, information technology and the medical field for
            students across Massachusetts.</p>
            <p>For interviews, campus visits or media requests, contact
            <a class="link-yellow" href="mailto:info@careerskillscenter.com">info@careerskillscenter.com</a>
            or call <a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a>.</p>
            <ul class="arrow-list">
              <li>Logo files <span class="tbd">(TBD)</span></li>
              <li>Campus photography <span class="tbd">(TBD)</span></li>
              <li>Leadership headshots and bios <span class="tbd">(TBD)</span></li>
            </ul>
          </div>
          <div class="split-media">
            <img src="images/aboutus.webp" alt="Career Skills Center campus" loading="lazy" decoding="async">
          </div>
        </div>
      </div>
    </section>

""" + cta("Want to know what we can do for you?")))


# ---- blog.html ------------------------------------------------------------
# Image-free blog index. Card layout leans on type, borders and colour accents.
# Post titles/excerpts below are PLACEHOLDER drafts; the real first article is
# the next task. Article links point to "#" until those pages exist.
def post_card(tag, date, read, title, excerpt, href="#"):
    return f"""          <a class="post-card" href="{href}">
            <span class="post-tag">{tag}</span>
            <p class="post-meta">{date}<span class="dot-sep"></span>{read}</p>
            <h3>{title}</h3>
            <p>{excerpt}</p>
            <span class="read-link">Read article</span>
          </a>"""

# Real launch posts. Order = newest first in the grid (the pillar is featured
# above the grid, so it is not repeated here). href points into /blog/.
BLOG_POSTS = [
    ("Paying for Training", "Sep 25, 2026", "8 min read",
     "Who Qualifies for WIOA Training in Massachusetts?",
     "WIOA training is for adults, dislocated workers, and low-income residents. Your local MassHire "
     "career center makes the final call. Here is how eligibility works.",
     "blog/wioa-eligibility-massachusetts.html"),
    ("Paying for Training", "Sep 25, 2026", "7 min read",
     "How to Get a MassHire Training Voucher (ITA): Step by Step",
     "An Individual Training Account (ITA) can pay for approved courses. Here is the step-by-step path, "
     "from your first career-center visit to an approved voucher.",
     "blog/masshire-training-voucher.html"),
    ("Paying for Training", "Sep 25, 2026", "6 min read",
     "Is WIOA Training Really Free? What's Covered and What Isn't",
     "WIOA can cover tuition and some costs, but not always everything. Here is an honest look at what a "
     "grant usually pays for and what you may still owe.",
     "blog/is-wioa-training-free.html"),
    # Post #5 (Highest-Paying Certifications) is ON HOLD until the pay-data work is
    # done (Site Structure Spec v1.5 §6). Kept in the build (noindex, off the sitemap)
    # but not featured in the index.
    ("Medical", "Sep 25, 2026", "6 min read",
     "Can Medical Billing and Coding Be Learned Online?",
     "Yes. Medical billing and coding is one of the healthcare fields you can learn fully online. Here is "
     "what the training covers and what employers want to see.",
     "blog/can-medical-billing-coding-be-learned-online.html"),
    ("Information Technology", "Sep 25, 2026", "6 min read",
     "Can You Learn IT Support Online? What Employers Actually Look For",
     "You can learn IT support online, and many people do. What matters most is a recognized "
     "certification and hands-on practice. Here is how to build both.",
     "blog/can-you-learn-it-support-online.html"),
    ("Skilled Trades", "Sep 25, 2026", "6 min read",
     "Can You Learn a Skilled Trade Online? What Works and What Needs Hands-On Time",
     "Some of a trade can be learned online: theory, codes, and safety. But the hands-on hours still "
     "matter. Here is what works online and what does not.",
     "blog/can-you-learn-a-trade-online.html"),
]

PAGES.append(dict(
    slug="blog.html", nav="blog.html",
    title="Blog | Career Skills Center — Massachusetts",
    ogtitle="Career Skills Center Blog",
    desc="Plain-language guides to career training and how to pay for it in Massachusetts, in the medical field, IT, and the skilled trades.",
    main=hero("Blog", "Career Insights",
              "Straight talk on training, careers, and how to pay for it, in the skilled trades, information "
              "technology, and the medical field. Written by the team at Career Skills Center.",
              "images/aboutus.webp") + f"""

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Latest</p>
        <h2 class="section-title left">From the Blog</h2>
        <div class="section-intro">
          <p>Practical articles for people deciding whether career training is right for them, and for
          students already on their way. No fluff, no jargon.</p>
        </div>

        <!-- Category filters: visual only for now. Wire them to real filtering
             or per-category pages once the article set grows. -->
        <div class="blog-filters" role="list" aria-label="Filter by topic">
          <a class="filter-pill is-active" href="blog.html" role="listitem">All</a>
          <a class="filter-pill" href="#" role="listitem">Paying for Training</a>
          <a class="filter-pill" href="#" role="listitem">Medical</a>
          <a class="filter-pill" href="#" role="listitem">Information Technology</a>
          <a class="filter-pill" href="#" role="listitem">Skilled Trades</a>
          <a class="filter-pill" href="#" role="listitem">Career Advice</a>
        </div>

        <!-- Featured: the funding pillar post -->
        <a class="post-featured" href="blog/free-job-training-massachusetts.html">
          <p class="post-meta"><span class="post-tag">Paying for Training</span></p>
          <p class="post-meta">Sep 25, 2026<span class="dot-sep"></span>11 min read</p>
          <h2>Free Job Training in Massachusetts: WIOA, MassHire and State Grants Explained</h2>
          <p>The complete, plain-language guide to the state and federal programs that can help pay for
          career training in Massachusetts &mdash; what they are, who they are for, and how to start.</p>
          <span class="read-link">Read article</span>
        </a>

        <div class="post-grid">
{chr(10).join(post_card(*p) for p in BLOG_POSTS)}
        </div>
      </div>
    </section>

""" + cta("Have a topic you want us to cover?", "Get in Touch")))


# ===========================================================================
# BLOG ARTICLES  (/blog/<slug>.html)
# ---------------------------------------------------------------------------
# All eight are DRAFTS for Emilio's review (see the <!-- DRAFT --> note at the
# top of each body). Compliance: no post claims Career Skills Center is
# ETPL-approved, WIOA-funded, or an approved/listed Express provider. Funding
# posts use the "we're working toward approval / here are options now" wording
# while FUNDING_ETPL_APPROVED is false. No invented statistics or salary
# figures — anything unverified is marked [VERIFY ...] for Emilio.
# ===========================================================================

# Reused funding disclosure box (matches FUNDING_ETPL_APPROVED = false wording).
# ---- 1. Pillar: Free Job Training in Massachusetts ------------------------
_p1_body = """        <!-- DRAFT – verified against docs/VERIFICATION_LOG.md (9/25/2026): center count "more than 25" (A1);
             Donnelly totals/dates $7.4M Oct 2025 + $5.9M Aug 2026 (A2); locator URL (A3); Section 30/TOP rules
             (B2); MDCS/ETPL/ITA (B1); income example is regional (B3). Still pending Emilio: the checklist
             download PDF (A9). Do NOT state ITA dollar caps — they vary by region. -->
        <p class="lead">Yes — Massachusetts has several real ways to get career training paid for, and most run
        through your local <strong>MassHire career center</strong>. This guide covers the five main options in
        plain language: what each one is, who it is for, and where to start.</p>

        <p>There is no single "free training" button. The money comes from a few different programs, each with
        its own rules. Many people combine more than one. Here is the whole picture in one place.</p>

        <h2>The 5 main ways to get training paid for in Massachusetts</h2>
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr><th>Program</th><th>Who it's for</th><th>What it pays</th><th>Where to start</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>WIOA training voucher (ITA)</strong></td><td>Laid-off workers, lower-income adults, youth</td><td>Tuition at an approved program (amount set by your career center)</td><td>MassHire career center</td></tr>
              <tr><td><strong>Section 30 / TOP</strong></td><td>People collecting unemployment</td><td>Keeps your unemployment checks coming during full-time training (not tuition)</td><td>DUA (apply by the 20th paid week)</td></tr>
              <tr><td><strong>Donnelly Workforce Success programs</strong></td><td>Unemployed and underemployed residents</td><td>Free training run by grant-funded partners</td><td>Program partners across MA (changes by year)</td></tr>
              <tr><td><strong>Employer-paid (Workforce Training Fund &ndash; Express)</strong></td><td>People already working</td><td>Your employer gets reimbursed for training staff</td><td>Your employer or HR</td></tr>
              <tr><td><strong>Payment plans &amp; other options</strong></td><td>Anyone</td><td>Spreads the cost out over time</td><td>The school</td></tr>
            </tbody>
          </table>
        </div>
        <p>The rest of this guide explains each one, then shows you the honest first step.</p>

        <h2>How the system is organized</h2>
        <p>Massachusetts is divided into <strong>16 workforce regions</strong>. Each region has a MassHire
        Workforce Board and one or more <strong>MassHire career centers</strong> &mdash; more than 25 across
        the state. These centers are free, state-run offices that help residents find jobs and pay for training.
        You may still hear the older name, "One-Stop Career Centers."</p>
        <p>One word you will see a lot is <strong>ETPL</strong>. It stands for the Eligible Training Provider
        List &mdash; the state's list of approved programs. A training voucher can only pay for a program that
        is on that list. Keep that in mind when you choose a school.</p>

        <h2>1. WIOA training vouchers (the ITA)</h2>
        <p>WIOA stands for the <strong>Workforce Innovation and Opportunity Act</strong>. It is a federal law
        that sends money to each state to help people train for in-demand jobs. In Massachusetts, that money is
        handled locally by MassHire career centers.</p>
        <p>If you qualify, WIOA can pay for approved training through an <strong>Individual Training Account
        (ITA)</strong> &mdash; think of it as a voucher for tuition at an ETPL-approved school. Your career
        center decides who qualifies and how much they can offer, so amounts vary by region. We do not list a
        dollar cap here because it is different from place to place.</p>
        <p>Career centers do not fund just any training. They look for programs that lead to jobs that are
        actually hiring in Massachusetts &mdash; health care, IT, skilled trades, and similar fields. Short,
        job-focused programs that end in a recognized credential tend to be the easiest to get approved.</p>
        <p>Two guides go deeper: <a href="blog/wioa-eligibility-massachusetts.html">Who qualifies for WIOA
        training in Massachusetts?</a> and <a href="blog/masshire-training-voucher.html">How to get a MassHire
        training voucher (ITA), step by step</a>. And for the honest answer on cost, see
        <a href="blog/is-wioa-training-free.html">Is WIOA training really free?</a></p>

        <h2>2. Section 30 / TOP: get paid while you train</h2>
        <p>Here is one many people miss. If you are collecting unemployment, the
        <strong>Training Opportunities Program (TOP)</strong>, also called <strong>Section 30</strong>, can let
        you keep getting your unemployment checks while you go to full-time approved training.</p>
        <p>The basics:</p>
        <ul>
          <li>Your training must be full-time &mdash; at least 20 classroom hours a week.</li>
          <li>It can add <strong>up to 26 extra weeks</strong> of benefits so you can finish.</li>
          <li>You usually must apply to the Department of Unemployment Assistance (DUA)
          <strong>by the 20th paid week</strong> of your claim, so do not wait.</li>
          <li>Section 30 does <em>not</em> pay tuition &mdash; it protects your income while you study. You can
          use it together with a WIOA voucher.</li>
        </ul>
        <p>Here is what that looks like in real life. Say you were laid off and started collecting unemployment.
        Instead of job-searching part-time, you enroll full-time in an approved program. With Section 30, your
        weekly checks keep coming while you study, and you may get extra weeks so your benefits do not run out
        before you finish.</p>
        <p>Read the state's page: <a href="https://www.mass.gov/info-details/training-opportunities-program-section-30">Training
        Opportunities Program (Section 30)</a>.</p>

        <h2>3. Donnelly Workforce Success programs</h2>
        <p>The <strong>Senator Kenneth J. Donnelly Workforce Success Grants</strong> (once called the Workforce
        Competitiveness Trust Fund) pay for training partnerships that serve unemployed and underemployed
        residents. Here is the key point: the money goes to <em>organizations</em>, not to individuals. Those
        organizations then offer training free to the people they serve.</p>
        <p>So you do not apply for a Donnelly grant yourself &mdash; you look for a local program that is funded
        by one. These change from year to year. To show this is real money: recent rounds awarded about
        <strong>$7.4 million (October 2025)</strong> and <strong>$5.9 million (August 2026)</strong>. Learn more
        at <a href="https://commcorp.org/program/senatordonnellygrants/">commcorp.org</a>.</p>

        <h2>4. Employer-paid training (Workforce Training Fund &ndash; Express)</h2>
        <p>If you already have a job, your employer may be able to get part of your training cost reimbursed by
        the state through the <strong>Workforce Training Fund Express Program</strong>, run by Commonwealth
        Corporation. This is money employers pay into, meant to train current staff. If that could be you, ask
        your manager or HR &mdash; and point them to our information for employers when we publish it.</p>

        <h2>5. Payment plans and other options</h2>
        <ul>
          <li><strong>Payment plans.</strong> Many schools, including us, offer a monthly plan so you can spread
          the cost out. See <a href="student-financing.html">Ways to Pay</a>.</li>
          <li><strong>Veterans benefits.</strong> If you served, you may have education benefits (like the GI
          Bill). The VA's <a href="https://www.va.gov/education/gi-bill-comparison-tool/">GI Bill Comparison
          Tool</a> shows which schools are approved.</li>
          <li><strong>Scholarships and community programs.</strong> Local nonprofits and workforce boards
          sometimes offer help. Your career center can point you to these.</li>
        </ul>

        <h2>Which option fits your situation?</h2>
        <ul>
          <li><strong>Just laid off?</strong> Start with a WIOA voucher as a dislocated worker, and ask about
          Section 30 to keep your unemployment while you train.</li>
          <li><strong>Working, but low pay?</strong> You may still qualify for a WIOA voucher as an adult. Ask
          your career center, and check whether your employer would use the Express Program.</li>
          <li><strong>On unemployment and want to keep your checks?</strong> Section 30 is built for you &mdash;
          just watch the 20th-week deadline.</li>
          <li><strong>Not eligible right now, or the funds are gone?</strong> Look for a Donnelly-funded free
          program, ask about veterans benefits if you served, or use a monthly payment plan to start now.</li>
          <li><strong>Already employed and your boss is open to it?</strong> The Express Program can reimburse
          your employer for training you.</li>
        </ul>
        <p>Most people mix and match. Your career center will help you build a plan that fits.</p>

        <h2>How long does it take?</h2>
        <div class="note"><strong>Plan on about 6&ndash;8 weeks</strong> from your first call to your first
        class. That covers an information meeting, an assessment, paperwork, and approval. One warning:
        <strong>funds can run out mid-year</strong>, so the earlier in the year you start, the better.</div>

        <h2>What to bring to your career center</h2>
        <p>Centers ask for different things, but most want to see:</p>
        <ul>
          <li>Proof you are allowed to work in the U.S.</li>
          <li>Proof of your age (a photo ID works).</li>
          <li>Selective Service registration, if you are a man born after January 1, 1960.</li>
          <li>Your household income for about the last 6 months.</li>
          <li>Proof of your family size.</li>
          <li>Layoff paperwork, if you were laid off.</li>
        </ul>
        <div class="note"><strong>Coming soon:</strong> a printable "Paying for Training in Massachusetts"
        checklist you can download and bring with you. <span class="tbd">[TODO: wire up the checklist download
        (needs the form backend + PDF from Emilio).]</span></div>

        <h2>The honest first step</h2>
        <ol>
          <li>Register in <strong>MassHire JobQuest</strong> at
          <a href="https://jobquest.mass.gov">jobquest.mass.gov</a> (you will also set up a MyMassGov account).</li>
          <li>Find your local MassHire career center &mdash; it is based on where you live or last worked. Search
          at <a href="https://www.mass.gov/info-details/masshire-career-center-locations">mass.gov (MassHire
          career center locations)</a>.</li>
          <li>Call or visit and say: "I want to train for a new career, and I want to know what funding I might
          qualify for."</li>
          <li>Ask about WIOA and an ITA &mdash; and if you are on unemployment, ask about Section 30 at the same
          time.</li>
          <li>Pick an approved program that fits your goals. Career Skills Center is preparing programs in IT,
          Medical Billing &amp; Coding and Skilled Trades &mdash; <a href="contact.html">join our interest
          list</a> to hear when they open.</li>
        </ol>
        <p>You do not have to figure this out alone. Career centers exist to help, and they do not charge you to
        walk in and ask.</p>

        <h2>The bottom line</h2>
        <p>Free or low-cost training in Massachusetts is real, but it takes a few steps and a little patience.
        The single best move is to register in JobQuest and talk to your local MassHire career center early
        &mdash; before funds run low for the year. Bring your documents, ask about every option above, and pick
        an approved program that leads to a job you actually want.</p>
        <p>And if funding does not come through right away, that does not have to stop you. A payment plan can
        get you started now, and you can keep working on funding in the background.</p>

""" + FUNDING_NOTE + """

""" + post_cta(
    "Want help figuring out how to pay?",
    "Start with how the main public training fund works, then check what you may qualify for. It only takes a "
    "minute.",
    "How WIOA works", "wioa-explained.html") + """

        <h2>Frequently asked questions</h2>
        <div class="faq">
          <details class="faq-item"><summary>Is job training really free in Massachusetts?</summary>
          <div><p>It can be, for people who qualify. Programs like WIOA, handled through MassHire career centers,
          can pay for approved training. It is not automatic &mdash; your local career center decides &mdash; and
          "free" may not cover 100% of every cost. Ask your career center what you qualify for.</p></div></details>
          <details class="faq-item"><summary>Can I get paid while I'm in training?</summary>
          <div><p>You may be able to. If you are collecting unemployment, Section 30 (the Training Opportunities
          Program) can let you keep your benefits during full-time approved training &mdash; at least 20 classroom
          hours a week, for up to 26 extra weeks. You usually must apply by the 20th paid week of your claim.</p></div></details>
          <details class="faq-item"><summary>Do I have to be unemployed to get WIOA funding?</summary>
          <div><p>No. WIOA serves adults, dislocated workers, and youth. People who are working but earning low
          wages may also qualify. Your career center reviews your situation.</p></div></details>
          <details class="faq-item"><summary>Do I need to be a U.S. citizen?</summary>
          <div><p>Not necessarily, but you generally must be authorized to work in the United States, and centers
          will ask for proof. Rules can vary, so ask your career center about your situation.</p></div></details>
          <details class="faq-item"><summary>Can I choose any school?</summary>
          <div><p>No. To use a training voucher, the program must be on the state's approved list (the ETPL). You
          can search approved programs in MassHire JobQuest.</p></div></details>
          <details class="faq-item"><summary>Can I train online?</summary>
          <div><p>Yes, as long as the online program is approved. Online training can be a great fit for fields
          like medical billing and coding or IT support.</p></div></details>
          <details class="faq-item"><summary>What if my career center says the funds are gone?</summary>
          <div><p>It happens, because funding is limited each year. Ask about the next program year, look for a
          Donnelly-funded free program, or use a payment plan to start now. See
          <a href="student-financing.html">Ways to Pay</a>.</p></div></details>
          <details class="faq-item"><summary>How long does it take to get approved?</summary>
          <div><p>Plan on about 6 to 8 weeks, though it varies by career center and by how quickly you complete
          the steps. Start early, because funds can run out mid-year and training must be approved before it
          begins.</p></div></details>
          <details class="faq-item"><summary>Does Career Skills Center accept WIOA funding?</summary>
          <div><p>We are working toward approval to accept state training funds. Until then, we will help you
          check what you may qualify for and show you other ways to pay, like a monthly payment plan. Only your
          MassHire career center can approve funding.</p></div></details>
        </div>

""" + related(
    ("Who Qualifies for WIOA Training in Massachusetts?", "blog/wioa-eligibility-massachusetts.html"),
    ("How to Get a MassHire Training Voucher (ITA)", "blog/masshire-training-voucher.html"),
    ("Is WIOA Training Really Free?", "blog/is-wioa-training-free.html"),
)

PAGES.append(dict(
    slug="blog/free-job-training-massachusetts.html", nav="blog.html",
    title="Free Job Training in Massachusetts: WIOA, MassHire & State Grants | Career Skills Center",
    ogtitle="Free Job Training in Massachusetts: WIOA, MassHire & State Grants Explained",
    desc="A plain-language guide to free and low-cost career training in Massachusetts: WIOA, MassHire career centers, Individual Training Accounts, and other ways to pay.",
    extrahead=article_ld("blog/free-job-training-massachusetts.html",
                         "Free Job Training in Massachusetts: WIOA, MassHire and State Grants Explained",
                         "A plain-language guide to free and low-cost career training in Massachusetts.",
                         "2026-09-25", "2026-09-25") + "\n" + faq_ld([
        ("Is job training really free in Massachusetts?",
         "It can be, for people who qualify. Programs like WIOA, handled through MassHire career centers, can pay for approved training. It is not automatic and may not cover 100% of every cost. Ask your local career center what you qualify for."),
        ("Can I get paid while I'm in training?",
         "You may be able to. If you are collecting unemployment, Section 30 (the Training Opportunities Program) can let you keep your benefits during full-time approved training — at least 20 classroom hours a week, for up to 26 extra weeks. You usually must apply by the 20th paid week of your claim."),
        ("Do I have to be unemployed to get WIOA funding?",
         "No. WIOA serves adults, dislocated workers, and youth. People who are working but earning low wages may also qualify. Your career center reviews your situation."),
        ("Do I need to be a U.S. citizen to get WIOA training funds?",
         "Not necessarily, but you generally must be authorized to work in the United States, and centers will ask for proof. Rules can vary, so ask your career center about your situation."),
        ("Can I choose any school for a WIOA training voucher?",
         "No. To use a training voucher, the program must be on the state's approved list (the Eligible Training Provider List, or ETPL). You can search approved programs in MassHire JobQuest."),
        ("Can I train online with WIOA funding?",
         "Yes, as long as the online program is approved. Online training can be a great fit for fields like medical billing and coding or IT support."),
        ("What if my career center says the funds are gone?",
         "It happens, because funding is limited each year. Ask about the next program year, look for a Donnelly-funded free program, or use a payment plan to start now."),
        ("How long does it take to get approved?",
         "Plan on about 6 to 8 weeks, though it varies by career center and how quickly you complete the steps. Start early because funds can run out mid-year and training must be approved before it begins."),
        ("Does Career Skills Center accept WIOA funding?",
         "Career Skills Center is working toward approval to accept state training funds. Until then, it will help you check what you may qualify for and show other ways to pay. Only your MassHire career center can approve funding."),
    ]),
    main=article(
        "Paying for Training",
        "Free Job Training in Massachusetts: WIOA, MassHire and State Grants Explained",
        "Everything you need to know about the state and federal programs that can help pay for career "
        "training in Massachusetts — in plain language.",
        "September 25, 2026", "12 min read", _p1_body)))


# ---- 2. Who Qualifies for WIOA Training in Massachusetts ------------------
_p2_body = """        <!-- DRAFT – verified against docs/VERIFICATION_LOG.md (9/25/2026): priority of service (B5),
             final decision is the local center's (B6), basic requirements incl. Selective Service (B7), income
             example $15,960–$60,124+ is a regional example only (B3). Dislocated-worker timing left soft
             ("varies, so ask"). No CSC program details (F1). Do not promise approval. -->
        <p class="lead">WIOA training in Massachusetts is mainly for three groups: adults (with priority for
        people with lower incomes), dislocated workers, and young people aged 16&ndash;24. But there is an
        important catch: your local <strong>MassHire career center</strong> makes the final decision, based on
        your situation and the funding available.</p>

        <p>That means the honest answer to "do I qualify?" is: maybe — and the only way to know for sure is to
        ask your career center. Here is what they generally look at.</p>

        <h2>The three main groups</h2>
        <h3>1. Adults</h3>
        <p>This is the broadest group. If you are 18 or older and want to train for a better job, you can ask.
        Career centers give priority to people who receive public assistance (like SNAP or TAFDC), earn low
        wages, or need to build basic reading or math skills. You do not have to be jobless to apply.</p>
        <h3>2. Dislocated workers</h3>
        <p>A "dislocated worker" is usually someone who lost a job through no fault of their own — a layoff, a
        plant or business closing, or the end of a contract. Often it means you are getting (or have used up)
        unemployment and are unlikely to return to the same kind of work. It can also include people who were
        self-employed but are now out of work, and some homemakers returning to the workforce. If your job
        ended, mention it.</p>
        <h3>3. Youth (16&ndash;24)</h3>
        <p>There are separate WIOA services for young people, especially those who are out of school, out of
        work, or facing challenges. If this is you or your child, ask about youth programs specifically.</p>

        <h2>The basic requirements most centers share</h2>
        <p>The rules vary by center, but most ask that you:</p>
        <ul>
          <li>Are 18 or older (for Adult and Dislocated Worker funds).</li>
          <li>Live in, or have worked in, that center's service area.</li>
          <li>Are legally authorized to work in the United States.</li>
          <li>If you are a man born after January 1, 1960, are registered with Selective Service.</li>
        </ul>
        <p><strong>Veterans and their eligible spouses get priority of service</strong> in these programs, so
        be sure to say so if it applies to you.</p>

        <h2>Priority of service: who gets served first</h2>
        <p>Funding is limited, so the law tells career centers who to help first. For Adult funds, priority
        goes to people who receive public assistance, other people with low incomes, and people who need to
        build basic reading or math skills. Veterans and their eligible spouses come first of all. This does
        not mean everyone else is turned away — it means these groups move to the front of the line.</p>

        <h2>Training has to point to a real job</h2>
        <p>Career centers fund training that leads to work that is actually hiring in Massachusetts, like health
        care, IT, and the skilled trades. Short programs that end in a recognized credential are usually the
        easiest to get approved. Come ready to explain how your training leads to a job.</p>

        <h2>What the career center will look at</h2>
        <ul>
          <li><strong>Your work authorization.</strong> You generally need to be legally allowed to work in the
          U.S.</li>
          <li><strong>Your income and household size.</strong> Lower income can raise your priority.</li>
          <li><strong>Your work history.</strong> Recent layoff? That matters for the dislocated-worker path.</li>
          <li><strong>Your goal.</strong> Training should point toward an in-demand job. Short, job-focused
          fields — like <a href="blog/can-medical-billing-coding-be-learned-online.html">medical billing and
          coding</a> or <a href="blog/can-you-learn-it-support-online.html">IT support</a> — fit this well.</li>
          <li><strong>Funding available.</strong> Budgets are limited and can run low late in the year, so
          earlier is better.</li>
        </ul>

        <p>None of these is a simple yes/no test. The career center weighs them together. That is why we say
        "you may qualify" — never that you are guaranteed.</p>

        <h2>What about income limits?</h2>
        <p>There is no single income cutoff. Lower income can raise your priority, especially for Adult funds.
        As an example, one region (MassHire Central) listed 2026 "economic disadvantage" limits ranging from
        about <strong>$15,960</strong> for a single person to <strong>$60,124 or more</strong> for a larger
        family. Every region sets its own table, so treat this as an example only, and ask your center for the
        current numbers where you live.</p>

        <h2>You might qualify even if&hellip;</h2>
        <ul>
          <li>You are working — but part-time or at low wages.</li>
          <li>You receive SNAP, TAFDC, or other public assistance.</li>
          <li>You were laid off a while ago, not just last week. (The timing rules vary, so ask.)</li>
          <li>You have never used a career center before.</li>
        </ul>
        <p>The worst thing that happens when you ask is a "not right now" — and even then, they can point you
        to other help.</p>

        <h2>What to bring when you ask</h2>
        <ol>
          <li>Photo ID and proof you can work in the U.S.</li>
          <li>Proof of income for the last few months (pay stubs, benefit letters).</li>
          <li>Proof of your family size.</li>
          <li>If you are a man born after January 1, 1960, your Selective Service registration.</li>
          <li>Any layoff or separation paperwork.</li>
          <li>A rough idea of the career you want to train for.</li>
        </ol>

        <h2>A quick self-check</h2>
        <p>Answer yes or no:</p>
        <ol>
          <li>Do you live in Massachusetts and are you allowed to work in the U.S.?</li>
          <li>Were you laid off, or are you out of work?</li>
          <li>Are you working but earning low wages?</li>
          <li>Do you receive SNAP, TAFDC, or other public assistance?</li>
          <li>Do you want to train for a specific in-demand job?</li>
        </ol>
        <p>If you answered yes to <strong>two or more</strong>, it is worth asking your career center. Not sure
        what to do first? Read our step-by-step guide to
        <a href="blog/masshire-training-voucher.html">getting a MassHire training voucher (ITA)</a>.</p>

        <h2>Not sure if it is worth asking?</h2>
        <p>It is. Walking into a MassHire career center and asking costs nothing. Even if WIOA is not a fit,
        they can point you to other help. And if funding is not available right now, you still have options —
        see <a href="student-financing.html">Ways to Pay</a>.</p>

        <h2>Frequently asked questions</h2>
        <div class="faq">
          <details class="faq-item"><summary>Do I have to be on unemployment to qualify?</summary>
          <div><p>No. WIOA serves adults, dislocated workers, and youth. You can be working — but at low wages —
          and still ask. Being on unemployment is not required.</p></div></details>
          <details class="faq-item"><summary>Is there an income limit?</summary>
          <div><p>There is no single cutoff. Lower income can raise your priority, especially for Adult funds,
          and each region publishes its own guidelines. Ask your career center for the numbers where you live.</p></div></details>
          <details class="faq-item"><summary>Can I qualify if I am not a U.S. citizen?</summary>
          <div><p>You do not have to be a citizen, but you generally must be authorized to work in the United
          States, and the center will ask for proof. Ask about your specific situation.</p></div></details>
          <details class="faq-item"><summary>Who makes the final decision?</summary>
          <div><p>Your local MassHire career center. No school, including us, can decide your eligibility or
          promise you funding. Only the career center can.</p></div></details>
        </div>

""" + FUNDING_NOTE + """

""" + post_cta(
    "Think you might qualify?",
    "Take our quick check to see which WIOA group you may fit and what to do next. It never gives a yes/no "
    "verdict &mdash; only your career center can do that.",
    "Do I Qualify?", "qualify.html") + """

""" + related(
    ("Free Job Training in Massachusetts (full guide)", "blog/free-job-training-massachusetts.html"),
    ("How to Get a MassHire Training Voucher (ITA)", "blog/masshire-training-voucher.html"),
    ("Is WIOA Training Really Free?", "blog/is-wioa-training-free.html"),
)

PAGES.append(dict(
    slug="blog/wioa-eligibility-massachusetts.html", nav="blog.html",
    title="Who Qualifies for WIOA Training in Massachusetts? | Career Skills Center",
    ogtitle="Who Qualifies for WIOA Training in Massachusetts?",
    desc="WIOA training in Massachusetts serves adults, dislocated workers, and youth. Learn what your MassHire career center looks at and how to check if you may qualify.",
    extrahead=article_ld("blog/wioa-eligibility-massachusetts.html",
                         "Who Qualifies for WIOA Training in Massachusetts?",
                         "Who WIOA training serves in Massachusetts and how eligibility is decided.",
                         "2026-09-25", "2026-09-25") + "\n" + faq_ld([
        ("Do I have to be on unemployment to qualify for WIOA training?",
         "No. WIOA serves adults, dislocated workers, and youth. You can be working but at low wages and still ask. Being on unemployment is not required."),
        ("Is there an income limit for WIOA training in Massachusetts?",
         "There is no single cutoff. Lower income can raise your priority, especially for Adult funds, and each region publishes its own guidelines. Ask your career center for the numbers where you live."),
        ("Can I qualify if I am not a U.S. citizen?",
         "You do not have to be a citizen, but you generally must be authorized to work in the United States, and the center will ask for proof. Ask about your specific situation."),
        ("Who makes the final decision on WIOA eligibility?",
         "Your local MassHire career center. No school can decide your eligibility or promise you funding — only the career center can."),
    ]),
    main=article(
        "Paying for Training",
        "Who Qualifies for WIOA Training in Massachusetts?",
        "The three groups WIOA serves, what your career center looks at, and how to check if you may qualify.",
        "September 25, 2026", "9 min read", _p2_body)))


# ---- 3. How to Get a MassHire Training Voucher (ITA) ----------------------
_p3_body = """        <!-- DRAFT – verified against docs/VERIFICATION_LOG.md (9/25/2026): the ITA step flow — MyMassGov +
             JobQuest, Training Information Meeting (or required video), TABE, career plan, documents, ETPL
             program, ITA/training proposal, approval; ~6–8 weeks (B8). "Don't start before approval" softened
             (B9). Keep the CSC "working toward listing" disclosure; do not list CSC as searchable in JobQuest. -->
        <p class="lead">A MassHire training voucher — officially an <strong>Individual Training Account
        (ITA)</strong> — is money the state can put toward tuition at an approved school. Getting one is a
        step-by-step process at your local career center. Here is the whole path, start to finish.</p>

        <p>Every MassHire center runs things a little differently, so treat this as the general map, not the
        exact turn-by-turn. When in doubt, ask your career-center advisor. Plan on the whole process taking
        <strong>about 6 to 8 weeks</strong>.</p>

        <h2>First, what is an ITA?</h2>
        <p>An Individual Training Account, or ITA, is not a check that lands in your bank account. It is an
        approval from your career center that says the state will pay an approved school directly for your
        training, up to a set amount. You pick the program (from an approved list), the center approves it, and
        the money goes to the school. Your job is to qualify, choose well, and finish. Now, the steps.</p>

        <h2>Step 1: Register in MassHire JobQuest</h2>
        <p>Start online. Create a <strong>MyMassGov</strong> account and register in
        <strong>MassHire JobQuest</strong> at <a href="https://jobquest.mass.gov">jobquest.mass.gov</a>. This is
        the state's job and training system, and your career center will expect you to be in it. Save your
        Jobseeker ID somewhere safe — you will use it again.</p>

        <h2>Step 2: Find your MassHire career center</h2>
        <p>Your center is based on where you live or last worked. Find it at
        <a href="https://www.mass.gov/info-details/masshire-career-center-locations">mass.gov (MassHire career
        center locations)</a>. Call or visit and say: "I want to train for a new career, and I want to see what
        funding I qualify for."</p>

        <h2>Step 3: Attend the Training Information Meeting</h2>
        <p>Most centers ask you to attend a short <strong>Training Information Meeting</strong> before they will
        talk about funding. Some hold it in person; others (like Downtown Boston) ask you to watch a training-
        grants video and fill out a screening form first. This is where you learn how the local process works.</p>

        <h2>Step 4: Take the TABE assessment (if asked)</h2>
        <p>Many centers ask you to take the <strong>TABE</strong>, a short reading and math assessment. It is
        not a pass/fail test — it helps the center confirm the training is a good fit and meets any basic-skills
        requirements. Ask ahead of time whether yours requires it.</p>

        <h2>Step 5: Meet a career counselor and make a plan</h2>
        <p>You will sit down with a counselor to talk through your work history, your goals, and which jobs are
        hiring. Together you build a simple career plan. Some centers ask you to sign an engagement letter that
        spells out what you both agree to do.</p>

        <h2>Step 6: Gather your documents</h2>
        <p>Bring proof you can work in the U.S., proof of age, your income for the last few months, proof of
        family size, Selective Service registration (for men born after January 1, 1960), and any layoff
        paperwork. Our guide to <a href="blog/wioa-eligibility-massachusetts.html">who qualifies for WIOA</a>
        has the full checklist.</p>

        <h2>Step 7: Choose an approved program</h2>
        <p>Here is a key rule: the training you pick usually has to be on the state's approved list, the
        <strong>Eligible Training Provider List (ETPL)</strong>. You can search approved programs inside
        JobQuest, under "Locate Training." Look for short, job-focused options that lead to a recognized
        credential — for example <a href="blog/can-you-learn-it-support-online.html">IT support</a> or
        <a href="blog/can-medical-billing-coding-be-learned-online.html">medical billing and coding</a>. Bring
        the school's program details, cost, and schedule to your counselor.</p>
        <div class="note"><strong>Note:</strong> Career Skills Center is working toward being listed as an
        approved provider, so we are not yet searchable in JobQuest. If a program you want is not on the list,
        ask your counselor about approved alternatives, and <a href="contact.html">join our interest list</a> —
        we will update our status as it changes.</div>

        <h2>Step 8: Submit the ITA (training proposal)</h2>
        <p>With a program chosen, your counselor helps you submit the ITA, sometimes called a training proposal.
        The center reviews it based on three things: whether you are eligible, whether the training leads to a
        job that is in demand, and whether funding is available. If everything lines up, they approve it and set
        the amount, up to their limit.</p>

        <h2>Step 9: Wait for written approval, then start</h2>
        <p>This is the one step people get wrong. <strong>Don't start class until your career center approves
        your training in writing.</strong> Ask them first. Training that begins before approval usually cannot be
        paid for. Once you have the approval, you enroll and begin. For the honest picture on what the money
        covers, read <a href="blog/is-wioa-training-free.html">is WIOA training really free?</a></p>

        <div class="post-cta" style="background:var(--surface-alt); color:var(--ink);">
          <h2 style="color:var(--navy);">On unemployment? Ask about Section 30</h2>
          <p style="color:var(--ink-light);">If you are collecting unemployment, ask about Section 30 at the same
          time. It can let you keep your benefits while you train full-time. See the
          <a href="blog/free-job-training-massachusetts.html">full funding guide</a> for how it works.</p>
        </div>

        <h2>Common mistakes to avoid</h2>
        <ul>
          <li><strong>Starting class before approval.</strong> The most common and costly mistake. Wait for the
          written OK.</li>
          <li><strong>Skipping the information meeting.</strong> Many centers will not move forward until you
          have attended it.</li>
          <li><strong>Picking a program that is not on the ETPL.</strong> If it is not approved, the voucher
          cannot pay for it.</li>
          <li><strong>Waiting until late in the year.</strong> Funds can run out, so start while money is
          available.</li>
          <li><strong>Showing up without documents.</strong> Missing paperwork slows everything down.</li>
        </ul>

        <h2>Tips to keep things moving</h2>
        <ul>
          <li><strong>Start early.</strong> Funding is limited and can run low later in the program year.</li>
          <li><strong>Keep copies</strong> of everything you submit.</li>
          <li><strong>Be ready to explain</strong> how the training leads to a job — that is what approval turns
          on.</li>
          <li><strong>Ask about support services</strong> (like help with transportation or childcare) if you
          need them.</li>
        </ul>

        <h2>After you're approved</h2>
        <p>Once your training is approved, the center works with the school to set up payment, and you enroll and
        start. Keep in touch with your counselor while you are in class — they may check on your progress, and
        they are the person to call if your schedule or plans change. Finishing the program is part of the deal,
        so treat attendance and completion as seriously as the funding.</p>

        <h2>The bottom line</h2>
        <p>Getting a MassHire voucher takes a few weeks and some paperwork, but the payoff — training paid for
        and pointed at a real job — is worth it. Register in JobQuest, call your career center, and start the
        clock early.</p>

""" + FUNDING_NOTE + """

""" + post_cta(
    "Getting ready to apply?",
    "See the full WIOA process from start to finish, then check what you may qualify for.",
    "How WIOA works", "wioa-explained.html") + """

        <h2>Frequently asked questions</h2>
        <div class="faq">
          <details class="faq-item"><summary>How long does the whole process take?</summary>
          <div><p>Plan on about 6 to 8 weeks from your first visit to your first class, though it varies by
          center and by how quickly you finish each step. Start early, because funds can run low later in the
          year.</p></div></details>
          <details class="faq-item"><summary>Can I choose any school?</summary>
          <div><p>No. To use the voucher, the program must be on the state's approved list (the ETPL). You can
          search approved programs in JobQuest under "Locate Training."</p></div></details>
          <details class="faq-item"><summary>Do I have to pay anything up front?</summary>
          <div><p>Usually the ITA pays the approved school directly, up to its limit, so you are not fronting
          tuition. If the program costs more than the cap, you cover the difference. Ask exactly what yours
          covers.</p></div></details>
          <details class="faq-item"><summary>What if I already started a class?</summary>
          <div><p>Training that begins before your center approves it usually cannot be paid for. If you are
          already enrolled, talk to a counselor right away rather than assuming it will be covered.</p></div></details>
        </div>

""" + related(
    ("Who Qualifies for WIOA Training in Massachusetts?", "blog/wioa-eligibility-massachusetts.html"),
    ("Free Job Training in Massachusetts (full guide)", "blog/free-job-training-massachusetts.html"),
    ("Is WIOA Training Really Free?", "blog/is-wioa-training-free.html"),
)

PAGES.append(dict(
    slug="blog/masshire-training-voucher.html", nav="blog.html",
    title="How to Get a MassHire Training Voucher (ITA): Step by Step | Career Skills Center",
    ogtitle="How to Get a MassHire Training Voucher (ITA): Step by Step",
    desc="A step-by-step guide to getting an Individual Training Account (ITA) voucher from a MassHire career center in Massachusetts, from your first visit to enrollment.",
    extrahead=article_ld("blog/masshire-training-voucher.html",
                         "How to Get a MassHire Training Voucher (ITA): Step by Step",
                         "Step-by-step guide to getting an ITA training voucher from a MassHire career center.",
                         "2026-09-25", "2026-09-25") + "\n" + faq_ld([
        ("How long does it take to get a MassHire training voucher?",
         "Plan on about 6 to 8 weeks from your first visit to your first class, though it varies by center and by how quickly you finish each step. Start early, because funds can run low later in the year."),
        ("Can I choose any school with a MassHire voucher?",
         "No. To use the voucher, the program must be on the state's approved list (the ETPL). You can search approved programs in JobQuest under Locate Training."),
        ("Do I have to pay anything up front?",
         "Usually the ITA pays the approved school directly, up to its limit, so you are not fronting tuition. If the program costs more than the cap, you cover the difference. Ask exactly what yours covers."),
        ("What if I already started a class?",
         "Training that begins before your center approves it usually cannot be paid for. If you are already enrolled, talk to a counselor right away rather than assuming it will be covered."),
    ]),
    main=article(
        "Paying for Training",
        "How to Get a MassHire Training Voucher (ITA): Step by Step",
        "The Individual Training Account process at a MassHire career center, from first visit to enrollment.",
        "September 25, 2026", "9 min read", _p3_body)))


# ---- 4. Is WIOA Training Really Free --------------------------------------
_p4_body = """        <!-- DRAFT – verified against docs/VERIFICATION_LOG.md (9/25/2026): ITA-covers wording softened (B10),
             supportive-services wording softened (B11), Section 30 income facts (B2). Do NOT state dollar caps. -->
        <p class="lead">Mostly, yes — but not always 100%. WIOA funding, given out as an Individual Training
        Account (ITA) through MassHire, can cover tuition for an approved program and sometimes more. But there
        are limits, and a few costs may still land on you. Here is the honest breakdown.</p>

        <h2>What WIOA usually covers</h2>
        <p>An ITA pays for approved training. Some career centers also cover related costs like books or exam
        fees, but this varies. Always ask your counselor exactly what yours covers &mdash; in writing:
        "What exactly does my ITA pay for?"</p>
        <p>Here is the rough shape of it, without the dollar amounts (those vary by region): the center sets a
        cap, your program has a price, and the ITA covers the price up to that cap. If your program costs less
        than the cap, it can be fully covered. If it costs more, you cover the difference or choose a program
        that fits. That is why picking an approved program within the cap matters so much.</p>

        <h2>What it may not cover</h2>
        <ul>
          <li><strong>Costs above the award cap.</strong> ITAs have a limit. If a program costs more, you may
          need to cover the difference or pick a program within the cap.</li>
          <li><strong>Some supplies or optional add-ons</strong>, like an extra certification exam you choose to
          take.</li>
          <li><strong>Everyday costs</strong> like gas, parking, or childcare. Some career centers can help with
          these through support services, depending on local funding &mdash; ask your counselor.</li>
        </ul>

        <h2>Why "free" is the wrong word to plan around</h2>
        <p>WIOA is real, valuable help, and for many people it covers the biggest cost: tuition. But treating it
        as "totally free, no matter what" can lead to surprises. Plan for the possibility of small out-of-pocket
        costs, and you will not be caught off guard.</p>

        <h2>What if I still need income while I train?</h2>
        <p>This is the real blocker for most people: the bills do not stop while you study. If you are collecting
        unemployment, <strong>Section 30</strong> (the Training Opportunities Program) can let you keep your
        benefits during full-time approved training — at least 20 classroom hours a week, for up to 26 extra
        weeks. You usually have to apply by the 20th paid week of your claim, so ask early. Section 30 does not
        pay tuition, but keeping your income coming is often what makes finishing possible.</p>

        <div class="note"><strong>"Free to you" vs. "free with conditions."</strong> WIOA can make training free
        to you out of pocket — but not with no strings. You have to be eligible, keep attending, and finish, and
        many centers follow up on whether you land a job afterward. Think of it as an investment the state makes
        in you, not a no-questions handout.</div>

        <h2>How to get the most out of your funding</h2>
        <ol>
          <li>Choose a program that fits within the award cap when possible.</li>
          <li>Ask what is covered and what is not — in writing.</li>
          <li>Ask about support services for transportation or childcare.</li>
          <li>Pick a short, job-focused program so more of your funding goes to what matters.
          <a href="contact.html">Join our interest list</a> to hear about ours.</li>
        </ol>

        <h2>Does everyone who qualifies get funded?</h2>
        <p>Not automatically. Being eligible and getting funded are two different things. Career centers work
        within a yearly budget, and popular programs and busy times of year can use it up. That is why advisors
        push you to apply early and to have a backup plan. Qualifying puts you in line; it does not guarantee a
        check.</p>

        <h2>Beyond tuition: help you might not expect</h2>
        <p>Money for tuition is not the only support a career center can offer. Depending on local funding, some
        can help with transportation, childcare, or work clothes and tools, and all of them offer free help with
        resumes, interviews, and the job search after you finish. When you ask about training funds, ask what
        else is available &mdash; it is often more than people expect.</p>

        <h2>If WIOA doesn't cover you</h2>
        <p>If your award falls short, or you do not qualify right now, you still have options:</p>
        <ul>
          <li><strong>Donnelly-funded programs.</strong> Some free training is paid for by state Donnelly
          grants. You look for a local program funded by one, not an application. See the
          <a href="blog/free-job-training-massachusetts.html">funding guide</a>.</li>
          <li><strong>Employer-paid training.</strong> If you have a job, your employer may be reimbursed
          through the Workforce Training Fund Express Program.</li>
          <li><strong>Payment plans.</strong> A monthly plan can spread the cost out. See
          <a href="student-financing.html">Ways to Pay</a>.</li>
        </ul>
        <p>Most people combine more than one. Cost does not have to be the thing that stops you.</p>

        <h2>The honest bottom line</h2>
        <p>For many people in Massachusetts, WIOA covers the biggest cost of training — tuition — and that is a
        real head start. Just go in with clear eyes: ask what is covered, plan for small extras, and line up a
        backup like a payment plan. That way, whatever the answer turns out to be, cost is not the thing that
        stops you from starting.</p>

        <h2>Frequently asked questions</h2>
        <div class="faq">
          <details class="faq-item"><summary>Does WIOA pay for books and exams?</summary>
          <div><p>Sometimes. An ITA pays for approved training, and some career centers also cover related costs
          like books or exam fees, but this varies by center. Ask your counselor exactly what yours covers.</p></div></details>
          <details class="faq-item"><summary>Will I have any out-of-pocket costs?</summary>
          <div><p>Maybe small ones. Awards have a limit, so a program that costs more than the cap, or optional
          add-ons, could leave a gap. Everyday costs like gas or childcare may be helped by support services —
          ask.</p></div></details>
          <details class="faq-item"><summary>Can I get paid while I train?</summary>
          <div><p>If you are on unemployment, Section 30 can keep your benefits going during full-time approved
          training (at least 20 classroom hours a week, up to 26 extra weeks). Apply by the 20th paid week of
          your claim.</p></div></details>
          <details class="faq-item"><summary>What if the funds run out?</summary>
          <div><p>It happens, because funding is limited each year. Ask about the next program year, look for a
          Donnelly-funded free program, or use a payment plan to start now.</p></div></details>
        </div>

""" + FUNDING_NOTE + """

""" + post_cta(
    "Worried about the gap?",
    "See how WIOA and Section 30 can fit together, then check what you may qualify for so cost isn&rsquo;t the "
    "thing that stops you.",
    "Do I Qualify?", "qualify.html") + """

""" + related(
    ("Free Job Training in Massachusetts (full guide)", "blog/free-job-training-massachusetts.html"),
    ("Who Qualifies for WIOA Training in Massachusetts?", "blog/wioa-eligibility-massachusetts.html"),
    ("How to Get a MassHire Training Voucher (ITA)", "blog/masshire-training-voucher.html"),
)

PAGES.append(dict(
    slug="blog/is-wioa-training-free.html", nav="blog.html",
    title="Is WIOA Training Really Free? What's Covered and What Isn't | Career Skills Center",
    ogtitle="Is WIOA Training Really Free? What's Covered and What Isn't",
    desc="WIOA can cover tuition and some costs for approved training in Massachusetts, but not always everything. An honest look at what a grant pays for and what you may still owe.",
    extrahead=article_ld("blog/is-wioa-training-free.html",
                         "Is WIOA Training Really Free? What's Covered and What Isn't",
                         "An honest look at what WIOA funding covers and what it may not.",
                         "2026-09-25", "2026-09-25") + "\n" + faq_ld([
        ("Does WIOA pay for books and exams?",
         "Sometimes. An ITA pays for approved training, and some career centers also cover related costs like books or exam fees, but this varies by center. Ask your counselor exactly what yours covers."),
        ("Will I have any out-of-pocket costs with WIOA training?",
         "Maybe small ones. Awards have a limit, so a program that costs more than the cap, or optional add-ons, could leave a gap. Everyday costs like gas or childcare may be helped by support services — ask."),
        ("Can I get paid while I train?",
         "If you are on unemployment, Section 30 can keep your benefits going during full-time approved training (at least 20 classroom hours a week, up to 26 extra weeks). Apply by the 20th paid week of your claim."),
        ("What if the WIOA funds run out?",
         "It happens, because funding is limited each year. Ask about the next program year, look for a Donnelly-funded free program, or use a payment plan to start now."),
    ]),
    main=article(
        "Paying for Training",
        "Is WIOA Training Really Free? What's Covered and What Isn't",
        "An honest look at what a WIOA grant usually pays for, where the limits are, and how to plan.",
        "September 25, 2026", "8 min read", _p4_body)))


# ---- 5. Highest-Paying Certifications in Massachusetts --------------------
_p5_body = """        <!-- DRAFT – verified against docs/VERIFICATION_LOG.md (9/25/2026): all wages are BLS OEWS May 2025
             Massachusetts medians (section C/G1). IT outlook is "steady demand," not "fast-growing" (C).
             No CSC program details — links go to the blog, not program pages (F1). Title year set to (2026). -->
        <p class="lead">You do not always need a four-year degree to earn a good living in Massachusetts. Some
        of the best returns come from short certificate programs that lead to a recognized credential. Here are
        fields worth a look, with real Massachusetts pay from the government's own wage data.</p>

        <div class="note"><strong>About the pay:</strong> the figures below are Massachusetts median annual
        wages from the U.S. Bureau of Labor Statistics (OEWS, May 2025). "Median" means half of workers earn
        more and half earn less. Your pay depends on experience, employer, and location.</div>

        <div class="table-wrap">
          <table class="data-table">
            <thead><tr><th>Job</th><th>Massachusetts median pay</th></tr></thead>
            <tbody>
              <tr><td>Medical records specialists (billing &amp; coding)</td><td>$60,350</td></tr>
              <tr><td>Billing and posting clerks</td><td>$56,110</td></tr>
              <tr><td>Medical secretaries &amp; administrative assistants</td><td>$50,290</td></tr>
              <tr><td>Computer user support specialists (IT help desk)</td><td>$75,070</td></tr>
              <tr><td>Computer network support specialists</td><td>$88,650</td></tr>
              <tr><td>Electricians</td><td>$79,420</td></tr>
              <tr><td>Plumbers, pipefitters &amp; steamfitters</td><td>$93,880</td></tr>
              <tr><td>HVAC &amp; refrigeration mechanics</td><td>$77,300</td></tr>
            </tbody>
          </table>
        </div>
        <p><em>Source: U.S. Bureau of Labor Statistics, OEWS, May 2025, Massachusetts.</em></p>

        <h2>How to judge a certification (before the pay)</h2>
        <p>A credential is worth more when: employers actually ask for it, it is recognized nationally, and it
        leads to jobs that are hiring near you. Pay matters, but so does whether you can get hired. Keep both in
        mind as you read.</p>

        <h2>Healthcare (non-clinical): Medical Billing &amp; Coding</h2>
        <p>Medical billing and coding is the paperwork engine behind healthcare — turning visits into correct
        codes and claims. It is office-based and can be learned online. In Massachusetts, medical records
        specialists earn a median of about <strong>$60,350</strong> a year (BLS, May 2025). The field's
        best-known credentials are the AAPC's CPC (Certified Professional Coder) and CPB (Certified Professional
        Biller).</p>
        <p>Read more: <a href="blog/can-medical-billing-coding-be-learned-online.html">Can medical billing and
        coding be learned online?</a></p>

        <h2>Information Technology: IT Support</h2>
        <p>IT support is a common first step into a tech career, and employers hire on skills and certifications,
        not only degrees. In Massachusetts, computer user support specialists earn a median of about
        <strong>$75,070</strong> a year (BLS, May 2025). A well-known starting credential is CompTIA (for
        example, the Tech+ level). One honest note: nationally, help-desk jobs are projected to hold steady
        rather than grow fast, but there are still thousands of openings each year as people move up or retire.</p>
        <p>Read more: <a href="blog/can-you-learn-it-support-online.html">Can you learn IT support online?</a></p>

        <h2>Skilled Trades: Electrical, HVAC/R, Plumbing and more</h2>
        <p>Licensed trades pay very well in Massachusetts, and the work cannot be shipped overseas. Electricians
        earn a median of about <strong>$79,420</strong>, HVAC and refrigeration mechanics about
        <strong>$77,300</strong>, and plumbers, pipefitters and steamfitters about <strong>$93,880</strong> a
        year (BLS, May 2025). The trade-off: trades are hands-on and require in-person hours, an apprenticeship,
        and a state license.</p>
        <p>Read more: <a href="blog/can-you-learn-a-trade-online.html">Can you learn a trade online?</a></p>

        <h2>How to check the pay for yourself</h2>
        <ol>
          <li>Open the BLS wage data for Massachusetts:
          <a href="https://data.bls.gov/oes/#/area/2500000/2025">data.bls.gov (Massachusetts, May 2025)</a>.</li>
          <li>Find the job title (for example, "computer user support specialists").</li>
          <li>Look at the "Annual median wage" column.</li>
          <li>Cross-check current job postings near you to see what employers are really offering.</li>
        </ol>

        <h2>The bottom line</h2>
        <p>The "highest-paying" certificate is the one that fits a job that is hiring near you, that you can
        finish, and that you can pay for. Start with a field that interests you, check the local pay, and check
        how to fund it.</p>

""" + FUNDING_NOTE + """

""" + post_cta(
    "Not sure which field fits?",
    "Compare healthcare, IT and the skilled trades &mdash; what each involves, how to train, and what the work "
    "is really like.",
    "Explore career paths", "career-paths.html") + """

""" + related(
    ("Can Medical Billing and Coding Be Learned Online?", "blog/can-medical-billing-coding-be-learned-online.html"),
    ("Can You Learn IT Support Online?", "blog/can-you-learn-it-support-online.html"),
    ("Free Job Training in Massachusetts (full guide)", "blog/free-job-training-massachusetts.html"),
)

PAGES.append(dict(
    slug="blog/highest-paying-certifications-massachusetts.html", nav="blog.html",
    title="Highest-Paying Certifications You Can Train For in Massachusetts (2026) | Career Skills Center",
    ogtitle="Highest-Paying Certifications You Can Train For in Massachusetts (2026)",
    desc="Short certificate programs can lead to good pay in Massachusetts healthcare, IT, and the trades. The credentials worth considering and how to check real local wages.",
    extrahead='  <meta name="robots" content="noindex">\n' + article_ld("blog/highest-paying-certifications-massachusetts.html",
                         "Highest-Paying Certifications You Can Train For in Massachusetts (2026)",
                         "Certificate programs with strong pay in Massachusetts and how to verify local wages.",
                         "2026-09-25", "2026-09-25"),
    main=article(
        "Paying for Training",
        "Highest-Paying Certifications You Can Train For in Massachusetts (2026)",
        "Short credentials with strong earning potential in healthcare, IT, and the trades — and how to check "
        "the real local pay yourself.",
        "September 25, 2026", "8 min read", _p5_body)))


# ---- 6. Can Medical Billing and Coding Be Learned Online -----------------
_p6_body = """        <!-- DRAFT – verified against docs/VERIFICATION_LOG.md (9/25/2026): AAPC CPC/CPB confirmed (B15); exam
             cost $425/$499 and testing options softened (B15/B16). No CSC program details per policy F1 —
             only "planning a program, join the interest list." -->
        <p class="lead">Yes — medical billing and coding is one of the best healthcare fields to learn online.
        The work itself is done on a computer, so training on a computer makes sense. What matters most is that
        you learn the codes well and earn a credential employers recognize.</p>

        <p>If you like detail, organization, and steady office work, this is a field worth a serious look. Here
        is how online learning works for it, and what to aim for.</p>

        <h2>Why this field fits online learning</h2>
        <p>Medical coders and billers translate doctor visits into standard codes, then prepare and follow up on
        insurance claims. It is screen-and-software work. So the skills you build in an online course — reading
        records, applying code sets, using billing software — are the same skills you use on the job.</p>

        <h2>Coding vs. billing: what's the difference?</h2>
        <p>People say "billing and coding" as one phrase, but they are two jobs that often overlap. A
        <strong>coder</strong> translates the visit into standard codes. A <strong>biller</strong> uses those
        codes to prepare claims, send them to insurers, and chase down payment. Small offices often have one
        person do both; larger ones split the roles. Training that covers both keeps your options open.</p>

        <h2>What the day-to-day looks like</h2>
        <p>A biller or coder spends the day reading clinical notes, assigning the right codes, preparing claims,
        and following up on the ones that get denied. It is quiet, focused, detail-heavy work — often in an
        office, a clinic's back room, or from home. If you like solving small puzzles and getting the details
        exactly right, the work tends to be satisfying rather than boring.</p>

        <h2>What good training covers</h2>
        <ul>
          <li><strong>Medical terminology and anatomy</strong> — enough to understand records.</li>
          <li><strong>Code sets</strong> — ICD-10-CM (diagnoses), CPT (procedures), and HCPCS.</li>
          <li><strong>The claims process</strong> — from a visit to a paid claim, including denials and
          appeals.</li>
          <li><strong>Compliance basics</strong> — rules like HIPAA that protect patient information.</li>
          <li><strong>Exam prep</strong> — practice for a recognized credential.</li>
        </ul>

        <h2>The credential is the goal</h2>
        <p>Employers want proof you can do the work. The best-known credentials come from the AAPC: the
        <strong>CPC</strong> (Certified Professional Coder) and <strong>CPB</strong> (Certified Professional
        Biller). Passing one of these tells an employer you are ready.</p>
        <p>Career Skills Center is planning a Medical Billing &amp; Coding program. <a href="contact.html">Join
        our interest list</a> to hear first when details are ready.</p>
        <p>Good to know: the AAPC exam is taken after training and, as of 2026, costs about <strong>$425</strong>
        for one attempt (or $499 for two). Check <a href="https://www.aapc.com/">AAPC</a> for current pricing
        and testing options (online or in person).</p>

        <h2>What you need to succeed online</h2>
        <ul>
          <li>A computer and steady internet.</li>
          <li>Discipline to keep a study schedule (online means flexible, not effortless).</li>
          <li>Attention to detail — a wrong code means a rejected claim.</li>
          <li>Patience for practice; coding gets easier with reps.</li>
        </ul>

        <h2>Is it right for you?</h2>
        <p>If you want a healthcare career without hands-on patient care, prefer office work, and are careful
        with details, medical billing and coding is a strong fit. It is also friendly to people changing careers
        or returning to work.</p>

        <h2>Is online training respected by employers?</h2>
        <p>Yes. In this field, employers hire on the credential and what you can do, not on where you studied. A
        recognized certification like the AAPC's CPC or CPB carries the same weight whether you earned it online
        or in a classroom. What matters is that you can code accurately and understand the claims process.</p>

        <h2>Can you work from home as a coder?</h2>
        <p>Often, yes — but be realistic about the timeline. Many billing and coding jobs are remote or hybrid,
        which is part of the appeal. That said, plenty of employers want new coders to start on-site, or to have
        a year or two of experience, before they go fully remote. A good first move is any coding role that gets
        you real reps; remote options open up as you build a track record.</p>

        <h2>Who does well learning it online</h2>
        <p>You do not need a science background, but you do need to be self-directed. If you can keep a study
        schedule, you are comfortable using a computer, and you like detailed, rule-based work, you are a good
        fit. English-language learners can do well too — the vocabulary is specific and learnable, and you can
        review lessons at your own pace. The learners who struggle are usually the ones who treat "online" as
        "no schedule"; the ones who succeed set aside regular study time and stick to it.</p>

        <h2>What it pays, and how to pay for it</h2>
        <p>In Massachusetts, medical records specialists earn a median of about <strong>$60,350</strong> a year
        (BLS, May 2025). For the full picture across healthcare, IT, and the trades, see our
        <a href="blog/highest-paying-certifications-massachusetts.html">highest-paying certifications</a> guide.
        And if cost is a concern, state funding may help — start with our
        <a href="blog/free-job-training-massachusetts.html">guide to free job training in Massachusetts</a>.</p>

""" + FUNDING_NOTE + """

""" + post_cta(
    "Interested in medical billing and coding?",
    "Explore healthcare careers &mdash; what the roles involve, how to train, and the certifications employers "
    "look for. <!-- COURSE-DEPENDENT: R-BLOG --> Career Skills Center plans to offer training in the medical "
    "field; get updates when we launch.",
    "Explore healthcare careers", "healthcare-careers.html") + """

        <h2>Frequently asked questions</h2>
        <div class="faq">
          <details class="faq-item"><summary>Can medical billing and coding really be learned online?</summary>
          <div><p>Yes. The work is done on a computer, so online training maps directly to the job. What matters
          is learning the code sets well and earning a recognized credential.</p></div></details>
          <details class="faq-item"><summary>Do I need a medical background?</summary>
          <div><p>No. Good training starts with the medical terminology and anatomy you need. You need attention
          to detail and the discipline to practice, not a science degree.</p></div></details>
          <details class="faq-item"><summary>What certification should I aim for?</summary>
          <div><p>The best-known are the AAPC's CPC (coder) and CPB (biller). Employers recognize them
          nationally. The exam is taken after training and, as of 2026, costs about $425 for one attempt.</p></div></details>
          <details class="faq-item"><summary>Can I work from home as a coder?</summary>
          <div><p>Many jobs are remote or hybrid, but new coders often start on-site or need a year or two of
          experience first. Remote options open up as you build a track record.</p></div></details>
          <details class="faq-item"><summary>How long does training take?</summary>
          <div><p>It varies by program and your pace. Focused certificate programs commonly run a few months.
          Details for our program will be shared before enrollment opens.</p></div></details>
        </div>

""" + related(
    ("WIOA Training Funds Explained", "wioa-explained.html"),
    ("Can You Learn IT Support Online?", "blog/can-you-learn-it-support-online.html"),
    ("Free Job Training in Massachusetts (full guide)", "blog/free-job-training-massachusetts.html"),
)

PAGES.append(dict(
    slug="blog/can-medical-billing-coding-be-learned-online.html", nav="blog.html",
    title="Can Medical Billing and Coding Be Learned Online? | Career Skills Center",
    ogtitle="Can Medical Billing and Coding Be Learned Online?",
    desc="Yes — medical billing and coding can be learned fully online. What the training covers, which credentials employers want (AAPC CPC/CPB), and what it takes to succeed.",
    extrahead=article_ld("blog/can-medical-billing-coding-be-learned-online.html",
                         "Can Medical Billing and Coding Be Learned Online?",
                         "How online medical billing and coding training works and what employers look for.",
                         "2026-09-25", "2026-09-25") + "\n" + faq_ld([
        ("Can medical billing and coding really be learned online?",
         "Yes. The work is done on a computer, so online training maps directly to the job. What matters is learning the code sets well and earning a recognized credential."),
        ("Do I need a medical background to learn medical billing and coding?",
         "No. Good training starts with the medical terminology and anatomy you need. You need attention to detail and the discipline to practice, not a science degree."),
        ("What certification should I aim for?",
         "The best-known are the AAPC's CPC (coder) and CPB (biller), recognized nationally. The exam is taken after training and, as of 2026, costs about $425 for one attempt."),
        ("Can I work from home as a medical coder?",
         "Many jobs are remote or hybrid, but new coders often start on-site or need a year or two of experience first. Remote options open up as you build a track record."),
        ("How long does medical billing and coding training take?",
         "It varies by program and your pace. Focused certificate programs commonly run a few months."),
    ]),
    main=article(
        "Medical",
        "Can Medical Billing and Coding Be Learned Online?",
        "Why this healthcare field fits online learning, what good training covers, and the credentials that "
        "matter.",
        "September 25, 2026", "8 min read", _p6_body)))


# ---- 7. Can You Learn IT Support Online ----------------------------------
_p7_body = """        <!-- DRAFT – verified against docs/VERIFICATION_LOG.md (9/25/2026): CompTIA Tech+/A+ confirmed (B13);
             employer-hiring claim softened (B14). No CSC program details per policy F1 — only "planning a
             program, join the interest list." -->
        <p class="lead">Yes, you can learn IT support online, and plenty of people break into tech this way. The
        two things that matter most are a recognized <strong>certification</strong> and real
        <strong>hands-on practice</strong>. Online training can give you both — if you put in the reps.</p>

        <p>IT support (the help desk) is the most common on-ramp to a technology career. Here is what employers
        actually look for, and how to build it from home.</p>

        <h2>What IT support work looks like</h2>
        <p>Support technicians solve everyday tech problems: setting up computers, fixing login issues,
        troubleshooting networks and printers, and helping people use software. It is part technical skill, part
        people skill. If you are the person friends call when their laptop breaks, you already have the
        instinct.</p>

        <h2>What employers actually look for</h2>
        <ul>
          <li><strong>A recognized certification.</strong> CompTIA is the common starting point — for example
          Tech+ or A+. It tells an employer you know the fundamentals.</li>
          <li><strong>Hands-on ability.</strong> Can you actually fix things? Practice matters more than
          memorizing.</li>
          <li><strong>Customer service.</strong> Ticketing systems, patience, and explaining a fix in plain
          words are half the job.</li>
          <li><strong>Everyday tech.</strong> Windows and Microsoft 365, basic networking, and a home lab or
          small project you can point to.</li>
        </ul>

        <h2>The certification ladder</h2>
        <p>CompTIA is the most common credential path for support roles, and it builds in steps:</p>
        <ul>
          <li><strong>CompTIA Tech+</strong> — the entry-level cert (it replaced ITF+). A good first proof that
          you know the fundamentals.</li>
          <li><strong>CompTIA A+</strong> — the standard help-desk credential most employers recognize.</li>
          <li><strong>Network+ and Security+</strong> — the next steps when you want to move up into networking
          or security.</li>
        </ul>
        <p>You do not need all of them to start. Many people get hired at the Tech+ or A+ level and add the
        others as they grow.</p>

        <h2>How online training builds real skill</h2>
        <p>Good online IT training is not just videos. Look for hands-on labs and simulations where you practice
        setting up systems and fixing problems. You can also build a home lab cheaply — an old computer, some
        free software, and time — to practice what you learn.</p>
        <p>Career Skills Center is planning an IT Support program. <a href="contact.html">Join our interest
        list</a> to hear first when details are ready.</p>

        <h2>Do you need a degree?</h2>
        <p>Usually not for a first support role. Many employers hire for entry-level help desk roles based on
        skills and certifications, not only degrees. A degree can help later, but it is often not the starting
        requirement.</p>

        <h2>How to stand out for that first job</h2>
        <ol>
          <li>Earn the certification employers ask for.</li>
          <li>Build a small home lab and practice, practice, practice.</li>
          <li>Learn to explain fixes simply — it shows in interviews.</li>
          <li>Apply widely for help-desk and support roles; the first job is the hardest to get.</li>
        </ol>

        <h2>How to build a home lab (for almost nothing)</h2>
        <p>The fastest way to turn study into skill is to practice on real gear. You do not need much: an old
        laptop or desktop, free operating systems and virtual-machine software, and time. Set things up and
        break them on purpose, then fix them. Reinstall Windows. Build a small network. Try free virtual labs and
        practice tickets. When an interviewer asks "have you actually done this?", a home lab is your answer.</p>

        <h2>Where the jobs are in Massachusetts</h2>
        <p>Demand is strong across the state. Hospitals, universities, and biotech and tech companies all run
        help desks and IT support teams, and someone has to keep those systems running. Entry-level support is
        often the doorway into those organizations.</p>

        <h2>What to expect in your first job</h2>
        <p>Most people start on a help desk, answering tickets and phone calls. It can be busy, but it is where
        you learn fastest — every ticket is a small lesson. Do it well for a year, keep earning certifications,
        and doors open to networking, security, and systems roles. Very few people stay on the help desk
        forever; it is a launch pad, not a ceiling.</p>

        <h2>Will AI replace IT support?</h2>
        <p>It is a fair question. AI tools are changing the work, but people still need help when things break,
        and someone has to set up, secure, and troubleshoot the systems AI runs on. The honest picture:
        help-desk roles are expected to hold steady rather than boom, and the people who do best keep learning.
        Treat your first support job as a starting point, not the finish line.</p>

        <h2>What it pays, and how to pay for it</h2>
        <p>In Massachusetts, computer user support specialists earn a median of about <strong>$75,070</strong> a
        year (BLS, May 2025). One honest note: nationally, help-desk roles are expected to hold steady rather
        than grow fast, but there are still thousands of openings each year as people move up or retire. For
        more, see our <a href="blog/highest-paying-certifications-massachusetts.html">highest-paying
        certifications</a> guide — and if cost is a worry, our
        <a href="blog/free-job-training-massachusetts.html">guide to free job training in Massachusetts</a>.</p>

""" + FUNDING_NOTE + """

""" + post_cta(
    "Thinking about a tech career?",
    "Explore IT careers &mdash; where you start, the certifications to aim for, and how to train online. "
    "<!-- COURSE-DEPENDENT: R-BLOG --> Career Skills Center plans to offer training in IT; get updates when we "
    "launch.",
    "Explore IT careers", "it-careers.html") + """

        <h2>Frequently asked questions</h2>
        <div class="faq">
          <details class="faq-item"><summary>Can you really learn IT support online?</summary>
          <div><p>Yes. IT support is learned and practiced on computers, and employers hire on certifications and
          demonstrated skill. Look for training with hands-on labs, and build a home lab to practice.</p></div></details>
          <details class="faq-item"><summary>Do I need a degree?</summary>
          <div><p>Usually not for a first support role. Many employers hire based on skills and certifications,
          not only degrees. A degree can help later, but it is often not the starting requirement.</p></div></details>
          <details class="faq-item"><summary>How long until I'm job-ready?</summary>
          <div><p>It varies by your pace, but a focused path — a starter certification plus real hands-on
          practice — can take a few months. The practice is what turns a cert into a job offer.</p></div></details>
          <details class="faq-item"><summary>Is CompTIA A+ hard?</summary>
          <div><p>It is challenging but very doable. It covers a lot of ground, so steady study and hands-on
          practice matter more than cramming. Many people pass it as their first real IT credential.</p></div></details>
          <details class="faq-item"><summary>Does Career Skills Center offer IT training?</summary>
          <div><p>Not yet. An IT Support program is in development. Join the interest list and we will let you
          know when it opens.</p></div></details>
        </div>

""" + related(
    ("WIOA Training Funds Explained", "wioa-explained.html"),
    ("Can Medical Billing and Coding Be Learned Online?", "blog/can-medical-billing-coding-be-learned-online.html"),
    ("Free Job Training in Massachusetts (full guide)", "blog/free-job-training-massachusetts.html"),
)

PAGES.append(dict(
    slug="blog/can-you-learn-it-support-online.html", nav="blog.html",
    title="Can You Learn IT Support Online? What Employers Actually Look For | Career Skills Center",
    ogtitle="Can You Learn IT Support Online? What Employers Actually Look For",
    desc="You can learn IT support online. What matters most is a recognized certification and hands-on practice. What employers look for and how to build both from home.",
    extrahead=article_ld("blog/can-you-learn-it-support-online.html",
                         "Can You Learn IT Support Online? What Employers Actually Look For",
                         "How to learn IT support online and what employers look for in a first support role.",
                         "2026-09-25", "2026-09-25") + "\n" + faq_ld([
        ("Can you really learn IT support online?",
         "Yes. IT support is learned and practiced on computers, and employers hire on certifications and demonstrated skill. Look for training with hands-on labs, and build a home lab to practice."),
        ("Do I need a degree for an IT support job?",
         "Usually not for a first support role. Many employers hire based on skills and certifications, not only degrees. A degree can help later, but it is often not the starting requirement."),
        ("How long until I'm job-ready for IT support?",
         "It varies by your pace, but a focused path — a starter certification plus real hands-on practice — can take a few months. The practice is what turns a cert into a job offer."),
        ("Is CompTIA A+ hard?",
         "It is challenging but very doable. It covers a lot of ground, so steady study and hands-on practice matter more than cramming. Many people pass it as their first real IT credential."),
        ("Does Career Skills Center offer IT training?",
         "Not yet. An IT Support program is in development. Join the interest list and Career Skills Center will let you know when it opens."),
    ]),
    main=article(
        "Information Technology",
        "Can You Learn IT Support Online? What Employers Actually Look For",
        "The certification and hands-on skills that get you hired for a first help-desk job — and how to build "
        "them online.",
        "September 25, 2026", "8 min read", _p7_body)))


# ---- 8. Can You Learn a Skilled Trade Online -----------------------------
_p8_body = """        <!-- DRAFT – verified against docs/VERIFICATION_LOG.md (9/25/2026): MA license-hour examples added
             (A8: electrician 600 + 8,000 hrs; refrigeration 6,000 apprentice hrs or 450 study hrs + CFC/EPA 608);
             online-vs-hands-on split confirmed (B17/B18). CSC trades = "in development" only (F1). -->
        <p class="lead">Some of a skilled trade can be learned online — the theory, the code books, the safety
        rules, and the math. But the hands-on hours are the heart of a trade, and those still have to happen in
        person. The honest answer is: online helps, but it is only part of the path.</p>

        <p>Do not trust anyone who says you can become a licensed electrician or plumber entirely from your
        couch. The good news: the classroom side of a trade — which used to mean night classes across town — is
        now something you can do from home, on your own schedule. Here is what really works online, and what
        still does not.</p>

        <h2>What works well online</h2>
        <ul>
          <li><strong>Theory and fundamentals.</strong> How electricity, HVAC systems, or plumbing work.</li>
          <li><strong>Code and standards.</strong> Reading and understanding the codes your work must meet.</li>
          <li><strong>Math and blueprint basics.</strong> Measuring, load calculations, and reading plans.</li>
          <li><strong>Safety certificates.</strong> OSHA 10 and OSHA 30 safety courses are widely available
          online.</li>
          <li><strong>EPA 608 exam prep.</strong> The federal certification you need to handle refrigerants can
          be studied for online (the exam itself is proctored).</li>
          <li><strong>Test prep</strong> for state licensing exams.</li>
        </ul>

        <h2>What needs hands-on time</h2>
        <p>You cannot learn to bend conduit, sweat a copper joint, wire a panel, or troubleshoot a live system
        from a video alone. Trades require supervised, hands-on hours — often through an apprenticeship — where
        you build muscle memory and judgment under someone experienced. In most trades, this is also required
        for licensing. It is also how you learn to work safely around real voltage, gas, and pressure.</p>

        <div class="note"><strong>Watch out for overpromising.</strong> Some online "trade schools" suggest you
        can finish entirely online and walk into a licensed job. In Massachusetts, that is not how licensing
        works. Honest programs are clear that online coursework is one part of the path, not the whole thing.</div>

        <h2>How licensing works in Massachusetts</h2>
        <p>Licensed trades are regulated by the state, and the exact rules depend on the trade. For example, a
        Massachusetts journeyman electrician needs 600 hours of classroom instruction and 8,000 hours of
        supervised work over at least four years. A refrigeration technician needs either 6,000 hours as a
        licensed apprentice, or 450 hours of approved study, plus universal CFC (EPA 608) certification.
        Plumbing and gas fitting have their own rules set by the state board.</p>
        <p>One thing that surprises people: in Massachusetts, "HVAC" is not a single license. Depending on the
        work, it can fall under refrigeration technician, sheet metal, and gas fitting licenses. If HVAC is your
        goal, ask which license fits the jobs you actually want.</p>

        <h2>Registered apprenticeship: earn while you learn</h2>
        <p>For most trades, the smartest path is a <strong>registered apprenticeship</strong>. You work for a
        licensed employer, earn a paycheck, and build the supervised hours you need for your license — while
        taking the required classroom hours, which can often be done online. In Massachusetts, apprenticeships
        are overseen by the state's Division of Apprentice Standards.</p>
        <p>So "learn a trade online" really means: study the theory and safety online, and log your hands-on
        hours on the job.</p>
        <p>To find one, ask local employers and unions, check the state's apprenticeship listings, or ask a
        MassHire career center. Some apprenticeship programs may even connect to the funding options in our
        <a href="blog/free-job-training-massachusetts.html">guide to free job training in Massachusetts</a>.</p>

        <h2>Do the trades pay off?</h2>
        <p>Yes — and the work cannot be shipped overseas. In Massachusetts, electricians, plumbers, and HVAC and
        refrigeration mechanics all earn solid middle-class wages. For the actual numbers, see our roundup of the
        <a href="blog/highest-paying-certifications-massachusetts.html">highest-paying certifications you can
        train for in Massachusetts</a>.</p>

        <h2>Which trade might fit you?</h2>
        <p>Each trade has a different day-to-day. A few quick contrasts to help you think it through:</p>
        <ul>
          <li><strong>Electrician.</strong> Detailed, code-heavy work, indoors and out. Steady demand and a
          clear license ladder from apprentice to journeyman to master.</li>
          <li><strong>Plumbing and pipefitting.</strong> Problem-solving and physical work, often on service
          calls. Licensed in stages, much like electrical.</li>
          <li><strong>HVAC and refrigeration.</strong> A mix of electrical, mechanical, and airflow work, with
          busy seasons. Remember it can span more than one license.</li>
        </ul>
        <p>You do not have to decide today. Learning the fundamentals online is a low-cost way to test which one
        holds your interest before you commit to an apprenticeship.</p>

        <h2>A realistic hybrid path</h2>
        <ol>
          <li>Learn the theory, code, and safety — online is great for this.</li>
          <li>Get into an apprenticeship or hands-on program for supervised hours.</li>
          <li>Log the required hours while you earn.</li>
          <li>Prepare for and pass your licensing exam.</li>
        </ol>
        <p>So online is a smart way to start and to study — just plan for the in-person hours too.</p>

        <h2>What we are building</h2>
        <p>Career Skills Center is developing skilled trades training for Massachusetts. Details are not final
        yet. <a href="contact.html">Join our interest list</a> to be first to know when programs open.</p>

""" + FUNDING_NOTE + """

""" + post_cta(
    "Interested in the trades?",
    "Explore skilled-trades careers &mdash; how licensing and apprenticeships work, and how to get in. "
    "<!-- COURSE-DEPENDENT: R-BLOG --> Career Skills Center plans to offer training in the skilled trades; get "
    "updates when we launch.",
    "Explore skilled-trades careers", "skilled-trades-careers.html") + """

        <h2>Frequently asked questions</h2>
        <div class="faq">
          <details class="faq-item"><summary>Can I get a trade license fully online?</summary>
          <div><p>No. Massachusetts trade licenses require supervised, hands-on hours that cannot be done online.
          You can study the theory, code, and safety online, but you still need real on-the-job hours.</p></div></details>
          <details class="faq-item"><summary>What parts of a trade can I actually learn online?</summary>
          <div><p>The classroom side: theory and fundamentals, code, math and blueprint reading, OSHA safety, EPA
          608 exam prep, and licensing-exam prep. The hands-on skills come from an apprenticeship or shop.</p></div></details>
          <details class="faq-item"><summary>Do I need EPA 608 for HVAC?</summary>
          <div><p>Yes, if you handle refrigerants. EPA 608 is a federal certification, and you can study for it
          online. In Massachusetts, refrigeration work also needs a state license.</p></div></details>
          <details class="faq-item"><summary>How long does it take to get licensed?</summary>
          <div><p>It varies by trade. As one example, becoming a journeyman electrician in Massachusetts takes
          about four years — 600 classroom hours and 8,000 hours of supervised work — before you sit for the
          licensing exam.</p></div></details>
          <details class="faq-item"><summary>Does Career Skills Center offer trades training?</summary>
          <div><p>Not yet. Skilled trades training is in development. Join our interest list and we will let you
          know when it opens.</p></div></details>
        </div>

""" + related(
    ("WIOA Training Funds Explained", "wioa-explained.html"),
    ("Can You Learn IT Support Online?", "blog/can-you-learn-it-support-online.html"),
    ("Free Job Training in Massachusetts (full guide)", "blog/free-job-training-massachusetts.html"),
)

PAGES.append(dict(
    slug="blog/can-you-learn-a-trade-online.html", nav="blog.html",
    title="Can You Learn a Skilled Trade Online? What Works and What Needs Hands-On Time | Career Skills Center",
    ogtitle="Can You Learn a Skilled Trade Online? What Works and What Needs Hands-On Time",
    desc="Some of a skilled trade can be learned online — theory, code, and safety — but the hands-on hours still matter. An honest look at what works online and what does not.",
    extrahead=article_ld("blog/can-you-learn-a-trade-online.html",
                         "Can You Learn a Skilled Trade Online? What Works and What Needs Hands-On Time",
                         "What parts of skilled-trades training work online and what still needs hands-on hours.",
                         "2026-09-25", "2026-09-25") + "\n" + faq_ld([
        ("Can I get a trade license fully online?",
         "No. Massachusetts trade licenses require supervised, hands-on hours that cannot be done online. You can study the theory, code, and safety online, but you still need real on-the-job hours."),
        ("What parts of a trade can I actually learn online?",
         "The classroom side: theory and fundamentals, code, math and blueprint reading, OSHA safety, EPA 608 exam prep, and licensing-exam prep. The hands-on skills come from an apprenticeship or shop."),
        ("Do I need EPA 608 for HVAC?",
         "Yes, if you handle refrigerants. EPA 608 is a federal certification, and you can study for it online. In Massachusetts, refrigeration work also needs a state license."),
        ("How long does it take to get licensed in a trade?",
         "It varies by trade. As one example, becoming a journeyman electrician in Massachusetts takes about four years — 600 classroom hours and 8,000 hours of supervised work — before you sit for the licensing exam."),
        ("Does Career Skills Center offer trades training?",
         "Not yet. Skilled trades training is in development. Join the interest list and Career Skills Center will let you know when it opens."),
    ]),
    main=article(
        "Skilled Trades",
        "Can You Learn a Skilled Trade Online? What Works and What Needs Hands-On Time",
        "The theory can be online; the hands-on hours cannot. An honest map of the hybrid path into a licensed "
        "trade.",
        "September 25, 2026", "8 min read", _p8_body)))


# ---- contact.html ---------------------------------------------------------
PAGES.append(dict(
    slug="contact.html", nav="contact.html",
    title="Contact | Career Skills Center — Massachusetts",
    ogtitle="Contact Us",
    desc="Contact Career Skills Center in Massachusetts. Call (617) 544-7155 or email info@careerskillscenter.com.",
    main=hero("Contact", "Contact Us",
              "You’re moments away from a new career and a brighter future. Tell us a little about yourself "
              "and we’ll take it from there.",
              "images/Hero.webp") + """

    <section class="section">
      <div class="container contact-grid">

        <div class="contact-panel">
          <p class="eyebrow eyebrow--light"><span class="eyebrow-line" aria-hidden="true"></span>Let’s get connected</p>
          <h2>Send us a message</h2>

          <form class="contact-form" id="contact-page-form" action="submit.php" method="post" novalidate>
            <input type="hidden" name="source" value="contact-page">
            <input type="text" class="hp-field" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
            <label class="sr-only" for="cp-name">First and Last Name</label>
            <input id="cp-name" name="name" type="text" placeholder="First and Last Name" autocomplete="name" required>

            <label class="sr-only" for="cp-phone">Phone Number</label>
            <input id="cp-phone" name="phone" type="tel" placeholder="Phone Number" autocomplete="tel" required>

            <label class="sr-only" for="cp-email">Email Address</label>
            <input id="cp-email" name="email" type="email" placeholder="Email Address" autocomplete="email" required>

            <label class="sr-only" for="cp-reason">Reason for contacting</label>
            <select id="cp-reason" name="reason" required>
              <option value="" selected disabled>Reason for contacting</option>
              <option value="general">General question</option>
              <option value="employer">Employer training</option>
              <option value="partnership">Partnership</option>
              <option value="media">Media</option>
            </select>

            <label class="sr-only" for="cp-message">Message</label>
            <textarea id="cp-message" name="message" rows="5" placeholder="Message"></textarea>

            <button class="btn btn-yellow" type="submit">Submit</button>
            <p class="form-status" role="status" aria-live="polite"></p>
          </form>
          <p style="font-size:13px; opacity:.8; margin-top:18px;">By submitting this form you give Career
          Skills Center permission to contact you by phone, text and email.</p>
        </div>

        <div class="contact-details">
          <div>
            <h3>Address</h3>
            <p>Quincy, MA 02171</p>
          </div>
          <div>
            <h3>Phone</h3>
            <p><a href="tel:+16175447155">(617) 544-7155</a></p>
          </div>
          <div>
            <h3>Email</h3>
            <p><a href="mailto:info@careerskillscenter.com">info@careerskillscenter.com</a></p>
          </div>
          <div>
            <h3>Office hours</h3>
            <p>Monday – Friday<br>9:00am – 5:00pm</p>
          </div>
          <div>
            <h3>Follow us</h3>
            <!-- PLACEHOLDER: social profile URLs -->
            <ul class="social">
              <li><a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.3c-.3 0-1.3-.1-2.5-.1-2.4 0-4.1 1.5-4.1 4.2v2.4H7.5V14h2.7v8h3.3z"/></svg></a></li>
              <li><a href="#" aria-label="X (Twitter)"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M17.5 3h3l-6.6 7.6L21.7 21h-6.1l-4.8-6.2L5.3 21h-3l7.1-8.1L2.3 3h6.2l4.3 5.7L17.5 3zm-1.1 16.2h1.7L7.7 4.7H5.9l10.5 14.5z"/></svg></a></li>
              <li><a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM21.9 12c0-1.4 0-2.7-.1-4.1-.1-1.6-.4-3-1.6-4.2S17.6 2.2 16 2.1C14.7 2 13.4 2 12 2s-2.7 0-4.1.1c-1.6.1-3 .4-4.2 1.6S2.2 6.4 2.1 8C2 9.3 2 10.6 2 12s0 2.7.1 4.1c.1 1.6.4 3 1.6 4.2s2.6 1.5 4.2 1.6c1.4.1 2.7.1 4.1.1s2.7 0 4.1-.1c1.6-.1 3-.4 4.2-1.6s1.5-2.6 1.6-4.2c.1-1.4.1-2.7.1-4.1zm-2.4 5.8a3 3 0 0 1-1.7 1.7c-1.2.5-4 .4-5.8.4s-4.6.1-5.8-.4a3 3 0 0 1-1.7-1.7c-.5-1.2-.4-4-.4-5.8s-.1-4.6.4-5.8a3 3 0 0 1 1.7-1.7c1.2-.5 4-.4 5.8-.4s4.6-.1 5.8.4a3 3 0 0 1 1.7 1.7c.5 1.2.4 4 .4 5.8s.1 4.6-.4 5.8z"/></svg></a></li>
              <li><a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.9 21H3.2V8.9h3.7V21zM5 7.3a2.2 2.2 0 1 1 0-4.3 2.2 2.2 0 0 1 0 4.3zM21 21h-3.7v-5.9c0-1.4 0-3.2-2-3.2s-2.3 1.5-2.3 3.1V21H9.3V8.9h3.6v1.7h.1c.5-.9 1.7-2 3.5-2 3.8 0 4.5 2.5 4.5 5.7V21z"/></svg></a></li>
            </ul>
          </div>
        </div>

      </div>
    </section>

    <section class="section section--alt section--tight">
      <div class="container narrow">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Based in Quincy</p>
        <h2 class="section-title left">How We Work</h2>
        <p>Career Skills Center is based in Quincy, Massachusetts, and our guides and support are offered
        online across the state. The fastest way to reach us is by phone or email &mdash; we usually reply
        within one business day.</p>
        <div class="feature-grid" style="margin-top: 40px;">
          <article class="feature">
            <h3 class="feature-title">Call us</h3>
            <p><a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a></p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Email us</h3>
            <p><a class="link-yellow" href="mailto:info@careerskillscenter.com">info@careerskillscenter.com</a></p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Office hours</h3>
            <p>Monday through Friday, 9:00am to 5:00pm. Evening appointments available by request.</p>
          </article>
        </div>
      </div>
    </section>
"""))


# ---- privacy-policy.html --------------------------------------------------
PAGES.append(dict(
    slug="privacy-policy.html", nav=None,
    title="Privacy Policy | Career Skills Center",
    ogtitle="Privacy Policy",
    desc="How Career Skills Center collects, uses and protects personal information.",
    main=hero("Legal", "Privacy Policy",
              "How we collect, use and protect the information you share with us.",
              None) + """

    <section class="section">
      <div class="container prose">
        <p class="updated">Last updated: [Month DD, YYYY]</p>

        <p class="note"><strong>Template only.</strong> This page is a starting structure, not legal advice.
        Have counsel review and finalize it before publishing, and confirm obligations under the
        Massachusetts data security regulation 201 CMR 17.00 and any student-records rules that apply.</p>

        <h2>Information we collect</h2>
        <p>When you contact us, join an interest list, use the &ldquo;Do I Qualify?&rdquo; check, or submit an
        employer inquiry, we may collect the details you provide &mdash; such as your name, email address, phone
        number, preferred language, company name, the reason you&rsquo;re contacting us, and any answers or
        message you choose to include. If you use the eligibility check, the answers you select are included when
        you ask us to email you your results.</p>

        <h2>How we use your information</h2>
        <ul>
          <li>To respond to your inquiry and help you understand your training and funding options</li>
          <li>To email the results and next steps you request</li>
          <li>To respond to employer training inquiries</li>
          <li>To send you updates you asked for, such as when training launches</li>
          <li>To improve this website and our guides</li>
          <li>To meet legal and reporting obligations</li>
        </ul>

        <h2>Communications consent</h2>
        <p>By submitting a form on this site you give Career Skills Center permission to contact you by
        phone, text message and email. Message and data rates may apply. You can opt out at any time by
        replying STOP to a text, using the unsubscribe link in an email, or calling us at
        <a href="tel:+16175447155">(617) 544-7155</a>.</p>

        <h2>Sharing your information</h2>
        <p>We do not sell your personal information. We share it only with service providers who help us
        operate the school, with funding agencies when you apply for assistance, and where required by law.</p>

        <h2>Cookies and analytics</h2>
        <p>This website uses <strong>Google Analytics 4 (GA4)</strong> to understand how visitors use the site
        &mdash; for example, which pages are viewed and when a form is submitted. GA4 sets cookies and collects
        usage data such as your approximate location, device and browser. We use this only in aggregate to
        improve the site. You can limit this with your browser settings or a tracking-blocker. See
        <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google&rsquo;s privacy
        policy</a> for how Google handles this data.</p>
        <p><span class="tbd">[Confirm and list any additional advertising or tracking tools before publishing.]</span></p>

        <h2>Data security</h2>
        <p>We maintain administrative, technical and physical safeguards intended to protect personal
        information against unauthorized access, use or disclosure.</p>

        <h2>Your choices</h2>
        <p>You may request access to, correction of, or deletion of the personal information we hold about
        you by contacting
        <a href="mailto:info@careerskillscenter.com">info@careerskillscenter.com</a>. Some records must
        be retained to meet legal and accreditation requirements.</p>

        <h2>Children’s privacy</h2>
        <p>This site is not directed to children under 13 and we do not knowingly collect their information.</p>

        <h2>Changes to this policy</h2>
        <p>We may update this policy from time to time. The revision date at the top of this page reflects the
        most recent version.</p>

        <h2>Contact us</h2>
        <p>Career Skills Center<br>
        Quincy, MA 02171<br>
        <a href="tel:+16175447155">(617) 544-7155</a><br>
        <a href="mailto:info@careerskillscenter.com">info@careerskillscenter.com</a></p>
      </div>
    </section>
"""))


# ---- terms.html (v1.5 rename of terms-of-use.html) ------------------------
PAGES.append(dict(
    slug="terms.html", nav=None,
    title="Terms of Use | Career Skills Center",
    ogtitle="Terms of Use",
    desc="The terms that govern your use of the Career Skills Center website.",
    main=hero("Legal", "Terms of Use",
              "The terms that govern your use of this website.",
              None) + """

    <section class="section">
      <div class="container prose">
        <p class="updated">Last updated: [Month DD, YYYY]</p>

        <p class="note"><strong>Template only.</strong> This page is a starting structure, not legal advice.
        Have counsel review and finalize it before publishing.</p>

        <h2>Acceptance of terms</h2>
        <p>By accessing careerskillscenter.com you agree to these terms. If you do not agree, please do not
        use the site.</p>

        <h2>Use of the site</h2>
        <p>You may use this site for lawful purposes only. You agree not to interfere with its operation,
        attempt unauthorized access, or use automated tools to collect information from it.</p>

        <h2>Program information</h2>
        <p>Program descriptions, lengths, credentials, schedules and pricing on this site are subject to
        change. Nothing on this site is a guarantee of admission, certification, employment or earnings. The
        enrollment agreement you sign governs the terms of your training.</p>

        <h2>Intellectual property</h2>
        <p>The content, design, logos and materials on this site are owned by Career Skills Center or its
        licensors and may not be reproduced without permission.</p>

        <h2>Third-party links</h2>
        <p>This site may link to third-party websites, including funding agencies and lending partners. We are
        not responsible for their content or practices, and a link is not an endorsement.</p>

        <h2>Disclaimer of warranties</h2>
        <p>This site is provided on an “as is” and “as available” basis without warranties of any kind, to the
        fullest extent permitted by law.</p>

        <h2>Limitation of liability</h2>
        <p>To the fullest extent permitted by law, Career Skills Center is not liable for any indirect,
        incidental or consequential damages arising from your use of this site.</p>

        <h2>Governing law</h2>
        <p>These terms are governed by the laws of the Commonwealth of Massachusetts, without regard to
        conflict of law principles.</p>

        <h2>Contact us</h2>
        <p>Questions about these terms? Email
        <a href="mailto:info@careerskillscenter.com">info@careerskillscenter.com</a> or call
        <a href="tel:+16175447155">(617) 544-7155</a>.</p>
      </div>
    </section>
"""))


# ---------------------------------------------------------------------------
# WRITE
# ---------------------------------------------------------------------------
written = 0
_seen = set()
for page in PAGES:
    if page["slug"] in ARCHIVED:
        print("skipped (archived)", page["slug"])
        continue
    if page["slug"] in REDIRECTS:
        # Emit a redirect stub instead of the (now unused) full page body.
        dest = ROOT / page["slug"]
        dest.write_text(redirect_html(page["slug"], REDIRECTS[page["slug"]]), encoding="utf-8")
        print("redirect", page["slug"], "->", REDIRECTS[page["slug"]])
        _seen.add(page["slug"])
        continue
    header = HEADER
    footer = FOOTER
    if page["nav"]:
        target = 'href="%s"' % page["nav"]
        header = header.replace(target, target + ' aria-current="page"')
        footer = footer.replace(target, target + ' aria-current="page"')

    html = (PAGE
            .replace("@@TITLE@@", page["title"])
            .replace("@@OGTITLE@@", page["ogtitle"])
            .replace("@@DESC@@", page["desc"])
            .replace("@@SLUG@@", page["slug"])
            .replace("@@EXTRAHEAD@@", page.get("extrahead", ""))
            .replace("@@HEADER@@", header)
            .replace("@@FOOTER@@", footer)
            .replace("@@DIALOG@@", DIALOG)
            .replace("@@MAIN@@", page["main"])
            .replace("@@CSSVER@@", CSS_VER)
            .replace("@@JSVER@@", JS_VER)
            .replace("@@CFGVER@@", CFG_VER))

    # Pages in a subdirectory (e.g. blog/<slug>.html) need every relative link in
    # the shared chrome and body rewritten one level up so it still resolves.
    depth = page["slug"].count("/")
    if depth:
        prefix = "../" * depth
        html = re.sub(
            r'(href|src|action)="(?!https?:|//|/|#|mailto:|tel:|data:|javascript:)',
            lambda m: '%s="%s' % (m.group(1), prefix), html)

    dest = ROOT / page["slug"]
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print("wrote", page["slug"], len(html), "bytes")
    written += 1

print("\n%d pages written." % written)

# ---------------------------------------------------------------------------
# SITEMAP  (auto-lists live public pages so search engines / AI can crawl)
# ---------------------------------------------------------------------------
SITE = "https://careerskillscenter.com/"
# Redirected + unlinked pages are left out of the sitemap.
SITEMAP_EXCLUDE = set(REDIRECTS) | HOLD
_today = datetime.date.today().isoformat()
_urls = ['  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>'
         % (SITE, _today)]
for page in PAGES:
    slug = page["slug"]
    if slug in ARCHIVED or slug in SITEMAP_EXCLUDE:
        continue
    _urls.append('  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
                 % (SITE, slug, _today))
_sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(_urls) + "\n</urlset>\n")
(ROOT / "sitemap.xml").write_text(_sitemap, encoding="utf-8")
print("wrote sitemap.xml (%d urls)" % len(_urls))
