# Eigene Caller-Soundpacks erstellen

[English](CALLER_SOUNDPACKS.en.md) · [Caller bedienen](CALLER_CONFIGURATION_AND_LOCALIZATION.md)

Diese Anleitung beschreibt die **aktuell in Darts-Hub 2.0 verwendeten** Soundnamen und Auslöser. Ein Soundpack besteht aus Audiodateien; der Dateiname ohne Endung ist der **Key**, über den der Caller die Aufnahme findet. `180.wav` hat beispielsweise den Key `180`. Die Sprache deiner Aufnahme ist frei wählbar und unabhängig von der Sprache der Oberfläche.

## 1. Schnellstart: ein eigenes Pack verwenden

1. Erstelle einen eigenen Ordner, etwa `de-MeineStimme`.
2. Lege die Aufnahmen **direkt in diesen Ordner**. Unterordner werden nicht durchsucht.
3. Lege den Ordner in den eingestellten Soundpack-Hauptordner. Alternativ wählst du im Caller einen eigenen **Medienpfad** als Hauptordner. Dieser enthält die einzelnen Pack-Ordner, nicht die Audiodateien selbst.
4. Aktualisiere die Bibliothek beziehungsweise öffne die Caller-Seite erneut. Lokale Pack-Ordner werden mit ihrem Ordnernamen angezeigt. Wähle dein Pack als Stimme und schalte die zufällige Stimmenwahl aus (`RandomCaller = 0`), damit es nicht beim nächsten Match ersetzt wird.
5. Aktiviere Caller und lokale Wiedergabe, übernimm die Einstellungen und teste. Nach dem Austauschen von Dateien die Stimme erneut auswählen und Einstellungen übernehmen oder Darts-Hub neu starten, damit die Dateiliste neu geladen wird.

Der Standardordner liegt im Darts-Hub-Datenverzeichnis (unter Windows normalerweise `%LOCALAPPDATA%\DartsHub\soundpacks`). Maßgeblich ist der in deiner Installation konfigurierte Pfad. Eigene Medienpfade müssen absolute Pfade sein.

```text
C:\MeineSoundpacks\              ← im Caller als Medienpfad auswählen
└── de-MeineStimme\               ← als Stimme auswählen
    ├── gameon.wav
    ├── matchon.wav
    ├── gameshot.wav
    ├── matchshot.wav
    ├── matchcancel.wav
    ├── busted.wav
    ├── 0.wav
    ├── 60.wav
    ├── 180.wav
    ├── player1.wav
    ├── player2.wav
    ├── you_require.wav
    ├── bulling_start.wav
    └── bulling_end.wav
```

Das ist eine Startauswahl, kein vollständiger Satz aller Punktzahlen. Du brauchst weder eine JSON-Datei noch eine CSV-Zuordnung für einen selbst angelegten lokalen Ordner. Eine ZIP-Datei allein wird dort nicht als Pack geladen: zum Weitergeben den Pack-Ordner zippen, beim Empfänger entpacken lassen und wie oben auswählen. Dadurch wird das Pack nicht automatisch Teil der Online-Downloadbibliothek.

### Dateiformate und Aufnahmen

- Der Loader erkennt `.wav`, `.mp3`, `.ogg` und `.flac`. Ob eine Datei abgespielt werden kann, hängt auch vom Audiobackend des Betriebssystems ab. **PCM-WAV** ist für eigene, plattformübergreifende Packs die einfachste Wahl; etwa 44,1 kHz, 16 Bit, Mono oder Stereo. Das ist eine Empfehlung, keine feste Vorgabe des Loaders.
- Halte die Aufnahme kurz und entferne Stille am Anfang und Ende. Der Caller wartet auf das Ende einer Aufnahme. Lange Pausen in der Audiodatei bleiben daher hörbar.
- Verwende pro Key eine Endung. Nicht gleichzeitig `180.wav` und `180.mp3` ablegen: welche davon verwendet wird, ist nicht zuverlässig festgelegt.
- Keys werden ohne Beachtung der Groß-/Kleinschreibung gesucht. Verwende trotzdem durchgehend die hier gezeigten kleinen Dateinamen. Sonderzeichen müssen exakt dem gesuchten Namen entsprechen.
- Verwende keine unter Windows reservierten Dateinamen wie `CON` oder `AUX` für eigene Namensaufnahmen. Heruntergeladene verwaltete Packs besitzen dafür eine interne Kodierung; für eigene Packs ist diese nicht nötig.

