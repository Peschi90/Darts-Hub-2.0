# PixelIt: Displays und Sequenzen / Displays and sequences

## Deutsch

### HubX-Vorlagen
Im Modul **Effekte entdecken** öffnen. Beim Teilen eines Ereignisses wird zusätzlich seine wirksame Vorlage inklusive Text-, Farb-, Scroll- und Helligkeitsanpassungen angeboten. Eine einzelne HubX-Vorlage wird mit `_hubX` in der Bibliothek gespeichert und sofort geladen, ohne Ereignisregel oder Zielgerät. Ereignispakete benötigen dagegen eine Gerätezuordnung. Direkte Zustellung und Paketdateiimport verwenden dieselben Prüfungen: [HubX](HUBX.md).

1. Autodarts verbinden und das gewünschte Board auswählen; der Caller ist nicht nötig.
   Die Seite **PixelIt** öffnen und das Modul aktivieren.
2. Ein Gerät mit Namen, Adresse und optionalem Port hinzufügen und aktivieren.
	  **Display testen** sendet auch vor dem Speichern ein echtes, sichtbares Bild.
3. Eine Regel anlegen und den Auslöser wählen; Spieler und Score bei Bedarf eingrenzen.
   Für die Sequenz die gewünschten Schritte hinzufügen.
4. Je Schritt Vorlage, optional Text, Zielgeräte sowie bei Bedarf Helligkeit und Verzögerung wählen.
   Die Reihenfolge mit den Pfeilen ändern; für Verzögerungen die UI-Hilfe beachten.
5. Mit **Sequenz testen** den Entwurf ohne Speichern auf den Geräten ausprobieren.
   Anschließend **Speichern** wählen, um die Einstellungen dauerhaft zu übernehmen und anzuwenden.

**Hinweise**
- Im Text sind besonders `{score}`, `{playername}` und `{points-left}` nützlich.
- Eigene Vorlagen optional auf dem Host ablegen, den Vorlagenordner einstellen und **Vorlagen neu laden** wählen.
- Entfernte gewählte Geräte deaktivieren betroffene Regeln; neue Ziele wählen, bevor die Regeln wieder aktiviert werden.
- TUI: auf der Seite **PixelIt** mit **Enter** bearbeiten und mit **Entwurf speichern** speichern.

## English

### HubX templates
Discover contributions in the module. Sharing an event also offers its effective template, including text/color/scroll/brightness overrides. Standalone templates save to the library with `_hubX` and load immediately without a rule or target device. Event packages need device selection. Direct and package-file imports share review: [HubX](HUBX.md).

1. Connect Autodarts and select the intended board; Caller is not required.
   Open **PixelIt** and enable the module.
2. Add and enable a device with a name, address and optional port.
   **Test display** sends a real, visible image even before saving.
3. Add a rule and choose its trigger; optionally filter by player and score.
   Add the desired steps to the sequence.
4. For each step choose a template, optional text, targets and optional brightness and delay.
   Use the arrows to reorder steps; follow the UI help for delays.
5. Use **Test sequence** to try the draft on the devices without saving.
   Then choose **Save** to persist and apply the settings.

**Notes**
- Useful text variables include `{score}`, `{playername}` and `{points-left}`.
- Optionally place custom templates on the host, set the template directory and choose **Reload templates**.
- Removing selected devices disables affected rules; choose new targets before enabling the rules again.
- TUI: edit with **Enter** on the **PixelIt** page and persist with **Save draft**.

### Live-Anzeige nach jedem Wurf (PixelIt und AwtrixNG)

**Eine Matrix für alle Spieler:** Lege zwei Regeln an: **Nach jedem Wurf** und **Spielerwechsel**. Lass den Spielerfilter leer und wähle in beiden Regeln dieselbe Matrix als Ziel. Aktiviere **Vorlagentext ersetzen** und trage z. B. ein:

```text
{playername} {points-left} D{dart-number}
```

Die Anzeige startet mit dem aktiven Spieler, aktualisiert sich nach jedem Wurf und wechselt beim Spielerwechsel automatisch. Bei PixelIt setze die Pause danach für eine schnelle Anzeige auf 0.

**Eine Matrix je Spieler:** Verwende dieselben Ereignisse und pro Matrix einen Text mit fester Spielernummer, etwa:

