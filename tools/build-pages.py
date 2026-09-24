#!/usr/bin/env python3
"""Generate the Career Skills Center inner pages.

Reads index.html, lifts the shared <header>, <footer> and <dialog> out of it so
every page stays byte-identical to the home page, then writes each inner page.
Re-run after changing the header/footer/dialog on index.html.
"""
import re
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

# index.html isn't regenerated, so keep its own asset links stamped here.
_stamped = re.sub(r'(href="css/style\.css)(\?v=\d+)?"', r'\1?v=%s"' % CSS_VER, home)
_stamped = re.sub(r'(src="js/main\.js)(\?v=\d+)?"', r'\1?v=%s"' % JS_VER, _stamped)
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
</head>
<body>

  <a class="skip-link" href="#main">Skip to content</a>

@@HEADER@@

  <main id="main">

@@MAIN@@

  </main>

@@FOOTER@@

@@DIALOG@@

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


def hero(label, title, lede, img="images/Hero.webp", btn2=("Our Programs", "our-programs.html")):
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


# ---- programs.html --------------------------------------------------------
PAGES.append(dict(
    slug="programs.html", nav="our-programs.html",
    title="Programs | Career Skills Center — Trade, IT &amp; Medical Training in Massachusetts",
    ogtitle="Our Programs",
    desc="Career-focused training programs in the skilled trades, information technology and the medical field at Career Skills Center in Massachusetts.",
    main=hero("Programs", "Our Programs",
              "The right training program sets you on a pathway to success with the certifications and "
              "credentials that open doors to new jobs and greater earning potential.",
              "images/programs-hero.webp", ("How to Enroll", "admissions.html")) + f"""

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Find Your Program</p>
        <h2 class="section-title left">Three Fields. One Future.</h2>
        <div class="section-intro">
          <p>Career Skills Center trains students for three of the strongest hiring markets in Massachusetts. Every program is built around hands-on practice, a recognized credential, and the job
          search that follows. Pick the field that fits you and we will walk you through the rest.</p>
        </div>
{program_cards()}
        {DRAFT_NOTE}
      </div>
    </section>

    <section class="section section--alt" id="trades">
      <div class="container">
        <div class="split-grid">
          <div class="split-media">
            <img src="images/trades.webp" alt="Technician in a hard hat servicing pipes and valves" loading="lazy" decoding="async">
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Skilled Trades</p>
            <h2 class="section-title left">Build a Hands-On Career</h2>
            <p>The trades are hiring. Electricians, HVAC technicians and plumbers are retiring faster than
            they are being replaced, and contractors across Massachusetts are competing for trained help.
            Our trade programs put tools in your hands early and prepare you for the credentials employers
            and licensing boards ask for.</p>
            <ul class="arrow-list">
              <li>Shop and lab time, not just lecture</li>
              <li>Safety credentials employers expect</li>
              <li>Apprenticeship and licensure preparation</li>
              <li>Day and evening options</li>
            </ul>
          </div>
        </div>

        <div class="program-items">
{prog_item("Electrical Technician", "Wiring, circuits, load calculations, and safe installation practice for residential and light commercial work.", "OSHA 10 &middot; apprenticeship prep")}
{prog_item("HVAC/R Technician", "Heating, ventilation, air conditioning and refrigeration service, diagnostics and installation.", "EPA Section 608 &middot; OSHA 10")}
{prog_item("Plumbing Technician", "Pipefitting, fixture installation, venting, drainage and water supply systems.", "OSHA 10 &middot; apprenticeship prep")}
{prog_item("Welding", "SMAW, MIG and TIG fundamentals with booth time, blueprint reading and weld inspection basics.", "AWS entry-level welder prep")}
{prog_item("Carpentry &amp; Construction", "Framing, finish carpentry, blueprint reading, materials and jobsite safety.", "OSHA 10 &middot; NCCER Core prep")}
        </div>
      </div>
    </section>

    <section class="section" id="it">
      <div class="container">
        <div class="split-grid reverse">
          <div class="split-media">
            <img src="images/hero2.webp" alt="Student working at a laptop" loading="lazy" decoding="async">
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Information Technology</p>
            <h2 class="section-title left">Launch Your Tech Career</h2>
            <p>You do not need a four-year degree to work in IT. Employers hire on certifications and
            demonstrated skill. Our IT track moves from the help desk fundamentals every employer tests for
            up through networking, security and cloud, so you can stack credentials as you go.</p>
            <ul class="arrow-list">
              <li>Hands-on labs and real hardware</li>
              <li>Industry certification exam preparation</li>
              <li>Stackable credentials you can build on</li>
              <li>Resume and interview coaching included</li>
            </ul>
          </div>
        </div>

        <div class="program-items">
{prog_item("IT Support Specialist", "Hardware, operating systems, troubleshooting and ticketing — the core help desk skill set.", "CompTIA A+ prep")}
{prog_item("Network Technician", "Routing, switching, cabling, wireless and network troubleshooting.", "CompTIA Network+ prep")}
{prog_item("Cybersecurity Fundamentals", "Threats, access control, encryption basics and incident response fundamentals.", "CompTIA Security+ prep")}
{prog_item("Cloud Fundamentals", "Core cloud concepts, services, billing and security across major providers.", "AWS Cloud Practitioner or AZ-900 prep")}
        </div>
      </div>
    </section>

    <section class="section section--alt" id="medical">
      <div class="container">
        <div class="split-grid">
          <div class="split-media">
            <img class="align-top" src="images/medical.webp" alt="Smiling medical assistant with clinical colleagues in a hospital corridor" loading="lazy" decoding="async">
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Medical</p>
            <h2 class="section-title left">Care for Your Community</h2>
            <p>Massachusetts is one of the largest healthcare employment markets in the country. Clinics,
            hospitals and long-term care facilities across the state need trained support
            staff now. These programs prepare you for entry-level clinical and administrative roles and the
            certification exams that go with them.</p>
            <ul class="arrow-list">
              <li>Clinical skills practice in a lab setting</li>
              <li>Certification exam preparation</li>
              <li>Externship placement support</li>
              <li>Pathways into further nursing and allied health study</li>
            </ul>
          </div>
        </div>

        <div class="program-items">
{prog_item("Medical Assistant", "Clinical and administrative duties: vitals, patient intake, injections, scheduling and records.", "CCMA prep")}
{prog_item("Phlebotomy Technician", "Venipuncture technique, specimen handling, safety and patient care.", "CPT prep")}
{prog_item("EKG Technician", "Electrocardiogram setup, lead placement, rhythm recognition and reporting.", "CET prep")}
{prog_item("Certified Nursing Assistant", "Direct patient care, mobility, hygiene, vitals and documentation.", "MA Nurse Aide Registry prep")}
{prog_item("Medical Billing &amp; Coding", "ICD-10 and CPT coding, claims, insurance workflows and compliance.", "CBCS prep")}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How It Works</p>
        <h2 class="section-title left">What Every Program Includes</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Hands-On Labs</h3>
            <p>You learn by doing. Every program pairs instruction with lab and shop time so you practice the
            work before you are hired to do it.</p>
            <a class="read-more" href="about.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
          <article class="feature">
            <h3 class="feature-title">Industry Certifications</h3>
            <p>Programs are built around the credentials employers screen for, with exam preparation built
            into the course.</p>
            <a class="read-more" href="faq.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
          <article class="feature">
            <h3 class="feature-title">Job Placement Support</h3>
            <p>Resume help, mock interviews and employer connections. Career Services works with every
            student through completion and beyond.</p>
            <a class="read-more" href="career-services.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
        </div>
      </div>
    </section>

""" + cta("Not sure which program is right for you?", "Talk to an Advisor")))


