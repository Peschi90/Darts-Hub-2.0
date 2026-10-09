# AwtrixNG – Funktionsübersicht

## Geräte und Ausgabe

- AwtrixNG-Firmware mit HTTP-API v1; Modul und bis zu 32 Displays aktivieren.
- Gerätename, Adresse und optional HTTP-Benutzer/Passwort einstellen. Leeres Passwort behält das gespeicherte; ausdrücklich entfernen ist möglich.
- Gerät prüfen und Informationen zu Gerät, Firmware, Fähigkeiten, Einstellungen und Apps laden.
- Timeout, Vorlagenordner, Standarddauer, Einschalten beim Start und optionale High-Finish-Schwelle einstellen.
- Gebündelte Vorlagen und eigene Vorlagen verwenden/neu laden.
- Status, letzte Übertragung, Warteschlange und Vorlagenfehler anzeigen.

## Regeln und Sequenzen

- Dieselben [20 Auslöser wie PixelIt](EREIGNISSE.md), einschließlich Match-Verlassen.
- Spielername, exakter Score/Bereich, Feld/Ring, Multiplikator und Kombination festlegen.
- Namensregel vor allgemeiner Regel desselben Typs pro Display; Groß-/Kleinschreibung und äußere Leerzeichen irrelevant.
- Exakter Score vor Scorebereich; erste passende Bereichsregel nach Namensvorrang. High Finish kann Gewinnanzeige ersetzen, wenn die Schwelle erreicht ist.
- Mehrere Schritte mit Vorlage, Zielgeräten, Text, Icon, Farbe, Dauer, Helligkeit, Scrollgeschwindigkeit, Textschreibweise und Sound.
- Ausgabe als Benachrichtigung, App oder automatisch; App-Name und zusätzliche JSON-Eigenschaften festlegen.
- Automatischer Modus mit Dauer **0** verwendet eine App; Displayrotation kann sie später ausblenden. Schritte mit positiver Dauer laufen zeitlich nacheinander.
- Dieselben Textvariablen wie PixelIt, einschließlich fester Spielerwerte p1–p32.
- Entwürfe auf echten Geräten testen; speichern und live anwenden. Idle bei Matchstart und Exit-Effekte beim Verlassen ausführen.

## Display-Einstellungen

Nur ausdrücklich aktivierte Werte werden gesetzt:

| Bereich | Einstellbarer Umfang |
| --- | --- |
| Anzeige | Automatische/manuelle Helligkeit, Sättigung, Gamma, Farbkorrektur, Farbton |
| Text | Textfarbe, Großschreibung, Scrollmodus/-richtung, Einlauf, Verhalten bei passendem Text, Geschwindigkeit, Abstand, Haltezeit |
| Rotation | Automatische Übergänge, Appdauer, Übergangseffekt/-richtung/-dauer, Navigationssperre |
| Uhr | Modus, Farbe, 24-Stunden-Format, führende Null, Sekunden, AM/PM, Trennzeichenverhalten |
| Kalender | Kopf-/Text-/Flächenfarben, Datumsreihenfolge, Trenner, Jahresanzeige, Wochentag, Monatsnamen, Datumsfarbe |
| Wochentagsleiste | Sichtbarkeit, Wochenbeginn, Wochenendtage, aktive/inaktive Farben einschließlich Wochenende |
| Sensoren | Celsius/Fahrenheit, Temperatur-/Feuchte-/Batteriefarbe |
| Ton | Aktivieren, Buzzer-/DFPlayer-/MP3-/Radio-Lautstärke, Radio-Metadaten |

## Gerätesteuerung

Der Operationskatalog umfasst folgende Aktionen. Ob eine Aktion funktioniert, hängt von der Firmware und den tatsächlichen Gerätefähigkeiten ab:

- Gerät, Version, Fähigkeiten, Einstellungen, Anzeige und Bildschirm lesen.
- Anzeige/Displaypower ändern; Moodlight und benannte Indikatoren setzen/entfernen.
- Apps auflisten/aktivieren; nächste/vorherige App; Reihenfolge und deaktivierte Apps setzen; App pushen/entfernen.
- App-Skript lesen/schreiben; gemeinsame Skripte auflisten.
- Benachrichtigung senden; aktive oder benannte Benachrichtigung entfernen.
- Audiozustand, Melodien und MP3 lesen; Sound/RTTTL spielen, Ton stoppen, Melodien speichern/löschen, MP3 hochladen/löschen, Radiostationen setzen.
- Systemdaten lesen/ändern, WLAN scannen, Logs lesen, Neustart und Schlaf.
- Dateien auflisten/hochladen/löschen; Icon-Ursprünge lesen/setzen/löschen.
- Einstellungen zurücksetzen, Geräte-Werksreset, Firmware hochladen und Sicherung wiederherstellen; die entsprechenden destruktiven Aktionen erfordern Bestätigung.

Die Firmware übernimmt Darstellung und Ton; diese Liste garantiert keine Fähigkeit eines beliebigen Awtrix-kompatiblen Displays.

Weiterlesen: [Einrichtung](../AWTRIX.md).

## Bedienung und Diagnose

GUI: Erweiterungsseite öffnen, Entwurf testen und speichern. TUI: `DartsHub --tui`, entsprechende Seite, **Enter** zum Bearbeiten und **Entwurf speichern**. Headless nutzt dieselbe Konfiguration. Vorschautests speichern nichts. Statuswerte und Fehler stehen auf Modulseite, Dashboard und Konsole.

[Gemeinsame Funktionen](GEMEINSAM.md) · [Zur Übersicht](README.md)