### Zufällige Varianten und gemeinsame Dateien

Du kannst zu **jedem Key** Varianten anlegen: `180.wav`, `180+1.wav`, `180+2.wav`. Bei jeder Verwendung wird zufällig aus Grunddatei und Varianten ausgewählt. Die Grunddatei ist optional; `180+1.wav` allein genügt. Nach `+` müssen Ziffern stehen. `180_alt.wav` ist keine Variante von `180`.

Ein **gemeinsamer Medienpfad** (`MediaPathShared`) ergänzt das ausgewählte Pack. Dort liegen die Dateien ebenfalls direkt im Ordner. So können mehrere Stimmen dieselben Namens- oder Ambient-Aufnahmen nutzen. Bei **identisch geschriebenem Key** überschreibt die gemeinsame Datei den Pack-Eintrag. Vermeide unterschiedliche Großschreibung und gleiche Keys mit verschiedenen Endungen, damit die Auswahl eindeutig bleibt. Der Pack-Ordner selbst muss vorhanden sein; der gemeinsame Pfad ist kein eigenständiges Pack.

## 2. Einstellungen, die bestimmen, welche Dateien benutzt werden

Die internen Einstellungsnamen helfen bei TUI, Headless und der Suche nach einer Option. In GUI und TUI findest du dieselben Einstellungen auf der Caller-Seite.

| Einstellung | Wirkung auf dein Pack |
| --- | --- |
| `Enabled`, `LocalPlayback` | Beide müssen für lokale Ansagen und Ambient-Sounds aktiv sein. |
| `EnableScoreCalls` | Aktiviert numerische Punktansagen, auch bei Einzelwurfmodus 1 und beim numerischen Checkout-Ersatz. |
| `CallEveryDart` / `-E` | `0`: keine normalen Einzelwurfansagen; `1`: Punktzahl; `2`: Segment; `3`: Soundeffekt. |
| `CallEveryDartTotalScore` / `-ETS` | Zusätzlich Gesamtscore am Ende der Aufnahme bei Einzelwurfmodus 1–3. Bei Modus 0 wird der Gesamtscore unabhängig von diesem Schalter angefordert. |
| `EnableSpecialSounds` | Aktiviert den Ersatz `100plus` und die zusätzlichen `reaction_<Punkte>`-Sounds. |
| `CallCurrentPlayer` / `-CCP` | `0`: keine normalen Namensansagen; `1`: bei Start, Checkout-Hinweis und Sieger; `2`: zusätzlich beim Spieler-/Aufnahmenwechsel. |
| `CallBotActions` / `-CBA` | Bei ausgeschaltetem Schalter werden Bot-Würfe, Bot-Namen und Bot-Siegeransagen übersprungen. |
| `PossibleCheckoutCall` / `-PCC` | `0`: keine Checkout-Hinweise; größer als 0: begrenzt die Hinweise pro Spieler und unverändertem Restscore. |
| `PossibleCheckoutCallYourselfOnly` / `-PCCYO` | Checkout nur für Spieler am eigenen Board. |
| `CallerRealLife` / `-CRL` | `1`: X01 verwendet spezielle Set-/Leg-Start- und Leg-Siegersounds, wenn vorhanden. |
| `CallBlindSupport` / `-CBS` | `1`: Ziel- und Wurferklärung für sehbehinderte Spieler; ersetzt die normalen Einzelwurfmodi. |
| `AmbientSounds` / `-A` | `0`: Hintergrundeffekte aus; größer als 0: relative Ambient-Lautstärke. Effektive Lautstärke = Caller-Lautstärke × dieser Wert. |
| `AmbientSoundsAfterCalls` / `-AAC` | Aus: Ambient vor der zugehörigen Ansage starten; ein: nach dieser Ansage starten. Ambient läuft unabhängig auf einem eigenen Kanal. |
| `TtsEnabled` | Optionaler Sprachersatz für bestimmte fehlende Dateien. Standard aus; nicht auf allen Plattformen verfügbar. |

