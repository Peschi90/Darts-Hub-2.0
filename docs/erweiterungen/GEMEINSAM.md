# Gemeinsame Funktionen und Bedienung

## Aktivieren, Speichern und Testen

- Caller, WLED, PixelIt, AwtrixNG und GIF unabhängig ein-/ausschalten; gespeicherte Regeln bleiben erhalten.
- Spielereignisse kommen zentral aus Autodarts. WLED, PixelIt, AwtrixNG und GIF benötigen keinen eingeschalteten Caller.
- GUI: jeweilige Erweiterungsseite öffnen, Werte ändern und speichern. TUI: `DartsHub --tui`, entsprechende Seite öffnen, mit **Enter** bearbeiten und **Entwurf speichern** verwenden.
- Gespeicherte Einstellungen werden im Betrieb angewendet; Headless nutzt dieselbe Konfiguration.
- Ungespeicherte Änderungen werden sichtbar gemeldet. Beim Seitenwechsel können Änderungen mit alten/neuen Werten übernommen oder verworfen werden.
- Vorschautests steuern echte Geräte bzw. spielen echte Medien ab. Sie speichern den Entwurf nicht.

## Ereignisregeln

- Spieler 1–6 behalten ab dem Ausbullen beziehungsweise Matchstart ihre Zuordnung bis zum Matchende. Ein Leg-/Setwechsel oder eine geänderte Wurfreihenfolge verschiebt weder WLED-Spielerregeln noch die nummerierten Spieler-Platzhalter der Anzeigen. Das gilt gleichermaßen in GUI, TUI und Weboberfläche.
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

Weiterlesen: [Import](../LEGACY_IMPORT.md), [Reset](../FACTORY_RESET.md), [Reihenfolge](../EVENT_RULE_ORDER.md), [TUI](../TUI.md).

## Fixed player assignments (English)

Player slots 1–6 remain assigned from bull-off or match start until the match ends. Leg/set changes and reordered throwing positions do not shift WLED player rules or numbered display placeholders. GUI, TUI and web use the same assignment. A new match establishes a new roster.


## Kostenlose Lizenz / Free license

Beim Auswählen einer geschützten WLED-Regel bietet ein Dialog den Zugang zur kostenlosen Wissensprüfung an. Unter **Einstellungen → Lizenz** findest du die hervorgehobene Lizenzkarte und kannst einen vorhandenen Schlüssel prüfen. Die Regel bleibt gespeichert; ohne passende Freigabe wird sie nicht ausgeführt. Im Terminal findest du **Einstellungen → Kostenlose Lizenz sichern**; bei gesperrten Einstellungen erscheint ebenfalls eine Auswahl mit Browseraufruf beziehungsweise der Adresse für ein anderes Gerät.

Selecting a protected WLED rule offers a dialog linking to the free knowledge check. **Settings → License** includes a prominent license card and validation for existing keys. The rule remains saved but does not run without the appropriate access. In the terminal use **Settings → Get a free license**; locked settings also offer browser access or the URL for another device.

## DMU: Treffer und Fehlwürfe / Hits and misses

In WLED, PixelIt, AWTRIX und GIF sind nur Feld 1–20, Bull (25) und MISS (0) auswählbar. Feldregeln unterstützen S/D/T und M1–M20. M bezeichnet Fehlwürfe außerhalb eines Zahlenfelds; MISS einen Fehlwurf ohne Zahlenfeld. Der allgemeine DMU-Trigger bietet S, D, T, M und MISS. Bull erlaubt nur S25/D25. WLED benötigt weiterhin die Freischaltung `im_able_to_read`.

All four modules offer fields 1–20, Bull (25) and MISS (0). Field rules support S/D/T and M1–M20. M means a miss outside a numbered field; MISS means no numbered field. The general DMU trigger supports S, D, T, M and MISS. Bull supports S25/D25. WLED still requires `im_able_to_read`.

TUI: WLED bietet Auswahllisten. Bei PixelIt/AWTRIX/GIF können Bedingungen als `M20`, `T20`, `M` oder `MISS` eingegeben werden; alternativ bleibt `Feld|Trefferart` möglich. Gespeicherte Trefferarten: 0 = offen (Feldregel), 1 = S, 2 = D, 3 = T, 4 = M, 5 = MISS.

TUI: WLED provides selection lists. PixelIt/AWTRIX/GIF accept `M20`, `T20`, `M` or `MISS`; `field|hit type` remains supported. Stored hit types: 0 = any (field rule), 1 = S, 2 = D, 3 = T, 4 = M, 5 = MISS.

Beispielansichten / Example screenshots: [WLED DE](../images/user-guide/de/wled-dmu.png), [WLED EN](../images/user-guide/en/wled-dmu.png), [PixelIt DE](../images/user-guide/de/pixelit-dmu.png), [PixelIt EN](../images/user-guide/en/pixelit-dmu.png), [AWTRIX DE](../images/user-guide/de/awtrix-dmu.png), [AWTRIX EN](../images/user-guide/en/awtrix-dmu.png).
