# Changelog – Darts-Hub 2.0

## v0.1.0-beta.29

<!-- Geplante nächste Version. Bei Bedarf vor dem Release anpassen. / Planned next version; adjust before release if needed. -->

### Deutsch

#### Allgemein / General

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Autodarts

- Cricket, Tactics und Hidden Cricket liefern jetzt gewertete Treffer und Feldzustände für alle Scoring-Modi.

- Rundennummern werden auch bei manueller Eingabe korrekt erkannt. Aufnahmen entfernen Avatar-Kennungen und erhalten die Feldnamen der Checkout-Vorschläge.

- Mit passender Lizenz lassen sich Spielsitzungen mit Markierungen aufnehmen und anonymisiert exportieren, auch im Terminal. Die Aufnahme-Anleitung liegt in der internen Dokumentation.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Caller

- Cricket-Ansagen und Effekte berücksichtigen Marks, Feldabschlüsse, Punkte und Undo. Alle Soundkeys und Auslöser sind dokumentiert; Bull-Dateien werden auch im Segmentmodus erkannt.

- Nachträglich korrigierte Einzeldarts werden erneut angesagt, ohne unveränderte Würfe zu wiederholen.

- Ambient-Sounds erkennen wieder Dartkombinationen, Punktebereiche, Gruppierungen und die Spiel- und Lobbyereignisse des alten Callers.

- Bei ausgeschalteten Einzeldartansagen unterbrechen neue Würfe laufende Ansagen nicht mehr; Blind-Support und Spielerwechsel behalten ihre bisherige Priorität.

- Ansagen in der gekoppelten Webapp werden schneller übertragen; Unterbrechungen werden sofort weitergeleitet.

- Matchbeginn und erster Spieler werden auch ohne Bull-off direkt angesagt, ohne auf den ersten Dart zu warten.

- Caller-Sounddateien können direkt im Browser abgespielt werden, auch ohne lokale Audioausgabe. Ansagefolgen und Unterbrechungen bleiben erhalten.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### WLED

- Cricket/Tactics-Effekte während eines Turns benötigen die bestehende Lizenzfreigabe.

- Neue Cricket/Tactics-Auslöser für gewertete Treffer, Feldabschlüsse, Punkte und entdeckte Hidden-Cricket-Felder, auch im Terminal.

- Kombinationseffekte berücksichtigen nachträglich korrigierte Würfe.

- Siegeseffekte werden bei Matchabschluss und beim Legwechsel wieder zuverlässig ausgelöst.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### PixelIt

- Fehlende Templates nach dem Import blockieren das Speichern nicht mehr; Pfade und Regeln lassen sich direkt korrigieren.

- Neue Cricket/Tactics-Auslöser für gewertete Treffer, Feldabschlüsse, Punkte und entdeckte Hidden-Cricket-Felder, auch im Terminal.

- Kombinationseffekte berücksichtigen nachträglich korrigierte Würfe.

- Spielerwechsel reagiert nur auf einen anderen Spieler. „Wurf oder Turnwechsel“ erkennt auch neue Aufnahmen desselben Spielers; Takeout ist als eigener Auslöser verfügbar. Bestehende kombinierte Regeln werden übernommen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### AwtrixNG

- Neue Cricket/Tactics-Auslöser für gewertete Treffer, Feldabschlüsse, Punkte und entdeckte Hidden-Cricket-Felder, auch im Terminal.

- Kombinationseffekte berücksichtigen nachträglich korrigierte Würfe.

- Spielerwechsel reagiert nur auf einen anderen Spieler. „Wurf oder Turnwechsel“ erkennt auch neue Aufnahmen desselben Spielers; Takeout ist als eigener Auslöser verfügbar. Bestehende kombinierte Regeln werden übernommen.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GIF

- Neue Cricket/Tactics-Auslöser für gewertete Treffer, Feldabschlüsse, Punkte und entdeckte Hidden-Cricket-Felder, auch im Terminal.

- Kombinationseffekte berücksichtigen nachträglich korrigierte Würfe.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Eigene Anwendungen / External Apps

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Einstellungen und Import / Settings and Import

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Updates und Installation / Updates and Installation

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Lizenz und Support / Licensing and Support

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

### English

#### Allgemein / General

<!-- Add brief user-facing changes here. -->

#### Autodarts

- Cricket, Tactics and Hidden Cricket now provide counting hits and field states for every scoring mode.

- Turn numbers are recognized correctly for manual scoring. Recordings remove avatar identifiers and preserve checkout suggestion field names.

- Eligible licenses can record game sessions with markers and export anonymized data, including from the terminal. The recording guide is kept in the internal documentation.

<!-- Add brief user-facing changes here. -->

#### Caller

- Cricket calls and effects use marks, field closures, scoring and undo. All sound keys and triggers are documented; Bull clips also work in segment mode.

- Corrected individual darts are announced again without repeating unchanged throws.

- Ambient sounds support dart combinations, score ranges, grouping, and the old Caller’s game and lobby events again.

- New darts no longer interrupt announcements when single-dart calls are disabled; blind support and player changes retain their existing priority.

- Announcements reach the paired web app faster; interruptions are forwarded immediately.

- Match start and the first player are announced immediately without bull-off, without waiting for the first dart.

- Caller sound files can play directly in the browser, including without local audio output. Announcement sequences and interruptions are preserved.

<!-- Add brief user-facing changes here. -->

#### WLED

- Cricket/Tactics effects during a turn require the existing license entitlement.

- New Cricket/Tactics triggers for counting hits, closed fields, points and revealed Hidden-Cricket fields, also in the terminal.

- Combination effects respond to corrected throws.

- Win effects trigger reliably again at match completion and when the leg changes.

<!-- Add brief user-facing changes here. -->

#### PixelIt

- Missing templates after import no longer block saving; paths and rules can be corrected directly.

- New Cricket/Tactics triggers for counting hits, closed fields, points and revealed Hidden-Cricket fields, also in the terminal.

- Combination effects respond to corrected throws.

- Player change only fires for a different player. “Throw or turn change” also detects new visits by the same player; Takeout is available as a separate trigger. Existing combined rules are migrated.

<!-- Add brief user-facing changes here. -->

#### AwtrixNG

- New Cricket/Tactics triggers for counting hits, closed fields, points and revealed Hidden-Cricket fields, also in the terminal.

- Combination effects respond to corrected throws.

- Player change only fires for a different player. “Throw or turn change” also detects new visits by the same player; Takeout is available as a separate trigger. Existing combined rules are migrated.

<!-- Add brief user-facing changes here. -->

#### GIF

- New Cricket/Tactics triggers for counting hits, closed fields, points and revealed Hidden-Cricket fields, also in the terminal.

- Combination effects respond to corrected throws.

<!-- Add brief user-facing changes here. -->

#### Eigene Anwendungen / External Apps

<!-- Add brief user-facing changes here. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

<!-- Add brief user-facing changes here. -->

#### Einstellungen und Import / Settings and Import

<!-- Add brief user-facing changes here. -->

#### Updates und Installation / Updates and Installation

<!-- Add brief user-facing changes here. -->

#### Lizenz und Support / Licensing and Support

<!-- Add brief user-facing changes here. -->
