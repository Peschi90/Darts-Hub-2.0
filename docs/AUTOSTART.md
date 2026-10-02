# Autostart / Background operation

## Deutsch

1. GUI: **Einstellungen → Autostart** öffnen, **GUI beim Anmelden starten** und optional **Minimiert starten** aktivieren, dann **Übernehmen**.
2. Nach dem Verschieben der Anwendung den Autostart erneut **Übernehmen**.
3. Für Hintergrundbetrieb in der TUI unter **Einstellungen / Lizenz** den **Headless-Autostart / Dienst** aktivieren. Der Host läuft nach dem Schließen der TUI weiter.
4. **Headless beenden** stoppt den aktuellen Host; die Autostart-Registrierung bleibt bestehen. Für keine weiteren automatischen Starts zuerst Autostart deaktivieren, dann den Host beenden.

Linux: Der Benutzerdienst startet normalerweise bei der Anmeldung. Optional kann ein Administrator den Start beim Booten ohne Anmeldung mit `sudo loginctl enable-linger "$USER"` erlauben; ein systemd-Benutzerdienst muss verfügbar sein.
Status prüfen: `systemctl --user status dartshub.service`.

## English

1. GUI: open **Settings → Autostart**, enable **Start GUI at login** and optionally **Start minimized**, then **Apply**.
2. **Apply** autostart again after moving the application.
3. For background operation, enable **Headless autostart / service** under **Settings / License** in the TUI. The host keeps running after closing the TUI.
4. **Stop headless** stops the current host but keeps its autostart registration. To prevent future automatic starts, disable autostart first, then stop the host.

Linux: The user service normally starts at login. Optionally, an administrator can allow startup at boot without login using `sudo loginctl enable-linger "$USER"`; a systemd user service must be available.
Check status: `systemctl --user status dartshub.service`.