# ---- our-programs.html ----------------------------------------------------
# Card-grid overview linked from the homepage "Our Programs" button. The image
# areas are intentional placeholders until program photos are chosen.
PAGES.append(dict(
    slug="our-programs.html", nav="our-programs.html",
    title="Our Programs | Career Skills Center — Massachusetts",
    ogtitle="Our Programs",
    desc="Explore Career Skills Center training in the skilled trades, information technology and the medical field in Massachusetts.",
    main=hero("Our Programs", "Our Programs",
              "Explore the fields we train for. Pick a path and we will walk you through the programs, "
              "credentials and the steps to enroll.",
              "images/programs-hero.webp", ("How to Enroll", "admissions.html")) + """

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Explore Our Programs</p>
        <h2 class="section-title left">Choose Your Field</h2>
        <div class="pcard-grid">

          <article class="pcard" id="trades">
            <img src="images/electrician.webp" alt="Electrician at work" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <h3 class="pcard-title">Skilled Trades</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Hands-on training for electrical, HVAC/R, plumbing, welding and carpentry, built around the credentials employers and licensing boards ask for.</p>
              <a class="btn btn-outline-navy" href="skilled-trades.html">Read more</a>
            </div>
          </article>

          <article class="pcard" id="it">
            <img src="images/comptia.webp" alt="CompTIA certification training" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <h3 class="pcard-title">Information Technology</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Stack industry certifications from help-desk fundamentals through networking, security and cloud. No four-year degree required.</p>
              <a class="btn btn-outline-navy" href="it-support-specialist.html">Read more</a>
            </div>
          </article>

          <article class="pcard" id="medical">
            <img src="images/medicalbilling.webp" alt="Medical billing and coding specialist" class="pcard-media" loading="lazy" decoding="async">
            <div class="pcard-body">
              <h3 class="pcard-title">Medical</h3>
              <span class="pcard-rule" aria-hidden="true"></span>
              <p>Train for in-demand clinical and administrative roles in healthcare, with certification exam preparation built into every program.</p>
              <a class="btn btn-outline-navy" href="medical-billing-coding.html">Read more</a>
            </div>
          </article>

        </div>
      </div>
    </section>

""" + cta("Not sure which program is right for you?", "Talk to an Advisor")))


# ---- it-support-specialist.html -------------------------------------------
# Detailed IT course page (equivalent of NTI's per-program pages), built around
# the entry-level CompTIA Tech+ (FC0-U71) certification. Students earn a Career
# Skills Center certificate; the CompTIA exam is scheduled and paid separately.
PAGES.append(dict(
    slug="it-support-specialist.html", nav="our-programs.html",
    title="IT Support Specialist &mdash; CompTIA Tech+ Training | Career Skills Center",
    ogtitle="IT Support Specialist",
    desc="Online IT Support Specialist training that prepares you for the CompTIA Tech+ (FC0-U71) certification. About 8 weeks, no experience required, at Career Skills Center in Massachusetts.",
    main=hero("Information Technology", "IT Support Specialist",
              "If you are a problem-solver who likes technology, a career in IT support may be perfect for "
              "you. Build the foundation employers look for, 100% online, in about eight weeks.",
              "images/comptia.webp", ("How to Enroll", "admissions.html")) + """

    <section class="section">
      <div class="container">
        <div class="split-grid">
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>100% Online Training</p>
            <h2 class="section-title left">Foundational IT Skills, Fully Online</h2>
            <p>Train on your own schedule and build the core knowledge every support role depends on:
            computers and devices, operating systems and applications, basic networking, data and security.
            You will be ready to sit for the CompTIA Tech+ (FC0-U71) certification exam, and no prior
            experience is required to start.</p>
            <button class="btn btn-navy js-open-contact" type="button">Get in Touch</button>
          </div>
          <div class="split-media">
            <img src="images/hero2.webp" alt="Student learning IT online at a laptop" loading="lazy" decoding="async">
          </div>
        </div>

        <div class="spec-grid">
          <div class="spec-card"><div class="spec-value">8 Weeks</div><div class="spec-label">Program Length</div></div>
          <div class="spec-card"><div class="spec-value">CompTIA Tech+ (FC0-U71)</div><div class="spec-label">Certification</div></div>
          <div class="spec-card"><div class="spec-value">CompTIA</div><div class="spec-label">Issuing Authority</div></div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split-grid reverse">
          <div class="split-media">
            <img src="images/programs-hero.webp" alt="IT support technician at work" loading="lazy" decoding="async">
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Career Insight</p>
            <h2 class="section-title left">What does an IT Support Specialist do?</h2>
            <p>IT support specialists keep people and technology working together. They set up and fix the
            devices, software and accounts a business runs on, and they are usually the first person a user
            turns to when something stops working. It is a role built on curiosity, patience and clear
            communication. Day to day, you might:</p>
            <ul class="arrow-list">
              <li>Set up and configure computers, peripherals and mobile devices</li>
              <li>Install and update operating systems and applications</li>
              <li>Diagnose and resolve common hardware and software problems</li>
              <li>Support users by phone, chat or in person and document tickets</li>
              <li>Apply everyday security best practices to protect devices and data</li>
              <li>Recognize when to solve an issue and when to escalate it</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Job Outlook</p>
        <div class="split-grid split-grid--top">
          <div class="split-copy">
            <h2 class="section-title left">Potential Career Paths</h2>
            <p>IT support specialists keep people and technology working together, and demand for them is
            steady as businesses of every kind rely on computers, software and networks. Entry-level IT
            support is one of the most common ways into a technology career.</p>
            <p>This program prepares you to find an entry-level support role and to keep stacking
            credentials, such as CompTIA A+, Network+ or Security+, as you decide where to specialize.</p>
            <p>Individuals who complete this program and earn the certification have the skills to find jobs
            as:</p>
            <ul class="arrow-list">
              <li>IT Support Specialist</li>
              <li>Help Desk Technician</li>
              <li>Technical Support Technician</li>
              <li>IT Operations Associate</li>
              <li>Desktop Support Assistant</li>
              <li>Junior Service Desk Analyst</li>
            </ul>
          </div>
          <div class="outlook-panel">
            <div class="outlook-value">48,700</div>
            <p class="outlook-caption">IT SUPPORT OPENINGS EACH YEAR IN THE U.S.</p>
            <p class="outlook-body">Entry-level IT support is an in-demand field with room to grow. Support
            specialists typically start around $21 to $25 per hour, and as you add certifications and
            experience you can move into higher-paying networking, security and systems roles.</p>
            <p class="outlook-note">Note: The U.S. Bureau of Labor Statistics projects about 48,700 job
            openings each year for computer support specialists, a field of roughly 903,100 jobs in 2025.
            Pay varies by education, experience, employer and location.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Soft Skills Check</p>
        <h2 class="section-title left">Do You Have What It Takes to Succeed?</h2>
        <div class="split-grid split-grid--top">
          <div class="split-copy">
            <p class="soft-subtitle">Common Attributes of Successful IT Support Specialists</p>
            <img class="soft-icon" src="images/comptia-logo.webp" alt="CompTIA" width="558" height="120" loading="lazy" decoding="async">
          </div>
          <ul class="check-list">
            <li><strong>Problem-Solving</strong>Break a problem into symptoms, likely causes and next steps instead of guessing.</li>
            <li><strong>Clear Communication</strong>Explain technical issues in plain language that users and coworkers trust.</li>
            <li><strong>Attention to Detail</strong>Small settings and skipped steps are often the difference between fixed and broken.</li>
            <li><strong>Patience</strong>Stay calm and methodical under pressure, even when a user is frustrated.</li>
            <li><strong>Curiosity and a Willingness to Learn</strong>Technology keeps changing, and the best techs keep learning with it.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How You Learn</p>
        <h2 class="section-title left">Learn Online, Get Certified</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Learn on Your Schedule</h3>
            <p>Self-paced video lessons, interactive exercises and hands-on practice scenarios, with closed
            captions, that you can work through anywhere. No commute, and no prior experience required.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Train and Get Certified</h3>
            <p>Prepare for the CompTIA Tech+ (FC0-U71) exam as you move through the curriculum, and earn a
            Career Skills Center Certificate of Completion so you can show employers the skills you have
            built.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--alt course-overview">
      <div class="deco-dots deco-dots--left" aria-hidden="true"></div>
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Course Overview</p>
        <h2 class="section-title left">IT Support Specialist &middot; CompTIA Tech+</h2>
        <div class="split-grid split-grid--top">
          <div class="split-copy">
            <p>This program builds entry-level technical fluency across the six areas the <strong>CompTIA
            Tech+ (FC0-U71)</strong> exam measures. In about eight weeks of online training you will be
            prepared to sit for the certification exam and to step into a help desk or support role. You earn
            a <strong>Career Skills Center Certificate of Completion</strong>; the CompTIA Tech+ exam is
            scheduled and paid separately through CompTIA.</p>
          </div>
          <div class="faq">
          <details class="faq-item">
            <summary>Scheduling details</summary>
            <div class="faq-body"><p>About 8 weeks, 89 program hours, delivered 100% online and self-paced
            within the term. <span class="tbd">Start dates TBD &mdash; call to confirm the next available
            cohort.</span></p></div>
          </details>
          <details class="faq-item">
            <summary>Instruction &amp; evaluation</summary>
            <div class="faq-body"><p>Guided video lessons, interactive exercises and hands-on practice
            scenarios, with knowledge checks and exam-style practice questions to prepare you for the
            certification exam.</p></div>
          </details>
          <details class="faq-item">
            <summary>Books &amp; materials</summary>
            <div class="faq-body"><p>All courseware is included in your tuition: online video lessons,
            interactive labs and exercises, practice questions and closed captions. No separate textbook
            purchase is required.</p></div>
          </details>
          <details class="faq-item">
            <summary>Course outline</summary>
            <div class="faq-body">
              <ul class="arrow-list">
                <li>IT concepts &amp; terminology, and troubleshooting logic</li>
                <li>Hardware, peripherals and device setup</li>
                <li>Operating systems and application software</li>
                <li>Programming and software development fundamentals</li>
                <li>Database concepts and data fundamentals</li>
                <li>Security principles and safe computing practices</li>
              </ul>
            </div>
          </details>
          <details class="faq-item">
            <summary>Upon completion, students will be able to&hellip;</summary>
            <div class="faq-body">
              <ul class="arrow-list">
                <li>Explain core computing concepts using the right technical vocabulary</li>
                <li>Identify hardware components and set up common peripherals and devices</li>
                <li>Describe how operating systems and applications work and are managed</li>
                <li>Understand basic programming logic and database concepts</li>
                <li>Apply confidentiality, integrity and availability to everyday security</li>
                <li>Troubleshoot common problems methodically and be ready for the CompTIA Tech+ exam</li>
              </ul>
            </div>
          </details>
          </div>
        </div>
      </div>
    </section>

""" + cta("Ready to start your IT career?", "Get in Touch")))


