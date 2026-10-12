# Changelog – Darts-Hub 2.0

## v0.1.0-beta.36

<!-- Geplante nächste Version. Bei Bedarf vor dem Release anpassen. / Planned next version; adjust before release if needed. -->

### Deutsch

#### Allgemein / General

- HubX-Rechtstexte direkt in Darts-Hub bestätigen und anschließend teilen. Fehler beim Teilen erscheinen nur einmal. Nach der Erfolgsmeldung schließen sich die Teilen-Dialoge.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Autodarts

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Caller

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### WLED

- HubX-Uploads übertragen Vorschau-Daten mit fester Größe. Unlesbare JSON-Daten werden klar gemeldet; die Konsole zeigt den betroffenen Übermittlungsschritt.

- Beim Teilen mit Controller-Vorschau wird eine veraltete HubX-Webseite klar gemeldet. Upload-Ablehnungen sind auch in der Konsole sichtbar.

- HubX-Uploads senden ungenutzte Vorschau-Aufnahmen nicht mehr als leeres Feld, um Ablehnungen älterer Server zu vermeiden.

- Beim Teilen wird die LED-Anzahl übernommen. Optional echte Effektvorschauen vom Controller aufnehmen; anschließend werden die vorherigen Einstellungen wiederhergestellt.

- Ereignisse mit den verwendeten Presets direkt auf HubX teilen. Beim Import belegter Preset-IDs eine freie ID wählen; das Ereignis wird automatisch angepasst.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### PixelIt

- Release-Prüfung für ältere Pixelit-Vorlagennamen korrigiert; bearbeitete Ereignisse bleiben beim Umsortieren erhalten.

- Ereignisse mit ihren Anzeigevorlagen direkt auf HubX teilen.
- Zusätzliche Bildschirmoptionen werden je Sequenzschritt gespeichert und gemeinsam für Anzeige und Vorschau angewendet; ungültige Werte werden abgewiesen.
- Anzeigeparameter komfortabel bearbeiten, Vorlagenwerte erben und einzeln zurücksetzen. Erweiterte JSON-Optionen bleiben erhalten; Desktop und Terminal zeigen farbige Animationen und verständliche Vorschaugrenzen.
- Die Matrixvorschau berücksichtigt Animationstempo, Pingpong, begrenzte Wiederholungen und laufenden Text. Uhrvorschauen verwenden eine lokale Referenzzeit; Darstellungsgrenzen werden ausgewiesen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### AwtrixNG

- Ereignisse samt Anzeigevorlagen und Controller-GIFs direkt auf HubX teilen. GIFs erscheinen zusätzlich einzeln.

- Die Matrixvorschau zeigt die ausgewählten animierten Icons, Farben und Effekte und berücksichtigt Iconbewegung, Scrolltempo und Einstellungen der Uhr.

- Beim Schließen von Darts-Hub werden pausierte Uhr-Apps im Modus „Solange Darts-Hub aktiv ist“ zuverlässig wiederhergestellt.
- Uhr-Apps lassen sich während des Matches (ab Bull-off), solange Darts-Hub läuft oder dauerhaft pausieren. Die vorherige Konfiguration kann wiederhergestellt werden.
- Optionen stehen direkt hinter den Ereignissen; selten benötigte Einstellungen sind erklärt und eingeklappt. Geräteeinstellungen zeigen einen Warnhinweis.


<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GIF

- Ereignisse mit festen Bilddateien direkt auf HubX teilen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Eigene Anwendungen / External Apps

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- HubX-GIFs behalten verständliche Dateinamen; Namenskonflikte lassen sich mit Bildvergleich, Umbenennen oder Überschreiben lösen. Anzeigenvorlagen erhalten den Zusatz `_hubX`.
- HubX-Inhalte an die eigene Installation senden und in einem Dialog prüfen, übernehmen, ablehnen oder später bearbeiten; neue Ereignisse werden sofort geladen.

