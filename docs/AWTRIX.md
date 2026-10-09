# AwtrixNG

## Deutsch

Voraussetzung: **AwtrixNG-Firmware** und verbundenes Board unter **Autodarts**. Der Caller darf ausgeschaltet sein.

1. **AwtrixNG → Geräte** öffnen, Erweiterung aktivieren und Display mit Adresse hinzufügen. Falls nötig, HTTP-Benutzer und Passwort eintragen.
2. Gerät mit **Prüfen / neu laden** prüfen.
3. Unter **Ereignisse** eine Regel anlegen: Auslöser wählen, bei Bedarf Spieler/Punktzahl einschränken.
4. Schritt hinzufügen, Vorlage und Zielgeräte wählen; Text, Icon und Dauer einstellen. `{score}` und `{playername}` setzen Spielwerte ein. Mehrere Schritte laufen nacheinander.
5. **Testen**, anschließend **Speichern**. Tests steuern das Display, speichern aber nichts.

- **Dauer** ist in Sekunden. Im automatischen Ausgabemodus bleibt bei Dauer **0** eine App aktiv; automatische App-Wechsel am Display können sie trotzdem ausblenden.
- **Display-Einstellungen:** Nur Werte aktivieren, die DartsHub auf dem Display ändern soll.
- **Gerätesteuerung:** Display ein/aus, Bildschirm wechseln. Löschen, Zurücksetzen und Firmware-Uploads nur bewusst verwenden.
- Ein leeres Passwortfeld behält das gespeicherte Passwort; zum Entfernen die entsprechende Option wählen.

TUI: Seite **AwtrixNG**, **Enter** zum Bearbeiten. Headless nutzt die gespeicherten Einstellungen; [Startargumente](START_ARGUMENTS.md).

## English

Requires **AwtrixNG firmware** and a connected board under **Autodarts**. Caller may stay disabled.

1. Open **AwtrixNG → Devices**, enable the extension and add the display address. Enter HTTP credentials if required.
2. Use **Check / reload** to check the device.
3. Under **Events**, add a rule with a trigger and optional player/score filter.
4. Add a step, select a template and target devices, then set text, icon and duration. `{score}` and `{playername}` insert game values. Steps run in order.
5. **Test**, then **Save**. Tests control the display but do not save settings.

- Duration is in seconds. In automatic output mode, **0** keeps an app active; automatic app switching can still hide it.
- Enable only **Display settings** you want DartsHub to change.
- **Device control** provides power, screen switching and stopping audio. Use deletion, reset and firmware uploads with care.
- An empty password field keeps the saved password; use the clear option to remove it.

TUI: **AwtrixNG**, **Enter** to edit. Headless uses saved settings; [startup arguments](START_ARGUMENTS.md).

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
