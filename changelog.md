# Changelog – Darts-Hub 2.0

## v0.1.0-beta.5

### Deutsch

- Linux-Caller erkennt ffplay, paplay und aplay automatisch und wählt den Player passend zum Dateiformat; ARM-Architekturen und 32-Bit-Benutzerbereiche werden korrekt erkannt. Der gesamte Soundpack-Bibliothekskopf ist klickbar.
- Neue Versionen werden in einem Update-Dialog mit Release Notes angekündigt; die TUI zeigt dieselben Versionshinweise.
- Einheitlicher Installer-Header mit ASCII-Monogramm, Dart-Motiv und klaren Installationsabschnitten.
- Optionale GUI-/TUI-Desktop-Verknüpfungen im Installer; Beta-Installationen aktivieren Beta-Updates automatisch. Headless-Autostart wird nur noch in der TUI angeboten.
- Windows-Online-Installer startet auch über `irm | iex`; Installer-Dateien werden zusätzlich als öffentliche Release-Downloads veröffentlicht.
- Gemeinsame Installationsadresse get.darts-hub.de mit automatischer Skriptauswahl und Browser-Anleitung.
- Online-Installer erkennt Betriebssystem und Architektur und bietet GUI, TUI, Headless, Beta-Versionen und Autostart an.
- Autodarts-Anmeldung mit gespeicherter Verbindung und direkten Spielereignissen.
- Caller, WLED, PixelIt, AwtrixNG und GIF mit Einstellungen in GUI, TUI und Headless.
- Eigene Anwendungen und Skripte starten gemeinsam mit DartsHub und werden beim Beenden geschlossen.
- Startverzögerung hält Module, eigene Autostart-Anwendungen und Updateprüfung zurück.
- Getrennte Erweiterungslogs, Support-Diagnose und Import alter Konfigurationen.
- Kompakte Betriebssystem-Pakete ohne Dokumentationsdateien; Updates kommen aus dem öffentlichen Release-Repository.

### English

- Linux caller detects ffplay, paplay and aplay automatically and selects a player matching the file format; ARM architectures and 32-bit userspace are detected correctly. The entire soundpack-library header is clickable.
- New versions are announced in an update dialog with release notes; the TUI exposes the same notes.
- Unified installer header with ASCII monogram, dart artwork and clear installation stages.
- Optional GUI/TUI desktop shortcuts in the installer; beta installations enable beta updates automatically. Headless autostart is offered only in the TUI.
- Windows online installer works through `irm | iex`; installer scripts are also published as public release downloads.
- Shared get.darts-hub.de installation URL with automatic script selection and browser instructions.
- Online installer detects OS and architecture and offers GUI, TUI, headless, beta releases and login autostart.
- Persistent Autodarts login and direct match events.
- Caller, WLED, PixelIt, AwtrixNG and GIF configuration through GUI, TUI and headless operation.
- Custom applications and scripts start with DartsHub and close when it exits.
- Startup countdown delays modules, custom startup applications and update checks.
- Separate extension logs, support diagnostics and legacy configuration import.
- Compact platform packages without documentation; updates use the public release repository.
