# Online-Installation / Online installation

## Deutsch

Der Installer erkennt Windows, Linux oder macOS und x64/ARM64. Er fragt nach stabiler oder Beta-Version, GUI/TUI/Headless, Installationsordner, Autostart und dem sofortigen Start. Installation und Autostart gelten für den angemeldeten Benutzer. Keine Administratorrechte bzw. kein `sudo` verwenden.

**Linux und macOS** – Terminal öffnen; `curl` und Python 3 müssen vorhanden sein:

```sh
curl -fsSL https://get.darts-hub.de/install.sh -o /tmp/dartshub-install.sh
sh /tmp/dartshub-install.sh
```

Auch als Einzeiler möglich:

```sh
curl -fsSL https://get.darts-hub.de | sh
```

**Windows** – PowerShell öffnen:

```powershell
irm https://get.darts-hub.de | iex
```

Falls ein Proxy die automatische Auswahl beeinflusst: `irm https://get.darts-hub.de/install.ps1 | iex`. Im Browser zeigt die Domain eine Installationsseite.

Der Installer fragt bei GUI und TUI zusätzlich, ob eine Desktop-Verknüpfung erstellt werden soll. Sie startet genau die gewählte Oberfläche. Bei einer Beta-Installation ist der Empfang von Beta-Updates automatisch aktiviert; du kannst ihn danach in GUI oder TUI wieder ausschalten. Der Windows-Installer legt außerdem einen Startmenüeintrag für die gewählte Betriebsart an. Unter Linux wird GUI-Autostart über die Desktop-Anmeldung eingerichtet, Headless über einen systemd-Benutzerdienst. Bei TUI-Autostart startet der Headless-Host; die TUI wird bei Bedarf mit `--tui` geöffnet. Unter macOS wird ein Benutzer-LaunchAgent eingerichtet. Diese Einträge verwenden dieselben Namen wie GUI und TUI und können dort verwaltet werden.

Ein Linux-Benutzerdienst startet normalerweise bei Anmeldung. Für Start ohne Anmeldung kann ein Administrator einmal `sudo loginctl enable-linger BENUTZERNAME` ausführen. Dafür verändert der Installer selbst keine Systemeinstellungen. Bei einem unsignierten macOS-Release kann die Freigabe unter Systemeinstellungen → Datenschutz & Sicherheit erforderlich sein.

Schließe DartsHub vor einer erneuten Installation. Der Installer ersetzt Programmdateien, behält lokale Einstellungen und Logs und prüft den Download vor dem Entpacken gegen den SHA256-Wert von GitHub. Bei einem Fehler wird kein ungeprüftes Programm gestartet. Autostart wird nur eingerichtet, wenn du zustimmst; vorhandene Autostart-Einträge werden bei „nein“ nicht verändert. Installiere neue Versionen in denselben Ordner, wenn bestehende Autostart-Einträge weiter darauf zeigen sollen.

Optionen: `sh /tmp/dartshub-install.sh --channel beta --mode headless --no-start` bzw. Windows `-Channel beta -Mode headless -NoStart`. Die übrigen Fragen bleiben interaktiv. Die Anmeldung bei Autodarts und die Erweiterungseinstellungen erledigst du danach in GUI/TUI oder mit Headless-Startargumenten.

Die URLs sind verfügbar, sobald get.darts-hub.de auf dem Webserver eingerichtet ist und die Installer im öffentlichen Repository veröffentlicht wurden. Unterstützt werden die sechs angebotenen x64-/ARM64-Pakete; keine 32-Bit-Systeme. Linux benötigt eine kompatible glibc-Distribution; Alpine/musl wird nicht unterstützt. Für die GUI müssen Desktop-Systembibliotheken vorhanden sein. Wenn Python 3 unter macOS fehlt, installiere es zunächst von python.org.

## English

Open a terminal and use the Linux/macOS or Windows commands above. The installer detects the OS and x64/ARM64 architecture and asks for stable/beta, GUI/TUI/headless, installation directory, login autostart and immediate launch. Run as a normal user. Linux/macOS require curl and Python 3; Windows requires PowerShell 5.1 or newer.

GUI starts at desktop login. Headless uses a Linux systemd user service, a macOS LaunchAgent or Windows user autostart. TUI autostart means starting the headless backend; launch `--tui` when you need to manage it. Linux boot without login requires an administrator to enable user lingering. macOS may require allowing an unsigned release in Privacy & Security.

Close DartsHub before reinstalling. Program files are replaced, settings/logs remain, and the download's SHA256 is checked before extraction. Existing autostart registrations remain unchanged when you decline autostart. Use the same installation directory to retain their paths. Optional flags are `--channel beta --mode headless --no-start` on Linux/macOS and `-Channel beta -Mode headless -NoStart` on Windows. Configuration and Autodarts login follow in GUI/TUI or through headless arguments.

Installer URLs become available after configuring get.darts-hub.de and publishing the installer files in the public repository. Only the six x64/ARM64 platform packages are supported; Linux requires glibc rather than Alpine/musl. GUI operation requires desktop libraries. Install Python 3 from python.org if it is missing on macOS.

For GUI and TUI, the installer also asks whether to create a desktop shortcut for the selected frontend. Installing a beta automatically enables beta updates; you can turn them off later in GUI or TUI.
