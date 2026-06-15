# 🌐 Landingpageplan: „DT-ProfiDreieck"

```
=============================================================================
  LANDINGPAGE-PLAN  –  Verkaufsseite für DT-ProfiDreieck
=============================================================================
  Version : 0.4.2
  Stand   : 2026-06-09
  Status  : Seite LIVE unter dt-profidreieck.de (HTTPS) – zwei Demo-Videos
            eingebettet & live geprüft; Inhalts-Feinschliff läuft; Preis 69 €
  Ziel    : eine Single-File-HTML-Landingpage, die neben der Testversion im
            GitHub-Ordner `dt-profidreieck-web` liegt
  Bezug   : ergänzt den Masterplan v0.17.0 (dort Punkt 4.2/4.3) – baut auf
            dessen Entscheidungen auf
=============================================================================
```

## So liest du dieses Dokument

Gleiches Prinzip wie der Masterplan – **zwei Ebenen**:

- **TEIL 1 – Ablauf-Checkliste:** kurz, zum Abhaken, Schritt für Schritt.
- **TEIL 2 – Ausführliche Erklärungen:** dieselben Nummern, ausführlich.

**Status-Marker:**
- ✅ **entschieden** – kann umgesetzt werden
- 💬 **in Klärung** – Ansatz steht, Details besprechen wir noch
- 🔲 **offen** – muss erst durchdacht werden
- 💡 **später** – bewusst nach hinten geschoben

**Checkbox** `[ ]` = real erledigt? (Noch alle leer – Stand ist reine Planung.)

> **📁 Wichtige Projektdateien (Bezug):**
> - `DT-ProfiDreieck_Test_1-1-0.html` – die Gratis-Testversion, kommt mit in den
>   GitHub-Ordner. Die Landingpage soll deren Designsprache spiegeln.
> - `Pflichttexte_Entwurf.md` – liefert die Texte für Impressum & Datenschutz
>   (Abschnitt 1 + 2) für die zwei Unterseiten der Landingpage.
> - `Masterplan_DT-ProfiDreieck.md` – Gesamtplan; Hosting/DNS steht dort (2.6/2.7).

---

## 🎯 Leitidee (in einem Satz)

> **„Sieht aus wie von Linear gebaut, fühlt sich an wie deine Werkstatt."**
> Die *Bauprinzipien* moderner Profi-Seiten (Ruhe, große Abstände, ein
> dominanter Knopf, dezente Bewegung) – aber das *Aussehen* deiner App
> (hell, Petrol-Teal, gleiche Karten/Schriften). Die Seite ist der natürliche
> Vorraum zum Tool.

---

# TEIL 1 — ABLAUF-CHECKLISTE (zum Abhaken)

### Phase 0 – Grundsatzentscheidungen
- [x] **0.1** Stil: Werkstatt-Blueprint (App-Designsprache), Bauprinzipien von Linear/Raycast/Paddle — ✅
- [x] **0.2** Sprache: nur Deutsch; Englisch später als eigene Seite — ✅
- [x] **0.3** Technik-Grundsatz: Single-File, keine externen Schriften/Skripte, offline-tauglich — ✅
- [x] **0.4** Vorgehen: Grundgerüst zuerst, dann Sektion für Sektion erweitern — ✅
- [ ] **0.5** Bilder-Strategie: inline-SVG bevorzugt; echtes Bild nur aus eigenem Ordner — 💬

### Phase 1 – Grundgerüst (das erste, testbare Skelett) — ✅ gebaut & live getestet
- [x] **1.1** HTML-Grundstruktur + Meta (responsive, `lang="de"`, Titel) — ✅
- [x] **1.2** Design-Tokens aus der App übernehmen (CSS-`:root`-Variablen) — ✅
- [x] **1.3** Sektions-Platzhalter mit Sprungankern anlegen — ✅
- [x] **1.4** Alle Links als Platzhalter verdrahten + durchklicken — ✅
      *(Test-Knopf startet die Gratis-Version live — bestätigt 2026-06-07.)*
