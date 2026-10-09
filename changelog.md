# Changelog – Darts-Hub 2.0

## v0.1.0-beta.28

<!-- Geplante nächste Version. Bei Bedarf vor dem Release anpassen. / Planned next version; adjust before release if needed. -->

### Deutsch

#### Allgemein / General

- Neue Funktionsübersichten für alle Erweiterungen mit Ereignissen, Einstellungen, Bedienung und Einschränkungen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Autodarts

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Caller

- Matchbeginn und erster Spieler werden auch ohne Bull-off direkt angesagt, ohne auf den ersten Dart zu warten.

- Caller-Sounddateien können direkt im Browser abgespielt werden, auch ohne lokale Audioausgabe. Ansagefolgen und Unterbrechungen bleiben erhalten.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### WLED

- Siegeseffekte werden bei Matchabschluss und beim Legwechsel wieder zuverlässig ausgelöst.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### PixelIt

- Spielerwechsel reagiert nur auf einen anderen Spieler. „Wurf oder Turnwechsel“ erkennt auch neue Aufnahmen desselben Spielers; Takeout ist als eigener Auslöser verfügbar. Bestehende kombinierte Regeln werden übernommen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### AwtrixNG

- Spielerwechsel reagiert nur auf einen anderen Spieler. „Wurf oder Turnwechsel“ erkennt auch neue Aufnahmen desselben Spielers; Takeout ist als eigener Auslöser verfügbar. Bestehende kombinierte Regeln werden übernommen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GIF

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Eigene Anwendungen / External Apps

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Die Online-Webapp lässt sich per QR-Code direkt mit dem Smartphone koppeln, ohne den Code abzutippen.

- Die gekoppelte Webapp erklärt bei fehlender Verbindung, wie Darts-Hub gestartet werden muss, und verbindet sich automatisch erneut.

- Die installierte Online-Webapp übernimmt die bestehende Kopplung beim ersten Öffnen ohne neuen Anmeldecode.

- Webapp-Verbindungsfehler zeigen jetzt den konkreten Ablehnungsgrund des Servers; die Anfrage ist mit PHP-Hosting kompatibler.

- Die Online-Webapp koppelt jeden Browser per einmaligem Code mit seiner eigenen Installation; Einstellungen und Caller-Audio sind über die gemeinsame HTTPS-Adresse erreichbar.

- Installation als Webapp mit Nachfrage beim Öffnen, Android-Installationsdialog und iOS-Anleitung; die Nachfrage lässt sich ausblenden.

- Browser-Audio lässt sich oben im Dashboard aktivieren und separat in der Lautstärke regeln; auch für Smartphones.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Einstellungen und Import / Settings and Import

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Updates und Installation / Updates and Installation

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Lizenz und Support / Licensing and Support

- Das Support-Dashboard zeigt Webapp-Verbindungen, aktive Browser und die letzte Nutzung je Installation.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

### English

#### Allgemein / General

- New feature guides for all extensions, covering events, settings, controls and limitations.

<!-- Add brief user-facing changes here. -->

#### Autodarts

<!-- Add brief user-facing changes here. -->

#### Caller

- Match start and the first player are announced immediately without bull-off, without waiting for the first dart.

- Caller sound files can play directly in the browser, including without local audio output. Announcement sequences and interruptions are preserved.

<!-- Add brief user-facing changes here. -->

#### WLED

- Win effects trigger reliably again at match completion and when the leg changes.

<!-- Add brief user-facing changes here. -->

#### PixelIt

- Player change only fires for a different player. “Throw or turn change” also detects new visits by the same player; Takeout is available as a separate trigger. Existing combined rules are migrated.

<!-- Add brief user-facing changes here. -->

#### AwtrixNG

- Player change only fires for a different player. “Throw or turn change” also detects new visits by the same player; Takeout is available as a separate trigger. Existing combined rules are migrated.

<!-- Add brief user-facing changes here. -->

#### GIF

<!-- Add brief user-facing changes here. -->

#### Eigene Anwendungen / External Apps

<!-- Add brief user-facing changes here. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Pair the online web app directly by scanning a QR code with your phone, without typing a code.

- The paired web app explains how to start Darts-Hub when it is unreachable and reconnects automatically.

- The installed online web app inherits its pairing on first launch without a new sign-in code.

- Web app connection errors now show the server rejection reason; requests are more compatible with PHP hosting.

- Pair the online web app with your own installation using a one-time code; access settings and Caller audio through the shared HTTPS address.

- Web app installation prompt with Android install dialog and iOS instructions; reminders can be dismissed.

- Enable browser audio at the top of the dashboard and adjust its volume separately, including on phones.

<!-- Add brief user-facing changes here. -->

#### Einstellungen und Import / Settings and Import

<!-- Add brief user-facing changes here. -->

#### Updates und Installation / Updates and Installation

<!-- Add brief user-facing changes here. -->

#### Lizenz und Support / Licensing and Support

- The support dashboard shows web app connections, active browsers and last usage for each installation.

<!-- Add brief user-facing changes here. -->
