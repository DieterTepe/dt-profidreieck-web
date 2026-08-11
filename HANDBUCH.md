# DT-ProfiTools — Projekthandbuch

**Landingpage für vier Berechnungsprogramme**
Stand: 11. August 2026 · index.html v1.3.0

> Dieses Dokument ist die Übergabe an alle, die künftig an der Seite arbeiten —
> Mensch oder KI. Es beschreibt, **was** existiert, **warum** es so gebaut ist und
> **wie** man es ändert, ohne etwas kaputtzumachen.
> Wer nur schnell etwas ändern will: Kapitel 3 (Häufige Aufgaben) reicht meistens.

---

## 1. Das Projekt in fünf Sätzen

Dieter Tepe entwickelt vier Berechnungsprogramme für Werkstatt, Konstruktion und
Ausbildung. Jedes Programm ist **eine einzige HTML-Datei**, die offline im Browser
läuft — ohne Installation, ohne Konto, ohne Internetverbindung. Diese Landingpage
bewirbt alle vier, verlinkt die kostenlosen Testversionen und führt zum Kauf über
Digistore24. Sie liegt als statische Seite auf GitHub Pages. Verkauft wird als
Kleinunternehmer nach § 19 UStG.

| Pos. | Produkt | Preis | Regelwerk | Farbe |
|---|---|---|---|---|
| 01 | DT-ProfiDreieck | 69 € | Dreiecksgeometrie, DXF-Export | Petrol-Teal `#0d7d8c` |
| 02 | DT-ProfiSchraube | 159 € | VDI 2230 Blatt 1 | Messing `#b9791c` |
| 03 | DT-ProfiPassung | 139 € | ISO 286, DIN 7190, ISO 2768 | Grün `#0f9d6e` |
| 04 | DT-ProfiSchweissnaht | 169 € | EN 1993-1-8, EN 1011-2, EN ISO 2553 | Glut-Orange `#d4560a` |

---

## 2. Die eisernen Regeln

Diese Punkte sind nicht verhandelbar. Sie sind der Grund, warum die Seite so
aussieht, wie sie aussieht.

**2.1 Keine fremden Server.** Keine CDN-Einbindung, keine Google Fonts, kein
Analytics, keine JavaScript-Bibliothek von außerhalb. Alle Schriften sind
System-Schriften, alle Bilder und Videos liegen im eigenen Repository, alle
Symbole sind Inline-SVG. Grund: strikte DSGVO-Linie ohne Cookie-Banner. Wer eine
externe Ressource einbaut, macht die Datenschutzerklärung unwahr.

**2.2 Keine Cookies, kein Speicher.** Weder `localStorage` noch `sessionStorage`
noch Cookies. Die Sprachwahl hängt ausschließlich am Adressparameter `?lang=`.

**2.3 Offline-Philosophie.** Was für die Programme gilt, gilt auch für die Seite:
so wenig Abhängigkeiten wie möglich, alles in wenigen Dateien.

**2.4 Erst besprechen, dann bauen.** Bei größeren Änderungen erst Konzept
abstimmen, dann umsetzen. Nach jeder Lieferung testet Dieter am Handy und gibt
Rückmeldung.

**2.5 Werbetexte nur nach Vorlage.** Für DT-ProfiSchweissnaht gilt die Datei
`Werbung.md` verbindlich — siehe Kapitel 7. Dort steht, was **nicht** geschrieben
werden darf.

---

## 3. Häufige Aufgaben (das Wichtigste zuerst)

### 3.1 Digistore-Kauflinks eintragen

Datei: **`config.js`**, ganz oben. Platzhalter ersetzen:

```js
kaufDreieck:      "#kauf-dreieck",        →  "https://www.digistore24.com/product/…"
kaufSchraube:     "#kauf-schraube",
kaufPassung:      "#kauf-passung",
kaufSchweissnaht: "#kauf-schweissnaht",
```

