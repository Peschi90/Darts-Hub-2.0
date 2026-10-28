# Autodarts-Anbindung – Funktionsübersicht

## Anmeldung und Board

- Interaktiven Gerätecode-Anmeldeablauf starten; Link/Code nutzen und Freigabe abwarten.
- Anmeldung abbrechen, Status prüfen und abmelden; Host verwaltet Tokens. Kein Autodarts-Passwort im Caller nötig.
- Board-ID festlegen und speichern; zentrale Ereignisquelle für alle Erweiterungen.
- Live-Verbindungs-/Anmeldestatus und Fehler anzeigen; nach Unterbrechung Verbindung und Abonnements wiederherstellen.

## Spielzustand und Steuerung

- Boardereignisse und aktuelles Match verfolgen; alte Match-Abonnements entfernen und neue abonnieren.
- Variante, Spieler, aktiven Spieler, Restpunkte, Aufnahmen, Darts, Bust und Gewinnerzustände auswerten.
- Match-/Spielstart, Wurf-/Spielerwechsel, Takeout, Kalibrierung, Board-Stopp und Verbindungsereignisse an Modullogik liefern.
- Gewinn und tatsächliches Verlassen unterscheiden, einschließlich Abbruch. Netzwerkunterbrechung allein bedeutet nicht „Match beendet und verlassen“.
- Live-Spielinformationen im Dashboard und Ereignisse zur Diagnose anzeigen; keine getrennte Anmeldung je Erweiterung.
- X01, Cricket, CountUp und weitere vom Parser erkannte Varianten verarbeiten; nicht jede Variante hat identische Checkout-/Caller-Spezialansagen.
- Gemeinsame Board-Manager-Anbindung für Erkennung starten/stoppen und Reset; WLED verwendet sie für konfigurierte Pausen.
- Lokale Adresse aus Autodarts oder ausdrücklicher WLED-Konfiguration; Cloud-Tokens werden nicht an den lokalen Board-Manager geschickt.

## Bedienung

GUI: **Autodarts**, Board-ID, Anmeldung und speichern. TUI: dieselbe Seite, Board bearbeiten und angebotenen Geräte-Anmeldevorgang nutzen. Legacy-E-Mail/Passwort-Import ersetzt diese Anmeldung nicht.

Weiterlesen: [Benutzeranleitung](../../README.md), [Ereignisse](EREIGNISSE.md), [gemeinsame Funktionen](GEMEINSAM.md).

## Statistikdaten beim Matchstart / Statistics at match start

Bei Matches ohne Sets können die Set-Statistiken leer sein. Darts-Hub lädt den
Spielstatus trotzdem; fehlende Averages bleiben leer, ein gemeldeter Average von
0 wird als 0 angezeigt. Das gilt für GUI, TUI und Weboberfläche. Es ist keine
zusätzliche Einstellung nötig.

Matches without sets may provide no set statistics. Darts-Hub still loads the
match state; unavailable averages stay empty, while a reported average of 0 stays
0. This applies to the GUI, TUI and web interface without additional settings.
