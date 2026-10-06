# Changelog – Darts-Hub 2.0

## v0.1.0-beta.16

### Deutsch

- Weboberfläche für GUI und Headless unter Port 8079: gemeinsames Design, Erweiterungseinstellungen, Autodarts-Anmeldung, Konsole, Lizenz, Support und Deutsch/Englisch. Direkt im Netzwerk ohne Zugangscode verfügbar; die Webseite wird in das Programm eingebettet.

- Ausführliche Soundpack-Anleitung auf Deutsch und Englisch: Dateinamen, Ereignisse, Ersatzsounds, Einzelwurfmodi, Spielernamen, Checkout, Blind-Support und Ambient sowie Einrichtung eigener Packs in GUI, TUI und Headless.

- Caller: neue Würfe ersetzen laufende Einzelwurfansagen; veraltete Einzelwürfe werden ausgelassen. Gesamtscore, Bust und Siegeransagen bleiben geschützt. Ambient-Sounds laufen auf einem unabhängigen Audiokanal parallel.

- Caller: feste 200-ms-Pause vor anschließenden TTS-Spielernamen entfernt.

- Logs: eine Datei pro Modul und Kalendertag (`Modulname_04.log`), Neustarts hängen an; am gleichen Tag im nächsten Monat wird die Datei neu begonnen. Keine Größenrotation und keine automatische 14-Tage-Löschung. Support-Sammlungen erfassen auch die neuen Dateinamen.

- Update-Dialog zeigt Release Notes als formatiertes Markdown mit Überschriften, Listen, Hervorhebungen, Code, Links und Tabellen. TUI zeigt lesbaren Text ohne Markdown-Steuerzeichen.

- WLED-Start-/Beenden-Befehle verwenden gepuffertes JSON mit Content-Length, wie die Effektbefehle; verhindert HTTP-400-Ablehnung durch Controller bei Chunked-Requests.

- WLED-Start-/Beenden-Aktionen von weiterer GUI-Initialisierung entkoppelt; Lizenz- und Versandfehler verbrauchen die Aktion nicht mehr. Beenden funktioniert auch ohne erfolgreiche Startaktion; Lizenzblockaden werden sichtbar protokolliert.

- WLED, PixelIt, GIF und Awtrix: normale Punkte-Effekte erst nach drei Darts; gemeinsame Zeitsteuerung mit Ausnahmen für Bust und explizite Einzelwurfregeln; Bots folgen derselben Drei-Dart-Regel.

- Konsole: Rechtsklick kopiert die Auswahl wahlweise ohne oder mit Details/Payloads. Betriebssystemsprache wird vor der Anmeldung beim ersten Start erkannt und gespeichert; manuelle Sprachwahl bleibt erhalten.

- Headless-Anmeldung nutzt fest hinterlegte interne Authentifizierungsparameter; entsprechende nutzerseitige Startoptionen und Konfigurations-Overrides entfernt.

- Update-Pakete werden für Linux und macOS passend zur Prozessarchitektur erkannt. Online-Installer bleiben im öffentlichen Repository, aber entfallen als Release-Anhänge; erneute Veröffentlichung entfernt alte Skript-Anhänge.

- Konsole mit fest erreichbaren kompakten Filtern, Debug-/Aktionsmenüs, Mehrfachauswahl und direktem Kopieren mit optionalen Details; TUI mit zusammenhängender Textansicht für Zeilenbereiche.

- Neustart bei laufendem Match: unvollständige REST-Matchübersichten lösen keine Startansage mit geratenem Spieler mehr aus; aktiver Spieler und Restpunkte kommen aus dem vollständigen Live-Status.

- Ereignisvorlagen mit Beschreibungen; Zugang im jeweiligen Ereignis-Reiter.

- WLED, PixelIt und Awtrix: komplette Ereignisvorlagen in GUI/TUI speichern und laden; externe JSON-Bibliotheken mit Beispielen unter `event-templates`.

- PixelIt und AwtrixNG: neue Ereignisse nach jedem Wurf und beim Spielerwechsel, Dartzähler und Restpunkte je Spieler; feste Spielernummern bleiben bei veränderter Wurfreihenfolge erhalten. Korrekturen und Überwerfen nutzen Autodarts-Werte.

- AwtrixNG-Editor in GUI und TUI vereinfacht: Ton, Appname, Ausgabeart, Palette und Überlagerung entfernt. PixelIt mit lokaler LED-Matrixvorschau für Vorlagen, Texte, Helligkeit und RGB565-Bitmaps.

- AwtrixNG-Farbauswahl mit RGB-Colorpicker im WLED-Stil; Matrixvorschau aktualisiert sich bei Parameteränderungen und berücksichtigt Helligkeit sowie Scrollgeschwindigkeit. TUI mit Farbvorgaben und Hexeingabe.