**Wichtig:** `EnablePlayerNameCalls` ist kein Ersatz für `CallCurrentPlayer`. Die normale Live-Spielernamenslogik richtet sich nach `CallCurrentPlayer`. Die Zusatzoption im Score-Helfer erzeugt in der aktuellen Live-Pipeline keine eigene Namensansage nach jeder Punktzahl.

## 3. Start, Sieg, Abbruch und Bull-Off

In den Tabellen bedeutet **stumm**: keine automatische Sprachausgabe als Ersatz. „TTS“ funktioniert nur, wenn TTS eingeschaltet und auf dem System verfügbar ist.

| Key / Beispieldatei | Wann / empfohlener Inhalt | Wenn die Datei fehlt |
| --- | --- | --- |
| `matchon` → `matchon.wav` | Neues normales Match beziehungsweise Wechsel von Bull-Off in das eigentliche Spiel. Inhalt z. B. „Match on“. | `gameon`, danach stumm. |
| `gameon` | Beginn eines weiteren Legs; außerdem Ersatz für fehlenden Match-/Set-Leg-Startsound. „Game on“. | Stumm. |
| `s<Set>_l<Leg>_n`, z. B. `s1_l2_n` | X01 mit `CallerRealLife = 1`: Start des angegebenen Sets/Legs. Eine komplette Phrase aufnehmen, z. B. „Erstes Set, zweites Leg“. | `gameon`. |
| `first_to_throw` | X01 mit `CallerRealLife = 1`: nach Startsound und optionalem Spielernamen. „Wirft zuerst“. | Stumm. |
| `gameshot` | Leg gewonnen. „Game shot“. | Stumm. |
| `gameshot_l<Leg>_n`, z. B. `gameshot_l2_n` | Leg-Sieg mit `CallerRealLife = 1`. „Game shot, zweites Leg“. Kein separater Set-Index in diesem Key. | `gameshot`. |
| `matchshot` | Match gewonnen; auch Matchende durch Aufgeben mit bekanntem Sieger. „Game shot and the match“. | `gameshot`. |
| `matchcancel` | Autodarts meldet das Löschen (`delete`) des Matches am Board; pro Match einmal. „Match abgebrochen“. Auch nach einem schon beendeten Match kann eine spätere Löschung diese Ansage auslösen. | TTS „Match abgebrochen“ / „Match cancelled“, sonst stumm. |
| `busted` | Überworfen/Bust, auch vor dem dritten Dart. | TTS „Überworfen“ / „Bust“, sonst stumm. |
| `bulling_start` | Neues, noch nicht beendetes Bull-Off. „Ausbullen“. | Stumm. |
| `bulling_end` | Bull-Off hat einen ermittelten Bull-Sieger; optionaler Siegername wird **vorher** angesagt. Beispielsweise „beginnt“. | Stumm. |

Die Platzhalter `<Set>` und `<Leg>` werden durch die tatsächlichen Zahlen von Autodarts ersetzt. Eine Datei namens `s<Set>_l<Leg>_n.wav` funktioniert nicht. Lege die benötigten Kombinationen einzeln an. Die Zahlen kommen aus dem Spielzustand; es werden keine gesprochenen Einzelzahlen zu einer Set-/Leg-Phrase zusammengesetzt.

