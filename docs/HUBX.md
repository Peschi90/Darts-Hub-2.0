# HubX: Entdecken und teilen / Discover and share

## Deutsch

### Vorlagen für mehrere Geräte

Mehrgeräte-Ereignisse sind im Katalog gekennzeichnet. Jede Anzeige hat ihre eigene animierte Vorschau, auch in der kleinen Katalogkarte. Vor **Download** oder **An Darts-Hub senden** wählst du alle Anzeigen oder nur eine. Die Einzelwahl enthält nur deren Schritte, Anzeigevorlagen und Bilder, weiterhin als ein Ereignis.

Im Darts-Hub-Empfangsdialog ordnest du jede gewählte Anzeige einem anderen Zielgerät zu. Dies gilt auch in TUI, lokaler Weboberfläche, Webapp und beim Paketdateiimport. Icon-Konflikte werden je Uhr geprüft; WLED-Preset-IDs müssen auf allen gewählten Controllern frei sein. Adressen, Zugangsdaten und lokale Geräte-IDs werden nicht veröffentlicht.

Für vollständige Mehrgeräte-Pakete werden aktuelle Versionen von HubX und Darts-Hub benötigt. Einzelne Anzeigen bleiben mit dem bisherigen Paketformat kompatibel. Alte Uploads ohne Gerätezuordnung bitte erneut teilen; ihre ursprüngliche Aufteilung lässt sich nicht zuverlässig nachträglich ermitteln.

HubX ist in **AWTRIX-NG, PixelIt und WLED** verfügbar. Das GIF-Anzeigemodul bietet keinen HubX-Browser und keine Teilen-Funktion. Pro Veröffentlichung wird genau ein Ereignis geteilt, mit allen zugehörigen Schritten und Bildern.

HubX unterstützt GIFs und PNG-Pixelgrafiken auch in **64×8**. Auflösungsfilter und Größenangaben unterscheiden die Inhalte. Bei AWTRIX-Ereignissen wird die 32×8- oder 64×8-Displaygröße des Quellcontrollers für die Vorschau übernommen; sie ändert beim Import keine Einstellungen des Zielcontrollers. Der AWTRIX-HubX-Browser in GUI, TUI, lokaler Weboberfläche und Webapp hat ebenfalls einen Auflösungsfilter. PixelIt-Animationen bleiben auf maximal 32×8 beschränkt.

