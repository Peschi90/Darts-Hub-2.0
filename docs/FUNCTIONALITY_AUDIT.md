# Darts-Hub Funktionalitäts-Audit

Stand: aktueller Repository-Zustand nach der Analyse.

## Kurzfazit
Die Lösung enthält bereits eine brauchbare Trennung aus Contracts, Core, API, GUI, TUI, CLI und Modulen. Die Runtime ist jedoch noch nicht vollständig als einheitlich verdrahtetes System umgesetzt: einige UI-Teile sind nur Shell/Platzhalter, die TUI ist derzeit kein Terminal.Gui-v2-Client, und mehrere Module sind im aktuellen Startpfad noch nicht aktiv an die Runtime angebunden.

## Audit-Tabelle

| Funktion | UI vorhanden | Backend vorhanden | Verdrahtet | Getestet | Status |
|---|---:|---:|---:|---:|---|
| Autodarts Connect | Nein | Teilweise | Teilweise | Nein | NOT IMPLEMENTED |
| Autodarts Reconnect | Nein | Teilweise | Nein | Nein | NOT IMPLEMENTED |
| Caller enable/disable | Ja | Teilweise | Nein | Nein | PARTIAL |
| Caller Audio | Ja | Ja | Nein | Nein | PARTIAL |
| Caller Soundpacks | Ja | Teilweise | Nein | Nein | PARTIAL |
| Caller Settings | Ja | Teilweise | Nein | Nein | PARTIAL |
| WLED enable/disable | Ja | Ja | Teilweise | Teilweise | PARTIAL |
| WLED connection | Ja | Ja | Teilweise | Teilweise | PARTIAL |
| WLED event handling | Teilweise | Ja | Teilweise | Teilweise | PARTIAL |
| PixelIt | Ja | Teilweise | Nein | Nein | PARTIAL |
| GIF | Teilweise | Teilweise | Nein | Nein | PARTIAL |
| External Apps | Teilweise | Ja | Nein | Nein | PARTIAL |
| Process Autostart | Teilweise | Ja | Nein | Nein | PARTIAL |
| Process Stop | Teilweise | Ja | Nein | Nein | PARTIAL |
| Process Restart | Teilweise | Ja | Nein | Nein | PARTIAL |
| User Extensions | Teilweise | Teilweise | Nein | Nein | PARTIAL |
| Extension API | Ja | Teilweise | Teilweise | Nein | PARTIAL |
| API Authentication | Ja | Ja | Teilweise | Ja | PARTIAL |
| WebSocket Events | Ja | Ja | Teilweise | Ja | PARTIAL |
| Logs | Ja | Teilweise | Nein | Nein | PARTIAL |
| Settings persistence | Ja | Teilweise | Teilweise | Nein | PARTIAL |
| GUI IPC | Nein | Nein | Nein | Nein | NOT IMPLEMENTED |
| TUI IPC | Nein | Nein | Nein | Nein | NOT IMPLEMENTED |
| CLI | Ja | Teilweise | Teilweise | Teilweise | PARTIAL |

## Beobachtungen

### Runtime / Host
- `DartsHub.Api` ist der aktuelle externe API-Host für GUI/TUI/CLI.
- `DartsHub.App` enthält die Core-Services für Runtime, Health, Module und Configuration, startet aber aktuell keine echten Module.
- Es gibt derzeit keinen vollständigen Runtime-Startpfad, der alle offiziellen Module automatisch registriert und startet.

### Module
- Die Modulprojekte existieren: Caller, WLED, PixelIt, Awtrix sowie Autodarts und ProcessManager.
- Die Modulklassen implementieren Lifecycle-Methoden und Health-Methoden.
- Es ist derzeit kein klarer zentraler Bootstrapping-Code sichtbar, der diese Module in der Runtime registriert.

### GUI
- Die GUI enthält Dashboard, Navigation, Statusbereiche und bindet reale API-Daten (`/status`, `/settings`) an.
- WLED-spezifische Live-Settings wurden erweitert (z. B. Sleep-/BoardStop-/ConnectionTest-Statusfelder und Effekt-Counts).
- Die GUI kann WLED-Basiskonfiguration jetzt editieren und per API persistieren (Host/Port/Timeout/Brightness/Sleep/Flags).
- Die Oberfläche ist weiterhin noch nicht auf vollständig modulgetrennte Detailseiten ausgebaut.

### TUI
- Die TUI läuft mit `Terminal.Gui v2` und wurde von statischen Platzhaltern auf Live-Status-/Settings-Befüllung umgestellt.
- Dashboard, Autodarts, Caller, WLED und Systemseiten lesen jetzt reale API-Daten.
- Für vollständige Parität fehlen noch tiefere modulbezogene Interaktionsflows.

### API / Events
- JWT-Authentifizierung ist vorhanden.
- Status- und Event-Stream-Endpoints sind vorhanden.
- Der WebSocket-Connect-Pfad wurde abgesichert, bleibt aber funktional abhängig von der Laufzeit des API-Hosts und der korrekten Zertifikats-/HTTPS-Konfiguration.

