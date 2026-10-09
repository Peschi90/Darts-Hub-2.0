# Ereignisse und Textvariablen

## Vollständige Ereignistabelle

Alle aktuell auswählbaren Regeltypen. Ein Haken bedeutet: Das Modul bietet den Typ an. Caller nutzt eigene Ansageoptionen statt dieser Regelkarten. Die Bezeichner in Klammern sind die stabilen Konfigurationsnamen.

| Ereignis | Bedeutung | WLED | PixelIt | AwtrixNG | GIF |
| --- | --- | --- | --- | --- | --- |
| Idle / Spielerfarbe (`Idle`) | Ruhezustand/Grundanzeige im Spielablauf. | ✓ | ✓ | ✓ | — |
| Match gestartet (`MatchStarted`) | Neues Match startet. | ✓ | ✓ | ✓ | — |
| Neues Leg / Set (`LegStarted`) | Neues Leg startet (WLED). | ✓ | — | — | — |
| Genauer Aufnahmescore (`Score`) | Abgeschlossene Aufnahme mit exakter Punktzahl. | ✓ | ✓ | ✓ | ✓ |
| Aufnahme im Scorebereich (`ScoreRange`) | Abgeschlossene Aufnahme innerhalb eines Punktebereichs. | ✓ | ✓ | ✓ | ✓ |
| Einzelwurf im Scorebereich (`DartScore`) | Einzel-Dartscore im eingestellten Bereich. | ✓ | — | — | — |
| Einzelwurf auf Feld (`DartField`) | Treffer auf gewähltem Feld und optionalem Ring. | ✓ | ✓ | ✓ | ✓ |
| Single / Double / Triple (`Multiplier`) | Treffer mit dem gewählten Multiplikator unabhängig vom Feld. | ✓ | ✓ | ✓ | ✓ |
| Drei-Dart-Kombination (`Combo`) | Drei-Dart-Kombination, Reihenfolge unerheblich, kein Bust. | ✓ | ✓ | ✓ | ✓ |
| Bust / Überworfen (`Bust`) | Aufnahme ist überworfen. | ✓ | ✓ | ✓ | ✓ |
| Leg gewonnen (`GameWon`) | Spiel/Leg gewonnen. | ✓ | ✓ | ✓ | ✓ |
| Match gewonnen (`MatchWon`) | Match gewonnen; Ergebnis kann noch geöffnet sein. | ✓ | ✓ | ✓ | ✓ |
| Match beendet und verlassen (`MatchExited`) | Match beendet und tatsächlich verlassen/entfernt, auch bei Abbruch. | ✓ | ✓ | ✓ | — |
| Highfinish (`HighFinish`) | Gewinn mit Abschluss-Score ab konfigurierter Schwelle. | ✓ | ✓ | ✓ | ✓ |
| Spieler beigetreten (`PlayerJoined`) | Spieler tritt der Lobby bei. | ✓ | ✓ | ✓ | — |
| Spieler verlassen (`PlayerLeft`) | Spieler verlässt die Lobby. | ✓ | ✓ | ✓ | — |
| Darts werden gezogen (`Takeout`) | Beginn des Herausnehmens der Darts. | ✓ | ✓ | ✓ | — |
| Kalibrierung gestartet (`Calibration`) | Board-Kalibrierungsereignis. | ✓ | — | — | — |
| Board-Erkennung gestoppt (`BoardStopped`) | Board-Erkennung wurde gestoppt. | ✓ | — | — | — |
| Ruhemodus (`Sleep`) | WLED-Inaktivitätsschwelle erreicht. | ✓ | — | — | — |
| Autodarts getrennt (`Disconnected`) | Autodarts-Verbindung getrennt. | ✓ | — | — | — |
| Anwendungsstart (`AppStart`) | Modul-Anwendungsstartaktion. | — | ✓ | ✓ | — |
| Leg gestartet (`GameStarted`) | Neues Spiel/Leg startet (Displays). | — | ✓ | ✓ | — |
| Nach jedem Wurf (`Throw`) | Neuer Wurf; auch für Live-Anzeigen. | — | ✓ | ✓ | — |
| Spielerwechsel (`PlayerChanged`) | Aktiver Spieler wechselt. | — | ✓ | ✓ | — |
| Wurf oder Turnwechsel (`ThrowOrTurnChanged`) | Eine Regel reagiert auf neuen Wurf und neue Aufnahme, auch beim selben Spieler. | — | ✓ | ✓ | — |

## Bedingungen und Zeitpunkt

- Score/Scorebereich betreffen eine Aufnahme; DartScore betrifft einen einzelnen Dart.
- Feld/Ring etwa Triple 20; Multiplikator Single/Double/Triple feldunabhängig. Kombinationen z. B. `t20,t20,t20` oder `s20,d20,t20`.
- Gewinn ist von Match-Verlassen getrennt; Netzwerkunterbrechung allein ist kein Exit.
- Globale Ereignisse ohne Spieler sollten keinen Spielernamenfilter erhalten. WLED blendet ihn bei globalen Board-/Schlaf-/Exit-Ereignissen aus.
- WLED hat eigene Auswahlprioritäten und Lizenzanforderungen. Ein Haken umgeht keine Lizenz.
- Namensvorrang und Sortierung: [gemeinsame Funktionen](GEMEINSAM.md). GIF hat keinen zusätzlichen Namensvorrang.

## Textvariablen für PixelIt und AwtrixNG

In Schritttexte einsetzen. Ereignisse ohne Spieler oder Dart können leere Werte liefern.

| Variable | Bedeutung |
| --- | --- |
| `{playername}` | Spielername des Ereignisses |
| `{player-number}` | Spielernummer |
| `{score}` | Ereignisscore |
| `{dart-score}` | Letzter Dartscore |
| `{dart-number}` | Dartnummer in der Aufnahme |
| `{darts-thrown}` | Geworfene Darts im aktuellen Leg |
| `{turn-score}` | Aktueller Aufnahme-Score |
| `{points-left}` | Restpunkte |
| `{game-mode}` | Spielmodus |
| `{game-mode-extra}` | Zusatzangabe zum Modus |

Feste Spielerpositionen **p1 bis p32** unterstützen jeweils `{pN-playername}`, `{pN-points-left}`, `{pN-darts-thrown}`, `{pN-dart-number}`, `{pN-dart-score}` und `{pN-turn-score}`. N durch die Nummer ersetzen, z. B. `{p2-points-left}`.

Beispiele: `{playername} {points-left} D{dart-number}` für aktiven Spieler; `{p1-playername} {p1-points-left}` für eine feste Spielermatrix.

[Zur Übersicht](README.md)

Der frühere gespeicherte Typ `ThrowOrPlayerChanged` wird beim Laden/Import auf `ThrowOrTurnChanged` umgestellt. Der separate Spielerwechsel vergleicht die Spieleridentität; der kombinierte Typ berücksichtigt zusätzlich die Aufnahme-ID und Leg-/Set-Wechsel.
