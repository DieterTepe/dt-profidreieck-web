# 📋 Masterplan: Vermarktung „DT-ProfiDreieck"

```
=============================================================================
  MASTERPLAN  –  Vermarktung der Dreiecksberechnung (Pro-Version)
=============================================================================
  Version : 0.18.1
  Stand   : 2026-06-09
  Status  : Umsetzung weit fortgeschritten – Produkt fertig & obfuskiert,
            Domain live; offen v. a. Digistore24 + Landingpage-Inhalt
  Produkt : DT-ProfiDreieck Test/Pro v1.1.0 (Engine 3.0.0), single-file,
            online & offline; live unter dt-profidreieck.de
=============================================================================
```

## So liest du dieses Dokument

Das Dokument hat **zwei Ebenen**:

- **TEIL 1 – Ablauf-Checkliste:** kurz, zum Abhaken. Hier arbeitest du dich
  Schritt für Schritt durch. Jede Zeile hat eine Nummer.
- **TEIL 2 – Ausführliche Erklärungen:** dieselben Nummern, ausführlich erklärt.
  Wenn du in der Checkliste nicht weiterweißt, springst du über die Nummer nach
  unten.

**Status-Marker** (stehen in beiden Teilen, gleich):
- ✅ **entschieden** – wir wissen, *wie* es geht; kann umgesetzt werden
- 💬 **in Klärung** – Ansatz steht, Details besprechen wir noch
- 🔲 **offen** – muss erst durchdacht werden, bevor es losgeht
- 💡 **später** – bewusst nach hinten geschoben

**Checkbox** `[ ]` = von dir in der Realität erledigt? (Noch alle leer –
Stand ist reine Planung.)

> **📁 Projektdateien (im Projektordner):**
> - `Dreiecksberechnung_3-0-0.html` – die lauffähige Vollversion = Basis für
>   Pro & Test.
> - `Pflichttexte_Entwurf.md` – Impressum + Datenschutz (Webseite) **und** die
>   fertigen Overlay-Textblöcke für Test/Pro (Abschnitt 3).
> - `Landingpageplan_DT-ProfiDreieck.md` – eigener Plan für die Verkaufsseite
>   (ergänzt 4.2/4.3); Grundgerüst + Rechtsseiten bereits live.
> - `Digistore24_Anleitung_DT-ProfiDreieck.md` – klickgenaue Laien-Anleitung für
>   Phase 3 (Konto, Produkt, Tresor, Lizenzschlüssel, Bestell-Link, Testkauf).
> Ein neuer Chat sollte beide lesen. Die konkrete Bauanleitung steht unten im
> Anhang „Bauanleitung für einen neuen Chat".

---

# TEIL 1 — ABLAUF-CHECKLISTE (zum Abhaken)

> Reihenfolge = empfohlene Abarbeitung. Hake ab, was du wirklich erledigt hast.
> Die Nummer führt dich zur ausführlichen Erklärung in Teil 2.

### Phase 0 – Strategie (Grundentscheidungen)
- [x] **0.1** Zielkunde: Profis zuerst, Schule als 2. Welle — ✅
- [x] **0.2** Kopierschutz: Ehrlichkeitsprinzip + Wasserzeichen — ✅
- [x] **0.3** Preis: 69 €, einmalig, ohne Staffelung — ✅

### Phase 1 – Fundament (Branding & Recht)
- [x] **1.1** Domains `dt-profidreieck.de` + `.com` sichern — bei INWX registriert ✅
- [ ] **1.2** Kleingewerbe beim Gewerbeamt Hörstel anmelden — ⚠️ Voraussetzung für Digistore-Auszahlung; **erledigt? bitte bestätigen**
- [x] **1.3** Pflichttexte (Impressum + Datenschutz) fertiggestellt — live auf der Webseite + in beiden Tool-Overlays ✅

### Phase 2 – Technik & Sicherheit (die HTML-Dateien)
- [x] **2.0a** Zweisprachigkeit DE/EN (in beiden Dateien umgesetzt)
- [x] **2.0b** Editions-APP-Block — Test ✅ und Pro ✅ (beide DT-ProfiDreieck 1.1.0 / Engine 3.0.0)
- [x] **2.0c** Overlay-Ordnung; DE/EN-Schalter neben Info sichtbar
- [x] **2.1** Konzept Zwei-Dateien (Test + Pro getrennt) – beide Dateien existieren
- [x] **2.2** Pro-Datei: Lizenz-Modal (Name + Schlüssel, kein prompt) umgesetzt
- [x] **2.3** Impressum/Info-Overlay — Test ✅ und Pro ✅ (inkl. §19-Satz)
- [x] **2.4** Testversion: Spezial-Pills gesperrt + Upsell-Texte; Exporte frei
- [x] **2.5** Beide Dateien obfuskiert (nur Script; HTML/CSS/IDs geprüft intakt) — finaler Funktionstest (DXF+Modal+SSW) läuft
- [x] **2.6** Hosting Teil 1: Repo `dt-profidreieck-web` + Pages — live mit obfuskierter Testversion + index + Rechtsseiten (Inhalts-Feinschliff der Landingpage läuft)
- [x] **2.7** Hosting Teil 2: Domain (INWX) → GitHub — live unter `dt-profidreieck.de` (HTTPS aktiv) ✅

### Phase 3 – Vertrieb & Auslieferung (Digistore24)
- [ ] **3.1** Digistore24-Verkäuferkonto erstellen + einrichten (Telefon, Steuer = Kleinunternehmer, Bank, 2FA) — ✅
- [x] **3.2** Reseller-Prinzip verstehen (Steuern laufen automatisch) — ✅
- [ ] **3.3** Produkt anlegen + Pro-Datei in Tresor + Lizenzschlüssel aktivieren — 💬
- [ ] **3.4** Preis 69 € eintragen — ✅
- [ ] **3.5** Verkaufs-Link erzeugen — ✅
- [ ] **3.6** Automatische Auslieferung einrichten/testen — ✅
- [ ] **3.7** Buchhaltung: Auszahlungs-PDFs sammeln — ✅
- [ ] **3.8** Jährlich: Summe in „Anlage EÜR" eintragen — ✅

### Phase 4 – Marketing & Reichweite
- [x] **4.1** Rolle der Gratis-Testversion als Köder verstehen — ✅
- [~] **4.2** Landingpage-Inhalt festlegen (4 Blöcke) — Struktur steht; Inhalts-Sektionen werden gefüllt
- [~] **4.3** Landingpage technisch erstellen — Grundgerüst + Rechtsseiten live & geprüft; Inhalt folgt (s. Landingpageplan)
- [ ] **4.4** Reichweite aufbauen (Pull + Push) — ✅
  - [ ] **4.4.1** In 2–3 Gruppen + 1–2 Foren stöbern, Regeln & Fragen sammeln — ✅
  - [ ] **4.4.2** YouTube-Reihe: mit DXF-Video starten — ✅
- [ ] **4.5** Aktuelle Kosten/Gebühren überall prüfen (vor Start) — 🔲

> **🔧 Noch einzubinden / offene Aktionen (Stand 07.06.2026):**
> 1. **Gewerbe (1.2):** bestätigen, dass das Kleingewerbe angemeldet ist
>    (Voraussetzung für die Digistore-Auszahlung).
> 2. **index.html mit 69 €** auf GitHub hochladen (falls noch nicht geschehen).
> 3. **Digistore (Phase 3):** Konto einrichten → Produkt anlegen → Pro-Datei in
>    den Tresor → Lizenzschlüssel-Automatik.
> 4. **Kauf-Link einbinden (3.5):** echten Digistore-Warenkorb-Link statt des
>    Platzhalters `#` in `index.html`.
> 5. **Landingpage-Inhalte (4.2/4.3):** Hero/Beweis/Vorteile/Test-vs-Pro/Kauf
>    füllen (Landingpageplan) – inkl. der „Warum 69 €?"-Texte aus 0.3.
> 6. **Screenshot ersetzen:** `app-eingabe.jpg` zeigt noch „Karl Mustermann –
>    Schlüssel 1234" → sauberes Bild ohne Lizenzzeile.
> 7. **YouTube-DXF-Video (4.4.2)** erstellen + auf der Seite verlinken.
> 8. **Optional:** `.com` → `.de` weiterleiten; E-Mail-Weiterleitung
>    `info@dt-profidreieck.de` → `Dieter.Tepe@live.de`.

---

# TEIL 2 — AUSFÜHRLICHE ERKLÄRUNGEN

## Phase 0 – Strategische Grundentscheidungen

### 0.1 Zielkunde & Reihenfolge ✅
- **Welle 1 – Profis/Werkstatt** (CNC, Metallbau, Tischlerei): DXF-Export
  konkurrenzlos, höchste Zahlungsbereitschaft, direkter Verkauf.
- **Welle 2 – Schule & Ausbildung** (später): Produkt kann es ohnehin; wird nur
  noch nicht aktiv beworben.
- **Warum nacheinander:** Das Produkt bedient beide, das *Marketing* nicht
  gleichzeitig – verschiedene Orte, verschiedene Worte. Erst an Welle 1 lernen.

### 0.2 Kopierschutz-Philosophie ✅
- **Variante A (Ehrlichkeitsprinzip):** Eine einzelne HTML-Datei lässt sich
  technisch nicht am Kopieren hindern. Kein Online-Lizenzserver, weil das
  „offline, eine Datei" zerstören würde.
- **Echtes Leck** ist nicht der Hacker, sondern der hilfsbereite Kunde, der die
  Datei weitergibt. → Gegenmittel: Obfuscation + Wasserzeichen (siehe 2.2/2.5).

### 0.3 Preis & Positionierung ✅
- **69 €, einmalig, ohne Staffelung, kein Abo.**
- **Wertbasierte Profi-Preisgestaltung.** Marktrecherche (07.06.2026): Große
  CAD/CAM-Suiten 5.000–15.000 $ + Wartung; fokussierte Einzweck-Werkzeuge als
  Einmalkauf real ~15–150 €. DT-ProfiDreieck ist ein fokussiertes **Profi**-Tool
  → oberes Drittel dieser Klasse. 24 € war Hobby-Niveau und ließ Marge liegen.
