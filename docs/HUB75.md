# Hub75

## Deutsch

Hub75 ist ein eigenes Modul für WLED-HUB75-Matrixdisplays. Geräte, Aktivierung,
Ereignisse und Betriebsoptionen werden unabhängig vom WLED-Modul gespeichert.
Beide verwenden dieselben Ereignisregeln, Text-/Scoreanzeigen und Lizenzprüfungen.
Ein Gerät sollte nur in einem aktiven Modul eingetragen sein.

In der GUI **Hub75 → Geräte & Einrichtung → Gerät hinzufügen** öffnen und
**Geführt einrichten** oder **Manuell hinzufügen** wählen. Erst diese Auswahl
legt ein neues Gerät an. Manuell Name und IP eintragen und **Verbindung prüfen**
wählen. Bereits eingerichtete Geräte
benötigen keinen Flashvorgang. **Einstellungen vom Display übernehmen** lädt Panelwerte
in den Entwurf. **Konfiguration speichern** speichert den Entwurf in Darts-Hub;
**Auf Display übertragen & prüfen** verändert nach Bestätigung den Controller.
Die Rücklesung prüft Panelwerte und Gesamtgröße. Segment 0 erhält die neuen
Grenzen. Andere Geräteeinstellungen bleiben erhalten. Eigene Mehrfachausgänge
oder mehrere logische 2D-Panels werden ausdrücklich abgelehnt.

Die Geräteübersicht zeigt den Anzeigemodus **MatrixMind** oder **Ereignisregeln**.
Unter **Betriebsoptionen** wählst du ein Gerät und aktivierst eigene Werte nach
Bedarf. Jedes andere Feld übernimmt den Modulstandard. Helligkeit, Effektdauer,
High-Finish-Schwelle und Ruhezeiten gelten im Ereignismodus. MatrixMind hat
eigene Anzeigeeinstellungen. Der Verbindungs-Timeout gilt pro Controller.

Zum Ändern der Panelgröße zuerst **MatrixMind ausschalten & speichern**, falls es
für dieses Gerät aktiv ist. Dann Größe und Anordnung bearbeiten, das
Neustart-Kontrollkästchen markieren und **Auf Display übertragen & prüfen** wählen.
Fortschritt, fehlende Bestätigung und Fehler stehen direkt unter dem Knopf.
Warte die Rücklesung ab und speichere anschließend die Konfiguration in Darts-Hub.
Ein Neustart kann die HTTP-Antwort unterbrechen; Darts-Hub prüft dann die Werte
erneut, ohne den Konfigurationsbefehl nochmals zu senden. Im Terminal dieselbe
Reihenfolge verwenden und den Neustart im Bestätigungsdialog freigeben.

Jeder Schritt zeigt drei kurze Anweisungen. Die aktuelle Station ist oben
markiert; **Weiter: …** steht nach den passenden Eingaben. **Technische Details
& Hilfe** enthält zusätzliche Hinweise und die USB-Fehlersuche.
Der erste Schritt markiert die Hardwareanforderung und zeigt den Affiliate-Link
beim Controllerfoto. Der Assistent ist für den gezeigten ESP32-S3 N16R8 ausgelegt.
Prüfe vor dem Flashen 16 MB Flash und 8 MB Octal-PSRAM. Verkabelung und Panelanordnung werden als
beschriftete Schemata gezeichnet. Die Anordnung folgt dem aktuellen Entwurf;
sie erkennt keine Kabel. Signal- und Strompfade sind getrennt beschriftet.

Der optionale Einrichtungsassistent führt durch sechs Schritte:

1. **Controller prüfen:** ESP32-S3 mit 16 MB QSPI-Flash und mindestens 8 MB
   Octal-PSRAM (typisch N16R8). Das Foto eines Boards mit zwei USB-Buchsen reicht
   zur Speicherbestimmung nicht aus. Aufdruck und Händlerdaten prüfen.
2. **Verdrahten:** Strom abschalten. Panel separat aus passendem 5-V-Netzteil
   versorgen, gemeinsame Masse verbinden. Keine Panelversorgung über ESP32/USB.
   Netzteil, Leitungen und Sicherung nach Paneldatenblatt; WLEDs Strombegrenzer
   erfasst HUB75 nicht. Bei Bedarf geeignete 3,3-V-/5-V-Pegelwandler verwenden.
   ESP32 an Panel IN, weitere Panels von OUT nach IN verketten.
