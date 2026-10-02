# Terminalbedienung / Terminal interface

## Deutsch

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