Solange der Platzhalter steht, springt der Button nur zum Kaufblock auf der Seite —
das ist Absicht, damit nichts kaputt wirkt. **Die index.html wird dabei nicht
angefasst.**

### 3.2 Ein Bild oder Video austauschen

Datei hochladen nach `<Produkt>_Daten/bilder/` bzw. `/videos/`, dann in
`config.js` die passende Zeile auf die neue URL setzen. Fertig. Die index.html
enthält **keine** Medienpfade.

Ein leerer Eintrag `""` blendet automatisch einen gestalteten Platzhalter
„folgt in Kürze" ein — nichts geht kaputt, keine defekten Bildsymbole.

### 3.3 Einen Text ändern

Deutschen Text direkt in der `index.html` ändern. **Wichtig:** Wenn der Satz
übersetzt sein soll, muss im Wörterbuch am Dateiende der **alte deutsche Satz als
Schlüssel** durch den neuen ersetzt werden — sonst bleibt die Stelle in EN/PT
deutsch (kaputt geht nichts, es fällt nur auf Deutsch zurück).

### 3.4 Einen Preis ändern

Der Preis steht an vier Stellen pro Produkt: Hero-Werkzeugkarte, Kaufblock,
Vergleichstabelle, Schluss-CTA. Zusätzlich im Wörterbuch (z. B. `"Dreieck · 69 €"`)
und in `og-card.jpg` sowie in der Abspannkarte des Teaser-Videos.

### 3.5 Ein fünftes Produkt ergänzen

Reihenfolge, die sich bewährt hat:

1. Ordner `<Produkt>_Daten/bilder/` und `/videos/` im Repo anlegen
2. Farb-Token in `:root` ergänzen (Haupt-, Dunkel- und Softton)
3. Hilfsklassen ergänzen: `.pos--x`, `.eyebrow--x`, `.btn--x`, `.tool--x`,
   `.feature--x .ico`, `.compare thead th:nth-child(n)`
4. Hero-Werkzeugkarte, Produktsektion `<section id="…">`, Navigationseintrag,
   Vergleichsspalte, Schluss-CTA-Button
5. Block in `config.js` (Kauf- und Testlink, Medien mit Kommentaren)
6. Zuweisungen im Verteiler am Ende der index.html
7. Wörterbuch-Einträge für EN/PT
8. `og-card.jpg` neu erzeugen, Impressum und Datenschutz ergänzen

---

## 4. Dateien und Ordner

### 4.1 Im Hauptverzeichnis (GitHub Pages Wurzel)