3. **Flashen:** Python 3.10+ mit venv/pip auf dem Hub-Rechner bereitstellen,
   **USB-Werkzeuge einrichten**, Ports laden und den nativen USB-/OTG-Port wählen.
   Bei Bedarf BOOT halten, RESET drücken, BOOT loslassen. Die Firmware verwendet
   USB-CDC. Das Boardprofil und vollständige Löschen müssen bestätigt werden.
   Darts-Hub prüft ESP32-S3/16 MB und schreibt Bootloader, Partitionstabelle und
   Firmware mit esptool 5.1.0. Anschließend RESET und Ports erneut laden.
   Bei bereits installierter passender Firmware die Überspringen-Option wählen.
4. **WLAN:** 2,4-GHz-SSID und Passwort eingeben. Improv Serial meldet die IP.
   Passwörter gehen über die Prozesseingabe und werden weder in Konfiguration,
   Prozessargumenten noch Diagnoseausgaben gespeichert. Alternativ WLED-AP
   (Standardpasswort `wled1234`) verbinden, `http://4.3.2.1` öffnen und unter
   WiFi Settings einrichten. Danach Heimnetz wieder verbinden und Geräte-IP
   aus Router/WLED eintragen. **Verbindung prüfen und weiter** prüft Erreichbarkeit
   und Firmwareversion. Nach erfolgreicher USB-WLAN-Einrichtung geschieht dies
   automatisch; bei fehlender Netzwerkverbindung bleibt der Assistent im WLAN-Schritt.
5. **Matrix:** Einzelpanelgröße, Reihen, Spalten und Half-/Quarter-Scan wählen.
   Unterstützte Einzelgrößen: 32×32, 64×32, 64×64, 128×64. Anzahl = Reihen ×
   Spalten, maximal vier Panels in WLED 16.0.1. Diese Hub-Version unterstützt
   insgesamt höchstens 256×128 und 16384 Pixel. Die physische Anordnung steht
   im HUB75-Ausgang; 2D bleibt **ein** flaches Panel in Gesamtgröße. Bei mehreren
   Reihen wird die Kette gefaltet und jede zweite Reihe um 180° montiert.
   Startkante, vertikale Richtung und Serpentinenmapping betreffen die logische
   Orientierung. Änderungen anwenden und Rücklesung abwarten.
6. **Prüfen:** **Speichern und Ereignisse einrichten** speichert das Gerät und
   öffnet den Ereigniseditor. Der Abschluss setzt eine geprüfte Verbindung und
   gelesene oder angewendete Matrixwerte voraus. Änderungen an Adresse oder
   Panelwerten erfordern eine erneute Prüfung. Modul nach Wunsch aktivieren.

Das **Matrix-Livebild** empfängt bis zum Stoppen fortlaufend neue Controllerframes.
Es zeigt einen Empfangszähler; ein Verbindungsfehler entfernt das letzte Bild.
Geräte-/Adresswechsel, Tabwechsel und Verlassen der Ansicht beenden den Stream.
Für große Matrizen benötigt die Firmware vollständige Pixelübertragung, zum Beispiel
über DHLive1. Reduzierte Bilder zeigen stattdessen einen Hinweis. Der Stream funktioniert über die authentifizierte
Host-/LAN-API, nicht über das Webrelay.

[GUI-Einrichtung mit Beispieldaten, kein angeschlossener Controller](images/user-guide/hub75-setup-de.png)
[Auswahl zwischen Assistent und manueller Einrichtung](images/user-guide/hub75-add-de.png)
[Boardfoto und nummerierte Anleitung](images/user-guide/hub75-board-de.png)

### Verdrahtung des gewählten Firmwareprofils

Die Nummern beziehen sich auf die Signalpositionen am HUB75-Eingang; Kabelansicht
und Einbaurichtung können spiegelverkehrt sein. Pin 1 und IN am Panel prüfen.
Das Profil verwendet `MOONHUB_S3_PINOUT`, nicht die klassische ESP32-Belegung.

| HUB75-Pin | Signal | ESP32-S3 GPIO |
|---|---|---|
| 1 | R1 | 1 |
| 2 | G1 | 5 |
| 3 | B1 | 6 |
| 4 | GND | GND |
| 5 | R2 | 7 |
| 6 | G2 | 13 |
| 7 | B2 | 9 |
| 8 | E / GND | 38 nur für E, sonst GND |
| 9 | A | 16 |
| 10 | B | 48 |
| 11 | C | 47 |
| 12 | D / GND | 21 nur für D, sonst GND |
| 13 | CLK | 18 |
| 14 | LAT | 8 |
| 15 | OE | 4 |
| 16 | GND | GND |

E wird typischerweise für 64 Zeilen benötigt. D/GND und E/GND stets nach der
Panelbeschriftung und dem Datenblatt verbinden. Pins sind im Build festgelegt.

### Terminal und Plattformen