- **Bedingung:** 69 € trägt nur, wenn die Landingpage den Nutzen klar belegt
  (Zeitersparnis, DXF direkt an die CNC, offline, einmalig statt Abo).
- 💡 Studenten-/Volumenstaffel kommt mit Welle 2.

> **💬 Preisbegründung „Warum 69 €?" (für die Landingpage verwendbar):**
> - **Spart bei jedem Auftrag Zeit:** Geometrie sofort gelöst und als DXF direkt
>   an die Maschine – das Werkzeug hat sich nach wenigen Einsätzen bezahlt.
> - **Einmal zahlen, dauerhaft nutzen – kein Abo.** Anders als die meisten
>   Werkstatt-Programme keine monatlichen Kosten.
> - **Läuft offline und eigenständig:** kein Internet, keine Cloud, kein Konto –
>   auf jedem Gerät in der Werkstatt, ohne laufende Kosten und ohne Datenabfluss.
> - **Risikofrei:** kostenlose Testversion mit allen Standardfällen – man kauft
>   erst, wenn man überzeugt ist.
> - **Spezialist statt überladenes CAD:** macht eine Sache richtig gut
>   (Dreiecke → DXF/SVG/PNG/PDF), ohne teure CAD-Komplexität.
> - **Für Profis:** als Betriebsausgabe absetzbar; 69 € einmalig sind gegenüber
>   dem Zeitgewinn im Werkstattalltag minimal.
> - *Kernsatz:* „Was kostet eine halbe Stunde Rechnen und Zeichnen pro Auftrag?
>   Ein einziger gesparter Auftrag, und das Werkzeug hat sich gelohnt."

---

## Phase 1 – Das Fundament (Branding & Rechtliches)

### 1.1 Domains sichern ✅
- `dt-profidreieck.de` (deutscher Markt) + `.com` (Markenschutz).
- 💲 ca. 15–30 €/Jahr für beide *(beim Anbieter prüfen)*.

### 1.2 Gewerbe anmelden ✅
- „Kleingewerbe für Softwarevertrieb" beim Gewerbeamt Hörstel; Finanzamt
  verknüpft mit der vorhandenen Steuernummer.
- 💲 ca. 20–30 € einmalig *(bei der Stadt prüfen)*.