**Bull-Off ist eine eigene Phase:** dort werden keine normalen Punktzahlen, Einzelwurfeffekte, Bust-, Checkout- oder Leg-Siegeransagen abgespielt. Beim Aufgeben während Bull-Off ohne Bull-Sieger wird stattdessen `matchshot` (Ersatz `gameshot`) und gegebenenfalls der Siegername benutzt. Ein bloßes Board-`finish` ohne Siegerdaten ist keine neue Startansage und bestimmt allein keinen Sieger.

Ein Neustart während eines laufenden Spiels kann eine Startansage auslösen, sobald ein verwendbarer Spielzustand vorliegt. Bereits vorhandene Würfe werden dabei als Ausgangszustand behandelt und nicht einzeln nachgesprochen. Es gibt keinen gesonderten Soundfile-Key „Programmstart“ oder „Programmende“ in dieser Caller-Pipeline.

## 4. Punktzahlen und besondere Reaktionen

| Key | Verwendung / Inhalt | Ersatz |
| --- | --- | --- |
| `<Punkte>`, z. B. `0`, `26`, `60`, `140`, `180` | Gesamtscore einer beendeten Aufnahme; außerdem Dart-Punktzahl bei `CallEveryDart = 1` und gegebenenfalls Checkout-Zahl. Die Aufnahme spricht die Zahl. `0` kann „No score“ sprechen. | Bei ≥100 zuerst `100plus`, sofern besondere Sounds aktiv sind; sonst TTS der Zahl, sonst stumm. |
| `100plus` | Allgemeiner Ersatz für eine **fehlende** Zahl ≥100. Z. B. „Hundert plus“. Nicht zusätzlich zur vorhandenen exakten Zahl. | TTS der exakten Zahl, sonst stumm. |
| `reaction_<Punkte>`, z. B. `reaction_180` | Zusätzliche Reaktion **nach** einer numerischen Ansage für exakt diese Punktzahl ≥100, wenn besondere Sounds aktiv sind. | Keine zusätzliche Reaktion. |

Für vollständige Scores ohne Sprachersatz ist ein Satz `0.wav` bis `180.wav` sinnvoll. Nicht jede Zahl ist mit drei Darts erreichbar, aber auch manuelle Korrekturen können Daten liefern. Für Blind-Zielansagen brauchst du ebenfalls die Feldzahlen. Zahlen haben keine führenden Nullen: `060.wav` wird nicht als `60` gesucht.

**Wann kommt der Gesamtscore?** Normalerweise nach drei Darts. Der Caller kann eine Aufnahme auch bei Bust, Sieg, einem Spielerwechsel oder einem gemeldeten Herausziehen als abgeschlossen behandeln, wenn Würfe vorhanden sind. Dadurch sind auch Aufnahmen mit einem oder zwei Darts möglich. Bei Bust wird `busted` anstelle der Punktzahl angefordert. Score-/Reaktionsdateien sind Vordergrundsounds; `reaction_180` ist kein Ambient-Sound.

Es gibt in dieser Implementierung keinen gesuchten Key `noscore`, `no_score`, `bust_reaction_1` oder `cpu`. Verwende für Nullpunkte `0`, für Bust `busted`, für Bots deren Namensdatei oder `player<N>`.

## 5. Einzelwürfe: Punkte, Segmente und Effekte

| Modus | Gesuchte Keys | Beispiele und Verhalten |
| --- | --- | --- |
| `CallEveryDart = 0` | Keine normalen Einzelwurfkeys. | Gesamtscore am Ende; Sonderereignisse bleiben aktiv. |
| `CallEveryDart = 1` | Numerischer Dart-Score. | T20 → `60`; D20 → `40`; Single20 → `20`; Fehlwurf → `0`. Ersatz wie in Abschnitt 4. |
| `CallEveryDart = 2` | `s<Feld>`, `d<Feld>`, `t<Feld>`, `m<Feld>`. | T20 → `t20`, D20 → `d20`, Single20 → `s20`; Nullpunkte → `m` plus übermitteltes Feld. Fehlt die Datei, TTS „Triple 20“, „Double 20“, „Single 20“ oder „Daneben“, sonst stumm. |
| `CallEveryDart = 3` | `effect_s<Feld>`, `effect_d<Feld>`, `effect_t<Feld>`, `effect_m<Feld>`. | Effekt pro Segment, keine gesprochene Zahl. Ersatz: `effect_single`, `effect_double`, `effect_triple`, `effect_miss`. Fehlt auch dieser, stumm; kein TTS-Ersatz. |

