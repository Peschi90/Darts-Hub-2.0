# Caller: Soundfile-Keys und Auslöser

[English](CALLER_SOUND_KEYS.en.md) · [Soundpacks einrichten](CALLER_SOUNDPACKS.de.md)

Diese Referenz beschreibt die in Darts-Hub verwendeten Keys. Ein Key ist der Dateiname ohne Endung: `effect_cricket_scored.wav` hat den Key `effect_cricket_scored`. WAV, MP3, OGG und FLAC sind zulässig. Alle Keys werden ohne Beachtung der Groß-/Kleinschreibung gesucht. Varianten `key+1`, `key+2` oder `key+jubel` funktionieren auch ohne Grunddatei. Gemeinsame Mediendateien ersetzen die Varianten des ausgewählten Packs.

GUI, TUI, lokale Wiedergabe und Browser-Caller verwenden dieselben aufgezeichneten Sounds und Ereignisse. TTS-Ersatz benötigt aktiviertes TTS und lokale Wiedergabe; er wird nicht als Audiodatei an den Browser gesendet. Fehlende optionale Effekte und Ambient-Dateien bleiben stumm. Die Pack-Vorschau testet eine Beispieldatei, nicht sämtliche Keys.

## Steuerung der Ausgabe

- Caller muss aktiviert und mindestens lokale oder Browser-Ausgabe aktiv sein.
- `CallEveryDart`: 0 = keine normalen Einzelwurfansagen; 1 = physische Dartpunktzahl; 2 = Segmentansage; 3 = Effekt. `CallBlindSupport = 1` ersetzt die normalen Einzelwurfmodi.
- `EnableScoreCalls` schaltet numerische Punkt- und Cricket-Aufnahmeansagen ein. `CallEveryDartTotalScore` fordert bei Modus 1–3 zusätzlich die Aufnahmeansage an; bei Modus 0 erfolgt sie unabhängig davon.
- `CallCurrentPlayer`: 0 = aus; 1 = Start, Checkout und Sieg; 2 = zusätzlich neuer Spieler/Turn. `CallBotActions` entscheidet über Bot-Ansagen.
- `AmbientSounds > 0` aktiviert den separaten Hintergrundkanal. `AmbientSoundsAfterCalls` bestimmt die Reihenfolge gegenüber Sprachansagen. Ein neuer Ambient-Effekt ersetzt den vorherigen.
- Ein neuer aktivierter Dartcall kann eine laufende normale Ansage abbrechen. Bei ausgeschalteten Einzelwurfansagen unterbricht ein Dart allein keine Ansage. Der Gesamtscore wartet auf Dart 3, kann danach aber unterbrochen werden. Bust und Siegeransagen behalten ihre Priorität.

## Start, Ende und Namen

| Key / Familie | Auslöser und Ersatz |
| --- | --- |
| `matchon` | Matchbeginn; Ersatz `gameon`. Nach Bull-off wird der Start des eigentlichen Spiels erkannt. |
| `gameon` | Legbeginn und Ersatz für Matchbeginn. |
| `s<Set>_l<Leg>_n` | X01-Start mit Sets bei `CallerRealLife = 1`, z. B. `s1_l2_n`; Ersatz `gameon`. Enthält die Set-/Legankündigung. |
| `l<Leg>_n` | X01 ohne Sets bei `CallerRealLife = 1` (`-crl`), z. B. `l2_n`; Ersatz `gameon`. Keine Set-Ansage. |
| `first_to_throw` | Nach Start- und Spielerphrase im X01-Real-Life-Modus. |
| `bulling_start` | Beginn des Bull-offs. |
| `bulling_end` | Bull-off entschieden; gegebenenfalls vorher Gewinnername. |
| `gameshot` | Leggewinn; auch Ersatz bei fehlendem Matchshot. |
| `gameshot_l<Leg>_n` | Leggewinn bei Real-Life-Modus; Ersatz `gameshot`. |
| `matchshot` | Matchgewinn; Ersatz `gameshot`. Der von Autodarts gemeldete Gewinner ist ausschlaggebend. |
| `matchcancel` | Match gelöscht/abgebrochen; Ersatz TTS, sonst stumm. Normales Verlassen eines beendeten Matches ist kein Abbruch. |
| `busted` | Überworfen; Ersatz TTS, sonst stumm. |
| `<spielername>` | Getrimmter Anzeigename in Kleinschreibung, auch Bot-Name. Ersatz `player<N>`, dann TTS. |
| `player<N>` | Aktuelle Spielerposition + 1, z. B. `player1`; die Position kann beim Legwechsel wechseln. |

