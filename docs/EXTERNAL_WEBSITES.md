# Webseiten in eigenen Anwendungen / Websites in external applications

GUI: **Eigene Anwendungen → Webseite hinzufügen**. Name, vollständige HTTP-/HTTPS-Adresse und Browser wählen; optional Startparameter im vorhandenen Argumentfeld eintragen. **Speichern**, anschließend auf dem Dashboard **Webseite öffnen**. Autostart steht im Reiter Verhalten zur Verfügung. Die Browserliste stammt vom Darts-Hub-System, auch bei einer Verbindung zu einem anderen Rechner.

TUI: **Eigene Anwendungen → Webseite hinzufügen**. **Url**, **Browser** und bei Bedarf **Arguments** bearbeiten, dann speichern. Auf dem Dashboard den Eintrag und **Webseite öffnen** auswählen. Vorhandene Einträge können über **Kind → Website** umgestellt werden.

Der System-Standardbrowser benötigt keine zusätzlichen Parameter. Für Parameter einen konkreten installierten Browser wählen; z. B. `--new-window` oder als JSON-Liste `["--new-window"]`. Welche Parameter wirksam sind, hängt vom Browser ab. Darts-Hub übergibt Browserfenster an den Nutzer und beendet sie beim Schließen nicht. Webseiten haben deshalb keine Prozessüberwachung oder automatische Absturz-Neustarts. Im Dashboard zeigt **An Browser übergeben** die Übergabe, nicht den Ladezustand der Webseite.

Der Import übernimmt alte `custom-url-*`-Einträge aus `apps-open.json`: `file`/`url` → Webadresse, `browser` → Browser und `arguments` → Startparameter. Fehlende Browserwerte verwenden den System-Standardbrowser; ein ausdrücklich gewählter, fehlender Browser bleibt erhalten und wird gemeldet. Importierte Einträge starten manuell. Nicht unterstützte Werte und ungültige Adressen werden im Prüfdialog gemeldet. Es werden beim Import keine Webseiten geöffnet.

GUI: **External applications → Add website**. Enter a name, full HTTP/HTTPS address, installed browser and optional startup arguments. **Save**, then choose **Open website** on the dashboard. Autostart is available on the Behaviour tab. The browser list comes from the Darts-Hub host, including remote connections.

TUI: **External applications → Add website**. Edit **Url**, **Browser** and optionally **Arguments**, then save. Select the dashboard entry and **Open website**. Existing entries can be switched via **Kind → Website**.

The system default browser accepts no extra arguments. Choose a specific browser for parameters, e.g. `--new-window` or `["--new-window"]`. Parameter support is browser-dependent. Browser windows remain under user control and are not closed when Darts-Hub shuts down. Websites therefore have no process monitoring or automatic crash restart. **Handed to browser** reports the handoff, not the page's loading status.

Legacy `custom-url-*` entries are imported from `apps-open.json`: `file`/`url` becomes the website address, `browser` selects a browser and `arguments` provides startup parameters. A missing browser field defaults to the system browser; an explicitly selected unavailable browser is preserved and reported. Imports remain on manual start and never open websites. Unsupported values and invalid addresses appear in the review dialog.

Webseiten benötigen weder Ausführungsart noch Arbeitsordner. In GUI und TUI entfällt die Betriebssystemauswahl für alle eigenen Anwendungen. Alte Betriebssystemfilter bleiben in gespeicherten Daten erhalten, verhindern aber keinen Start mehr; alte Webseiten-Arbeitsordner werden nicht verwendet. Die Installation auf dem Darts-Hub-Rechner bestimmt das Betriebssystem.

Websites require no execution type or working directory. Neither frontend requires an operating-system selection for external applications. Legacy OS filters are preserved in saved configurations but no longer prevent launching; legacy website working directories are ignored. The Darts-Hub host installation determines the operating system.
