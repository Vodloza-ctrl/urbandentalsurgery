# -*- coding: utf-8 -*-
import os
OUT = os.path.dirname(os.path.abspath(__file__))

services = [
    {"icon": "ic-sparkle-tooth", "title": "Teeth Cleaning",
     "short": "Professional scale and polish to clear plaque and tartar and keep gums healthy.",
     "long": "Professional scale and polish to clear plaque and tartar buildup that brushing alone can't reach. Regular cleaning keeps your gums healthy, freshens breath, and catches small problems before they grow &mdash; recommended as part of a routine check-up."},
    {"icon": "ic-drop", "title": "Fillings",
     "short": "Tooth-coloured fillings that treat decay early and restore natural strength.",
     "long": "Comfortable, tooth-coloured fillings that treat decay while it's still small. We remove the affected area and rebuild the tooth so it looks natural and bites the way it should &mdash; often finished in a single visit."},
    {"icon": "ic-root", "title": "Root Canal Treatment",
     "short": "Gentle care that relieves pain and saves a damaged or infected tooth.",
     "long": "When decay or infection reaches the nerve, root canal treatment removes the source of pain and saves the natural tooth rather than removing it. The procedure is done under local anaesthetic and finished with a protective restoration."},
    {"icon": "ic-bridge", "title": "Tooth Replacement",
     "short": "Bridges, crowns and restorations that bring back full function.",
     "long": "Missing or badly damaged teeth affect chewing, speech and confidence. We assess your bite and recommend the right restoration &mdash; bridge, crown, or partial replacement &mdash; to close the gap and restore full function."},
    {"icon": "ic-tooth", "title": "Teeth Whitening",
     "short": "A safe, in-chair treatment for a noticeably brighter smile.",
     "long": "A supervised, in-chair whitening treatment designed to lift stains and brighten your smile safely, with results tailored to your natural shade rather than a one-size-fits-all approach."},
]

values = [
    {"icon": "ic-heart", "title": "Comfort first",
     "body": "Every visit is paced around you &mdash; clear explanations before any treatment, in a room designed to feel calm rather than clinical."},
    {"icon": "ic-tool", "title": "Modern equipment",
     "body": "The practice is fitted with current dental chairs and instruments, kept to a consistent standard of hygiene between every patient."},
    {"icon": "ic-shield", "title": "Personal attention",
     "body": "As a focused practice in Nkulumane, appointments aren't rushed &mdash; you see the same care and attention to detail on every visit."},
]