[HubX](https://hubx.darts-hub.de/) benötigt **hubx_access** in deinem Lizenzschlüssel. Unter **Einstellungen → Lizenz** prüfen. Die Plattform verlangt die Zustimmung zu ihren aktuellen Rechtstexten; beim Teilen aus Darts-Hub kann dies direkt im Dialog erfolgen.

### Entdecken und übernehmen

Im HubX-Bereich der gewünschten Erweiterung **Effekte entdecken** öffnen. Beiträge suchen, animierte Vorschau und Auslöseeinstellungen ansehen und gegebenenfalls bewerten. Eine Miniansicht muss eventuell auf HubX erst vorbereitet werden. **Übernehmen** startet die lokale Prüfung: Geräte wählen, Konflikte lösen und bestätigen. Einstellungen werden gespeichert und sofort geladen.

Auf der Website liefert **An Darts-Hub senden** einen Beitrag an eine verfügbare Installation. Darts-Hub muss laufen und HubX erreichen können. Der Posteingang übernimmt nichts ohne deine Bestätigung. Alternativ die **Paket-JSON** herunterladen und im HubX-Dateiimport öffnen. Eine rohe GIF-Datei ist keine Paket-JSON. Beide Wege verwenden dieselben Prüfungen.

| Beitrag | Ergebnis |
| --- | --- |
| AWTRIX-Ereignis | Regel, benötigte Anzeigevorlagen und Bilder; Zielcontroller und Dateikonflikte prüfen. |
| WLED-Ereignis | Regel und verwendete Presets; Controller und freie Preset-IDs prüfen. |
| Pixelit-Ereignis | Regel und angepasste Vorlagen; Zielanzeigen zuordnen. |
| Einzelnes GIF | Auf einen ausgewählten AWTRIX-NG-Controller laden; keine Ereignisregel. |
| Einzelnes WLED-Preset | Nur auf den ausgewählten Controller laden; keine Ereignisregel. |
| Einzelne Pixelit-Vorlage | In der Vorlagenbibliothek speichern, ohne Zielgerät oder neue Regel. |

Bei gleichen GIF-Namen werden beide Bilder gegenübergestellt: umbenennen, überschreiben oder abbrechen. Belegte WLED-Preset-IDs benötigen eine andere, freie ID; übernommene Regeln verwenden diese ID. Anzeigevorlagen erhalten aussagekräftige Namen mit `_hubX`. Vorschauen sind Simulationen oder aufgezeichnete Controller-Ausgaben. Zufall, Audioeingaben und Firmwareunterschiede können reale Effekte verändern.

### Teilen

**Auf HubX teilen** im jeweiligen Modul öffnen. Titel selbst eingeben, ausdrücklich genau ein Ereignis auswählen und den benötigten Quellcontroller bestimmen. Daten prüfen und die öffentliche **CC0**-Freigabe bestätigen. Geräteadressen und Zugangsdaten bleiben privat. Nur eigene oder entsprechend freigegebene Inhalte hochladen.

AWTRIX-GIFs werden zusätzlich einzeln angeboten. Verknüpfte WLED-Presets erscheinen zusätzlich als eigene Beiträge mit passender Vorschau. Eine optionale Controller-Aufnahme benötigt ein erreichbares Gerät und ist während eines laufenden Matches gesperrt. Pixelit veröffentlicht auch die wirksamen Vorlagen inklusive Text-, Farb-, Scroll- und Helligkeitsanpassungen. Manuelle Website-Uploads sind für GIFs und PNG-Pixelgrafiken; Ereignisse kommen aus Darts-Hub.

Studio-Zugang: Administratoren oder **studio_access**. Eigene GIFs lassen sich im Studio bearbeiten; Administratoren können weitere Beiträge öffnen. Profile, Bewertungen und Badges werden auf der Website verwaltet.

TUI: HubX-Posteingang beziehungsweise HubX-Aktionen der Erweiterung verwenden. Lokale Weboberfläche und gekoppelte Webapp bieten dieselben Konfliktprüfungen.

## English

### Multi-device templates

Multi-device events are marked in the catalogue. Each display has its own animated preview, including compact cards. Before **Download** or **Send to Darts-Hub**, choose all displays or one. Selecting one keeps only its steps, templates and images, still as a single event.

In Darts-Hub, assign each selected display to a different target device. The same workflow applies to TUI, local web UI, paired webapp and package-file imports. Icon conflicts are checked per clock; WLED preset IDs must be free on every selected controller. Device addresses, credentials and local IDs remain private.

Full multi-device packages require current HubX and Darts-Hub versions. Single-display selections retain the previous package format. Re-share old uploads that lack device information: their original allocation cannot be reliably reconstructed.

HubX is available in **AWTRIX NG, PixelIt and WLED**. The GIF display module has no HubX browser or sharing action. Each publication shares exactly one event, including all its steps and images.

HubX supports GIFs and PNG pixel graphics in **64×8** too, with resolution filters and size labels. AWTRIX event previews use the source controller's 32×8 or 64×8 display size; importing does not change target device settings. The AWTRIX HubX browser in GUI, TUI, local web UI and webapp also offers a resolution filter. PixelIt animations remain limited to 32×8.

HubX requires **hubx_access**. Verify your saved license and accept the current legal documents when prompted. Discover effects from the HubX section of each module, inspect previews and trigger conditions, then confirm the local import. Website **Send to Darts-Hub** delivers a package to a running installation for review. Downloaded **package JSON** files use the same workflow.

Event packages include their required resources. Standalone GIFs upload to a selected AWTRIX NG controller, standalone WLED presets upload only to a selected controller, and standalone Pixelit templates save to the template library: none creates a rule. Compare, rename or overwrite GIF name collisions. WLED requires free replacement IDs, which imported rules then use. Templates use meaningful `_hubX` names.

When sharing, enter a title, choose exactly one event and the source controller, review and confirm public **CC0** sharing. Device addresses and credentials stay private. Included AWTRIX GIFs, linked WLED presets and effective Pixelit templates are also offered separately. Manual website uploads accept GIFs and PNG pixel graphics; event packages originate in Darts-Hub. Studio requires administrator rights or **studio_access**. GUI, TUI, local web UI and paired webapp share import validation. Previews have simulation, firmware and external-input limitations.

[GIF import](HubX-GIF-Import.md) · [AWTRIX](AWTRIX.md) · [Pixelit](PIXELIT.md) · [WLED](WLED_CONFIGURATION_AND_AUTODARTS.md)

Standalone GIFs can also become PixelIt animation templates, retaining their original dimensions (maximum 32 × 8) and timing. Select this destination in the Darts-Hub inbox and configure repetition there. Einzelne GIFs lassen sich im Posteingang auch als PixelIt-Animation übernehmen; Originalgröße bis 32 × 8, Bilddauer und einstellbare Wiederholung bleiben erhalten. [GIF import / GIF-Import](HubX-GIF-Import.md).
