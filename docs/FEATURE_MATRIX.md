# Feature Matrix - Darts-Hub 2.0

> Klassifikation: IMPLEMENTED | PARTIAL | MISSING | OBSOLETE | UNKNOWN. Legacy-Code ist Source of Truth.

## A. Funktions-Matrix

| Legacy App | Feature | Source File | Config | Events | Dependencies | Target Component | Implemented | Tested |
|---|---|---|---|---|---|---|---|---|
| Caller | Autodarts-WS-Verbindung | darts-caller.py | AUTODARTS_WEBSOCKET_URL | connect/disconnect/message | Keycloak,websocket | DartsHub.Autodarts | PARTIAL (falscher Endpoint) | MISSING |
| Caller | Board-Events subscribe | darts-caller.py | topic <boardId>.events | board events | WS | DartsHub.Autodarts | MISSING | MISSING |
| Caller | Match-State subscribe | darts-caller.py | topic <matchId>.state | match state | WS | DartsHub.Autodarts | MISSING | MISSING |
| Caller | Audio-Ausgabe | darts-caller.py | -V,-BAV,-LPB,-MIF/-MIS/-MIC/-MIB | throw/score/bust/checkout | pygame.mixer | DartsHub.Modules.Caller | PARTIAL | MISSING |
| Caller | Soundpack-Verwaltung | darts-caller.py | -M,-MS | - | Dateisystem | Caller.Soundpacks | PARTIAL | MISSING |
| Caller | Voice-Pack-Download | darts-caller.py | -DL,-DLLA,-DLN,-ROVP | - | HTTP | DartsHub.Modules.Caller | MISSING | MISSING |
| Caller | Checkout-Ansage | darts-caller.py | -PCC,-PCCYO | checkout | Audio | Caller.Calling | MISSING | MISSING |
| Caller | Call-every-dart | darts-caller.py | -E,-ETS | throw | Audio | Caller.Calling | MISSING | MISSING |
| Caller | Ambient-Sounds | darts-caller.py | -A,-AAC | idle | Audio | Caller | MISSING | MISSING |
| Caller | Blind-Support | blind_support.py | -CBS | throw | Audio | Caller | MISSING | MISSING |
| Caller | Random-Caller | darts-caller.py | -R,-RL,-RG | - | - | Caller | MISSING | MISSING |
| Caller | Extension-Server | darts-caller.py | -HP,-WST,-ULE | ext events | Flask-SocketIO | DartsHub.Api/ExtensionHost | PARTIAL | MISSING |
| WLED | Geraete-Kommunikation | darts-wled.py | -CON,-WEPS | Match-Events | requests | DartsHub.Modules.Wled | DONE | PARTIAL |
| WLED | Event->Effect-Mapping | darts-wled.py | -HF,-G,-M,-B,-PJ,-PL | throw/game/match/bust | - | DartsHub.Modules.Wled | PARTIAL (inkl. player_joined/player_left, takeout/calibration) | PARTIAL |
| WLED | Score/Multiplier/Combo | *_effects.py | -DSBULL,-DMU,-CMB | score | Helper | DartsHub.Modules.Wled | PARTIAL (DMU + Combo umgesetzt, restliche Spezialfaelle offen) | PARTIAL |
| WLED | Idle/Player-Idle | player_idle_effects.py | -IDE,-IDE2..6,-PIDE | idle/player | - | DartsHub.Modules.Wled | PARTIAL (Sleep + player_idle_effects Parsing/Aufloesung umgesetzt; volle Turn-Idle-Paritaet offen) | PARTIAL |
| WLED | Board-Stop/Sleep/Off | darts-wled.py | -BSS,-BSW,-OFF,-SOFF,-SLE | board/idle | HTTP | DartsHub.Modules.Wled | PARTIAL (inkl. connection_test/takeout/calibration-Boardstatuspfade) | PARTIAL |
| WLED | Connection-Test | connection_diagnostics.py | -CT | - | HTTP | DartsHub.Modules.Wled | PARTIAL | PARTIAL |
| GUI | WLED Settings bearbeiten/speichern | DartsHub.Gui MainWindow | Host/Port/Timeout/Brightness/Sleep/Flags | save action | DartsHub.Api.Client | DartsHub.Gui + DartsHub.Api | PARTIAL (Write-Back fuer WLED-Basiseinstellungen umgesetzt) | PARTIAL |
| PixelIt | Geraete-Kommunikation | darts-pixelit.py | -CON,-PEPS | Match-Events | requests | DartsHub.Modules.PixelIt | PARTIAL | MISSING |
| PixelIt | Templates | darts-pixelit.py | -TP | - | Dateisystem | DartsHub.Modules.PixelIt | MISSING | MISSING |
| PixelIt | Event-Effekte | darts-pixelit.py | -HF,-AS,-IDE,-GS,-MS,-G,-M,-B,-PJ,-PL | game/match/bust/player | HTTP | DartsHub.Modules.PixelIt | MISSING | MISSING |
| GIF | Web-Wiedergabe | darts-gif.py | -WEB,-WEBP | game/match/bust/finish | Browser/HTTP | DartsHub.Modules.Gif (fehlt) | MISSING | MISSING |
| GIF | Medien-/Event-Mapping | darts-gif.py | -MP,-HF,-G,-M,-B | game/match/bust | Dateisystem | DartsHub.Modules.Gif (fehlt) | MISSING | MISSING |
| Alter Hub | Prozess-/App-Start | ProfileManager.cs | Profile/Argument | - | Process | DartsHub.ProcessManager | PARTIAL | MISSING |
| Alter Hub | Update-/Release-System | Updater.cs | Catalog | - | HTTP/GitHub | DartsHub (fehlt) | MISSING | MISSING |
| Alter Hub | License/Auth | LicenseManager.cs | Token | - | HTTP | DartsHub.Api | UNKNOWN | MISSING |
| Alter Hub | Setup-Wizard | SetupWizardManager.cs | alle | - | UI | DartsHub.Gui | MISSING | MISSING |
| Alter Hub | Config-Export/Import | ConfigExportManager.cs | Profile | - | Dateisystem | DartsHub.Core | MISSING | MISSING |

