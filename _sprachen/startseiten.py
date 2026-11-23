"""Startseiten der vier Testversionen in Deutsch, Englisch und Portugiesisch (Brasilien).

  python3 _sprachen/startseiten.py /pfad/zu/den/repos

Erwartet die vier Repos nebeneinander (test-dreieck, dt-profischraube-web,
dt-profipassung-web, dt-profischweissnaht-web) und schreibt in jedes:
  index.html, en/index.html, pt/index.html, sitemap_….xml
Texte: startseiten_de.json (Deutsch) und startseiten_en_pt.py (EN/PT, Titel, Oberflaeche).
Titel <= 60 und Beschreibungen 110–160 Zeichen werden geprueft.
"""
import json, re, sys, html as H
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from startseiten_en_pt import UI, KOPF, T

HERE = Path(__file__).resolve().parent
DOM = "https://dt-profidreieck.de/"
GH = "https://dietertepe.github.io/"
HEUTE = "2026-11-23"
DIRS = {"de": "", "en": "en/", "pt": "pt/"}
HTML_LANG = {"de": "de", "en": "en", "pt": "pt-BR"}
OG = {"de": "de_DE", "en": "en_US", "pt": "pt_BR"}
FLAG = {"de": "DE", "en": "EN", "pt": "PT"}
SITEMAP = {"test-dreieck": "sitemap_profidreieck.xml", "dt-profischraube-web": "sitemap_profischraube.xml",
           "dt-profipassung-web": "sitemap_profipassung.xml", "dt-profischweissnaht-web": "sitemap_profischweissnaht.xml"}
VIDEO_POSTER = {
    "dreieck-dxf-werkstatt": "Dreieck_Daten/bilder/poster-v2-werkstatt.jpg",
    "schraube-vdi-2230": "Schraube_Daten/bilder/schraube-start.jpg",
    "passung-iso-286": "Passung_Daten/bilder/passung-start.jpg",
    "schweissnaht-en-1993-1-8": "Schweissnaht_Daten/bilder/schweissnaht-start.jpg",
}
ORDER = ["dreieck", "schraube", "passung", "schweissnaht"]
DE = json.loads((HERE / "startseiten_de.json").read_text(encoding="utf-8"))
CSS = (HERE / "startseiten.css").read_text(encoding="utf-8") + """
    .langs { display:inline-flex; gap:4px; margin-left:14px; }
    .langs a { text-decoration:none; font-size:.8rem; font-weight:800; padding:3px 8px; border-radius:999px; border:1px solid var(--line); color:var(--muted); }
    .langs a[aria-current="page"] { background:var(--cyan); border-color:var(--cyan); color:#062128; }
"""
CSS_AUFG = (HERE / "startseiten_aufgaben.css").read_text(encoding="utf-8")
plain = lambda s: re.sub("<[^>]+>", "", s)


def pruefen():
    f = []
    for k, langs in KOPF.items():
        for l, (t, d) in langs.items():
            if len(t) > 60: f.append(f"{k}/{l} Titel {len(t)}")
            if not 110 <= len(d) <= 160: f.append(f"{k}/{l} Beschreibung {len(d)}")
    if f: sys.exit("Laengenpruefung: " + "; ".join(f))


def texte(k, l):
    d = DE[k]
    if l == "de":
        return dict(kat=d["kat"], h1=d["h1"], lead=d["lead"], caption=d["caption"], img_alt=d["img_alt"], trust=d["trust"],
                    features=[(t, x) for _, t, x in d["features"]], steps=d["steps"], box=(d["box"][0], d["box"][1]), faq=d["faq"], aufgaben=d.get("aufgaben"))
    return T[k][l]


