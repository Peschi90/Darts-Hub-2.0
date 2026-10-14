# Caller: Medienpfad / Media folder

## Deutsch

Ohne eigenen Medienpfad installiert der Caller Voicepacks im bisherigen Standardordner. Der Installationsstatus bezieht sich immer auf den gespeicherten Medienpfad.

Neue Standardinstallationen verwenden normalerweise `%USERPROFILE%\DartsHub\soundpacks` unter Windows und `~/dartshub/soundpacks` unter Linux. Eigene oder ältere Medienpfade haben Vorrang. Vor Änderungen Caller-Pfad und [Systeminformationen](SYSTEM.md) prüfen.

In der GUI den Medienpfad bearbeiten und speichern. Sind im alten Pfad Packs installiert, bietet der Dialog **Ja, umziehen**, **Nein, im alten Ordner lassen** oder **Abbrechen** an. Der Umzug zeigt Animation und Dateifortschritt. Nach erfolgreichem Umzug ist die ausgewählte Stimme sofort nutzbar. Ohne Umzug bleiben die Dateien erhalten; eine dort nicht verfügbare Stimmenauswahl wird aufgehoben und die Packs können im neuen Ordner erneut installiert werden. Vorhandene gleichnamige Zielordner werden nicht überschrieben.

Terminal: **Caller → Caller konfigurieren / Mediengruppe → Medienpfad → Speichern**. Die TUI bietet dieselbe Abfrage und zeigt den Umzug mit Spinner und Fortschrittsbalken. Auch die Weboberfläche nutzt denselben Umzug.

Der JSON-Import übernimmt weiterhin den angegebenen Medienpfad, verschiebt aber keine lokalen Dateien ohne ausdrückliche Auswahl. GUI und TUI verwenden dieselbe Prüfung und denselben Installationsstatus.

## English

With no custom media folder, the caller installs voicepacks in its existing default folder. Installation status always reflects the saved media folder.

New default installations normally use `%USERPROFILE%\DartsHub\soundpacks` on Windows and `~/dartshub/soundpacks` on Linux. Custom or legacy media paths take precedence. Check the Caller path and [System information](SYSTEM.md) before changing it.

Edit the media folder and save. If packs exist in the previous folder, choose **Yes, move**, **No, leave in old folder** or **Cancel**. Moving shows animation and file progress. After a successful move, the selected voice is immediately usable. Without moving, the original files remain; unavailable voice selections are cleared and packs can be installed in the new folder. Existing destination folders with the same name are never overwritten.

Terminal: **Caller → Configure caller / media group → Media folder → Save**. The TUI offers the same choice and displays a spinner and progress bar. The web interface uses the same operation.

JSON import still applies the supplied media folder but never moves local files without an explicit choice. GUI and TUI share validation and installation status.
