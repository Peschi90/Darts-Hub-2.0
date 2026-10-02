# Startargumente / Startup arguments

## Deutsch

GUI, TUI und Headless teilen die gespeicherte Konfiguration. Nur angegebene Werte werden geändert und bleiben nach Neustarts erhalten.

1. Zur ersten Autodarts-Anmeldung die Board-ID einsetzen und im Programmordner starten:

| System | Befehl |
| --- | --- |
| Windows | `.\DartsHub.exe --headless --board-id "DEINE-BOARD-ID" --ad-login` |
| Linux | `./DartsHub --headless --board-id "DEINE-BOARD-ID" --ad-login` |
| macOS | `./DartsHub.app/Contents/MacOS/DartsHub --headless --board-id "DEINE-BOARD-ID" --ad-login` |

2. Den angezeigten Gerätecode auf der angegebenen Seite im Browser bestätigen. Danach ohne `--ad-login` starten; die gespeicherte Anmeldung wird wiederverwendet.
3. Optional `start.bat` (Windows) oder `start.sh` (Linux/macOS) anpassen und starten. Launcher überschreiben ihre angegebenen Vorgaben bei jedem Aufruf: Variablen prüfen und Geräteadressen anpassen.

| Option / Beispiel | Wirkung |
| --- | --- |
| `--tui` | Terminaloberfläche öffnen |
| `--headless` | Ohne Oberfläche starten |
| `--board-id "DEINE-BOARD-ID"` | Board-ID speichern |
| `--ad-login` | Geräteanmeldung starten |
| `--caller-enabled false --caller-tts-enabled false` | Caller und TTS ausschalten |
| `--wled-enabled true --wled-device HOST` | WLED aktivieren und Geräteadresse setzen |
| `--help` | Alle Optionen und Alternativen anzeigen |

- Boolesche Einstellungswerte ausdrücklich als `true` oder `false` angeben. Pfade mit Leerzeichen und Effekte mit `|` in Anführungszeichen setzen, z. B. `--caller-media-path "C:/Meine Sounds"`.
- **Strg+C** beendet den Terminalbetrieb sauber.
- Module: [Caller](CALLER_CONFIGURATION_AND_LOCALIZATION.md) · [WLED](WLED_CONFIGURATION_AND_AUTODARTS.md) · [PixelIt](PIXELIT.md) · [AWTRIX](AWTRIX.md) · [GIF](GIF.md)
- [Import](LEGACY_IMPORT.md) · [Eigene Anwendungen](OWN_APPLICATIONS.md) · [Telemetrie](TELEMETRY.md)

## English

GUI, TUI and headless share the saved configuration. Only supplied values change and remain saved across restarts.

1. For your first Autodarts login, insert your board ID and start from the program folder:

| System | Command |
| --- | --- |
| Windows | `.\DartsHub.exe --headless --board-id "YOUR-BOARD-ID" --ad-login` |
| Linux | `./DartsHub --headless --board-id "YOUR-BOARD-ID" --ad-login` |
| macOS | `./DartsHub.app/Contents/MacOS/DartsHub --headless --board-id "YOUR-BOARD-ID" --ad-login` |

2. Confirm the displayed device code on the indicated page in your browser. Afterwards, start without `--ad-login` to reuse the saved login.
3. Optionally edit and run `start.bat` (Windows) or `start.sh` (Linux/macOS). Launchers overwrite their supplied settings on every run: check variables and adjust device addresses.

| Option / example | Effect |
| --- | --- |
| `--tui` | Open the terminal interface |
| `--headless` | Start without a UI |
| `--board-id "YOUR-BOARD-ID"` | Save the board ID |
| `--ad-login` | Start device login |
| `--caller-enabled false --caller-tts-enabled false` | Disable Caller and TTS |
| `--wled-enabled true --wled-device HOST` | Enable WLED and set the device address |
| `--help` | Show all options and alternatives |

- Specify boolean setting values explicitly as `true` or `false`. Quote paths containing spaces and effects containing `|`, e.g. `--caller-media-path "C:/My Sounds"`.
- **Ctrl+C** cleanly stops terminal operation.
- Modules: [Caller](CALLER_CONFIGURATION_AND_LOCALIZATION.md) · [WLED](WLED_CONFIGURATION_AND_AUTODARTS.md) · [PixelIt](PIXELIT.md) · [AWTRIX](AWTRIX.md) · [GIF](GIF.md)
- [Import](LEGACY_IMPORT.md) · [Own applications](OWN_APPLICATIONS.md) · [Telemetry](TELEMETRY.md)