## Zahlen, Einzelwürfe und Checkout

| Key / Familie | Auslöser und Ersatz |
| --- | --- |
| `<Zahl>`, z. B. `0`, `60`, `180` | Numerische Dart-/Aufnahme-/Checkout-Zahl. Der tatsächlich angeforderte Wert wird gesucht; kein Zusammensetzen aus Ziffern. Ersatz ab 100: `100plus`, falls Spezial-Sounds aktiv; danach TTS, sonst stumm. |
| `100plus` | Ersatz für fehlende Zahlen ab 100 bei `EnableSpecialSounds`. |
| `reaction_<Zahl>` | Zusätzlich nach numerischen Ansagen ab 100 bei `EnableSpecialSounds`; nur wenn vorhanden. |
| `s<Feld>`, `d<Feld>`, `t<Feld>` | Segmentmodus 2: Single, Double oder Triple auf 1–20. Ersatz TTS der Trefferphrase. |
| `m<Feld>` | Segmentmodus 2 bei physischem Fehlwurf; Feld stammt aus der Nachricht, auch `m0`. Ersatz TTS „Daneben“. |
| `bull`, `bullseye` | Single-/Double-Bull in Segmentmodus 2 sowie im Blind-Support. Im normalen Segmentmodus sind `s25`/`d25` kompatible Ersatzkeys. |
| `effect_s<Feld>`, `effect_d<Feld>`, `effect_t<Feld>`, `effect_m<Feld>` | Einzelwurfmodus 3; Ersatz `effect_single`, `effect_double`, `effect_triple`, `effect_miss`. Kein TTS. Bei Cricket gelten zunächst die Cricket-Keys unten. |
| `effect_bull`, `effect_bullseye` | Bull-Effekt in Modus 3; Ersatz `effect_s25`/`effect_d25`, danach allgemeiner Single-/Double-Effekt. |
| `effect_single`, `effect_double`, `effect_triple`, `effect_miss` | Allgemeine Ersatz-Effekte bei fehlendem Segmenteffekt. |
| `yr_<Rest>` | Komplette X01-Checkout-Phrase, z. B. „Du benötigst vierzig“. Höchste Priorität. |
| `you_require` | Einleitung des X01-Checkout-Hinweises, wenn `yr_<Rest>` fehlt; Ersatz TTS. |
| `c_<Rest>` | Checkout-Zahl nach `you_require`; Ersatz normaler Zahlen-Key/TTS. |

Checkout-Hinweise gelten nur für X01, Rest 2–170, mit den eingestellten Wiederholungs- und Board-Grenzen. Bogey-Zahlen 159, 162, 163, 165, 166, 168 und 169 erzeugen keinen normalen Checkout-Hinweis.

## Cricket, Tactics und Hidden Cricket

Cricket verwendet 15–20 und Bull, Tactics 10–20 und Bull. Bei Hidden Cricket werden ausschließlich tatsächlich aufgedeckte Felder verwendet. Marks, Feldstände, Punkte und Gewinner stammen aus Autodarts. Drei Marks schließen ein Feld für den Spieler; Werte größer als drei bedeuten ebenfalls abgeschlossen.

Die folgenden vier Effekte gelten bei `CallEveryDart = 3`. Pro Dart wird **nur einer** ausgewählt: Punkte vor Feldabschluss, danach Mark oder nicht gewertet. Ein Abschluss mit übrigen punktenden Marks verwendet ausschließlich den Punkte-Effekt.