def seite(k, l):
    d = DE[k]; t = texte(k, l); ui = UI[l]
    base = GH + d["repo"] + "/"; page = base + DIRS[l]
    app = base + d["app"] + ("" if l == "de" else f"?lang={l}")
    name, preis = d["name"], d["preis"]
    title, desc = KOPF[k][l]
    if d.get("img"):
        ipath, iw, ih, _ = d["img"]; img_url = DOM + ipath
        picture = f'<img src="{img_url}" width="{iw}" height="{ih}" fetchpriority="high" decoding="async" alt="{H.escape(t["img_alt"])}">'
    else:
        img_url = base + "dreieck-berechnen.jpg"
        picture = (f'<picture>\n              <source srcset="{base}dreieck-berechnen.webp" type="image/webp">\n'
                   f'              <img src="{img_url}" width="700" height="570" fetchpriority="high" decoding="async"\n'
                   f'                   alt="{H.escape(t["img_alt"])}">\n            </picture>')
    accent = ""
    if d.get("accent"):
        accent = (f"\n    :root {{ --cyan: {d['accent']}; --cyan-dark: {d['accent_dark']}; }}"
                  f"\n    .primary {{ background: linear-gradient(135deg, {d['accent']}, {d['accent_dark']}); color:#fff; box-shadow:none; }}")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": page + "#webpage", "url": page, "name": title, "description": desc,
         "inLanguage": HTML_LANG[l], "primaryImageOfPage": img_url,
         "isPartOf": {"@type": "WebSite", "name": "DT-ProfiTools", "url": DOM}, "mainEntity": {"@id": page + "#software"}},
        {"@type": "SoftwareApplication", "@id": page + "#software", "name": name, "url": app,
         "applicationCategory": "BusinessApplication", "applicationSubCategory": t["kat"],
         "operatingSystem": "Webbrowser (Windows, macOS, Linux, Android, iOS)", "browserRequirements": "JavaScript",
         "inLanguage": ["de", "en", "pt-BR"], "image": img_url, "description": plain(t["lead"]),
         "author": {"@type": "Person", "name": "Dieter Tepe", "url": DOM},
         "offers": [
             {"@type": "Offer", "name": ui["start"], "price": "0.00", "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": app},
             {"@type": "Offer", "name": ui["k_eyebrow"], "price": f"{preis:.2f}", "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": d["kauf"]}]}]}
    if t.get("aufgaben"):
        ld["@graph"][1]["featureList"] = [plain(x["h3"]) for x in t["aufgaben"]["items"]]
    alt_links = "".join(f'  <link rel="alternate" hreflang="{x}" href="{base}{DIRS[x]}">\n' for x in DIRS)
    alt_links += f'  <link rel="alternate" hreflang="x-default" href="{base}">\n'
    og_alt = "".join(f'  <meta property="og:locale:alternate" content="{OG[x]}">\n' for x in DIRS if x != l)
    langs = "".join(f'<a href="{base}{DIRS[x]}" hreflang="{x}" lang="{x}"' + (' aria-current="page"' if x == l else "") + f'>{FLAG[x]}</a>' for x in DIRS)
    trust = "\n".join(f'          <div class="trust"><strong>{a}</strong><span>{b}</span></div>' for a, b in t["trust"])
    feats = "\n".join(
        f'          <article class="feature">\n            <div class="feature-icon" aria-hidden="true">{ic}</div>\n'
        f'            <h3>{ti}</h3>\n            <p>{tx}</p>\n          </article>'
        for (ic, _, _), (ti, tx) in zip(d["features"], t["features"]))
    steps = "\n".join(f"            <li>{s}</li>" for s in t["steps"])
    faq = "\n".join(f"          <details>\n            <summary>{q}</summary>\n            <p>{a}</p>\n          </details>" for q, a in t["faq"])
    aufg = ""
    if t.get("aufgaben"):
        a = t["aufgaben"]
        karten = "\n".join(
            f'          <article class="task" id="{x["id"]}">\n            <h3>{x["h3"]}</h3>\n            <p>{x["text"]}</p>\n'
            + "".join(f'            <div class="formula task-f">{f}</div>\n' for f in x["formeln"]) + "          </article>"
            for x in a["items"])
        aufg = f"""
    <section class="content" id="aufgaben">
      <div class="wrap">
        <div class="section-head">
          <div class="eyebrow">{a["eyebrow"]}</div>
          <h2>{a["h2"]}</h2>
          <p class="muted">{a["text"]}</p>
        </div>
        <div class="task-grid">
{karten}
        </div>
        <div class="actions task-cta"><a class="button primary" href="{app}">{a["btn"]}</a></div>
      </div>
    </section>
"""
    vurl = f"{DOM}videos/{d['video']}.html"; vposter = VIDEO_POSTER[d["video"]]
    tools = " · ".join((f'<a href="{GH}{DE[x]["repo"]}/{DIRS[l]}">{ui["tools"][x]}</a>' if x != k else f"<span>{ui['tools'][x]}</span>") for x in ORDER)
    short = name.replace("DT-Profi", "")
    fmt = lambda s: s.format(name=name, preis=preis)
    return f"""<!DOCTYPE html>
<html lang="{HTML_LANG[l]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="theme-color" content="#101923">

  <title>{H.escape(title)}</title>
  <meta name="description" content="{H.escape(desc)}">
  <meta name="author" content="Dieter Tepe">

  <link rel="canonical" href="{page}">
{alt_links}  <link rel="icon" href="{DOM}Landigpage_Daten/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="{DOM}Landigpage_Daten/favicon.png" type="image/png" sizes="48x48">
  <link rel="apple-touch-icon" href="{DOM}Landigpage_Daten/apple-touch-icon.png">

  <meta property="og:type" content="website">
  <meta property="og:locale" content="{OG[l]}">
{og_alt}  <meta property="og:site_name" content="DT-ProfiTools">
  <meta property="og:title" content="{H.escape(title)}">
  <meta property="og:description" content="{H.escape(desc)}">
  <meta property="og:url" content="{page}">
  <meta property="og:image" content="{img_url}">
  <meta name="twitter:card" content="summary_large_image">

  <!-- AUTOMATISCH ERZEUGT mit _sprachen/startseiten.py (Repo dt-profidreieck-web) – nicht von Hand bearbeiten -->
  <script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
  </script>

  <style>{CSS}{CSS_AUFG if t.get("aufgaben") else ""}{accent}
  </style>
</head>
<body>
  <header class="topline">
    <div class="wrap nav">
      <div class="brand">DT-<span>Profi</span>{short}</div>
      <div class="nav-note"><a href="{DOM}{DIRS[l]}">{ui["nav"]}</a><nav class="langs" aria-label="{ui["sprache"]}">{langs}</nav></div>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="wrap">
        <div class="hero-grid">
          <div>
            <div class="eyebrow">{H.escape(t["kat"])}</div>
            <h1>{t["h1"]}</h1>
            <p class="lead">{t["lead"]}</p>
            <div class="actions">
              <a class="button primary" href="{app}">{ui["start"]} <span aria-hidden="true">→</span></a>
              <a class="button secondary" href="#funktionen">{ui["mehr"]}</a>
            </div>
            <p class="micro">{ui["micro"]}</p>
          </div>
          <div class="diagram">
            {picture}
            <div class="diagram-caption">{t["caption"]}</div>
          </div>
        </div>
        <div class="trust-row" aria-label="{ui["f_eyebrow"]}">
{trust}
        </div>
      </div>
    </section>

    <section class="content" id="funktionen">
      <div class="wrap">
        <div class="section-head">
          <div class="eyebrow">{ui["f_eyebrow"]}</div>
          <h2>{fmt(ui["f_h2"])}</h2>
          <p class="muted">{ui["f_text"]}</p>
        </div>
        <div class="feature-grid">
{feats}
        </div>
      </div>
    </section>
{aufg}
    <section class="content">
      <div class="wrap split">
        <div>
          <div class="eyebrow">{ui["s_eyebrow"]}</div>
          <h2>{ui["s_h2"]}</h2>
          <ul class="checklist">
{steps}
          </ul>
        </div>
        <aside class="formula-box">
          <h3>{t["box"][0]}</h3>
          <p class="muted">{t["box"][1]}</p>
          <div class="formula">{d["box"][2]}</div>
          <p class="muted">{ui["box_tail"]}</p>
          <a href="{app}" class="button secondary">{ui["box_btn"]}</a>
        </aside>
      </div>
    </section>

    <section class="content" id="video">
      <div class="wrap media-link">
        <a class="thumb" href="{vurl}">
          <img src="{DOM}{vposter}" width="1280" height="720" loading="lazy" alt="{ui["v_alt"]}: {H.escape(name)}">
          <span>{ui["v_btn"]}</span>
        </a>
        <div>
          <div class="eyebrow">{ui["k_eyebrow"]}</div>
          <h2>{fmt(ui["k_h2"])}</h2>
          <div class="price">{preis} € <small>{ui["k_small"]}</small></div>
          <p class="muted">{ui["k_text"]}</p>
          <div class="actions">
            <a class="button primary" rel="nofollow" href="{d["kauf"]}">{fmt(ui["k_btn"])}</a>
            <a class="button secondary" href="{DOM}{DIRS[l]}#{k}">{ui["k_prod"]}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="content">
      <div class="wrap">
        <div class="section-head">
          <div class="eyebrow">{ui["faq_eyebrow"]}</div>
          <h2>{fmt(ui["faq_h2"])}</h2>
        </div>
        <div class="faq">
{faq}
        </div>
      </div>
    </section>

    <section class="content">
      <div class="wrap">
        <div class="closing">
          <div class="eyebrow">{ui["c_eyebrow"]}</div>
          <h2>{fmt(ui["c_h2"])}</h2>
          <p>{ui["c_text"]}</p>
          <a class="button primary" href="{app}">{fmt(ui["c_btn"])}</a>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="wrap">
      <div class="footrow">
        <span>© <span id="year">2026</span> Dieter Tepe · {name}</span>
        <span>{ui["hinweis"]}</span>
        <a href="{DOM}impressum.html">{ui["impressum"]}</a>
        <a href="{DOM}datenschutz.html">{ui["datenschutz"]}</a>
      </div>
      <nav class="tools" aria-label="{ui["weitere"]}">{ui["weitere"]} {tools}</nav>
    </div>
  </footer>
  <script>
    document.getElementById("year").textContent = new Date().getFullYear();
  </script>
</body>
</html>
"""


def sitemap(k):
    d = DE[k]; base = GH + d["repo"] + "/"
    alt = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{base}{DIRS[x]}"/>\n' for x in DIRS)
    alt += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{base}"/>\n'
    urls = "".join(f"  <url>\n    <loc>{base}{DIRS[x]}</loc>\n    <lastmod>{HEUTE}</lastmod>\n{alt}  </url>\n" for x in DIRS)
    urls += f"  <url>\n    <loc>{base}{d['app']}</loc>\n    <lastmod>{HEUTE}</lastmod>\n  </url>\n"
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")


def main():
    pruefen()
    root = Path(sys.argv[1] if len(sys.argv) > 1 else HERE.parent.parent)
    for k in ORDER:
        repo = root / DE[k]["repo"]
        for l, sub in DIRS.items():
            (repo / sub).mkdir(exist_ok=True)
            (repo / sub / "index.html").write_text(seite(k, l), encoding="utf-8")
        (repo / SITEMAP[DE[k]["repo"]]).write_text(sitemap(k), encoding="utf-8")
        print("ok", DE[k]["repo"], [len(KOPF[k][l][0]) for l in DIRS], [len(KOPF[k][l][1]) for l in DIRS])


if __name__ == "__main__":
    main()
