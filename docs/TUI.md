# Terminalbedienung / Terminal interface

## Deutsch

Die **System**-Ansicht unter **Weitere Module / System** zeigt die echten Backend-Pfade. HubX-Pakete lassen sich über den Posteingang oder den Dateiimport prüfen und übernehmen. Terminal-Updates funktionieren auch ohne TUI mit `--update`; vollständige Entfernung mit `--uninstall` nach Bestätigung. [System](SYSTEM.md) · [HubX](HUBX.md) · [Startargumente](START_ARGUMENTS.md)

1. Im entpackten Programmordner starten:

| System | Befehl |
| --- | --- |
| Windows | `.\DartsHub.exe --tui` |
| Linux | `./DartsHub --tui` |
| macOS | `./DartsHub.app/Contents/MacOS/DartsHub --tui` |

2. Mit **Tab** Bereiche wechseln, mit **Pfeiltasten** auswählen, mit **Enter** bearbeiten/Aktion ausführen, mit **Esc** Dialoge schließen.
3. Zuerst unter **Autodarts** die Board-ID eingeben, Geräteanmeldung starten und den angezeigten Code im Browser bestätigen.
4. Module auf der **Übersicht** mit **Enter** ein-/ausschalten: sofort gespeichert. Andere Werte mit **Speichern** übernehmen; Tests speichern nicht.

- Für einen separaten Host ohne Oberfläche im Startbefehl `--tui` durch `--headless` ersetzen; die TUI in einem zweiten Terminal öffnen.
- Ein von der TUI automatisch gestarteter Host endet beim Schließen der TUI, außer Headless-Autostart ist aktiv. Ein separat gestarteter Host läuft weiter.
- [Autostart](AUTOSTART.md) · [Startargumente](START_ARGUMENTS.md)

## English

**System** under **Other modules / system** reports actual backend paths. Review HubX packages through the inbox or file import. Terminal maintenance also works without the TUI: `--update` updates in place; `--uninstall` performs complete removal after confirmation. [System](SYSTEM.md) · [HubX](HUBX.md) · [Arguments](START_ARGUMENTS.md)

1. Start from the extracted program folder:

| System | Command |
| --- | --- |
| Windows | `.\DartsHub.exe --tui` |
| Linux | `./DartsHub --tui` |
| macOS | `./DartsHub.app/Contents/MacOS/DartsHub --tui` |

2. Use **Tab** to switch areas, **arrow keys** to select, **Enter** to edit/run actions, and **Esc** to close dialogs.
3. First, enter your board ID under **Autodarts**, start device login and confirm the displayed code in your browser.
4. Toggle modules on the **Overview** with **Enter**: saved immediately. Apply other values with **Save**; tests do not save.

- For a separate host without a UI, replace `--tui` with `--headless` in the start command; open the TUI in a second terminal.
- A host automatically started by the TUI stops when the TUI closes, unless headless autostart is enabled. A separately started host keeps running.
- [Autostart](AUTOSTART.md) · [Startup arguments](START_ARGUMENTS.md)

## PixelIt-GIF-Import / PixelIt GIF import

Im HubX-Posteingang beim Übernehmen eines GIFs „Als animierte PixelIt-Vorlage übernehmen“ wählen. Name und Wiederholung festlegen (1–100 Durchläufe / bis zum nächsten Effekt / bis zum nächsten Turn). Die Vorlage anschließend im PixelIt-Ereignisschritt wählen; dessen Menü kann die Wiederholung überschreiben. Originalgröße maximal 32 × 8, Darts-Hub muss laufen.

When accepting a GIF in the HubX inbox, select “Import as an animated PixelIt template”, then choose its name and repetition (1–100 plays / until next effect / until next turn). Select the template in a PixelIt event step; its menu can override repetition. Original dimensions must not exceed 32 × 8 and Darts-Hub must remain running.

## Geführte Einführung / Guided introduction

Im Menü oder über die Schaltfläche **Geführte Einführung** dieselben 28 Kapitel wie in der GUI öffnen. **Lerninhalt öffnen** zeigt Erklärung, Beispiel und Aufgabe; **Bereich zeigen** öffnet die echte Konfiguration. Übungen und Verständnisfragen senden keine Befehle. Kapitelwahl, Pause, Fortsetzen und Neustart sind verfügbar. [Anleitung](GUIDED_INTRODUCTION.md)

Choose **Guided introduction** in navigation or its button for the same 28 lessons as the GUI. **Open lesson** shows explanation, example and task; **Show section** opens actual settings. Exercises and checks send no commands. Choose chapters, pause, resume or restart. [Guide](GUIDED_INTRODUCTION.md)