| Key | Exakter Auslöser |
| --- | --- |
| `effect_cricket_mark` | Gewertete Marks, ohne Feldabschluss und ohne Punkte. |
| `effect_cricket_closed` | Der Dart erreicht mindestens die dritte Mark für den Spieler, erzielt aber keine Punkte. |
| `effect_cricket_scored` | Tatsächlich Punkte erzielt. Standard: für den Werfer; Cut Throat: für offene Gegner. Nie bei No Score. |
| `effect_cricket_no_mark` | Keine gewerteten Marks: Nicht-Zielfeld, physischer Fehlwurf oder für alle geschlossenes Feld. |
| `cricket_marks_0` … `cricket_marks_9` | Aufnahme beendet: komplette Phrase „Keine Marks“ oder „Sechs Marks“. Ersatz TTS, danach vorhandene numerische Marks-Zahl ohne Zusatzphrase. Bei Sieg hat die Siegeransage Vorrang. Auch No Score verwendet Marks. |
| `cricket_points` | Optionaler Zusatz nach Marks-Ansage und Zahl, wenn Standard tatsächlich Punkte bringt: z. B. „Punkte“. Nur das Vorhandensein dieser Datei aktiviert den Zusatz. |
| `cricket_penalty_points` | Entsprechender optionaler Cut-Throat-Zusatz: „Strafpunkte“. No Score spielt keinen Punkte-Zusatz. |
| `cricket_field_opened` | Optional nach Segmentansage in Modus 2 oder Blind-Support: erste Mark auf einem zuvor unberührten Feld. Ein direkter Abschluss verwendet stattdessen den Abschluss-Key. |
| `cricket_field_closed` | Optional nach Segmentansage: Feld für den Spieler abgeschlossen. |
| `cricket_field_closed_all` | Optional nach Segmentansage: Feld jetzt für alle geschlossen; Vorrang vor `cricket_field_closed`. |
| `cricket_field_revealed` | Optional nach Segmentansage: Hidden-Cricket-Zielfeld erstmals aufgedeckt. Kann vor einer Abschlussphrase stehen. |
| `ambient_cricket_marks_0` … `ambient_cricket_marks_9` | Hintergrundeffekt für die gewerteten Marks einer beendeten Aufnahme, ohne Sieg. Exakter Key vor allgemeinen Ersatz-Effekten. |

Fehlt ein Cricket-Treffereffekt, wird bei gewerteten Marks der vorhandene Segmenteffekt verwendet. Bei null Marks ist ausschließlich `effect_miss` der Ersatz. Fehlende optionale Feldphrasen bleiben stumm. Korrigierte Treffer und per Undo geänderte Aufnahmen werden anhand ihres neuen Inhalts bewertet; identische Wiederholungen bleiben ohne erneute Ausgabe.

Cricket-Ambient-Ersatz bei fehlendem exakten Marks-Key: 9 → `ambient_180`; 7–8 → `ambient_150more`; 6 → `ambient_120more`; 5 → `ambient_100more`; 4 → `ambient_50more`; 0 → `ambient_noscore`. Bei 1–3 Marks gibt es ohne exakten Key keinen Ersatz. Diese Namen bezeichnen hier Effekte, keine erspielte Punktzahl.

## Blind-Support

| Key / Familie | Auslöser |
| --- | --- |
| `bs_target_is` | Einleitung vor einem aus dem Spielzustand bekannten Ziel. |
| `bs_any_double`, `bs_any_triple` | Beliebiges Double-/Triple-Ziel. |
| `bs_<Zielbett>` | Geliefertes Zielbett in Kleinschreibung, wenn nicht leer/`Full`; anschließend Feldzahl. |
| `bs_single_inner` | Vor einem Single-Innen-Treffer mit Bett `SingleInner` oder `Inner Single`. |
| `d<Feld>`, `t<Feld>`, `m<Feld>` | Vollständige Trefferphrase; Single verwendet direkt die Feldzahl. |
| `bs_double`, `bs_triple`, `bs_outside` | Ersatzpräfix, wenn die vollständige Trefferphrase fehlt; danach Feldzahl. |
| `bull`, `bullseye`, `<Feldzahl>` | Bull-/Feldziel oder Treffer; Ersatz TTS. |

Alle Blind-Phrasen haben TTS-Ersatz. Cricket verwendet zusätzlich die optionalen Feldphrasen; noch verborgene Ziele werden nicht vorab angesagt.

## Ambient-Keyfamilien