## B. Konfigurations-Matrix Caller (37 CLI-Argumente)

| Legacy App | Setting | Old Key | Type | Default | New Setting | Persisted | GUI | TUI |
|---|---|---|---|---|---|---|---|---|
| Caller | E-Mail | -U/--autodarts_email | string | - | CallerOptions.Email | MISSING | MISSING | MISSING |
| Caller | Passwort | -P/--autodarts_password | secret | - | CallerOptions.Password | MISSING | MISSING | MISSING |
| Caller | Board-ID | -B/--autodarts_board_id | string | - | AutodartsOptions.BoardId | MISSING | MISSING | MISSING |
| Caller | Media-Pfad | -M/--media_path | path | - | CallerOptions.MediaPath | PARTIAL | MISSING | MISSING |
| Caller | Media-Pfad shared | -MS/--media_path_shared | path | - | CallerOptions.MediaPathShared | MISSING | MISSING | MISSING |
| Caller | Lautstaerke | -V/--caller_volume | float | UNKNOWN | CallerOptions.Volume | PARTIAL | MISSING | MISSING |
| Caller | Caller (Voice) | -C/--caller | string | UNKNOWN | CallerOptions.Caller | PARTIAL | MISSING | MISSING |
| Caller | Random-Caller | -R/--random_caller | int | UNKNOWN | CallerOptions.RandomCaller | MISSING | MISSING | MISSING |
| Caller | Random-Language | -RL/--random_caller_language | int | UNKNOWN | CallerOptions.RandomLanguage | MISSING | MISSING | MISSING |
| Caller | Random-Gender | -RG/--random_caller_gender | int | UNKNOWN | CallerOptions.RandomGender | MISSING | MISSING | MISSING |
| Caller | Call-current-player | -CCP/--call_current_player | int | UNKNOWN | CallerOptions.CallCurrentPlayer | MISSING | MISSING | MISSING |
| Caller | Call-bot-actions | -CBA/--call_bot_actions | int | UNKNOWN | CallerOptions.CallBotActions | MISSING | MISSING | MISSING |
| Caller | Call-every-dart | -E/--call_every_dart | int | UNKNOWN | CallerOptions.CallEveryDart | MISSING | MISSING | MISSING |
| Caller | Every-dart-total | -ETS/--call_every_dart_total_score | int | UNKNOWN | CallerOptions.CallEveryDartTotal | MISSING | MISSING | MISSING |
| Caller | Checkout-Call | -PCC/--possible_checkout_call | int | UNKNOWN | CallerOptions.PossibleCheckoutCall | MISSING | MISSING | MISSING |
| Caller | Checkout-yourself | -PCCYO/--possible_checkout_call_yourself_only | int | UNKNOWN | CallerOptions.CheckoutYourselfOnly | MISSING | MISSING | MISSING |
| Caller | Ambient-Sounds | -A/--ambient_sounds | float | UNKNOWN | CallerOptions.AmbientSounds | MISSING | MISSING | MISSING |
| Caller | Ambient-after-calls | -AAC/--ambient_sounds_after_calls | int | DEFAULT_* | CallerOptions.AmbientAfterCalls | MISSING | MISSING | MISSING |
| Caller | Downloads | -DL/--downloads | int(0-100) | UNKNOWN | CallerOptions.Downloads | MISSING | MISSING | MISSING |
| Caller | Download-Language | -DLLA/--downloads_language | int | UNKNOWN | CallerOptions.DownloadsLanguage | MISSING | MISSING | MISSING |
| Caller | Download-Name | -DLN/--downloads_name | string | UNKNOWN | CallerOptions.DownloadsName | MISSING | MISSING | MISSING |
| Caller | Remove-old-packs | -ROVP/--remove_old_voice_packs | int | UNKNOWN | CallerOptions.RemoveOldVoicePacks | MISSING | MISSING | MISSING |
| Caller | Background-Volume | -BAV/--background_audio_volume | float(0.1-1.0) | UNKNOWN | CallerOptions.BackgroundVolume | MISSING | MISSING | MISSING |
| Caller | Local-Playback | -LPB/--local_playback | int | UNKNOWN | CallerOptions.LocalPlayback | MISSING | MISSING | MISSING |
| Caller | Web-disable-https | -WEBDH/--web_caller_disable_https | int | UNKNOWN | CallerOptions.WebDisableHttps | MISSING | MISSING | MISSING |
| Caller | Host-Port | -HP/--host_port | int | DEFAULT_HOST_PORT | ApiOptions.Port | PARTIAL | MISSING | MISSING |
| Caller | Debug | -DEB/--debug | int | UNKNOWN | CallerOptions.Debug | PARTIAL | MISSING | MISSING |
| Caller | Message-log-all | -MLA/--message_log_all | int | 0 | CallerOptions.MessageLogAll | MISSING | MISSING | MISSING |
| Caller | Cert-Check | -CC/--cert_check | int | UNKNOWN | AutodartsOptions.CertCheck | MISSING | MISSING | MISSING |
| Caller | Mixer-Frequency | -MIF/--mixer_frequency | int | DEFAULT_MIXER_FREQUENCY | CallerOptions.MixerFrequency | MISSING | MISSING | MISSING |
| Caller | Mixer-Size | -MIS/--mixer_size | int | DEFAULT_MIXER_SIZE | CallerOptions.MixerSize | MISSING | MISSING | MISSING |
| Caller | Mixer-Channels | -MIC/--mixer_channels | int | 2 | CallerOptions.MixerChannels | MISSING | MISSING | MISSING |
| Caller | Mixer-Buffersize | -MIB/--mixer_buffersize | int | DEFAULT_MIXER_BUFFERSIZE | CallerOptions.MixerBuffersize | MISSING | MISSING | MISSING |
| Caller | Caller-real-life | -CRL/--caller_real_life | int | UNKNOWN | CallerOptions.RealLife | MISSING | MISSING | MISSING |
| Caller | Blind-Support | -CBS/--call_blind_support | int | UNKNOWN | CallerOptions.BlindSupport | MISSING | MISSING | MISSING |
| Caller | User-License-Ext | -ULE/--user_license_extensions | int | UNKNOWN | ExtensionOptions.UserLicense | MISSING | MISSING | MISSING |
| Caller | WS-Transport | -WST/--ws-transport | enum | both | ExtensionOptions.Transport | MISSING | MISSING | MISSING |

