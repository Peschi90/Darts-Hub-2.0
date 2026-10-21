# Changelog – Darts-Hub 2.0

## v0.1.0-beta.52

<!-- Geplante nächste Version. Bei Bedarf vor dem Release anpassen. / Planned next version; adjust before release if needed. -->

### Deutsch

#### Allgemein / General

- Ein Dokumentations-Wegweiser in der README erklärt die Anleitungen in sinnvoller Reihenfolge.

- Die Web-Supportseite führt mit klarer Aufteilung, Datenschutzinformationen und sichtbarem Diagnosefortschritt durch die Anfrage.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Autodarts

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Caller

- Die Caller-Webseite bietet eine hervorgehobene Soundpack-Auswahl, übersichtliche Themenreiter und kompakte Audio-Einstellungen.


- Soundpack-Downloads zeigen getrennten Fortschritt für Herunterladen, Entpacken und Installation. Der neue Webdialog meldet Erfolg oder Fehler und aktualisiert die Soundpack-Liste automatisch; GUI und Terminal zeigen denselben Phasenfortschritt.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### WLED

- Die Weboberfläche bietet eine Setup-Übersicht, kompakte Gerätekarten und Ereignisse sowie einen eigenen Bereich für gespeicherte Ereignisvorlagen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### PixelIt

- Die Weboberfläche bündelt Geräte, Ereignisse und Vorlagen im neuen Caller-Stil mit direktem HubX-Zugang.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### AwtrixNG

- Die Weboberfläche zeigt Geräte und Ereignisse übersichtlicher; Einstellungen der Uhr haben einen eigenen Reiter.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GIF

- Die Weboberfläche zeigt Ereignisse, Anzeigeoptionen und Medien in übersichtlichen Themenbereichen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Eigene Anwendungen / External Apps

- Konfiguration und Laufstatus sind in der Weboberfläche getrennt und im neuen Kartenstil gestaltet.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Netzwerk-GUIs bleiben verbunden, wenn die ausschließlich lokale Skriptverwaltung nicht zugänglich ist. Zeitüberschreitungen beenden die Wiederverbindung nicht mehr dauerhaft.

- GUI, TUI und Headless stellen das Backend automatisch im LAN bereit. Eine zweite GUI verbindet sich mit `bip=IPADRESSE` ohne Host-Einstellungen, Token oder Bestätigung; ältere Hosts werden auch über ihren Webzugang gefunden.

- Terminaloberfläche beim Starten und Schließen stabilisiert; Abstürze liefern jetzt ein bereinigtes Fehlerprotokoll.


<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Einstellungen und Import / Settings and Import

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Updates und Installation / Updates and Installation

- Release-Prüfungen berücksichtigen die LAN-Erreichbarkeit in GUI, TUI und Headless korrekt.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Lizenz und Support / Licensing and Support

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

### English

#### Allgemein / General

- The README now guides you through the documentation in a useful reading order.

- The web support page guides requests with a clear layout, privacy information and visible diagnostic progress.

<!-- Add brief user-facing changes here. -->

#### Autodarts

<!-- Add brief user-facing changes here. -->

#### Caller

- The Caller web page now offers a prominent soundpack overview, themed tabs and compact audio settings.


- Soundpack downloads show separate progress for downloading, extraction and installation. The new web dialog reports success or errors and refreshes the soundpack list automatically; GUI and terminal show the same phase progress.

<!-- Add brief user-facing changes here. -->

#### WLED

- The web interface adds a setup overview, compact device and event cards, and a dedicated area for saved event templates.

<!-- Add brief user-facing changes here. -->

#### PixelIt

- The web interface groups devices, events and templates in the new Caller style with direct HubX access.

<!-- Add brief user-facing changes here. -->

#### AwtrixNG

- The web interface presents devices and events more clearly; clock settings have their own tab.

<!-- Add brief user-facing changes here. -->

#### GIF

- The web interface presents events, display options and media in clear themed sections.

<!-- Add brief user-facing changes here. -->

#### Eigene Anwendungen / External Apps

- Configuration and runtime status have separate tabs in the web interface with the new card design.

<!-- Add brief user-facing changes here. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Network GUIs stay connected when local-only script management is unavailable. Request timeouts no longer permanently stop reconnection.

- GUI, TUI and headless automatically expose the backend on the LAN. A second GUI connects with `bip=IPADDRESS` without host settings, tokens or confirmation; older hosts can also be reached through their web listener.

- Stabilized terminal startup and shutdown; crashes now provide a redacted diagnostic log.


<!-- Add brief user-facing changes here. -->

#### Einstellungen und Import / Settings and Import

<!-- Add brief user-facing changes here. -->

#### Updates und Installation / Updates and Installation

- Release checks correctly account for LAN access in GUI, TUI and headless mode.

<!-- Add brief user-facing changes here. -->

#### Lizenz und Support / Licensing and Support

<!-- Add brief user-facing changes here. -->