ICON_DEFS = """
<svg width="0" height="0" style="position:absolute">
  <defs>
    <symbol id="ic-tooth" viewBox="0 0 48 48"><path d="M24 6c-5 0-7 3-9 3-3 0-6-2-9-2-1 8 2 12 3 20 1 7 3 15 6 15 3 0 3-9 5-9s2 9 5 9c3 0 5-8 6-15 1-8 4-12 3-20-3 0-6 2-9 2-2 0-4-3-9-3z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></symbol>
    <symbol id="ic-sparkle-tooth" viewBox="0 0 48 48"><path d="M22 10c-4.5 0-6.3 2.6-8 2.6-2.7 0-5.4-1.8-8-1.8-.9 7.2 1.8 10.8 2.7 18 .9 6.3 2.7 13.5 5.4 13.5 2.7 0 2.7-8.1 4.5-8.1s1.8 8.1 4.5 8.1c2.7 0 4.5-7.2 5.4-13.5.9-7.2 3.6-10.8 2.7-18-2.6 0-5.3 1.8-8 1.8-1 0-1.8-.8-1.2-2.6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" transform="translate(1,0)"/><path d="M38 6l1.4 3.6L43 11l-3.6 1.4L38 16l-1.4-3.6L33 11l3.6-1.4z" fill="currentColor"/><path d="M41 20l.9 2.1 2.1.9-2.1.9-.9 2.1-.9-2.1-2.1-.9 2.1-.9z" fill="currentColor"/></symbol>
    <symbol id="ic-drop" viewBox="0 0 48 48"><path d="M24 6c8 10 14 18 14 26a14 14 0 1 1-28 0c0-8 6-16 14-26z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M17 32c0-4 2-7 5-9" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></symbol>
    <symbol id="ic-root" viewBox="0 0 48 48"><path d="M16 8h16v10c0 3-2 4-2 8v4l3 12-4 1-3-10-2 5-2-5-3 10-4-1 3-12v-4c0-4-2-5-2-8z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></symbol>
    <symbol id="ic-bridge" viewBox="0 0 48 48"><rect x="6" y="20" width="10" height="16" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="19" y="12" width="10" height="24" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="32" y="20" width="10" height="16" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M6 20c4-4 8-4 10 0M29 12c4-8 9-8 13 0" fill="none" stroke="currentColor" stroke-width="1.4" stroke-dasharray="2 3"/></symbol>
    <symbol id="ic-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 7v5l3.5 2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol>
    <symbol id="ic-pin" viewBox="0 0 24 24"><path d="M12 21s7-7.5 7-12.5A7 7 0 1 0 5 8.5C5 13.5 12 21 12 21z" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="8.5" r="2.4" fill="none" stroke="currentColor" stroke-width="1.6"/></symbol>
    <symbol id="ic-phone" viewBox="0 0 24 24"><path d="M6.5 3h3l1.5 5-2.3 1.8a13 13 0 0 0 5.5 5.5L16 13l5 1.5v3a2 2 0 0 1-2.2 2A17 17 0 0 1 4.5 5.2 2 2 0 0 1 6.5 3z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></symbol>
    <symbol id="ic-mail" viewBox="0 0 24 24"><rect x="3" y="5.5" width="18" height="13" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M4 7l8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></symbol>
    <symbol id="ic-whatsapp" viewBox="0 0 24 24"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.7-1.2A9 9 0 1 0 12 3z" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8.3 8.6c.2-.5.5-.5.8-.5h.6c.2 0 .5 0 .7.5s.8 1.9.8 2 .1.3 0 .5-.2.3-.4.5-.4.5-.5.6c-.2.2-.4.4-.2.8.3.5 1.1 1.6 2.3 2.6 1.6 1.3 2.3 1.4 2.6 1.4.3 0 .5-.2.7-.5l.5-.8c.2-.3.4-.3.7-.2l1.9.9c.3.1.5.2.5.4 0 .8-.3 1.6-1.3 2.1-.9.5-1.8.5-2.8.2-1.7-.5-3.6-1.7-5-3.5-1-1.3-1.6-2.6-1.7-3.9-.1-1 .2-1.8.8-2.5z" fill="currentColor" stroke="none"/></symbol>
    <symbol id="ic-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></symbol>
    <symbol id="ic-shield" viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 5-3 8-7 9-4-1-7-4-7-9V6z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 12l2 2 4-4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
    <symbol id="ic-heart" viewBox="0 0 24 24"><path d="M12 20s-7-4.4-9.3-8.7C1.3 8 3 5 6.3 5 8.6 5 10.7 6.4 12 8.4 13.3 6.4 15.4 5 17.7 5 21 5 22.7 8 21.3 11.3 19 15.6 12 20 12 20z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></symbol>
    <symbol id="ic-tool" viewBox="0 0 24 24"><path d="M14.5 6.5a4 4 0 0 0-5.4 4.9L3 17.5 5.5 20l6-6.1a4 4 0 0 0 4.9-5.4l-2.4 2.4-2-2z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></symbol>
  </defs>
</svg>
"""

def svc_cards():
    out = []
    for s in services:
        out.append(f'''
    <div class="svc-card" data-reveal>
      <div class="svc-badge"><svg><use href="#{s['icon']}"/></svg></div>
      <h3>{s['title']}</h3>
      <p>{s['short']}</p>
    </div>''')
    return "".join(out)

def svc_rows():
    out = []
    for s in services:
        out.append(f'''
    <div class="svc-row" data-reveal>
      <div class="svc-badge"><svg><use href="#{s['icon']}"/></svg></div>
      <div>
        <h3>{s['title']}</h3>
        <p>{s['long']}</p>
      </div>
    </div>''')
    return "".join(out)

def value_rows():
    out = []
    for v in values:
        out.append(f'''
    <div class="value-row">
      <div class="svc-badge"><svg><use href="#{v['icon']}"/></svg></div>
      <div><h4>{v['title']}</h4><p>{v['body']}</p></div>
    </div>''')
    return "".join(out)

NAV_ITEMS = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

