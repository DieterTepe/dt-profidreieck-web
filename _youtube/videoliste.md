# Videoliste – Entwurf

Stand: 25.11.2026 · noch nicht freigegeben

Grundidee: Jedes Video zeigt **genau das Rechenbeispiel, das schon auf der passenden
Startseite steht**. Dann passen Video, Seitentext und Suchbegriff zusammen, und die
Zahlen sind geprüft (sie stammen aus den eingebauten Programmbeispielen).

Format für alle: 16:9, 1920 × 1080, 30 fps, mit ruhiger Musik, 60–120 s. Texte im Bild kurz und groß
(aufs Handy achten). Aufbau: Vorspann 3–5 s → Eingabe → Ergebnis/Rechenweg →
Abspann mit Adresse der Startseite und „Kostenlos testen, ohne Anmeldung“.

Später zusätzlich möglich: je Video ein **Short** (Hochformat 9:16, unter 60 s) mit nur
dem wichtigsten Moment.

---

## Y01 – Dreieck: Fläche, Winkel und Höhe aus drei Seiten

- **Ersetzt:** V1 (`videos/dreieck-berechnen-demo.html`)
- **Ziel-Seite:** https://dietertepe.github.io/test-dreieck/#aufgaben
- **Suchbegriffe:** DE „dreieck berechnen“ (14.800), „fläche dreieck berechnen ohne höhe“,
  „dreieck winkel berechnen mit 3 seiten“ · EN „triangle calculator“ (40.500),
  „area of a triangle with 3 sides“ · PT „calculadora de triângulo“
- **Inhalt:** drei Seiten eingeben → Winkel, Fläche (Heron), Höhen erscheinen →
  maßstäbliche Zeichnung → Rechenweg aufklappen.
- **Hinweis:** größtes Potenzial aller Videos (vor allem EN). Als Erstes machen.
- **Stand 25.11.:** Entwurf 1 fertig (72 s): Vorspann → Aufgabe (a = 7, b = 5, c = 6 mm) →
  Eingabe über den Assistenten → Ergebnis mit Hervorhebung (Winkel, Fläche 14,70 mm², Höhen) →
  Rechenweg (Kosinussatz, Winkelsumme, Heron, Höhen, Proben) → Zeichnung mit Höhen → Abspann
  „Jetzt kostenlos testen“. **Von Dieter freigegeben (25.11.).** Eingebaut mit Untertiteln (`.de.vtt`), Kapiteln (`.kapitel.vtt`), Sprungmarken (`?t=…`) und Beispieltext.

## Y02 – Dreieck: vom Werkstück zur DXF für die CNC

- **Ersetzt:** V2 (`videos/dreieck-dxf-werkstatt.html`)
- **Ziel-Seite:** https://dietertepe.github.io/test-dreieck/
- **Suchbegriffe:** DE „winkel am werkstück berechnen“, „dreieck dxf“, CNC ·
  EN „triangle solver dxf“
- **Inhalt (umgesetzt):** Knotenblech a = 400 mm, b = 250 mm, γ = 70° (Fall SWS) im Assistenten
  der **Vollversion** → c = 392,55 mm, α = 73,24°, β = 36,76°, A = 46.984,63 mm² → Rechenweg
  (Kosinussatz, Heron) → Zeichnung, Hilfslinien aus → Bezeichnung „Knotenblech K1“, DXF mm →
  DXF-Vorschau aus der echten Datei (Kontur wie Laserbahn) → Abspann Testversion / Vollversion 69 €.
- **Status:** freigegeben und live seit 27.11.2026 (`Dreieck_Daten/videos/dreieck-knotenblech-dxf.mp4`, 1:22).
- **Hinweis:** Die Vollversion liegt nur lokal bei der Aufnahme, nie im Repo.

## Y03 – Schraube: VDI 2230 Beispiel M12 10.9

- **Ersetzt:** `schraube-teaser.mp4` (`videos/schraube-vdi-2230.html`)
- **Ziel-Seite:** https://dietertepe.github.io/dt-profischraube-web/
- **Suchbegriffe:** DE „schraubenberechnung vdi 2230“, „vdi 2230 beispiel“,
  „vorspannkraft berechnen“, „anziehdrehmoment berechnen“ · EN „VDI 2230 bolt calculator“