> Exakte DEFAULT_-Zahlenwerte muessen aus dem Konstanten-Block von darts-caller.py verifiziert werden.

> **Update (Phase 4):** Die Caller-Settings sind jetzt im Modell `CallerConfig`
> (`src/DartsHub.Modules.Caller/Models/CallerConfig.cs`) mit den **verifizierten** Legacy-Defaults
> abgebildet (u.a. RandomCaller=1, MixerFrequency=44100, MixerSize=32, MixerChannels=2,
> MixerBuffersize=4096, Downloads=3, LocalPlayback=true, CallBotActions=true,
> CallEveryDartTotalScore=true, PossibleCheckoutCall=1). Validierung via `CallerConfig.Validate()`
> (Volume/AmbientSounds 0..1, BackgroundAudioVolume 0 oder 0.1..1.0, Downloads 0..100, Mixer > 0).
> Persistenz laeuft ueber `IConfigurationService` (`com.dartshub.caller`). Tests:
> `tests/DartsHub.Core.Tests/CallerConfigTests.cs` (11 Tests, gruen). Offen: GUI/TUI-Bindings
> fuer die neuen Felder, Anwendung zur Laufzeit im Audio-Pfad.

> **Update (Phase 4, Audio):** Cross-Platform-Audio-Abstraktion aktiv. `CallerModule` nutzt jetzt
> `AudioBackendFactory` (`src/DartsHub.Infrastructure/Audio/AudioBackendFactory.cs`) statt harter
> Windows-Kopplung: Windows verwendet NAudio/System.Speech, andere Plattformen bzw. Headless-
> Umgebungen ohne Audio-Session fallen sauber auf `NullAudioDevice`/`NullTtsEngine` zurueck (Warnung
> statt Crash). Config wird beim Init via `CallerConfig.Validate()` geprueft. Tests:
> `tests/DartsHub.Core.Tests/NullAudioBackendTests.cs` (6 Tests, gruen). Offen: nativer Linux/macOS-
> Audiobackend (aktuell dokumentierte Luecke), GUI/TUI-Bindings.

## C. WLED / PixelIt / GIF
Vollstaendige Argumentliste in LEGACY_ANALYSIS.md (Abschnitte 3-5). Mapping auf WledOptions /
PixelItOptions / GifOptions je Modul-Phase; aktuell durchgehend MISSING/PARTIAL bis Portierung + Tests.
