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
| Einzelwurf auf Feld (`DartField`) | Treffer auf gewähltem Feld und optionalem Ring. | ✓ | ✓ | ✓ | ✓ |
| Single / Double / Triple (`Multiplier`) | Treffer mit dem gewählten Multiplikator unabhängig vom Feld. | ✓ | ✓ | ✓ | ✓ |
| Drei-Dart-Kombination (`Combo`) | Drei-Dart-Kombination, Reihenfolge unerheblich, kein Bust. | ✓ | ✓ | ✓ | ✓ |
| Cricket/Tactics-Mark (`CricketMark`) | Gewertete Marks ohne Abschluss oder Punkte. | ✓ | ✓ | ✓ | ✓ |
| Cricket/Tactics-Feld abgeschlossen (`CricketClosed`) | Dritte Mark erreicht, ohne Punkte. | ✓ | ✓ | ✓ | ✓ |
| Cricket/Tactics-Punkte (`CricketScored`) | Punkte erzielt; bei Cut Throat für offene Gegner. | ✓ | ✓ | ✓ | ✓ |
| Cricket/Tactics: nicht gewertet (`CricketNoMark`) | Kein Zielfeld oder bereits für alle geschlossen. | ✓ | ✓ | ✓ | ✓ |
| Erste Cricket/Tactics-Mark (`CricketOpened`) | Erste Mark auf einem zuvor unberührten Feld. | ✓ | ✓ | ✓ | ✓ |
| Cricket/Tactics-Feld für alle geschlossen (`CricketClosedAll`) | Letzter Spieler schließt das Feld. | ✓ | ✓ | ✓ | ✓ |
| Cricket/Tactics: verborgenes Feld entdeckt (`CricketRevealed`) | Zielfeld erstmals von Autodarts aufgedeckt. | ✓ | ✓ | ✓ | ✓ |
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

## Regeln in der Android-App

Jede Regel lässt sich durch Tippen auf ihre Kopfzeile einzeln öffnen und schließen. Name, Auslöser und Aktivstatus bleiben sichtbar; getrennte Karten erleichtern die Übersicht. Neue Regeln öffnen sich direkt. Beim Zuklappen gehen Entwürfe nicht verloren. Zum Sortieren den Griff halten oder die Pfeile verwenden; der offene Zustand bleibt bei der Regel.

GUI: Ereigniskarte öffnen und speichern. TUI: `DartsHub --tui`, Modul auswählen, **Ereignisse**, Regel und Auslöser bearbeiten, dann **Entwurf speichern**. Der exakte Score benötigt eine Punktzahl, der Scorebereich zwei Grenzen.

## Bedingungen und Zeitpunkt

- Score/Scorebereich betreffen eine Aufnahme. Beim exakten Score wird nur die **Punktzahl** eingegeben, beim Bereich Minimum und Maximum. Einzelwurf-Effekte werden über **DMU** mit Feld und Ring oder Multiplikator konfiguriert.
- Einzelwurf-Punkte (`DartScore`) stehen nicht mehr zur Neuauswahl. Auch für animierte Matrix-Scores **DMU** mit Feld/Ring oder Multiplikator verwenden. Bereits gespeicherte und aus V1 importierte Altregeln behalten ihre Werte und Lizenzanforderungen.
- Feld/Ring etwa Triple 20; Multiplikator Single/Double/Triple feldunabhängig. Kombinationen z. B. `t20,t20,t20` oder `s20,d20,t20`.
- Gewinn ist von Match-Verlassen getrennt; Netzwerkunterbrechung allein ist kein Exit.
- Globale Ereignisse ohne Spieler sollten keinen Spielernamenfilter erhalten. WLED blendet ihn bei globalen Board-/Schlaf-/Exit-Ereignissen aus.
- WLED hat eigene Auswahlprioritäten und Lizenzanforderungen. Ein Haken umgeht keine Lizenz.
- Namensvorrang und Sortierung: [gemeinsame Funktionen](GEMEINSAM.md). GIF hat keinen zusätzlichen Namensvorrang.

Use **DMU** with a field/ring or multiplier for single-dart effects, including animated matrix scores. `DartScore` is no longer offered for new rules. Saved and v1-imported legacy rules retain their values and license requirements.

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

Feste Spielerpositionen **p1 bis p6** unterstützen jeweils `{pN-playername}`, `{pN-points-left}`, `{pN-darts-thrown}`, `{pN-dart-number}`, `{pN-dart-score}` und `{pN-turn-score}`. N durch die Nummer ersetzen, z. B. `{p2-points-left}`.

