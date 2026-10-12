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

### HubX-Posteingang
- `GET /api/v1/hubx/inbox`: Installationsname, echter Verbindungsstatus und wartende Pakete mit Regel-/Dateiliste, Geräteauswahl und Konfigurationsversion.
- `POST /api/v1/hubx/import`: `{ id, confirmed:true, deviceId?, trigger?, resizeIcons:false, configurationVersion }`.
- `POST /api/v1/hubx/reject`: `{ id, confirmed:true }`.

Nur authentifizierte lokale Clients bzw. gekoppelte Webapp-Sitzungen. Vor Übernahme
wird `hubx_access` erneut geprüft; besondere WLED-Regeln erfordern zusätzlich
`im_able_to_read`. Gleichzeitige Änderungen führen zu erneuter Prüfung statt
Überschreiben. Die Gerätezugänge bleiben lokal.

HubX file conflict review: `POST /api/v1/hubx/files` with `{id, deviceId}` returns
existing/incoming animated pixel previews and the current content hash. Import
accepts optional `fileChoices: [{source, name, overwrite, existingHash}]`.
Different existing contents require explicit overwrite plus its reviewed hash,
or a new free filename. Matching bytes are reused. Template display names use
`_hubX`; delivery IDs remain internal. All routes retain local authentication and
HubX license checks.

### HubX-Rechtstexte / Legal documents

`POST /api/v1/hubx/legal` mit `{ "language": "de" }` (oder `en`) lädt die aktuellen Texte, Erklärungen, Version und Revision für die aktive Lizenz. `POST /api/v1/hubx/legal/accept` benötigt `revision`, `language`, `termsAccepted: true` und `privacyAcknowledged: true`. Beide Endpunkte verlangen lokale Authentifizierung und eine gültige HubX-Lizenz. Der Lizenzschlüssel bleibt im Backend. Bei Textänderungen: HTTP 409 / `HubX.LegalChanged`; fehlende Bestätigung: HTTP 428 / `HubX.LegalRequired`. GUI, TUI und Webansicht zeigen die exakten Texte und erfordern zwei ausdrückliche Bestätigungen, bevor das Teilen fortgesetzt wird.

Both endpoints require local authentication and a valid HubX license. The license key stays on the backend. Clients must display the exact versioned texts and request two explicit declarations before continuing the upload. Settings and legacy-import formats are unchanged.

`POST /api/v1/hubx/presets` (`id`, `deviceId`) reviews WLED preset-ID conflicts. Import requests accept `presetChoices` with `sourceId` and `targetId`; occupied or duplicate IDs and unconfirmed conflicts are rejected. Free original IDs are retained and event/playlist references are remapped. GUI, TUI and web share this validation.
