# Changelog – Darts-Hub 2.0

## v0.1.0-beta.41

<!-- Geplante nächste Version. Bei Bedarf vor dem Release anpassen. / Planned next version; adjust before release if needed. -->

### Deutsch

#### Allgemein / General

- Release-Prüfungen der WLED-Vorschau sind unabhängig von der Geschwindigkeit des Build-Servers zuverlässiger.

#### Autodarts

- Abgelehnte gespeicherte Anmeldungen werden automatisch erneuert. Ist die Anmeldung nicht mehr gültig, wird eine erneute Anmeldung verlangt.

#### Caller

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### WLED

- Beim Teilen auf HubX wird ein verknüpftes Preset zusätzlich einzeln mit derselben Vorschau angeboten. Einzelne Presets werden ohne Ereignis auf den Controller geladen; belegte IDs bleiben geschützt.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### PixelIt

- HubX bietet angepasste Anzeigevorlagen zusätzlich einzeln an. Beim Übernehmen werden sie direkt in der Vorlagenbibliothek gespeichert, ohne neue Ereignisregel.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### AwtrixNG

- Sequenztests und GIF-Uploads funktionieren auch, wenn die Firmware ihre Displaygröße erst über das aktuelle Displaybild meldet.
- Einzelne HubX-GIFs können direkt auf einen ausgewählten AWTRIX-NG-Controller geladen werden; gleiche Namen lassen sich vergleichen, überschreiben oder ändern.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GIF

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Eigene Anwendungen / External Apps

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Einstellungen und Import / Settings and Import

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Updates und Installation / Updates and Installation

- Die vollständige Entfernung funktioniert auch mit den üblichen macOS-Verzeichnissen; fremde Verknüpfungen und Systemordner bleiben geschützt.
- Die lokale Weboberfläche meldet neue Updates automatisch; Headless-Systeme lassen sich direkt mit --update aktualisieren und mit --uninstall vollständig entfernen. Beide Befehle sind in der README erklärt.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Lizenz und Support / Licensing and Support

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

### English

#### Allgemein / General

- WLED preview release checks are more reliable regardless of build-server speed.

#### Autodarts

- Rejected saved logins are renewed automatically. If the login is no longer valid, signing in again is required.

#### Caller

<!-- Add brief user-facing changes here. -->

#### WLED

- Sharing on HubX also publishes linked presets separately with the same preview. Standalone presets upload without creating an event; occupied IDs remain protected.

<!-- Add brief user-facing changes here. -->

#### PixelIt

- HubX also offers adjusted display templates separately. Imports save them directly to the template library without adding an event.

<!-- Add brief user-facing changes here. -->

#### AwtrixNG

- Sequence tests and GIF uploads also work when the firmware reports its display size through the current screen image.
- Standalone HubX GIFs can be uploaded directly to a selected AWTRIX NG controller; matching filenames can be compared, overwritten or renamed.

<!-- Add brief user-facing changes here. -->

#### GIF

<!-- Add brief user-facing changes here. -->

#### Eigene Anwendungen / External Apps

<!-- Add brief user-facing changes here. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

<!-- Add brief user-facing changes here. -->

#### Einstellungen und Import / Settings and Import

<!-- Add brief user-facing changes here. -->

#### Updates und Installation / Updates and Installation

- Complete removal also works with standard macOS directory aliases; unrelated links and system folders remain protected.
- The local web interface automatically announces updates; headless systems can update directly with --update or remove the installation with --uninstall. Both commands are documented in the README.

<!-- Add brief user-facing changes here. -->

#### Lizenz und Support / Licensing and Support

<!-- Add brief user-facing changes here. -->