Beispiele: `{playername} {points-left} D{dart-number}` für aktiven Spieler; `{p1-playername} {p1-points-left}` für eine feste Spielermatrix.

[Zur Übersicht](README.md)

Der frühere gespeicherte Typ `ThrowOrPlayerChanged` wird beim Laden/Import auf `ThrowOrTurnChanged` umgestellt. Der separate Spielerwechsel vergleicht die Spieleridentität; der kombinierte Typ berücksichtigt zusätzlich die Aufnahme-ID und Leg-/Set-Wechsel.

## Cricket, Tactics und Hidden Cricket

Die vier Trefferergebnisse Mark, Abschluss, Punkte und nicht gewertet sind pro Dart gegenseitig ausschließend. Punkte haben Vorrang vor einem gleichzeitigen Abschluss. Erste Mark, Abschluss für alle und Entdecken sind zusätzliche Zustandsübergänge. Standard, Cut Throat und No Score werden aus dem Autodarts-Scoring-Modus erkannt; No Score erzeugt keine Punkteereignisse. Noch verborgene Hidden-Cricket/Tactics-Felder werden nicht vorab verwendet. Korrekturen werden neu ausgewertet, unveränderte Nachrichten nicht wiederholt.

Neue PixelIt-/Awtrix-Textvariablen: `{cricket-scoring-mode}`, `{cricket-field}`, `{cricket-marks}`, `{cricket-turn-marks}`. Bei einem Cricket/Tactics-Trefferereignis ist `{score}` dessen erspielte Punktzahl, `{dart-score}` sein physischer Wert. `{game-mode-extra}` enthält Cricket, Tactics oder Hidden Cricket.

GUI und TUI: jeweiliges Modul → Regeln → Regel hinzufügen/bearbeiten → Cricket/Tactics-Auslöser wählen → Effekte/Schritte/Medien einstellen → speichern. Es gibt bei diesen Ereignissen keinen zusätzlichen Scorefilter. [Caller-Soundkeys und genaue Auslöser](../CALLER_SOUND_KEYS.de.md).


## Gespeicherte Bedingungen / Stored conditions

WLED, Pixelit, AWTRIX NG und GIF speichern nur die zum Auslöser passenden Bedingungen:
`Score` die Punktzahl (`Minimum`), `ScoreRange` beide Grenzen, `DartField` Feld und Ring,
`Multiplier` nur den Ring, `Combo` nur die Kombination. Andere Auslöser benötigen
keine dieser fünf Bedingungen. Leere optionale Spielerfilter werden weggelassen;
gesetzte wirksame Filter und gültige Nullwerte (z. B. MISS) bleiben erhalten.
Die bestehende WLED-Altregel `DartScore` behält ihre beiden Grenzen.

Beim ersten Start der aktualisierten Version wird `settings.json` automatisch und
atomar bereinigt. GUI, TUI, lokale Weboberfläche und Webapp verwenden denselben
Speicherweg; kein Zurücksetzen und keine Neueinrichtung erforderlich. Alte Backups
werden beim Wiederherstellen bereinigt; neue Backups und HubX-Ereignispakete sind
kompakt. Unbekannte Auslöser und unbekannte Felder werden nicht gelöscht.
Bereits heruntergeladene Dateien und bestehende HubX-Veröffentlichungen bleiben
unverändert. In der TUI wie gewohnt das Modul bearbeiten und speichern; es gibt
keinen gesonderten Bereinigungsbefehl. Die internen Bearbeitungsmodelle und API-DTOs
können weiterhin Startwerte enthalten, damit ein Triggerwechsel konfigurierbar bleibt.
Diese Startwerte werden nicht als ungenutzte Ereignisbedingungen persistiert.

WLED, Pixelit, AWTRIX NG and GIF persist only the conditions their trigger uses:
`Score`: minimum/exact score; `ScoreRange`: both bounds; `DartField`: field and multiplier;
`Multiplier`: multiplier; `Combo`: combo. Other triggers omit all five. Empty optional
player filters are omitted; active filters and meaningful zero values are retained.
Legacy WLED `DartScore` keeps both bounds. Existing settings are cleaned atomically
when the updated host starts. GUI, TUI, local web and webapp share the same storage;
no reset or separate maintenance command is necessary. Old backups are cleaned on
restore, and new backups/HubX exports omit unused conditions. Unknown triggers and
fields are preserved. Existing downloads and published HubX items are not rewritten.
Typed editor/API models retain their editing defaults; storage removes inactive ones.
