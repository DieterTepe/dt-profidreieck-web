/* =========================================================================
   DT-ProfiTools – ZENTRALE LINK- UND MEDIEN-KONFIGURATION
   =========================================================================
   NUR DIESE DATEI bearbeiten, um Links, Bilder oder Videos zu ändern –
   die index.html bleibt vollkommen unberührt.

   REGELN:
   - Alle Medienpfade sind VOLLSTÄNDIGE, ABSOLUTE URLs (https://...), damit
     sofort erkennbar ist, aus welchem Repository eine Datei kommt.
   - Ein leerer Eintrag ("") blendet auf der Seite automatisch einen sauberen
     Platzhalter ein ("folgt in Kürze") – nichts geht kaputt. Sobald du die
     URL einträgst und hochlädst, erscheint das Medium an seinem Platz.

   DIGISTORE-LINKS EINTRAGEN:
     Das "#kauf-..." durch den echten Bestelllink ersetzen, z. B.:
     kaufDreieck: "https://www.digistore24.com/product/123456",
     Solange der Platzhalter drinsteht, springt der Button nur zum
     jeweiligen Kaufblock auf der Seite.
   ========================================================================= */

window.DT_CONFIG = {

  /* --- Digistore24-Bestelllinks (Platzhalter ersetzen!) ------------------ */
  kaufDreieck:  "#kauf-dreieck",
  kaufSchraube: "#kauf-schraube",
  kaufPassung:  "#kauf-passung",

  /* --- Gratis-Testversionen ---------------------------------------------- */
  testDreieck:  "https://dietertepe.github.io/dt-profidreieck-web/DT-ProfiDreieck_Test_1-1-0.html",
  testSchraube: "https://dietertepe.github.io/dt-profischraube-web/DT-ProfiSchraube_Test.html",
  testPassung:  "https://dietertepe.github.io/dt-profipassung-web/DT-ProfiPassung_Testversion.html",

  /* ======================================================================
     MEDIEN – DT-PROFIDREIECK   (Ordner: Dreieck_Daten/)
     ====================================================================== */
  dreieck: {

    // Marken-Zeichnung: erscheint ZWEIMAL – als kleines Bild in der
    // Hero-Werkzeugkarte oben UND als große Blueprint-Grafik in Pos. 01.
    // Querformat, ca. 1200-1600 px breit, JPG < 300 KB
    bildZeichnung: "https://dietertepe.github.io/dt-profidreieck-web/Dreieck_Daten/bilder/app-zeichnung.jpg",

    // Erstes Video in Pos. 01 ("ein Winkel am Werkstück ... DXF in CAD/CNC")
    // MP4 (H.264), 1280x720, optimiert für Web, ideal < 15 MB
    videoWerkstatt: "https://dietertepe.github.io/dt-profidreieck-web/Dreieck_Daten/videos/V2.mp4",

    // Zweites Video in Pos. 01 ("Von der Eingabe bis zum Ergebnis")
    // MP4 (H.264), 1280x720, optimiert für Web
    videoDemo: "https://dietertepe.github.io/dt-profidreieck-web/Dreieck_Daten/videos/V1.mp4",

    // Screenshot-Paar unter den Videos in Pos. 01 – links: Eingabemaske
    // Hochkant/Handy-Format ok, ca. 1000-1500 px breit, JPG < 300 KB
    bildEingabe: "https://dietertepe.github.io/dt-profidreieck-web/Dreieck_Daten/bilder/app-eingabe.jpg",

    // Screenshot-Paar unter den Videos in Pos. 01 – rechts: Rechenweg/Ergebnis
    bildErgebnis: "https://dietertepe.github.io/dt-profidreieck-web/Dreieck_Daten/bilder/app-ergebnis.jpg"
  },

  /* ======================================================================
     MEDIEN – DT-PROFISCHRAUBE   (Ordner: Schraube_Daten/)
     ====================================================================== */
  schraube: {

    // Startansicht mit grünen Nachweisen: erscheint in der Hero-Werkzeugkarte
    // UND als Vorschaubild (Poster) des Teaser-Videos in Pos. 02.
    // Querformat, ca. 1500 px breit, JPG < 300 KB
    bildStart: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-start.jpg",

    // 40-Sekunden-Teaser oben in Pos. 02
    // MP4 (H.264), 1280x720, < 10 MB
    videoTeaser: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/videos/schraube-teaser.mp4",

    // Großes Screenshot-Paar in Pos. 02 – links: dokumentierter Rechenweg
    // ca. 1200-1500 px breit, JPG < 300 KB
    bildRechenweg: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-rechenweg.jpg",

    // Großes Screenshot-Paar in Pos. 02 – rechts: Verspannungsschaubild
    bildSchaubild: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-schaubild.jpg",

    // Dreierreihe darunter – links: Flansch-Assistent (Hochformat ok)
    bildFlansch: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-flansch.jpg",

    // Dreierreihe – Mitte: Hilfetext / Anziehverfahren
    bildHilfe: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-hilfe.jpg",

    // Dreierreihe – rechts: Word-Export-Bestätigung
    bildWord: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-word.jpg"
  },

  /* ======================================================================
     MEDIEN – DT-PROFIPASSUNG   (Ordner: Passung_Daten/)
     ----------------------------------------------------------------------
     Noch keine Dateien vorhanden -> Einträge leer lassen ("").
     Die Seite zeigt an diesen Stellen automatisch "folgt in Kürze".
     Sobald Screenshots/Video fertig sind: hochladen nach
     Passung_Daten/bilder/ bzw. Passung_Daten/videos/ und hier die
     vollständige URL eintragen (Beispielnamen stehen als Muster dabei).
     ====================================================================== */
  passung: {

    // Startansicht: Hero-Werkzeugkarte oben UND Poster des Teaser-Videos.
    // Querformat, ca. 1500 px breit, JPG < 300 KB
    // Beispiel: "https://dietertepe.github.io/dt-profidreieck-web/Passung_Daten/bilder/passung-start.jpg"
    bildStart: "",

    // Teaser-/Demovideo oben in Pos. 03
    // MP4 (H.264), 1280x720, 30-60 s, < 10 MB
    // Beispiel: ".../Passung_Daten/videos/passung-teaser.mp4"
    videoTeaser: "",

    // Großes Screenshot-Paar – links: Toleranzfeld-Schaubild
    // (Bohrung grün, Welle blau – der stärkste Blickfang!)
    bildSchaubild: "",

    // Großes Screenshot-Paar – rechts: aufgeklappter Rechenweg mit Häkchen
    bildRechenweg: "",

    // Dreierreihe – links: Passungs-Assistent mit Empfehlung
    bildAssistent: "",

    // Dreierreihe – Mitte: Sprachumschalter DE / EN / PT
    bildSprachen: "",

    // Dreierreihe – rechts: Praxis-Beratung (Kostenampel, Messmittel)
    bildBeratung: ""
  }

  /* ----------------------------------------------------------------------
     HINWEIS: Favicons und die Social-Vorschaukarte (og-card.jpg) liegen
     BEWUSST NICHT hier, sondern fest im <head> der index.html – WhatsApp,
     LinkedIn & Co. lesen nur das rohe HTML und führen kein JavaScript aus.
     Die Dateien liegen im Ordner Landigpage_Daten/.
     ---------------------------------------------------------------------- */
};
