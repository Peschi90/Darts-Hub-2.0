# Changelog – Darts-Hub 2.0

## v0.1.0-beta.56

<!-- Geplante nächste Version. Bei Bedarf vor dem Release anpassen. / Planned next version; adjust before release if needed. -->

### Deutsch

#### Allgemein / General

- GIF-Vorlagen bleiben in Geräteausgabe und Matrixvorschau rein grafisch; Textüberschreibungen und Ersatztexte werden unterdrückt.

- Ereignisse speichern nur zum Auslöser passende Bedingungen. Alte Einstellungen werden beim Start bereinigt; Backups und HubX-Exporte enthalten keine ungenutzten Standardwerte mehr.

- Ausgaben eigener Anwendungen verfälschen die Telemetrie-Fehlerstatistik nicht mehr. Webseiten können optional mit Darts-Hub geschlossen werden.

- Änderungen an Schnittstellen werden künftig auch auf Verträglichkeit mit der neuen mobilen App geprüft.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Autodarts

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Caller

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### WLED

- Einzelwurf-Scorebereich aus der Triggerauswahl entfernt; für neue Einzelwurf-Effekte DMU verwenden. Gespeicherte und importierte ältere Regeln bleiben erhalten.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### PixelIt

- Ereignisse unterstützen zufällige Effektvarianten. Zusammengehörige Schritte laufen als Sequenz mit gemeinsamer Auswahl für alle Zielgeräte.

- Exakte Scores zeigen eine Punktzahl; die zweite Grenze erscheint nur bei Scorebereichen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### AwtrixNG

- Ereignisse unterstützen zufällige Effektvarianten. Zusammengehörige Schritte laufen als Sequenz mit gemeinsamer Auswahl für alle Zielgeräte.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GIF

- Exakte Scores zeigen eine Punktzahl; die zweite Grenze erscheint nur bei Scorebereichen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### darts-voice / darts-extern

- Einstellungsseiten folgen jetzt dem gewohnten Moduldesign mit Reitern, kompakten Karten, kontextbezogener Hilfe sowie passenden Zahlen-, Auswahl- und Pfadfeldern.
- Offline-Sprachsteuerung für Spiel, Board, Wurfkorrekturen und Caller mit eigenen Schlüsselwörtern in GUI und TUI.
- Aufnahmen aus Autodarts nach Lidarts, Nakka und Dartboards übertragen; endgültige Korrekturen vor Takeout, Spieler-/Boardfilter und Schutz vor Doppelübertragungen.
- Alte Moduleinstellungen importieren und sichern; Anmeldedaten bleiben ausgeschlossen und übernommene Module zunächst deaktiviert. Python-Pakete, Sprachmodell und Browser werden separat eingerichtet.

#### Eigene Anwendungen / External Apps

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Die Android-App zeigt klar getrennte, einzeln aufklappbare Ereignisregeln. Entwürfe und der offene Zustand bleiben beim Sortieren erhalten. Exakte Scores heißen verständlich „Punktzahl“.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Einstellungen und Import / Settings and Import

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Updates und Installation / Updates and Installation

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Lizenz und Support / Licensing and Support

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

### English

#### Allgemein / General

- GIF templates remain image-only in device output and matrix previews; text overrides and fallback labels are suppressed.

- Events store only conditions used by their trigger. Existing settings are cleaned on startup; backups and HubX exports omit unused default values.

- External application output no longer distorts telemetry error statistics. Websites can optionally close with Darts-Hub.

- Interface changes now require compatibility review with the new mobile app.

<!-- Add brief user-facing changes here. -->

#### Autodarts

<!-- Add brief user-facing changes here. -->

#### Caller

<!-- Add brief user-facing changes here. -->

#### WLED

- Removed single-dart score ranges from trigger selection; use DMU for new single-dart effects. Saved and imported legacy rules remain intact.

<!-- Add brief user-facing changes here. -->

#### PixelIt

- Events support random effect variants. Grouped steps play as a sequence with one shared selection across target devices.

- Exact scores show one score value; a second boundary appears only for score ranges.

<!-- Add brief user-facing changes here. -->

#### AwtrixNG

- Events support random effect variants. Grouped steps play as a sequence with one shared selection across target devices.

<!-- Add brief user-facing changes here. -->

#### GIF

- Exact scores show one score value; a second boundary appears only for score ranges.

<!-- Add brief user-facing changes here. -->

#### darts-voice / darts-extern

- Settings pages now follow the familiar module layout with tabs, compact cards, contextual help and appropriate numeric, choice and path controls.
- Offline voice control for games, board, dart corrections and Caller, with custom keywords in GUI and TUI.
- Transfer Autodarts visits to Lidarts, Nakka and Dartboards, respecting corrections before takeout, player/board filters and duplicate protection.
- Import and back up legacy module settings; credentials stay excluded and imported modules remain disabled. Python packages, speech model and browser require separate setup.

#### Eigene Anwendungen / External Apps

<!-- Add brief user-facing changes here. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- The Android app now shows clearly separated event rules that expand independently. Drafts and expansion follow rules when reordered. Exact scores use a clear “Score” label.

<!-- Add brief user-facing changes here. -->

#### Einstellungen und Import / Settings and Import

<!-- Add brief user-facing changes here. -->

#### Updates und Installation / Updates and Installation

<!-- Add brief user-facing changes here. -->

#### Lizenz und Support / Licensing and Support

<!-- Add brief user-facing changes here. -->
