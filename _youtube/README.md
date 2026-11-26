# YouTube – Arbeitsordner

Stand: 25.11.2026 · Besitzer: Dieter Tepe

Hier liegt alles, was für die YouTube-Videos gebraucht wird: Planung, Drehbücher,
Titel und Beschreibungen in DE/EN/PT, Status.

**Der Ordner ist nicht öffentlich.** Weil sein Name mit `_` beginnt, veröffentlicht
GitHub Pages ihn nicht (wie `_sprachen/`). Er taucht also weder auf dt-profidreieck.de
noch in Suchmaschinen auf.

## Wichtige Regeln

- **Claude filmt selbst:** Das Programm läuft in Claudes Browser (aus dem GitHub-Repo, ohne
  Internet). Ein Skript tippt die Werte ein und macht scharfe Bilder (doppelte Auflösung).
  Dieter muss nichts aufnehmen. Werkzeuge dazu in `werkzeuge/` (siehe unten).
- **In jedem Video wird der Ergebnisbereich mit Rechenweg und Formeln aufgeklappt** und
  lange genug gezeigt, dass man alles lesen kann – das ist das Wichtigste.
- **Ton:** ruhige Hintergrundmusik und leise Bediengeräusche, von Claude selbst erzeugt
  (keine fremden Musikstücke → keine Lizenzfragen). Lautheit −16 LUFS.
- **Freigabe:** Jedes Video schickt Claude zuerst **hier im Chat** (lässt sich auf dem Tablet
  direkt abspielen). Erst nach „freigegeben“ wird es per Pull Request eingebaut; den PR-Link
  bekommt Dieter vor dem Mergen. YouTube-Hochladen braucht eine **zweite Freigabe**.
- **Keine Entwürfe ins Repo** – jede Videodatei bliebe sonst für immer in der Versionsgeschichte.
- **Fertige Videodateien** gehören in den öffentlichen Ordner des Programms, z. B.
  `Dreieck_Daten/videos/`, mit **neuem Dateinamen** (dann merkt Google die Änderung). Die
  alten Videos werden danach gelöscht. Für die Webseite klein halten (ca. 5–10 MB).
- **Ersetzen auf den Webseiten:** Hauptseite (`config.js` **und** `index.html`), Video-Sitemap
  (`sitemap.xml`) und die Videoseite unter `videos/` – mit Länge, Vorschaubild und Datum im JSON-LD.
- **Auf den eigenen Seiten kein eingebettetes YouTube** (lädt Google-Skripte und Cookies);
  höchstens ein einfacher Link „Auf YouTube ansehen“.
- **Bessere Einbindung für Suchmaschinen:** Untertitel-Datei (WebVTT) mit den eingeblendeten
  Texten und Werten, Sprungmarken („Eingabe“, „Ergebnis“, „Rechenweg“), VideoObject im JSON-LD,
  Vorschaubild mit Ergebnis, kurzer Text zum Beispiel auf der Videoseite.
- **Sprachen:** Claude kann das Programm auf EN/PT umstellen → echte Fassungen je Sprache möglich.
- **Beschreibung (YouTube und Videoseite)** enthält immer den Satz
  „Bildschirmaufnahme des Programms, Schnitt mit KI-Unterstützung.“ (EN/PT übersetzt).
  Beim YouTube-Upload „Veränderte Inhalte“ = **Nein** (echte Aufnahme, keine Täuschung).
- **V1/V2 (KI-Videos) bleiben vorerst unverändert**, bis Y01/Y02 sie ersetzen (Entscheidung 25.11.).
- Hochgeladen wird **jedes Video erst nach Dieters Freigabe**; YouTube erst, wenn die Seiten
  in den Suchmaschinen bekannter sind (Entscheidung 25.11.2026).
- Begriffe für Titel und Beschreibung nach der Begriffs-Tabelle in Projekt.md (Abschnitt 4b).

## Ablauf je Video

| Schritt | Was | Wer |
|---|---|---|
| 1. Idee | Inhalt, Ziel-Suchbegriff, Ziel-Seite festlegen | Claude + Dieter |
| 2. Drehbuch | Szenen, Eingabewerte, Texte im Bild | Claude |
| 3. Aufnahme | Programm in Claudes Browser, Skript gibt die Werte ein (`werkzeuge/capture.py`) | Claude |
| 4. Schnitt & Ton | Vorspann, Bildunterschriften, Rechenweg, Abspann, Musik (`werkzeuge/`) | Claude |
| 4b. Freigabe | Video im Chat ansehen, Änderungswünsche, „freigegeben“ | Dieter |
| 5. Webseite | Datei in `…_Daten/videos/`, Videoseite und JSON-LD (Dauer, Poster) anpassen | Claude |
| 6. YouTube | Titel/Beschreibung DE/EN/PT, Playlist, Link zur Startseite, Hochladen nach Freigabe | Claude nach Freigabe |

## Status

