# Changelog – Darts-Hub 2.0

## v0.1.0-beta.45

<!-- Geplante nächste Version. Bei Bedarf vor dem Release anpassen. / Planned next version; adjust before release if needed. -->

### Deutsch

#### Allgemein / General

- Ausführlichere Konsolendetails für Geräteaktionen, Caller, GIFs, eigene Anwendungen und User-Erweiterungen erleichtern die Fehlersuche; Zugangsdaten bleiben geschützt.

- DMU-Regeln in WLED, PixelIt, AWTRIX und GIF unterstützen M1–M20 sowie M und MISS. Auswahlfelder verhindern ungültige Dartfelder 21–24.

- Lizenzgeschützte WLED-Funktionen bieten einen gestalteten Dialog zur kostenlosen Lizenz; Hinweise stehen einmal direkt bei den betroffenen Funktionen statt über allen Einstellungstabs.

- Nutzeranleitungen und deutsche/englische Bildschirmfotos aktualisiert, einschließlich HubX, GIF-Vorlage, Systeminformationen, Updates und Raspberry Pi. Technische Berichte und UI-Referenzen sind von den Nutzeranleitungen getrennt.
- Spielerzuordnungen für Effekte, Anzeigen und nummerierte Caller-Ansagen bleiben ab dem Ausbullen beziehungsweise Matchstart über alle Legs und Sets gleich.

#### Autodarts

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Caller

- Mit `-crl` werden in Matches ohne Sets keine Set-Ansagen mehr abgespielt; reine Leg-Ansagen nutzen bei Bedarf „Game on“ als Ersatz.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### WLED

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### PixelIt

- HubX-GIFs bis 32 × 8 Pixel als animierte Vorlagen übernehmen: Originalgröße, feste Wiederholung oder Wiedergabe bis zum nächsten Effekt bzw. Turn; einstellbar in GUI, Terminal und Weboberfläche.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### AwtrixNG

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GIF

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Eigene Anwendungen / External Apps

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Frühe Backend-Abbrüche erhalten eine Fehlerdatei; GUI und Terminal zeigen Ursache und Dateipfad. Netzwerkfreigaben beim GUI-Start bleiben erhalten.

- GUI und TUI können mit `bip=IPADRESSE` ein Netzwerkbackend auf Port 5069 nutzen, ohne ein eigenes Backend zu starten. Kein API-Token und keine Bestätigung nötig. Der normale lokale Start bleibt erhalten.

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Einstellungen und Import / Settings and Import

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Updates und Installation / Updates and Installation

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

#### Lizenz und Support / Licensing and Support

<!-- Kurze Änderungen für Nutzer hier eintragen. -->

### English

#### Allgemein / General

- Richer console details for device commands, Caller, GIFs, external applications and user extensions make troubleshooting easier while protecting credentials.

- DMU rules in WLED, PixelIt, AWTRIX and GIF support M1–M20, M and MISS. Selection lists prevent invalid dart fields 21–24.

- License-protected WLED functions offer a designed dialog for a free license; notices appear once alongside the affected functions rather than above all settings tabs.

- Player assignments for effects, displays and numbered Caller announcements stay fixed from bull-off or match start across all legs and sets.
- Updated user guides and German/English screenshots, including HubX, the GIF template, System information, updates and Raspberry Pi. Technical reports and UI references are separated from user guides.

#### Autodarts

<!-- Add brief user-facing changes here. -->

#### Caller

- With `-crl`, matches without sets no longer play set announcements; leg-only calls fall back to “Game on” when needed.

<!-- Add brief user-facing changes here. -->

#### WLED

<!-- Add brief user-facing changes here. -->

#### PixelIt

- Import HubX GIFs up to 32 × 8 pixels as animated templates: original dimensions, fixed repetitions or playback until the next effect or turn, configurable in GUI, terminal and web UI.

<!-- Add brief user-facing changes here. -->

#### AwtrixNG

<!-- Add brief user-facing changes here. -->

#### GIF

<!-- Add brief user-facing changes here. -->

#### Eigene Anwendungen / External Apps

<!-- Add brief user-facing changes here. -->

#### GUI, TUI und Weboberfläche / GUI, TUI and Web Interface

- Early backend failures produce a failure log; GUI and terminal show the cause and file path. GUI startup preserves network listener settings.

- GUI and TUI can use a network backend on port 5069 with `bip=IPADDRESS`, without starting their own backend. No API token or confirmation is needed. Normal local startup remains available.

<!-- Add brief user-facing changes here. -->

#### Einstellungen und Import / Settings and Import

<!-- Add brief user-facing changes here. -->

#### Updates und Installation / Updates and Installation

<!-- Add brief user-facing changes here. -->

#### Lizenz und Support / Licensing and Support

<!-- Add brief user-facing changes here. -->