def header(active):
    link_tags = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ''
        link_tags.append(f'<a href="{href}"{cls}>{label}</a>')
    links = "\n      ".join(link_tags)
    drawer_links = "\n    ".join(f'<a href="{href}">{label}</a>' for href, label in NAV_ITEMS)
    return f"""
<div class="announce">
  <div class="wrap">
    <span><b>Visit us today</b><span class="dot">&bull;</span>Walk-ins accepted</span>
    <a href="tel:+263714936261">Call Hotline: +263 71 493 6261</a>
  </div>
</div>
<header class="site">
  <div class="wrap nav">
    <a href="index.html" class="brand"><img src="img/logo-color.png" alt="Urban Dental Solutions"></a>
    <nav class="links" id="navLinks">
      {links}
    </nav>
    <div class="head-right">
      <a class="head-phone" href="tel:+263714936261"><svg viewBox="0 0 24 24"><use href="#ic-phone"/></svg>+263 71 493 6261</a>
      <a class="btn-pill navy" href="tel:+263714936261">Book Appointment</a>
      <button class="menu-btn" id="menuBtn" aria-label="Open menu"><span></span></button>
    </div>
  </div>
</header>

<div class="drawer" id="drawer">
  <div class="drawer-panel">
    <button class="drawer-close" id="drawerClose" aria-label="Close menu">&times;</button>
    {drawer_links}
    <a href="tel:+263714936261" style="margin-top:16px;color:#0878A6;font-weight:600;">Call +263 71 493 6261</a>
  </div>
</div>
"""

FOOTER = """
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-brand"><img src="img/logo-white.png" alt="Urban Dental Solutions"></div>
        <p>General dentistry in Nkulumane, Bulawayo &mdash; cleaning, fillings, root canal treatment, tooth replacement and whitening, delivered with confidence, care and community.</p>
      </div>
      <div>
        <h5>NAVIGATE</h5>
        <div class="flinks">
          <a href="index.html">Home</a>
          <a href="services.html">Services</a>
          <a href="about.html">About</a>
          <a href="contact.html">Contact</a>
        </div>
      </div>
      <div>
        <h5>GET IN TOUCH</h5>
        <div class="flinks">
          <a href="tel:+263714936261">+263 71 493 6261</a>
          <a href="tel:+263784599794">+263 78 459 9794</a>
          <a href="mailto:urbandental3@gmail.com">urbandental3@gmail.com</a>
          <a href="contact.html">14818 Nkulumane 12 Medical Centre, Bulawayo</a>
        </div>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="yr"></span> Urban Dental Solutions. Nkulumane 12 Medical Centre, Bulawayo.</span>
      <span>Mon &ndash; Fri, 8am &ndash; 5pm &bull; Walk-ins accepted</span>
    </div>
  </div>
</footer>
"""