| Nr. | Video | Ersetzt | Status |
|---|---|---|---|
| Y01 | Dreieck: Fläche, Winkel, Höhe aus 3 Seiten | V1 (KI, `videos/dreieck-berechnen-demo.html`) | **Freigegeben 25.11.** · Webseite: `Dreieck_Daten/videos/dreieck-aus-3-seiten.mp4` (5,7 MB) auf `videos/dreieck-berechnen-demo.html` + Hauptseite · YouTube: offen |
| Y02 | Dreieck: Werkstück, Zeichnung, DXF für CNC | V2 (KI, `videos/dreieck-dxf-werkstatt.html`) | Idee |
| Y03 | Schraube: VDI 2230, Beispiel „Kombiniert M16 10.9 (axial + Querkraft)“ | `schraube-teaser.mp4` | **Freigegeben 26.11.** · Webseite: `Schraube_Daten/videos/schraube-m16-vdi-2230.mp4` (8,9 MB, 1:33) auf `videos/schraube-vdi-2230.html` + Hauptseite · YouTube: offen |
| Y04 | Passung: H7/g6 (Kurzeingabe) und Pressverband H7/s6 | `passung-teaser.mp4` | **Freigegeben 26.11.** · Webseite: `Passung_Daten/videos/passung-h7g6-h7s6.mp4` (8,3 MB, 1:26) auf `videos/passung-iso-286.html` + Hauptseite · YouTube: offen · Hinweis: im Rechenweg steht bei Schritt 27/32 „— artok“ (Fehler im Programm, behebt Dieter im Quellcode; danach Video neu) |
| Y05 | Schweißnaht: Rohr unter Torsion | `schweissnaht-teaser.mp4` | **Freigegeben 26.11.** · Webseite: `Schweissnaht_Daten/videos/schweissnaht-rohr-torsion.mp4` (9,1 MB, 1:27) auf `videos/schweissnaht-en-1993-1-8.html` + Hauptseite · YouTube: offen |

Einzelheiten: [videoliste.md](videoliste.md)

## Vorhandene Videos (Stand 25.11.2026)

| Datei | Größe | Verwendet auf | Bemerkung |
|---|---|---|---|
| ~~`Dreieck_Daten/videos/V1.mp4`~~ | – | – | gelöscht 25.11., ersetzt durch Y01 |
| `Dreieck_Daten/videos/V2.mp4` | 3,4 MB, 10 s | `videos/dreieck-dxf-werkstatt.html` | KI-generiert, seit 26.11. mit Hinweis „KI-generierte Darstellung“ im Bild |
| `Dreieck_Daten/videos/V3.mp4` … `V8.mp4` | je 2,4–3,0 MB | nirgends verlinkt | ungenutzt – ansehen, ob brauchbar, sonst später löschen |
| ~~`Schraube_Daten/videos/schraube-teaser.mp4`~~ | – | – | gelöscht 26.11., ersetzt durch Y03 |
| ~~`Passung_Daten/videos/passung-teaser.mp4`~~ | – | – | gelöscht 26.11., ersetzt durch Y04 |
| ~~`Schweissnaht_Daten/videos/schweissnaht-teaser.mp4`~~ | – | – | gelöscht 26.11., ersetzt durch Y05 |

## Werkzeuge (`werkzeuge/`)

Skripte, mit denen Y01 entstanden ist (Python + Playwright + ffmpeg, laufen in Claudes Umgebung).
Für ein neues Video kopieren und anpassen.

| Datei | Aufgabe |
|---|---|
| `capture.py` | Programm öffnen, Werte über den Assistenten eingeben, Bildschirmfotos (2×), Rechenweg und Zeichnung |
| `tiles.py` | Lage der Ergebnis-Kacheln für die Hervorhebungen |
| `cards.py` | Vorspann, Aufgaben-Karte, Abspann als Ebenen (HTML → PNG) |
| `render.py` | Szenen zusammensetzen (Kamera, Bildunterschriften, Übergänge) → je Szene eine MP4 |
| `audio.py` | Hintergrundmusik und Geräusche erzeugen |

Y05: angepasste Fassung in `werkzeuge/y05/` (Beispiel laden, Bereiche aufklappen, Ergebnis, Nahtbild, „Rechenweg im Detail“ mit 7 Stationen).

Y03: Fassung in `werkzeuge/y03/` (Beispiel laden, Bereiche, Ergebnis kurz, Visualisierung mit Kamerafahrt, Rechenweg mit 8 Stationen).

Y04: Fassung in `werkzeuge/y04/` (zwei Teile, Kamerafahrten innerhalb eines Bildes, Rechenweg mit hohem Browserfenster aufnehmen).

Zusammenfügen: `ffmpeg -f concat -safe 0 -i list.txt -c copy` und Ton mit `loudnorm=I=-16:TP=-1.5`.

## Ordner-Inhalt

- `README.md` – diese Übersicht (Regeln, Ablauf, Status)
- `videoliste.md` – Inhalt, Ziel-Suchbegriffe und Ziel-Seite je Video
- `werkzeuge/` – Skripte zum Filmen, Schneiden und für den Ton
- später je Video eine Datei `Y01-….md` mit Drehbuch, Titeln und Beschreibungen DE/EN/PT
