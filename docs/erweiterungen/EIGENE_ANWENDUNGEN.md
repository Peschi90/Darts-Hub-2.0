# Eigene Anwendungen und Webseiten – Funktionsübersicht

## Programme und Skripte

- Mehrere benannte Einträge hinzufügen, aktivieren/deaktivieren, bearbeiten und entfernen.
- Programm/Skript auswählen; Ausführungsart automatisch erkennen oder Executable, PowerShell, Batch, Python bzw. Shell wählen.
- Optional Interpreter, Startparameter und Arbeitsordner; ohne Arbeitsordner gilt Programmordner bzw. bei PATH-Befehlen DartsHub-Ordner.
- Argumente mit Anführungszeichen oder JSON-Liste, z. B. `["hello world", "--option"]`.
- Automatisch bei DartsHub starten oder manuell im Dashboard starten, beenden und neu starten.
- Absturz-Neustart mit maximaler Anzahl (0 = unbegrenzt) und Wartezeit.
- Wartezeit für normales Beenden; danach zwangsweise beenden, einschließlich zugehöriger Kindprozesse.
- stdout/stderr in Konsole/Logs erfassen; Prozessstatus, PID, Exitcode, Fehler und Neustartzähler auswerten.
- Änderungen speichern/anwenden: unveränderte Programme laufen weiter; geänderte laufende Einträge stoppen und bei aktivem Autostart neu starten.
- Programme laufen mit Hostbenutzerrechten. Interpreter müssen installiert sein; Batch ist Windows-spezifisch.

## Webseiten

- Name, vollständige HTTP-/HTTPS-Adresse und installierten Browser wählen.
- Systemstandardbrowser oder konkreten Browser; Parameter benötigen einen konkreten Browser.
- Manuell öffnen oder per Autostart an Browser übergeben.
- Kein Arbeitsordner, keine Ausführungsart und keine Betriebssystemwahl erforderlich.
- Browserliste stammt vom Host, auch bei Fernverbindung. Status „An Browser übergeben“ bestätigt die Übergabe, nicht das Laden.
- Browserfenster bleiben unter Nutzerkontrolle und werden beim DartsHub-Beenden nicht geschlossen. Keine Webseiten-Prozessüberwachung/Absturz-Neustarts.

## Lebenszyklus und Import

- GUI schließen beendet gestartete eigene Programme samt Kindprozessen auch bei weiterlaufendem Headless-Host.
- TUI schließen lässt Programme laufen, solange Host weiterläuft; Host beenden stoppt sie.
- Alte OS-Filter bleiben gespeichert, verhindern aber keinen Start; Hostinstallation bestimmt das Betriebssystem.
- Programme und alte `custom-url-*`-Webseiten importieren; Einträge bleiben nach Import auf manuellem Start.
- TUI: **Eigene Anwendungen**, Eintrag bearbeiten/Webseite hinzufügen, speichern; Dashboardaktionen starten, stoppen bzw. öffnen.

Weiterlesen: [Programme](../OWN_APPLICATIONS.md), [Webseiten](../EXTERNAL_WEBSITES.md), [Gemeinsame Funktionen](GEMEINSAM.md).
