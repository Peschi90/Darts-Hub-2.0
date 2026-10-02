# Alte Konfiguration importieren / Import old configuration

## Deutsch

### Import durchführen
1. GUI: **Einstellungen → Allgemein → Alte Darts-Hub-Konfiguration importieren**.
   TUI: **Einstellungen / Lizenz → Alte Darts-Hub-Konfiguration importieren**.
2. Die originalen `apps-downloadable.json`, `apps-local.json` und `apps-open.json` auswählen.
   In der TUI Dateipfade durch Semikolon trennen oder ihren Ordner angeben.
3. Vorschau und Warnungen lesen; nicht unterstützte oder ungültige Werte prüfen.
4. Vorhandene Modulkonfigurationen bleiben standardmäßig erhalten.
   **Überschreiben** nur ausdrücklich wählen, wenn alte Werte vorhandene ersetzen sollen.
5. Import bestätigen; danach **DartsHub bzw. den Headless-Host neu starten**.

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
3. Read the preview and warnings; check unsupported or invalid values.
4. Existing module configurations are preserved by default.
   Explicitly select **Overwrite** only if old values should replace existing ones.
5. Confirm the import, then **restart DartsHub or the headless host**.

### Check afterwards
- Original files remain unchanged; reinstall required soundpacks, which are not copied automatically.
- Media and template paths must exist on the new host; adjust them as needed.
- Connect Autodarts through device login, not your old password.
- Imported own applications have **autostart off** and are not started during import.
- Old AWTRIX3 firmware needs an update to AwtrixNG; see [AWTRIX](AWTRIX.md) and [GIF](GIF.md).
