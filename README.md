# DT-ProfiDreieck – Dreiecksberechnung mit DXF-Export

DT-ProfiDreieck berechnet Dreiecke aus drei beliebigen bekannten Größen und
zeichnet sie maßstäblich. Anschließend lässt sich die Zeichnung als DXF
exportieren und direkt in CAD oder an der CNC weiterverwenden.

Gedacht für Werkstatt, Konstruktion, Vorrichtungsbau und für den Unterricht.

## Testversion

**[DT-ProfiDreieck Testversion starten](https://dietertepe.github.io/dt-profidreieck-web/DT-ProfiDreieck_Test_1-1-0.html)**

Läuft direkt im Browser, ohne Anmeldung und ohne Installation.
Der Funktionsumfang der Testversion ist eingeschränkt.

## Vollversion

Die Vollversion kostet **69 € einmalig**. Kein Abonnement, keine laufenden
Kosten. Sie besteht aus einer einzelnen HTML-Datei, die offline läuft.

**[Zur Produktseite: dt-profidreieck.de](https://dt-profidreieck.de/)**

Dort finden sich auch die drei weiteren Programme: DT-ProfiSchraube
(Schraubenverbindungen nach VDI 2230), DT-ProfiPassung (Passungen nach ISO 286)
und DT-ProfiSchweissnaht (Schweißnähte nach EN 1993-1-8).

## Was das Programm rechnet

Drei bekannte Größen genügen – aus Seiten, Winkeln, Umkreisradius,
Inkreisradius, Fläche oder den Höhen. Alle übrigen Werte werden ermittelt und
das Dreieck wird gezeichnet.

- Klassische Fälle SSS, SWS, WSW, SWW und SSW, letzterer mit automatischer
  Erkennung von null, einer oder zwei Lösungen
- Rechnung auch aus Umkreisradius, Inkreisradius, Flächeninhalt und Höhen
- Prüfung der Eingaben auf Widersprüche, unter anderem gegen die Euler-Ungleichung

## Geometrie zum Einblenden

Zusätzlich lassen sich einblenden und antippen, jeweils mit Koordinatenanzeige:

- Höhenschnittpunkt
- Mittelsenkrechte und Umkreismittelpunkt
- Winkelhalbierende und Inkreismittelpunkt
- Euler-Gerade durch Schwerpunkt, Umkreismittelpunkt und Höhenschnittpunkt
- Feuerbachkreis (Neunpunktekreis)
- Die drei Ankreise

## Ausgabe

- **DXF:** echtes CAD-Format in realen Einheiten, getrennt nach Ebenen für
  Dreieck, Kreise, Hilfslinien und Beschriftung
- **SVG:** verlustfrei skalierbar, für Dokumente und Arbeitsblätter
- **PNG und PDF** für die Dokumentation

## Technisches

Eine einzelne HTML-Datei. Keine Installation, kein Konto, keine
Administratorrechte. Alle Berechnungen laufen im Browser auf dem eigenen Gerät;
es werden keine Daten an Server übertragen. Läuft dadurch auch ohne
Internetverbindung.

---

*Die Ergebnisse sind ohne Gewähr. Die fachliche Verantwortung für die
Verwendung der Werte bleibt beim Anwender.*
