# Changelog – Darts-Hub 2.0

## v0.1.0-beta.65

<!-- Geplante nächste Version. Bei Bedarf vor dem Release anpassen. / Planned next version; adjust before release if needed. -->

### Deutsch

#### Allgemein / General

- Release-Prüfungen für Windows, Linux und macOS korrigiert. Der lokale Start verkraftet vorübergehend langsame Antworten des Backends.

- Support-Sammlungen enthalten ausgewählte Modul-Logs ohne zusätzliche Leerzeilen; vollständige Autodarts-Spielzustände sind wie Rohdaten nur mit passender Freischaltung sichtbar.


- Release-Prüfungen für die erweiterten Matrix-Farbwähler korrigiert; das Öffnen der WLED-Ereignisse erzeugt keine falsche Änderungsmeldung mehr.

- Farbauswahl auch in bisherigen reinen Farbeingabefeldern; Terminal-Farbpalette mit eigener Eingabe und Erhalt des WLED-Weißkanals.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Autodarts

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Caller

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Hub75

- Die Einstellung zum Tauschen der logischen Matrixachsen wird auf Deutsch und Englisch beschriftet.

- HubX-Effekte entdecken und Ereignisse teilen direkt über die hervorgehobenen Buttons im Hub75-Kopfbereich.


- Die Helligkeit im Hub75-Modul ist auf 150 begrenzt. Ältere höhere Einstellungen werden beim Laden angepasst.
- Die Hub75-GIF-Verwaltung lädt die Dateien vom Controller wieder. Hochladen und Löschen sind ebenfalls wieder erreichbar.
- MatrixMind zeigt Trefferzoom, 180, Big Fish und weitere Animationen für manuell eingetragene Darts genauso wie für automatisch erkannte Würfe.
- Hub75 behält die Aufnahmehistorie beim Spielerwechsel. In der Layoutvorschau wird das ausgewählte Text- oder Balkenfeld umrandet.
- Bei vertauschter Auflösung kann der HubX-Import die logische Matrix nach Bestätigung um 90° drehen.
- Der Hub75-Live-Spielstand zeigt pro Spieler bis zu zehn Aufnahmen, die jüngste zuerst.
- Hub75 zeigt beim HubX-Import beide Auflösungen, wenn das Layout nicht zum Ziel passt. Der Live-Spielstand bietet Chalkboard-Platzhalter für bis zu sechs Spieler.
- HubX Studio bietet 32 Farbpaletten und 28 Pixeleffekte für alle Ebenen. Funken, Matrix-Regen und andere Partikel lassen darunterliegende Ebenen sichtbar. Fett, Schrägschrift und Unterstreichen behalten ihre Konturen.
- Hub75 sendet berechnete Layouts und Matrixtext per DDP. Gespeicherte GIFs und WLED-Effekte laufen direkt auf dem Controller.
- HubX zeigt animierte Layout- und GIF-Vorschauen. Das Studio bietet Hintergrundeffekte, Paletten und Pixelschriften, erklärt ungültige Größen und speichert vollständige Ereignisbedingungen.
- Hub75-Trigger werden beim Import übersetzt. Geteilte Ereignisse enthalten ihre Controller-GIFs, die auch in der GIF-Kategorie erscheinen.
- Hub75 trennt MatrixMind von Ereignissen. Im Ereignismodus stehen die Matrixeffekte des Controllers, Text, GIFs und eigene HubX-Layouts zur Wahl.
- HubX Studio erstellt Hub75-Layouts mit Pixelauflösung, Ebenen, Balken und animierten Texten. Vorlagen und Ereignisse haben eigene Kategorien.

- MatrixMind-Vorschaubilder werden beim Scrollen wiederverwendet und beim Verlassen der Seite freigegeben. Das reduziert Rechenaufwand und Speicherbedarf bei unveränderten Farben und Auflösungen.

- Panelkonfigurationen werden im von WLED unterstützten Format übertragen. Abgelehnte Anfragen erscheinen nicht mehr als Verbindungsfehler; die Konsole nennt Aufruf und HTTP-Status.

- Panelwerte lassen sich ohne springende Eingabefelder bearbeiten; das ausgewählte Gerät bleibt beim Synchronisieren erhalten. Übertragung, fehlende Neustartbestätigung und Fehler sind direkt am Übertragen-Knopf sichtbar. Neustartbedingte Verbindungsabbrüche werden durch Rücklesen geprüft.

- MatrixMind 1.3.0 unterstützt 1, 2 oder 3 Panels mit passenden Vorschauen, 18 Designs und 8 Schriftoptionen für die breiten Anzeigen; ein Panel nutzt das originale Kompaktlayout.

- MatrixMind bietet eine Bildschirmvorschau mit Beispieldaten, Helligkeitsregler, Effektnamen, Controllerprüfung und Pause/Fortsetzen der Ausgabe; Größenfehler beim Speichern erklären jetzt die Einrichtung und die passende Panel-Anordnung.

- MatrixMind läuft direkt in Darts-Hub ohne Python-Installation; Originalanimationen und Pixelausgabe werden gegen die ursprüngliche Version geprüft.

