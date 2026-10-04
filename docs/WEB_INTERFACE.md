# Darts-Hub im Browser / Darts-Hub in your browser

## Deutsch

![Web-Dashboard](images/web/dashboard.de.png)

Die Bilder zeigen einen lokalen Testbetrieb mit abweichendem Port. Im normalen Betrieb verwendest du Port 8079.

Darts-Hub stellt automatisch eine Weboberfläche bereit, sobald die Anwendung läuft. Das gilt für die GUI und für `--headless`; du brauchst keinen zusätzlichen Webserver.

1. Starte Darts-Hub auf dem Rechner, der deine Erweiterungen steuern soll.
2. Öffne auf einem Gerät im selben Netzwerk `http://IP-DES-RECHNERS:8079`, beispielsweise `http://192.168.1.100:8079`.
3. Gib den **Web-Zugangscode** ein. Du findest ihn in der GUI unter **Einstellungen / Lizenz → Weboberfläche**, in der TUI unter **Einstellungen → Weboberfläche** oder beim Headless-Start im Terminal. Dieser Code ist unabhängig von der Autodarts-Anmeldung.
4. Wähle im Seitenmenü die gewünschte Erweiterung. Bearbeite ihre Einstellungen und drücke **Speichern**. Dashboard-Schalter wirken sofort.

Die Weboberfläche bietet Autodarts-Anmeldung und Board-Auswahl, Caller und Soundpacks, WLED, PixelIt, AwtrixNG, GIF, eigene Anwendungen, Konsole, Lizenz, allgemeine Einstellungen, Import, Telemetrie und Support. Die gemeinsamen Einstellungen werden auf dem Darts-Hub-Rechner gespeichert und gelten auch für GUI und TUI. Speichere deine Änderungen, bevor du in einer anderen Oberfläche weiterarbeitest; mit **Neu laden** holst du den gespeicherten Stand.

Farben, Karten, Logo und das einklappbare Seitenmenü folgen der GUI. Auf schmalen Bildschirmen bleibt das Menü als Symbolleiste sichtbar. PixelIt und AwtrixNG haben eine Live-Matrixvorschau mit Beispielwerten; **Am Gerät testen** sendet die aktuelle Regel an die eingerichteten Geräte. WLED nutzt den vorhandenen Controller-Katalog. **Gerät laden / testen** aktualisiert diesen bewusst.

In der Konsole kannst du mit Strg-Klick mehrere Meldungen oder mit Umschalt-Klick einen Bereich auswählen. Rechtsklick bietet **Meldungen kopieren** oder **Mit Details kopieren**. Debug ist zunächst ausgeblendet. Die bestehende Lizenzregel für vollständige WebSocket-Payloads gilt weiterhin.

Die erste Sprache folgt der Betriebssystemsprache des Darts-Hub-Rechners: Deutsch, sonst Englisch. Eine später gewählte Sprache wird gespeichert. Fenster, Monitorwahl und GUI-Autostart sind bewusst der Desktop-GUI vorbehalten. Ein Headless-Host kann im Browser für den Autostart eingerichtet und beendet werden.

Dateipfade und gestartete Skripte beziehen sich auf den Darts-Hub-Rechner. Caller-Vorschauen werden dort abgespielt. Support-ZIP-Dateien können im Browser heruntergeladen werden; ein Upload erfolgt erst über **Senden** nach Bestätigung. Die Update-Suche wartet auf das Ende der Startverzögerung und zeigt formatierte Release Notes.

Der Zugangscode bleibt nach Neustarts erhalten. **Zugangscode erneuern** in GUI oder TUI sperrt vorhandene Browser-Anmeldungen und beendet ihre Web-Verbindungen. Browser-Sitzungen laufen nach acht Stunden ab. **Abmelden** beendet die Anmeldung auf diesem Browser; der Host läuft weiter. Beim Schließen der GUI endet auch deren Webserver. Ein als Service eingerichteter Headless-Host bleibt nach dem Schließen der TUI aktiv.

Falls ein anderer Rechner die Seite nicht erreicht, prüfe die IP-Adresse und erlaube eingehende TCP-Verbindungen auf Port **8079** in der Firewall für dein lokales Netzwerk. Die Webseite verwendet im lokalen Netzwerk HTTP; richte dafür keine Internet-Portweiterleitung ein. Bei mehreren Hosts auf demselben Rechner kann der Port mit `--DartsHub:WebPort 8080` geändert werden; `0` deaktiviert den zusätzlichen Netzwerk-Port. Die lokale API auf Port 5069 bleibt bestehen.

## English

![Web dashboard](images/web/dashboard.en.png)

Screenshots show a local test host using a different port. Normal installations use port 8079.

Darts-Hub automatically serves its web interface while the application is running, both with the desktop GUI and with `--headless`. No separate web server is needed.

1. Start Darts-Hub on the computer that controls your extensions.
2. From a device on the same network, open `http://HOST-IP:8079`, for example `http://192.168.1.100:8079`.
3. Enter the **web access code**. Find it in the GUI under **Settings / License → Web interface**, in the TUI under **Settings → Web interface**, or in the terminal when starting headless. This code is separate from Autodarts authentication.
4. Select an extension in the sidebar, adjust its settings and click **Save**. Dashboard switches apply immediately.

The web interface includes Autodarts login and board selection, Caller and soundpacks, WLED, PixelIt, AwtrixNG, GIF, external applications, console, licensing, application settings, legacy import, telemetry and support. Shared settings are saved on the host and also apply to the GUI and TUI. Save before switching frontends; **Reload** retrieves the latest saved configuration.

Colors, cards, logo and collapsible navigation follow the desktop GUI. Narrow screens use icon navigation. PixelIt and AwtrixNG provide live matrix previews with example values. **Test on device** sends the current rule to the configured devices. WLED uses its loaded controller catalog; **Load / test device** explicitly refreshes it.

Use Ctrl-click to select console messages or Shift-click to select a range. Right-click offers **Copy messages** and **Copy with details**. Debug output is initially hidden. Existing license restrictions on full WebSocket payloads continue to apply.

The initial language follows the host operating system: German or otherwise English. A manually selected language is saved. Window positioning, monitor selection and GUI autostart stay in the desktop application. A headless host can be configured for autostart and stopped through the web interface.

File paths and scripts refer to the host computer. Caller previews play there. Download support ZIPs in your browser; upload only starts after choosing **Send** and confirming. Update checks wait until the startup countdown finishes and show formatted release notes.

The access code survives restarts. **Renew access code** in the GUI or TUI revokes existing browser sessions and ends their web connections. Sessions expire after eight hours. **Sign out** leaves the host running. Closing the GUI also stops its web server. A headless service continues running after you close the TUI.

If another device cannot reach the page, check the host IP and permit incoming TCP traffic on **8079** in your firewall for your local network. The local interface uses HTTP; do not forward this port to the internet. Multiple hosts on one computer can use `--DartsHub:WebPort 8080`; `0` disables the additional network listener. The existing local API remains on port 5069.
