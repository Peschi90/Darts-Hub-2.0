# Telemetrie / Telemetry

## Deutsch

### Auswahl und Umfang
- **Vor bestätigter Profilauswahl werden keine Telemetriedaten erhoben oder gesendet.**
- GUI: **Einstellungen → Datenschutz & Diagnose**; TUI: **Einstellungen / Lizenz → Datenschutz & Diagnose**.
- Vor der Auswahl den vollständigen, verbindlichen Datenschutzhinweis in der Oberfläche lesen.
  **Später entscheiden** bestätigt kein Profil; ohne vorherige Auswahl bleibt Telemetrie aus.
- **Minimal:** Modulnamen, Aktivierung und Versionen sowie eine zufällige, dauerhaft gespeicherte Installations-ID.
- **Voll / erweiterte Diagnose:** zusätzlich Betriebssystem, Nutzung, Ressourcen, effektive Einstellungen,
  Fehlerdaten und Lizenzstatus. Adressen, Pfade und freie Texte werden maskiert;
  keine Zugangsdaten oder Autodarts-Rohnachrichten werden übertragen.
- **Nicht anonym:** Die dauerhafte ID kann Telemetrie mit freiwilligen [Supportfällen](SUPPORT.md) verknüpfen.
  Der empfangende Server sieht außerdem die Verbindungs-IP als Netzwerkmetadatum.

### Entscheidung ändern
- **Erweiterte Diagnose aus bedeutet Minimalprofil, nicht das Ende aller Übertragungen.**
- Ausstehende Vollberichte werden verworfen, laufende Vollübertragungen abgebrochen.
  Bereits empfangene Daten lassen sich dadurch nicht zurückholen.
- Headless benötigt eine gespeicherte Zustimmung oder beide Argumente im Beispiel unten.
  Den Datenschutzhinweis vorher lesen; GUI, TUI und Headless nutzen dieselbe gespeicherte Entscheidung.

## English

### Choice and scope
- **No telemetry is collected or sent before a profile selection is confirmed.**
- GUI: **Settings → Privacy & diagnostics**; TUI: **Settings / License → Privacy & diagnostics**.
- Read the full, binding privacy notice in the interface before choosing.
  **Decide later** confirms no profile; without a previous choice, telemetry remains inactive.
- **Minimal:** module names, enabled state and versions, plus a random, persistent installation ID.
- **Full / enhanced diagnostics:** additionally OS, usage, resources, effective settings,
  error data and license status. Addresses, paths and free text are masked;
  no credentials or raw Autodarts messages are transmitted.
- **Not anonymous:** The persistent ID can link telemetry to voluntary [support cases](SUPPORT.md).
  The receiving server also sees your connection IP as network metadata.

### Change your decision
- **Turning enhanced diagnostics off selects minimal, not an end to all transmissions.**
- Pending full reports are discarded and ongoing full transmissions aborted.
  Data already received cannot be recalled this way.
- Headless requires saved consent or both arguments below. Read the privacy notice first;
  GUI, TUI and headless use the same saved decision.

### Headless: Windows / Linux / macOS
`DartsHub.exe --headless --telemetry-profile minimal --telemetry-policy telemetry-v2`
Linux: `./DartsHub`; macOS: `./DartsHub.app/Contents/MacOS/DartsHub` statt `DartsHub.exe` / instead of `DartsHub.exe`.