# ---- medical-billing-coding.html ------------------------------------------
# Detailed Medical program page. Online medical billing & coding built around
# the AAPC CPC and CPB certifications. Students earn a Career Skills Center
# certificate; AAPC exams are scheduled and paid separately through AAPC.
PAGES.append(dict(
    slug="medical-billing-coding.html", nav="our-programs.html",
    title="Medical Billing &amp; Coding &mdash; AAPC CPC &amp; CPB Training | Career Skills Center",
    ogtitle="Medical Billing & Coding",
    desc="Online Medical Billing & Coding training that prepares you for the AAPC CPC and CPB certifications. About 11 weeks, 100% online, at Career Skills Center in Massachusetts.",
    main=hero("Medical", "Medical Billing &amp; Coding",
              "If you are detail-oriented and want a healthcare career without years of school, medical "
              "billing and coding could be your path. Train 100% online in about eleven weeks.",
              "images/medicalbilling.webp", ("How to Enroll", "admissions.html")) + """

    <section class="section">
      <div class="container">
        <div class="split-grid">
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>100% Online Training</p>
            <h2 class="section-title left">Job-Ready Skills, Fully Online</h2>
            <p>Learn how documentation becomes codes, how those codes drive reimbursement, and how to keep
            claims clean, complete and compliant. You will train on current ICD-10-CM standards with ICD-11
            awareness, and be ready to sit for the AAPC CPC and CPB certification exams. No prior experience
            required.</p>
            <button class="btn btn-navy js-open-contact" type="button">Get in Touch</button>
          </div>
          <div class="split-media">
            <img class="align-top" src="images/billing-coding.webp" alt="Medical billing and coding specialist reviewing records" loading="lazy" decoding="async">
          </div>
        </div>

        <div class="spec-grid">
          <div class="spec-card"><div class="spec-value">11 Weeks</div><div class="spec-label">Program Length</div></div>
          <div class="spec-card"><div class="spec-value">AAPC CPC &amp; CPB</div><div class="spec-label">Certification</div></div>
          <div class="spec-card"><div class="spec-value">AAPC</div><div class="spec-label">Issuing Authority</div></div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split-grid reverse">
          <div class="split-media">
            <img src="images/medicalbilling.webp" alt="Medical coder working at a computer" loading="lazy" decoding="async">
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Career Insight</p>
            <h2 class="section-title left">What does a medical biller and coder do?</h2>
            <p>Medical billers and coders turn a patient visit into an accurate, payable claim. They read the
            clinical documentation, assign the right codes, and make sure the paperwork holds up so providers
            get reimbursed and patients are billed correctly. It is careful, behind-the-scenes work that keeps
            a healthcare practice running. Day to day, you might:</p>
            <ul class="arrow-list">
              <li>Read clinical notes and assign accurate ICD-10-CM diagnosis and procedure codes</li>
              <li>Translate visits into clean, complete insurance claims</li>
              <li>Apply payer rules and billing guidelines so claims get paid</li>
              <li>Review and correct documentation issues that cause denials</li>
              <li>Protect patient information under HIPAA privacy rules</li>
              <li>Follow up on claims, denials and reimbursements</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Job Outlook</p>
        <div class="split-grid split-grid--top">
          <div class="split-copy">
            <h2 class="section-title left">Potential Career Paths</h2>
            <p>Medical records and coding is one of the steadier ways into healthcare, and it does not require
            hands-on patient care. Demand is projected to grow much faster than average as the healthcare
            system expands and every visit has to be documented, coded and billed.</p>
            <p>This program prepares you to work in a provider office, hospital, clinic or remote coding role,
            and to keep building credentials through AAPC as you specialize.</p>
            <p>Individuals who complete this program and earn certification have the skills to find jobs as:</p>
            <ul class="arrow-list">
              <li>Medical Coder</li>
              <li>Medical Biller</li>
              <li>Medical Records Specialist</li>
              <li>Coding Specialist</li>
              <li>Billing / Claims Specialist</li>
              <li>Health Information Clerk</li>
            </ul>
          </div>
          <div class="outlook-panel">
            <div class="outlook-value">14,000</div>
            <p class="outlook-caption">MEDICAL RECORDS &amp; CODING OPENINGS EACH YEAR IN THE U.S.</p>
            <p class="outlook-body">The field is projected to grow 8% through 2035, much faster than average.
            Median pay is about $48,000 a year (roughly $23 an hour), and it climbs as you add certifications
            and experience.</p>
            <p class="outlook-note">Note: The U.S. Bureau of Labor Statistics projects about 14,000 openings
            each year for medical records specialists, a field of roughly 200,700 jobs in 2025. Pay varies by
            education, experience, employer and location.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Soft Skills Check</p>
        <h2 class="section-title left">Do You Have What It Takes to Succeed?</h2>
        <div class="split-grid split-grid--top">
          <div class="split-copy">
            <p class="soft-subtitle">Common Attributes of Successful Medical Billers &amp; Coders</p>
            <img class="soft-icon soft-photo" src="images/billing.webp" alt="Medical billing and coding professional reviewing records on a tablet" width="500" height="750" loading="lazy" decoding="async">
          </div>
          <ul class="check-list">
            <li><strong>Attention to Detail</strong>A single wrong digit can deny a claim, so precision matters on every record.</li>
            <li><strong>Analytical Thinking</strong>Read the documentation and choose the most accurate, specific code.</li>
            <li><strong>Integrity and Discretion</strong>You handle protected health information every day and must keep it private.</li>
            <li><strong>Persistence</strong>Follow up on denials and unpaid claims until they are resolved.</li>
            <li><strong>Continuous Learning</strong>Code sets and payer rules change every year, and good coders keep up.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>How You Learn</p>
        <h2 class="section-title left">Learn Online, Get Certified</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Learn on Your Schedule</h3>
            <p>Self-paced video lessons and real-world coding examples, with closed captions, that you can
            work through anywhere. No commute, and no prior experience required.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Train and Get Certified</h3>
            <p>Prepare for the AAPC CPC (Certified Professional Coder) and CPB (Certified Professional Biller)
            exams, and earn a Career Skills Center Certificate of Completion to show employers.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--alt course-overview">
      <div class="deco-dots deco-dots--left" aria-hidden="true"></div>
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Course Overview</p>
        <h2 class="section-title left">Medical Billing &amp; Coding</h2>
        <div class="split-grid split-grid--top">
          <div class="split-copy">
            <p>This program builds job-ready medical billing and coding skills using current ICD-10-CM
            standards, with ICD-11 awareness, plus the billing, claims and HIPAA compliance knowledge every
            healthcare office depends on. In about eleven weeks of online training you graduate with a
            <strong>Career Skills Center Certificate of Completion</strong>, included in your tuition. To
            stand out to employers, you can also add a nationally recognized <strong>AAPC certification (CPC
            or CPB)</strong> &mdash; we prepare you for the exam, which you schedule and pay for directly with
            AAPC.</p>
          </div>
          <div class="faq">
          <details class="faq-item">
            <summary>Scheduling details</summary>
            <div class="faq-body"><p>About 11 weeks, 117 program hours, delivered 100% online and self-paced
            within the term. <span class="tbd">Start dates TBD &mdash; call to confirm the next available
            cohort.</span></p></div>
          </details>
          <details class="faq-item">
            <summary>Instruction &amp; evaluation</summary>
            <div class="faq-body"><p>Guided video lessons and real-world coding examples, with knowledge
            checks and practice to prepare you for the certification exams.</p></div>
          </details>
          <details class="faq-item">
            <summary>Books &amp; materials</summary>
            <div class="faq-body"><p>All courseware is included in your tuition: online video lessons, coding
            practice and closed captions. No separate textbook purchase is required. <span class="tbd">Official
            AAPC code books for the exam are confirmed separately &mdash; ask an advisor.</span></p></div>
          </details>
          <details class="faq-item">
            <summary>Course outline</summary>
            <div class="faq-body">
              <ul class="arrow-list">
                <li>Medical terminology and anatomy</li>
                <li>ICD-10-CM foundations and ICD-11 awareness</li>
                <li>Diagnosis coding and documentation support</li>
                <li>Procedure coding and claim alignment</li>
                <li>Billing rules, claim workflow and reimbursement</li>
                <li>HIPAA, compliance and avoiding denials</li>
              </ul>
            </div>
          </details>
          <details class="faq-item">
            <summary>Upon completion, students will be able to&hellip;</summary>
            <div class="faq-body">
              <ul class="arrow-list">
                <li>Read clinical documentation and assign accurate diagnosis and procedure codes</li>
                <li>Build clean, complete insurance claims</li>
                <li>Apply payer rules and billing guidelines to support reimbursement</li>
                <li>Identify documentation errors that lead to denials</li>
                <li>Apply HIPAA privacy and compliance basics</li>
                <li>Be prepared to sit for the AAPC CPC and CPB exams</li>
              </ul>
            </div>
          </details>
          </div>
        </div>
      </div>
    </section>

""" + cta("Ready to start your healthcare career?", "Get in Touch")))


