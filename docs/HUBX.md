# HubX: Entdecken und teilen / Discover and share

## Deutsch

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

**Auf HubX teilen** im jeweiligen Modul öffnen. Titel selbst eingeben, ausdrücklich die richtigen Ereignisse auswählen und den benötigten Quellcontroller bestimmen. Daten prüfen und die öffentliche **CC0**-Freigabe bestätigen. Geräteadressen und Zugangsdaten bleiben privat. Nur eigene oder entsprechend freigegebene Inhalte hochladen.

AWTRIX-GIFs werden zusätzlich einzeln angeboten. Verknüpfte WLED-Presets erscheinen zusätzlich als eigene Beiträge mit passender Vorschau. Eine optionale Controller-Aufnahme benötigt ein erreichbares Gerät und ist während eines laufenden Matches gesperrt. Pixelit veröffentlicht auch die wirksamen Vorlagen inklusive Text-, Farb-, Scroll- und Helligkeitsanpassungen. Manuelle Website-Uploads sind für GIFs; Ereignisse kommen aus Darts-Hub.

Studio-Zugang: Administratoren oder **studio_access**. Eigene GIFs lassen sich im Studio bearbeiten; Administratoren können weitere Beiträge öffnen. Profile, Bewertungen und Badges werden auf der Website verwaltet.

TUI: HubX-Posteingang beziehungsweise HubX-Aktionen der Erweiterung verwenden. Lokale Weboberfläche und gekoppelte Webapp bieten dieselben Konfliktprüfungen.

## English

HubX requires **hubx_access**. Verify your saved license and accept the current legal documents when prompted. Discover effects from the HubX section of each module, inspect previews and trigger conditions, then confirm the local import. Website **Send to Darts-Hub** delivers a package to a running installation for review. Downloaded **package JSON** files use the same workflow.

Event packages include their required resources. Standalone GIFs upload to a selected AWTRIX NG controller, standalone WLED presets upload only to a selected controller, and standalone Pixelit templates save to the template library: none creates a rule. Compare, rename or overwrite GIF name collisions. WLED requires free replacement IDs, which imported rules then use. Templates use meaningful `_hubX` names.

When sharing, enter a title, choose the intended events and source controller, review and confirm public **CC0** sharing. Device addresses and credentials stay private. Included AWTRIX GIFs, linked WLED presets and effective Pixelit templates are also offered separately. Manual website uploads accept GIFs; event packages originate in Darts-Hub. Studio requires administrator rights or **studio_access**. GUI, TUI, local web UI and paired webapp share import validation. Previews have simulation, firmware and external-input limitations.

[GIF import](HubX-GIF-Import.md) · [AWTRIX](AWTRIX.md) · [Pixelit](PIXELIT.md) · [WLED](WLED_CONFIGURATION_AND_AUTODARTS.md)
