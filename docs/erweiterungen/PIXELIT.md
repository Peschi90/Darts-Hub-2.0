# PixelIt – Funktionsübersicht

## Geräte und Grundeinstellungen

- Modul und bis zu 32 Displays aktivieren; Name, HTTP-/HTTPS-Adresse und optionaler Port.
- Verbindung prüfen bzw. sichtbares Testbild senden, auch vor dem Speichern.
- Helligkeit 1–255, Timeout 1–30 Sekunden, Vorlagenordner und optionale High-Finish-Schwelle 1–170.
- Status, Fehler, letzte Übertragung, Warteschlange, empfangene Ereignisse und Vorlagenfehler anzeigen.

## Regeln und Sequenzen

- [Alle 20 Auslöser](EREIGNISSE.md), einschließlich Wurf, Spielerwechsel, kombiniertem Live-Trigger und Match-Verlassen.
- Spielername, exakter Score/Bereich, Dartfeld/Ring, Multiplikator und Drei-Dart-Kombination einschränken.
- Passende Namensregeln vor allgemeinen Regeln desselben Typs pro Display; Namen unabhängig von Groß-/Kleinschreibung.
- Exakter Score vor Scorebereich; im Bereich die erste passende Regel nach Namensvorrang verwenden.
- Bis zu 64 Schritte pro Regel; Vorlage, Ersatztext, Helligkeit, Pause danach und Zielgeräte pro Schritt.
- Schritte sortieren; alle/ausgewählte Geräte; maximal 60 Sekunden Pausen in einer Sequenz.
- Gebündelte und eigene Vorlagen verwenden/neu laden; Text-/Matrixvorschau sowie Test der Sequenz auf echten Geräten.
- Idle bei Match-/Spielstart und nach passendem Spielerwechsel einer Bot-Aufnahme wiederherstellen.
- Kombinationen reihenfolgeunabhängig einmal pro Aufnahme; kein Bust oder Nachspielen historischer Aufnahmen beim Verbinden.

## Live-Text

Spielername/-nummer, Restpunkte, letzter Dartscore, Dartnummer, Dartanzahl, Aufnahme-Score und Spielmodus einsetzen. Feste Werte für Spieler 1–32 ermöglichen eine Matrix je Spieler. **Wurf oder Turnwechsel** aktualisiert beides mit einer Regel. Beispiel: `{playername} {points-left} D{dart-number}`. Alle Platzhalter: [Ereignisse und Variablen](EREIGNISSE.md).

Weiterlesen: [Einrichtung](../PIXELIT.md), [Feld-/Kombinationseffekte](../DISPLAY_DART_EFFECTS.md).

## Bedienung und Diagnose

GUI: Erweiterungsseite öffnen, Entwurf testen und speichern. TUI: `DartsHub --tui`, entsprechende Seite, **Enter** zum Bearbeiten und **Entwurf speichern**. Headless nutzt dieselbe Konfiguration. Vorschautests speichern nichts. Reale Statuswerte und Fehler stehen im Dashboard, auf der Modulseite und in der Konsole.

[Gemeinsame Funktionen](GEMEINSAM.md) · [Zur Übersicht](README.md)