# ---- skilled-trades.html --------------------------------------------------
PAGES.append(dict(
    slug="skilled-trades.html", nav="our-programs.html",
    title="Skilled Trades Training | Career Skills Center",
    ogtitle="Skilled Trades",
    desc="Hands-on skilled trades training &mdash; electrical, HVAC/R, plumbing, welding and carpentry &mdash; at Career Skills Center in Massachusetts. Program details coming soon.",
    main=hero("Skilled Trades", "Skilled Trades",
              "The trades are hiring. Electricians, HVAC technicians, welders and plumbers are in demand "
              "across Massachusetts. Get the hands-on training and safety credentials employers and "
              "licensing boards ask for.",
              "images/trades.webp", ("How to Enroll", "admissions.html")) + """

    <section class="section section--alt">
      <div class="container coming-soon">
        <p class="cs-badge">Skilled Trades</p>
        <h2 class="section-title">Coming Soon</h2>
        <p class="lede">Our hands-on skilled trades programs &mdash; Electrical, HVAC/R, Plumbing, Welding and
        Carpentry &mdash; are being finalized. Check back soon for program details, start dates and
        enrollment. Want to be the first to know when they launch? Get in touch and we&rsquo;ll reach out.</p>
      </div>
    </section>

""" + cta("Ready to start your career?", "Get in Touch")))


