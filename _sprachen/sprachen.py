"""Sprachseiten der Hauptseite erzeugen.

  python3 _sprachen/sprachen.py

Quelle ist die deutsche index.html. Daraus entstehen en/index.html (Englisch,
international) und pt/index.html (Portugiesisch, Brasilien). Die Uebersetzungen
stehen in _sprachen/uebersetzungen.json (Schluessel = deutscher Text).
Titel/Beschreibungen je Sprache stehen unten in KOPF und werden auf die
Laengen geprueft, die Google und Bing vertragen (Titel <= 60, Beschreibung <= 160).

Der Ordner beginnt mit "_" -> GitHub Pages veroeffentlicht ihn nicht.
"""
import json, re, sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Comment

REPO = Path(__file__).resolve().parent.parent
DOM = "https://dt-profidreieck.de/"
LANGS = {"de": "", "en": "en/", "pt": "pt/"}
HTML_LANG = {"de": "de", "en": "en", "pt": "pt-BR"}
OG_LOCALE = {"de": "de_DE", "en": "en_US", "pt": "pt_BR"}
TITLE_MAX, DESC_MAX, DESC_MIN = 60, 160, 110

KOPF = {
    "de": {"title": "Berechnungsprogramme Maschinenbau offline – DT-ProfiTools",
           "desc": "Vier Profi-Programme, offline im Browser: Dreieck mit DXF für die CNC, Schrauben nach VDI 2230, Passungen nach ISO 286, Schweißnähte nach EN 1993-1-8."},
    "en": {"title": "Engineering Calculators for Workshop & CNC – DT-ProfiTools",
           "desc": "Four offline engineering tools: triangle solver with DXF for CNC, bolted joints to VDI 2230, ISO 286 fits and welds to EN 1993-1-8. Try them free."},
    "pt": {"title": "Calculadoras de Engenharia Mecânica – DT-ProfiTools",
           "desc": "Quatro programas de engenharia offline: triângulo com DXF para CNC, parafusos VDI 2230, ajustes ISO 286 e soldas EN 1993-1-8. Teste grátis."},
}
PRODUKTE = [  # key, name, preis, kauf, test, beschreibung je Sprache, bild
    ("dreieck", "DT-ProfiDreieck", 69, "https://www.checkout-ds24.com/product/722585",
     "https://dietertepe.github.io/test-dreieck/DT-ProfiDreieck_Test_1-1-0.html",
     {"de": "Dreiecksberechnung aus drei beliebigen Größen mit maßstäblicher Zeichnung, vollständigem Rechenweg und DXF-Export für CAD und CNC.",
      "en": "Triangle solver from any three values with a true-to-scale drawing, full calculation path and DXF export for CAD and CNC.",
      "pt": "Cálculo de triângulos a partir de três valores quaisquer, com desenho em escala, memória de cálculo completa e exportação DXF para CAD e CNC."},
     "Dreieck_Daten/bilder/app-zeichnung.jpg"),
    ("schraube", "DT-ProfiSchraube", 159, "https://www.checkout-ds24.com/product/722968",
     "https://dietertepe.github.io/dt-profischraube-web/DT-ProfiSchraube_Test.html",
     {"de": "Berechnung vorgespannter Schraubenverbindungen nach VDI 2230 Blatt 1 mit fünf Nachweisen, Verspannungsschaubild und dokumentiertem Rechenweg.",
      "en": "Bolted joint calculation to VDI 2230 Part 1 with five safety checks, joint diagram and a documented calculation path.",
      "pt": "Cálculo de uniões parafusadas conforme VDI 2230 Parte 1, com cinco verificações, diagrama de tensões e memória de cálculo documentada."},
     "Schraube_Daten/bilder/schraube-start.jpg"),
    ("passung", "DT-ProfiPassung", 139, "https://www.checkout-ds24.com/product/722972",
     "https://dietertepe.github.io/dt-profipassung-web/DT-ProfiPassung_Testversion.html",
     {"de": "Toleranzen und Passungen nach ISO 286, Pressverband nach DIN 7190 und Allgemeintoleranzen nach ISO 2768 mit selbstprüfendem Rechenweg.",
      "en": "Limits and fits to ISO 286, interference fits to DIN 7190 and general tolerances to ISO 2768 with a self-checking calculation path.",
      "pt": "Tolerâncias e ajustes conforme ISO 286, ajuste por interferência conforme DIN 7190 e tolerâncias gerais ISO 2768, com memória de cálculo autoverificada."},
     "Passung_Daten/bilder/passung-start.jpg"),
    ("schweissnaht", "DT-ProfiSchweissnaht", 169, "https://www.checkout-ds24.com/product/722975",
     "https://dietertepe.github.io/dt-profischweissnaht-web/DT-ProfiSchweissnaht_Testversion.html",
     {"de": "Schweißnahtberechnung nach EN 1993-1-8 und Maschinenbau-Ansätzen mit maßstäblichem Nahtbild, Rechenweg und Wärmeführung.",
      "en": "Weld calculation to EN 1993-1-8 and classic mechanical engineering methods with a true-to-scale weld layout, calculation path and heat control.",
      "pt": "Cálculo de soldas conforme EN 1993-1-8 e métodos clássicos de engenharia mecânica, com geometria do cordão em escala, memória de cálculo e controle térmico."},
     "Schweissnaht_Daten/bilder/schweissnaht-start.jpg"),
]
FLAG_LABEL = {"de": "Deutsch", "en": "English", "pt": "Português"}


