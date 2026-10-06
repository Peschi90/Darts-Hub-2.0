# PixelIt: Displays und Sequenzen / Displays and sequences

## Deutsch

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

Korrekturen, Zurücknehmen und Überwerfen verwenden die von Autodarts gemeldeten Werte. In der TUI stehen dieselben Ereignisse und Textfelder zur Verfügung. Der Auslöser **Wurf oder Spielerwechsel** aktualisiert eine Regel bei beiden Ereignissen. In der TUI unter Ereignisse → Auslöser auswählen; Headless-Konfigurationen verwenden `ThrowOrPlayerChanged` (oder einzeln `Throw` und `PlayerChanged`).


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

Corrections, undo and busts use the values reported by Autodarts. The TUI provides the same events and text fields. The **Throw or player change** trigger updates one rule for both events. In the TUI, select it under Events → Trigger; headless configurations use `ThrowOrPlayerChanged` (or separately `Throw` and `PlayerChanged`).
