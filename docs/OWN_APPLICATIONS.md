# Eigene Anwendungen / Own applications

## Deutsch

### Einrichten und bedienen
1. **Eigene Anwendungen → Anwendung hinzufügen** öffnen; Namen vergeben und Programm/Skript auswählen.
2. Bei Bedarf Argumente und Arbeitsordner eintragen. Argumente mit Leerzeichen in Anführungszeichen setzen,
   nicht das Feld für die Programmdatei.
3. Unter **Verhalten und Diagnose** bei Bedarf **Aktiviert** und **Mit DartsHub starten** wählen.
4. **Speichern und anwenden** speichert die Einstellungen. Geänderte laufende Anwendungen werden beendet
   und bei aktiviertem Autostart neu gestartet; unveränderte Anwendungen laufen weiter.
5. Im Dashboard **Starten**, **Beenden** oder **Neu starten** verwenden.
   TUI: **Enter** öffnet Einträge zum Bearbeiten bzw. die Aktionen in der Übersicht.

### Beenden und Sicherheit
- **GUI schließen beendet alle von DartsHub gestarteten eigenen Anwendungen samt Unterprozessen**,
  auch wenn ein verbundener Headless-Host weiterläuft.
- TUI schließen lässt Anwendungen laufen, wenn der Headless-Host weiterläuft; Host beenden stoppt sie.
- Headless nutzt dieselben gespeicherten Einstellungen. Nur vertrauenswürdige Programme verwenden:
  Sie laufen mit den Rechten des DartsHub-Benutzers. Python-/PowerShell-Skripte benötigen den jeweiligen Interpreter.
- Aufgezeichnete Ausgaben: **Konsole → Prozessverwaltung**, Log-Unterordner `ProcessManager`.

## English

### Set up and control
1. Open **Own applications → Add application**; enter a name and select the program or script.
2. Add arguments and a working directory if needed. Quote arguments containing spaces,
   not the program file field.
3. Under **Behaviour and diagnostics**, select **Enabled** and **Start with DartsHub** as needed.
4. **Save and apply** persists settings. Changed running applications are stopped and restarted
   if autostart is enabled; unchanged applications keep running.
5. Use **Start**, **Stop** or **Restart** in the dashboard.
   TUI: **Enter** opens entries for editing or actions in the overview.

### Shutdown and safety
- **Closing the GUI stops all own applications started by DartsHub, including child processes**,
  even if a connected headless host remains running.
- Closing the TUI leaves applications running if the headless host continues; exiting the host stops them.
- Headless uses the same saved settings. Only run trusted programs: they use the DartsHub user's permissions.
  Python and PowerShell scripts require their respective interpreter.
- Captured output: **Console → Process Manager**, log subfolder `ProcessManager`.