Für normale Felder ist `<Feld>` 1–20. Bull wird mit Feld **25** verarbeitet: bei Modus 2 `s25` für Single Bull und `d25` für Bullseye; bei Modus 3 `effect_s25` / `effect_d25`. Bei Modus 1 sind es `25` / `50`. Die Keys `bull` und `bullseye` gehören zu Blind-Support (Abschnitt 8), nicht automatisch zum normalen Segmentmodus.

Beim Fehlwurf wird das übermittelte Feld verwendet, z. B. `m0`, `m20`, `effect_m0`, `effect_m20`. Der allgemeine Effekt `effect_miss` deckt alle Nullpunkte ab. Der Segmentmodus 2 hat **keinen** allgemeinen `miss`-Dateiersatz; dort gibt es nur die konkrete `m<Feld>`-Datei oder TTS.

Ein neuer Dart unterbricht eine noch laufende normale Einzelwurfansage und ersetzt sie. Veraltete Einzelwürfe in der Warteschlange werden ausgelassen. Bei aktivem Gesamtscore hat dieser nach dem dritten Dart Vorrang; dann kann dessen Einzelwurfansage/-effekt ausfallen. Gesamtscore, Bust und Siegeransagen werden zu Ende abgespielt. Die erklärenden Ansagen im Blind-Modus werden nicht wie normale Einzelwürfe unterbrochen.

## 6. Spielernamen und Bots

| Key | Wann / Inhalt | Ersatz |
| --- | --- | --- |
| `<spielername>`, z. B. `alice` oder `bot level 4` | Aufnahme des Namens. Gesuchter Name = Anzeigename ohne führende/abschließende Leerzeichen, in Kleinschreibung; innere Leerzeichen bleiben. | `player<N>`. |
| `player<N>`, z. B. `player1`, `player2`, `player3` | „Spieler 1“, „Spieler 2“ usw.; `<N>` = aktuelle Spielerposition + 1. | TTS „Spieler N“ / „Player N“, sonst stumm. |

Es wird kein Bot-Key `cpu` automatisch gesucht. Ein Bot heißt z. B. `Bot Level 4` und wird über `bot level 4.wav` oder den Positionsersatz angesagt. `CallBotActions` muss dafür aktiv sein. Die aktuelle Spielerposition kann sich nach Bull-Off ändern; `player1` bezeichnet eine Position, keine feste Person. Ein Spielernamen-Key wie `180` würde mit dem Zahlen-Key kollidieren: verwende in solchen Fällen den Positionsersatz.

Namensansagen benötigen `CallCurrentPlayer > 0`: beim Start, vor Checkout-Hinweisen und nach normalen Siegeransagen; beim Bull-Off-Sieger vor `bulling_end`. Für jeden Spieler-/Aufnahmenwechsel `CallCurrentPlayer = 2` einstellen.

## 7. Checkout-Hinweise

Nur X01, mit aktiviertem Checkout-Hinweis. Berücksichtigt werden Restpunkte **2–170**, außer 159, 162, 163, 165, 166, 168 und 169. Hinweise kommen beim Spiel-/Leg-Start und Spieler-/Aufnahmenwechsel; Blind-Support kann sie außerdem nach einem neuen Dart auslösen. Die Einstellungen zur Wiederholungszahl und zum eigenen Board gelten weiterhin.