# ---- admissions.html ------------------------------------------------------
PAGES.append(dict(
    slug="admissions.html", nav="admissions.html",
    title="Admissions | Career Skills Center — Massachusetts",
    ogtitle="Admissions",
    desc="How to enroll at Career Skills Center in Massachusetts. Requirements, documents, funding options and start dates.",
    main=hero("Admissions", "Admissions",
              "Getting started is simple. Call, get qualified, enroll. Our team walks you through every "
              "step, including how to pay for it.",
              "images/hero3.webp") + f"""

{STEPS}

    <section class="section">
      <div class="container">
        <div class="split-grid">
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Requirements</p>
            <h2 class="section-title left">Who Can Enroll</h2>
            <p>We keep requirements straightforward. If you are unsure whether you qualify, call us at
            <a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a> and we will tell you in a few
            minutes.</p>
            <ul class="check-list">
              <li><strong>Be 18 or older</strong>Applicants who are 17 may enroll with a parent or guardian signature.</li>
              <li><strong>High school diploma or GED</strong>Required for most programs. Ask us about options if you do not have one yet.</li>
              <li><strong>Valid government-issued photo ID</strong>Driver’s license, state ID or passport.</li>
              <li><strong>Enrollment interview</strong>A short conversation about your goals, schedule and funding.</li>
              <li><strong>Program prerequisites</strong>Some medical programs require immunization records and a background check.</li>
            </ul>
          </div>
          <div class="split-media">
            <img src="images/person2.webp" alt="Career Skills Center student" loading="lazy" decoding="async">
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Paying For It</p>
        <h2 class="section-title left">Funding Your Training</h2>
        <div class="section-intro">
          <p>Most students use more than one source. Our enrollment team will help you find every option you
          qualify for before you commit to anything.</p>
        </div>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Tuition</h3>
            <p>Clear, upfront pricing per program with no hidden fees.</p>
            <a class="read-more" href="tuition.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
          <article class="feature">
            <h3 class="feature-title">Student Financing</h3>
            <p>Monthly payment plans and third-party lending partners.</p>
            <a class="read-more" href="student-financing.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Start Dates</p>
        <h2 class="section-title left">When You Can Begin</h2>
        <div class="section-intro">
          <p>New cohorts start on a rolling basis. Seats are limited, so the earlier you qualify the more
          choice you have over your schedule.</p>
        </div>
        <div class="table-wrap">
          <table class="data-table">
            <caption class="sr-only">Upcoming program start dates</caption>
            <thead>
              <tr><th scope="col">Program area</th><th scope="col">Next start</th><th scope="col">Schedule</th><th scope="col">Seats</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Skilled Trades</th><td class="tbd">TBD</td><td class="tbd">Day / Evening — TBD</td><td class="tbd">TBD</td></tr>
              <tr><th scope="row">Information Technology</th><td class="tbd">TBD</td><td class="tbd">Day / Evening — TBD</td><td class="tbd">TBD</td></tr>
              <tr><th scope="row">Medical</th><td class="tbd">TBD</td><td class="tbd">Day / Evening — TBD</td><td class="tbd">TBD</td></tr>
            </tbody>
          </table>
        </div>
        <p class="note"><strong>Placeholder.</strong> Replace the TBD cells with the real term calendar once
        cohort dates and class schedules are set.</p>
      </div>
    </section>

""" + cta("Ready to apply?")))


# ---- tuition.html ---------------------------------------------------------
PAGES.append(dict(
    slug="tuition.html", nav="tuition.html",
    title="Tuition | Career Skills Center — Massachusetts",
    ogtitle="Tuition",
    desc="Affordable, upfront tuition for trade, IT and medical training at Career Skills Center in Massachusetts.",
    main=hero("Tuition", "Tuition",
              "Clear, upfront pricing with no surprises, plus help finding every funding source you "
              "qualify for.",
              "images/tuition-hero.webp") + f"""

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Competitive Pricing</p>
        <h2 class="section-title left">An Education You Can Afford</h2>
        <div class="section-intro">
          <p>With student loan debt in the United States now measured in the trillions, more people are
          questioning the price of a traditional degree. Affordability drives how we price every course at
          Career Skills Center. Our tuition is lower than most career schools, and we work to connect
          students with every available funding source so training does not leave you buried in debt.</p>
          <p>Short programs also mean you stop paying sooner and start earning sooner. That combination,
          lower cost and less time out of the workforce, is what makes career training a strong return.</p>
        </div>

        <div class="table-wrap">
          <table class="data-table">
            <caption class="sr-only">Tuition and fees by program</caption>
            <thead>
              <tr>
                <th scope="col">Program</th><th scope="col">Length</th><th scope="col">Tuition</th>
                <th scope="col">Books &amp; supplies</th><th scope="col">Exam fees</th><th scope="col">Total</th>
              </tr>
            </thead>
            <tbody>
              <tr class="group"><td colspan="6">Skilled Trades</td></tr>
              <tr><th scope="row">Electrical Technician</th><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td></tr>
              <tr><th scope="row">HVAC/R Technician</th><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td></tr>
              <tr><th scope="row">Plumbing Technician</th><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td></tr>
              <tr><th scope="row">Welding</th><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td></tr>
              <tr><th scope="row">Carpentry &amp; Construction</th><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td><td class="tbd">TBD</td></tr>

              <tr class="group"><td colspan="6">Information Technology</td></tr>
              <tr><th scope="row">IT Support Specialist</th><td>89 hours</td><td>$299</td><td>Yes</td><td>Free</td><td>$299</td></tr>

              <tr class="group"><td colspan="6">Medical</td></tr>
              <tr><th scope="row">Medical Billing &amp; Coding</th><td>117 hours</td><td>$329</td><td>Yes</td><td>Free</td><td>$329</td></tr>
            </tbody>
          </table>
        </div>
        <p class="note"><strong>Placeholder pricing.</strong> Every figure above is marked TBD on purpose. Do
        not publish this page until real tuition, fees and program lengths are confirmed — advertised prices
        are a regulated disclosure.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split-grid">
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>What You Get</p>
            <h2 class="section-title left">What’s Included</h2>
            <ul class="check-list">
              <li><strong>Instruction and lab time</strong>All classroom hours, shop and lab sessions with your instructor.</li>
              <li><strong>Course materials</strong>Textbooks, workbooks and consumable lab materials for your program.</li>
              <li><strong>Certification exam preparation</strong>Practice exams and review built into the course.</li>
              <li><strong>Career services</strong>Resume help, mock interviews and employer introductions, before and after you finish.</li>
              <li><strong>Ongoing support</strong>Access to Career Services after graduation at no additional cost.</li>
            </ul>
          </div>
          <div class="split-media">
            <img src="images/person1.webp" alt="Career Skills Center graduate" loading="lazy" decoding="async">
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Find Your Fit</p>
        <h2 class="section-title left">Ways to Pay</h2>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Self Pay</h3>
            <p>We accept credit card and ACH payments. Call us or use the Get in Touch button for details.</p>
            <a class="read-more" href="contact.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
          <article class="feature">
            <h3 class="feature-title">Payment Plans</h3>
            <p>Split your tuition into monthly payments, or apply through a financing partner.</p>
            <a class="read-more" href="student-financing.html"><span class="arrow" aria-hidden="true"></span> Read more</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <h2 class="section-title">A Great Return on Your Investment</h2>
        <div class="table-wrap">
          <table class="data-table compare-table">
            <thead>
              <tr>
                <th scope="col" class="compare-corner"></th>
                <th scope="col" class="compare-us">Career Skills Center</th>
                <th scope="col">Four-Year University</th>
                <th scope="col">Two-Year College</th>
              </tr>
            </thead>
            <tbody>
              <tr><th scope="row">Average time to complete</th><td class="compare-us-cell">3 months</td><td>5.2 years</td><td>3.4 years</td></tr>
              <tr><th scope="row">Average tuition and fees</th><td class="compare-us-cell">$299 to $329</td><td>$103,000</td><td>$39,000</td></tr>
              <tr><th scope="row">Education cost + lost income</th><td class="compare-us-cell">$36,000</td><td>$261,120</td><td>$141,461</td></tr>
              <tr><th scope="row">Median compensation</th><td class="compare-us-cell">$42,000</td><td>$47,000</td><td>$38,600</td></tr>
              <tr><th scope="row">Time to recover investment</th><td class="compare-us-cell">1 year</td><td>4.7 years</td><td>3.7 years</td></tr>
            </tbody>
          </table>
        </div>
        <p class="note"><strong>Placeholder comparison.</strong> Confirm and source every figure before publishing. The tuition range shown here does not yet match the program catalog above.</p>
      </div>
    </section>

""" + cta("Call today to see how you may qualify.")))


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
    title="Student Financing | Career Skills Center — Massachusetts",
    ogtitle="Student Financing",
    desc="Monthly payment plans and lending partners that make Career Skills Center training affordable.",
    main=hero("Student Financing", "Student Financing",
              "Funding made simple. Invest in your future with a payment plan that fits your budget.",
              "images/hero2.webp") + f"""

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Overview</p>
        <h2 class="section-title left">Financing for Your Future</h2>
        <div class="section-intro">
          <p>Now is a good time to start a career with in-demand skills. If paying tuition up front is not
          realistic, financing lets you spread the cost over time and start training sooner.</p>
          <p>We offer an in-house payment plan, and we can refer you to lending partners who specialize in
          career-focused programs. Our enrollment team will walk you through the numbers before you sign
          anything, so you know exactly what you are committing to.</p>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split-grid">
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Payment Plans</p>
            <h2 class="section-title left">Pay Monthly, Start Now</h2>
            <p>Our in-house plan splits your balance into monthly installments across the length of your
            program. There is no credit check for the standard plan and no prepayment penalty if you decide
            to pay it off early.</p>
            <ul class="check-list">
              <li><strong>Deposit to reserve your seat</strong><span class="tbd">Amount: TBD</span></li>
              <li><strong>Monthly installments</strong><span class="tbd">Term length and amount: TBD</span></li>
              <li><strong>No prepayment penalty</strong>Pay ahead or pay off in full at any time.</li>
              <li><strong>Interest terms</strong><span class="tbd">TBD — confirm before publishing.</span></li>
            </ul>
          </div>
          <div class="split-media">
            <img src="images/aboutus.webp" alt="Career Skills Center office" loading="lazy" decoding="async">
          </div>
        </div>
        <p class="note"><strong>Placeholder terms.</strong> Payment plan amounts, term lengths and any
        interest or finance charges must be confirmed and disclosed accurately before this page goes live.
        Consumer lending disclosures are regulated.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Lending Partners</p>
        <h2 class="section-title left">Third-Party Financing</h2>
        <div class="section-intro">
          <p>For students who prefer a longer term, outside lenders offer loans built for career training
          rather than four-year degrees. Applications are typically short and many lenders can pre-qualify
          you with a soft credit check that does not affect your score.</p>
        </div>
        <div class="logo-strip">
          <div class="logo-slot">Lender logo</div>
          <div class="logo-slot">Lender logo</div>
          <div class="logo-slot">Lender logo</div>
          <div class="logo-slot">Lender logo</div>
        </div>
        <p class="note"><strong>Placeholder.</strong> Add lending partners once agreements are in place, along
        with this required style of disclosure: Career Skills Center does not endorse any particular
        lender and is not affiliated with them. Check rates and terms directly with the lender.</p>
      </div>
    </section>

""" + cta("Ready to see if you qualify?", "Talk to an Advisor")))


