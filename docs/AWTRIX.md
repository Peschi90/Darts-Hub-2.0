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
- **Gerätesteuerung:** Display ein/aus, Bildschirm wechseln oder Ton stoppen. Löschen, Zurücksetzen und Firmware-Uploads nur bewusst verwenden.
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