Die Einführung führt jede kleine Teilaufgabe einzeln auf. Nach dem Ausprobieren **Aufgabe selbst ausprobiert** wählen oder die Aufgabe ausdrücklich überspringen. Kapitel und Teilaufgabe bleiben gespeichert. Die Animationswahl betrifft die visuelle Hervorhebung in der GUI.

The guide lists small subtasks separately. After trying one, select **I tried the task**, or deliberately skip it. Chapter and subtask are saved. The animation preference affects visual highlighting in the GUI.


## Gespeicherte Lizenz / Saved license

Unter **Einstellungen → Lizenz** kannst du denselben gespeicherten Schlüssel prüfen wie im Browser. Die Lizenz wird verschlüsselt auf dem Darts-Hub-Rechner gespeichert. Ein leeres Eingabefeld bedeutet nicht, dass sie fehlt; der Status weist auf einen gespeicherten Schlüssel hin. Nach Verbindungsfehlern wird etwa nach einer Minute automatisch erneut geprüft, sonst alle 15 Minuten. Bis zur erfolgreichen Prüfung bleiben geschützte Funktionen gesperrt. Sichere und übertrage `settings.json` und den zugehörigen Ordner `keys` gemeinsam und verwende denselben Dienstbenutzer.

Under **Settings → License**, you can validate the same saved key as in the browser. The license is stored encrypted on the Darts-Hub host. An empty input does not mean it is missing; the status indicates a saved key. Connection failures are retried automatically after about one minute; otherwise validation runs every 15 minutes. Protected features remain locked until validation succeeds. Back up and transfer `settings.json` together with its matching `keys` directory and use the same service account.


## Änderungen aus anderen Oberflächen / Changes from other frontends

GUI, Terminal und Weboberfläche derselben laufenden Installation übernehmen gespeicherte Änderungen automatisch, normalerweise innerhalb weniger Sekunden. Ein Neuladen ist nicht nötig. Bei offenen Entwürfen oder Bearbeitungsdialogen bleibt die Eingabe erhalten und ein Hinweis meldet wartende Änderungen. Speichere oder verwirf deinen Entwurf beziehungsweise schließe den Dialog, damit der aktuelle Stand geladen wird. Speichern übernimmt deinen lokalen Entwurf; prüfe bei gleichzeitiger Bearbeitung derselben Einstellungen zuvor die Änderungen. Getrennte Darts-Hub-Backends werden nicht miteinander synchronisiert.

GUI, terminal and web frontends connected to the same running installation automatically load saved changes, normally within a few seconds. Manual refresh is unnecessary. Unsaved drafts and open editors are preserved; a notice indicates pending changes. Save or discard your draft, or close the editor, to load the current settings. Saving applies your local draft; review changes first when editing the same settings concurrently. Separate Darts-Hub backends are not synchronized.


## Updates auf dem Darts-Hub-Rechner / Updates on the Darts-Hub host

Unter **Einstellungen / Lizenz → Updates prüfen** lädt die TUI das Paket auf dem verbundenen Backend herunter. Nach vollständigem Download erscheint die Installation mit Bestätigung. Sie verwendet denselben Ablauf wie GUI und Web, auch bei einer entfernten Verbindung. Ohne TUI bleibt `DartsHub --update` verfügbar.

Under **Settings / license → Check updates**, the TUI downloads the package on the connected backend. Once downloaded, installation becomes available with confirmation. This uses the same workflow as GUI and web, including remote connections. Without the TUI, `DartsHub --update` remains available.


## Soundpacks herunterladen / Download soundpacks

Unter **Soundpacks → Herunterladen** zeigt das Terminal den aktuellen Schritt, dessen Prozentwert sowie beim Entpacken und Zuordnen die verarbeiteten Dateien. Während des Aufräumens wird weiter gewartet. Die Liste installierter Packs aktualisiert sich automatisch nach der Verarbeitung. **Download abbrechen** beendet Download oder Verarbeitung.

Under **Soundpacks → Download**, the terminal shows the current phase and its percentage, plus processed file counts while extracting and mapping. Cleanup remains a waiting phase. The installed pack list refreshes automatically after processing. **Cancel download** stops downloading or processing.


## darts-voice / darts-extern

Die Module haben eigene TUI-Menüs und akzeptieren `--voice-PROPERTY` bzw. `--extern-PROPERTY`. Der Legacy-Import übernimmt unterstützte Einstellungen mit deaktiviertem Start und schließt Anmeldedaten aus. Einrichtung, Voraussetzungen und Terminalbeispiele: [Voice / Extern](VOICE_EXTERN.md).

Both modules have dedicated TUI menus and accept `--voice-PROPERTY` / `--extern-PROPERTY`. Legacy import preserves supported settings, excludes credentials and keeps workers disabled. See the linked guide for dependencies and terminal examples.
