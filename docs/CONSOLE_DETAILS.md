# Console details / Konsolendetails

GUI, TUI and the web interface receive compact console summaries. Complete details are read from local logs when opening a row, searching details, copying or exporting. No external service is used.

The runtime keeps at most 5,000 summaries with a 24 MiB estimated managed-data budget, plus an 8 MiB pending-write buffer. A full buffer applies write backpressure instead of dropping details. GUI and TUI histories have a 32 MiB budget; the web history is limited to 2,000 entries and 32 MiB. Detail caches are limited to 4 MiB. These are data budgets, not a limit on total process memory. A large clipboard copy or export temporarily needs memory for its complete output.

The configured log directory contains `console-details/<session>.jsonl` and `<session>.idx`. References combine the session identifier and sequence number; the on-disk index records the exact byte offset. Fresh records are read from the pending buffer until persisted. Old companion files are cleaned up on startup after 31 days. Keep both files together when archiving logs. Existing plain text logs remain available.

Secrets are redacted before persistence. Device/licensing restrictions are checked again when reading details. Missing or damaged detail files cause an explicit error; a full-detail copy never silently overwrites the clipboard with partial data. Telemetry warnings/errors resolve their full details from the same store.

## Frontend actions

- GUI: select multiple rows, then right-click **Copy with details**. Selected rows are copied in timeline order. **Export** includes complete details.
- TUI: open Console, select a row for its details, or use the existing range/visible-copy and export actions. Complete text is displayed for terminal selection/copy. Detail searches use the same backend lookup.
- Web: open a row to load details; use selection copy or export for complete text. A loading indication accompanies asynchronous reads.

## Deutsch

Die Details werden bei Bedarf aus den lokalen Protokolldateien geladen. Mehrfachauswahl und vollständiger Export bleiben erhalten. Fehlende Dateien erzeugen eine Fehlermeldung; die Zwischenablage bleibt bei einer fehlgeschlagenen vollständigen Kopie unverändert. Große Kopien und Exporte benötigen vorübergehend Speicher für den gesamten Text. Die Speicherbudgets begrenzen die Konsolendaten, nicht den gesamten Arbeitsspeicher der Anwendung.
