# Robbel3D One-Click

## Deutsch

In der GUI unter **WLED → Robbel3D One-Click** öffnen. Die Einrichtung verwendet
die ursprüngliche Robbel3D-Konfiguration mit 145 LEDs und sechs benannten Presets.
Sie ist im Programm enthalten; zusätzliche Konfigurationsdateien sind nicht nötig.

1. Konfiguration und WLED-Adresse auswählen. Für die Gerätesuche eine lokale
   IPv4-Adresse eingeben; die Suche prüft das zugehörige /24-Netz. Hostnamen und
   HTTPS-Adressen können direkt eingegeben werden.
2. Den GPIO des angeschlossenen LED-Rings wählen. Die vorhandene Board-ID und
   der Soundpack-Ordner werden vorgeschlagen. Der Medienordner muss auf dem
   Rechner vorhanden sein, auf dem die DartsHub-Runtime läuft.
3. **Prüfen und Vorschau anzeigen** wählen. Die Liste zeigt die übernommenen
   Einstellungen und auch alte Optionen, die im neuen Hub entfallen. Alte
   Caller-Serverports und Zertifikatsschalter werden nicht übernommen.
4. Zielgerät, GPIO und Vorschau prüfen und bestätigen. **Robbel3D einrichten**
   sichert den Controller, überträgt die LED-Konfiguration und Presets, prüft
   das Ergebnis und übernimmt die Caller-/WLED-Einstellungen sofort.
5. Mit **Sicherung speichern** die ursprüngliche `cfg.json` und `presets.json`
   als ZIP herunterladen. Die enthaltenen Dateien können bei Bedarf in WLED
   unter **Config → Security & Updates → Backup & Restore** eingespielt werden.

WLAN, Gerätekennung und übrige Controller-Einstellungen bleiben erhalten.
Weitere LED-Ausgänge werden deaktiviert und vorhandene Presets ersetzt. Bereits
belegte GPIOs werden abgelehnt. Die alten Vorlagen enthalten teilweise längere
Segmentgrenzen; die Einrichtung begrenzt sie auf die 145 LEDs des LED-Rings.
Die Autodarts-Anmeldung und Lizenzregeln bleiben bestehen. Ein Werksreset vor
dem Upload ist nicht erforderlich; Netzwerk- und Zugangseinstellungen werden
bewusst erhalten.

Bei einem Fehler werden keine ungeprüften Anwendungseinstellungen übernommen.
Der Controller kann jedoch bereits geändert sein; eine erstellte Sicherung
bleibt auch dann herunterladbar. Fortschritt und Fehler werden im Dialog
angezeigt. Nach Änderungen seit der Vorschau muss erneut geprüft werden.

### Terminal

`DartsHub --tui` starten, **WLED → Robbel3D One-Click** wählen und Konfiguration,
Adresse, GPIO, Board-ID, Medienordner und Sicherung angeben. Der Dialog bietet
dieselbe Vorschau, Bestätigung, Einrichtung und Sicherung. **Im lokalen Netz
suchen** zeigt die gefundenen Controller-Adressen.

## English

Open **WLED → Robbel3D One-Click** in the GUI. The original 145-LED Robbel3D
configuration and its six named presets are bundled into the application.

Select the device address and LED GPIO, check the board ID and media folder,
then choose **Validate and preview**. Discovery accepts a private IPv4 address
and searches its /24 network; hostnames and HTTPS addresses can be entered
directly. The media folder must exist on the computer running the runtime.
Confirm the displayed changes and select **Set up Robbel3D**. Progress reflects
device backup, configuration upload, preset upload, verification and immediate
application of Caller/WLED settings.

Wi-Fi, device identity, other controller settings, Autodarts login and licensing
are preserved. Additional LED outputs are disabled and existing presets replaced.
Occupied GPIOs are rejected. Legacy segment bounds are limited to the ring's
145 LEDs. Obsolete Caller server ports and certificate switches are displayed
as unsupported in the preview. A factory reset is unnecessary.

**Save backup** downloads a ZIP containing the original `cfg.json` and
`presets.json`. Restore the extracted files using WLED's **Config → Security &
Updates → Backup & Restore**. A failed setup may have already changed the device;
its backup remains available. Unverified application settings are not committed.

For the terminal equivalent, run `DartsHub --tui`, open **WLED → Robbel3D
One-Click**, enter the same inputs and use the shared preview/confirmation flow.
**Search local network** lists discovered device addresses.

## Implementation references

The original hub's `Robbel3DConfigurationManager`, `Robbel3DConfigWindow` and
`configs/robbel3d-configuration.json` define the profile, settings and upload
flow. Only the LED hardware block is bundled from its controller configuration;
the donor controller's network and security settings are excluded.
WLED's [JSON API](https://kno.wled.ge/interfaces/json-api/) documents named
presets, saving segment bounds/brightness and deleting presets. Both legacy
file uploads and modern JSON configuration/preset uploads are supported.
