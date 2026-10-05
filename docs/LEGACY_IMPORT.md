# Alte Konfiguration importieren / Import old configuration

## Deutsch

### Import durchführen
1. GUI: **Einstellungen → Allgemein → Alte Darts-Hub-Konfiguration importieren**.
   TUI: **Einstellungen / Lizenz → Alte Darts-Hub-Konfiguration importieren**.
2. Die originalen `apps-downloadable.json`, `apps-local.json` und `apps-open.json` auswählen.
   In der TUI Dateipfade durch Semikolon trennen oder ihren Ordner angeben.
3. Das Einstellungsmenü enthält nur die Dateiauswahl. Im eigenen Importdialog läuft die Prüfung mit Fortschrittsanimation und animiertem Wartehinweis (die Verarbeitung kann bis zu 3 Minuten dauern). Die Liste enthält nur Argumente mit gesetztem `Value` (auch `0` und `false`) und zeigt Originalwert, Wert für den Import, Importziel, Umrechnung und Prüfergebnis. Anmeldedaten bleiben ausgeblendet.
   Einzelne Werte im Feld **Wert für den Import** korrigieren und **Daten erneut prüfen** wählen. In der TUI einen Eintrag auswählen und Enter drücken; dort öffnet sich ein Werteditor. Arrays und Objekte als gültiges JSON eingeben. Nach einer Änderung ist die Übernahme bis zur neuen Prüfung gesperrt. Die Quelldateien bleiben unverändert. Neu geprüft werden nur geänderte Werte und davon abhängige Einstellungen; unveränderte Prüfergebnisse werden wiederverwendet.
   **Nicht importieren** schließt einen Eintrag aus. Halbtransparente rote Diagonalen markieren die komplette Karte. **Wieder für Import aktivieren** hebt die Auswahl auf. Nicht übernehmbare und nur teilweise gültige Einträge sind standardmäßig ausgeschlossen; eine Aktivierung umgeht keine Validierung oder Sperre für Anmeldedaten. In der TUI steht dieselbe Schaltfläche zur Verfügung, ausgeschlossene Einträge erhalten eine `////`-Markierung.
4. Vorhandene Modulkonfigurationen bleiben standardmäßig erhalten.
   **Überschreiben** nur ausdrücklich wählen, wenn alte Werte vorhandene ersetzen sollen.
5. **Import übernehmen** wählen; auch die Übernahme zeigt eine Animation. Schließen vor der Übernahme verwirft die Änderungen. Die Einstellungen werden gespeichert und sofort auf die laufenden Module angewendet; GUI und TUI laden den neuen Stand. Ein Neustart ist nicht erforderlich.

WLED übernimmt alle Effektalternativen eines Punktebereichs sowie Spieler-, Combo-
und Multiplikator-Definitionen. Kurze und lange Parameternamen werden mit denselben
Zuordnungen und Validatoren wie beim Terminalstart verarbeitet. Boolesche
Wertzuordnungen aus den alten Dateien werden berücksichtigt. Unbekannte
Effektparameter erscheinen als ungültig. `74|9` und `74|p9` übernehmen beide Palette 9.
Eine nackte Zahl nach einer Preset-/Playlist-ID bleibt die Dauer. Ungültige Angaben ersetzen
keine vorhandene Regel. URL-Verknüpfungen aus `apps-open.json` bleiben als nicht
unterstützte Anwendungen im Bericht sichtbar.

Importierte WLED-Effekt-IDs werden im GUI dem Namen aus dem Gerätekatalog zugeordnet, ohne die gespeicherte ID zu verändern. Solange der Katalog fehlt, bleiben Effekt-, Preset- und Palette-IDs sichtbar. Die TUI erlaubt dieselben IDs und Gerätenamen im WLED-Regel-Editor.

Terminal/Headless: `DartsHub --headless --import-legacy apps-downloadable.json
--import-legacy apps-local.json --import-legacy apps-open.json
--import-legacy-overwrite true` (als eine Befehlszeile ausführen).

### Danach prüfen
- Die ursprünglichen Dateien bleiben unverändert.
- Soundpacks werden nicht automatisch kopiert: benötigte Soundpacks erneut installieren.
- Medien- und Vorlagenpfade müssen auf dem neuen Host verfügbar sein; Pfade anpassen.
- Autodarts über die Geräteanmeldung verbinden, nicht mit dem alten Passwort.
- Importierte eigene Anwendungen haben **Autostart aus** und starten beim Import nicht.
- Alte AWTRIX3-Firmware benötigt ein Update auf AwtrixNG; siehe [AWTRIX](AWTRIX.md).
  GIF-Medien und Einstellungen: [GIF](GIF.md).

## English

### Run the import
1. GUI: **Settings → General → Import old Darts-Hub configuration**.
   TUI: **Settings / License → Import old Darts-Hub configuration**.
2. Select the original `apps-downloadable.json`, `apps-local.json` and `apps-open.json`.
   In the TUI, separate file paths with semicolons or enter their folder.
3. The settings page only selects files. Validation runs with a progress animation and an animated wait message (processing can take up to 3 minutes) in a separate import dialog. Its list includes only arguments with populated `Value` fields (including `0` and `false`), showing original value, value to import, destination, conversion and result. Credentials remain hidden.
   Correct individual entries in **Value to import** and choose **Recheck data**. In the TUI, select an entry and press Enter to open its value editor. Enter arrays and objects as valid JSON. Changes disable import until rechecked. Source files remain unchanged. Only changed values and dependent settings are checked again; unchanged results are reused.
   **Exclude from import** disables an entry. Translucent red diagonal lines cover its entire card. **Enable for import again** reverses the selection. Unsupported and partially invalid entries are excluded by default; enabling them cannot bypass validation or credential protection. The TUI provides the same action and marks excluded entries with `////`.
4. Existing module configurations are preserved by default.
   Explicitly select **Overwrite** only if old values should replace existing ones.
5. Choose **Apply import**; an animation also runs during application. Closing before applying discards the corrections. Settings are saved and immediately applied to running modules; GUI and TUI refresh their settings. No restart is required.

WLED preserves all alternatives in score ranges and player, combo and multiplier
definitions. Short and long names share the terminal aliases and validators. Legacy
boolean value mappings are honored. Unknown effect parameters are reported as
invalid. Both `74|9` and `74|p9` import palette 9. A bare number after a preset or playlist ID remains its duration. Invalid definitions
do not replace existing rules. URL shortcuts from `apps-open.json` remain reported
as unsupported applications.

The GUI displays imported WLED effect IDs using names from the device catalog without changing the stored ID. Effect, preset and palette IDs remain visible when the catalog is unavailable. The TUI accepts the same IDs and device effect names in its WLED rule editor.

Terminal/headless: `DartsHub --headless --import-legacy apps-downloadable.json
--import-legacy apps-local.json --import-legacy apps-open.json
--import-legacy-overwrite true` (run as one command line).

### Check afterwards
- Original files remain unchanged; reinstall required soundpacks, which are not copied automatically.
- Media and template paths must exist on the new host; adjust them as needed.
- Connect Autodarts through device login, not your old password.
- Imported own applications have **autostart off** and are not started during import.
- Old AWTRIX3 firmware needs an update to AwtrixNG; see [AWTRIX](AWTRIX.md) and [GIF](GIF.md).

Review state remains available for 15 minutes on the runtime host. If it expires, the host restarts, file structure changes, overwrite mode changes or stored settings change, a complete review is required. The dialog displays newly checked and reused result counts. No source JSON files are modified.
