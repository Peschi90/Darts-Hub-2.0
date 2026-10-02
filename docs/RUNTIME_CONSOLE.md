# Runtime-Konsole / Runtime console

## Deutsch

### Meldungen finden
1. **Konsole** in GUI oder TUI öffnen.
2. Über die Suche filtern. In der GUI zusätzlich Erweiterung und Mindest-Level wählen.
3. Eine Zeile auswählen, um Zeit, Quelle, Nachricht und Details zu lesen.
4. Bei Problemen **Debug** für die betroffene Erweiterung einblenden;
   das zeigt zusätzliche Diagnosemeldungen, ohne die Modulkonfiguration zu ändern.
5. **Ansicht pausieren** (TUI: **Pausieren**) hält nur die Anzeige an. Module und Logdateien laufen weiter.
6. Gefilterte Zeilen exportieren: GUI **Ansicht als .log speichern**, TUI **Gefilterte Konsole als .log exportieren**.
   Nur GUI: **Gesamten Puffer speichern** exportiert auch ausgeblendete Meldungen im geladenen Puffer.

### Dateien und Datenschutz
- GUI und TUI zeigen den tatsächlichen Logpfad. Standard: `logs` neben der ausführbaren Anwendung.
- Logdateien werden 14 Tage aufbewahrt; ältere Meldungen können dort noch vorhanden sein.
- Geheimnisse werden geschwärzt, eigene Texte können dennoch sensible Angaben enthalten.
  **Export vor dem Teilen prüfen.** Vollständige Autodarts-Nachrichten benötigen die passende Lizenz.

## English

### Find messages
1. Open **Console** in the GUI or TUI.
2. Use search to filter messages. In the GUI, also select an extension and minimum level.
3. Select a row to read its time, source, message and details.
4. For troubleshooting, show **Debug** for the affected extension;
   this reveals additional diagnostics without changing module settings.
5. **Pause view** (TUI: **Pause**) pauses only the display. Modules and log files continue running.
6. Export filtered rows: GUI **Save view as .log**, TUI **Export filtered console as .log**.
   GUI only: **Save entire buffer** also exports hidden messages within the loaded buffer.

### Files and privacy
- GUI and TUI show the actual log path. Default: `logs` beside the executable.
- Log files are retained for 14 days; older messages may still be available there.
- Secrets are redacted, but your own text may still contain sensitive information.
  **Review exports before sharing.** Full Autodarts messages require the appropriate license.