```text
{p1-playername} {p1-points-left} D{p1-darts-thrown}
```

Auf der zweiten Matrix ersetze `p1` durch `p2`, usw. Die Nummern bleiben gleich, auch wenn sich der Startspieler ändert. Lass den Spielerfilter leer, damit die Werte bei jedem Ereignis aktualisiert werden. Weise den Anzeigeschritt jeweils der gewünschten Matrix zu.

| Platzhalter | Bedeutung |
| --- | --- |
| `{dart-score}` | Punkte des letzten Darts |
| `{dart-number}` | Dartnummer in der aktuellen Aufnahme (0–3) |
| `{darts-thrown}` | Anzahl geworfener Darts im aktuellen Leg |
| `{turn-score}` | Punkte der aktuellen Aufnahme |
| `{points-left}` | Restpunkte des ausgewählten/aktiven Spielers |
| `{p1-points-left}`, `{p1-darts-thrown}` | Feste Werte von Spieler 1; ebenso für p2 bis p32 |

Korrekturen, Zurücknehmen und Überwerfen verwenden die von Autodarts gemeldeten Werte. In der TUI stehen dieselben Ereignisse und Textfelder zur Verfügung. Der Auslöser **Wurf oder Turnwechsel** aktualisiert eine Regel bei Würfen und neuen Aufnahmen, auch desselben Spielers. In der TUI unter Ereignisse → Auslöser auswählen; Headless-Konfigurationen verwenden `ThrowOrTurnChanged` (`PlayerChanged` bleibt der separate tatsächliche Spielerwechsel).


### Live display after each dart (PixelIt and AwtrixNG)

**One matrix for all players:** Create two rules: **After each dart** and **Player change**. Leave the player filter empty and target the same matrix in both rules. Enable **Replace template text** and enter, for example:

```text
{playername} {points-left} D{dart-number}
```

The display starts with the active player, updates after each dart and follows player changes. For a fast PixelIt display, set the pause after the step to 0.

**One matrix per player:** Use the same events and a fixed player number in each matrix's text, for example:

```text
{p1-playername} {p1-points-left} D{p1-darts-thrown}
```

Replace `p1` with `p2` on the second matrix, and so on. Numbers stay the same when the starting player changes. Leave the player filter empty to refresh values on every event. Target the appropriate matrix from each display step.

| Placeholder | Meaning |
| --- | --- |
| `{dart-score}` | Last dart score |
| `{dart-number}` | Dart number within the current visit (0–3) |
| `{darts-thrown}` | Darts thrown in the current leg |
| `{turn-score}` | Current visit score |
| `{points-left}` | Remaining score of the selected/active player |
| `{p1-points-left}`, `{p1-darts-thrown}` | Fixed values for player 1; likewise for p2 through p32 |

Corrections, undo and busts use the values reported by Autodarts. The TUI provides the same events and text fields. The **Throw or turn change** trigger updates on throws and new visits, including the same player. In the TUI, select it under Events → Trigger; headless configurations use `ThrowOrTurnChanged` (`PlayerChanged` remains the separate actual player change).

## GIF-Animationen / GIF animations

HubX-GIFs bis 32 × 8 Pixel können als animierte PixelIt-Vorlagen importiert werden. Originalgröße, Bilddauer und Farben bleiben erhalten. Wiederholung: 1–100 Durchläufe, bis zum nächsten Effekt oder bis zum nächsten Turn. Im Ereignisschritt kann die Vorlagenvorgabe überschrieben werden. Darts-Hub muss zur Wiedergabe laufen. [Anleitung und Grenzen](HubX-GIF-Import.md).

HubX GIFs up to 32 × 8 pixels can be imported as animated PixelIt templates. Original dimensions, frame timing and colors are preserved. Choose 1–100 plays, until the next effect or until the next turn; each event step can override the template settings. Darts-Hub must remain running. See [workflow and limits](HubX-GIF-Import.md).

## Zufällige Effektvarianten / Random effect variants