- Das Geräte-Livebild unterstützt vollständige Controllerbilder für GIFs, WLED-Effekte und MatrixMind. Für große Matrizen ist die gesonderte DHLive1-Firmware-Erweiterung nötig; reduzierte Bilder zeigen stattdessen einen verständlichen Hinweis. Keine automatische Firmwareinstallation.
- MatrixMind führt durch Einrichten, Darstellung und Ausgabe & Test. Eine Aktion aktiviert alle nötigen Schalter; Paneltests übernehmen zuvor die gewählten Einstellungen, auch im Terminal.
- Beispielvorschau und laufende MatrixMind-Ausgabe sind getrennt und zeigen unveränderte Farben. Langsame Controllerabfragen unterbrechen den Bildversand nicht mehr.

- MatrixMind bringt das originale Scoreboard von BernyBoneBreaker mit direkten Autodarts-Spieldaten, Animationen, Demos und Diagnose in GUI und Terminal.
- Geräte-GIFs lassen sich jetzt auch bei Hub75 hochladen, herunterladen und verwalten; breite Panelketten bis 256 Spalten sind unterstützt.

- „Gerät hinzufügen“ öffnet die Auswahl für die geführte oder manuelle Einrichtung. Der Assistent zeigt einen animierten Hinweis zum passenden Controller und den gekennzeichneten Affiliate-Link am Foto.
- Die Hub75-Geräteübersicht zeigt MatrixMind oder Ereignisregeln als Anzeigemodus.
- Die Hub75-Betriebsoptionen bieten Modulstandards und eigene Werte je Gerät. Debug-, Board- und Ausschaltoptionen beim Start und nach dem Spiel entfallen für Hub75.

- Der Einrichtungsassistent öffnet sich in einem eigenen Dialog mit dauerhaft sichtbaren Zurück-/Weiter-Schaltflächen; die Geräteseite bleibt übersichtlich.

- Neues Matrixmodul mit optionalem Einrichtungsassistenten, Verdrahtungshilfe, USB-Flashen, WLAN-Einrichtung und geprüfter Panel-/2D-Konfiguration in GUI und Terminal.
- Beim Hinzufügen zwischen geführter und manueller Einrichtung wählen; nach erfolgreicher Prüfung direkt zu den Ereignissen. Das Matrix-Livebild aktualisiert sich fortlaufend und lässt sich starten und stoppen.
- Verständlichere Einrichtung mit Boardfoto, kurzen nummerierten Anweisungen, Verkabelungsschema und einer Vorschau der Panelanordnung. Technische Details lassen sich bei Bedarf aufklappen; dieselben Anleitungen sind im Terminal verfügbar.

#### WLED

- Geräteaktionen bleiben vollständig innerhalb ihrer Karte und brechen bei Bedarf um; Matrix-Hilfetexte erscheinen nur bei erkannten Matrizen.

- GIF-Dateien vom Controller direkt herunterladen; breite Matrixbereiche bis 256 Spalten bearbeiten.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### PixelIt

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### AwtrixNG

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GIF

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Eigene Anwendungen / External Apps

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Ereignisse nach Zielgerät filtern; kompakte Beispielvorschauen in eingeklappten Regeln pausieren außerhalb des sichtbaren Bereichs. Die TUI bietet den Gerätefilter ohne Miniaturen.


- Schwebender Nach-oben-Pfeil und direkter Sprung zu neu angelegten Ereignisregeln; die TUI öffnet neue Regeln sofort.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Einstellungen und Import / Settings and Import

- Nicht gesetzte v1-Optionen werden beim automatischen Umstieg übersprungen, statt den Import abzubrechen.
- Installiert der v1-Umstieg eine Beta, aktiviert Darts-Hub Beta-Updates. Stabile Versionen bleiben im Beta-Kanal verfügbar.

- Der automatische v1-Umstieg ist für ein separates Brückenupdate vorbereitet. Die Anleitung erklärt den Ablauf und die Voraussetzungen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Updates und Installation / Updates and Installation

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Lizenz und Support / Licensing and Support

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

### English

#### Allgemein / General

- Corrected release checks for Windows, Linux and macOS. Local startup now tolerates temporarily slow backend responses.

- Support collections include selected module logs without extra blank lines; full Autodarts game states require the same access feature as raw payloads.


- Corrected release checks for the additional matrix color pickers; opening WLED events no longer incorrectly reports unsaved changes.

- Color pickers for remaining plain color fields; keyboard palette with custom input and preserved WLED white channel.

<!-- Add brief user-facing changes here. -->

#### Autodarts

<!-- Add brief user-facing changes here. -->

#### Caller

<!-- Add brief user-facing changes here. -->

#### Hub75

- The setting for swapping the logical matrix axes now shows its label in German and English.

- Discover HubX effects and share events directly from prominent buttons in the Hub75 header.


