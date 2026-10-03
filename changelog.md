# Changelog – Darts-Hub 2.0

## v0.1.0-beta.6

### Deutsch

- Aufgeben (auch während BullOff) oder ein abgeschlossener Leg-/Set-Wechsel löst keine Startansage mehr aus. Bei Board-finish vor dem letzten Spielstatus wird der Endzustand vor dem Abmelden abgerufen.

- Fehlende Spieler-Namensdateien werden bei aktivierter Namensansage durch player1, player2 usw. ersetzt; optionales TTS spricht andernfalls die Spielernummer.

- Autodarts-Matchlöschung spielt einmal matchcancel und optional ambient_matchcancel, auch nach einem Sieg; normale Matchabschlüsse bleiben ohne Abbruchansage.

- Autodarts-Matchgewinner werden über den ursprünglichen Spielerindex zugeordnet; Leggewinner nutzen die aktuelle Reihenfolge. Turns werden über playerId zugeordnet, damit nach BullOff der richtige Sieger angesagt wird.

- Caller behandelt BullOff separat: einmalige Bulling-Start-/Endansagen ohne Game-on-, No-score-, Bust- oder Game-shot-Ansagen. Der anschließende Spielstart wird auch bei gleicher Match-ID erkannt.

- Direkte WLED-Effekte nutzen den gesamten LED-Streifen; die manuelle Segmentauswahl entfällt. Segmentaufteilungen werden über Presets gesteuert.

- Updateprüfung beim Start zeigt eine Animation und öffnet den Hinweisdialog zuverlässig auf dem GUI-Thread; unabhängig von Erweiterungseinstellungen.

- Linux-Caller erkennt ffplay, paplay und aplay automatisch und wählt den Player passend zum Dateiformat; ARM-Architekturen und 32-Bit-Benutzerbereiche werden korrekt erkannt. Der gesamte Soundpack-Bibliothekskopf ist klickbar.
- Neue Versionen werden in einem Update-Dialog mit Release Notes angekündigt; die TUI zeigt dieselben Versionshinweise.
- Einheitlicher Installer-Header mit ASCII-Monogramm, Dart-Motiv und klaren Installationsabschnitten.
- Optionale GUI-/TUI-Desktop-Verknüpfungen im Installer; Beta-Installationen aktivieren Beta-Updates automatisch. Headless-Autostart wird nur noch in der TUI angeboten.
- Windows-Online-Installer startet auch über `irm | iex`; Installer-Dateien werden zusätzlich als öffentliche Release-Downloads veröffentlicht.
- Gemeinsame Installationsadresse get.darts-hub.de mit automatischer Skriptauswahl und Browser-Anleitung.
- Online-Installer erkennt Betriebssystem und Architektur und bietet GUI, TUI, Headless, Beta-Versionen und Autostart an.
- Autodarts-Anmeldung mit gespeicherter Verbindung und direkten Spielereignissen.
- Caller, WLED, PixelIt, AwtrixNG und GIF mit Einstellungen in GUI, TUI und Headless.
- Eigene Anwendungen und Skripte starten gemeinsam mit DartsHub und werden beim Beenden geschlossen.
- Startverzögerung hält Module, eigene Autostart-Anwendungen und Updateprüfung zurück.
- Getrennte Erweiterungslogs, Support-Diagnose und Import alter Konfigurationen.
- Kompakte Betriebssystem-Pakete ohne Dokumentationsdateien; Updates kommen aus dem öffentlichen Release-Repository.

### English

- Forfeits (including during BullOff) and finished leg/set changes no longer trigger start announcements. Board-finish preceding the final state retrieves that state before unsubscribing.

- Enabled player-name calls fall back to player1, player2 etc. when a name file is missing; optional TTS otherwise speaks the player number.

- Autodarts match deletion plays matchcancel once with optional ambient_matchcancel, including deletion after a win; normal finishes do not announce cancellation.

- Autodarts match winners use original player indices while leg winners use the current order. Turns are assigned by playerId so the correct winner is announced after BullOff.

- Caller handles BullOff separately with deduplicated bulling start/end sounds, without game-on, no-score, bust or game-shot calls. The subsequent game starts correctly even with the same match ID.

- Direct WLED effects control the entire LED strip; manual segment selection has been removed. Use presets for custom segment layouts.

- Startup update checks show progress and open the notification on the UI thread independently of extension settings.

- Linux caller detects ffplay, paplay and aplay automatically and selects a player matching the file format; ARM architectures and 32-bit userspace are detected correctly. The entire soundpack-library header is clickable.
- New versions are announced in an update dialog with release notes; the TUI exposes the same notes.
- Unified installer header with ASCII monogram, dart artwork and clear installation stages.
- Optional GUI/TUI desktop shortcuts in the installer; beta installations enable beta updates automatically. Headless autostart is offered only in the TUI.
- Windows online installer works through `irm | iex`; installer scripts are also published as public release downloads.
- Shared get.darts-hub.de installation URL with automatic script selection and browser instructions.
- Online installer detects OS and architecture and offers GUI, TUI, headless, beta releases and login autostart.
- Persistent Autodarts login and direct match events.
- Caller, WLED, PixelIt, AwtrixNG and GIF configuration through GUI, TUI and headless operation.
- Custom applications and scripts start with DartsHub and close when it exits.
- Startup countdown delays modules, custom startup applications and update checks.
- Separate extension logs, support diagnostics and legacy configuration import.
- Compact platform packages without documentation; updates use the public release repository.
