Urban Dental Solutions — Full Website
=======================================

This is a real, multi-page static website: separate HTML pages
with shared CSS, JS and image files, ready to upload to any web
host, Cloudflare Pages, or your own server.

FOLDER STRUCTURE
----------------
index.html        Home page
services.html     Services page
about.html        About page
contact.html      Contact page
css/styles.css    All styling (colours, type, layout)
js/main.js        Mobile menu + scroll-reveal behaviour
img/logo.png      Urban Dental Solutions logo
img/chair.jpg     Treatment room photo (hero)
img/smiles.jpg    Patient photo (About section)
img/crowns.jpg    Restorations photo (Services banner)
img/tools.jpg     Instruments photo (About banner)
build.py          The Python script that generated the HTML pages
                  (only needed if you want to regenerate the site
                  after editing copy in this script — optional)

HOW TO USE IT
-------------
1. Preview locally: double-click index.html to open it in a
   browser, or run a simple local server, e.g.
       python3 -m http.server 8000
   then visit http://localhost:8000

2. Host it: upload the whole folder (keeping the same folder
   structure — css/, js/, img/ alongside the .html files) to any
   static web host, Cloudflare Pages, Netlify, or a standard
   shared-hosting file manager.

3. Edit copy or contact details: open the .html files directly
   and edit the text, or edit build.py and re-run
       python3 build.py
   to regenerate all four pages from one place.

4. Edit styling: all colours, fonts and spacing live in
   css/styles.css. The colour palette is defined at the top under
   :root { --navy: ...; --gold: ...; }.

CONTACT DETAILS USED
---------------------
Phone: +263 71 493 6261 / +263 78 459 9794
Email: urbandental3@gmail.com
Address: 14818 Nkulumane 12 Medical Centre, Bulawayo
Hours: Monday–Friday, 8am–5pm
