# YouTube – Arbeitsordner

Stand: 25.11.2026 · Besitzer: Dieter Tepe

Hier liegt alles, was für die YouTube-Videos gebraucht wird: Planung, Drehbücher,
Titel und Beschreibungen in DE/EN/PT, Status.

**Der Ordner ist nicht öffentlich.** Weil sein Name mit `_` beginnt, veröffentlicht
GitHub Pages ihn nicht (wie `_sprachen/`). Er taucht also weder auf dt-profidreieck.de
noch in Suchmaschinen auf.

## Wichtige Regeln

- **Fertige Videodateien gehören nicht hierher**, sondern in den öffentlichen Ordner des
  Programms, z. B. `Dreieck_Daten/videos/`. Grund: Windsor lädt Videos von einer
  Internetadresse zu YouTube hoch (max. 100 MB), die Datei muss also online erreichbar sein.
- Hier stehen nur Texte und Planung (Markdown), höchstens kleine Hilfsbilder.
- Hochgeladen wird **jedes Video erst nach Dieters Freigabe**.
- Zeitpunkt: erst wenn die Videos besser sind und die Seiten in den Suchmaschinen
  bekannter sind (Entscheidung 25.11.2026).
- Videos haben keinen Ton → Text im Bild oder Untertitel. So reicht **ein Video für alle
  drei Sprachen**; nur Titel, Beschreibung und Untertitel werden übersetzt.
- Begriffe für Titel und Beschreibung nach der Begriffs-Tabelle in Projekt.md (Abschnitt 4b).

## Ablauf je Video

| Schritt | Was | Wer |
|---|---|---|
| 1. Idee | Inhalt, Ziel-Suchbegriff, Ziel-Seite festlegen | Claude + Dieter |
| 2. Drehbuch | Szenen, Eingabewerte, Texte im Bild | Claude |
| 3. Aufnahme | Bildschirmaufnahme der Testversion (Android: Schnelleinstellungen → „Bildschirmaufnahme“) | Dieter |
| 4. Schnitt | Vorspann/Abspann (z. B. HyperFrames), Texte einblenden, kürzen | Claude + Dieter |
| 5. Webseite | Datei in `…_Daten/videos/`, Videoseite und JSON-LD (Dauer, Poster) anpassen | Claude |
| 6. YouTube | Titel/Beschreibung DE/EN/PT, Playlist, Link zur Startseite, Hochladen nach Freigabe | Claude nach Freigabe |

## Status

| Nr. | Video | Ersetzt | Status |
|---|---|---|---|
| Y01 | Dreieck: Fläche, Winkel, Höhe aus 3 Seiten | V1 (KI, `videos/dreieck-berechnen-demo.html`) | Idee |
| Y02 | Dreieck: Werkstück, Zeichnung, DXF für CNC | V2 (KI, `videos/dreieck-dxf-werkstatt.html`) | Idee |
| Y03 | Schraube: VDI 2230 Beispiel M12 10.9 | `schraube-teaser.mp4` | Idee |
| Y04 | Passung: H7/g6 und Pressverband H7/s6 | `passung-teaser.mp4` | Idee |
| Y05 | Schweißnaht: Rohr unter Torsion | `schweissnaht-teaser.mp4` | Idee |

Einzelheiten: [videoliste.md](videoliste.md)

## Vorhandene Videos (Stand 25.11.2026)

| Datei | Größe | Verwendet auf | Bemerkung |
|---|---|---|---|
| `Dreieck_Daten/videos/V1.mp4` | 2,9 MB, 10 s | `videos/dreieck-berechnen-demo.html` | KI-generiert, Formeln unleserlich, „Google“-Schriftzug |
| `Dreieck_Daten/videos/V2.mp4` | 2,6 MB, 10 s | `videos/dreieck-dxf-werkstatt.html` | KI-generiert |
| `Dreieck_Daten/videos/V3.mp4` … `V8.mp4` | je 2,4–3,0 MB | nirgends verlinkt | ungenutzt – ansehen, ob brauchbar, sonst später löschen |
| `Schraube_Daten/videos/schraube-teaser.mp4` | 4,1 MB, 40 s | `videos/schraube-vdi-2230.html` | Teaser |
| `Passung_Daten/videos/passung-teaser.mp4` | 3,8 MB, 40 s | `videos/passung-iso-286.html` | Teaser |
| `Schweissnaht_Daten/videos/schweissnaht-teaser.mp4` | 5,2 MB, 40 s | `videos/schweissnaht-en-1993-1-8.html` | Teaser |

## Ordner-Inhalt

- `README.md` – diese Übersicht (Regeln, Ablauf, Status)
- `videoliste.md` – Inhalt, Ziel-Suchbegriffe und Ziel-Seite je Video
- später je Video eine Datei `Y01-….md` mit Drehbuch, Titeln und Beschreibungen DE/EN/PT
