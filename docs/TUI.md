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

Hub75: `DartsHub --tui` → **Hub75**; [Einrichtung und entsprechende GUI-Aktionen / setup and GUI equivalents](HUB75.md).

**Gerät hinzufügen / Add device** öffnet die Auswahl für geführte oder manuelle
Einrichtung. Der erste Schritt zeigt die Controller-Anforderung und den
gekennzeichneten Affiliate-Link. Die Geräteliste zeigt den Anzeigemodus.
**Gerät · Betriebsoptionen pro Gerät / Device · Runtime options per device**
überschreibt einzelne Modulstandards. Leere Felder übernehmen die Vorgabe.

**Add device** opens the guided or manual setup choice. The first step shows
the controller requirement and labelled affiliate link. The device list shows
the display mode. **Device · Runtime options per device** overrides individual
module defaults. Leave a field blank to inherit it.

## MatrixMind / Hub75 GIFs

`DartsHub --tui` → Hub75 → device · MatrixMind: typed settings, outgoing-frame preview, X01/Cricket/Ultra demos, stop demo, view/export diagnostics and guide/credits. Save the draft to activate settings. Supports 64/128/192×32 natively without Python. Design & font offers the original choices for 2–3 panels; Preview images shows selectable rendered samples. One panel uses the fixed compact layout. Standby adds the animated logo preview. Device · Manage GIFs: upload, preview, download and delete with confirmation. Details: [Deutsch / English](MATRIXMIND.md).

**Gerät · GIFs verwalten / Device · Manage GIFs** lädt dieselbe Controller-Dateiliste wie die GUI unter **Hub75 → Geräte & Einrichtung / Devices & setup**.

MatrixMind: **Einrichten / Setup** erklärt den Ablauf. **MatrixMind aktivieren &
speichern / Activate MatrixMind & save** prüft den Controller und aktiviert Modul,
Gerät und MatrixMind gemeinsam. **Speichern & auf dem Panel testen / Save & test on
the panel** übernimmt den gesamten Entwurf vor dem Paneltest. **MatrixMind deaktivieren /
Deactivate MatrixMind** lässt Modul und Gerät eingeschaltet. Bildschirm-Beispielvorschau
und tatsächliche Ausgabe sind getrennt; RGB-Werte werden nicht künstlich aufgehellt.

The terminal offers the same ordered steps. Activation and panel tests check and
save the complete Hub75 draft; all three required switches are enabled together.
Deactivation changes only MatrixMind. Sample frames and current output stay separate.
Controller live view now requires every controller pixel. Reduced or unverified
firmware previews show an actionable message in GUI and TUI instead of an incomplete
image. This applies to GIFs and internal WLED effects too. See the optional
[DHLive1 firmware build](../scripts/wled-full-preview/README.md); it is not installed automatically.

Hub75-Paneländerungen / panel changes: MatrixMind ausschalten & speichern / deactivate & save → Panelentwurf bearbeiten / edit panels → auf Display übertragen & Neustart bestätigen / apply & confirm restart → Rücklesung abwarten / wait for verification → Konfiguration speichern / save configuration.


Hub75-Ereignisse / HUB75 events: **Hub75 → Konfiguration bearbeiten / Edit configuration → Rules**. Nur Panels im Ereignismodus sind Ziele. **Effects → HubX-Layout → Layout** lädt die Layoutdatei oder ändert Textplatzhalter. HubX-Pakete können über den HubX-Posteingang geprüft und übernommen werden. [Ablauf / Workflow](HUB75.md).


### Ereignisse nach Gerät / Events by device

WLED, HUB75, Pixelit und AWTRIX bieten **Gerät filtern**. In WLED/HUB75 ist die Auswahl auch im Konfigurationseditor verfügbar. „Alle Geräte“ setzt den Filter zurück. Regeln mit mehreren Schritten erscheinen, sobald mindestens ein Schritt das Gerät anspricht. Der Filter ändert keine Zuordnung und wird nicht im Backup gespeichert. Neu angelegte Regeln werden unabhängig vom bisherigen Filter geöffnet.

WLED, HUB75, Pixelit and AWTRIX offer **Filter by device**, also inside the WLED/HUB75 configuration editor. **All devices** clears the filter. A rule matches when at least one step targets the device, including steps targeting all devices. Filtering does not change assignments or backup data. New rules open independently of the previous filter.

GUI, Web/Webapp und Android zeigen zusätzlich kleine Beispielvorschauen in eingeklappten Regeln, sofern ein lokaler Renderer verfügbar ist. Sie zeigen den ersten Schritt bzw. den ersten darstellbaren Effekt, keine komplette zufällige Sequenz. Die Vorschau pausiert außerhalb des sichtbaren Bereichs; aufgeklappt ersetzt die große Vorschau die Miniatur. Es werden keine Effekte an Geräte gesendet. Die TUI zeigt keine Miniaturen.

GUI, web/webapp and Android additionally show small sample previews in collapsed rules where a local renderer is available. They show the first step or first supported effect, not an entire random sequence. Off-screen previews pause; expanding the rule replaces the miniature with its full preview. No effects are sent to devices. The TUI has no miniatures.