`DartsHub --tui` starten und **Hub75** wählen. Dort gibt es dieselben Aktionen:
Geräte/Ereignisse/Optionen bearbeiten, Assistent, Verdrahtung, Geräteprüfung,
Panelentwurf lesen/bearbeiten/speichern/anwenden, Livebild, USB-Werkzeuge,
Portauswahl, Flashen, WLAN und Abbrechen. Fortschritt und IP stammen vom Backend.
**Gerät hinzufügen → Geführt einrichten** startet denselben geprüften Ablauf;
**Manuell hinzufügen** öffnet Name/IP direkt. Der letzte Schritt öffnet die
Ereignisregeln nach dem Speichern. Das Livefenster aktualisiert sich fortlaufend;
**Stoppen** oder **Schließen** beendet die Verbindung.
**Anleitung zu diesem Schritt lesen** öffnet dieselben nummerierten Anweisungen
einschließlich der technischen Hinweise. **Deine Panelanordnung · Schema**
zeigt die Verkabelungsreihenfolge als Textgrafik. Die GPIO-Liste verwendet
dieselben Signalpositionen wie die GUI.
Der Abbruch verwendet die ID des laufenden Vorgangs. Beim Abbruch während des
Flashens anschließend über BOOT/RESET neu flashen.

USB gehört zum Hub-Rechner und ist nur für seine authentifizierten lokalen
GUI-/TUI-Sitzungen freigegeben. Browser-/Relay-Sitzungen dürfen nicht auf Host-USB
zugreifen. Windows, Linux und macOS verwenden denselben eingebetteten Python-
Helfer und eine eigene virtuelle Umgebung; unter Linux sind serielle
Benutzerrechte nötig. Es gibt keine automatische Installation eines Python-
Interpreters. Ein COM-Port auf einem entfernten GUI-Rechner wird nicht benutzt.
Die mobile App bietet noch keinen Hub75-Assistenten; ihre bestehenden
Konfigurations- und Sicherungswege behalten unbekannte Felder bei.

Firmware ist bewusst auf die geprüfte Version
`WLED_16.0.1_ESP32-S3_16MB_opi_HUB75.bin` festgelegt. Alle drei Downloads haben
festgelegte SHA-256-Werte. Bootloader (QSPI/QIO; **OPI bezeichnet hier PSRAM**)
und 16-MB-Partitionstabelle kommen aus einem festen Commit des offiziellen
Webinstallers. Der Firmware-Download allein ist kein vollständiges Factory-Image:
Bootloader wird bei `0x0`, Partitionstabelle bei `0x8000`, Anwendung bei `0x10000`
geschrieben. Vollständiges Löschen entfernt auch WLAN, Presets und Einstellungen.
Vorher eigene WLED-Sicherungen erstellen. Gesperrte WLED-Einstellungen müssen
mit der Geräte-PIN im WLED-Webinterface entsperrt werden; Darts-Hub umgeht das nicht.

Hub75 ist ein neues v2-Modul ohne v1-Aliase. Legacy-WLED-Importe bleiben WLED;
bestehende Hub75-Konfigurationen werden nicht daraus erzeugt oder überschrieben.
Hub75 ist in Modulschaltern, Teil-/Gesamtsicherungen, Supportpaketen und Zurücksetzen enthalten.
Sicherungen enthalten Hub-Konfigurationen, kein ESP32-Flashabbild oder WLAN-Passwort.

## English

To resize panels, first **Deactivate MatrixMind & save** if it is active for this
controller. Edit size and arrangement, tick the restart confirmation and select
**Apply to display & verify**. Progress and errors appear beside that button.
Wait for verification, then save the configuration in Darts-Hub. A restart may
close HTTP before the acknowledgement; Darts-Hub reads back the settings without
resending the configuration write. In `DartsHub --tui` → **Hub75**, follow the same
sequence and approve the restart in the confirmation dialog.


Hub75 is an independent module for WLED HUB75 displays, sharing WLED event,
text/score and licensing logic. Open **Hub75 → Devices & setup → Add device** and
choose **Guided setup** or **Add manually**. The choice creates the device.
For manual setup, enter its address and test it. Existing controllers do not require flashing.
**Read settings from display** loads a draft. **Save configuration** saves it in Darts-Hub;
**Apply to display & verify** explicitly writes to the controller, resizes
segment 0 and verifies readback. Other settings are preserved. Multiple outputs
and custom multi-panel logical 2D maps are rejected rather than overwritten.

The device overview shows the **MatrixMind** or **Event rules** display mode.
In **Runtime options**, select a device and override individual values. Other
fields inherit the module defaults. Brightness, effect duration, high finish
threshold and sleep timers apply in event mode. MatrixMind has its own display
settings. The connection timeout applies per controller.

