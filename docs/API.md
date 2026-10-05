# Darts-Hub API

## Übersicht
Die API dient als externer Zugangs- und Kommunikationskanal für GUI, TUI und CLI.

## Basis
- `https://localhost:7237`
- `http://localhost:5069`

## Endpunkte
### Auth
- `POST /api/v1/auth/token`

Erzeugt ein lokales JWT für GUI/TUI/CLI-Clients.

### Status
- `GET /api/v1/status`
- `GET /api/v1/status/health`

Liefert Runtime-Status und Health-Informationen.

### Events
- `GET /api/v1/events/stream`

WebSocket-Stream für Runtime-Events.

### Health
- `GET /health`

Einfacher technischer Health-Check des Hosts.

## Authentifizierung
Die API verwendet JWT-Bearer-Authentifizierung. WebSocket-Verbindungen nutzen denselben Token-Mechanismus.

## Aktueller Stand
- Authentifizierung ist vorhanden.
- Status und Event-Stream sind vorhanden.
- Die Runtime-Daten müssen aus den registrierten Core-Services stammen.
