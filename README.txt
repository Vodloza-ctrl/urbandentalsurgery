Urban Dental Solutions — On-Brand Website (v2)
================================================

This version is built from the official brand guide you provided
(Urban_Dental_Solutions_Logo_Presentation_1.pdf), not the earlier
placeholder styling.

WHAT CHANGED FROM THE FIRST VERSION
------------------------------------
- Colours now match the guide exactly:
    Navy   #223954
    Taupe  #8A7C72
    Teal   #0878A6
    Cream  #E9DBC9
- Typeface is Outfit (Google Font) throughout, with a small italic
  serif accent (Newsreader) used only for the hero headline, matching
  the guide's own website mockup.
- The real logo was extracted directly from your PDF — full-colour
  version for light backgrounds (img/logo-color.png) and a white
  version for dark backgrounds (img/logo-white.png).
- Correct tagline: "Laugh with confidence, today, tomorrow, always."
- Real mission copy from the brand guide is used on the Home and
  About pages, instead of generic placeholder text.
- Layout follows the guide's own website mockup: announcement bar
  ("Visit us today • Walk-ins accepted"), rounded hero card, pill-
  shaped buttons, circular icon badges on service cards, and a
  three-photo "Welcome to Urban Dental Solutions" strip.

FOLDER STRUCTURE
-----------------
index.html        Home
services.html     Services
about.html        About
contact.html      Contact
css/styles.css     All styling — colours are set once at the top
                    under :root, so you can retint the whole site
                    from one place.
js/main.js         Mobile menu + scroll-reveal behaviour
img/logo-color.png Full-colour logo (light backgrounds)
img/logo-white.png White logo (dark backgrounds, used in footer)
img/chair.jpg, smiles.jpg, crowns.jpg, tools.jpg — practice photos
build.py           The Python script that generated the HTML pages.
                    Edit the copy/services/values lists in this file
                    and re-run `python3 build.py` to regenerate all
                    four pages at once — much faster than editing
                    each HTML file by hand.

HOW TO USE IT
--------------
1. Preview locally: double-click index.html, or run
       python3 -m http.server 8000
   and visit http://localhost:8000

2. Host it: upload the whole folder (css/, js/, img/ alongside the
   .html files) to any static host — Cloudflare Pages, Netlify, or
   standard shared hosting.

3. Edit content: either edit the .html files directly, or edit the
   text in build.py and re-run it to regenerate all four pages.

CONTACT DETAILS USED
----------------------
Phone: +263 71 493 6261 / +263 78 459 9794
Email: urbandental3@gmail.com
Address: 14818 Nkulumane 12 Medical Centre, Bulawayo
Hours: Monday–Friday, 8am–5pm • Walk-ins accepted
