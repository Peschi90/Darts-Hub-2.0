# Legacy Analysis - Darts-Hub 2.0 Migration

> Quelle der Wahrheit ist ausschliesslich der tatsaechliche Legacy-Code (statische Analyse).
> Nicht verifizierte Punkte sind mit `UNKNOWN` gekennzeichnet.

## Analysierte Legacy-Projekte

| Projekt | Pfad | Sprache | Haupt-Datei |
|--------|------|---------|-------------|
| Alter Darts-Hub | repos\lbormann\darts-hub | C#/Avalonia | darts-hub/ |
| Darts-Caller | Documents\Github\darts-caller-source | Python | darts-caller.py (~317 KB) |
| Darts-WLED | Documents\Github\darts-wled-source | Python | darts-wled.py (~118 KB) |
| Darts-PixelIt | Documents\Github\darts-pixelit-source | Python | darts-pixelit.py (~29 KB) |
| Darts-GIF | Documents\Github\darts-gif-source | Python | darts-gif.py (~29 KB) |
| Darts-Awtrix | Documents\Github\darts-awtrix-source | Python | UNKNOWN |
| Darts-Extern | Documents\Github\darts-extern-source | Python | UNKNOWN |

## 1. Autodarts-Anbindung (aus Darts-Caller, Source of Truth)

```
AUTODARTS_API_BASE  = getenv AUTODARTS_API_URL default https://api.autodarts.com
AUTODARTS_WS_BASE   = getenv AUTODARTS_WS_URL  default wss://api.autodarts.com
AUTODARTS_AUTH_URL  = {API_BASE}/auth/v1/
AUTODARTS_MATCHES_URL = {API_BASE}/gs/v0/matches/
AUTODARTS_BOARDS_URL  = {API_BASE}/bs/v0/boards/
AUTODARTS_USERS_URL   = {API_BASE}/as/v0/users/
AUTODARTS_WEBSOCKET_URL = {WS_BASE}/ms/v0/subscribe
AUTODARTS_CLIENT_ID = load_client_id()  # Keycloak
```

Subscription-Modell (nach Connect gesendet):

```
{ "channel":"autodarts.boards",  "type":"subscribe", "topic":"<boardId>.events" }
{ "channel":"autodarts.matches", "type":"subscribe", "topic":"<matchId>.state" }
```

`unsubscribe` = gleiche Struktur mit `type=unsubscribe`. Topic `<matchId>.game-events` auskommentiert.
Auth: Keycloak `/auth/v1/`, Login via `--autodarts_email`/`--autodarts_password`, Bearer-Token.

### KERNBEFUND (Gap)
`src/DartsHub.Autodarts/Core/AutodartsWebSocketClient.cs` nutzt `wss://api.autodarts.io/connect`
(falscher Host `.io`, falscher Pfad, ohne channel/topic-Subscription). Muss angeglichen werden.

## 2. Darts-Caller
- CLI: 37 Argumente (siehe FEATURE_MATRIX.md).
- Audio: pygame.mixer, VOICE_CHANNEL_ID=1, AMBIENT_CHANNEL_ID=0; `play_sound`, `play_sound_effect`, `play_sound_effect_variant`. Voice blockiert; Ambient blockiert Voice nicht.
- Handler: `handle_connect(auth)`, `handle_disconnect(reason)`, `handle_message(message)`.
- Voice-Packs: `--downloads`, `--downloads_language`, `--downloads_name`, `--remove_old_voice_packs`.
- Sprachen: en-US-v1.csv, it-IT-v1.csv, ru_RU_v1.csv.
- Blind-Support: `blind_support.py`, `--call_blind_support`.
- Extension-Server: Flask-SocketIO (gevent, ping 25/90) + Raw-WS `/api/ext/ws`, `--ws-transport {socketio|raw|both}`. Auth JWT/Lizenz, `--user_license_extensions`. Gehoert NICHT in neuen Caller, sondern DartsHub.Api/ExtensionHost.

