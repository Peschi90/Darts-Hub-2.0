# Telemetrie / Telemetry

## Deutsch

### Auswahl und Umfang
- **Vor bestätigter Profilauswahl werden keine Telemetriedaten erhoben oder gesendet.**
- GUI: **Einstellungen → Datenschutz & Diagnose**; TUI: **Einstellungen / Lizenz → Datenschutz & Diagnose**.
- Vor der Auswahl den vollständigen, verbindlichen Datenschutzhinweis in der Oberfläche lesen.
  **Später entscheiden** bestätigt kein Profil; ohne vorherige Auswahl bleibt Telemetrie aus.
- **Minimal:** Modulnamen, Aktivierung und Versionen sowie eine zufällige, dauerhaft gespeicherte Installations-ID.
- **Voll / erweiterte Diagnose:** zusätzlich Betriebssystem, Nutzung, Ressourcen, effektive Einstellungen,
  Warnungen und Fehler einschließlich Meldungstext und Details sowie Lizenzstatus. Namen, Adressen,
  Pfade und freie Texte werden übertragen. Passwörter, E-Mail-Adressen und Authentifizierungsgeheimnisse
  werden maskiert; Autodarts-Rohnachrichten werden nicht erhoben.
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
  warnings and errors including message text and details, and license status. Names, addresses,
  paths and free text are transmitted. Passwords, email addresses and authentication secrets
  are masked; raw Autodarts messages are not collected.
- **Not anonymous:** The persistent ID can link telemetry to voluntary [support cases](SUPPORT.md).
  The receiving server also sees your connection IP as network metadata.

### Change your decision
- **Turning enhanced diagnostics off selects minimal, not an end to all transmissions.**
- Pending full reports are discarded and ongoing full transmissions aborted.
  Data already received cannot be recalled this way.
- Headless requires saved consent or both arguments below. Read the privacy notice first;
  GUI, TUI and headless use the same saved decision.

### Headless: Windows / Linux / macOS
`DartsHub.exe --headless --telemetry-profile minimal --telemetry-policy telemetry-v3`
Linux: `./DartsHub`; macOS: `./DartsHub.app/Contents/MacOS/DartsHub` statt `DartsHub.exe` / instead of `DartsHub.exe`.

Changed diagnostic scope requires a new confirmed choice (telemetry-v3) in GUI, TUI or headless mode.
Der erweiterte Diagnoseumfang erfordert eine neue bestätigte Auswahl (telemetry-v3) in GUI, TUI oder Headless.