- [x] **1.5** Mobil/Tablet/Desktop-Check des Skeletts — ✅ (auf dem Handy bestätigt)

### Phase 2 – Inhalt der Sektionen (nach und nach füllen)
- [~] **2.1** Hero: Versprechen + 2 Knöpfe + SVG-Dreieck — steht im Grundgerüst; Feinschliff Text offen
- [x] **2.2** Praxis-Beweis: **zwei eigene MP4-Videos** eingebettet (V2 Werkstatt, V1 App-Demo) — ✅ live & getestet
- [~] **2.3** Vorteile der Vollversion (Funktionsliste + Burggraben) — Grundgerüst zeigt 4 Punkte + 2 App-Belege; Ausbau offen
- [ ] **2.4** Test vs. Pro (kleiner, ehrlicher Vergleich) — 🔲 (noch nicht angelegt)
- [~] **2.5** Kauf-Block: Preis **69 €** + Digistore24-Knopf + Vertrauen — Block steht (69 €); echter Kauf-Link + Nutzen-Texte offen
- [ ] **2.6** FAQ (kurz, optional) — 💡
- [x] **2.7** Footer: Links Impressum/Datenschutz, §19-Bezug, Kontakt — ✅ steht & verlinkt

### Phase 3 – Recht & Datenschutz (eigene Unterseiten) — ✅ gebaut & live getestet
- [x] **3.1** `impressum.html` aus Pflichttexte (Abschnitt 1) — ✅
- [x] **3.2** `datenschutz.html` aus Pflichttexte (Abschnitt 2) — ✅
- [x] **3.3** Beweis: Seite lädt KEINE externen Ressourcen — ✅ (geprüft)
      *(Beide Seiten live auf GitHub Pages bestätigt – laden korrekt, Footer-
      Links greifen, kein 404 mehr. Bestätigt 2026-06-07.)*

### Phase 4 – Feinschliff & Go-Live
- [x] **4.1** Dezente Mikro-Animationen (mit `prefers-reduced-motion`) — ✅ (Einblenden beim Laden, reduced-motion beachtet)
- [ ] **4.2** SEO-Basics (Titel, Description, ggf. eigenes OG-Bild) — Titel + Description gesetzt; OG-Bild offen
- [ ] **4.3** Selbstcheck Performance/Größe — 🔲
- [x] **4.4** Dateien in GitHub-Ordner `dt-profidreieck-web` legen — ✅ hochgeladen & live
- [x] **4.5** Domain-Verknüpfung (→ Masterplan 2.7) — ✅ live unter `dt-profidreieck.de` (HTTPS aktiv)

---

# TEIL 2 — AUSFÜHRLICHE ERKLÄRUNGEN

## Phase 0 – Grundsatzentscheidungen

### 0.1 Stil: Werkstatt-Blueprint ✅
- **Aussehen = deine App:** heller Hintergrund mit feinem Verlauf, weiße Karten
  mit weichem Schatten, 18px-Radien, Petrol-Teal-Akzent (`#0d7d8c`), Graphit-Navy
  (`#0f1b2d`), Messing als Zweitfarbe – **System-Schriften** (kein Google Fonts).
- **Bauprinzipien von Linear/Raycast/Paddle (nicht deren Look):** großzügige
  Abstände (8px-Raster), klar getrennte Sektionen, *eine* starke Headline, *ein*
  dominanter Hauptknopf je Sektion, viel Weißraum, ruhige Mikro-Bewegung.
- **Warum nicht dunkel/glossy wie Linear & Raycast:** das ist Startup-Sprache.
  Die Zielgruppe (CNC/Metallbau/Tischlerei) vertraut einem soliden Werkzeug von
  einem Macher mehr als einem hippen Dark-Mode-Auftritt.
- **Warum nicht 1:1 Paddle:** Paddle ist von den dreien am nächsten (hell,
  vertrauenswürdig), aber Enterprise-Marketing – wir bleiben handfester.