- **Inhalt:** Programmbeispiel „Hydraulikzylinder (M12, VDI-2230-Beispiel)“ laden →
  F_Mmin 27.519 N, F_Mmax 46.782 N ≤ F_Mzul 58.379 N → M_A 103,4 N·m →
  Sicherheiten S_F 1,23 · S_D 10,27 · S_P 3,15.
- **Stand 26.11.:** Auf Dieters Wunsch mit **M16 10.9** statt M12 – Programmbeispiel „Kombiniert M16 10.9 (axial + Querkraft)“: F_Mzul = 106.119 N, M_A = 274 N·m, S_F 1,25 · S_P 1,38 · S_G 1,30 (Ampel gelb: Dauerhaltbarkeit/Einschraubtiefe nicht gefordert). Mit Verspannungsdiagramm und Schnittdarstellung. Freigegeben und eingebaut.

## Y04 – Passung: H7/g6 und Pressverband H7/s6

- **Ersetzt:** `passung-teaser.mp4` (`videos/passung-iso-286.html`)
- **Ziel-Seite:** https://dietertepe.github.io/dt-profipassung-web/
- **Suchbegriffe:** DE „h7 g6“, „passung h7 g6“, „passungsrechner“,
  „einpresskraft passung berechnen“ · EN „H7/g6 fit“ · PT „ajuste H7 g6“
- **Inhalt:** Teil 1 „25 H7/g6“ → Spiel 7 … 41 µm, Toleranzfeld-Bild.
  Teil 2 „Zahnrad-Schrumpfsitz · 60 H7/s6“ → Übermaß 23 … 72 µm,
  Fugendruck 24,3 … 88,6 N/mm², M_t,max 962,2 N·m, Einpresskraft 116,9 kN,
  Nabe auf 211,3 °C.
- **Stand 26.11.:** Freigegeben und eingebaut (86 s). Teil 1: „25 H7/g6“ in die Kurzeingabe getippt (rechnet sofort). Teil 2: Beispiel „Zahnrad-Schrumpfsitz · 60 H7/s6“ mit Pressverband und Rechenweg (7 Stationen). Programmfehler „— artok“ in Schritt 27/32 noch sichtbar.

## Y05 – Schweißnaht: Rohr unter Torsion

- **Ersetzt:** `schweissnaht-teaser.mp4` (`videos/schweissnaht-en-1993-1-8.html`)
- **Ziel-Seite:** https://dietertepe.github.io/dt-profischweissnaht-web/#rohr-torsion
- **Suchbegriffe:** DE „schweißnahtberechnung rohr torsion“, „kehlnaht berechnen“,
  „schweißnaht berechnen eurocode 3“ · EN „fillet weld calculator“,
  „weld strength calculator“ (260)
- **Inhalt:** Rundrohr 114,3 × 6, Kehlnaht a = 4 mm, S235, T = 9 kNm →
  W_t = 79.408 mm³ → τ∥ = 113,3 N/mm² → σ_v = 196,3 ≤ 360 N/mm² → η = 0,55.
- **Stand 26.11.:** Freigegeben ohne Änderungen und eingebaut (87 s). Programmbeispiel „Rundrohr 114,3×6 auf Platte, Kreisnaht, Torsion 9 kNm“ → η = 0,545, σ_v = 196,3 N/mm², 21/21 Rechenproben.

---

## Offene Fragen

- Reihenfolge: Vorschlag Y01 ✓ → Y05 ✓ → Y03 ✓ → Y04 ✓ → Y02 ✓.
- ~~Aufnahme auf dem Tablet oder am PC?~~ → **Claude filmt selbst im Browser** (Entscheidung 25.11.), Dieter gibt nur frei.
- V3–V8 ansehen: brauchbar oder löschen?
- YouTube-Kanal: Name „DT-ProfiTools“? Kanalbild und Banner nötig.
- Playlists: je Programm eine, oder eine gemeinsame?