- The HUB75 module caps brightness at 150 and lowers higher saved settings when loading them.
- HUB75 GIF management loads files from the controller again. Upload and delete also work again.
- MatrixMind shows hit zoom, 180, Big Fish and other animations for manually entered darts just as it does for automatically detected throws.
- HUB75 keeps visit history when players switch. The layout preview outlines the selected text or bar field.
- When dimensions are swapped, HubX import can rotate the logical matrix by 90° after confirmation.
- The HUB75 live scoreboard shows up to ten visits per player, newest first.
- HUB75 imports show both resolutions when a layout does not fit the target. The live scoreboard adds chalkboard placeholders for up to six players.
- HubX Studio offers 32 color palettes and 28 pixel effects on every layer. Sparkles, matrix rain and other particles reveal layers below. Bold, slant and underline preserve glyph outlines.
- HUB75 sends rendered layouts and matrix text over DDP. Stored GIFs and WLED effects run on the controller.
- HubX shows animated layout and GIF previews. Studio adds backgrounds, palettes and pixel fonts, explains invalid sizes and saves complete event conditions.
- HUB75 triggers are translated on import. Shared events include their controller GIFs, which also appear in the GIF category.
- HUB75 separates MatrixMind from event rules. Event mode offers the controller’s matrix effects, text, GIFs and custom HubX layouts.
- HubX Studio builds HUB75 layouts with pixel dimensions, layers, bars and animated text. Templates and events have dedicated categories.

- MatrixMind previews are reused while scrolling and released when leaving the page, reducing rendering work and memory use while preserving colors and resolution.

- Panel settings use the transfer format supported by WLED. Rejected requests no longer appear as connection failures; the console identifies the request and HTTP status.

- Panel fields stay stable while editing, and synchronization preserves the selected device. Transfer progress, missing restart confirmation and errors appear beside the apply button. Restart connection drops are checked by reading back the controller settings.

- MatrixMind 1.3.0 supports 1, 2 or 3 panels with matching previews, 18 designs and 8 font options for wide displays; one panel uses the original compact layout.

- MatrixMind adds an on-screen sample preview, brightness slider, effect names, controller checks and pause/resume; layout errors when saving now explain setup and the matching panel arrangement.

- MatrixMind runs directly inside Darts-Hub without installing Python; original animations and pixel output are checked against the original version.

- Device live view supports complete controller frames for GIFs, WLED effects and MatrixMind. Large matrices require the separate DHLive1 firmware extension; reduced frames show an actionable message instead. Firmware is not installed automatically.
- MatrixMind separates Setup, Appearance and Output & test. One action enables all required switches; panel tests first apply the selected settings, including in the terminal.
- Sample previews and current MatrixMind output stay separate and use unmodified colors. Slow controller queries no longer interrupt frame transmission.

- MatrixMind adds BernyBoneBreaker’s original scoreboard with direct Autodarts game data, animations, demos and diagnostics in GUI and terminal.
- Hub75 now supports device GIF uploads, downloads and management, including wide panel chains up to 256 columns.

- “Add device” opens the guided or manual setup choice. The guide shows an animated controller compatibility notice and a labelled affiliate link next to the photo.
- The HUB75 device overview shows whether each display uses MatrixMind or event rules.
- HUB75 runtime options offer module defaults and per-device values. Debug, board and startup or post-game power-off controls are removed from HUB75.

- Setup opens in a dedicated dialog with always-visible Back/Next buttons, keeping the device page clear.

- New matrix module with an optional setup wizard, wiring guide, USB flashing, Wi-Fi setup and verified panel/2D configuration in GUI and terminal.
- Choose guided or manual setup when adding a device, then continue directly to events after verification. The matrix live view refreshes continuously and provides start/stop controls.
- Clearer setup with a board photo, short numbered instructions, a wiring schematic and a panel-layout preview. Technical details expand when needed; the same instructions are available in the terminal.

#### WLED

- Device actions stay inside their cards and wrap when needed; matrix help appears only for detected matrices.

- Download original GIF files from the controller and edit wide matrix areas up to 256 columns.

<!-- Add brief user-facing changes here. -->

#### PixelIt

<!-- Add brief user-facing changes here. -->

#### AwtrixNG

<!-- Add brief user-facing changes here. -->

#### GIF

<!-- Add brief user-facing changes here. -->

#### Eigene Anwendungen / External Apps

<!-- Add brief user-facing changes here. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Filter events by target device; compact sample previews in collapsed rules pause off-screen. The TUI offers device filtering without miniatures.


- Floating back-to-top arrow and automatic focus for newly created event rules; TUI opens new rules immediately.

<!-- Add brief user-facing changes here. -->

#### Einstellungen und Import / Settings and Import

- Unset v1 options are skipped during automatic migration instead of aborting the import.
- Migrating from v1 to a beta enables beta updates. Stable releases remain available on the beta channel.

- The automatic v1 migration is prepared for a dedicated bridge update, with updated rollout instructions and prerequisites.

<!-- Add brief user-facing changes here. -->

#### Updates und Installation / Updates and Installation

<!-- Add brief user-facing changes here. -->

#### Lizenz und Support / Licensing and Support

<!-- Add brief user-facing changes here. -->