| Key / Familie | Auslöser und Auswahl |
| --- | --- |
| `ambient_<Kombination>` | X01/Shanghai, abgeschlossene Aufnahme mit Punkten und ohne Sieg; originale Segmentnamen in Wurfreihenfolge, kleingeschrieben, z. B. `ambient_t20t20t20`. Vor exakter Zahl und Bereich. |
| `ambient_<Gesamtwert>` | X01/Shanghai: Ersatz für fehlende Kombination. |
| `ambient_180` | Exakt 180 in Count-up/Gotcha; neun Trefferwerte in RTW; Cricket-Ersatz für neun Marks. |
| `ambient_150more`, `ambient_120more`, `ambient_100more`, `ambient_50more`, `ambient_1more` | X01/Shanghai/Bermuda: höchster Bereich ab 150/120/100/50/1. Count-up/Gotcha: ab 153/120/100/50, keine 1more-Auswahl. RTW: ab 7/6/5/4 Trefferwerten. Cricket: Marks-Ersatz wie oben. |
| `ambient_noscore` | Nullpunkte/Überwerfen in entsprechenden Modi; bei Cricket null gewertete Marks. |
| `ambient_group_legendary`, `ambient_group_perfect`, `ambient_group_very_nice`, `ambient_group_good`, `ambient_group_normal` | Zusätzliche Gruppierung bei drei Koordinaten in X01/Shanghai/Bermuda; Schwellen 98/95/92/89/86 nach bestehender Gruppierungsberechnung. |
| `ambient_matchon`, `ambient_gameon` | Match-/Legbeginn; Match-on verwendet Game-on als Ersatz. |
| `ambient_matchshot`, `ambient_setshot`, `ambient_gameshot` | Match-/Set-/Leggewinn; Match-/Setshot verwenden Game-shot als Ersatz. |
| `ambient_playerchange` | Neuer Spieler/Turn, wenn kein Checkout-Hinweis gesprochen wird. |
| `ambient_<Ereignis>_<spielername>` | Namensvariante für Match-/Game-on, Match-/Set-/Game-shot und Playerchange; vor dem allgemeinen Key. |
| `ambient_lobby_in`, `ambient_lobby_out` | Spieler betritt/verlässt eine verfolgte Lobby. |
| `ambient_bogey_number_<Rest>`, `ambient_bogey_number` | Nicht auscheckbare X01-Bogey-Zahl; exakter Wert vor allgemeinem Key. |
| `ambient_checkout_call_limit` | Checkout-Wiederholungsgrenze erreicht, wenn erneut ein Hinweis angefordert wird. |
| `ambient_matchcancel` | Matchabbruch; ersetzt den laufenden Ambient-Effekt. |

ATC erzeugt keine Aufnahme-Punkte-Ambienteffekte. Cricket verwendet die Marks-Auswahl und nicht die physische Punktesumme. Nicht aufgeführte Fantasienamen werden nicht automatisch als Ereignis gesucht; sie können lediglich als explizit ausgewählte Vorschau-Datei gespielt werden.

## Erweiterungstrigger und Terminal-Bedienung

WLED, PixelIt, Awtrix und GIF bieten dieselben Cricket-Trigger: `CricketMark`, `CricketClosed`, `CricketScored`, `CricketNoMark`, `CricketOpened`, `CricketClosedAll`, `CricketRevealed`. Die ersten vier sind gegenseitig ausschließende Trefferergebnisse. Die weiteren sind zusätzliche Zustandsübergänge. Siegerereignisse haben Vorrang; bei WLED unterliegen die neuen Dartregeln derselben Expertenfreigabe wie andere detaillierte Dartregeln.

GUI: Erweiterung → Ereignisregel hinzufügen → Cricket-Auslöser auswählen → Effekte/Medien/Display-Schritte einstellen → speichern. TUI: jeweilige Erweiterung → Regeln → Regel hinzufügen/bearbeiten → denselben Auslöser wählen → speichern. Bestehende JSON-Regeln behalten ihre Trigger beim Speichern und Import; neue Cricket-Regeln werden nicht aus alten allgemeinen Score-Regeln erfunden.

PixelIt/Awtrix-Platzhalter: `cricket-scoring-mode`, `cricket-field`, `cricket-marks`, `cricket-turn-marks`; `score` bei einem Cricket-Trefferereignis enthält dessen erspielte Punkte, `dart-score` weiterhin den physischen Dartwert. `game-mode-extra` enthält Cricket/Tactics/Hidden Cricket. Marks sind Trefferwerte, nicht automatisch neue Feldabschlüsse oder Punkte.