Each step provides three short instructions and highlights the current stage.
**Next: …** follows the relevant controls. **Technical details & help** expands
additional information and USB troubleshooting. The first step highlights the
hardware requirement and shows a labelled affiliate link beside the photo.
The guide is designed for the pictured ESP32-S3 N16R8. Check for 16 MB flash
and 8 MB octal PSRAM before flashing. Labelled schematics show
wiring and the current draft layout; they do not detect cables. Signal and
power paths are labelled separately.

The optional six-step wizard covers controller identification, wiring, USB
flashing, Wi-Fi, matrix layout and verification. Existing matching firmware can
be explicitly skipped. Wi-Fi must pass a connection/version check; the matrix
must be read or applied and verified. Changing its address or panel settings
requires another check. **Save and configure events** saves and opens the event
editor directly. It targets an ESP32-S3 with
16 MB QSPI flash and at least 8 MB octal PSRAM (typically N16R8). Check the marking
and supplier specification; the board photograph does not establish memory size.
The GPIO table above is the fixed MOONHUB S3 mapping for the selected firmware.
Check pin 1/IN and the panel datasheet for E/GND and D/GND. Power panels separately
from a suitable 5 V supply with common ground, correctly sized wiring and fuse;
never power panels through ESP32/USB. WLED's current limiter does not cover HUB75.

Install Python 3.10+ with venv/pip on the host, then select **Set up USB tools**.
Darts-Hub installs esptool 5.1.0 in its own environment. Use a USB data cable and
the native USB/OTG connector (USB CDC). Hold BOOT, press RESET and release BOOT
if necessary. Select the correct port and confirm both board profile and full
erasure. After installation press RESET and refresh ports, which may have changed.
Firmware, bootloader and partition table are hash-checked; chip/flash size and
the written data are verified. The application image alone is insufficient for
a fresh board. Flashing erases credentials, presets and settings; back up WLED
first. Firmware is pinned to the exact official 16.0.1 asset listed above.

Wi-Fi setup uses Improv Serial at 115200 baud with a 2.4 GHz SSID. The returned IP
is shown; passwords are ephemeral and never placed in command arguments, stored
configuration or diagnostics. Fallback: join WLED-AP (`wled1234` by default), visit
`http://4.3.2.1`, save WiFi Settings, rejoin the home network and enter its new IP.

Set single-panel dimensions (32×32, 64×32, 64×64 or 128×64), columns, rows and
Half/Quarter Scan. WLED 16.0.1 supports at most four chained panels. This Hub
version supports total dimensions up to 256×128 / 16384 pixels. Physical layout
belongs to the HUB75 output; the 2D layer uses one flat panel at the total size.
Fold multi-row chains and rotate alternate physical rows 180°. The orientation
options affect logical mapping. Apply, verify, then configure events and enable
and save the module. Do not control the same device from both active modules.

**Live matrix** continuously receives controller frames until stopped. Its counter
reports received frames; errors clear the last image. Switching devices, addresses,
tabs or leaving the view cancels it. Large matrices require full pixel transmission
by firmware such as DHLive1; reduced images show a message instead. Streaming uses the authenticated host/LAN
API and is unavailable through the web relay.

[GUI setup with sample data, no controller connected](images/user-guide/hub75-setup-en.png)
[Choose guided or manual setup](images/user-guide/hub75-add-en.png)
[Board photo and numbered instructions](images/user-guide/hub75-board-en.png)

Run `DartsHub --tui` and select **Hub75** for all equivalent actions, the same
wizard text, progress and cancellation. **Add device → Guided setup** uses the same verified workflow;
**Add manually** opens name/address fields. The final step saves and opens event
rules. The live window refreshes continuously until **Stop** or **Close**.
**Read instructions for this step** opens the same numbered instructions and
technical notes. **Your panel layout · schematic** shows cable order as a text
diagram, and the GPIO list uses the same signal positions as the GUI.
USB works only in local authenticated
native GUI/TUI sessions on the host. Browser/relay sessions cannot access it.
Windows/Linux/macOS use the same embedded helper; Linux requires serial-port
permissions. Python itself must already be installed. The mobile app does not
yet provide a Hub75 wizard; existing editing/backup paths preserve unknown data.
Device PIN protection is respected. Hub75 settings participate in module switches,
backups, support packages and reset; backups are not controller flash images. There are no legacy
v1 Hub75 aliases, and legacy WLED imports stay in WLED.

## Sources / Quellen