- HubX-Titel und Ereignisauswahl starten leer, damit nur bewusst ausgewählte Inhalte geteilt werden.
- Der HubX-Dialog führt mit übersichtlichen Karten durch Auswahl, Prüfung und Veröffentlichung. Ein eigener Ergebnisdialog bestätigt den Upload oder erklärt den Fehler.
- HubX-Uploadfehler zeigen den konkreten Grund; abgelehnte Uploads können erneut versucht werden.

- Teilen-Dialog in GUI, Terminal und Weboberflächen: Inhalte auswählen, prüfen und frei für alle veröffentlichen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Einstellungen und Import / Settings and Import

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Updates und Installation / Updates and Installation

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Lizenz und Support / Licensing and Support

- HubX-Teilen mit dem Lizenzfeature hubx_access; geteilte Inhalte sind immer öffentlich und frei verwendbar.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

### English

#### Allgemein / General

- Confirm HubX legal documents directly in Darts-Hub and continue sharing. Sharing errors appear only once. Sharing dialogs close after the success message.

<!-- Add brief user-facing changes here. -->

#### Autodarts

<!-- Add brief user-facing changes here. -->

#### Caller

<!-- Add brief user-facing changes here. -->

#### WLED

- HubX uploads send preview data with a fixed size. Unreadable JSON is clearly reported; the console identifies the failed transfer step.

- Sharing controller previews clearly reports an outdated HubX website. Upload rejections also appear in the console.

- HubX uploads omit unused preview recordings to avoid rejection by older servers.

- Optionally record actual controller effects for HubX previews; previous settings are restored afterwards.

- Sharing includes the source controller LED count for the HubX preview.

- Share events with their selected presets on HubX. Choose a free preset ID during import when an ID is occupied; the event is updated automatically.

<!-- Add brief user-facing changes here. -->

#### PixelIt

- Fixed release checks for older Pixelit template names; edited events remain intact when reordered.

- Share events with their display templates directly on HubX.
- Additional screen options are saved per sequence step and applied consistently to displays and previews; invalid values are rejected.
- Edit display parameters comfortably, inherit template values and reset individual fields. Advanced JSON options are preserved; desktop and terminal show color animations and readable preview limitations.
- The matrix preview respects animation timing, ping-pong, limited loops and scrolling text. Clock previews use a local reference time; rendering limitations are reported.

<!-- Add brief user-facing changes here. -->

#### AwtrixNG

- Share events with display templates and controller GIFs directly on HubX. GIFs also appear separately.

- The matrix preview displays selected animated icons, colors and effects and respects icon movement, scrolling speed and clock settings.

- Closing Darts-Hub restores paused clock apps in “While Darts-Hub is running” mode before exiting.
- Clock apps can be paused during matches (from bull-off onwards), while Darts-Hub runs, or permanently. The previous configuration can be restored.
- Options follow events; advanced settings are explained and collapsed. Device settings show a caution notice.


<!-- Add brief user-facing changes here. -->

#### GIF

- Share events with fixed image files directly on HubX.

<!-- Add brief user-facing changes here. -->

#### Eigene Anwendungen / External Apps

<!-- Add brief user-facing changes here. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- HubX images keep their original names; resolve name conflicts with image previews, renaming or explicit overwriting. Display templates use the `_hubX` suffix.

- Send HubX content to your installation and review, import, decline or defer it in a dialog; new events are loaded immediately.

- HubX titles and event selections start empty so only deliberately selected content is shared.
- The HubX dialog uses clear cards for selecting, reviewing and publishing content. A dedicated result dialog confirms the upload or explains the failure.
- HubX upload errors show the specific reason; rejected uploads can be retried.

- Sharing dialog in GUI, terminal and web interfaces: select, review and release content freely for everyone.

<!-- Add brief user-facing changes here. -->

#### Einstellungen und Import / Settings and Import

<!-- Add brief user-facing changes here. -->

#### Updates und Installation / Updates and Installation

<!-- Add brief user-facing changes here. -->

#### Lizenz und Support / Licensing and Support

- Share on HubX with the hubx_access license feature; shared content is always public and free to use.

<!-- Add brief user-facing changes here. -->
