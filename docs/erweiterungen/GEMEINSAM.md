# Gemeinsame Funktionen und Bedienung

## Aktivieren, Speichern und Testen

- Caller, WLED, PixelIt, AwtrixNG und GIF unabhängig ein-/ausschalten; gespeicherte Regeln bleiben erhalten.
- Spielereignisse kommen zentral aus Autodarts. WLED, PixelIt, AwtrixNG und GIF benötigen keinen eingeschalteten Caller.
- GUI: jeweilige Erweiterungsseite öffnen, Werte ändern und speichern. TUI: `DartsHub --tui`, entsprechende Seite öffnen, mit **Enter** bearbeiten und **Entwurf speichern** verwenden.
- Gespeicherte Einstellungen werden im Betrieb angewendet; Headless nutzt dieselbe Konfiguration.
- Ungespeicherte Änderungen werden sichtbar gemeldet. Beim Seitenwechsel können Änderungen mit alten/neuen Werten übernommen oder verworfen werden.
- Vorschautests steuern echte Geräte bzw. spielen echte Medien ab. Sie speichern den Entwurf nicht.

## Ereignisregeln

- Benannte Regeln anlegen, aktivieren/deaktivieren, löschen und sortieren; GUI-Karten per Drag-and-drop, TUI über die angebotenen Sortieraktionen.
- Je nach Regeltyp Score, Bereich, Feld/Ring, Multiplikator oder Kombination einschränken; optional Spielername.
- Leerer Spielername bedeutet allgemeine Regel. Groß-/Kleinschreibung und äußere Leerzeichen sind beim Namensvergleich unerheblich.
- **WLED, PixelIt und AwtrixNG:** Passende aktive Namensregeln unterdrücken allgemeine Regeln desselben Regeltyps pro Zielgerät. Ereignisbedingungen und Gerätezuordnung müssen ebenfalls passen. GIF bietet diesen zusätzlichen Namensvorrang nicht.
- WLED-Ziele gelten pro Regel, PixelIt-/Awtrix-Ziele pro Schritt; alle oder ausgewählte Geräte.
- Gelöschte Zielgeräte müssen ersetzt werden; Regeln mit verlorener Zuordnung werden in der Oberfläche deaktiviert.
- Kartenreihenfolge garantiert nicht, dass alle passenden Regeln laufen. Die Module haben zusätzlich Auswahlprioritäten für Scores, Bereiche und Gewinne.

## Import und Werkseinstellungen

- Alte `apps-downloadable.json`, `apps-local.json` und `apps-open.json` auswählen.
- Analyse im eigenen Dialog mit Animation/Fortschritt und Wartehinweis; gesetzte Werte mit Original, Ziel und Prüfergebnis ansehen.
- Werte korrigieren oder einzeln ausschließen; ausgeschlossene Karten sind diagonal rot markiert.
- Nach Korrekturen werden geänderte Werte und notwendige Abhängigkeiten neu geprüft; unveränderte Ergebnisse werden wiederverwendet.
- Unterstützte Moduleinstellungen, Geräte, Ereignisse, Programme und Webseiten übernehmen; nicht unterstützte oder verlustbehaftete Angaben melden.
- Zugangsdaten bleiben ausgeschlossen; importierte Programme/Webseiten starten manuell. Der Import öffnet keine Webseite.
- Übernommene Einstellungen speichern und direkt anwenden.
- Gesamte Anwendung oder einzelne Module nach Bestätigung auf Werkseinstellungen zurücksetzen.

## Status und Diagnose

Dashboard, Erweiterungsseiten und Konsole zeigen reale Verbindungen, letzte Ereignisse/Aktionen und Fehler. Die Konsole kann filtern und vollständige Details mehrerer markierter Einträge kopieren. Lizenz- und Geräteanmeldung gelten auch im Terminal.

Weiterlesen: [Import](../LEGACY_IMPORT.md), [Reset](../FACTORY_RESET.md), [Änderungshinweise](../UNSAVED_SETTINGS.md), [Reihenfolge](../EVENT_RULE_ORDER.md), [Namensregeln](../PLAYER_EVENT_RULES.md), [TUI](../TUI.md).