- [Official WLED 16.0.1 release](https://github.com/wled/WLED/releases/tag/v16.0.1)
- [HUB75 configuration and wiring](https://kno.wled.ge/advanced/HUB75/)
- [Versioned HUB75 implementation and MOONHUB GPIOs](https://github.com/wled/WLED/blob/v16.0.1/wled00/bus_manager.cpp)
- [Versioned board profile](https://github.com/wled/WLED/blob/v16.0.1/platformio.ini)
- [WLED serial / Improv](https://kno.wled.ge/interfaces/serial/)
- [Pinned official boot images](https://github.com/wled/WLED-WebInstaller/tree/cb540fdf7380d8fc7ac9de0835d028cbbb1bef26/bin/boot)
- [esptool installation](https://docs.espressif.com/projects/esptool/en/latest/esp32/installation.html)

Der GUI-Assistent öffnet sich in einem eigenen modalen Dialog. Nur der aktuelle Schritt scrollt; Zurück und Weiter bleiben erreichbar. Schließen erhält den Geräteentwurf. Während einer laufenden USB-Aktion bleibt der Dialog offen; dort kann die Aktion abgebrochen werden. Die TUI verwendet weiterhin ihre eigene Schrittansicht mit denselben Aktionen und Prüfungen.

The GUI wizard opens in a dedicated modal dialog. Only the current step scrolls; Back and Next stay visible. Closing preserves the device draft. During a USB operation the dialog stays open and provides cancellation. The TUI retains its separate step view with the same actions and validation.

## MatrixMind

Das eigene Scoreboard mit Originalanimationen von BernyBoneBreaker, direkten Websocket-Spieldaten und der Geräte-GIF-Bibliothek ist unter [MatrixMind](MATRIXMIND.md) beschrieben (Deutsch / English).

## Livebild: Controllergröße und Vorschau / Live view resolution

Das Livebild zeigt jeden Controllerpixel für GIFs, WLED-Effekte und MatrixMind.
Die Standardfirmware WLED 16.0.1 sendet für 64×32 jedoch nur 32×16 Bildpunkte.
Solche reduzierten Bilder werden nicht mehr angezeigt; GUI und TUI erklären die
benötigte Firmware-Erweiterung. Auch eine unbekannte Auflösung wird nicht als
vollständig ausgegeben. Kleine Matrizen mit vollständigem Standard-Peek bleiben
kompatibel. [DHLive1-Build und Installation](../scripts/wled-full-preview/README.md).
Für ESP32-S3 mit 16 MB Flash und Octal-PSRAM ist ein gesonderter Build vorbereitet.
Er wird nicht automatisch geflasht; der USB-Assistent nutzt weiterhin die offizielle
Firmware. Bis zu zehn volle Bilder pro Sekunde, ohne Änderung der Effekte oder GIFs.
**MatrixMind-Ausgabe in voller Auflösung öffnen** wechselt zur berechneten
Geräte-Vorschau. Diese zeigt die vollständigen Rendererbilder, keine Bestätigung
des Controllerempfangs. Terminal: `DartsHub --tui` → Hub75 → Gerät → Matrix-Livebild;
für die berechnete Ausgabe Gerät · MatrixMind → MatrixMind-Vorschau.

Live view shows every controller pixel for GIFs, WLED effects and MatrixMind.
Stock WLED 16.0.1 sends only 32×16 samples for 64×32. These reduced frames are no
longer displayed; GUI and TUI explain the required firmware extension. Unknown
resolution is not presented as complete. Small matrices with full stock Peek remain
compatible. [DHLive1 build and installation](../scripts/wled-full-preview/README.md).
A separate build is prepared for ESP32-S3 with 16 MB flash and octal PSRAM. It is
not flashed automatically; the USB wizard still uses official firmware. Up to ten
full frames per second, without changing effects or GIF playback.
**Open full-resolution MatrixMind output** switches to the rendered device preview.
It shows complete renderer frames, not controller delivery acknowledgement.
Terminal: `DartsHub --tui` → Hub75 → device → matrix live view; for rendered output,
use device · MatrixMind → MatrixMind preview.

Firmware reference: [WLED 16.0.1 live sampling](https://github.com/wled/WLED/blob/v16.0.1/wled00/ws.cpp).

## MatrixMind starten / Starting MatrixMind

**Hub75 → MatrixMind** ist in **Einrichten**, **Darstellung** und **Ausgabe & Test**
gegliedert. Gerät und Panelanzahl wählen; **MatrixMind aktivieren & speichern**
prüft den Controller und schaltet Modul, Gerät und MatrixMind gemeinsam ein.
**Speichern & auf dem Panel testen** übernimmt die gewählte Darstellung vor dem
Test. Bildschirm-Beispielvorschau und laufende Ausgabe bleiben getrennt.
Im Terminal: **Hub75 → Gerät · MatrixMind → Einrichten**; dieselben Aktivierungs-,
Test- und Deaktivierungsaktionen stehen dort bereit. [Details](MATRIXMIND.md).

**Hub75 → MatrixMind** separates **Setup**, **Appearance** and **Output & test**.
Choose a device and matching panel count; **Activate MatrixMind & save** checks the
controller and enables module, device and MatrixMind together. **Save & test on the
panel** applies the chosen appearance before testing. Sample previews and current
output remain separate. Terminal: **Hub75 → device · MatrixMind → Setup**, with the
same activation, test and deactivation actions. [Details](MATRIXMIND.md).

### Übertragungsfehler / Transfer failures

GUI und TUI unterscheiden nicht erreichbare Controller von abgelehnten Anfragen,
fehlenden Konfigurationsaufrufen (404/405), zu großen Anfragen (413), internen
Controllerfehlern (5xx) und ungültigen Antworten. Die Konsole protokolliert Methode,
Pfad und HTTP-Status, keine Konfigurationsinhalte oder WLAN-Daten. Erfolgreiches
`GET json/info` bestätigt Erreichbarkeit, aber noch keine erfolgreiche Übertragung.
Die Konfigurations- und Segmentbefehle werden mit bekannter Anfragelänge gesendet,
wie es der WLED-JSON-Empfänger benötigt.

GUI and TUI distinguish unreachable controllers from rejected requests, missing
configuration endpoints (404/405), oversized requests (413), controller errors
(5xx), and invalid responses. The console records method, path, and HTTP status,
never configuration bodies or Wi-Fi data. A successful `GET json/info` confirms
reachability, not a successful configuration transfer. Configuration and segment
commands use a known request length as required by WLED's JSON receiver.


## Ereignismodus und HubX-Layouts

1. In **Hub75 → MatrixMind** prüfen, welches Panel MatrixMind steuert. Für das Zielpanel MatrixMind deaktivieren und speichern, wenn du stattdessen Ereignisse anzeigen möchtest. **Alle Geräte** erreicht nur Panels im Ereignismodus. Alte Zuweisungen zu MatrixMind-Panels bleiben gespeichert und pausieren.
2. Unter **Hub75 → Ereignisregeln** einen Auslöser und eine Ausgabe wählen. Der WLED-Effektkatalog kommt vom Controller. Die angebotenen Ausgaben sind Matrixeffekt (einschließlich WLED-Laufschrift), animierter Matrixtext, GIF vom Controller und HubX-Layout.
3. Für ein eigenes Layout **HubX Studio → Hub75-Layout gestalten** öffnen. Die Auflösung muss dem Panel entsprechen. Ebenen lassen sich positionieren, anordnen, einfärben und mit Schriftgröße sowie Texteffekt versehen. Balken nutzen Werte von 0 bis 100. Die Vorschau verwendet Beispieldaten.
4. Ein HubX-Paket herunterladen oder veröffentlichen und senden. Im **HubX-Posteingang** Zielpanel und bei Vorlagen den Auslöser auswählen. Alternativ lässt sich die lokale **Layoutdatei** direkt in einer Aktion vom Typ **HubX-Layout** öffnen. Text und Balken können Platzhalter wie **{playername}**, **{score}** oder **{points-left}** enthalten. Die Werte kommen beim Auslösen aus Autodarts.
5. Im Terminal: **DartsHub --tui → Hub75 → Konfiguration bearbeiten → Rules**. Für die Datei unter **Effects → HubX-Layout → Layout** den Dateipfad angeben. Über **Layout → Text bearbeiten** wählst du den Platzhalter einer Ebene. Die HubX-Importprüfung steht auch im Terminal und in der lokalen Weboberfläche zur Verfügung.

## Event mode and HubX layouts

1. Open **Hub75 → MatrixMind** to see which panel MatrixMind controls. Disable MatrixMind for the target panel and save if you want it to show event rules. **All devices** targets panels in event mode. Existing assignments to MatrixMind panels are kept and paused.
2. Under **Hub75 → Event rules**, choose a trigger and output. The WLED controller supplies its effect catalog. Options include a matrix effect (including WLED scrolling text), animated matrix text, a device GIF, or a HubX layout.
3. Open **HubX Studio → Design a HUB75 layout**. Match the panel resolution. Position, reorder and color layers, then choose text scale and motion. Bars accept values from 0 to 100. The preview uses sample data.
4. Download a HubX package, or publish and send it. Choose the panel in the **HubX inbox**. For a template, also choose a trigger. An editable layout file can also be opened directly in a **HubX layout** action. Text and bars can use placeholders such as **{playername}**, **{score}** and **{points-left}**. Autodarts supplies the values when the rule triggers.
5. In the terminal, use **DartsHub --tui → Hub75 → Edit configuration → Rules**. Open **Effects → HubX layout → Layout** to enter the file path and **Layout → Edit text** to edit a layer’s placeholders. HubX review is also available in the terminal and local web interface.


In HubX Studio steht **Vorlage oder Ereignis** über dem Layout. Bei einem Ereignis wählst du den Auslöser, seine Bedingungen und die Anzeigedauer. Die Vorschau bleibt bei ungültigen Maßen sichtbar und nennt die betroffene Ebene. **Ebenen an Matrix anpassen** ändert den Entwurf erst beim Klick. Animierte Hintergründe können eine Palette und ein Tempo haben. Textebenen bieten Pixelschriften und Formatierung. Darts-Hub verwendet diese Einstellungen für die Ausgabe.

Teile in der GUI über **Hub75 → Ereignisregeln → Auf HubX teilen**. Im Terminal verwende **DartsHub --tui → Hub75 → Auf HubX teilen**. Bei GIF-Regeln wird die Datei vom ausgewählten Zielcontroller gelesen. Im Prüfbericht stehen die mitgelieferten Dateien. HubX führt das GIF zusätzlich in der GIF-Kategorie.

In Studio, **Template or event** is above the layout. Events store their trigger, conditions and display duration. Invalid dimensions retain the last valid preview and identify the affected layer. **Fit layers to matrix** applies the changes explicitly. Animated backgrounds have a palette and speed. Text layers offer pixel fonts and formatting. Darts-Hub renders these settings on the panel.

Share from **Hub75 → Event rules → Share on HubX** in the GUI, or **DartsHub --tui → Hub75 → Share on HubX** in the terminal. GIF rules read the file from the selected target controller. Review lists the bundled files. HubX also lists the GIF in its GIF category.


Jede Ebene hat unter **Aussehen der Ebene** einen Pixeleffekt, eine Palette, Tempo, Dichte und Deckkraft. Partikeleffekte lassen die Bereiche zwischen den Partikeln transparent. Setze eine Fläche unter die Partikelebene, wenn du dort eine feste Hintergrundfarbe möchtest. Text bietet zusätzlich Schrift, Formatierung und Zeichenabstand. Die Vorschau berücksichtigt den Platz für Schrägschrift, dickere Striche und die separate Unterstreichung.

Darts-Hub sendet **HubX-Layouts und berechneten Matrixtext per DDP** (UDP 4048). Auf dem Controller muss der Empfang von Echtzeitdaten aktiviert sein. **GIF vom Controller** und Firmwareeffekte bleiben WLED-Befehle. Beim Wechsel beendet Darts-Hub den DDP-Strom, bevor WLED das ausgewählte GIF lokal abspielt. Der Test in GUI und Terminal verwendet dieselbe Ausgabe wie die Ereignisregel.

Every layer has a pixel effect, palette, speed, density and opacity under **Layer appearance**. Particle effects leave the spaces between particles transparent. Add a fill below the particle layer for a solid backdrop. Text also supports font, formatting and letter spacing. The preview accounts for slant, thicker strokes and a separate underline.

Darts-Hub sends **HubX layouts and rendered matrix text over DDP** (UDP 4048). Enable realtime reception on the controller. **Device GIFs** and firmware effects remain WLED commands. Darts-Hub stops streaming before WLED plays the selected GIF locally. GUI and terminal tests use the same output path as the rule.

### Chalkboard als Live-Spielstand

Wähle im HubX Studio die Pixelgröße des Controllers und verwende **Live-Spielstand (Chalkboard)** als Ereignis. Für Vorlagen kannst du den Auslöser beim Import wählen. Darts-Hub aktualisiert das Layout bei einem veränderten Spielstand und zeigt es nach zeitbegrenzten Ereigniseffekten wieder an. Das Zielpanel muss im Ereignismodus sein. Bei abweichender Auflösung nennt die Übernahme die Größen von Layout und Controller.

Die Platzhalterliste unterscheidet Spielwerte, den Spieler des Ereignisses und feste Spielerpositionen. Verwende zum Beispiel {current-player}, {leg}, {set}, {p1-playername}, {p1-points-left}, {p2-legs}, {p2-dart-1}, {p2-checkout} oder {p2-visit-2}. Die Aufnahmehistorie reicht von {p1-visit-1} bis {p1-visit-10}, entsprechend für p2 bis p6. Die jüngste Aufnahme steht an erster Stelle, einschließlich der laufenden Aufnahme ab dem ersten Dart. Darts-Hub sammelt beobachtete Aufnahmen pro Spieler während des aktuellen Legs. Beim Spielerwechsel bleibt die letzte Aufnahme sichtbar, bis eine neue beginnt. Ein Bust ergibt 0 Punkte. Die Positionen p1 bis p6 bleiben bei wechselnder Wurfreihenfolge stabil. Fehlende Daten bleiben leer. Die Checkout-Wege kommen vom Spielstand und die Vorschau zeigt Beispieldaten.

In der GUI findest du die Auswahl in **Hub75 → Ereignisregeln → HubX-Layout** unter der Textebene. Der Fokus im Feld markiert seinen Bereich im Vorschaubild. Im Terminal öffnest du **DartsHub --tui → Hub75 → Konfiguration bearbeiten → Rules → Effects → Layout → Text bearbeiten**. Nach der Feldwahl zeigen ein Rahmen und Pixelkoordinaten die Position.

### Chalkboard as a live scoreboard

Set the controller resolution in HubX Studio and select **Live scoreboard (chalkboard)** as the event. For a template, select the trigger during import. Darts-Hub refreshes the layout when match data changes and restores it after timed effects. The panel must use event mode. If the resolutions differ, the import shows the layout and controller sizes.

Placeholders cover match details, the event player and fixed slots. Examples include {current-player}, {leg}, {set}, {p1-playername}, {p1-points-left}, {p2-legs}, {p2-dart-1}, {p2-checkout} and {p2-visit-2}. Visit history runs from {p1-visit-1} to {p1-visit-10}, and likewise for p2 through p6. The most recent visit comes first, including the current visit once its first dart is recorded. Darts-Hub collects observed visits per player during the current leg. When the active player changes, each player’s latest visit stays visible until their next visit begins. A bust counts as zero. Slots p1 to p6 remain stable when throwing order changes. Unavailable data is blank. Checkout routes come from match data and previews use samples.

In the GUI, open **Hub75 → Event rules → HubX layout** and choose a placeholder for a text layer. Focusing a field outlines its area in the preview. In the terminal, use **DartsHub --tui → Hub75 → Edit configuration → Rules → Effects → Layout → Edit text**. Selecting a field shows its outline and pixel coordinates.

### Gedrehte Matrix beim Import

Für ein Layout mit 32 × 192 Pixeln und einen Controller mit 192 × 32 Pixeln wähle im HubX-Importdialog unter **Displayausrichtung** die passende 90°-Drehrichtung. Beim Bestätigen übernimmt WLED die gedrehte logische Zuordnung und startet neu. Die physische Panelgröße, Verkabelung und Reihenfolge bleiben gleich. Die Drehrichtung beschreibt die Drehung der logischen Koordinaten. Die Panels müssen entsprechend montiert sein. WLED benötigt **Respect LED maps** für die DDP-Ausgabe. Aktive Regeln mit inkompatiblen Layouts verhindern die Drehung.

Im Terminal unter **HubX → Posteingang → Daten übernehmen** nach dem Zielgerät die Drehrichtung wählen. Die lokale Weboberfläche hat dieselbe Auswahl. **Hub75 → Geräte & Einrichtung → Scanart & Bildausrichtung** zeigt die logischen Achsen in der Gerätekonfiguration an.

### Rotated matrix on import

For a 32 × 192 layout and a controller reporting 192 × 32, choose the required 90° rotation in **Display orientation** during HubX review. Confirmation updates the logical mapping and restarts WLED. Physical panel size, wiring and order stay the same. The direction describes rotation of the logical coordinates. Mount the panels accordingly. WLED needs **Respect LED maps** for DDP output. Active rules with incompatible layouts prevent rotation.

In the terminal, open **HubX → Inbox → Accept** and choose the direction after choosing the target. The local web interface offers the same choice. **Hub75 → Devices & setup → Scan type & orientation** shows the logical axes in the device configuration.

Die Hub75-Helligkeit reicht von 1 bis 150. Das gilt für die Betriebsoptionen und die gerätespezifische Helligkeit in der GUI und im Terminal. Ältere höhere Werte werden beim Laden auf 150 gesetzt.

HUB75 brightness ranges from 1 to 150. This applies to the runtime default and device overrides in the GUI and terminal. Older values above 150 are lowered when loaded.


### HubX

Im Kopfbereich öffnen **HubX · Effekte entdecken** und **Auf HubX teilen** die Hub75-Ereignisse. Import, Lizenzprüfung und Übernahmebestätigung verwenden den bestehenden HubX-Ablauf. Im Terminal: Hub75 → HubX · Effekte entdecken bzw. Auf HubX teilen.

The header offers **HubX · Discover effects** and **Share on HubX** for Hub75 events, using the existing licensed import and review workflow. Terminal: Hub75 → Discover effects / Share on HubX.
