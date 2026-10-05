# Migration Plan - Darts-Hub 2.0

> Reihenfolge gemäß Auftrag: Audit -> Autodarts -> Core Events -> Caller -> WLED ->
> PixelIt -> GIF -> ProcessManager -> Extension API -> Config Migration -> GUI/TUI Wiring ->
> Integration Tests -> Packaging. Legacy-Code ist Source of Truth; keine Mock-Funktionalität.

## Phase 1 - Audit (ABGESCHLOSSEN)
- [x] Legacy-Pfade verifiziert (Caller, WLED, PixelIt, GIF, Awtrix, Extern, alter Hub).
- [x] `docs/LEGACY_ANALYSIS.md` erstellt.
- [x] `docs/FEATURE_MATRIX.md` erstellt (Funktions- + Caller-Config-Matrix, 37 Args).
- [x] `docs/FUNCTIONALITY_AUDIT.md` um Legacy-Audit erweitert.
- [x] `docs/AUTODARTS.md` erstellt (Protokoll + Gap-Analyse).
- [ ] Awtrix/Extern Detailanalyse (offen).
- [ ] `.state`/`.events`-Payload-Felder aus `broadcast-examples.dat` extrahieren (offen).

## Phase 2 - Autodarts (NÄCHSTE)
1. `AutodartsOptions` mit `ApiBaseUrl` (Default `https://api.autodarts.com`),
   `WsBaseUrl` (Default `wss://api.autodarts.com`), `BoardId`, `CertCheck` einführen.
2. `AutodartsWebSocketClient` auf `{WsBaseUrl}/ms/v0/subscribe` umstellen.
3. channel/topic-Subscription implementieren (`autodarts.boards/<boardId>.events`,
   `autodarts.matches/<matchId>.state`) inkl. Unsubscribe bei Match-Wechsel.
4. State-Machine + Reconnect-Backoff verifizieren/ergänzen (Health-Status).
5. Parser-Tests aus Legacy-Payloadstrukturen.
- DoD: siehe `AUTODARTS.md` Abschnitt 6.

## Phase 3 - Core Events
- Interne Event-Contracts (AutodartsConnected/Disconnected, Match/Game/Leg/Turn Started/Finished,
  ThrowDetected, ScoreChanged, BustDetected, CheckoutAvailable, GameShot, PlayerChanged).
- EventBus: Thread-Safety, Cancellation, Fehlerisolation pro Handler, Logging, Tests.

## Phase 4 - Caller
- `CallerOptions` mit allen 37 Legacy-Settings (FEATURE_MATRIX.md B).
- Cross-Platform-Audio-Abstraktion (Windows/Linux/macOS), Voice/Ambient-Kanäle, Queue/Debounce.
- Soundpack-Format kompatibel halten; Voice-Pack-Download; Checkout/Bust/Special/Player/Game-Calls.
- Persistenz + GUI/TUI-Anbindung; Tests (Score-Handling, Special-Calls, Config).

## Phase 5-6 - WLED / PixelIt
- `WledOptions`/`PixelItOptions` aus Legacy-Args; echte HTTP-Kommunikation (Timeout,
  Cancellation, Health, Logging); Event->Action-Mapping konfigurierbar + persistent; Tests.

## Phase 7 - GIF
- Neues Modul `DartsHub.Modules.Gif` anlegen (fehlt komplett).
- Web-Wiedergabe (`--web_gif`/`--web_gif_port`), Medien-Management, Event-Mapping, Tests.

## Phase 8 - ProcessManager
- Vollständige Parität: Name, Executable, Arguments (sicheres ProcessStartInfo),
  WorkingDirectory, EnvVars, Enabled, AutoStart, StartDelay, StopWithDartsHub,
  RestartOnCrash, RestartDelay, OS-Filter; Status/PID/ExitCode; stdout/stderr; Tests.

## Phase 9 - Extension API
- Legacy-Protokoll dokumentieren (`docs/LEGACY_EXTENSION_PROTOCOL.md`).
- Extension-Server aus Caller nach `DartsHub.Api`/`ExtensionHost` verlagern.
- API v1 (REST + WebSocket), Auth (ClientID/Secret/Token), Permission-Enforcement, Tests.

## Phase 10 - Config Migration
- Read-only Importer für alte Hub-/Caller-/WLED-/PixelIt-/GIF-Configs.
- Strongly Typed Options, Validation (Port/URL/IP/Pfad/Volume/Delay), Persistenz, Tests.

## Phase 11 - GUI/TUI/CLI Wiring
- Bindings gegen echte Application-Services; keine ViewModel-Dummywerte.
- TUI mit Terminal.Gui v2; CLI-Kommandos (status/modules/caller/apps).

## Phase 12-13 - Integration Tests + Packaging
- E2E: Autodarts-Testevent -> Parser -> EventBus -> Caller/WLED.
- Prozess-Start/Stop/Restart; API Auth/Permission/WebSocket; Packaging.

## Nicht-migrierte Funktionen (bewusst dokumentiert)
> Noch keine. Sobald etwas technisch nicht portierbar ist, wird es hier mit
> Legacy-Verhalten/Problem/Grund/Alternative/Impact dokumentiert (Regel 105).

## Build-Gates
Nach jeder Phase: `dotnet restore` / `dotnet build` / `dotnet test`; Warnings prüfen.