# ---- about.html -----------------------------------------------------------
PAGES.append(dict(
    slug="about.html", nav="about.html",
    title="About Us | Career Skills Center — Massachusetts",
    ogtitle="About Career Skills Center",
    desc="Career Skills Center is a career school in Massachusetts training students for the skilled trades, IT and the medical field.",
    main=hero("About Us", "About Us",
              "A career school built for Massachusetts, with online and hands-on training options. "
              "Our focus is your potential.",
              "images/aboutus.webp") + f"""

    <section class="section">
      <div class="container narrow text-center">
        <h2 class="section-title">Our Focus: Your Potential</h2>
        <p class="lede">Our goal isn’t just to help you achieve your potential. It’s to <strong>activate your
        potential</strong>. Career Skills Center prepares committed students for rewarding careers through
        high-caliber training, hands-on experience and student-focused support.</p>
        <p class="lede">Employers today expect more than knowledge and technical skill. They look for
        discipline, integrity, teamwork and the professionalism that defines someone worth hiring. We take on
        the work of building those habits alongside the trade itself.</p>
      </div>
      <div class="container narrow">
        <blockquote class="quote-block">
          <p>It is better to be prepared for an opportunity and not have one than to have an opportunity and
          not be prepared.</p>
          <cite>Les Brown</cite>
        </blockquote>
      </div>
    </section>

    <section class="about section section--alt" id="mission">
      <div class="container about-grid">
        <div class="about-media">
          <div class="deco-dots deco-dots--about" aria-hidden="true"></div>
          <img src="images/aboutus.webp" alt="Training and meeting space at Career Skills Center" loading="lazy" decoding="async">
        </div>
        <div class="about-copy">
          <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Our Mission</p>
          <h2 class="section-title left">Our Mission</h2>
          <p>We believe that a well-trained workforce contributes to the economic and social vibrancy of the
          Massachusetts communities in which our students, instructors, and
          staff live. To accomplish our mission, we are committed to providing a <strong>caring learning
          environment</strong> where a <strong>technically rich, hands-on, quality education</strong> is
          delivered by professionals who have worked in the field.</p>
          <ul class="arrow-list">
            <li>Flexible schedules to help you reach your potential</li>
            <li>Knowledgeable instructors to support you along the way</li>
            <li>In-demand trade, IT, and medical programs to keep you motivated</li>
            <li>Structured courses to facilitate your success</li>
            <li>Ongoing partnership to assist in your career journey</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Your Success Is</p>
        <h2 class="section-title left">Our Purpose</h2>
        <div class="section-intro">
          <p>Our reason for existing is to support and advance people through meaningful education and real
          relationships. These are the values we hold ourselves to.</p>
        </div>
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Hands-On Learning</h3>
            <p>You learn the work by doing the work. Lab and shop time is not an add-on, it is the course.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Student Support</h3>
            <p>Small cohorts, accessible instructors, and staff who know your name and your goals.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Industry Relevance</h3>
            <p>Programs built around the credentials and skills local employers actually hire for.</p>
          </article>
        </div>
        <div class="feature-grid" style="margin-top: 40px;">
          <article class="feature">
            <h3 class="feature-title">Integrity</h3>
            <p>Straight answers about cost, length and outcomes. No pressure and no surprises.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Growth Mindset</h3>
            <p>Every student starts somewhere. Effort and coaching close the gap faster than talent alone.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Community</h3>
            <p>We train people who stay and work here, strengthening the neighborhoods we all live in.</p>
          </article>
        </div>
      </div>
    </section>

""" + cta("Want to know what we can do for you?")))


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
    desc="Resume help, interview preparation, employer connections and job search support for Career Skills Center students and graduates.",
    main=hero("Career Services", "Career Services",
              "Get certified. Begin your career. Our work does not stop when the course does.",
              "images/person1.webp") + f"""

    <section class="section">
      <div class="container narrow text-center">
        <h2 class="section-title">Beyond the Classroom</h2>
        <p class="lede">At Career Skills Center we want to see our students reach their goals, not just in
        the curriculum but in the industry they trained for. Career Services works with every student through
        completion and stays available afterward.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="feature-grid">
          <article class="feature">
            <h3 class="feature-title">Resume Assistance</h3>
            <p>We help you design and write a resume that puts your new credentials first, and we review
            employment applications with you before you send them.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Interview Preparation</h3>
            <p>Mock interviews, advice on professional appearance, and guidance on how to follow up after an
            interview.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Employer Connections</h3>
            <p>Introductions to local contractors, clinics and IT departments who hire from our programs.</p>
          </article>
        </div>
        <div class="feature-grid" style="margin-top: 40px;">
          <article class="feature">
            <h3 class="feature-title">Certification Exam Prep</h3>
            <p>Practice exams, review sessions and scheduling help so you sit for your credential while the
            material is fresh.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Job Fairs</h3>
            <p>On-site and regional hiring events where you meet employers face to face.</p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Alumni Network</h3>
            <p>Graduates stay connected, refer openings, and often come back to hire the next cohort.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split-grid">
          <div class="split-media">
            <img src="images/person2.webp" alt="Career Skills Center graduate" loading="lazy" decoding="async">
          </div>
          <div class="split-copy">
            <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Every Student</p>
            <h2 class="section-title left">Support for Everyone, Not a Waiting List</h2>
            <p>Our Career Services department is staffed to work with every student upon completion. You are
            not a number here and you will not wait in a queue to speak with someone. In many cases we reach
            out to you first.</p>
            <p>The goal is simple: that you feel supported, prepared and part of something that changes your
            situation for the better.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Outcomes</p>
        <h2 class="section-title left">By the Numbers</h2>
        <div class="stat-grid">
          <div class="stat-tile"><div class="stat-value">TBD</div><div class="stat-label">Placement rate</div></div>
          <div class="stat-tile"><div class="stat-value">TBD</div><div class="stat-label">Certification pass rate</div></div>
          <div class="stat-tile"><div class="stat-value">TBD</div><div class="stat-label">Employer partners</div></div>
          <div class="stat-tile"><div class="stat-value">TBD</div><div class="stat-label">Graduates to date</div></div>
        </div>
        <p class="note"><strong>Publish verified numbers only.</strong> Placement and completion rates are
        regulated disclosures. Leave these as TBD until the figures are documented and you can show the
        methodology behind them.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Common Questions</p>
        <h2 class="section-title left">Career Services FAQ</h2>
        <div class="faq">
          <p class="faq-group-title">General questions</p>
          <details class="faq-item">
            <summary>When should I start contacting a Career Services representative?</summary>
            <div class="faq-body"><p>Earlier than most students think. Reach out as soon as you are partway
            through your program so your resume and interview prep are ready the week you finish.</p></div>
          </details>
          <details class="faq-item">
            <summary>Do I have to contact Career Services, or will they contact me?</summary>
            <div class="faq-body"><p>Both. We reach out to students as they approach completion, and you are
            welcome to come to us at any point before that.</p></div>
          </details>
          <details class="faq-item">
            <summary>Do I have to pay for help from Career Services?</summary>
            <div class="faq-body"><p>No. Career Services is included in your tuition, during your program and
            after you graduate.</p></div>
          </details>

          <p class="faq-group-title">After you finish</p>
          <details class="faq-item">
            <summary>How will Career Services help me find work in my field?</summary>
            <div class="faq-body"><p>We help target your search to employers hiring for your credential, refer
            you into openings we know about, prepare you for the interview, and coach you through offers.</p></div>
          </details>
          <details class="faq-item">
            <summary>How many times can I come back for help?</summary>
            <div class="faq-body"><p>As many as you need. Graduates use us again years later when they are
            ready for the next move, and that is exactly what we are here for.</p></div>
          </details>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container narrow text-center">
        <h2 class="section-title">For Employers</h2>
        <p class="lede">Hiring? Our graduates arrive with current credentials, safety training and hands-on
        practice. Tell us what you need and we will connect you with candidates from the next cohort.</p>
        <p><button class="btn btn-navy js-open-contact" type="button">Hire Our Graduates</button></p>
      </div>
    </section>

""" + cta("Ready to start your career?")))


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
    desc="Answers about programs, admissions, tuition, schedules and career services at Career Skills Center in Massachusetts.",
    main=hero("FAQ", "Find Answers",
              "The questions we hear most, answered plainly. If yours is not here, call us at "
              "(617) 544-7155.",
              "images/hero3.webp") + f"""

    <section class="section">
      <div class="container">
        <div class="faq">

          <p class="faq-group-title">Programs</p>
{faq("How long are your programs?", 'Program lengths vary by field. <span class="tbd">Exact lengths are TBD until the course catalog is final.</span> Career training is measured in weeks and months rather than years, which is the point: you finish sooner and start earning sooner.')}
{faq("Are classes in person?", "Yes. Trade, medical and IT programs all include hands-on lab or shop time at our Quincy campus, because the skills employers test for cannot be learned from video alone.")}
{faq("Do you offer evening or weekend classes?", 'We plan to offer schedules that work around a job. <span class="tbd">Final day, evening and weekend options are TBD.</span> Ask your enrollment advisor which cohorts fit your availability.')}
{faq("Do I need experience to start?", "No. Our programs are built for people starting from zero, including career changers who have been out of school for years. Every skilled tradesperson started exactly where you are.")}
{faq("What certifications will I earn?", "It depends on the program: EPA 608 and OSHA 10 for trades, CompTIA A+, Network+ or Security+ for IT, and CCMA, CPT, CET or CBCS preparation for medical. Your advisor will confirm which credential your program prepares you for.")}

          <p class="faq-group-title">Admissions</p>
{faq("What do I need to enroll?", 'Generally you need to be 18 or older, have a high school diploma or GED, and bring a valid photo ID. Some medical programs also require immunization records and a background check. See <a class="link-yellow" href="admissions.html">Admissions</a> for the full list.')}
{faq("What if I was not great at school?", "Career training is different from traditional academics. It is practical, short, and focused on one skill set at a time, with instructors who work the trade. Plenty of our students did not enjoy high school and do well here.")}
{faq("How do I get started?", 'Call <a class="link-yellow" href="tel:+16175447155">(617) 544-7155</a> or use the Get in Touch button. The first conversation takes a few minutes and costs nothing.')}

          <p class="faq-group-title">Tuition &amp; funding</p>
{faq("How much does it cost?", 'Tuition varies by program. <span class="tbd">Pricing is TBD until the catalog is final.</span> We price for affordability and we will tell you the full cost, including books and exam fees, before you enroll.')}
{faq("What if I cannot afford the tuition?", 'Most students combine sources. We offer payment plans and third-party financing partners, and our enrollment team will help you find every option you qualify for. See <a class="link-yellow" href="student-financing.html">Student Financing</a>.')}
{faq("Do you accept VA benefits?", '<span class="tbd">TBD.</span> Approval to accept veterans education benefits must be granted before we can advertise it. Call us and we will tell you our current status.')}
{faq("Is financial aid available?", 'We will walk you through every funding option you may qualify for, including payment plans and third-party financing partners. Call us and we will tell you what is currently available.')}

          <p class="faq-group-title">Career services</p>
{faq("Do you help with job placement?", 'Yes. Resume help, mock interviews, employer introductions and job search support are included in your tuition, during the program and after you graduate. See <a class="link-yellow" href="career-services.html">Career Services</a>.')}
{faq("Will employers hire me with a certificate instead of a degree?", "In the trades, IT and allied health, employers hire on credentials and demonstrated skill. A current certification plus hands-on training is what gets you through the door for these roles.")}
{faq("What happens after I finish?", "You sit for your certification exam, work with Career Services on your search, and stay connected to us afterward. Graduates come back years later for help with their next move.")}

          <p class="faq-group-title">Location &amp; schedule</p>
{faq("Where are you located?", 'Quincy, MA 02171. The campus is convenient to the South Shore and reachable on the MBTA Red Line.')}
{faq("Is parking available?", '<span class="tbd">TBD — confirm parking and transit details once the campus address is final.</span>')}

        </div>
      </div>
    </section>

""" + cta("Still have questions? Call (617) 544-7155.")))


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