- Virtuelle 32×8-LED-Matrix für AwtrixNG-Vorlagen und Anzeigeschritte: Live-Vorschau von Text/Farbe mit Laufschrift in der GUI und lokale Matrixansicht in der TUI.

- AwtrixNG trennt klar Ereignis und Anzeigevorlage, bietet passende Vorlagenvorschläge in GUI und TUI und zeigt bei exakter Punktzahl nur ein Eingabefeld.

- PixelIt verarbeitet auch abgeschlossene Bot-Turns ohne einzelne Wurfdaten, einschließlich null Punkten. Neueste Turns werden anhand der Zeit/Turnnummer zugeordnet; Regeln gelten für alle Spieler, sofern kein Name gefiltert ist.

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
- Windows-Online-Installer startet auch über `irm | iex`; Installer-Dateien sind im öffentlichen Repository für den Online-Installer verfügbar.
- Gemeinsame Installationsadresse get.darts-hub.de mit automatischer Skriptauswahl und Browser-Anleitung.
- Online-Installer erkennt Betriebssystem und Architektur und bietet GUI, TUI, Headless, Beta-Versionen und Autostart an.
- Autodarts-Anmeldung mit gespeicherter Verbindung und direkten Spielereignissen.
- Caller, WLED, PixelIt, AwtrixNG und GIF mit Einstellungen in GUI, TUI und Headless.
- Eigene Anwendungen und Skripte starten gemeinsam mit DartsHub und werden beim Beenden geschlossen.
- Startverzögerung hält Module, eigene Autostart-Anwendungen und Updateprüfung zurück.
- Getrennte Erweiterungslogs, Support-Diagnose und Import alter Konfigurationen.
- Kompakte Betriebssystem-Pakete ohne Dokumentationsdateien; Updates kommen aus dem öffentlichen Release-Repository.

### English

- Web interface for GUI and headless on port 8079: shared design, extension settings, Autodarts login, console, licensing, support and German/English. Direct network access without an access code; web assets are embedded in the executable.

- Detailed German and English soundpack guides covering filenames, events, fallbacks, single-dart modes, player names, checkout, blind support and ambient, plus custom pack setup for GUI, TUI and headless.

- Caller: new darts replace active single-dart announcements and stale individual darts are skipped. Turn totals, busts and winner announcements remain protected. Ambient sounds play in parallel on an independent audio channel.

- Console context menu copies selected messages with or without details/payloads. First launch detects and saves OS language before login; manual language choices persist.

- Headless login uses built-in authentication parameters; user-facing startup options and configuration overrides removed.

- Update packages support Linux and macOS process architectures. Online installers remain public repository files but are no longer release attachments; reruns remove legacy script attachments.

- Console with compact persistent filters, debug/action menus, multiple selection and direct copying with optional details; TUI adds a combined text view for row ranges.

- Restarting during a match: incomplete REST match overviews no longer trigger start announcements with a guessed player; active player and remaining points come from the complete live state.

- Event template descriptions; library access moved into each extension’s event tab.

- WLED, PixelIt and Awtrix: save and load complete event rules in GUI/TUI; external example libraries under `event-templates`, preserved by installer upgrades.

- PixelIt and AwtrixNG: per-dart and player-change events, dart counts and remaining points for each player; fixed player numbers survive throwing-order changes. Corrections and busts use authoritative Autodarts values.

- Simplified AwtrixNG editors in GUI and TUI: removed sound, app name, output mode, palette and overlay controls. PixelIt gains local LED matrix previews for templates, text, brightness and RGB565 bitmaps.

- AwtrixNG RGB color picker matching WLED; matrix preview updates on parameter changes and respects brightness and scroll speed. TUI offers color presets and hex input.

- Virtual 32×8 LED matrix for AwtrixNG templates and display steps: live text/color preview with scrolling in the GUI and a local matrix view in the TUI.

- AwtrixNG clearly separates events from display templates, offers matching template suggestions in GUI and TUI, and uses a single input for exact scores.

- PixelIt handles completed bot turns without individual throws, including zero scores. Latest turns are selected by timestamp/turn number; rules cover all players unless filtered by name.

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
- Windows online installer works through `irm | iex`; installer scripts are published as public repository files for the online installer.
- Shared get.darts-hub.de installation URL with automatic script selection and browser instructions.
- Online installer detects OS and architecture and offers GUI, TUI, headless, beta releases and login autostart.
- Persistent Autodarts login and direct match events.
- Caller, WLED, PixelIt, AwtrixNG and GIF configuration through GUI, TUI and headless operation.
- Custom applications and scripts start with DartsHub and close when it exits.
- Startup countdown delays modules, custom startup applications and update checks.
- Separate extension logs, support diagnostics and legacy configuration import.
- Compact platform packages without documentation; updates use the public release repository.
