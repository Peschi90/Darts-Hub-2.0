# Grenzen und Fehlersuche / Limitations and troubleshooting

| Problem | Prüfen |
| --- | --- |
| Keine Spielereignisse | Autodarts-Board-ID, Anmeldung und Verbindung. Der Caller ist für die Displaymodule nicht erforderlich. |
| Autodarts HTTP 401 | Anmeldung abgelehnt. Darts-Hub versucht eine Erneuerung; gegebenenfalls erneut anmelden. Unabhängig von der Darts-Hub-Lizenz. |
| Keine Ansagen | Caller aktiviert, Soundpack im aktuellen Medienpfad installiert/ausgewählt, lokale oder Browser-Ausgabe freigegeben? Linux-TTS ist kein allgemeiner Ersatz. |
| Handy-Audio stoppt im Hintergrund | Browser/OS können Wiedergabe und Netzwerk pausieren. Auch eine Webapp garantiert keine Wiedergabe bei gesperrtem Bildschirm. |
| AWTRIX-Icon fehlt | Datei auf allen Zielcontrollern, exakter Name, Gerätezugang und Format prüfen. Für Vollbild die textfreie `gif`-Vorlage und eine 32×8-Datei verwenden. |
| Vorschau weicht ab | Lokale Simulation; Schrift, Effekte und Scrollen können je Firmware abweichen. Gerätetest ist maßgeblich. |
| HubX blockiert | Lizenzfeature, Zustimmung zu Rechtstexten, Zielcontroller, Dateiname und belegte Preset-IDs prüfen. |
| Einstellungen fehlen | Unter **System** den tatsächlichen Datenordner prüfen. Ältere Speicherorte bleiben gegebenenfalls in Verwendung. |
| Update/Start scheitert | Passendes OS/x64-/ARM64-Paket, Berechtigungen und Logs prüfen. GUI benötigt Betriebssystem-Bibliotheken. |

[Konsole](RUNTIME_CONSOLE.md) · [System](SYSTEM.md) · [Support](SUPPORT.md) · [HubX](HUBX.md)

## English

Check board/sign-in for missing events and Caller activation, current media path, installed voice and playback permission for missing audio. Autodarts 401 is a sign-in rejection, not a Darts-Hub license failure. Browser/OS policies can suspend locked-screen audio even in an installed webapp. AWTRIX needs the icon on every target controller; `gif` is the text-free fullscreen template. Matrix previews are simulations. For HubX check license, legal consent and name/preset-ID conflicts. For apparently lost settings inspect **System** paths. Use console logs and the support workflow for persistent errors.