## Offene Kernpunkte
1. Echten Modul-Bootstrap für die Runtime einführen.
2. GUI in modulare Seiten mit echter Navigation umstellen.
3. TUI auf `Terminal.Gui v2` umbauen.
4. Persistente Einstellungen hinzufügen.
5. Echte Runtime-State-Synchronisation zwischen GUI/TUI/CLI sicherstellen.

## Legacy-basierter Funktions-Audit (Phase 1)

Klassifikation gegen den Legacy-Code (Source of Truth). Details siehe
`LEGACY_ANALYSIS.md` und `FEATURE_MATRIX.md`.

| Bereich | Legacy-Quelle | Neue Zielkomponente | Status |
|---|---|---|---|
| Autodarts WS-Endpoint | `wss://api.autodarts.com/ms/v0/subscribe` | `AutodartsWebSocketClient` nutzt `wss://api.autodarts.io/connect` | MISSING (Endpoint falsch) |
| Autodarts channel/topic-Subscription | `autodarts.boards/.events`, `autodarts.matches/.state` | nicht implementiert | MISSING |
| Autodarts Keycloak-Auth | `load_client_id()` + `/auth/v1/` | `AutodartsOAuth2Client` | PARTIAL (Verfahren zu verifizieren) |
| Caller CLI-Config (37 Args) | argparse in `darts-caller.py` | `CallerConfig`/`CallerOptions` | PARTIAL |
| Caller Audio-Engine | `pygame.mixer`, 2 Kanäle | `ScoreCaller` + Audio-Abstraktion (fehlt) | PARTIAL |
| Caller Voice-Pack-Download | `--downloads*` | - | MISSING |
| Caller Checkout/Bust/Special-Calls | `handle_message` | - | MISSING |
| WLED Effekt-Mapping | `darts-wled.py` + `*_effects.py` | `DartsHub.Modules.Wled` | PARTIAL (dynamische Effekt-ID-Aufloesung via /json/eff, Trigger-Aliase, Legacy-DMU-Normalisierung inkl. spezifischer Keys, BoardStopAfterWin/ConnectionTest/Sleep-Integration, Combo-Effects, Player-Idle-Effects, PlayerJoined/PlayerLeft sowie Takeout/Calibration-Trigger umgesetzt; offene Restluecken: volle Turn-Idle-Paritaet und eventuelle Feindetails aus Legacy-Boardstatus) |
| WLED HTTP-Kommunikation | `requests` an WLED | `WledDeviceManager` (/json/info, /json/eff, /json/state) | DONE |
| PixelIt Kommunikation/Templates | `darts-pixelit.py` | `DartsHub.Modules.PixelIt` | PARTIAL |
| GIF Web-Wiedergabe | `darts-gif.py` (`--web_gif`) | Modul fehlt vollständig | MISSING |
| Extension-Server (SocketIO/Raw) | Caller Flask-SocketIO + `/api/ext/ws` | `DartsHub.Api`/`ExtensionHost` | PARTIAL |
| Update-/Release-System | `Updater.cs` (alter Hub) | - | MISSING |
| Setup-Wizard | `SetupWizardManager.cs` | - | MISSING |
| Config-Persistenz | Legacy JSON/Profile | - | MISSING |

### Priorisierte Reihenfolge (gemäß Auftrag)
1. Autodarts-Endpoint + Subscription-Modell an Legacy angleichen (höchste Priorität).
2. Autodarts State-Machine + Reconnect-Backoff verifizieren.
3. Parser-Tests aus Legacy-Payloadstrukturen.
4. Caller-Config-Parität + Audio-Abstraktion.
5. WLED/PixelIt echte Gerätekommunikation.
6. GIF-Modul neu anlegen (Web-Wiedergabe).
7. ProcessManager-Parität, Extension-Host, Config-Migration.
8. GUI/TUI/CLI-Verdrahtung + Integrationstests.

## Fortschritt / erledigte Schritte
- [x] 1-3: Autodarts Endpoint/Subscriptions/Envelope-Routing/Reconnect + Parser-Tests (Phase 2).
- [x] 4: Caller-Config-Parität (verifizierte Legacy-Defaults + Validierung) und Cross-Platform-
  Audio-Abstraktion (`AudioBackendFactory`, `NullAudioDevice`/`NullTtsEngine`).

## Bewusst dokumentierte Lücken (Regel 105)
- **Nativer Linux/macOS-Audio-Backend fehlt.**
  - Legacy-Verhalten: Der Python-Caller nutzt pygame.mixer (plattformübergreifend) für Playback.
  - Problem: Die aktuelle .NET-Implementierung nutzt NAudio/System.Speech (Windows-only).
  - Aktuelles Verhalten: Auf Nicht-Windows bzw. Headless ohne Audio-Session wird auf
    `NullAudioDevice`/`NullTtsEngine` zurückgegriffen (Warnung, kein Crash).
  - Mögliche Alternative: Native ALSA/PulseAudio- bzw. CoreAudio-Implementierung oder ein
    plattformübergreifendes Playback-NuGet.
  - Impact: Auf Linux/macOS gibt es aktuell keine hörbaren Calls; Runtime bleibt funktionsfähig.
