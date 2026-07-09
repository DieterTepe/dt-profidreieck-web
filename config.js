/* =========================================================================
   DT-ProfiTools – ZENTRALE LINK-KONFIGURATION
   =========================================================================
   NUR DIESE DATEI bearbeiten, um Links zu ändern – index.html bleibt unberührt.

   Digistore24-Links eintragen:
     1. Zeile mit kaufDreieck / kaufSchraube suchen
     2. Das "#kauf-dreieck" bzw. "#kauf-schraube" durch den echten
        Digistore-Bestelllink ersetzen, z. B.:
        kaufDreieck: "https://www.digistore24.com/product/123456",
     3. Datei speichern und zu GitHub hochladen – fertig.

   Solange noch "#kauf-..." drinsteht, springen die Kauf-Buttons einfach
   zum jeweiligen Kaufblock auf der Seite (nichts geht kaputt).
   ========================================================================= */

window.DT_CONFIG = {

  /* --- Digistore24-Bestelllinks (Platzhalter ersetzen!) ---------------- */
  kaufDreieck:  "#kauf-dreieck",
  kaufSchraube: "#kauf-schraube",

  /* --- Gratis-Testversionen -------------------------------------------- */
  testDreieck:  "DT-ProfiDreieck_Test_1-1-0.html",
  testSchraube: "https://dietertepe.github.io/dt-profischraube-web/DT-ProfiSchraube_Test.html"

};