BLOG_POSTS = [
    ("Skilled Trades", "Sep 8, 2026", "6 min read",
     "Electrician, HVAC, or Plumbing: Which Trade Pays Off Fastest?",
     "The three biggest trades in Massachusetts all pay well, but they differ in training length, "
     "licensing, and day-to-day work. Here is how to choose."),
    ("Information Technology", "Sep 2, 2026", "5 min read",
     "The Fastest Way Into an IT Career Without a Degree",
     "Employers in tech hire on certifications and demonstrated skill. Here is the shortest honest path "
     "from zero to your first help-desk role."),
    ("Medical", "Aug 26, 2026", "4 min read",
     "What a Medical Assistant Actually Does All Day",
     "Vitals, patient intake, scheduling, and a lot of people skills. A realistic look at the role before "
     "you commit to the training."),
    ("Admissions", "Aug 19, 2026", "5 min read",
     "Day Classes vs. Evening Classes: Picking a Schedule That Sticks",
     "The best schedule is the one you can actually finish. How to weigh work, family, and focus before "
     "you enroll."),
    ("Career Advice", "Aug 12, 2026", "7 min read",
     "5 Questions to Ask Before You Enroll in Any Career Program",
     "Not every program is worth the time or money. These five questions separate real career training "
     "from an expensive detour."),
    ("Financial Aid", "Aug 5, 2026", "6 min read",
     "Paying for Training: Grants, Plans, and What Actually Works",
     "Between workforce grants, payment plans, and employer help, most students combine sources. Here is "
     "how to stack them."),
]