### 1.3 Pflichttexte für die Webseite ✅
- **Generator-Weg gewählt** (statt Anwalt). Entwurf für Impressum &
  Datenschutzerklärung liegt vor (Datei „Pflichttexte_Entwurf").
- Nötig: Impressum (§ 5 DDG), Datenschutzerklärung, Widerrufsverzicht bei
  digitalen Produkten (Letzteres deckt Digistore24 als Reseller ab).
- **Steuerstatus entschieden: Kleinunternehmer (§ 19 UStG).**
  - *Bedeutung:* Du schlägst keine Umsatzsteuer auf und machst keine
    monatlichen Meldungen; Einnahmen einmal jährlich in der Einkommensteuer-
    erklärung. Umsatzgrenzen seit 2025: **Vorjahr ≤ 25.000 €**, laufendes Jahr
    ≤ 100.000 € (gilt für ALLE gewerblichen Tätigkeiten zusammen). Für ein
    Nebenprojekt reichlich Luft.
  - *Zusammenspiel Digistore24:* Digistore ist Wiederverkäufer → schlägt dem
    Endkunden die Steuer auf und führt sie ab; an dich zahlt es die Provision
    netto aus. Du verkaufst rechtlich nur an Digistore.
  - *Im Impressum:* statt USt-IdNr der Satz „Gemäß § 19 UStG wird keine
    Umsatzsteuer berechnet und folglich auch nicht ausgewiesen."
  - *Hinweis:* kein Steuerrat; im Zweifel mit dem Finanzamt gegenchecken.

---

## Phase 2 – Technik & Sicherheit (die HTML-Dateien)

> Wichtig: Das lesbare Original bleibt **immer lokal** auf deinem PC.
> Hochgeladen werden nur verschlüsselte Fassungen.

### 2.0 Quellcode-Ausbau (Editionen + Zweisprachigkeit) – VOR dem Test/Pro-Split

> **📦 Aktueller Build-Stand (Stand 07.06.2026):**
> - **Beide Editionen fertig & obfuskiert.** APP-Schema einheitlich:
>   `name:'DT-ProfiDreieck', edition:'Test'|'Pro', version:'1.1.0', engine:'3.0.0'`.
>   - Test: DE/EN, Spezial-Pills gesperrt + Upsell, Eigenwerbungs-Banner. ✅
>   - Pro: Overlay „… Pro v1.1.0 (Engine 3.0.0)", §19-Satz, Lizenz-Modal +
>     Wasserzeichen, keine Spezial-Sperre (Pro = alles). ✅
> - **Datei-Konvention:** lesbare Master = `…_Orginal.html`; Verteildateien =
>   obfuskiert (nur `<script>`; CSS/HTML/IDs geprüft intakt). **WICHTIG:
>   Änderungen immer am `_Orginal`, danach neu obfuskieren.**
> - **Live auf GitHub Pages** (`dietertepe.github.io/dt-profidreieck-web/`):
>   `index.html` (Landingpage) ruft die **obfuskierte** `DT-ProfiDreieck_Test_1-1-0.html`
>   auf; `impressum.html` + `datenschutz.html` verlinkt und geladen; keine
>   externen Ladequellen. ✅
> - **Pro-Datei wird NICHT öffentlich gehostet** – sie kommt nur in den
>   Digistore24-Tresor (Phase 3).
> - Logik-Korrektheit: Dieters Funktionstest (erste Durchläufe fehlerfrei).


> Diese Punkte verändern nur **UI/Verpackung** – die **Engine (Mathematik)
> bleibt 3.0.0**, unverändert. Solver/Geometry/Renderer/Narrator NICHT anfassen.
> Verbindliche Detailvorgaben siehe „Bauanleitung → Verbindliche Bauvorgaben".

**2.0a – Zweisprachigkeit DE/EN ✅**
- Einfaches **I18N-Wörterbuch** (`I18N = { de:{…}, en:{…} }`), kein Framework;
  feste UI-Texte durch Nachschlag ersetzen; **Standard Deutsch**; Auswahl in
  `localStorage`.
- **Übersetzt:** UI-Labels, Buttons, **Grid-/Ergebnis-Beschriftungen**
  (Seiten/Sides, Winkel/Angles, Fläche/Area, Umkreis/Circumradius …).
- **Bleibt IMMER Deutsch:** **Narrator (Rechenweg)**, **Solver-Fehlermeldungen**,
  Impressum & Datenschutz → bleibt rechtlich ein deutsches Produkt.
- **DE/EN-Toggle sichtbar neben dem Info-Button** (`#infoBtn`).
- Im **EN-Modus** Hinweis anzeigen: „Legal information in German only."

**2.0b – Editions-Namen + Versionierung ✅ (gelöst)**
- `APP`-Block neu strukturieren:
  - `APP.name = 'DT-ProfiDreieck'`
  - `APP.edition = 'Pro'` bzw. `'Test'`
  - `APP.version = '1.0.0'` (Editions-Version)
  - `APP.engine = '3.0.0'` (unverändert)
- **Overlay-Anzeige:** „DT-ProfiDreieck Pro v1.0.0 (Engine 3.0.0)" (bzw. Test).
- Jede Edition führt ihren eigenen Changelog.

**2.0c – Overlay-Ordnung ✅**
- „Meta"-Funktionen (Info/Impressum, Lizenz, Sprache, Upsell) in Overlays →
  Hauptbildschirm bleibt schlank.
- **Ausnahme:** Der DE/EN-Schalter bleibt klein, aber immer sichtbar (neben
  `#infoBtn`).

### 2.1 Konzept Zwei-Dateien-System ✅
- Getrennte **Test**- und **Pro**-Datei, damit die Profi-Mathematik gar nicht
  erst im Code der Gratis-Version auftaucht.
- Beide entstehen aus deiner heutigen `Dreiecksberechnung_3-0-0.html` als Basis.

### 2.2 Pro-Datei vorbereiten: Wasserzeichen (A+B) + Versionsnummer ✅
- **Ziel:** In der gekauften Datei steht dezent, wem sie gehört, z. B.
  „Lizenziert für: Dieter Tepe – Schlüssel: ABCD-1234 – v3.0.0".

- **WICHTIGE KORREKTUR (vorherige Annahme war falsch):** Digistore24 kann eine
  **HTML**-Datei NICHT automatisch personalisieren. Der „Download-Vault" gibt die
  hochgeladene Datei **unverändert** an den Käufer weiter (wie ein versiegelter
  Umschlag). Die bekannte Stempel-/Namensfunktion greift bei PDFs, nicht bei
  HTML. Es gibt also **keinen** `{{…}}`-Platzhalter, den Digistore ersetzt.

- **Gewählte Lösung: Mischung A + B** (psychologisch + rückverfolgbar):

  **Teil A – selbst eingegebener Name (Einsteiger-Erklärung):**
  1. Öffnet der Kunde die Pro-Datei zum **ersten Mal**, erscheint ein kleines
     Fenster: „Bitte Namen und Lizenzschlüssel zur Aktivierung eingeben".
  2. Das Programm **merkt sich** die Eingabe lokal im Browser-Speicher
     (LocalStorage) → fragt nur **einmal pro Gerät**.
  3. Ab dann zeigt der **Info-Bereich** dauerhaft: „Lizenziert für: <Name> –
     Schlüssel: <Schlüssel> – v<Version>" (Version aus dem `APP`-Block).

  **Teil B – Lizenzschlüssel von Digistore24 (Einsteiger-Erklärung):**
  1. Digistore24 kann für Software pro Verkauf einen **eindeutigen
     Lizenzschlüssel** erzeugen und ihn dem Käufer automatisch anzeigen/mailen
     (du richtest das einmal beim Produkt ein, siehe 3.3 – danach läuft es
     automatisch, kein Aufwand pro Verkauf).
  2. Der Käufer trägt im Fenster aus Teil A **diesen Schlüssel** ein (nicht
     irgendeinen Fantasie-Text).
  3. Weil der Schlüssel **eindeutig** und bei Digistore mit dem Käufer
     verknüpft ist, lässt sich eine aufgetauchte Kopie **zurückverfolgen**.

- **Ehrlich bleibt:** Das ist **kein Schloss**. Offline kann die HTML den
  Schlüssel nicht „prüfen"; der Käufer könnte das Feld leer lassen oder einen
  Fantasienamen eintippen. Es ist eine **psychologische Hürde + Rückverfolg-
  barkeit**, kein echter Kopierschutz. Den Hauptschutz leisten weiterhin der
  faire Preis und die Verschleierung (2.5).

- 👉 **Cross-Check beim Bauen:** Dieses A+B-Eingabefenster + die Info-Anzeige
  gehören NUR in die **Pro-Version** (2.2), NICHT in die Testversion (2.4)!

### 2.3 Impressum/Rechtshinweis IN der HTML ✅
- **Gelöst:** Im **Info-Overlay** stehen die Kerndaten (Name, Anschrift, E-Mail)
  direkt – offline immer verfügbar – plus Link zum vollen Impressum &
  Datenschutz auf der Webseite. In **Pro** zusätzlich der Wasserzeichen-Block
  (Lizenziert für / Schlüssel) aus 2.2.
- **Fertige, korrigierte Textblöcke** (Test + Pro): Datei „Pflichttexte_Entwurf",
  Abschnitt 3. Korrekturen ggü. erstem Entwurf: kaputter Markdown-Link
  entfernt, `<br>` ergänzt, Version über `<span id="appVersion">` (eine Quelle:
  `APP`-Block), `rel="noopener noreferrer"`, neutrale Platzhalter „—".
- **Privatsphäre:** Telefonnummer bewusst NUR im Online-Impressum, nicht in der
  frei verteilten Datei.
- *Hinweis:* keine Rechtsberatung; Kerndaten eingebettet + Link auf Volltexte
  ist gängige, sinnvolle Praxis. Webseite muss vor Verteilung online sein.

### 2.4 Testversion bauen ✅
- Aus der Basis eine **Gratis-Testversion** ableiten. Entschieden:
  - **Sperr-Methode (Idee 1, „jedes Schloss ist ein Verkäufer"):** Die
    Spezial-Pills (**R, r, Fläche, Höhen**) werden **sichtbar, aber gesperrt**
    (ausgegraut + Schloss/✦, `.pill.disabled`). Die Gruppen „Seiten" und
    „Winkel" bleiben frei. Beim Antippen erscheint eine **konkrete** Mini-Werbung
    für genau diesen Nutzen (nicht nur „ist Teil der Vollversion"):
    - R: „Vollversion: Dreieck allein aus dem Umkreisradius berechnen – das kann
      kein anderes Tool."
    - r: „Vollversion: aus dem Inkreisradius das ganze Dreieck rekonstruieren."
    - Fläche: „Vollversion: Fläche vorgeben, Seiten & Winkel daraus berechnen."
    - Höhe: „Vollversion: aus einer Höhe heraus rechnen."
    Darunter Knopf „Vollversion freischalten →" (zur Webseite). So *sieht* der
    Tester genau, was er bekommt → Verlangen statt Frust.
  - **„Werbung" = Eigenwerbung für Pro:** dezenter Banner/Knopf „Vollversion
    freischalten →" zur Webseite. KEINE externen Werbenetzwerke (brauchen
    Internet, wirken billig, Datenschutz-Ärger).
  - **DXF bleibt FREI** (für Standardfälle) – bewusst als Kaufanreiz: Tester
    erlebt das Killer-Feature Dreieck→DXF→CNC. Konsequenz: dann auch SVG/PNG/
    Druck frei → **alle Exporte frei**.
  - **Pro-Burggraben = die Spezial-Eingabefälle** (R/r/Fläche/Höhen), die kein
    Gratis-Tool kann.
- 👉 **Cross-Check Wasserzeichen:** Die Testversion bekommt **KEIN** Namens-/
  Lizenz-Fenster und KEINE „Lizenziert für"-Zeile (aus 2.2). Sie ist gratis und
  soll **frei weitergegeben** werden.
- ❌ **Verworfen – Zeitsperre** (nach einer Berechnung 4 h warten): frustriert
  genau die Tester/Käufer, killt die Weiterempfehlung/Verbreitung und ist
  offline trivial auszuhebeln (LocalStorage löschen / Inkognito / neu laden).
  Frust vertreibt Käufer; Verlangen zieht sie an – deshalb bewusst NICHT.
- 💡 *Optional (sanfter Schubs):* nach jeder Berechnung ein **wegklickbarer**
  Hinweis „Spezialfälle gibt's in der Vollversion → freischalten". Stupst, ohne
  zu blockieren.
- *Pro = nur die Spezial-Eingabefälle; alle Exporte (inkl. SVG/DXF) bleiben frei.*


### 2.5 Code-Verschlüsselung (Obfuscation) ✅

> **Wichtig – Verschleierung ≠ Verschlüsselung:** Die „Verschlüsselung" hier ist
> eigentlich *Verschleierung (Obfuscation)*. Der Code wird unleserlich, bleibt
> aber voll lauffähig – nichts wird „mit einem Käufercode entsperrt".
> Eine echte Sperre (Code erst nach Schlüssel nutzbar) ist bei einem **offline**
> laufenden Single-File-Produkt nicht möglich: Alles zum Laufen Nötige steckt in
> der Datei auf dem Käufer-PC; ein „Schlüssel" müsste mitliegen und wäre
> herausnehmbar. Eine echte Sperre bräuchte einen Server im Internet – das würde
> das Versprechen „offline, eine Datei" zerstören (Entscheidung 0.2).
> **Was Verschleierung bringt:** Sie schützt nicht die Ausführung, sondern das
> *Verstehen/Nachbauen* deiner Mathematik. Drei Schutzschichten teilen sich die
> Arbeit: Verschleierung (Mathematik schwer lesbar) + Wasserzeichen (gegen
> Weitergabe) + fairer Preis (nimmt den Anreiz). Der Browser führt verschleierten
> Code identisch aus – es ist weiterhin gültiges JavaScript, nur hässlich.

- **Gewähltes Werkzeug: obfuscator.io** (Web, einsteigerfreundlich, gratis für
  Standard-Obfuscation). → https://obfuscator.io
- *Alternative für später (optional):* dieselbe Engine lokal als
  `javascript-obfuscator` (Code bleibt auf dem PC, aber braucht Node.js +
  Kommandozeile). → https://github.com/javascript-obfuscator/javascript-obfuscator
- **Empfohlene Einstellungen (mittlere Stärke – „läuft + schnell" vor „maximal"):**
  - ✅ *Anhaken:* **Compact code**; **String Array** (Base64-Kodierung, Rotate,
    Shuffle – nicht RC4, das bremst); **Simplify**; optional **Numbers to
    Expressions** (versteckt Formel-Konstanten, billig).
  - ❌ *NICHT anhaken:* **Control Flow Flattening** (stärkste, aber langsamste
    Option – die 15–80 % Bremse); **Rename Global Variables** (WICHTIG aus
    lassen – Knöpfe/Felder rufen Funktionen beim Namen auf; Umbenennen bricht
    alles); **Transform Object Keys** (kann DXF-Export/benannte Felder
    zerschießen); **Debug Protection** (kann Seite einfrieren); **Disable
    Console Output** (aus, solange getestet wird); **Dead Code Injection** und
    **Split Strings** (Beiwerk, mehr Risiko als Nutzen).
  - ⚙️ *Setzen:* **Target: Browser**.
  - 💡 *Später optional:* **Self Defending** (erschwert das Zurück-Schönmachen)
    – erst nach Test dazunehmen.
- **Danach IMMER jeden Solver-Fall testen.** Hakt etwas, ist meist eine scharfe
  Option schuld.
- **Premium (kostenpflichtig, Overkill): JScrambler** – Enterprise-Schutz, teuer.
  Für 24-€-Software nicht nötig.
- **Vorgehen (Single-File-HTML):** nur den eigenen `<script>`-Inhalt
  verschleiern; lesbares Original IMMER lokal behalten.
- **Für Einsteiger – so läuft es konkret ab (mit obfuscator.io, ohne Installation):**
  1. HTML in einem Text-Editor öffnen (gratis: Notepad++ oder VS Code).
  2. Das JavaScript steht in *einem* Block zwischen `<script>` (≈ Zeile 723) und
     `</script>` (≈ Zeile 2645). Die jsPDF-Zeile (242) und das CSS NICHT anfassen.
  3. Alles zwischen den `<script>`-Zeilen markieren und kopieren.
  4. Auf obfuscator.io links einfügen → „Obfuscate".
  5. Verschlüsseltes Ergebnis rechts kopieren.
  6. Im Editor den alten Code zwischen den `<script>`-Zeilen ersetzen, als neue
     Pro-Datei speichern.
  - *Hinweis Werkzeug-Wahl:* Web-Tool obfuscator.io = einsteigerfreundlich
    (nichts installieren). Lokales `javascript-obfuscator` = sicherer (Code
    bleibt auf dem PC), aber braucht Node.js + Kommandozeile → später optional.
- **Wie der Käufer es nutzt:** Eine verschlüsselte HTML ist weiterhin eine
  normale HTML-Datei. Doppelklick → öffnet im Browser → läuft identisch. Keine
  Installation, weiterhin offline, eine Datei. Für den Käufer ändert sich nichts.
- **Stolpersteine (wichtiger als die Tool-Wahl):**
  - *Nicht übertreiben:* aggressive Optionen (control-flow flattening,
    self-defending) machen Code 15–80 % langsamer/größer → moderate
    Einstellungen wegen der rechenintensiven Mathematik.
  - *Danach alles testen:* jeden Solver-Fall prüfen (ein falsches Zeichen →
    nichts läuft).
  - *Wasserzeichen-Funktion (2.2) muss nach dem Verschleiern noch laufen:* Das
    Namens-/Lizenz-Fenster und die Info-Anzeige sind normaler Code – mit den
    obigen Einstellungen (kein „Rename Globals") bleiben sie funktionsfähig;
    nach dem Verschleiern einmal testen. (Einen von Digistore ersetzten
    Platzhalter gibt es NICHT mehr – der Käufer gibt Name/Schlüssel selbst ein.)

### 2.6 Hosting Teil 1 – Speicherplatz (GitHub Pages) ✅
- Ordner `dt-profidreieck-web` auf GitHub. Dort hinein **nur** Landingpage +
  verschlüsselte **Test**version. Niemals die Pro-Datei.
- **Stand 07.06.2026:** live – obfuskierte `DT-ProfiDreieck_Test_1-1-0.html`,
  `index.html`, `impressum.html`, `datenschutz.html` geladen und verlinkt;
  Inhalts-Feinschliff der Landingpage läuft (siehe Landingpageplan).
- 💲 0 € (GitHub Pages kostenlos).

### 2.7 Hosting Teil 2 – Domain (INWX) → GitHub ✅ ERLEDIGT (07.06.2026)
> **Ergebnis:** `dt-profidreieck.de` ist live – Landingpage, Testversion,
> Impressum und Datenschutz laufen über die eigene Domain (HTTPS aktiv).
> Unten die komplette Anleitung, so wie sie umgesetzt wurde – für Laien.

> **Idee in einem Satz:** Bei **INWX** sagst du „*wo* die Seite liegt"
> (DNS-Einträge), bei **GitHub** sagst du „*unter welchem Namen*". Reihenfolge:
> erst der GitHub-Ordner (2.6) muss existieren, dann diese Schritte.

**Diese 5 Einträge gehören bei INWX rein** (von GitHub vorgegeben):

| Typ | Name | Wert |
|---|---|---|
| A | *(leer)* | 185.199.108.153 |
| A | *(leer)* | 185.199.109.153 |
| A | *(leer)* | 185.199.110.153 |
| A | *(leer)* | 185.199.111.153 |
| CNAME | www | dietertepe.github.io |

**TEIL A – bei INWX (DNS-Einträge):**
1. Auf **inwx.de** einloggen.
2. Linkes Menü **„Nameserver"** → bei `dt-profidreieck.de` auf das
   **Augen-Symbol** klicken (zeigt die DNS-Einträge).
3. **„DNS-Eintrag hinzufügen"** → je A-Record: Typ **A**, Feld **„Name" leer**,
   IP ins Feld **„Wert"**, speichern. Für alle **vier** IPs wiederholen.
4. **www:** nochmal „DNS-Eintrag hinzufügen" → Typ **CNAME**, Name **`www`**,
   Wert **`dietertepe.github.io`**. (CNAME nur für www, nie für die nackte Domain.)
5. ⚠️ **Stolperstein (wichtig!):** INWX legt anfangs eigene **Parkseiten-Einträge**
   an, die auf eine INWX-IP (z. B. `185.181.104.242`) zeigen – als A bei „Name
   leer", als `*` (Wildcard) und als `www`. Diese **drei löschen** (✗-Symbol),
   sonst lädt die Domain mal die echte Seite, mal die Parkseite.
6. **Finger weg** von den **NS-** und **SOA-**Einträgen – die gehören zu INWX.

**TEIL B – bei GitHub (Name + HTTPS):**
7. Repo **`dt-profidreieck-web`** → **„Settings"/„Einstellungen"** →
   **„Pages"/„Seiten"**.
8. Abschnitt **„Custom domain"/„Benutzerdefinierte Domäne"**: `dt-profidreieck.de`
   eintragen → **„Save"/„Speichern"**. (GitHub legt automatisch eine `CNAME`-Datei
   im Repo an.)
9. GitHub prüft die DNS-Einträge (Minuten bis Stunden). Danach
   **„HTTPS erzwingen"/„Enforce HTTPS"** anhaken → kostenloses SSL automatisch.
   (Haken anfangs ausgegraut = normal, Zertifikat braucht ggf. bis 24 h.)

**TEIL C – prüfen:** `dt-profidreieck.de` aufrufen → Landingpage erscheint,
Test-Knopf öffnet `dt-profidreieck.de/DT-ProfiDreieck_Test_1-1-0.html`.

- An den **Dateien nichts ändern** – die relativen Links passen sich automatisch
  an; die Links *in* der App zeigen bereits auf `www.dt-profidreieck.de`.
- DNS-Änderungen brauchen bis zu **24 h** (meist viel schneller).
- **`.com`** vorerst offen – später optional als Weiterleitung auf `.de`.
- **Optional bei INWX:** E-Mail-Weiterleitung `info@dt-profidreieck.de`
  → `Dieter.Tepe@live.de`.
- 💲 0 € (im Domainpreis enthalten; SSL bei GitHub gratis).

---

## Phase 3 – Vertrieb, Finanzamt & Auslieferung (Digistore24)

> **📄 Ausführliche Laien-Anleitung:** `Digistore24_Anleitung_DT-ProfiDreieck.md`
> (klickgenau, mit allen Eingabewerten). Phase 3 hier = Kurzfassung/Roadmap.
>
> **8-Punkte-Roadmap:** 1) Konto-Basis (Vendor, Steuer = Kleinunternehmer, 2FA)
> → 2) Produkt als „Software" anlegen → 3) Datei in Download-Tresor →
> 4) Reiter „Ausliefern": Datei verknüpfen + Lizenzschlüssel „von Digistore24
> generiert" → 5) Dankeseite LEER lassen → 6) Bestell-Link aus „Links" in
> die index.html → 7) Testkauf („Testzahlung") → 8) „Genehmigung beantragen".
>
> **Exakte Produktdaten (1:1 eintragen):**
> - Produktname intern: `DT-ProfiDreieck_Pro_1-1-0`; für Käufer: `DT-ProfiDreieck Pro`
> - Typ: **Software**; Preis: **69 € brutto, Einmalzahlung** (37-€-Standardplan löschen!)
> - Verkaufsseite: `https://www.dt-profidreieck.de/`; **Dankeseite: LEER**
> - Datei: `DT-ProfiDreieck_Pro_1-1-0.html` (obfuskiert)
> - Beschreibung: „Dreiecke berechnen und direkt als DXF an die CNC oder zum
>   CAD. Alle Spezialfälle & Exporte berechenbar."
> - Kosten pro Verkauf ≈ 6,70 € (7,9 % + 1 € + 0,25 € Tresor) → ~62,30 € netto.

### 3.1 Konto erstellen & einrichten (ausführlich für Laien) ✅
> Ziel: ein kostenloses **Verkäufer-Konto** bei Digistore24, vollständig
> eingerichtet, sodass Auszahlungen funktionieren. Fixkosten 0 €; Digistore
> behält nur eine Provision pro Verkauf ein.

**A) Das vorher bereitlegen:**
- Gewerbe-Daten: Name + Adresse – **identisch** zum Impressum (Dieter Tepe,
  Mühlenstraße 2, 48477 Dreierwalde).