def page_shell(title, description, active, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>%F0%9F%A6%B7</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
{ICON_DEFS}
{header(active)}
<main>
{body}
</main>
{FOOTER}
<script src="js/main.js"></script>
</body>
</html>
"""

# ---------------- HOME ----------------
home_body = f"""
    <div class="hero-section">
      <div class="wrap">
        <div class="hero-card">
          <div class="hero-copy" data-reveal>
            <div class="eyebrow">CONFIDENCE &bull; CARE &bull; COMMUNITY</div>
            <h1><span class="accent">Laugh with confidence,</span><span class="bold-line">today, tomorrow, always.</span></h1>
            <p class="lede">Urban Dental Solutions is a general dentistry practice in Nkulumane, Bulawayo, offering cleaning, fillings, root canal treatment, tooth replacement and whitening &mdash; for you and your family.</p>
            <a class="btn-pill navy" href="tel:+263714936261">Book Appointment</a>
          </div>
          <div class="hero-photo"><img src="img/smiles.jpg" alt="Patients smiling with confidence at Urban Dental Solutions"></div>
        </div>
      </div>
    </div>

    <div class="strip">
      <div class="wrap">
        <div class="strip-item"><svg><use href="#ic-clock"/></svg><div><b>Working hours</b><span>Monday to Friday, 8am &ndash; 5pm</span></div></div>
        <div class="strip-item"><svg><use href="#ic-pin"/></svg><div><b>Location</b><span>14818 Nkulumane 12 Medical Centre, Bulawayo</span></div></div>
        <div class="strip-item"><svg><use href="#ic-phone"/></svg><div><b>Call to book</b><span>+263 71 493 6261 &nbsp;/&nbsp; +263 78 459 9794</span></div></div>
      </div>
    </div>

    <section>
      <div class="wrap">
        <div class="section-head" data-reveal>
          <div class="eyebrow">WHAT WE TREAT</div>
          <h2>Our Dental Services</h2>
          <p>Comprehensive general dentistry tailored to keep your smile healthy, comfortable and confident.</p>
        </div>
        <div class="svc-grid">{svc_cards()}</div>
      </div>
    </section>

    <div class="cta-wrap-outer">
      <div class="cta-band">
        <div class="wrap">
          <h3>Book now &amp; get a free consultation.</h3>
          <a class="btn-pill teal" href="tel:+263714936261"><svg width="14" height="14"><use href="#ic-phone"/></svg>+263 71 493 6261</a>
        </div>
      </div>
    </div>

    <section>
      <div class="wrap welcome-grid">
        <div class="welcome-copy" data-reveal>
          <div class="eyebrow">WELCOME TO</div>
          <h2>Urban Dental Solutions</h2>
          <p>Built on the belief that exceptional dentistry changes lives, Urban Dental Solutions exists to make oral healthcare more personal, accessible and reassuring.</p>
          <p>We combine modern clinical care with a genuinely welcoming practice &mdash; so every visit, whatever it's for, leaves you feeling informed, comfortable and confident.</p>
          <a class="btn-pill outline" href="about.html">More about us</a>
        </div>
        <div class="photo-strip" data-reveal>
          <div class="ph"><img src="img/smiles.jpg" alt="Patient smiling"></div>
          <div class="ph"><img src="img/chair.jpg" alt="Treatment room"></div>
          <div class="ph"><img src="img/crowns.jpg" alt="Dental restorations"></div>
        </div>
      </div>
    </section>
"""

# ---------------- SERVICES ----------------
services_body = f"""
    <div class="page-head">
      <div class="wrap">
        <div class="eyebrow">WHAT WE TREAT</div>
        <h1>General dentistry services</h1>
        <p>Five core treatments cover most of what brings patients through the door &mdash; from a routine clean to replacing a missing tooth.</p>
      </div>
    </div>
    <div class="wrap">
      <div class="banner-photo" data-reveal>
        <img src="img/crowns.jpg" alt="Custom dental restorations crafted to match your natural shade">
        <span class="cap">Restorations shaped and shaded to match your own teeth.</span>
      </div>
    </div>
    <section style="padding-top:0;">
      <div class="wrap">
        <div class="svc-full">{svc_rows()}</div>
      </div>
    </section>
    <div class="cta-wrap-outer">
      <div class="cta-band">
        <div class="wrap">
          <h3>Not sure which treatment you need?</h3>
          <a class="btn-pill teal" href="contact.html">Get in touch</a>
        </div>
      </div>
    </div>
"""

# ---------------- ABOUT ----------------
about_body = f"""
    <div class="page-head">
      <div class="wrap">
        <div class="eyebrow">OUR PRACTICE</div>
        <h1>Dentistry built around the patient in front of us.</h1>
      </div>
    </div>
    <section>
      <div class="wrap about-grid">
        <div class="lede-block" data-reveal>
          <p class="drop">Built on the belief that exceptional dentistry changes lives, Urban Dental Solutions exists to make oral healthcare more personal, accessible and reassuring. We combine modern clinical expertise with compassionate care to create an environment where patients feel informed, comfortable and confident throughout every stage of their dental journey.</p>
          <p>Whether it's preventive care, restorative treatment or cosmetic dentistry, every consultation is guided by precision, integrity and a commitment to long-term wellbeing. We don't simply treat teeth &mdash; we build trusted relationships, promote healthier communities and help every patient smile with confidence for life.</p>
          <div class="banner-photo" style="margin-top:34px;">
            <img src="img/tools.jpg" alt="Sterilised dental instruments used at Urban Dental Solutions">
            <span class="cap">Every instrument sterilised between patients.</span>
          </div>
        </div>
        <div data-reveal>
          <div class="hours-card">
            <div class="eyebrow" style="margin-bottom:16px;">WORKING HOURS</div>
            <div class="hours-row"><span>Monday</span><span>8:00am &ndash; 5:00pm</span></div>
            <div class="hours-row"><span>Tuesday</span><span>8:00am &ndash; 5:00pm</span></div>
            <div class="hours-row"><span>Wednesday</span><span>8:00am &ndash; 5:00pm</span></div>
            <div class="hours-row"><span>Thursday</span><span>8:00am &ndash; 5:00pm</span></div>
            <div class="hours-row"><span>Friday</span><span>8:00am &ndash; 5:00pm</span></div>
            <div class="hours-row off"><span>Saturday</span><span>Closed</span></div>
            <div class="hours-row off"><span>Sunday</span><span>Closed</span></div>
          </div>
        </div>
      </div>
    </section>
    <section style="padding-top:0;">
      <div class="wrap">
        <div class="section-head" data-reveal>
          <div class="eyebrow">OUR APPROACH</div>
          <h2>What guides every appointment.</h2>
        </div>
        <div class="value-list">{value_rows()}</div>
      </div>
    </section>
"""

# ---------------- CONTACT ----------------
contact_body = """
    <div class="page-head">
      <div class="wrap">
        <div class="eyebrow">VISIT OR CALL</div>
        <h1>Get in touch</h1>
        <p>Reach the practice by phone, WhatsApp or email, or come by Nkulumane 12 Medical Centre during working hours. Walk-ins accepted.</p>
      </div>
    </div>
    <section>
      <div class="wrap contact-grid">
        <div data-reveal>
          <div class="contact-card">
            <div class="svc-badge"><svg><use href="#ic-phone"/></svg></div>
            <div><h4>Phone</h4><a href="tel:+263714936261">+263 71 493 6261</a><br><a href="tel:+263784599794">+263 78 459 9794</a></div>
          </div>
          <div class="contact-card">
            <div class="svc-badge"><svg><use href="#ic-mail"/></svg></div>
            <div><h4>Email</h4><a href="mailto:urbandental3@gmail.com">urbandental3@gmail.com</a></div>
          </div>
          <div class="contact-card">
            <div class="svc-badge"><svg><use href="#ic-pin"/></svg></div>
            <div><h4>Address</h4><p>14818 Nkulumane 12 Medical Centre, Bulawayo, Zimbabwe</p></div>
          </div>
          <div class="contact-card">
            <div class="svc-badge"><svg><use href="#ic-clock"/></svg></div>
            <div><h4>Working hours</h4><p>Monday &ndash; Friday, 8am &ndash; 5pm. Walk-ins accepted.</p></div>
          </div>

          <div class="quick-actions">
            <a class="qbtn" href="tel:+263714936261"><span class="qa-l"><svg class="lead"><use href="#ic-phone"/></svg>Call the practice</span><svg class="arrow"><use href="#ic-arrow"/></svg></a>
            <a class="qbtn" href="https://wa.me/263784599794" target="_blank" rel="noopener"><span class="qa-l"><svg class="lead"><use href="#ic-whatsapp"/></svg>Message on WhatsApp</span><svg class="arrow"><use href="#ic-arrow"/></svg></a>
            <a class="qbtn" href="mailto:urbandental3@gmail.com"><span class="qa-l"><svg class="lead"><use href="#ic-mail"/></svg>Send an email</span><svg class="arrow"><use href="#ic-arrow"/></svg></a>
          </div>
        </div>

        <div data-reveal>
          <div class="map-block">
            <svg viewBox="0 0 500 340" preserveAspectRatio="xMidYMid slice">
              <rect width="500" height="340" fill="#E9DBC9"/>
              <g opacity="0.5" stroke="#8A7C72" stroke-width="1">
                <line x1="0" y1="60" x2="500" y2="60"/><line x1="0" y1="140" x2="500" y2="140"/>
                <line x1="0" y1="220" x2="500" y2="220"/><line x1="0" y1="300" x2="500" y2="300"/>
                <line x1="90" y1="0" x2="90" y2="340"/><line x1="220" y1="0" x2="220" y2="340"/>
                <line x1="350" y1="0" x2="350" y2="340"/><line x1="450" y1="0" x2="450" y2="340"/>
              </g>
              <circle cx="250" cy="150" r="9" fill="#223954"/>
              <circle cx="250" cy="150" r="18" fill="none" stroke="#223954" stroke-width="1.4"/>
            </svg>
            <div class="map-pin-label">Nkulumane 12 Medical Centre</div>
          </div>
          <p style="font-size:13px;color:#6b7280;margin-top:14px;">
            <a href="https://www.google.com/maps/search/?api=1&query=14818+Nkulumane+12+Medical+Centre+Bulawayo" target="_blank" rel="noopener" style="color:#223954;font-weight:600;text-decoration:none;">Get directions on Google Maps &nbsp;&rarr;</a>
          </p>
        </div>
      </div>
    </section>
"""

pages = [
    ("index.html", "Urban Dental Solutions — Bulawayo", "General dentistry in Nkulumane, Bulawayo. Cleaning, fillings, root canal treatment, tooth replacement and whitening.", home_body),
    ("services.html", "Services — Urban Dental Solutions", "Teeth cleaning, fillings, root canal treatment, tooth replacement and whitening at Urban Dental Solutions, Bulawayo.", services_body),
    ("about.html", "About — Urban Dental Solutions", "About Urban Dental Solutions, a general dentistry practice at Nkulumane 12 Medical Centre, Bulawayo.", about_body),
    ("contact.html", "Contact — Urban Dental Solutions", "Contact Urban Dental Solutions in Bulawayo by phone, WhatsApp, email or in person.", contact_body),
]

for fname, title, desc, body in pages:
    html = page_shell(title, desc, fname, body)
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname, len(html))
