# Installation / Installation

## Deutsch

1. Paket für dein Betriebssystem und deine Architektur (x64/ARM64) laden und vollständig entpacken.
2. Darts-Hub starten:

| System | Start |
| --- | --- |
| Windows | Doppelklick auf `DartsHub.exe` |
| Linux | `./DartsHub` (bei Bedarf zuvor `chmod +x DartsHub`) |
| macOS | Doppelklick auf `DartsHub.app` |

3. Unter **Autodarts** die Board-ID eingeben, Geräteanmeldung starten und den Gerätecode im Browser bestätigen.
4. Gewünschte Erweiterung einrichten und **Speichern** wählen.

- Keine separate .NET-Installation oder zusätzliche API-Anwendung nötig.
- Neue Windows-Installationen verwenden normalerweise `%USERPROFILE%\DartsHub`, Linux `~/dartshub`. Ältere Datenordner können weiterhin aktiv sein. Unter [System](SYSTEM.md) die echten Pfade prüfen. Updates aus der Anwendung oder mit `--update` erhalten Einstellungen und ersetzen die Installation am vorhandenen Ort; nicht manuell einen leeren Datenordner darüber kopieren.
- macOS kann unsignierte Downloads blockieren. Nur Anwendungen aus einer verlässlichen Quelle öffnen.
- [TUI / Headless](TUI.md) · [Startargumente](START_ARGUMENTS.md)

## English

1. Download the package for your operating system and architecture (x64/ARM64) and extract it completely.
2. Start Darts-Hub:

| System | Start |
| --- | --- |
| Windows | Double-click `DartsHub.exe` |
| Linux | `./DartsHub` (run `chmod +x DartsHub` first if needed) |
| macOS | Double-click `DartsHub.app` |

3. Under **Autodarts**, enter your board ID, start device login and confirm the device code in your browser.
4. Configure the desired extension and select **Save**.

- No separate .NET installation or additional API application is needed.
- New Windows installations normally use `%USERPROFILE%\DartsHub`; Linux uses `~/dartshub`. Legacy data folders may remain active. Check [System](SYSTEM.md) for actual paths. App updates or `--update` preserve settings and replace the current installation in place; do not copy an empty data folder over it.
- macOS may block unsigned downloads. Only open applications from a trusted source.
- [TUI / Headless](TUI.md) · [Startup arguments](START_ARGUMENTS.md)