In der Ereignisregel „Zufällige Effektvariante“ aktivieren. Jeder Schritt hat eine
Variantenummer (1–64). Für einzelne Zufallseffekte jedem Schritt eine andere Nummer
geben. Für eine mehrteilige Variante mehreren Schritten dieselbe Nummer geben:
Diese Schritte laufen in ihrer Listenreihenfolge nacheinander. Neu hinzugefügte
Schritte bekommen bei aktivierter Zufallsauswahl automatisch die nächste Nummer.
Bestehende Schritte bleiben in Variante 1; ihre Zuordnung bewusst ändern.

Pro Auslösung wird genau eine Variante gewählt, gemeinsam für alle Zielgeräte.
Direkte Wiederholungen sind möglich. Ohne Zufallsauswahl laufen alle Schritte wie
bisher. Testsequenz und Echtbetrieb verwenden dieselbe Auswahl. Bei Pixelit darf
eine endlose Animation nur der letzte Schritt ihrer Variante am jeweiligen Gerät
sein. Speichern und Übernehmen ist wie gewohnt erforderlich.

TUI: Ereignis bearbeiten → „Zufällige Effektvariante“; beim Schritt die
Variantenummer einstellen. Weboberfläche/Webapp bieten dieselben Regel-/Schrittfelder.
HubX-Dateiimport, Teilen und Sicherungen behalten Auswahl und Variantenummern.
HubX zeigt in seiner Vorschau eine vollständige repräsentative Variante.

Enable **Random effect variant** in the event rule. Assign different **Variant
numbers** to alternatives; steps sharing a number play sequentially in list order.
New steps automatically receive the next number while random selection is enabled.
Existing steps remain in group 1. One variant is chosen per trigger for all target
devices; repeats are possible. Disable random selection to play the original full
sequence. Configure the same fields in the terminal or web editor, then save.
Sharing, file imports and backups preserve the settings. HubX previews show one
complete representative variant. Older Darts-Hub versions may reject these fields;
update the receiving installation before importing.


## GIF-Vorlagen ohne Text / Image-only GIF templates

Die GIF-Vorlage erzeugt ausschließlich Bildinhalt. Ereignistext, Platzhalter,
Textfragmente und Text-Zeichenbefehle werden für diese Vorlage unterdrückt, auch
bei bereits vorhandenen Regeln. Das gilt für Geräteausgabe und die gemeinsame
Vorschau in GUI, TUI und Web. Importierte Pixelit-GIF-Animationen bleiben ebenfalls
textfrei. HubX-Kopien behalten diese Eigenschaft bei einer Umbenennung; HubX zeigt
keinen Vorlagennamen oder Score als Ersatztext. Lade-/Dateifehler stehen außerhalb
der Matrix. Normale Textvorlagen bleiben unverändert. Kein neuer Schalter nötig.

GIF templates generate image content only. Event text, placeholders, fragments and
text drawing commands are suppressed, including in existing rules. Device output
and the shared GUI/TUI/web previews agree. Imported Pixelit GIF animations are also
textless. Renamed HubX copies retain their image-only intent; HubX does not invent
score/name fallback text. Loading/file diagnostics remain outside the matrix.
Ordinary text templates are unchanged. No additional setting is needed.

## Average / MPR

Deutsch: `{average}` ist der X01-Match-Average des auslösenden Spielers, `{leg-average}` der Leg-Average und `{set-average}` der Set-Average. Für Cricket/Tactics stehen `{mpr}` und `{leg-mpr}` zur Verfügung. Feste Spieler: `{p1-average}` bis `{p32-average}` (entsprechend auch die anderen Statistikvariablen). Die Nummern folgen der stabilen Match-Spielerzuordnung. Werte kommen direkt aus Autodarts, mit zwei Nachkommastellen und Dezimalpunkt. Nicht verfügbare Statistiken bleiben leer; Profil-Averages werden nicht verwendet.

English: `{average}` is the triggering player's X01 match average; `{leg-average}` and `{set-average}` select the leg/set. Cricket/Tactics provide `{mpr}` and `{leg-mpr}`. Fixed players use `{p1-average}` through `{p32-average}` (also for the other statistics). Player numbers follow the stable match assignment. Values come directly from Autodarts, formatted with two decimal places and a decimal point. Unavailable statistics remain empty; profile averages are never substituted.

DE: Anzeigevorlage `templates/average` auswählen, Textüberschreibung deaktivieren. EN: Select display template `templates/average` and disable the text override.