| Priorität / Key | Inhalt / Verwendung |
| --- | --- |
| 1. `yr_<Rest>`, z. B. `yr_40` | **Komplette Phrase**, z. B. „Du benötigst vierzig“. Falls vorhanden, wird weder `you_require` noch eine weitere Zahl abgespielt. |
| 2. `you_require` | Einleitung „Du benötigst“. Fehlt sie, TTS der Einleitung oder stumm; danach trotzdem die Zahl. |
| 3. `c_<Rest>`, z. B. `c_40` | Checkout-Zahl nach der Einleitung. Beispielsweise „vierzig“. Diese Datei ist von der normalen `40` getrennt. |
| 4. `<Rest>`, z. B. `40` | Wenn `c_40` fehlt, normaler numerischer Score-Aufruf: Zahl → gegebenenfalls `100plus` → TTS → stumm; dabei können aktivierte `reaction_<Rest>`-Dateien ebenfalls folgen. |

Vor dem Hinweis wird gegebenenfalls der Spielername gesprochen. Die Dateien enthalten keine Platzhalter; `yr_40.wav` muss die komplette Aufnahme für 40 enthalten. Auch werden aus diesen Dateien keine Checkout-Wege wie „Single 8, Double 16“ zusammengesetzt.

## 8. Blind-Support: Ziel und Treffer erklären

`CallBlindSupport = 1` aktiviert diese Logik und ersetzt die normalen Einzelwurfmodi. Sie verwendet die Zielinformationen, die Autodarts tatsächlich liefert. Fehlt ein Ziel, gibt es keine Zielansage. Bei Bull-Off läuft weiterhin ausschließlich die Bull-Off-Logik.

| Key | Wann / Beispielinhalt | Ersatz |
| --- | --- | --- |
| `bs_target_is` | Vor einer vorhandenen Zielansage: „Ziel ist“. | TTS der Einleitung. |
| `bs_any_double` | Ziel ist ein beliebiges Double. | TTS „Double“. |
| `bs_any_triple` | Ziel ist ein beliebiges Triple. | TTS „Triple“. |
| `bull` | Ziel/Treffer Feld 25 ohne Double. „Bull“. | TTS „Bull“. |
| `bullseye` | Ziel/Treffer Feld 25 mit Double. „Bullseye“. | TTS „Bullseye“. |
| `bs_<zielbett in kleinschreibung>` | Zielbett, sofern weder leer noch `Full`; etwa `bs_double`, `bs_triple`, `bs_singleinner` oder `bs_singleouter`, wenn Autodarts dieses Bett liefert. | TTS des gelieferten Bett-Namens; danach Feldzahl, sofern vorhanden. |
| `bs_single_inner` | Vor einem Treffer, dessen Bett `SingleInner` oder `Inner Single` ist: „Single innen“. **Beachte den Unterstrich; das ist ein anderer Key als `bs_singleinner`.** | TTS „Single innen“ / „Inner single“. |
| `d<Feld>`, `t<Feld>`, `m<Feld>` | Vollständige Trefferphrase für Double, Triple oder Nullpunkte; `d20`, `t20`, `m0` usw. | Bett-Präfix aus nächster Zeile, dann Feldzahl. |
| `bs_double`, `bs_triple`, `bs_outside` | Ersatz-Präfix vor einer Feldzahl, wenn der vollständige Treffer-Key fehlt. „Double“, „Triple“, „Daneben“. | TTS des Präfixes. |
| `<Feld>`, z. B. `20` | Single-Treffer oder Feldzahl nach einem Präfix / einer Zielansage. | TTS der Zahl. |

TTS-Ersatz bleibt in allen Zeilen stumm, wenn TTS nicht aktiv/verfügbar ist. Bull/Bullseye wird als eigene Phrase behandelt und nicht aus Präfix plus Zahl zusammengesetzt. Bei Single innen kann die Zusatzphrase `bs_single_inner` vor der Zahl stehen. Nach einer abgeschlossenen Aufnahme kann zusätzlich der normale Gesamtscore kommen.

## 9. Ambient-Sounds: eigener Hintergrundkanal

