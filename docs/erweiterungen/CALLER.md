# Caller – Funktionsübersicht

## Ansagen

- Sprachansagen für Scores, Bust und Spiel-/Leg-/Match-Gewinne sowie besondere Score-Reaktionen, sofern im Soundpack vorhanden.
- Einzel-Darts als Punktzahl, Segmentname oder Segment-Effekt; zusätzlich den Gesamtscore der Aufnahme ansagen.
- Gesamtscore wartet auf die Dart-3-Ansage. Neue passende Ansagen können laufende Calls einschließlich Gesamtscore unterbrechen.
- Spielernamen bzw. Spielernummern bei Leg-/Set-Anfang und -Ende, Checkout und optional jedem Spielerwechsel.
- Bot-Aktionen ein-/ausschließen; Checkout-Hinweise in ihrer Wiederholung begrenzen und auf den Spieler des eigenen Boards einschränken.
- Realistische X01-Bühnenansagen mit Set-/Leg-Nummer und Startspieler; Ersatzansagen bei fehlenden Spezialdateien.
- Blind-Unterstützung mit Ziel- und Trefferpositionen einschließlich innerem Single und Bull und Zielansagen für unterstützte Spielvarianten.
- Atmosphäre vor/nach Hauptansagen und mit eigener Lautstärke; zusammengehörige Dateien als Ansagefolge wiedergeben.

## Stimmen, Medien und Audio

- Feste installierte Stimme oder Zufallsstimme bei Matchstart/neuem Leg; Sprache/Geschlecht eingrenzen.
- Soundpack-Bibliothek durchsuchen, Hörproben abspielen, Stimmen herunterladen und verwenden; Downloadfortschritt und Fehler anzeigen.
- Downloads nach Anzahl, Sprache oder explizitem Profilnamen auswählen; ältere von DartsHub installierte Versionen nach Erfolg bereinigen.
- Eigene Soundpacks verwenden; Medienordner und gemeinsamen überschreibenden Medienordner konfigurieren.
- Bei Medienordnerwechsel Packs auf Wunsch mit Fortschritt verschieben; ohne Umzug gelten alte Packs nicht als im neuen Ordner installiert.
- Lautstärke und lokale Wiedergabe einstellen; optionale TTS-Ersatzansagen für fehlende Sounds/Namen. Ohne TTS werden fehlende Dateien stumm übersprungen.
- Oberfläche, Soundpack-Sprache und TTS-Sprache sind getrennt; TTS benötigt eine verfügbare Host-Stimme.
- Absenken anderer Audio-Sitzungen ist eine Windows-Systemintegration, keine Zusage für andere Betriebssysteme.
- Erweiterte Caller-Diagnose in Konsole/Logs einschalten.

## Vollständiger Einstellungskatalog

Alle Optionen des aktuellen Katalogs sind unten aufgeführt. **Altoption** bedeutet: keine aktive native Funktion; ihre Erklärung beschreibt den ursprünglichen Zweck. Insbesondere Python-Webcaller-, Mixer- und Login-Optionen sind kein Ersatz für die native Anmeldung/Audioausgabe.