- **Telefonnummer** (wird per Code bestätigt).
- **Steuernummer** (vom Finanzamt / aus der Gewerbeanmeldung).
- **Bankverbindung: IBAN + BIC** – du musst **Kontoinhaber** sein.
  (Alternativ geht PayPal.)
- Fürs Handy eine **Authenticator-App** (für die Zwei-Faktor-Anmeldung) –
  Empfehlung: **Microsoft Authenticator** (kostenlos, mit Cloud-Backup).

**B) Schritt für Schritt:**
1. Auf **digistore24.com** „Konto erstellen / Registrieren". Wichtig: als
   **Verkäufer/Vendor** registrieren (nicht nur Affiliate) – nur Vendoren dürfen
   eigene Produkte verkaufen. Kostenlos.
2. **E-Mail bestätigen** und einloggen.
3. Menü **„Konto → Details"** öffnen. Zuerst die **Telefonnummer bestätigen**
   (Code eingeben).
4. **Umsatzsteuerregelung wählen: „Kleinunternehmer"** (passt zu unserem §19).
   Dann die **Steuernummer** eintragen und speichern. Eine **USt-IdNr ist nicht
   nötig** und du hast bewusst keine.
5. **Auszahlungskonto einrichten:** IBAN + BIC eingeben (du als Kontoinhaber),
   und festlegen, **wie oft** ausgezahlt wird (z. B. monatlich). Alternativ
   PayPal.
6. **Zwei-Faktor-Anmeldung (2FA) aktivieren** (Pflicht für Auszahlungen). Du
   brauchst eine kostenlose **Authenticator-App** (zeigt alle 30 Sek. einen
   6-stelligen Code). Empfehlung für Einsteiger: **Microsoft Authenticator**
   (kostenlos, kein MS-Konto nötig, Cloud-Backup); Alternativen: Google
   Authenticator, 2FAS, Aegis.
   - **Ablauf:** App aus dem Play Store installieren → bei Digistore die
     2FA-Aktivierung starten (QR-Code erscheint) → in der App
     „Konto hinzufügen → QR-Code scannen" → 6-stelligen Code einmal bei
     Digistore eingeben. Fertig.
   - **Tipp:** in der App das **Cloud-Backup** aktivieren (sonst bei Handywechsel
     ausgesperrt); etwaige **Wiederherstellungs-Codes** notieren und sicher
     ablegen.

**C) Worauf besonders achten:**
- Digistore zahlt **nur an Unternehmen**, nicht an Privatpersonen → dein
  Kleingewerbe ist die Voraussetzung (hast du). ✓
- **Daten konsistent** zum Impressum/Gewerbe halten (gleicher Name/Adresse) –
  sonst Rückfragen.
- Bei der Steuer **„Kleinunternehmer"** wählen, **nicht** „umsatzsteuerpflichtig"
  – sonst widerspricht es §19.