| Key | Auslöser |
| --- | --- |
| `ambient_<Gesamtscore>`, z. B. `ambient_60`, `ambient_140`, `ambient_180` | Abgeschlossene Aufnahme mit genau diesem Gesamtscore. Nicht jeder Einzelwurf. |
| `ambient_busted` | Abgeschlossene überworfen/Bust-Aufnahme, statt `ambient_<Gesamtscore>`. |
| `ambient_matchcancel` | Matchlöschung zusammen mit der Abbruchansage. |

Ambient benötigt `AmbientSounds > 0`. Es gibt keinen allgemeinen Ersatz-Key und keinen TTS-Ersatz. Die genaue Datei muss vorhanden sein. Ambient ist von der gesprochenen Score-Ansage unabhängig: ein ausgeschalteter Score-Schalter verhindert bei ansonsten aktivem Caller nicht den passenden Ambient-Sound. Bull-Off erzeugt keine normalen Ambient-Score-Effekte.

Ambient wird niemals wegen einer neuen Vordergrundansage abgebrochen. Sounds auf dem Ambient-Kanal werden untereinander nacheinander abgespielt; währenddessen kann der Vordergrund sprechen. Beim Beenden des Callers enden beide Kanäle. `AmbientSoundsAfterCalls` bestimmt den Startzeitpunkt vor/nach der passenden Score-/Bust-/Abbruchansage, nicht ob Ambient den Vordergrund blockiert.

## 10. Beispielabläufe und Test-Checkliste

| Situation | Beispiel der angeforderten Dateien |
| --- | --- |
| Normaler Matchstart, Alice mit Checkout-Hinweisen aus | `matchon` → `alice` (oder `player1`). |
| Drei T20, Einzelwürfe aus, besondere Sounds und Ambient an | Vordergrund `180` → optional `reaction_180`; Hintergrund `ambient_180` unabhängig davon. |
| T20 im Segmentmodus | `t20`; bei fehlender Datei TTS „Triple 20“, wenn aktiv. |
| T20 im Effektmodus | `effect_t20`; sonst `effect_triple`. |
| Checkout-Hinweis für 40 | Name → `yr_40`; andernfalls Name → `you_require` → `c_40` oder `40`. |
| Bust | Vordergrund `busted`, Hintergrund optional `ambient_busted`. |
| Matchgewinn | Gegebenenfalls abgeschlossene Aufnahme, dann `matchshot` (sonst `gameshot`) → Siegername, sofern Namen aktiv. |
| Bull-Off | `bulling_start`; bei Bull-Sieger optional Name → `bulling_end`; anschließend normales Match mit `matchon`. |

Zum Testen zunächst zufällige Stimmenwahl und TTS ausschalten, damit fehlende Dateien auffallen. Pack-Vorschau verwendet bevorzugt `180`, dann `matchon`, dann `gameon`, sonst eine verfügbare Datei; sie prüft **nicht** alle Ereignisse. Spiele gezielt Single, Double, Triple, Nullpunkte, Bust, Checkout, Leg-/Matchgewinn und Bull-Off durch. Aktiviere Caller-Debug in der Konsole: `Sound not found` nennt fehlende Keys; `Played sound` nennt den verwendeten Key; ausgelassene veraltete Einzelwürfe sind beabsichtigt.

**Headless-Beispiel** (Windows; unter Linux `./DartsHub` statt `.\DartsHub.exe`):

```powershell
.\DartsHub.exe --headless --caller-media-path "C:/MeineSoundpacks" --caller-caller "de-MeineStimme" --caller-random-caller 0 --caller-enabled true --caller-local-playback true --caller-tts-enabled false --caller-call-every-dart 3 --caller-call-every-dart-total-score true
```

Die Einstellungen sind für GUI, TUI und Headless gemeinsam. Prüfe mit `--help` die verfügbaren Startoptionen deiner Version; Namen hier beziehen sich auf die aktuelle Implementierung. Die Kurzoption heißt **`-E`** (großes E). Siehe [Startargumente](START_ARGUMENTS.md).
