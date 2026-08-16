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
  kaufDreieck:      "https://www.checkout-ds24.com/product/722585",
  kaufSchraube:     "https://www.checkout-ds24.com/product/722968",
  kaufPassung:      "https://www.checkout-ds24.com/product/722972",
  kaufSchweissnaht: "https://www.checkout-ds24.com/product/722975",

  /* --- Gratis-Testversionen ---------------------------------------------- */
  testDreieck:      "https://dietertepe.github.io/dt-profidreieck-web/DT-ProfiDreieck_Test_1-1-0.html",
  testSchraube:     "https://dietertepe.github.io/dt-profischraube-web/DT-ProfiSchraube_Test.html",
  testPassung:      "https://dietertepe.github.io/dt-profipassung-web/DT-ProfiPassung_Testversion.html",
  testSchweissnaht: "https://dietertepe.github.io/dt-profischweissnaht-web/DT-ProfiSchweissnaht_Testversion.html",

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
    videoDemo: "https://dietertepe.github.io/dt-profidreieck-web/Dreieck_Daten/videos/V1.mp4",

    // Screenshot-Paar unter den Videos in Pos. 01 – links: Eingabemaske
    bildEingabe: "https://dietertepe.github.io/dt-profidreieck-web/Dreieck_Daten/bilder/app-eingabe.jpg",

    // Screenshot-Paar unter den Videos in Pos. 01 – rechts: Rechenweg/Ergebnis
    bildErgebnis: "https://dietertepe.github.io/dt-profidreieck-web/Dreieck_Daten/bilder/app-ergebnis.jpg"
  },

  /* ======================================================================
     MEDIEN – DT-PROFISCHRAUBE   (Ordner: Schraube_Daten/)
     ====================================================================== */
  schraube: {

    // Startansicht mit grünen Nachweisen: Hero-Werkzeugkarte UND
    // Vorschaubild (Poster) des Teaser-Videos in Pos. 02.
    bildStart: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-start.jpg",

    // 40-Sekunden-Teaser oben in Pos. 02 – MP4 (H.264), 1280x720, < 10 MB
    videoTeaser: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/videos/schraube-teaser.mp4",

    // Großes Screenshot-Paar in Pos. 02 – links: dokumentierter Rechenweg
    bildRechenweg: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-rechenweg.jpg",

    // Großes Screenshot-Paar in Pos. 02 – rechts: Verspannungsschaubild
    bildSchaubild: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-schaubild.jpg",

    // Dreierreihe darunter – links: Flansch-Assistent
    bildFlansch: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-flansch.jpg",

    // Dreierreihe – Mitte: Hilfetext / Anziehverfahren
    bildHilfe: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-hilfe.jpg",

    // Dreierreihe – rechts: Word-Export-Bestätigung
    bildWord: "https://dietertepe.github.io/dt-profidreieck-web/Schraube_Daten/bilder/schraube-word.jpg"
  },

  /* ======================================================================
     MEDIEN – DT-PROFIPASSUNG   (Ordner: Passung_Daten/)
     ====================================================================== */
  passung: {

    // Startansicht (Eingabe + Ergebnis): Hero-Werkzeugkarte UND
    // Vorschaubild (Poster) des Teaser-Videos in Pos. 03.
    bildStart: "https://dietertepe.github.io/dt-profidreieck-web/Passung_Daten/bilder/passung-start.jpg",

    // 40-Sekunden-Teaser oben in Pos. 03
    videoTeaser: "https://dietertepe.github.io/dt-profidreieck-web/Passung_Daten/videos/passung-teaser.mp4",

    // Großes Screenshot-Paar – links: Toleranzfeld-Schaubild
    bildSchaubild: "https://dietertepe.github.io/dt-profidreieck-web/Passung_Daten/bilder/passung-schaubild.jpg",

    // Großes Screenshot-Paar – rechts: selbstprüfender Rechenweg
    bildRechenweg: "https://dietertepe.github.io/dt-profidreieck-web/Passung_Daten/bilder/passung-rechenweg.jpg",

    // Dreierreihe – links: Passungs-Assistent mit Vorschlägen
    bildAssistent: "https://dietertepe.github.io/dt-profidreieck-web/Passung_Daten/bilder/passung-assistent.jpg",

    // Dreierreihe – Mitte: Pressverband nach DIN 7190
    bildPressverband: "https://dietertepe.github.io/dt-profidreieck-web/Passung_Daten/bilder/passung-pressverband.jpg",

    // Dreierreihe – rechts: Praxis-Beratung (Thermik, Kostenampel, Messmittel)
    bildBeratung: "https://dietertepe.github.io/dt-profidreieck-web/Passung_Daten/bilder/passung-beratung.jpg"
  },

  /* ======================================================================
     MEDIEN – DT-PROFISCHWEISSNAHT   (Ordner: Schweissnaht_Daten/)
     ====================================================================== */
  schweissnaht: {

    // Startansicht (Eingabe + Ergebnis mit Ausnutzung, σ_v, maßgebender Punkt):
    // Hero-Werkzeugkarte oben UND Vorschaubild (Poster) des Teaser-Videos.
    // Querformat, ca. 1500 px breit, JPG < 300 KB
    bildStart: "https://dietertepe.github.io/dt-profidreieck-web/Schweissnaht_Daten/bilder/schweissnaht-start.jpg",

    // 40-Sekunden-Teaser oben in Pos. 04
    // MP4 (H.264), 1280x720, < 10 MB
    videoTeaser: "https://dietertepe.github.io/dt-profidreieck-web/Schweissnaht_Daten/videos/schweissnaht-teaser.mp4",

    // Großes Screenshot-Paar – links: gezeichnetes Nahtbild mit Schwerpunkt
    // (das Alleinstellungsmerkmal – Hochformat)
    bildNahtbild: "https://dietertepe.github.io/dt-profidreieck-web/Schweissnaht_Daten/bilder/schweissnaht-nahtbild.jpg",

    // Großes Screenshot-Paar – rechts: Rechenweg mit Häkchen und Quellenangabe
    bildRechenweg: "https://dietertepe.github.io/dt-profidreieck-web/Schweissnaht_Daten/bilder/schweissnaht-rechenweg.jpg",

    // Dreierreihe – links: geführter Assistent (Bemessungswelt)
    bildAssistent: "https://dietertepe.github.io/dt-profidreieck-web/Schweissnaht_Daten/bilder/schweissnaht-assistent.jpg",

    // Dreierreihe – Mitte: Rechenproben mit bestandenen Häkchen
    bildProben: "https://dietertepe.github.io/dt-profidreieck-web/Schweissnaht_Daten/bilder/schweissnaht-proben.jpg",

    // Dreierreihe – rechts: Liste „Was NICHT geprüft wird“
    bildGrenzen: "https://dietertepe.github.io/dt-profidreieck-web/Schweissnaht_Daten/bilder/schweissnaht-grenzen.jpg"
  }

  /* ----------------------------------------------------------------------
     HINWEIS: Favicons und die Social-Vorschaukarte (og-card.jpg) liegen
     BEWUSST NICHT hier, sondern fest im <head> der index.html – WhatsApp,
     LinkedIn & Co. lesen nur das rohe HTML und führen kein JavaScript aus.
     Die Dateien liegen im Ordner Landigpage_Daten/.
     ---------------------------------------------------------------------- */
};