### 0.2 Sprache: nur Deutsch ✅
- Markt zuerst Deutschland (wie im Masterplan, Welle 1).
- **Englisch später als eigenständige Seite**, nicht als Umschalter. Vorteil:
  volle Flexibilität, und der deutsche Rechtsraum (Impressum/§19) bleibt sauber
  getrennt – konsistent mit der Tool-Entscheidung „Rechtstexte bleiben Deutsch".

### 0.3 Technik-Grundsatz ✅
- **Single-File-HTML** je Seite (Landingpage + zwei Rechts-Unterseiten), genau
  wie dein Tool. CSS und JS *in* der Datei.
- **Keine externen Schriften, keine fremden Skripte** – sonst stimmt die
  Datenschutz-Aussage nicht mehr (Masterplan 4.3 Designregel). Das ist die
  wichtigste Regel der ganzen Seite.
- **Offline-tauglich:** Doppelklick → öffnet im Browser → läuft. Kein Nachladen.
- **YouTube wird nur verlinkt, nie eingebettet** (ein Embed lädt Google-Skripte).

### 0.4 Vorgehen: Grundgerüst zuerst ✅
- **Erst das Skelett** (Phase 1): Struktur, Design-Tokens, leere Sektionen mit
  Ankern, **alle Links verdrahtet**. Sofort auf Handy/Tablet/PC testbar.
- **Dann Sektion für Sektion füllen** (Phase 2). Nach jedem Schritt kann getestet
  werden, ob Layout und Links weiter sauber funktionieren.
- Vorteil: nichts kippt am Ende um; du siehst früh, dass z. B. der Digistore- und
  der Testversion-Link gehen, bevor wir Texte/Bilder feilen.

### 0.5 Bilder-Strategie 💬
- **Bevorzugt – inline-SVG:** Dreiecks-Zeichnung und Icons direkt als SVG-Code in
  der HTML. Lädt nichts nach, gestochen scharf auf jedem Bildschirm, datenschutz-
  sicher. Damit braucht der Hero-Bereich gar keine echte Bilddatei.
