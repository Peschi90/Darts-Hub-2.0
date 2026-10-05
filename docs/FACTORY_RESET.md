# Werkseinstellungen / Factory reset

## Deutsch

GUI: **Einstellungen → Allgemein → Werkseinstellungen** öffnen. Einzelne Module bzw. Einstellungsbereiche auswählen oder **Gesamte Anwendung zurücksetzen** aktivieren. **Umfang prüfen** zeigt die konkreten Folgen. Danach die Bestätigung aktivieren und **Jetzt zurücksetzen** wählen. Die Übernahme läuft mit Animation; die Einstellungen werden ohne Neustart angewendet.

TUI: **Einstellungen / Lizenz → Werkseinstellungen**, anschließend gesamte Anwendung oder einzelne Bereiche mit `[x]` markieren und **Umfang prüfen** wählen. Der separate Dialog zeigt denselben Umfang, dieselben Hinweise und eine Fortschrittsanimation. **Jetzt zurücksetzen** öffnet die ausdrückliche Bestätigung. Alle Bereiche der GUI sind auch im Terminal erreichbar.

- Zurückgesetzt werden die nativen Standardwerte der gewählten Module, einschließlich Geräte und Regeln. Beim WLED-Reset werden auch WLED-Aktionen beim Starten und Beenden entfernt.
- Der vollständige Reset umfasst Autodarts, Caller, WLED, PixelIt, Awtrix, GIF, eigene Anwendungen, Anwendungseinstellungen, Sprache, Datenschutzentscheidung und GUI-/Headless-Autostart.
- Autodarts wird getrennt und abgemeldet, die Board-Zuordnung gelöscht und die automatische Verbindung deaktiviert. Eine laufende Geräteanmeldung muss zuerst abgeschlossen oder abgebrochen werden.
- Eigene Anwendungen werden aus der Konfiguration entfernt. Von DartsHub verwaltete Prozesse werden gestoppt; Programmdateien bleiben erhalten.
- Lizenz, Installations-ID, installierte Soundpacks, Medien, Vorlagen, Protokolle und API-Authentifizierung bleiben erhalten. Geräte-Firmware und Geräteeinstellungen außerhalb DartsHub werden nicht verändert.
- Geänderte Einstellungen zwischen Vorschau und Bestätigung erfordern eine neue Vorschau. Schlägt die Übernahme fehl, wird der vorherige Konfigurationsstand wiederhergestellt. Fehler bei abschließender Abmeldung oder beim Entfernen von Autostart-Einträgen erscheinen ausdrücklich als Warnung nach dem gespeicherten Reset.

## English

GUI: **Settings → General → Factory settings**. Select individual modules/settings areas or **Reset the entire application**. **Review scope** lists the effects. Enable the confirmation and choose **Reset now**. The animated operation applies defaults without restarting.

TUI: **Settings / License → Factory settings**, then mark the entire application or individual settings areas with `[x]` and choose **Review scope**. A separate animated dialog displays the same scope and warnings. **Reset now** requests explicit confirmation. Every GUI reset area is available in the terminal.

Native module defaults replace selected options, devices and rules. WLED reset also clears startup/shutdown actions. Full reset covers all built-in modules, custom applications, application preferences, language, privacy choice and GUI/headless autostart. Autodarts disconnects and signs out, clears the board and disables automatic connection. Complete or cancel a pending device login first. Managed custom processes stop; their program files remain.

License, installation ID, installed soundpacks, media, templates, logs and API authentication are retained. Physical device firmware is unchanged. Changes after preview require another preview. Failed configuration application restores the previous configuration. Any post-commit sign-out or autostart cleanup failure is reported as a warning.

## Authenticated API / terminal integrations

Use the existing authenticated API token. First POST `/api/v1/settings/factory-reset/preview` with:

```json
{"targets":["wled"],"all":false}
```

Review the returned target labels/impact keys, then POST `/api/v1/settings/factory-reset/apply` with the returned token and explicit confirmation:

```json
{"targets":["wled"],"all":false,"previewToken":"TOKEN_FROM_PREVIEW","confirmed":true}
```

For the full reset use `"targets":[],"all":true` in both requests. Valid target IDs are returned by authenticated GET `/api/v1/settings/factory-reset/targets`. Multiple IDs are supported. Check the apply result's `warnings` even when the request succeeds. Reset does not start imported/custom programs or reactivate paid features.
