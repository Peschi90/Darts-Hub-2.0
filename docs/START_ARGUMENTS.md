# Startargumente / Startup arguments

## Deutsch

GUI, TUI und Headless teilen die gespeicherte Konfiguration. Nur angegebene Werte werden geÃ¤ndert und bleiben nach Neustarts erhalten.

1. Zur ersten Autodarts-Anmeldung die Board-ID einsetzen und im Programmordner starten:

| System | Befehl |
| --- | --- |
| Windows | `.\DartsHub.exe --headless --board-id "DEINE-BOARD-ID" --ad-login` |
| Linux | `./DartsHub --headless --board-id "DEINE-BOARD-ID" --ad-login` |
| macOS | `./DartsHub.app/Contents/MacOS/DartsHub --headless --board-id "DEINE-BOARD-ID" --ad-login` |

2. Den angezeigten GerÃ¤tecode auf der angegebenen Seite im Browser bestÃ¤tigen. Danach ohne `--ad-login` starten; die gespeicherte Anmeldung wird wiederverwendet.
3. Optional `start.bat` (Windows) oder `start.sh` (Linux/macOS) anpassen und starten. Launcher Ã¼berschreiben ihre angegebenen Vorgaben bei jedem Aufruf: Variablen prÃ¼fen und GerÃ¤teadressen anpassen.

| Option / Beispiel | Wirkung |
| --- | --- |
| `--tui` | TerminaloberflÃ¤che Ã¶ffnen |
| `--headless` | Ohne OberflÃ¤che starten |
| `--board-id "DEINE-BOARD-ID"` | Board-ID speichern |
| `--ad-login` | GerÃ¤teanmeldung starten |
| `--caller-enabled false --caller-tts-enabled false` | Caller und TTS ausschalten |
| `--wled-enabled true --wled-device HOST` | WLED aktivieren und GerÃ¤teadresse setzen |
| `--help` | Alle Optionen und Alternativen anzeigen |

- Boolesche Einstellungswerte ausdrÃ¼cklich als `true` oder `false` angeben. Pfade mit Leerzeichen und Effekte mit `|` in AnfÃ¼hrungszeichen setzen, z. B. `--caller-media-path "C:/Meine Sounds"`.
- **Strg+C** beendet den Terminalbetrieb sauber.
- Module: [Caller](CALLER_CONFIGURATION_AND_LOCALIZATION.md) Â· [WLED](WLED_CONFIGURATION_AND_AUTODARTS.md) Â· [PixelIt](PIXELIT.md) Â· [AWTRIX](AWTRIX.md) Â· [GIF](GIF.md)
- [Import](LEGACY_IMPORT.md) Â· [Eigene Anwendungen](OWN_APPLICATIONS.md) Â· [Telemetrie](TELEMETRY.md)

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
- Modules: [Caller](CALLER_CONFIGURATION_AND_LOCALIZATION.md) Â· [WLED](WLED_CONFIGURATION_AND_AUTODARTS.md) Â· [PixelIt](PIXELIT.md) Â· [AWTRIX](AWTRIX.md) Â· [GIF](GIF.md)
- [Import](LEGACY_IMPORT.md) Â· [Own applications](OWN_APPLICATIONS.md) Â· [Telemetry](TELEMETRY.md)

Die Anmeldung benÃ¶tigt nur die Board-ID und `--ad-login`. Interne Anmeldedaten sind fest in DartsHub hinterlegt und werden nicht als Startargument angegeben.

The login only requires the board ID and `--ad-login`. Internal authentication parameters are built into DartsHub and are not supplied as startup arguments.


## Terminal-Wartung / Terminal maintenance

- `--update [--yes] [--check-only] [--beta|--stable]`: aktuelle Installation aktualisieren und headless neu starten / update the current installation and restart headless.
- `--uninstall [--yes]`: Installation einschlieÃŸlich eigener Daten entfernen / remove the installation and its owned data.
- Bei eigenen Datenpfaden `--DartsHub:DataDirectory PATH`, beim Update bei Bedarf `--urls URL` mitgeben / supply custom data paths and update restart URLs explicitly.