## 3. Darts-WLED
- Verbindung: `--connection`, mehrere Geraete via `--wled_endpoints`.
- Effekte: `--effect_duration`, `--effect_brightness`, `--high_finish_effects`, `--game_won_effects`, `--match_won_effects`, `--busted_effects`, `--player_joined_effects`, `--player_left_effects`, `--takeout_effect`, `--calibration_effect`, `--board_stop_effect`, `--sleep_effect`.
- Idle/Player: `--idle_effect` + `--idle_effect_player2..6`, `--player_idle_effects`.
- Score: `--dart_score_BULL_effects`, `--dart_multiplier_effects`, `--combo_effects` (WledScoreAreaHelper).
- Board: `--board_stop_start`, `--board_stop_after_win`, `--wled_off`, `--wled_off_at_start`, `--sleep_timeout`, `--sleep_off_timeout`.
- Test: `--connection_test`, connection_diagnostics.py.
- Module: color_constants.py, combo_effects.py, dart_multiplier_effects.py, player_idle_effects.py, effect_targeting.py, raw_ws_client.py, wled_data_manager.py, caller_auth.py, manifest.sig.json.

## 4. Darts-PixelIt
- Verbindung: `--connection`, `--pixelit_endpoints`, `--templates_path`.
- Effekte: `--effect_brightness`, `--high_finish_effects`, `--app_start_effects`, `--idle_effects`, `--game_start_effects`, `--match_start_effects`, `--game_won_effects`, `--match_won_effects`, `--busted_effects`, `--player_joined_effects`, `--player_left_effects`.
- Templates: templates_path; alter Hub PixelitTemplateProvider/Downloader/TestService.

## 5. Darts-GIF
- Verbindung: `--connection`, Medien via `--media_path`.
- Event-Bilder: `--high_finish_images`, `--game_won_images`, `--match_won_images`, `--busted_images`.
- Web-Ausgabe: `--web_gif`, `--web_gif_port` (Browser).

## 6. Alter Darts-Hub (C#/Avalonia) - App-Management
- Model: Argument.cs, Configuration.cs, Profile.cs, ProfileState.cs, IApp.cs, ExportMetadata.cs, ExportParameter.cs, Notification.cs, ReleaseEventArgs.cs, WledDeviceConfig.cs, Robbel3DConfiguration.cs.
- Control: ProfileManager.cs, Configurator.cs, Updater.cs (+Logger/Tester/TestRunner), DownloadMap.cs, LicenseClient.cs, LicenseManager.cs, CallerAuthMonitor.cs, NotificationManager/Store/Api.cs, ConfigExportManager.cs, RetryHelper.cs, SecurityEnvironmentInspector.cs, ReadmeParser.cs.
- WLED im Hub: WledApi.cs, WledSettings.cs, WledColorDefinitions.cs, WledComboEffectHelper.cs, WledDartMultiplierEffectHelper.cs, WledPlayerIdleEffectHelper.cs, WledScoreAreaHelper.cs, WledShutdownService.cs.
- PixelIt im Hub: PixelitSettings.cs, PixelitTemplateProvider.cs, PixelitTemplateDownloader.cs, PixelitTestService.cs.
- Setup-Wizard: Welcome, Extension-Selection, Caller/WLED/PixelIt/GIF-Steps, Completion, NetworkDeviceScanner.
- Update/Release: Updater laedt Releases/Assets (Catalog), Versionsverwaltung, Download-Mapping.

## Offene Punkte / UNKNOWN
- Darts-Awtrix, Darts-Extern: Detailanalyse ausstehend.
- Caller-Score-Regelwerk (Checkout/Bust, caller_real_life): handle_message-Detailanalyse ausstehend.
- Updater-Signatur/Checksum: nicht verifiziert.
- Payload-Struktur .state/.events: aus broadcast-examples.dat/darts-caller.log extrahierbar (ausstehend).