PAGES.append(dict(
    slug="blog.html", nav="blog.html",
    title="Blog | Career Skills Center — Massachusetts",
    ogtitle="Career Skills Center Blog",
    desc="Guidance on training, careers, and funding in the skilled trades, IT, and healthcare from the team at Career Skills Center.",
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
          <a class="filter-pill" href="#" role="listitem">Skilled Trades</a>
          <a class="filter-pill" href="#" role="listitem">Information Technology</a>
          <a class="filter-pill" href="#" role="listitem">Medical</a>
          <a class="filter-pill" href="#" role="listitem">Admissions &amp; Funding</a>
          <a class="filter-pill" href="#" role="listitem">Career Advice</a>
        </div>

        <!-- Featured / most recent article -->
        <a class="post-featured" href="#">
          <p class="post-meta"><span class="post-tag">Career Advice</span></p>
          <p class="post-meta">Sep 16, 2026<span class="dot-sep"></span>8 min read</p>
          <h2>How to Choose a Career Training Program That Actually Leads to a Job</h2>
          <p>What separates real, job-focused training from an expensive detour: the credentials that matter,
          the questions to ask before you enroll, and how to tell whether a program's graduates are actually
          getting hired.</p>
          <span class="read-link">Read article</span>
        </a>

        <div class="post-grid">
{chr(10).join(post_card(*p) for p in BLOG_POSTS)}
        </div>

        <div class="blog-more">
          <!-- Static for now; becomes pagination or "load more" when the archive grows. -->
          <button class="btn btn-navy" type="button" disabled>More articles coming soon</button>
        </div>

        <p class="note"><strong>Placeholder content.</strong> The headlines and summaries above are drafts to
        show the layout. Real articles replace them one at a time as they are written.</p>
      </div>
    </section>

""" + cta("Have a topic you want us to cover?", "Get in Touch")))


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

          <!-- TODO: point action at the form backend and remove the demo handler in js/main.js. -->
          <form class="contact-form" id="contact-page-form" action="#" method="post" novalidate>
            <label class="sr-only" for="cp-name">First and Last Name</label>
            <input id="cp-name" name="name" type="text" placeholder="First and Last Name" autocomplete="name" required>

            <label class="sr-only" for="cp-phone">Phone Number</label>
            <input id="cp-phone" name="phone" type="tel" placeholder="Phone Number" autocomplete="tel" required>

            <label class="sr-only" for="cp-email">Email Address</label>
            <input id="cp-email" name="email" type="email" placeholder="Email Address" autocomplete="email" required>

            <label class="sr-only" for="cp-program">Program of interest</label>
            <select id="cp-program" name="program" required>
              <option value="" selected disabled>Program of interest</option>
              <option value="trades">Skilled Trades</option>
              <option value="it">Information Technology</option>
              <option value="medical">Medical</option>
              <option value="unsure">Not sure yet</option>
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
      <div class="container">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Visit</p>
        <h2 class="section-title left">Find Us in Quincy</h2>
        <div class="map-placeholder">Map embed placeholder — add a Google Maps iframe once the street address is final</div>
        <div class="feature-grid" style="margin-top: 48px;">
          <article class="feature">
            <h3 class="feature-title">By Car</h3>
            <p><span class="tbd">Directions and parking details TBD once the campus address is confirmed.</span></p>
          </article>
          <article class="feature">
            <h3 class="feature-title">By MBTA</h3>
            <p>Quincy is served by the MBTA Red Line. <span class="tbd">Confirm the nearest station and
            walking time once the address is set.</span></p>
          </article>
          <article class="feature">
            <h3 class="feature-title">Office Hours</h3>
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
        <p>When you contact us, request information or enroll, we may collect your name, phone number, email
        address, mailing address, program of interest and any information you choose to include in a message.
        Students provide additional records required for enrollment and funding.</p>

        <h2>How we use your information</h2>
        <ul>
          <li>To respond to your inquiry and discuss programs with you</li>
          <li>To process enrollment, funding applications and student records</li>
          <li>To provide career services during and after your program</li>
          <li>To send information about programs, start dates and events</li>
          <li>To meet legal, accreditation and reporting obligations</li>
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
        <p><span class="tbd">Describe any analytics, advertising or tracking tools in use once they are
        configured.</span></p>

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


# ---- terms-of-use.html ----------------------------------------------------
PAGES.append(dict(
    slug="terms-of-use.html", nav=None,
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
for page in PAGES:
    if page["slug"] in ARCHIVED:
        print("skipped (archived)", page["slug"])
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
            .replace("@@HEADER@@", header)
            .replace("@@FOOTER@@", footer)
            .replace("@@DIALOG@@", DIALOG)
            .replace("@@MAIN@@", page["main"])
            .replace("@@CSSVER@@", CSS_VER)
            .replace("@@JSVER@@", JS_VER))

    (ROOT / page["slug"]).write_text(html, encoding="utf-8")
    print("wrote", page["slug"], len(html), "bytes")
    written += 1

print("\n%d pages written." % written)

# ---------------------------------------------------------------------------
# SITEMAP  (auto-lists live public pages so search engines / AI can crawl)
# ---------------------------------------------------------------------------
SITE = "https://careerskillscenter.com/"
# Unlinked / deprecated pages kept on disk but left out of the sitemap.
SITEMAP_EXCLUDE = {"programs.html", "team.html", "media.html"}
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
