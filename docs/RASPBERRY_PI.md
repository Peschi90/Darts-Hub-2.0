# Raspberry Pi / Raspberry Pi

## Deutsch

Für das Linux-ARM64-Paket wird ein **64-Bit-Betriebssystem mit glibc** benötigt, etwa ein passendes 64-Bit Raspberry Pi OS. Ein 64-Bit-fähiger Prozessor allein genügt nicht: ein installiertes 32-Bit-System ist kein unterstütztes Releaseziel. `uname -m` sollte `aarch64` oder `arm64` melden. Für die GUI wird zusätzlich eine grafische Sitzung benötigt.

1. Den [Online-Installer](ONLINE_INSTALLER.md) verwenden oder das Linux-ARM64-Paket vollständig entpacken. Standardordner: `~/dartshub`.
2. Im Programmordner `./DartsHub --tui` starten. Autodarts mit Board-ID und Browser-Anmeldecode verbinden; Erweiterungen konfigurieren und speichern.
3. Ohne Desktop `./DartsHub --headless` verwenden. Den Dienst-Autostart über [Autostart](AUTOSTART.md) einrichten. Die lokale Weboberfläche beziehungsweise gekoppelte Webapp dient zur Fernbedienung.
4. Caller-Soundpack installieren und auswählen. Für lokale Ausgabe das gewünschte Audiogerät in den Systemeinstellungen wählen und dort zunächst einen Ton testen. Falls keine Host-Ausgabe benötigt wird, lokale Wiedergabe im Caller ausschalten und **Audio hier aktivieren** im Browser-Dashboard verwenden.
5. `./DartsHub --update` aktualisiert die aktuelle Installation und erhält die Konfiguration. Bei eigenen Datenpfaden/Ports die vorhandenen Startargumente mitgeben. [System](SYSTEM.md) zeigt die tatsächlich verwendeten Ordner.

Linux-TTS ist kein allgemeiner Ersatz für fehlende Soundpacks. Ein per `systemd --user` gestarteter Dienst läuft im Benutzerkontext; Audiozugang und Sitzung müssen dazu passen. Browser-Audio benötigt keine Soundkarte am Pi, aber eine erreichbare Verbindung und die Freigabe am Browser. Gesperrte Smartphones können Audio trotzdem pausieren.

## English

The Linux ARM64 package requires a **64-bit glibc OS**. A capable CPU with a 32-bit OS is not enough. `uname -m` should report `aarch64` or `arm64`; the GUI additionally needs a desktop session. Install using the [online installer](ONLINE_INSTALLER.md) or extract the ARM64 package, then use `./DartsHub --tui` to configure it or `./DartsHub --headless` for background operation. See [autostart](AUTOSTART.md) for the user service.

Install/select a Caller soundpack. For local audio, select and test the audio device in OS settings; a user service needs access to the appropriate audio session. Alternatively disable local Caller playback and enable audio on the browser dashboard. Browser audio needs no Pi sound card, but requires an active connection and browser permission. Locked-screen playback is not guaranteed. Linux TTS is not a general replacement for soundpacks. Use `./DartsHub --update` for in-place updates, preserving custom startup arguments and data; check [System](SYSTEM.md) for actual storage paths.
