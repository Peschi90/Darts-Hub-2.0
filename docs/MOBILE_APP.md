# Native Android-App / Native Android app

## Deutsch

Das eigenständige Projekt `darts-hub2.0-app` ist eine **Entwicklungsversion**. Es ist
noch nicht im Store verfügbar und ersetzt die Desktop-GUI noch nicht vollständig.
Die bestehende Webapp bleibt unabhängig davon nutzbar.

Die erste Android-Version verbindet sich direkt mit dem lokalen Darts-Hub oder
mit einem Kopplungscode über die Online-Webapp. Sie zeigt echte Statusdaten und
Modulschalter, bietet schema-basierte Einstellungsformulare, Soundpack-Downloads,
Autodarts-Anmeldung, Konsole und Systeminformationen. Einstellungen werden erst
beim Speichern übernommen; unbekannte Serverfelder bleiben erhalten.

Die Caller-Wiedergabe wird im Dashboard ausdrücklich aktiviert und über die
Medienbenachrichtigung wieder beendet. Die vorhandenen Play/Stop-Befehle und
Audiokanäle des Darts-Hub bleiben maßgeblich. Hörqualität und Hintergrundverhalten
müssen zusätzlich auf echten Android-Geräten überprüft werden.

Eine spätere iOS-Version kann den gemeinsamen Kotlin-Multiplatform-Kern nutzen.
Eine iOS-Oberfläche, Keychain-Anbindung und iOS-Prüfungen sind noch nicht enthalten.
Diese Schritte benötigen macOS und Xcode. HubX-Dialoge, reichhaltige Gerätevorschauen,
Supportversand, Backups und die vollständige Einführung fehlen in der App noch.

Die Build- und Startanleitung liegt in der README des App-Projekts. Bei Änderungen
an Darts-Hub müssen App-Verträge und Tests mitgeprüft werden; der Release-Test
fordert diese Prüfung bei geänderten Schnittstellen ausdrücklich ein.

## English

The independent `darts-hub2.0-app` project is a **development version**, not yet
available in stores and not complete desktop-GUI parity. The existing web app
continues to work independently.

The initial native Android app supports LAN access or pairing through the online
relay, real dashboard data/module switches, schema-driven configuration editing,
soundpack downloads, Autodarts sign-in, console and system information. Writes
require explicit saving and preserve unknown server properties.

Caller playback is opt-in and is stopped from the media notification; server
play/stop IDs and audio lanes remain authoritative. Physical-device audio and
background behavior need additional verification. A shared Kotlin Multiplatform
core prepares a future iOS version, but no iOS shell, Keychain integration or native
iOS verification is included. Those steps require macOS/Xcode. HubX dialogs, rich
device previews, support uploads, backups and full onboarding are not implemented
in the native app yet. See its README for builds, coverage and limitations.

Backend interface changes require a mobile compatibility review and tests. The
backend release check detects changes to the reviewed contracts.