| Einstellung | Funktion | Status |
| --- | --- | --- |
| Lautstärke | Lautstärke relativ zur Systemlautstärke: 0 = stumm, 1 = maximal. Der Webcaller hat eine eigene Lautstärke. | Aktiv |
| Lokale Wiedergabe | Spielt die Ansagen auf den Lautsprechern dieses Computers ab. | Aktiv |
| Text-to-Speech aktivieren | Standardmäßig ausgeschaltet. Wenn aktiv, spricht die Systemstimme fehlende Soundpack-Ansagen und Spielernamen. Wenn ausgeschaltet, werden fehlende Sounds still übersprungen; Soundpacks und Hörproben bleiben nutzbar. | Aktiv |
| TTS-Ersatzstimme | Wenn ein Sound fehlt, wird die Windows-Sprachausgabe verwendet. Eine passende Stimme muss in Windows installiert sein. | Aktiv |
| Score-Ansagen | Aktiviert Score-Ansagen aus Soundpacks oder per Sprachausgabe. | Aktiv |
| Specials | Spielt besondere Reaktionen zu hohen Scores, wenn das Soundpack sie enthält. | Aktiv |
| Feste Stimme | Name eines installierten Soundpacks. Über „Verwenden“ in der Bibliothek wählen. Leerer Name erlaubt eine Zufallsauswahl. | Aktiv |
| Stimmenwechsel | 0 = feste Stimme, 1 = zufällige Stimme bei Matchstart, 2 = bei jedem neuen Leg. Es werden die neuesten installierten Versionen verwendet. | Aktiv |
| Sprache der Stimmen | Begrenzt zufällige Stimmen auf eine Sprache. 0 erlaubt alle Sprachen; 1 Englisch, 2 Französisch, 3 Russisch, 4 Deutsch, 5 Spanisch, 6 Niederländisch, 7 Italienisch. | Aktiv |
| Stimmtyp | 0 = alle Stimmen, 1 = weiblich, 2 = männlich. | Aktiv |
| Spielernamen ansagen | 0 = keine Namen, 1 = am Leg-/Set-Anfang und -Ende sowie beim Checkout, 2 = zusätzlich bei jedem Spielerwechsel. Fehlt eine Namensdatei, wird player1, player2 usw. entsprechend der aktuellen Spielerreihenfolge verwendet. Fehlt auch diese Datei, kann aktiviertes TTS die Spielernummer sprechen. | Aktiv |
| Bot-Ansagen | Aktiviert Ansagen für Aktionen von Bots. | Aktiv |
| Einzelne Darts | 0 = aus, 1 = Score jedes Darts (60), 2 = Segmentname (Triple 20), 3 = Segment-Effekt. Fehlende Sounds verwenden die im Caller beschriebenen Ersatzschlüssel. | Aktiv |
| Zusätzlich Aufnahme ansagen | Sagt auch den Gesamtscore einer Aufnahme an, wenn Einzel-Dart-Ansagen aktiv sind. | Aktiv |
| Checkout-Wiederholungen | Anzahl der Checkout-Ansagen bei derselben Restpunktzahl. 0 deaktiviert sie. Gilt für checkbare Scores bis 170; der Zähler wird bei geänderter Restpunktzahl zurückgesetzt. | Aktiv |
| Nur auf meinem Board | Beschränkt Checkout-Ansagen auf den Spieler, der mit deinem Board verknüpft ist. Ohne Board-Zuordnung gibt es dann keine Checkout-Ansage. | Aktiv |
| Atmosphäre | 0 deaktiviert Atmosphäre. Die Lautstärke multipliziert die Caller-Lautstärke; 0,5 ist die Hälfte davon. | Aktiv |
| Atmosphäre nach Ansagen | Spielt die Atmosphäre erst nach den Hauptansagen. Sonst wird sie vor ihnen gespielt. | Aktiv |
| Andere Anwendungen absenken | Senkt unter Windows die Lautstärke anderer Audio-Sitzungen während einer Ansage. 0 = aus, 1 = unverändert. Nur bei lokaler Wiedergabe. | Aktiv |
| Soundpack-Ordner | Absoluter Speicherort für Soundpacks und Downloads. Leer verwendet den dauerhaften DartsHub-Datenordner. | Aktiv |
| Gemeinsame Sounds | Absoluter Ordner mit Sounds, die für alle Stimmen gelten und die Dateien des Soundpacks überschreiben. | Aktiv |
| Anzahl der Downloads | 0 deaktiviert die Auswahl. Ansonsten werden die letzten N passenden Profile aus dem Katalog gewählt und bereits installierte übersprungen. | Aktiv |
| Download-Sprache | Beschränkt die Download-Auswahl auf eine Sprache. Ein ausdrücklich benanntes Soundpack hat Vorrang. | Aktiv |
| Bestimmtes Soundpack | Optionaler Profilname (auch mit Versionssuffix), ohne Beachtung der Groß-/Kleinschreibung. Hat Vorrang vor Sprache und Anzahl. | Aktiv |
| Alte Versionen entfernen | Entfernt nach erfolgreichem Download ältere, von DartsHub installierte Versionen derselben Stimme. Eigene Soundpacks und die ausgewählte Stimme bleiben erhalten. | Aktiv |
| Realistische Bühnenansagen | Realistischere Bühnenansagen für X01: Set-/Leg-Nummer, startender Spieler und „first to throw“. Das Soundpack muss die passenden sN_lN_n- und gameshot_lN_n-Schlüssel enthalten; sonst wird auf normale Ansagen zurückgegriffen. | Aktiv |
| Assistenz für blinde Spieler | Sagt das Ziel am Aufnahme-Anfang und die Trefferposition jedes Darts an, einschließlich Single innen und Bull. Unterstützt Zielansagen für ATC, RTW, Bermuda und Shanghai; bei X01 Checkout nach jedem Dart. Verhindert doppelte Einzel-Dart-Ansagen und sagt die fertige Aufnahme an. | Aktiv |
| Webcaller ohne HTTPS | Deaktiviert HTTPS für den Python-Webcaller. DartsHub verwendet seinen eigenen API-Server. | Altoption |
| Webcaller-Port | Port des Python-Webcallers; ist nicht der DartsHub-API-Port. | Altoption |
| Zertifikate prüfen | TLS-Prüfung des Python-Callers. Die native Verbindung prüft Zertifikate immer. | Altoption |
| Mixer-Frequenz | Pygame-Abtastrate in Hertz. Der native Audiotreiber verwendet das Format der Audiodatei. | Altoption |
| Mixer-Samplegröße | Pygame-Samplegröße. Wird vom nativen Audiotreiber nicht verwendet. | Altoption |
| Mixer-Kanäle | Anzahl der Pygame-Kanäle; native Wiedergabe verwendet das Dateiformat. | Altoption |
| Mixer-Puffer | Pygame-Puffergröße. Der native Audiotreiber hat einen eigenen Puffer. | Altoption |
| Zusätzliche Diagnose | Zusätzliche Python-Diagnose. DartsHub hat eine eigene Ereignisanzeige. | Altoption |
| Alle Nachrichten protokollieren | Python-Nachrichtenprotokollierung. DartsHub zeigt maskierte Nachrichten im Autodarts-Ereignisfenster. | Altoption |
| Benutzerlizenzen akzeptieren | Akzeptiert Python-Erweiterungslizenzen. Nicht Teil der nativen DartsHub-Lizenzverwaltung. | Altoption |
| Caller-Diagnose | Erweiterte Laufzeitdiagnose in der Konsole und Logdatei: Match-Zustände, Spieler, Aufnahme, Soundauswahl und übersprungene Ansagen. Entspricht dem Caller-Debugschalter in der Konsole. | Aktiv |
| Extension-Transport | Transport des Python-Extension-Servers: Socket.IO, Raw-WebSocket oder beide. Nicht für den nativen DartsHub-Server. | Altoption |
| E-Mail (veraltet) | Dieses Argument wird vom aktuellen Caller ignoriert. Verwende die interaktive Autodarts-Anmeldung. | Altoption |
| Passwort (veraltet) | Dieses Argument wird vom aktuellen Caller ignoriert. Verwende die interaktive Autodarts-Anmeldung. | Altoption |
| Board-ID | Wird in den Autodarts-Einstellungen gespeichert und dort abonniert. | Altoption |

Weiterlesen: [Soundpack-Schlüssel](../CALLER_SOUNDPACKS.de.md), [Medienordner](../CALLER_MEDIA_PATH.md).

## Bedienung und Diagnose

GUI: Erweiterungsseite öffnen, Entwurf testen und speichern. TUI: `DartsHub --tui`, entsprechende Seite, **Enter** zum Bearbeiten und **Entwurf speichern**. Headless nutzt dieselbe Konfiguration. Vorschautests speichern nichts. Reale Statuswerte und Fehler stehen im Dashboard, auf der Modulseite und in der Konsole.

[Gemeinsame Funktionen](GEMEINSAM.md) · [Zur Übersicht](README.md)

## Ausgabe im Browser

Die Weboberfläche bietet oben im Dashboard eine pro Tab aktivierbare Caller-Wiedergabe mit eigener Lautstärke. Sie funktioniert auch bei ausgeschalteter lokaler Ausgabe. Details und die Bedienung über GUI/TUI stehen in [Weboberfläche](../WEB_INTERFACE.md#caller-audio-im-browser--caller-browser-audio).