def check_laengen():
    fehler = []
    for l, k in KOPF.items():
        if len(k["title"]) > TITLE_MAX: fehler.append(f"{l}: Titel {len(k['title'])} Zeichen")
        if not DESC_MIN <= len(k["desc"]) <= DESC_MAX: fehler.append(f"{l}: Beschreibung {len(k['desc'])} Zeichen")
    if fehler: sys.exit("Laengenpruefung fehlgeschlagen: " + "; ".join(fehler))


def url(l): return DOM + LANGS[l]


def kopf_block(l):
    k = KOPF[l]
    t = (f'<title>{esc(k["title"])}</title>\n'
         f'<meta name="description" content="{esc(k["desc"])}">\n'
         f'<link rel="canonical" href="{url(l)}">\n')
    for x in LANGS:
        t += f'<link rel="alternate" hreflang="{x}" href="{url(x)}">\n'
    t += f'<link rel="alternate" hreflang="x-default" href="{url("de")}">\n'
    return t


def esc(s): return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def jsonld(l):
    test_q = "" if l == "de" else f"?lang={l}"
    graph = [
        {"@type": "Person", "@id": DOM + "#dieter-tepe", "name": "Dieter Tepe", "url": DOM},
        {"@type": "WebSite", "@id": DOM + "#website", "url": DOM, "name": "DT-ProfiTools",
         "inLanguage": ["de", "en", "pt-BR"], "publisher": {"@id": DOM + "#dieter-tepe"}},
        {"@type": "WebPage", "@id": url(l) + "#webpage", "url": url(l), "name": KOPF[l]["title"],
         "description": KOPF[l]["desc"], "isPartOf": {"@id": DOM + "#website"}, "inLanguage": HTML_LANG[l],
         "primaryImageOfPage": DOM + "Landigpage_Daten/og-card.jpg",
         "hasPart": [{"@id": url(l) + "#" + p[0]} for p in PRODUKTE]},
    ]
    for key, name, preis, kauf, test, beschr, bild in PRODUKTE:
        graph.append({
            "@type": "SoftwareApplication", "@id": url(l) + "#" + key, "name": name, "url": url(l) + "#" + key,
            "description": beschr[l], "applicationCategory": "BusinessApplication",
            "operatingSystem": "Webbrowser (Windows, macOS, Linux, Android, iOS)",
            "inLanguage": ["de", "en", "pt-BR"], "image": DOM + bild, "author": {"@id": DOM + "#dieter-tepe"},
            "offers": [
                {"@type": "Offer", "name": {"de": "Vollversion", "en": "Full version", "pt": "Versão completa"}[l],
                 "price": f"{preis:.2f}", "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": kauf},
                {"@type": "Offer", "name": {"de": "Gratis-Testversion", "en": "Free trial version", "pt": "Versão de teste grátis"}[l],
                 "price": "0.00", "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": test + test_q}]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def sprachumschalter(l):
    """Flaggen als echte Links (statt Knoepfe) – jede Sprache hat ihre eigene Adresse."""
    return l


def deutsch_vorbereiten(s):
    """Deutsche Seite: Kopf, Sprachlinks, altes JS-Woerterbuch -> Weiterleitung. Idempotent."""
    # 1) Kopf: Titel/Beschreibung/Canonical/hreflang ersetzen
    s = re.sub(r"<title>.*?</title>\n", "", s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description"[^>]*>\n', "", s, count=1)
    s = re.sub(r'<link rel="canonical"[^>]*>\n', "", s, count=1)
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', "", s)
    s = s.replace('<meta name="viewport" content="width=device-width, initial-scale=1">\n',
                  '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + kopf_block("de"), 1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(KOPF["de"]["title"])}">', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(KOPF["de"]["desc"])}">', s, count=1)
    if 'og:locale:alternate' not in s:
        s = s.replace('<meta property="og:locale" content="de_DE">',
                      '<meta property="og:locale" content="de_DE">\n<meta property="og:locale:alternate" content="en_US">\n<meta property="og:locale:alternate" content="pt_BR">', 1)
    # 2) JSON-LD erneuern
    s = re.sub(r'(<script type="application/ld\+json">\n).*?(\n</script>)', lambda m: m.group(1) + jsonld("de") + m.group(2), s, count=1, flags=re.S)
    # 3) Flaggen-Knoepfe -> Links
    def knopf(m):
        tag, inner = m.group(1), m.group(2)
        x = re.search(r'data-lang="(\w+)"', tag).group(1)
        return (f'<a class="lang-btn" data-lang="{x}" lang="{x}" hreflang="{x}" href="/{LANGS[x]}"'
                + (' aria-current="page"' if x == "de" else "") + f'>{inner}</a>')
    s = re.sub(r'(<button type="button" class="lang-btn"[^>]*>)(.*?)</button>', knopf, s, flags=re.S)
    # 4) Altes Woerterbuch + Umschalt-Skript entfernen, kleine Weiterleitung fuer alte ?lang=-Links
    a = s.find("<!-- ============================================================\n     SPRACHEN:")
    if a != -1:
        b = s.index("</script>", s.index("var I18N = {", a)) + len("</script>")
        weiter = ('<!-- Sprachen: eigene Seiten /en/ und /pt/ (erzeugt mit _sprachen/sprachen.py).\n'
                  '     Alte Links mit ?lang=en|pt werden dorthin weitergeleitet. -->\n'
                  '<script>(function(){var l=new URLSearchParams(location.search).get("lang");'
                  'if(l==="en"||l==="pt"){location.replace("/"+l+"/"+location.hash)}})();</script>')
        s = s[:a] + weiter + s[b:]
    # 5) Testversion-Links: Sprache der Seite an das Programm weitergeben
    alt = 'if (url && a.getAttribute("href") !== url) a.setAttribute("href", url);'
    neu = ('var sp = (document.documentElement.lang || "de").slice(0, 2);\n'
           '    if (url && sp !== "de" && a.getAttribute("data-link").indexOf("test-") === 0) url += "?lang=" + sp;\n'
           '    if (url && a.getAttribute("href") !== url) a.setAttribute("href", url);')
    if alt in s and "var sp = (document.documentElement.lang" not in s:
        s = s.replace(alt, neu, 1)
    # 6) Kommentar + CSS fuer Sprachlinks
    alt_k = """  SPRACHEN: Deutsch steht fest im HTML. Englisch und Portugiesisch liegen
    als Woerterbuch im Skript ganz unten (I18N). Der Umschalter oben rechts
    tauscht die Texte aus und haengt ?lang=en bzw. ?lang=pt an die Adresse,
    damit die Wahl beim Neuladen und Weitergeben erhalten bleibt.
    KEINE Cookies, KEIN Speicher, KEINE fremden Dienste.
    Neue Texte uebersetzen: deutschen Satz als Schluessel ins Woerterbuch
    eintragen. Fehlt ein Eintrag, bleibt an der Stelle einfach Deutsch stehen.
    Elemente mit farbigen Teilstuecken tragen data-i18n-html und werden
    komplett ersetzt (siehe I18N_HTML)."""
    neu_k = """  SPRACHEN: Diese Datei ist die DEUTSCHE Quelle. Englisch (/en/) und
    Portugiesisch-Brasilien (/pt/) sind eigene Seiten, erzeugt mit
      python3 _sprachen/sprachen.py
    aus dieser Datei + _sprachen/uebersetzungen.json (Schluessel = deutscher
    Text). Nach JEDER Textaenderung hier das Skript erneut ausfuehren.
    en/index.html und pt/index.html nie von Hand bearbeiten.
    KEINE Cookies, KEIN Speicher, KEINE fremden Dienste."""
    s = s.replace(alt_k, neu_k)
    css_alt = '  .lang-btn[aria-pressed="true"]{background:var(--accent); color:#fff;}'
    css_neu = '  .lang-btn[aria-current="page"]{background:var(--accent); color:#fff;}\n  a.lang-btn{text-decoration:none;}'
    s = s.replace(css_alt, css_neu)
    s = re.sub(r'<html lang="[^"]*">', '<html lang="de">', s, count=1)
    return s


RELATIV = re.compile(r"^(?![a-z][a-z0-9+.-]*:|/|#|\?)", re.I)


def uebersetzen(de_html, l, tr):
    soup = BeautifulSoup(de_html, "html.parser")
    texte, htmls = tr["texte"], tr["html"]
    fehlend = set()
    # Texte im <body>
    for node in soup.body.find_all(string=True):
        if isinstance(node, Comment): continue
        p = node.parent
        if p.name in ("script", "style") or p.find_parent(attrs={"data-i18n-html": True}) or p.has_attr("data-i18n-html"):
            continue
        roh = str(node).strip()
        if len(roh) <= 1: continue
        if roh in texte:
            vorn = str(node)[: len(str(node)) - len(str(node).lstrip())]
            hinten = str(node)[len(str(node).rstrip()):]
            node.replace_with(NavigableString(vorn + texte[roh][l] + hinten))
        elif re.search(r"[A-Za-zÄÖÜäöüß]{3}", roh) and not roh.startswith("DT-Profi"):
            fehlend.add(roh)
    for attr in ("alt", "aria-label", "title", "data-hinweis"):
        for el in soup.body.find_all(attrs={attr: True}):
            v = el[attr].strip()
            if v in texte: el[attr] = texte[v][l]
    for el in soup.find_all(attrs={"data-i18n-html": True}):
        k = el["data-i18n-html"]
        if k in htmls:
            el.clear(); el.append(BeautifulSoup(htmls[k][l], "html.parser"))
    # Testversion-Links direkt in der Sprache oeffnen
    for a in soup.select('a[data-link^="test-"]'):
        if "?lang=" not in a["href"]: a["href"] += f"?lang={l}"
    # Sprachlinks
    for a in soup.select("a.lang-btn"):
        if a.has_attr("aria-current"): del a["aria-current"]
        if a["data-lang"] == l: a["aria-current"] = "page"
    # Relative Pfade eine Ebene hoeher
    for el in soup.find_all(True):
        for attr in ("src", "href", "poster"):
            if el.has_attr(attr) and el[attr] and RELATIV.match(el[attr]):
                el[attr] = "../" + el[attr]
        if el.has_attr("srcset"):
            el["srcset"] = ", ".join(("../" + p.strip()) if RELATIV.match(p.strip()) else p.strip() for p in el["srcset"].split(","))
    soup.html["lang"] = HTML_LANG[l]
    out = soup.decode(formatter="html5")
    # Kopf
    out = re.sub(r"<title>.*?</title>\n", "", out, count=1, flags=re.S)
    out = re.sub(r'<meta content="[^"]*" name="description">\n|<meta name="description" content="[^"]*">\n', "", out, count=1)
    out = re.sub(r'<link href="[^"]*" rel="canonical">\n|<link rel="canonical" href="[^"]*">\n', "", out, count=1)
    out = re.sub(r'<link (?:href="[^"]*" hreflang="[^"]*" rel="alternate"|rel="alternate" hreflang="[^"]*" href="[^"]*")>\n', "", out)
    out = out.replace('<meta content="width=device-width, initial-scale=1" name="viewport">\n',
                      '<meta content="width=device-width, initial-scale=1" name="viewport">\n' + kopf_block(l), 1)
    out = out.replace('<meta name="viewport" content="width=device-width, initial-scale=1">\n',
                      '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + kopf_block(l), 1)
    for prop, val in (("og:title", KOPF[l]["title"]), ("og:description", KOPF[l]["desc"]), ("og:url", url(l)), ("og:locale", OG_LOCALE[l])):
        out = re.sub(r'<meta content="[^"]*" property="%s">' % re.escape(prop), f'<meta content="{esc(val)}" property="{prop}">', out, count=1)
        out = re.sub(r'<meta property="%s" content="[^"]*">' % re.escape(prop), f'<meta property="{prop}" content="{esc(val)}">', out, count=1)
    out = re.sub(r'(<script type="application/ld\+json">\n).*?(\n</script>)', lambda m: m.group(1) + jsonld(l) + m.group(2), out, count=1, flags=re.S)
    out = out.replace("SPRACHEN: Diese Datei ist die DEUTSCHE Quelle.", "SPRACHEN: AUTOMATISCH ERZEUGT aus ../index.html – NICHT von Hand bearbeiten!")
    if "<title>" not in out: sys.exit(f"{l}: Kopf konnte nicht gesetzt werden")
    return out, fehlend


def main():
    check_laengen()
    tr = json.loads((REPO / "_sprachen/uebersetzungen.json").read_text(encoding="utf-8"))
    de = deutsch_vorbereiten((REPO / "index.html").read_text(encoding="utf-8"))
    (REPO / "index.html").write_text(de, encoding="utf-8")
    alle_fehlend = set()
    for l in ("en", "pt"):
        out, fehlend = uebersetzen(de, l, tr)
        alle_fehlend |= fehlend
        (REPO / LANGS[l]).mkdir(exist_ok=True)
        (REPO / LANGS[l] / "index.html").write_text(out, encoding="utf-8")
        print(f"{l}/index.html geschrieben ({len(out)//1024} KB)")
    if alle_fehlend:
        print("\nOHNE UEBERSETZUNG (bleibt deutsch) – bitte in uebersetzungen.json ergaenzen:")
        for f in sorted(alle_fehlend): print("  -", f[:110])
    for l, k in KOPF.items():
        print(f"{l}: Titel {len(k['title'])} / Beschreibung {len(k['desc'])} Zeichen")


if __name__ == "__main__":
    main()
