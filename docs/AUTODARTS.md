# Autodarts-Anbindung - Referenz und Zielarchitektur

> Basis: `darts-caller.py` (Source of Truth). Diese Datei dokumentiert das reale
> Legacy-Protokoll und die Ziel-Implementierung in `DartsHub.Autodarts`.

## 1. Endpunkte (Legacy)

| Zweck | URL |
|---|---|
| API-Basis | `https://api.autodarts.com` (env `AUTODARTS_API_URL`) |
| WS-Basis | `wss://api.autodarts.com` (env `AUTODARTS_WS_URL`) |
| Auth (Keycloak) | `{API}/auth/v1/` |
| Boards | `{API}/bs/v0/boards/` |
| Matches | `{API}/gs/v0/matches/` |
| Lobbies | `{API}/gs/v0/lobbies/` |
| Users/Stats | `{API}/as/v0/users/` |
| WebSocket | `{WS}/ms/v0/subscribe` |

Client-ID: `load_client_id()` (Keycloak-Client, aus Konfiguration geladen).

## 2. Verbindungsaufbau

1. Login via Keycloak (`/auth/v1/`) mit E-Mail/Passwort -> Access-Token (Bearer).
2. WebSocket-Connect auf `{WS}/ms/v0/subscribe` mit Authorization-Header/Handshake-Auth.
3. Subscribe-Nachrichten senden:

```json
{ "channel": "autodarts.boards",  "type": "subscribe", "topic": "<boardId>.events" }
{ "channel": "autodarts.matches", "type": "subscribe", "topic": "<matchId>.state" }
```

4. Bei Match-Wechsel: alte Match-Topics `unsubscribe`, neue `subscribe`.

`unsubscribe`:
```json
{ "channel": "autodarts.matches", "type": "unsubscribe", "topic": "<matchId>.state" }
{ "channel": "autodarts.boards",  "type": "unsubscribe", "topic": "<boardId>.events" }
```

Auskommentiert im Legacy (nicht aktiv): Topic `<matchId>.game-events`.

## 3. Nachrichten-Verarbeitung (Legacy)

- Board-Events (`<boardId>.events`): Board-Status, Takeout-Erkennung, Kalibrierung.
- Match-State (`<matchId>.state`): vollständiger Match-Zustand (Spieler, Turn, Score,
  Bust, Checkout, Game/Leg/Set, Winner). Der Caller leitet daraus die Ansagen ab.
- Board-Reset/Kalibrierung lokal: `POST <boardManager>/api/reset`,
  `POST <boardManager>/api/config/calibration/auto`.

> Genaue Feldnamen der `.state`/`.events`-Payloads sind aus `broadcast-examples.dat`
> und `darts-caller.log` zu extrahieren (Basis für Parser-Tests, UNKNOWN bis verifiziert).

## 4. Zielarchitektur (neu)

```
Autodarts  ->  DartsHub.Autodarts (Connect/Auth/Subscribe)
		   ->  Parsing/State (MatchStateParser, State-Machine)
		   ->  DartsHub Events (interne Event-Contracts)
		   ->  EventBus
		   ->  Caller / WLED / PixelIt / GIF / External Extensions
```

- Zentrale Verbindung ausschließlich in `DartsHub.Autodarts`. Module verbinden sich NICHT selbst.
- State-Machine: ConnectionState, BoardState, MatchState, GameState, TurnState,
  PlayerState, ThrowState, ScoreState.
- Reconnect: Connecting/Connected/Disconnected/Reconnecting/AuthenticationFailed/Error
  mit CancellationToken, Backoff, Logging, Health.

## 5. Gap zum aktuellen Code

`src/DartsHub.Autodarts/Core/AutodartsWebSocketClient.cs`:
- ✅ Endpoint auf `{WS_BASE}/ms/v0/subscribe` korrigiert (Default `wss://api.autodarts.com/ms/v0/subscribe`,
  überschreibbar via `WebSocketUrl`).
- ✅ channel/topic-Subscription-Modell implementiert:
  `SubscribeToBoardEventsAsync`/`UnsubscribeFromBoardEventsAsync` (`autodarts.boards`, `<boardId>.events`)
  und `SubscribeToMatchAsync`/`UnsubscribeFromMatchAsync` (`autodarts.matches`, `<matchId>.state`).
- ✅ Reconnect-/Receive-Loop-Grundgerüst vorhanden.

`src/DartsHub.Autodarts/AutodartsModule.cs`:
- ✅ Board-ID konfigurierbar (`BoardId`-Property + Fallback `AUTODARTS_BOARD_ID`), nicht mehr `"default"`.
- ✅ Abonniert beim Connect die Board-Events (Legacy-Verhalten).
- ✅ Envelope-Routing implementiert (`channel`/`topic`/`data`): Board-Events extrahieren die Match-ID
  und lösen dynamisch `SubscribeToMatchAsync`/`UnsubscribeFromMatchAsync` bei Match-Wechsel aus;
  Match-Events werden an den `MatchStateParser` übergeben.

**Tests:** `tests/DartsHub.Core.Tests/AutodartsMatchStateParserTests.cs` deckt Match-Parsing,
Variant-Erkennung und Change-Detection (Score, Game-Won) ab (11 Tests, grün).

- ✅ Reconnect-Logik mit exponentiellem Backoff (2s → max 60s), CancellationToken und
  Re-Authentifizierung/Re-Subscribe implementiert (`ReconnectAsync`). Läuft nur solange das Modul
  im Running-Zustand ist; `ConnectAsync` verwirft alte Sockets vor dem Neuaufbau.

**Nächster Schritt (Phase 2 fortlaufend):** Parser-Verfeinerung anhand realer `.state`/`.events`-Payloads
aus `broadcast-examples.dat`/`darts-caller.log`; danach Phase 4 (Caller-Config-Parität + Audio-Abstraktion).

## 6. Konfiguration: Device-Flow wie Legacy (`darts-caller`)

Für den API-Host (`src/DartsHub.Api`) gilt jetzt:

- **Feste Client-ID:** `darts-caller`
- **Kein Client-Secret erforderlich**
- `BoardId` bleibt benutzerkonfigurierbar über die Anwendung (`/api/v1/settings/autodarts`)

Optional weiterhin:

- `AUTODARTS_WEBSOCKET_URL` (Default: `wss://api.autodarts.com/ms/v0/subscribe`)

Konfigurierbar in `appsettings.json` bleibt nur die technische Endpoint-Konfiguration (`Autodarts:AuthorizationEndpoint`, `Autodarts:TokenEndpoint`, `Autodarts:Scopes`, `Autodarts:WebSocketUrl`) sowie optional initiale `Autodarts:BoardId`.

## 7. Definition of Done

Echte Verbindung, Reconnect, State, Throw/Score/Player/Turn/Game erkannt,
relevante Match-Events, interne Events erzeugt, Parser-Tests vorhanden.
