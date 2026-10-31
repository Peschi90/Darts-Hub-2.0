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
- GUI, TUI und Weboberfläche zeigen den tatsächlichen Logpfad: immer `logs` neben der gestarteten Programmdatei, unabhängig vom Arbeitsverzeichnis. Bei macOS-App-Bundles liegt er neben `DartsHub.app`. Kein Ausweichpfad nach AppData oder `.local`; ein Schreibfehler wird angezeigt. Frühere `DartsHub:LogDirectory`-Vorgaben werden nicht mehr verwendet.
- Pro lokalem Kalendertag gibt es ein Gesamtlog `DartsHub_04.log` und je Erweiterung z. B. `Caller/Caller_04.log`. Weitere Starts am selben Tag schreiben in dieselbe Datei. Das Gesamtlog bleibt für heute und die sechs vorherigen Kalendertage erhalten. Nur die Moduldateien behalten die bisherige Wiederverwendung im nächsten Monat. Konsolendetails und Indexdateien bleiben für heute und gestern verfügbar. Die Bereinigung läuft beim Start, beim Tageswechsel und auch ohne neue Meldungen spätestens nach einer Minute. Keine Rotation nach Dateigröße. Alte AppData-/`.local`-Ordner werden nicht mehr beschrieben, aber auch nicht automatisch mitsamt möglichen Einstellungen gelöscht.
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
- GUI, TUI and web control show the actual log path: always `logs` beside the launched executable, independently of the working directory. For macOS app bundles it is beside `DartsHub.app`. No AppData or `.local` fallback; write failures are reported. Previous `DartsHub:LogDirectory` overrides are no longer used.
- Each local calendar day has a combined log `DartsHub_04.log` and module logs such as `Caller/Caller_04.log`. Restarts append to the same file. Combined logs retain today and the preceding six calendar days. Only module logs retain the existing monthly day-slot reuse. Console details and index files retain today and yesterday. Cleanup runs at startup, on date changes and within one minute even when idle. File size remains unlimited. Old AppData/`.local` directories are no longer written, but are not automatically deleted along with any settings they may contain.
- Secrets are redacted, but your own text may still contain sensitive information.
  **Review exports before sharing.** Full Autodarts messages require the appropriate license.