| Datei | Inhalt |
|---|---|
| `index.html` | Die komplette Landingpage: HTML, CSS, Verteiler, Wörterbuch. ~1390 Zeilen |
| `config.js` | **Einzige Stellschraube** für alle Links und Medien. ~150 Zeilen |
| `impressum.html` | § 5 DDG, § 18 MStV, Kleinunternehmer, Haftung, nur deutsch |
| `datenschutz.html` | DSGVO, GitHub Pages, Digistore24, nur deutsch |
| `info.html` | Informationsseite (Ziel des „i"-Buttons), nur deutsch |
| `DT-ProfiDreieck_Test_1-1-0.html` | Testversion, die auf diesem Repo liegt |

### 4.2 Medien-Unterordner

```
Dreieck_Daten/      bilder/  app-zeichnung.jpg · app-eingabe.jpg · app-ergebnis.jpg
                    videos/  V1.mp4 · V2.mp4
Schraube_Daten/     bilder/  schraube-start · -rechenweg · -schaubild
                             · -flansch · -hilfe · -word .jpg
                    videos/  schraube-teaser.mp4
Passung_Daten/      bilder/  passung-start · -schaubild · -rechenweg
                             · -assistent · -pressverband · -beratung .jpg
                    videos/  passung-teaser.mp4
Schweissnaht_Daten/ bilder/  schweissnaht-start · -nahtbild · -rechenweg
                             · -assistent · -proben · -grenzen .jpg
                    videos/  schweissnaht-teaser.mp4
Landigpage_Daten/   favicon.svg · favicon.png · apple-touch-icon.png · og-card.jpg
```

> Der Ordnername `Landigpage_Daten` enthält einen Tippfehler (fehlendes „n").
> **Nicht korrigieren** — er steht so in der index.html und auf GitHub. Eine
> Umbenennung müsste an vier Stellen im `<head>` nachgezogen werden.

### 4.3 Testversionen (eigene Repositories)

| Produkt | Adresse |
|---|---|
| Dreieck | `dt-profidreieck-web/DT-ProfiDreieck_Test_1-1-0.html` |
| Schraube | `dt-profischraube-web/DT-ProfiSchraube_Test.html` |
| Passung | `dt-profipassung-web/DT-ProfiPassung_Testversion.html` |
| Schweissnaht | `dt-profischweissnaht-web/DT-ProfiSchweissnaht_Testversion.html` |

> **Sicherheitsregel:** In den öffentlichen Repositories darf **niemals** eine
> Vollversion liegen — sie wäre ohne Kauf herunterladbar. Vollversionen gehören
> ausschließlich in den geschützten Downloadbereich von Digistore24.

---

## 5. Aufbau der index.html

Die Datei ist bewusst eine einzige Datei und von oben nach unten lesbar:

```
<head>
  Meta, Favicons, Open-Graph-Karte      ← feste Pfade, KEIN config.js!
  <script src="config.js">              ← muss im head stehen
  Wartungskommentar                     ← erklärt Aufbau und Regeln
  <style>  1) Tokens  2) Basis  3) Bausteine  4) Sektionen
<body>
  Kopfleiste (Navigation, Sprachumschalter, „i")
  Hero mit vier Werkzeugkarten
  Warum-Sektion
  Pos. 01 Dreieck · Pos. 02 Schraube · Pos. 03 Passung · Pos. 04 Schweissnaht
  Vergleichstabelle · FAQ · Schluss-CTA · Fußzeile
  <script> Verteiler   (Links + Medien aus config.js)
  <script> Einblendung (IntersectionObserver)
  <script> Sprachen    (Wörterbuch + Umschaltlogik)
```

Sektions-IDs: `start`, `warum`, `dreieck`, `schraube`, `passung`, `schweissnaht`,
`vergleich`, `faq`. Kaufblock-IDs: `kauf-dreieck`, `kauf-schraube`,
`kauf-passung`, `kauf-schweissnaht`.

### 5.1 Der Verteiler — warum es ihn gibt

Im HTML stehen bei Bildern und Videos **leere** `src`-Attribute mit einer
eindeutigen ID (27 Stück). Ein Skript am Dateiende trägt die Pfade beim Laden aus
`config.js` ein:

```js
bild("img-schweissnaht-nahtbild", w.bildNahtbild);
video("video-schraube-teaser", s.videoTeaser, s.bildStart);   // 3. Wert = Poster
```

Fehlt eine URL, bekommt der umgebende `.media-slot` die Klasse `.media-missing`
und zeigt den Text aus `data-hinweis` statt eines defekten Bildes.

**Links** laufen bewusst **nicht** über IDs, sondern über `data-link="kauf-passung"`.
Grund: Mehrere Buttons teilen sich denselben Link (Kaufblock und Schluss-CTA),
IDs müssen aber eindeutig sein.

### 5.2 Die Sprachumschaltung

- **Deutsch steht fest im HTML.** Ohne JavaScript zeigt die Seite korrektes
  Deutsch — wichtig für die Social-Vorschau und für Suchmaschinen.
- **EN und PT liegen im Wörterbuch** `I18N` am Dateiende (~180 Einträge).
  Schlüssel = der deutsche Satz, Wert = `["English", "Português"]`.
- Beim Umschalten werden alle Textknoten durchlaufen und ersetzt; der deutsche
  Originaltext bleibt im Speicher, damit zurückgeschaltet werden kann.
- **Fehlt ein Eintrag, bleibt Deutsch stehen** — es gibt keine Fehlermeldung und
  keine leere Stelle. Das macht das Wörterbuch gutmütig gegenüber Textänderungen.
- Elemente mit farbigen Teilstücken (Überschriften mit `<span>`) tragen
  `data-i18n-html="…"` und werden über `I18N_HTML` **komplett** ersetzt, weil sich
  die Wortstellung zwischen den Sprachen unterscheidet.
- Die Wahl hängt an `?lang=en` bzw. `?lang=pt`; beim ersten Besuch entscheidet die
  Browsersprache. Kein Cookie, kein Speicher.
- Bewusst **nicht** übersetzt: Produktnamen, Preiszahlen, Normkürzel (VDI, ISO,
  DIN, EN, DXF), E-Mail-Adresse, Zeile mit Copyright.
- Noch **offen**: die unsichtbaren `alt`-Bildbeschreibungen sind deutsch.

### 5.3 Gestaltung

Werkstatt-Blueprint: heller Hintergrund, weiße Karten, dunkle Panels mit
Rasterlinien für Screenshots und Videos. Alle Farben und Abstände sind Tokens in
`:root`. Positionsnummern („Pos. 01 · Geometrie") sind die optische Signatur der
Seite — sie zitieren eine technische Stückliste.

Zwei Details, die aus Fehlern gelernt wurden:

- `.grid-3 > .shot { align-self: start; }` verhindert, dass sich Kacheln in einer
  Dreierreihe auf die Höhe der höchsten strecken und weiße Flächen entstehen.
- Screenshots werden **nicht** beschnitten (kein `object-fit: cover`), weil sie
  Rechenwege und Zahlen zeigen, die vollständig lesbar bleiben müssen.

---

## 6. Rechtliches

- **Impressum**: § 5 DDG und § 18 Abs. 2 MStV, Kleinunternehmer nach § 19 Abs. 1
  UStG, Digistore24 als Reseller mit voller Anschrift, Haftungsabschnitt für die
  Berechnungsprogramme.
- **Datenschutz**: GitHub Pages als Hoster mit EU-U.S. Data Privacy Framework,
  Digistore24 als eigener Verantwortlicher, ausdrücklich keine Cookies und kein
  Tracking.
- Kein Link zur EU-Streitschlichtungsplattform — sie wurde 2025 eingestellt.
- Beide Seiten und `info.html` bleiben **deutsch**, auch wenn die Landingpage
  umgeschaltet ist. In der englischen und portugiesischen Fußzeile steht deshalb
  ein Hinweis „(in German)".

---

## 7. Textregeln für DT-ProfiSchweissnaht

Verbindlich aus `Werbung.md`. Diese Regeln schützen vor Haftung und vor falschen
Erwartungen:

**Nicht schreiben:** „normkonform", „geprüft", „sicher" als Eigenschaft des
Ergebnisses, „vollständiger Nachweis", „ersetzt den Statiker". Ermüdung,
Betriebsfestigkeit, Verzug und Schrumpfung dürfen **in keiner Form** erwähnt oder
angedeutet werden — auch nicht als „kommt später". Keine Zusage, dass Updates
kostenlos sind.

**Stattdessen:** „rechnet nach EN 1993-1-8". Die Stärken so benennen, wie das
Programm selbst auftritt: Nahtbild statt Nahtlänge, Rechenweg mit Quelle je
Schritt, mitlaufende Rechenproben, offene Liste dessen, was nicht geprüft wird.

Aus demselben Grund zeigt der Teaser vom Rechenweg-Screenshot nur die rechte
Bildhälfte: links standen die Zusatzbereiche mit „folgt in einem Update".

Die Anzahl der Rechenproben wird bewusst **nicht** genannt (`Werbung.md` spricht
von 19, ein Beispielfall zeigt 17/17 — die Zahl hängt offenbar vom Fall ab).

---

## 8. Medienproduktion

Die Teaser-Videos sind aus Standbildern erzeugt, nicht abgefilmt — die Programme
lassen sich nicht sinnvoll screen-recorden.

**Rezept (ffmpeg + Python/PIL), 40 Sekunden:**

1. Screenshots zuschneiden, Statusleiste des Tablets entfernen, auf das
   eigentliche Panel zoomen
2. Je Szene ein Bild 2560×1440 komponieren: Hintergrund = Screenshot,
   stark unscharf und abgedunkelt; darauf der scharfe Screenshot mit farbigem
   Rahmen in der Produktfarbe, Marke oben links, Untertitel unten
3. Sechs Szenen à 6 s mit langsamem Zoom (`zoompan`) und Ein-/Ausblendung, dazu
   eine Abspannkarte à 4,5 s im Blueprint-Raster mit Preis
4. Segmente mit `concat` zusammenfügen, H.264, 1280×720, `+faststart`

Web-Bilder: maximal 1500 px breit, JPG Qualität 88, progressiv, unter 300 KB.
Social-Vorschau `og-card.jpg`: exakt 1200×630.

---

## 9. Prüfliste vor jedem Hochladen

- [ ] HTML-Struktur fehlerfrei (keine offenen Tags)
- [ ] Jede Medien-ID im HTML hat eine Zuweisung im Verteiler — und umgekehrt
- [ ] Jeder `config.js`-Schlüssel wird benutzt, jeder benutzte existiert
- [ ] Keine festen Medienpfade im HTML außerhalb des `<head>`
- [ ] Keine externen Adressen außer `dietertepe.github.io` und Digistore24
- [ ] JavaScript-Syntax fehlerfrei
- [ ] Texte gegen die Regeln aus Kapitel 7 geprüft
- [ ] Test am Handy **und** am Tablet: Querformat prüfen, dort sind
      Layout-Probleme aufgetreten, die am Handy unsichtbar waren
- [ ] Sprachumschaltung in allen drei Sprachen, danach neu laden
- [ ] Alle acht Links (vier Test, vier Kauf) angeklickt

---

## 10. Offene Punkte

| Punkt | Status |
|---|---|
| Digistore-Produkte anlegen und die vier Links eintragen | **offen — letzter Schritt vor dem Verkauf** |
| Kompletter Probekauf im Testmodus, Download offline öffnen | offen |
| Prüfen, dass keine Vollversion in einem öffentlichen Repo liegt | offen |
| `alt`-Bildbeschreibungen für EN/PT übersetzen | offen, optional |
| Meta-Description und Social-Vorschau je Sprache | offen, optional |

---

## 11. Arbeitsweise mit Dieter

- Er arbeitet meist vom Tablet, gelegentlich vom PC. Große Dateien lassen sich
  vom Tablet nicht überall hochladen.
- Er schickt bei Darstellungsproblemen **Fotos vom Bildschirm** — das hat sich
  als sehr effizient erwiesen.
- Er möchte verstehen, was gebaut wird: Erklärungen in normaler Sprache, ohne
  Fachjargon, sind ausdrücklich erwünscht.
- Lieferungen kommen als fertige Dateien mit klarer Ansage, welche Datei in
  welchen Ordner gehört.
- Der Projektordner in der Chat-Oberfläche hinkt dem Stand auf GitHub manchmal
  hinterher. **Im Zweifel gilt GitHub** — vor größeren Umbauten den aktuellen
  Stand anfordern.

---

*Ende des Handbuchs. Bei Unklarheiten: `index.html` von oben nach unten lesen —
die Wartungskommentare im Kopf und an den Skripten erklären die Mechanik an Ort
und Stelle.*