- Du musst **Kontoinhaber** des angegebenen Bankkontos sein.
- **Gebühren vor dem Start prüfen:** Provision pro Verkauf (Richtwert ~7,9 % + 1 €,
  kann sich ändern; steht in deinem Konto). Bei 69 € bleibt dir der Großteil.
- **Auszahlungsschwelle:** Digistore zahlt erst ab einem Mindestbetrag aus
  (im Kundenbereich einsehbar) – am Anfang kann die erste Auszahlung also etwas
  dauern.

### 3.2 Reseller-Prinzip ✅
- Digistore24 ist Wiederverkäufer, berechnet & führt die Mehrwertsteuer (auch
  EU-weit) automatisch ab. → nimmt dir die Umsatzsteuer-Hölle ab.
- Als Kleinunternehmer (§ 19, siehe 1.3): du verkaufst rechtlich nur an
  Digistore und bekommst die Provision **netto** ausgezahlt.

### 3.3 Produkt anlegen, Tresor füllen & Lizenzschlüssel-Automatik 💬
**Produkt anlegen:**
1. „Meine Produkte → Produktliste → **Produkt hinzufügen**" → Reiter
   „Eigenschaften" → Produkttyp **Software**; Namen + Beschreibung + Verkaufsseite
   eintragen (Werte s. Box oben). **Dankeseite LEER lassen.**
2. Reiter „Zahlungspläne": **69 € brutto, Einmalzahlung, Aktiv = Ja** →
   „Zahlungsplan hinzufügen". **Den automatisch angelegten 37-€-Standardplan
   löschen** (X-Icon).
3. **Download-Tresor** („Meine Produkte → Download-Tresor → Datei-Paket
   hinzufügen"): die **obfuskierte** `DT-ProfiDreieck_Pro_1-1-0.html` hochladen,
   in „Dateien im Paket" ziehen, speichern. **Nie öffentlich auf GitHub!**
4. Reiter „Ausliefern": **Datei-Paket** auswählen + **Lizenzschlüssel-Typ „von
   Digistore24 generiert"**. Optional Nutzungshinweise + Support-Mail im Reiter
   „Bestellformular".
- **Lizenzschlüssel-Automatik (Teil B des Wasserzeichens):** Digistore erzeugt
  pro Kauf einen eindeutigen Schlüssel, schreibt ihn automatisch in die
  Kaufbestätigungs-E-Mail **und** auf die Bestätigungsseite – kein manueller
  Aufwand, kein Platzhalter nötig (intern Parameter `license_key`, nur für ein
  eigenes Prüfsystem relevant). Käufer tippt Name + Schlüssel ins Pro-Fenster.

### 3.4 Preis eintragen ✅
- **69 €**, keine Staffelung.

### 3.5 Verkaufs-Link einbauen ✅
- Bestell-Link im Reiter „Links" holen (Format
  `https://www.checkout-ds24.com/product/PRODUKT-ID`).
- In `index.html` an den **„Jetzt kaufen"-Knopf** setzen (zeigt aktuell auf
  `href="#"`). Tipp: an allen drei Kauf-Knöpfen (Kopfleiste, Hero, Kauf-Block)
  hinterlegen, dann landet jeder Klick direkt im Checkout.

### 3.6 Automatische Auslieferung + Testkauf ✅
- **Testkauf zuerst:** eingeloggt bleiben → beim Produkt Einkaufswagen-Icon →
  Bezahlart **„Testzahlung"**. Prüfen: E-Mail kommt an, Lizenzschlüssel enthalten,
  Download lädt die richtige Datei, Aktivierung im Tool klappt.
- **Dann „Genehmigung beantragen"** (Bearbeitung i. d. R. < 48 h werktags) → live.
- Danach: Kunde zahlt → automatisch Rechnung + sicherer Download-Link + Schlüssel.

### 3.7 Laufende Buchhaltung ✅
- Pro Auszahlung ein PDF-Beleg; sammeln.

### 3.8 Jährliche Steuererklärung ✅
- Summe der Auszahlungen in der „Anlage EÜR" eintragen.

---

## Phase 4 – Marketing & Reichweite

### 4.1 Rolle der Gratis-Testversion ✅
- Die Testversion ist der **Köder** und zugleich **Selbstläufer**: ohne
  Wasserzeichen frei weitergebbar, verbreitet sich von allein und zieht Leute
  zur Pro-Version. (Gebaut wird sie in 2.4.)

### 4.2 Landingpage-Inhalt ✅
1. **Versprechen:** „Komplexe Dreiecke berechnen und direkt als DXF an die CNC".
2. **Praxis-Beweis:** kurzes YouTube-Werkstattvideo (= das DXF-Video aus 4.4.2).
3. **Köder:** Button „Jetzt Gratis-Version testen" → stößt auf gesperrte Funktion.
4. **Verkauf:** Vorteile der Vollversion + Digistore24-Button.

### 4.3 Landingpage technisch erstellen 💬 (in Arbeit – eigener Plan)
- Wird in einem eigenen Dokument geführt: **`Landingpageplan_DT-ProfiDreieck.md`**
  (Werkstatt-Blueprint-Stil, Single-File, keine externen Ressourcen).
- **Stand 07.06.2026 (geprüft):** `index.html` + `impressum.html` +
  `datenschutz.html` gebaut und **live auf GitHub Pages**
  (`dietertepe.github.io/dt-profidreieck-web/`). Geprüft: keine externen
  Ladequellen (Datenschutz-Regel erfüllt); Rechtstexte = Pflichttexte §1/§2
  (inkl. §19, ohne USt-IdNr/OS-Plattform); `lang=de`, Viewport, Suchtitel;
  Test-Link relativ korrekt.
- **Noch offen:** Inhalts-Sektionen füllen (Hero/Beweis/Vorteile/Test-vs-Pro/
  Kauf); Digistore-Kauf-Link (Phase 3); YouTube-Link (4.4.2); sauberer
  Eingabe-Screenshot ohne Lizenzzeile.
- **Designregel:** weiterhin keine externen Schriften/Skripte (sonst stimmt die
  Datenschutz-Aussage nicht).

### 4.4 Reichweite: Wie finden Käufer die Seite? ✅
- **Pull** = gefunden werden, während Leute suchen (langsam, dauerhaft).
- **Push** = aktiv dorthin gehen, wo die Profis sind (schnelle erste Käufer).
- Anfänger brauchen beides.
- **Kanäle:** YouTube (4.4.2), Facebook-Gruppen & Foren (4.4.1), Gratis-Test als
  Selbstläufer (4.1).
- ❌ **Abgeraten:** Kleinanzeigen (falsche Käufer, digitale Downloads meist gegen
  AGB) und bezahlte Anzeigen zum Start (verbrennt Budget).

#### 4.4.1 Gruppen & Foren – ohne Spam ✅
**Selbsttest vor jedem Beitrag:** „Wäre mein Beitrag auch *ohne* den Link
nützlich?" Ja → Hilfe. Nein → Werbung.

**Grundregeln:**
1. Erst geben, dann sichtbar werden (2–3 Wochen nur helfen, Ruf aufbauen).
2. Regeln lesen, Admin vorher privat fragen.
3. Immer mit der **Gratis-Version** führen, nie mit dem Preis.
4. Ehrlich: „Ich hab das gebaut."
5. Tempo: 2–3 Gruppen/Foren, nicht 20 auf einmal.

**Erste Aktion – Stöbern als Aufklärung:** ein paar Tage mitlesen und sammeln:
(1) Regeln, (2) wiederkehrende Fragen → werden Video-Titel + Antwort-Chancen,
(3) Ton. So baust du Ruf auf und füllst die Themenliste.

**Forum vs. Facebook:** Foren haben oft „Eigene Projekte"-Bereiche (Thread lange
bei Google auffindbar = Pull-Bonus); Facebook ist schneller, aber flüchtiger.

**Vorlage A – Admin privat anschreiben:**
> Hallo [Name], ich bin Dieter und tüftle nebenbei. Ich habe ein kleines
> Werkzeug gebaut, das Dreiecke aus drei Größen berechnet und als DXF für
> CAD/CNC exportiert – es gibt eine kostenlose Version. Darf ich es in der
> Gruppe einmal vorstellen, oder gibt es dafür einen passenden Bereich/Tag?
> Ich möchte nicht spammen, deshalb frage ich vorher. Danke dir!

**Vorlage B – reaktive Hilfe-Antwort** (zuerst die Frage wirklich beantworten):
> [Konkrete Lösung in eigenen Worten …] Falls du sowas öfter brauchst: Ich hab
> dafür ein kleines Tool gebaut – die Gratis-Version rechnet genau das und gibt
> das Dreieck auch als DXF für die CNC aus: [Link]. Selbst gemacht; sag gern
> Bescheid, wenn dir etwas fehlt.

**Vorlage C – Vorstellungs-Post (einmalig, mit Erlaubnis):**
> Moin zusammen – ich tüftle nebenbei und hab ein Werkzeug gebaut, das mir in
> der Werkstatt das Berechnen von Winkeln/Dreiecken abnimmt: drei Größen
> eingeben (Seiten, Winkel, auch Umkreis/Inkreis/Fläche/Höhen), es rechnet
> alles aus, zeichnet das Dreieck und exportiert es als DXF direkt für die CNC.
> Läuft offline als eine einzige Datei, ohne Installation. Gratis-Version:
> [Link]. Ehrliches Feedback willkommen – was fehlt euch?

🔲 *Noch zu klären:* nach dem Stöbern die konkreten 2–3 Gruppen + 1–2 Foren
namentlich festlegen.

#### 4.4.2 YouTube-Reihe ✅
**Prinzip:** echte Werkstatt-Probleme lösen, Tool macht es nebenbei. Mehrere
kurze Videos (2–3 Min.), jedes auf *einen* Suchbegriff.

