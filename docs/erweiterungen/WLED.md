# WLED – Funktionsübersicht

## Geräte und Effektgestaltung

- Modul und einzelne Controller aktivieren; bis zu 32 Controller mit Namen, Adresse und optional eigener Helligkeit.
- Verbindung prüfen und echten Effekt-/Paletten-/Preset-Katalog manuell neu laden; Firmware, LED-Anzahl, Status und letzte Aktion sehen.
- Globale Helligkeit, Timeout, Standarddauer sowie Debug-/Protokollausgaben einstellen.
- Effekt oder Controller-Preset auswählen; mehrere Effektalternativen je Regel hinterlegen.
- Haupt-/Zweit-/Drittfarbe, Palette, Geschwindigkeit, Intensität und individuelle Dauer setzen; Palettenvorschau nutzen, soweit der Controller sie liefert.
- Preset-ID bleibt controllergebunden; ein Preset muss auf dem angesprochenen Controller vorhanden sein.
- Legacy-Palette auch ohne `p` importieren, z. B. `74|9`.

## Ereignisse und Automatik

- [Alle 21 WLED-Regeltypen](EREIGNISSE.md): Aufnahme, Einzel-Dart, Feld/Ring, Multiplikator, Kombination, Gewinne, Spieler- und Boardereignisse.
- Zielgeräte, Spielername und bei geeigneten Ereignissen Spielerposition eingrenzen; Namen unabhängig von Schreibweise.
- Namensregel übersteuert allgemeinen gleichen Regeltyp pro Zielgerät.
- Bei gleichzeitig passenden Ereignissen: High Finish vor Matchgewinn, Spielgewinn, Bust, Kombination, exaktem Score, Scorebereich, Feld, Multiplikator und übrigen Ereignissen. Danach zählt Regelspezifität; pro Gerät wird ein Effekt gewählt.
- Idle bei Match-/Legstart und im Spielablauf; Rückkehr nach begrenzten Effekten/Takeout. Dauer **0** bei Spielregeln bedeutet bis zum Takeout.
- Ausschalten bei Anwendungsstart bzw. nach Spielende; Schlaf-Effekt nach Inaktivität und optional späteres Ausschalten.
- **Match beendet und verlassen:** regulären Abschluss und Abbruch erfassen. Passende Exit-Regel übersteuert das automatische Ausschalten pro Zielgerät.
- Board vor Effekten kurz pausieren oder nach Gewinn stoppen; Board-Manager-Adresse einstellen bzw. aus Autodarts beziehen. Kein Caller nötig.

## Robbel3D One-Click

Gebündelten 145-LED-Ring und sechs Presets einrichten: Controller suchen, Adresse/GPIO, Board-ID und Medienordner wählen, Änderungen prüfen/bestätigen, Controller sichern, LED-Konfiguration/Presets übertragen, Ergebnis prüfen und Caller/WLED sofort anwenden. Sicherung als ZIP herunterladen. WLAN/Gerätekennung bleiben erhalten; weitere LED-Ausgänge werden deaktiviert und Presets ersetzt. GUI und TUI bieten denselben Ablauf.

## Grenzen

DartScore, Feld, Multiplikator, Kombination, Schlaf, namensgebundenes Idle und Schlafparameter können die WLED-Lizenz benötigen. Ein gespeicherter gesperrter Wert umgeht sie nicht. Kataloge werden beim Start oder manuell geladen. Ein Vorschautest stellt den vorherigen Controllerzustand nicht automatisch wieder her. WLED-UDP-Synchronisation kann unabhängig angesprochene Controller gegenseitig überschreiben.

Weiterlesen: [Einrichtung](../WLED_CONFIGURATION_AND_AUTODARTS.md), [Robbel3D](../ROBBEL3D.md), [Exit-Regel](../MATCH_EXIT_TRIGGER.md).

## Bedienung und Diagnose

GUI: Erweiterungsseite öffnen, Entwurf testen und speichern. TUI: `DartsHub --tui`, entsprechende Seite, **Enter** zum Bearbeiten und **Entwurf speichern**. Headless nutzt dieselbe Konfiguration. Vorschautests speichern nichts. Reale Statuswerte und Fehler stehen im Dashboard, auf der Modulseite und in der Konsole.

[Gemeinsame Funktionen](GEMEINSAM.md) · [Zur Übersicht](README.md)