Siehe README fÃ¼r RÃ¼ckfragen, Ablauf und LÃ¶schumfang / See README for confirmation, workflow and removal scope.

## Netzwerk-GUI / Network GUI

GUI: `DartsHub.exe bip=192.168.1.100` (auch als Argument im Ziel einer Windows-VerknÃ¼pfung).
TUI: `DartsHub.exe --tui bip=192.168.1.100`.
Linux/macOS: `./DartsHub bip=192.168.1.100` beziehungsweise `./DartsHub --tui bip=192.168.1.100`.
IPv6: `bip=2001:db8::1`. Keine Portangabe; verwendet wird HTTP-Port **5069**.

Auf dem Host: `DartsHub --headless --urls http://0.0.0.0:5069` und TCP 5069 im lokalen Netzwerk freigeben.
Bei `bip=` ist kein API-Token und keine Bestätigung erforderlich. GUI und TUI verwenden automatisch dieselbe Sitzung wie die lokale Weboberfläche. `bip=` hat Vorrang vor `DARTSHUB_API_URL`. Es startet auch bei einem unerreichbaren Host kein lokales Backend. Ohne Parameter bleibt der bisherige Start erhalten. Einstellungen und Dateipfade gehören zum Backendhost; der Parameter wird nicht als Konfiguration gespeichert.

Start the host with `DartsHub --headless --urls http://0.0.0.0:5069` and allow TCP 5069 on the LAN.
Append `bip=IPADDRESS` to the GUI command or shortcut target; use `--tui bip=IPADDRESS` for the terminal frontend.
No API token or confirmation is required with `bip=`: both frontends automatically use the existing local web session authentication.
IPv4 and IPv6 are supported without a port. This selects HTTP port **5069**, overrides `DARTSHUB_API_URL`, and never starts a local backend, even if the host is unreachable. Startup without this parameter keeps its existing behavior. Settings and file paths belong to the backend host; this argument is not persisted.

## Backend startet nicht / Backend startup failure

Bei „Backend offline“ die Ursache prüfen, bevor Einstellungen zurückgesetzt werden. GUI: **Einstellungen → Anwendung** zeigt bei einem lokalen Backend-Abbruch Ursache und Pfad der Datei `backend-failure.log`; im Autodarts-Bereich erscheint dieselbe Ursache. TUI: `DartsHub --tui` zeigt den Dateipfad bei einem Startfehler. Headless: `DartsHub --headless` zeigt den Fehler im Terminal.
Die Fehlerdatei liegt im Logordner (normalerweise `logs` im Installationsordner, bei einem Windows-Debugstart `%USERPROFILE%\DartsHub\logs`). Ist dieser nicht beschreibbar, wird der Benutzerordner `%LOCALAPPDATA%\DartsHub\logs` verwendet. Zugangsdaten werden geschwärzt. `--DartsHub:LogDirectory PFAD` setzt einen eigenen Logordner. Bei `bip=` befinden sich Backendfehler auf dem anderen Rechner.

When the GUI shows “Backend offline”, inspect the cause before resetting settings. GUI: **Settings → Application** shows the local backend failure and the path to `backend-failure.log`; the Autodarts area also shows the cause. TUI: `DartsHub --tui` prints the log path on startup failure. Headless: `DartsHub --headless` prints the error in the terminal.
The file is stored in the log directory (usually `logs` in the installation directory; Windows debug launches use `%USERPROFILE%\DartsHub\logs`). If writing fails, the user directory `%LOCALAPPDATA%\DartsHub\logs` is tried. Credentials are redacted. Set a custom directory with `--DartsHub:LogDirectory PATH`. With `bip=`, backend failures are on the other computer.