**Aufbau:** Haken (Problem) → Problem zeigen → Lösung im Tool → Aha-Moment
(DXF an CNC) → sanfter Abschluss („Gratis-Version in der Beschreibung").

**SEO-Einsicht:** Generisches („Dreieck berechnen") = viel Konkurrenz. **Spezial-
fälle** (Umkreis/Inkreis/Fläche/Höhe) = fast keine Konkurrenz → leichteste
Treffer für einen neuen Kanal.

**Video-Vorrat (nach und nach abarbeiten):**
- *A – Trumpf/DXF:* „Dreieck berechnen und als DXF an die CNC senden";
  „Gehrung/Winkel am Werkstück berechnen + DXF"
- *B – Klassiker:* SSS; SWS; WSW; SSW (2 Lösungen)
- *C – Nur dieses Tool:* aus Umkreisradius R; aus Inkreisradius r; aus der
  Fläche; aus einer Höhe; aus Umkreis + Inkreis
- *D – Lehrreich (Brücke Welle 2):* „mit komplettem Rechenweg, Schritt für Schritt"

✅ **Start:** DXF-Video zuerst, dann 2–3 Spezialfälle in derselben Aufnahme.
💡 **Später:** komplettes Skript fürs erste Video (Wort für Wort + Klick-Reihenfolge).
**Tipps:** mehrere Videos je Aufnahme-Sitzung; Serien-Stil im Titel
(„Dreieck-Rechner: …"); Beschreibung mit Stichworten + Link, Link auch als
angepinnter Kommentar.

### 4.5 Kosten/Gebühren prüfen 🔲
- Vor dem Start überall aktuelle Zahlen prüfen: Domain, Gewerbe, Digistore24.

---

## Anhang: Stammdaten (für Impressum & Datenschutz)
*(Vom Betreiber bereitgestellt – wird im Impressum veröffentlicht.)*
- **Name:** Dieter Tepe
- **Anschrift:** Mühlenstraße 2, 48477 Dreierwalde
- **E-Mail:** Dieter.Tepe@live.de *(ggf. später info@dt-profidreieck.de)*
- **Telefon:** +49 160 99303256
- **Steuerstatus:** Kleinunternehmer (§ 19 UStG) → KEINE USt-IdNr; im Impressum
  stattdessen der §19-Hinweis.

**Genutzte Webdienste:** GitHub Pages (Hosting); YouTube (nur verlinkt);
Digistore24 (Kauf-Weiterleitung); E-Mail-Kontakt; keine Analyse-Tools.

---

## Anhang: Funktionsübersicht (für die Werbung)
- **Was die App kann:** Dreieck vollständig aus drei Größen berechnen. Online &
  offline, eine HTML-Datei, keine Installation, responsiv (Handy/Tablet/Desktop).
- **Eingabefälle:** klassisch (SSS, SWS, WSW, SWW, SSW) + erweitert (Umkreis,
  Inkreis, Fläche, Höhen) in vielen Kombinationen; Engine über hunderttausende
  Zufallsdreiecke verifiziert.
- **Ergebnisse:** alle Seiten/Winkel, Umfang, Fläche, Höhen, Radien, Schwerpunkt,
  Umkreismittelpunkt, Orthozentrum; Typbestimmung; Umschalter bei 2 Lösungen.
- **Rechenweg:** Schritt für Schritt in Lehrbuch-Darstellung, aufklappbar + als
  Druckseite; bei 2 Lösungen je eigener Weg.
- **Zeichnung:** CAD-artig, 11 ein-/ausblendbare Elemente (Umkreis, Inkreis,
  Feuerbachkreis, Euler-Gerade …), interaktive Punkte, Legende als Schalter.
- **Export:** PNG, SVG, **DXF (CAD/CNC)**, Drucken/PDF (inkl. Rechenweg),
  wählbare Maßeinheit.

---

## Anhang: Technische Anker in Dreiecksberechnung_3-0-0.html
*(Damit ein neuer Chat Pro/Test fehlerfrei aus dieser Datei bauen kann.
Zeilennummern ca. – können sich beim Bearbeiten leicht verschieben.)*

- **Version (einzige Quelle):**
  `const APP = { name:'Dreiecksberechnung', version:'3.0.0', date:'2026-06-04' };`
  (~Z. 726). Alle Versionsanzeigen aus `APP.version` speisen.
- **JavaScript-Block:** *ein* `<script> … </script>` (~Z. 723–2645). NUR dieser
  wird obfuskiert (2.5). Externe jsPDF-Zeile (~Z. 242) und `<style>`
  (~Z. 244–569) nicht anfassen.
- **Info-Overlay:** Button `#infoBtn` (~Z. 580) öffnet `#overlay` (~Z. 651);
  Titel `#modalTitle`, Version `#verTag` (~Z. 654); Fuß **`#modalFoot`**
  (~Z. 718) → Einbauort für Impressum-/Wasserzeichen-Block (Texte:
  Pflichttexte_Entwurf §3).
- **Eingabe-Pills:** 4 Gruppen (Seiten·Winkel·Kreise·…), Slots in `#slots`
  (~Z. 587); Stile `.pill` / `.pill.active` / `.pill.disabled` (~Z. 316–323;
  „disabled" für das Sperren bereits vorhanden).
- **Aktionen:** `#calcBtn` (Berechnen, ~Z. 598), `#resetBtn` (~Z. 599).
- **Ergebnis/Anzeige:** `#resultCard`, `#grid`, Rechenweg `#traceBody`;
  Zeichnung `#graphCard`, `#canvas`, Element-Schalter `#visToggles`.
- **Export-Knöpfe (je eigene ID):** `#svgBtn`, `#dxfBtn`, `#pngBtn`,
  `#printBtn`, `#pdfBtn` (~Z. 637–641).
- **Fall-Erkennung:** nach dem Lösen steht der Fall in `result.caseType`.
  Standard = `'SSS'`, `'SWS'`, `'SSW'`, `'WSW / SWW'`; Spezial = beginnt mit
  `'R '`/`'r '` bzw. `'R + r …'` (Umkreis/Inkreis), plus Fälle mit Fläche/Höhen.
  → zuverlässiges Signal für die Pro-Sperre auf Aufgaben-Ebene.

---

## Anhang: Bauanleitung für einen neuen Chat (Test- & Pro-Version aus 3-0-0)

> Ziel: Aus `Dreiecksberechnung_3-0-0.html` zwei Dateien bauen – **Pro** und
> **Test**. Overlay-Texte aus `Pflichttexte_Entwurf.md` Abschnitt 3.
> **Grundregel: NUR die UI-Schicht anfassen – Solver/Geometry/Renderer/Narrator
> NICHT verändern.** Die **Engine bleibt 3.0.0**.

> **🔒 VERBINDLICHE BAUVORGABEN (Build-Kontext):**
> 1. **Quellen:** nur `Dreiecksberechnung_3-0-0.html` (Basis), dieser Masterplan,
>    `Pflichttexte_Entwurf.md`.
> 2. **APP-Block:** `name='DT-ProfiDreieck'`, `edition='Pro'|'Test'`,
>    `version='1.0.0'`, `engine='3.0.0'`. Overlay zeigt:
>    „DT-ProfiDreieck Pro v1.0.0 (Engine 3.0.0)".
> 3. **I18N:** nur UI-Labels/Buttons/Grid übersetzen; **Narrator (Rechenweg),
>    Solver-Fehler und Rechtstexte BLEIBEN DEUTSCH**. Einfaches Dictionary, kein
>    Framework. DE/EN-Toggle sichtbar neben `#infoBtn`, speichert in
>    `localStorage`. EN-Modus zeigt „Legal information in German only."
> 4. **Lizenz-Modal (Pro):** eigenes HTML/CSS-Modal (KEIN `window.prompt()`),
>    passend zum `.overlay`-Design; speichert `localStorage['dt_name']` +
>    `localStorage['dt_key']`.
> 5. **Obfuscation strikt:** nur `<script>`; **verboten:** renameGlobals,
>    controlFlowFlattening, transformObjectKeys; **erlaubt:** compact,
>    stringArray (base64), simplify, numbersToExpressions; Target: Browser.
>    **Pflichttest nach Obfuscation:** DXF-Export + Lizenz-Modal + SSW-Fall.
> 6. Im Übrigen exakt dieser Bauanleitung folgen (prompt() ist durch das eigene
>    Modal ersetzt).

> **Schnelltest (nur Mechanik prüfen):** Aus `3-0-0` bauen, **I18N/Umbenennung
> und Obfuscation weglassen** (lesbare Datei testen). Beim Pro-Modal genügt ein
> beliebiger Schlüssel – offline wird er ohnehin nicht geprüft. Die Testversion
> hat gar kein Schlüsselfeld.

### Gemeinsam (für Pro UND Test)
1. Eine Kopie von `Dreiecksberechnung_3-0-0.html` anlegen.
2. **APP-Block** auf die Editions-Struktur umstellen (Vorgabe 2) und die
   Versions-Anzeige im Overlay (`#verTag` bzw. `initModal()`) auf
   „… v{version} (Engine {engine})" setzen.
3. **Overlay/Impressum:** In `initModal()` die Zeile, die `#modalFoot` per
   `innerHTML` setzt (~Z. 2293), durch den passenden Block ersetzen
   (Test → Pflichttexte §3a, Pro → §3b).
4. **I18N (Vorgabe 3):** Dictionary `I18N={de:{…},en:{…}}` für UI-Labels,
   Buttons, Grid-Beschriftungen; DE/EN-Toggle neben `#infoBtn`, Wahl in
   `localStorage`; Standard DE; EN zeigt „Legal information in German only".
   Narrator/Solver-Fehler/Rechtstexte NICHT übersetzen.
5. Zum Schluss **Obfuscation** des einen `<script>`-Blocks (~Z. 723–2645) nach
   Vorgabe 5; danach Pflichttest (DXF + Lizenz-Modal + SSW).

### Nur PRO-Version (Wasserzeichen A+B, volle Funktion)
6. Keine Funktionssperre – Pro kann alles.
7. **Lizenz/Wasserzeichen (eigenes Modal, KEIN prompt()):**
   - Beim Laden prüfen, ob `localStorage['dt_name']` existiert.
   - Falls nein: ein **eigenes HTML/CSS-Modal** im `.overlay`-Stil zeigen
     („Name + Lizenzschlüssel zur Aktivierung"), Werte in
     `localStorage['dt_name']` / `localStorage['dt_key']` speichern.
   - Dann `#lizenzName` und `#lizenzKey` füllen (die `<span>`s stammen aus dem
     Pro-Overlay-Block §3b und existieren nach Schritt 3).

### Nur TEST-Version (Spezialfälle gesperrt, Eigenwerbung, KEIN Wasserzeichen)
8. Oben in der UI-Schicht definieren: `const PRO_KEYS=['R','r','A','ha','hb','hc'];`
   (= Gruppen „Kreise" + „Fläche & Höhen"; „Seiten" und „Winkel" bleiben frei.)
9. In `refreshPillStates()` zusätzlich: Pills, deren `dataset.key` in `PRO_KEYS`
   liegt, dauerhaft auf `.disabled` setzen und ein Schloss/✦ anzeigen.
10. In `selectQuant(slot,key,el)` ganz oben einfügen:
    `if(PRO_KEYS.includes(key)){ showUpsell(key); return; }`
11. Funktion `showUpsell(key)` ergänzen: zeigt die **konkrete** Botschaft je
    Größe (Tabelle unten) + Knopf „Vollversion freischalten →"
    (Link: `https://www.dt-profidreieck.de`).
12. **Eigenwerbungs-Banner** „Vollversion freischalten →" einbauen (z. B. über
    der Button-Reihe `#calcBtn`). KEINE externen Werbenetze.
13. **KEIN** Lizenz-/Namensfenster, KEINE `#lizenzName`/`#lizenzKey`-Zeile.
14. *Optional:* nach `calculate()` ein wegklickbarer Hinweis „Spezialfälle gibt's
    in der Vollversion → freischalten".

### Upsell-Texte (Schritt 9)
- `R`  → „Vollversion: Dreieck allein aus dem Umkreisradius berechnen – das kann kein anderes Tool."
- `r`  → „Vollversion: aus dem Inkreisradius das ganze Dreieck rekonstruieren."
- `A`  → „Vollversion: Fläche vorgeben, Seiten & Winkel daraus berechnen."
- `ha`/`hb`/`hc` → „Vollversion: aus einer Höhe heraus rechnen."

### Selbsttest nach dem Bauen
- **Pflichttest nach Obfuscation (beide, Vorgabe 5):** DXF-Export funktioniert,
  Lizenz-Modal (Pro) erscheint/speichert, der **SSW-Fall** rechnet korrekt
  (0/1/2 Lösungen).
- **Pro:** alle Fälle inkl. R/r/Fläche/Höhe rechnen; Overlay zeigt Name+Schlüssel;
  alle Exporte (DXF/SVG/PNG/Druck) funktionieren; Sprache DE/EN umschaltbar.
- **Test:** Spezial-Pills gesperrt + Werbebotschaft; Standardfälle (SSS/SWS/WSW/
  SWW/SSW) rechnen + alle Exporte frei; kein Lizenzfenster.

---

## 💬 Noch zu besprechen (Diskussions-Agenda, getrennt von der Checkliste)
1. Landingpage: Aufbau planen, dann bauen (4.3)
2. Konkrete Gruppen/Foren nach dem Stöbern (4.4.1)

---

## 📝 Changelog
```
v0.18.1 (2026-06-09)
  - 2FA für Laien ausgebaut (3.1 Schritt 6 + Vorbereiten-Liste): App-Empfehlung
    Microsoft Authenticator, QR-Scan-Ablauf in 4 Schritten, Cloud-Backup- und
    Wiederherstellungscode-Tipp. Gleiche Erweiterung in der Begleitdatei
    Digistore24_Anleitung_DT-ProfiDreieck.md.

v0.18.0 (2026-06-09)
  - Phase 3 mit recherchierter Digistore24-Realität synchronisiert: 8-Punkte-
    Roadmap + exakte Produktdaten-Box am Phase-3-Kopf; 3.3 korrigiert (Typ
    „Software", Dankeseite LEER, 37-€-Standardplan löschen, Lizenzschlüssel „von
    Digistore24 generiert" – automatisch in E-Mail); 3.5 Bestell-Link-Format +
    index.html-Stellen; 3.6 Testkauf („Testzahlung") + Genehmigung.
  - Neue Begleitdatei `Digistore24_Anleitung_DT-ProfiDreieck.md` verlinkt
    (klickgenaue Laien-Anleitung mit allen Eingabewerten).

v0.17.1 (2026-06-07)
  - Checkliste aktualisiert: 0.1/0.2/0.3, 1.3, 3.2, 4.1 abgehakt (erledigt/
    verstanden). 1.2 (Gewerbe) als „bitte bestätigen" markiert – Voraussetzung
    für Digistore. Neuer Kasten „🔧 Noch einzubinden / offene Aktionen".

v0.17.0 (2026-06-07)
  - Phase 3 für Laien stark ausgebaut: 3.1 = vollständige Konto-Anleitung
    (Daten bereitlegen, Vendor-Registrierung, Telefon bestätigen, Steuer =
    Kleinunternehmer + Steuernummer, Auszahlungskonto IBAN/BIC, 2FA) + Kasten
    „Worauf achten" (nur Firmen-Auszahlung, Kontoinhaber, Gebühren/Schwelle).
    3.3 um konkrete Produkt-Anlege-Schritte ergänzt.

v0.16.9 (2026-06-07)
  - index.html-Preis auf 69 € umgestellt (drei Stellen: Kopf-Knopf, Hero-Knopf,
    Preis-Anzeige), Style/Funktion unverändert. Datei liegt bereit zum Hochladen.
    Kauf-Knopf weiterhin Platzhalter (#) bis Digistore (Phase 3).

v0.16.8 (2026-06-07)
  - Preis von 24 € auf 69 € geändert (wertbasiert, nach Marktrecherche). 0.3 + 3.4
    aktualisiert. Landingpage-taugliche „Warum 69 €?"-Begründung in 0.3 ergänzt.
  - To-do (Dieter): „24" in index.html auf „69" ändern (mehrere Stellen).

v0.16.7 (2026-06-07)
  - Domain LIVE: dt-profidreieck.de zeigt auf GitHub Pages, HTTPS aktiv. 2.7
    abgehakt. Vollständige Laien-Anleitung (INWX A/CNAME + Parkeinträge löschen,
    GitHub „Benutzerdefinierte Domäne" + „HTTPS erzwingen") in 2.7 dokumentiert.
  - Kopf aktualisiert (Status/Produkt) – Plan spiegelt jetzt den realen Fortschritt.

v0.16.6 (2026-06-07)
  - 2.7 für Anfänger ausgebaut: konkreter INWX-Klickpfad (Nameserver → Domain →
    DNS-Eintrag hinzufügen), A-Records mit leerem „Name", www-CNAME auf
    dietertepe.github.io, Hinweis auf bestehenden Park-A-Eintrag.

v0.16.5 (2026-06-07)
  - Build-Stand bereinigt: widersprüchliche/veraltete Zeilen entfernt. Stand jetzt
    klar: beide Editionen obfuskiert; index.html ruft die obfuskierte Testversion
    auf; Rechtsseiten verlinkt; alles live, keine externen Ladequellen.
  - 2.6 (Hosting/Repo) abgehakt – Repo live mit obfuskierter Test + index +
    Impressum/Datenschutz. Pro-Datei bleibt bewusst draußen (nur Digistore-Tresor).

v0.16.4 (2026-06-07)
  - Landingpage geprüft: index.html + impressum.html + datenschutz.html live auf
    GitHub Pages, KEINE externen Ladequellen, Rechtstexte = Pflichttexte (inkl.
    §19, ohne USt-IdNr/OS-Plattform). 4.2/4.3 auf „in Arbeit" gesetzt; eigener
    `Landingpageplan_DT-ProfiDreieck.md` verlinkt.
  - Offen: Inhalts-Sektionen, Digistore-Link, YouTube-Link, sauberer Screenshot.

v0.16.3 (2026-06-06)
  - Obfuskierte Verteildateien geprüft (strukturell): nur Script verschleiert,
    CSS/HTML/DOM-IDs intakt, jsPDF heil, Dateien vollständig. 2.5 abgehakt
    (Funktionstest läuft).
  - Datei-Konvention festgehalten: `_Orginal` = lesbarer Master; Änderungen
    immer am Master, danach neu obfuskieren.

v0.16.2 (2026-06-06)
  - Online-Test bestätigt: beide Dateien liefen live über GitHub Pages
    (Repo dt-profidreieck-web) → ganze Hosting-Kette funktioniert. 2.6 auf
    „Mechanik getestet" gesetzt. Test-Uploads temporär/unverschlüsselt.

v0.16.1 (2026-06-06)
  - Pro-Datei korrigiert geprüft: `DT-ProfiDreieck_Pro_1-1-0.html` – APP-Block
    editioniert, Overlay „DT-ProfiDreieck Pro v1.1.0 (Engine 3.0.0)", §19-Satz
    vorhanden, Lizenz-Modal ok, keine Sperre. Beide Dateien jetzt konsistent.
  - 2.0b und 2.3 vollständig abgehakt; Build-Stand aktualisiert.

v0.16.0 (2026-06-06)
  - Domains bei INWX registriert → 1.1 abgehakt.
  - Zwei Build-Dateien geprüft: Test (1-1-0) passt zur Vorgabe ✅; Pro (3-1-0)
    hat i18n + Lizenz-Modal ✅, aber APP-Block noch nicht editioniert
    (name 'Dreiecksberechnung'/3.1.0) → Build-Stand-Notiz + offene Angleichung.
  - Editions-Version einheitlich auf 1.1.0 gesetzt.
  - 2.7 mit konkreten INWX/GitHub-DNS-Einträgen ausgebaut (A-Records, www-CNAME,
    Enforce HTTPS, optional E-Mail-Weiterleitung) inkl. Reihenfolge-Hinweis.
  - Checklisten-Status aktualisiert (erledigt/teilweise/offen).

v0.15.0 (2026-06-04)
  - Verbindlicher Build-Kontext übernommen; 2.0a/2.0b/2.0c jetzt entschieden (✅).
  - KLARSTELLUNG: Engine bleibt 3.0.0 (kein „3.1.0" mehr); Editionen = 1.0.0.
    APP-Block: name='DT-ProfiDreieck', edition='Pro'/'Test', version='1.0.0',
    engine='3.0.0'; Overlay „… v1.0.0 (Engine 3.0.0)".
  - I18N präzisiert (nur UI/Buttons/Grid; Narrator/Fehler/Recht bleiben DE;
    Toggle neben #infoBtn; EN-Hinweis „Legal information in German only").
  - Lizenz-Modal (Pro): eigenes .overlay-Modal statt prompt().
  - Bauanleitung: „🔒 Verbindliche Bauvorgaben"-Box + angepasste Schritte
    (APP-Block, I18N, Modal); Pflichttest nach Obfuscation: DXF + Modal + SSW.
  - Pflichttexte §3: Overlay-Titel auf Editions-/Engine-Schema umgestellt.

v0.14.1 (2026-06-04)
  - Bauanleitung: „Schnelltest"-Hinweis ergänzt – für reine Mechanik-Tests aus
    3-0-0 bauen, Schritt 2.0 und Obfuscation weglassen, beliebiger Schlüssel.

v0.14.0 (2026-06-04)
  - Steuerstatus entschieden: Kleinunternehmer (§ 19 UStG). 1.3 + Stammdaten +
    Pflichttexte aktualisiert; USt-IdNr-Frage damit gelöst (§19-Satz statt IdNr).
  - KORREKTUR Umsatzgrenze: seit 2025 Vorjahr ≤ 25.000 € / laufendes Jahr
    ≤ 100.000 € (nicht mehr 22.000 €).
  - 3.2 Reseller: Kleinunternehmer bekommt Provision netto.
  - 3.3 Lizenzschlüssel-Automatik in 3 Schritten konkretisiert (einschalten,
    E-Mail-Platzhalter, automatische Auslieferung).

v0.13.0 (2026-06-04)
  - NEUE Vorstufe 2.0 „Quellcode-Ausbau zur 3.1.0" (vor dem Test/Pro-Split):
    * 2.0a Zweisprachigkeit DE/EN – Tiefe: Bedienung + Ergebnis-Beschriftungen.
      Rechtstexte, Rechenweg und Solver-Fehlermeldungen bleiben Deutsch
      (bewusst kein englischer Rechtsbereich); DE Standard, sichtbarer Schalter.
    * 2.0b Editions-Namen (Pro/Test) + eigene Historie + Edition-/Engine-Version.
    * 2.0c Overlay-Ordnung; DE/EN-Schalter klein aber sichtbar.
  - Hinweis ergänzt: Pro/Test bauen auf der 3.1.0 auf; Anker/Bauanleitung danach
    aktualisieren.

v0.12.0 (2026-06-04)
  - Kompatibilität mit 3-0-0 verifiziert (echte Funktionen geprüft: initModal/
    #modalFoot, QUANTS/GROUPS, refreshPillStates, selectQuant, addEventListener-
    Verdrahtung).
  - NEU: Anhang „Bauanleitung für einen neuen Chat" – Schritt-für-Schritt für
    Pro & Test, mit exakten Andockpunkten und Upsell-Texten.
  - NEU: Projektdateien-Hinweis oben (3-0-0.html + Pflichttexte_Entwurf.md),
    damit ein neuer Chat beide Dateien kennt und nutzt.
  - Klargestellt: Datei ist addEventListener-basiert → obfuscation-freundlich.

v0.11.0 (2026-06-04)
  - 2.4 abgeschlossen: Idee 1 ausgebaut – Spezial-Pills (R/r/Fläche/Höhen)
    gesperrt mit je eigener, konkreter Upsell-Botschaft + „freischalten"-Knopf.
  - Zeitsperre ausdrücklich VERWORFEN (mit Begründung), damit sie nicht
    wiederkommt. Optionaler wegklickbarer Hinweis als 💡 vermerkt.

v0.10.0 (2026-06-04)
  - NEU: Anhang „Technische Anker in Dreiecksberechnung_3-0-0.html" – präzise
    Haltegriffe (APP.version, #modalFoot, Pill-Stile, Export-IDs, caseType),
    damit ein neuer Chat Pro/Test fehlerfrei bauen kann.
  - 2.4 Testversion-Entscheidungen festgehalten: sichtbar-gesperrt + Upsell;
    „Werbung" = Eigenwerbung für Pro; DXF (und damit alle Exporte) bleiben frei;
    Pro-Burggraben = Spezialfälle (R/r/Fläche/Höhen). Feinschliff offen.

v0.9.1 (2026-06-04)
  - 2.3 abgeschlossen: Info-Overlay-Texte für Test- und Pro-Version festgelegt.
  - Korrigierte HTML-Blöcke in „Pflichttexte_Entwurf" (Abschnitt 3) gespeichert
    (kaputter Link gefixt, <br> ergänzt, Version via APP-Block, rel=noopener,
    Platzhalter „—"). Telefon bewusst nur im Online-Impressum.

v0.9.0 (2026-06-04)
  - KORREKTUR: Digistore24 personalisiert KEINE HTML-Dateien (Download-Vault
    liefert unverändert aus); frühere {{LIZENZ}}-Platzhalter-Annahme verworfen.
  - Wasserzeichen entschieden: Mischung A+B (selbst eingegebener Name +
    eindeutiger Digistore-Lizenzschlüssel), einsteigergerecht in 2.2 erklärt.
  - Cross-Checks ergänzt: A+B NUR in die Pro-Version (2.2), Testversion bleibt
    OHNE Wasserzeichen (2.4); Lizenzschlüssel-Aktivierung bei 3.3 vermerkt.
  - 2.5-Hinweis an neue Lösung angepasst (kein Digistore-Platzhalter mehr).

v0.8.0 (2026-06-04)
  - Werkzeug-Entscheidung: obfuscator.io (Web) gewählt; javascript-obfuscator
    (lokal) als spätere Option vermerkt.
  - Empfohlene Einstellungen mit Begründung ergänzt (anhaken/nicht anhaken/
    Target Browser), zugeschnitten auf rechenintensives, offline laufendes Tool.
  - Wichtigste Warnungen: Control Flow Flattening (Tempo) und Rename Globals
    (bricht Knopf→Funktion-Aufrufe) aus lassen.

v0.7.3 (2026-06-04)
  - 2.5 Klarstellung ergänzt: Verschleierung ≠ Verschlüsselung; warum eine
    echte „Sperre mit Käufercode" bei einem offline laufenden Single-File-
    Produkt nicht möglich ist; was Obfuscation tatsächlich schützt
    (Verstehen/Nachbauen, nicht die Ausführung).

v0.7.2 (2026-06-04)
  - 2.5 für Einsteiger erklärt: nur der <script>-Block (≈ Zeile 723–2645) wird
    verschleiert, nicht die ganze HTML; Schritt-für-Schritt mit obfuscator.io
    (ohne Installation); Klarstellung Java ≠ JavaScript.
  - Ergänzt: Käufer nutzt die verschlüsselte HTML wie jede HTML (Doppelklick →
    Browser → läuft, offline, keine Installation).

v0.7.1 (2026-06-04)
  - 2.5 Obfuscation konkretisiert: Tool-Empfehlungen mit Links und Begründung.
    Favorit javascript-obfuscator (lokal, gratis), obfuscator.io (gratis,
    Web), JScrambler (paid/Overkill). Plus Stolpersteine (moderate Optionen,
    danach testen, Wasserzeichen-Platzhalter muss Obfuscation überleben).

v0.7.0 (2026-06-04)
  - GROSSER UMBAU: Dokument in zwei Ebenen geteilt –
    Teil 1 kurze Ablauf-Checkliste zum Abhaken, Teil 2 ausführliche
    Erklärungen mit gleicher Nummerierung und gleichen Markern.
  - Checkbox-Logik ergänzt (was real erledigt ist).
  - NEUE Bau-Punkte aufgenommen:
      2.2 Wasserzeichen + Versionsnummer in die Pro-Datei einbauen,
      2.3 Impressum/Rechtshinweis IN der HTML (Info-Bereich),
      2.4 Testversion bauen (Feature-Sperre, Overlay, Werbung),
      4.3 Landingpage technisch erstellen.
  - Phase 2 technisch sinnvoll neu sortiert (2.1–2.7).
  - Reichweite zu 4.4 verschoben (4.4.1 Gruppen/Foren, 4.4.2 YouTube).

v0.6.1 (2026-06-04)
  - Start-Video DXF festgelegt; Skript auf später vertagt.
  - „Stöbern als Aufklärung" ergänzt.

v0.6.0 (2026-06-04)
  - YouTube zur Video-Reihe ausgebaut; SEO-Einsicht Spezialfälle;
    vollständiger Video-Vorrat (A–D).

v0.5.0 (2026-06-04)
  - YouTube fest eingeplant; Aufbau, Fallbeispiele, Doppelnutzung.

v0.4.0 (2026-06-04)
  - Gruppen/Foren ohne Spam; Selbsttest, Grundregeln, 3 Vorlagen.

v0.3.0 (2026-06-04)
  - Reichweite (Pull vs. Push); Kanal-Kandidaten; Kleinanzeigen abgeraten.

v0.2.1 (2026-06-04)
  - Stammdaten erfasst; Webdienste-Liste; Pflichttexte-Entwurf erstellt.

v0.2.0 (2026-06-04)
  - Preis 24 € ohne Staffelung; Pflichttexte über Generator.

v0.1.0 (2026-06-04)
  - Erste Fassung; Phase 0 ergänzt; Wasserzeichen & Pflichttexte aufgenommen.
```