- **Falls echtes Bild gewünscht** (z. B. Handy-Screenshot „App in der Werkstatt"):
  als *eine* Datei in denselben GitHub-Ordner legen und relativ einbinden
  (`<img src="screenshot.png">`). Lädt von GitHub Pages = *deinem* Server → kein
  Datenschutzproblem wie bei Fremddiensten.
- 🔲 *Noch zu klären:* ob/welche echten Bilder wir wollen – besprechen wir, wenn
  die Sektionen stehen.

---

## Phase 1 – Grundgerüst (testbares Skelett)

### 1.1 HTML-Grundstruktur + Meta 🔲
- `<!DOCTYPE html>`, `<html lang="de">`, `<meta charset>`,
  `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- Sprechender `<title>` und `<meta name="description">` (für Google).

### 1.2 Design-Tokens aus der App übernehmen 🔲
- Die `:root`-Farbvariablen der App 1:1 übernehmen (Teal, Navy, Card, Line,
  Shadow, Radius, Font-Stack). So sieht die Seite automatisch „wie das Tool" aus
  und bleibt später leicht anpassbar (eine Stelle ändern → ganze Seite zieht mit).

### 1.3 Sektions-Platzhalter mit Sprungankern 🔲
- Leere `<section>`-Blöcke in der späteren Reihenfolge anlegen, jeder mit `id`
  (z. B. `#start`, `#beweis`, `#vorteile`, `#kaufen`, `#footer`). So funktionieren
  Menü-Sprünge und „nach oben"-Knöpfe sofort.

### 1.4 Alle Links verdrahten + durchklicken 🔲
- **Kauf-Knopf** → Digistore24-Warenkorb-Link (Platzhalter, bis 3.5 im Masterplan
  steht).
- **Test-Knopf** → relative Datei `DT-ProfiDreieck_Test_1-1-0.html` im selben
  Ordner.
- **YouTube-Knopf** → Video-URL (Platzhalter, bis Video aus 4.4.2 existiert).
- **Footer** → `impressum.html` und `datenschutz.html`.
- Jeden Link einmal anklicken: geht er ins Leere oder zum Ziel?

### 1.5 Geräte-Check des Skeletts 🔲
- Handy (schmal), Tablet (mittel), PC (breit): bricht nichts um, sind Knöpfe groß
  genug zum Tippen, ist Text lesbar? Erst wenn das Skelett überall sauber sitzt,
  geht's an die Inhalte.

---

## Phase 2 – Inhalt der Sektionen

> Reihenfolge folgt dem Masterplan 4.2 (Versprechen → Beweis → Köder → Verkauf),
> erweitert um Footer/Recht.

### 2.1 Hero (oben, das Erste was man sieht) 🔲
- **Versprechen (Headline):** „Komplexe Dreiecke berechnen und direkt als DXF an
  die CNC." (aus Masterplan 4.2.1)
- **Kurzer Untertitel:** offline, eine Datei, keine Installation, läuft auf
  Handy/Tablet/PC.
- **Zwei Knöpfe:** primär „Gratis-Version testen →" (Test-HTML), sekundär „Jetzt
  kaufen – 69 €" (Digistore). Ein dominanter Knopf, einer dezenter.
- **Visuell:** inline-SVG eines sauber vermaßten Dreiecks (Blueprint-Optik).

### 2.2 Praxis-Beweis ✅ (umgesetzt – besser als ursprünglich geplant)
- **Statt YouTube-Link jetzt zwei eigene MP4-Videos direkt eingebettet**
  (`<video controls>`), beide live & getestet:
  - **V2.mp4** – Werkstattvideo „Vom Wert zum fertigen DXF"
  - **V1.mp4** – App-Demo „Von der Eingabe bis zum Ergebnis"
- **Warum das besser ist:** Eigene MP4s im GitHub-Ordner laden — anders als ein
  YouTube-Embed — **nichts von fremden Servern**. Die Datenschutz-Regel („keine
  externen Ladequellen") bleibt erfüllt, und es gibt trotzdem einen echten
  Player auf der Seite. Mit Download-Fallback für alte Browser.
- 💡 *Wartung im Blick behalten:* Videos sind groß. GitHub warnt > 50 MB, blockt
  > 100 MB. **Aktueller Stand bestätigt (09.06.2026):** beide MP4 vorbildlich
  klein — V1 ≈ 2,9 MB, V2 ≈ 2,5 MB, je 10 s, 1280×720 (HD), H.264+AAC →
  läuft überall, lädt flott. Bedenken wegen Dateigröße damit erledigt.
- Das YouTube-Video aus Masterplan 4.4.2 bleibt davon unberührt — es dient der
  *Reichweite* (Suchtreffer), nicht als Player auf der Seite.

### 2.3 Vorteile der Vollversion 🔲
- Kurze, scanbare Funktionsliste (aus „Funktionsübersicht" im Masterplan):
  alle Eingabefälle (SSS/SWS/WSW/SWW/SSW + Umkreis/Inkreis/Fläche/Höhen),
  voller Rechenweg, CAD-Zeichnung, Export PNG/SVG/**DXF**/PDF.
- **Burggraben betonen:** die Spezialfälle (R/r/Fläche/Höhe) „kann kein anderes
  Tool" – das ist das Kaufargument.

### 2.4 Test vs. Pro 🔲
- Kleiner, **ehrlicher** Vergleich: Test rechnet Standardfälle + alle Exporte
  frei; Pro schaltet zusätzlich die Spezial-Eingabefälle frei. Kein
  Schlechtreden der Testversion – sie ist der Köder.

### 2.5 Kauf-Block 🔲
- **Preis klar: 69 €, einmalig**, keine Staffelung.
  *(Strategiewechsel: war 24 € = Hobby-Niveau; jetzt wertbasierte Profi-
  Preisgestaltung — Begründung siehe Masterplan 0.3. In `index.html` bereits
  überall auf 69 € gesetzt.)*
- **Wichtige Bedingung (aus Masterplan 0.3):** 69 € trägt nur, wenn der Kauf-
  Block den Nutzen klar belegt. Dafür liegt im Masterplan fertiges Material
  bereit („Warum 69 €?") — beim Füllen einarbeiten:
  - Spart bei jedem Auftrag Zeit (Geometrie sofort als DXF an die Maschine).
  - Einmal zahlen, dauerhaft nutzen — **kein Abo**.
  - Läuft offline/eigenständig — kein Konto, kein Datenabfluss.
  - Risikofrei: Gratis-Test mit allen Standardfällen vor dem Kauf.
  - Spezialist statt überladenes CAD.
  - Für Profis als Betriebsausgabe absetzbar.
  - *Kernsatz:* „Ein einziger gesparter Auftrag, und das Werkzeug hat sich
    gelohnt."
- Großer Digistore24-Knopf. Daneben Vertrauens-Stichpunkte: sofortiger Download,
  läuft offline, keine Installation, sichere Abwicklung über Digistore24.

### 2.6 FAQ 💡
- *Später/optional:* 4–6 kurze Fragen (Läuft es offline? Brauche ich Internet?
  Was ist DXF? Mac/Windows?). Senkt Kauf-Hürden, ist aber kein Muss zum Start.

### 2.7 Footer 🔲
- Links zu `impressum.html` + `datenschutz.html`.
- §19-Hinweis kurz, Kontakt-E-Mail, Copyright. Schlicht halten.

---

## Phase 3 – Recht & Datenschutz (eigene Unterseiten)

### 3.1 impressum.html 🔲
- Inhalt aus `Pflichttexte_Entwurf.md`, Abschnitt 1 (inkl. Telefon – das darf
  online stehen, nur die frei verteilte Tool-Datei bleibt ohne Telefon).
- Gleiche Design-Tokens wie die Landingpage, „zurück"-Link.

### 3.2 datenschutz.html 🔲
- Inhalt aus `Pflichttexte_Entwurf.md`, Abschnitt 2 (GitHub Pages, Server-Logs,
  E-Mail-Kontakt, externe Links, Digistore24, keine Cookies/Analyse).

### 3.3 Beweis: keine externen Ressourcen 🔲
- Browser-Entwicklertools → Tab „Netzwerk" → Seite laden: es darf **nichts** von
  fremden Domains geladen werden (keine Fonts, keine Skripte, keine Tracker).
  Erst dann stimmt die Datenschutzerklärung.

---

## Phase 4 – Feinschliff & Go-Live

### 4.1 Mikro-Animationen 💡
- Dezentes Einblenden beim Scrollen, sanfter Knopf-Hover – sparsam, „ruhig".
- `@media (prefers-reduced-motion)` respektieren (wie schon im Tool).

### 4.2 SEO-Basics 🔲
- Aussagekräftiger Titel/Description; sprechende Überschriften. Optional ein
  eigenes Vorschaubild (OG-Image) **aus dem eigenen Ordner**, nicht extern.

### 4.3 Selbstcheck 🔲
- Lädt schnell, Datei schlank, auf den drei Geräteklassen sauber, alle Links ok.

### 4.4 In GitHub-Ordner legen 🔲
- Landingpage (`index.html`) + `impressum.html` + `datenschutz.html` +
  Testversion + evtl. ein Bild → in `dt-profidreieck-web`. **Nie die Pro-Datei.**

### 4.5 Domain-Verknüpfung 🔲
- DNS-Schritte stehen im Masterplan (2.7). Hier nur der Verweis, damit die Seite
  unter `dt-profidreieck.de` erscheint.

---

## 💬 Noch zu besprechen (Diskussions-Agenda)
1. Bilder-Strategie konkretisieren (0.5): reicht inline-SVG, oder wollen wir
   einen echten Handy-Screenshot der App im Hero?
2. Dateinamen festzurren: `index.html` für die Landingpage — ✅ entschieden.
3. Brauchen wir ein kleines Sprungmenü oben, oder reicht reines Scrollen?
   — *im Grundgerüst sind beide drin: Sprungmenü ab Tablet-Breite + Scrollen.*
4. FAQ (2.6) — zum Start mit dabei oder bewusst später?
5. **`app-eingabe.jpg` zeigt die Test-Lizenzzeile** „Karl Mustermann –
   Schlüssel 1234…". Für den echten Online-Auftritt später einen Screenshot
   OHNE diese Zeile machen und austauschen. — 🔲
6. *Optionaler Feinschliff (aus Live-Analyse 09.06.2026, keine Fehler):*
   - **Link-Stil vereinheitlichen:** Videos relativ (`V2.mp4`), Bilder absolut
     (`https://dt-profidreieck.de/app-…jpg`). Beides läuft; bei Gelegenheit auf
     einen Stil bringen (relativ ist am robustesten). — 💡
   - **Dichte Hero→Video prüfen:** Hero zeigt `app-zeichnung.jpg`, direkt darunter
     das Werkstattvideo. Inhaltlich gut; falls es zu „voll" wirkt, später Bild
     vs. Video gegeneinander abwägen. Reine Geschmacksfrage. — 💡

---

## 📝 Changelog
```
v0.4.2 (2026-06-09)
  - Live-Analyse von www.dt-profidreieck.de + Prüfung der Originaldateien V1/V2:
    Seite läuft sauber, beide Videos eingebettet & abspielbar, Preis 69 €
    durchgängig, Bilder laden, Recht verlinkt, keine externen Ladequellen.
  - Video-Specs bestätigt (in 2.2 vermerkt): V1 ≈ 2,9 MB / V2 ≈ 2,5 MB, je 10 s,
    720p, H.264+AAC → ideal, Größen-Bedenken erledigt.
  - Zwei optionale Feinschliff-Punkte aufgenommen (Agenda 6): Link-Stil
    vereinheitlichen (relativ vs. absolut); Dichte Hero→Video im Blick behalten.
  - Bleibt offen: echter Digistore-Kauf-Link (zeigt noch auf #), sauberer
    Eingabe-Screenshot ohne Lizenzzeile.

v0.4.1 (2026-06-07)
  - Praxis-Beweis (2.2) umgesetzt & live: statt geplantem YouTube-Link jetzt
    ZWEI eigene MP4-Videos direkt eingebettet (V2 = Werkstatt, V1 = App-Demo),
    von Dieter getestet. Datenschutz weiterhin sauber, da MP4s aus dem eigenen
    GitHub-Ordner laden (keine fremden Server). 2.2 auf ✅ gesetzt.
  - Hinweis ergänzt: Videodateien klein/komprimiert halten (GitHub-Grenzen
    50/100 MB); YouTube-Video aus Masterplan 4.4.2 bleibt separat für Reichweite.

v0.4.0 (2026-06-07)
  - Abgleich mit Masterplan v0.17.0 + von Dieter erweiterter index.html.
  - PREIS 24 € → 69 € überall im Plan nachgezogen (Hero, Checkliste 2.5,
    Abschnitt 2.5). Hintergrund: wertbasierte Profi-Preisgestaltung statt
    Hobby-Niveau (Masterplan 0.3). In index.html bereits an allen drei Stellen
    (Kopfleiste, Hero, Kauf-Block) auf 69 € gesetzt — bestätigt.
  - Preisbegründung „Warum 69 €?" aus Masterplan 0.3 als Baumaterial in 2.5
    aufgenommen (Zeitersparnis, kein Abo, offline, risikofrei, absetzbar,
    Kernsatz „ein gesparter Auftrag …").
  - Realstand der Checkliste korrigiert: Seite ist LIVE unter
    dt-profidreieck.de (HTTPS aktiv). 4.4 (hochgeladen) + 4.5 (Domain) ✅;
    4.1 (Mikro-Animation) ✅; Footer 2.7 ✅. Hero/Vorteile/Kauf stehen im
    Grundgerüst (~), Feinschliff der Texte offen.
  - Weiterhin offen (Zutaten): echter Digistore-Kauf-Link (Masterplan 3.5),
    YouTube-Video (4.4.2), sauberer Eingabe-Screenshot ohne Lizenzzeile,
    Test-vs-Pro-Sektion (2.4), optionale FAQ (2.6), OG-Bild (4.2).

v0.3.1 (2026-06-07)
  - Live-Test bestätigt: ganze Seite über GitHub Pages geprüft
    (dietertepe.github.io/dt-profidreieck-web). index.html + impressum.html +
    datenschutz.html laden korrekt, alle internen Links greifen, Bilder werden
    geladen, kein 404 mehr. Phase 3 auf „gebaut & live getestet" gesetzt.
  - Weiterhin offen (nur Zutaten, kein Bauaufwand): Digistore-Kauf-Link (3.5),
    YouTube-Video (4.4.2), sauberer Eingabe-Screenshot ohne Lizenzzeile (Agenda 5).

v0.3.0 (2026-06-07)
  - Phase 3 gebaut: impressum.html + datenschutz.html im Landingpage-Design,
    Inhalt 1:1 aus Pflichttexte_Entwurf (Abschnitt 1 + 2). „← Zur Startseite"-
    Link, noindex, dezenter Entwurfs-Hinweis. Datenschutz-Check bestanden
    (keine externen Ladequellen). Footer-Links der Landingpage greifen damit.
  - OS-Plattform-Pflicht geprüft: zum 20.07.2025 entfallen → korrekterweise
    KEIN OS-Link im Impressum; §36-VSBG-Hinweis bleibt drin. Impressum für den
    geplanten Fall (Kleinunternehmer, kein Handelsregister) vollständig.
  - 3.1–3.3 abgehakt.

v0.2.0 (2026-06-07)
  - Phase 1 (Grundgerüst) gebaut und LIVE getestet: index.html + 3 Bilder
    (app-zeichnung/app-eingabe/app-ergebnis.jpg). Werkstatt-Blueprint-Stil,
    Design-Tokens aus der App, responsive, Sprunganker, Sektionen Hero/Beweis/
    Vorteile/Kauf/Footer. Datenschutz-Check bestanden (keine externen Ladequellen).
  - Auf dem Handy bestätigt; der „Gratis testen"-Knopf startet die Testversion.
  - 1.1–1.5 abgehakt; Dateiname index.html entschieden (Agenda 2).
  - Neuer offener Punkt (Agenda 5): app-eingabe.jpg zeigt noch die Test-
    Lizenzzeile → später durch sauberen Screenshot ersetzen.
  - Weiterhin Platzhalter: Digistore-Kauf-Link (Masterplan 3.5), YouTube-Video
    (4.4.2), Impressum/Datenschutz-Seiten (Phase 3).

v0.1.0 (2026-06-07)
  - Erste Fassung des Landingpageplans im Masterplan-Stil.
  - Entscheidungen festgehalten: Stil = Werkstatt-Blueprint (App-Designsprache,
    Bauprinzipien von Linear/Raycast/Paddle, NICHT deren Dark-Look); Sprache =
    nur Deutsch (EN später als eigene Seite); Technik = Single-File, keine
    externen Schriften/Skripte, offline-tauglich, YouTube nur verlinkt.
  - Vorgehen festgelegt: Grundgerüst zuerst (Phase 1, alle Links verdrahtet +
    testbar), dann Sektion für Sektion füllen (Phase 2).
  - Phasen 0–4 angelegt; Inhalt der Sektionen an Masterplan 4.2 + Funktions-
    übersicht angedockt; Recht/Datenschutz aus Pflichttexte_Entwurf verknüpft.
  - Offene Punkte: Bilder-Strategie (0.5), Dateinamen, Sprungmenü, FAQ.
```
