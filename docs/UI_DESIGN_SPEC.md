# Darts-Hub UI Design Spec

Diese Spezifikation definiert das Ziel-UI-System für Darts-Hub.

## Designziele
- dunkel
- technisch
- professionell
- klar
- modern
- dezenter Neon-/Glow-Effekt
- Darts-bezogen

Nicht:
- übertriebenes Gaming-Design
- Cyberpunk-Overkill
- bunte Verlaufsflächen überall
- Glassmorphism auf jedem Element
- visuelle Attrappen ohne echte Funktion

## Farbpalette
Zentrale Theme-Ressourcen verwenden. Keine harten Farbcodes in einzelnen Views.

- Background: `#07111D`
- Navigation Background: `#081421`
- Surface: `#0B1726`
- Surface Elevated: `#0E1C2D`
- Surface Hover: `#12243A`
- Border: `#173D5E`
- Border Highlight: `#176DA5`
- Primary: `#179BFF`
- Primary Bright: `#20C4FF`
- Text Primary: `#F1F6FC`
- Text Secondary: `#A9B8C8`
- Text Muted: `#708297`
- Success: `#2DE58A`
- Warning: `#FFB547`
- Error: `#FF5D6C`

## Layoutprinzip
Die Desktop-Anwendung nutzt eine Shell-Struktur:

- Top Bar
- linke Navigation
- Main Content

### Navigationbreite
- ca. 210–240 px

### Top Bar
Enthält kompakt:
- aktuellen Bereich
- Runtime-Status
- Autodarts-Status
- Versionshinweis
- Fensteraktionen

Keine große Toolbar.

## Navigation
Eigene Seiten für:
- Dashboard
- Autodarts
- Caller
- WLED
- PixelIt
- GIF
- External Apps
- User Extensions
- Logs
- Settings
- System

Module dürfen nicht auf einer einzigen Sammelseite zusammengequetscht werden.

## Dashboard
Das Dashboard ist eine Status- und Übersichtsseite.
Es ist keine vollständige Konfigurationsseite.

Enthaltene Bereiche:
- Hero-Zone
- Runtime-Statuskarten
- Modulübersicht
- Recent Events
- optional Current Match

### Modulkarten
Kompakte Karten für:
- Caller
- WLED
- PixelIt
- GIF

Jede Karte zeigt:
- Name
- Enabled / Disabled
- Running / Stopped / Error
- Version
- kurze Quick Action

## Module Pages
Jedes Hauptmodul erhält eine eigene Seite.

### Caller
Tabs oder Bereiche je nach tatsächlicher Funktion:
- Allgemein
- Sounds
- Score Calls
- Game Calls
- Player Calls
- Audio
- Events
- Advanced

### WLED
- General
- Devices
- Animations
- Event Mapping
- Colors
- Brightness
- Testing
- Advanced

### PixelIt
- General
- Devices
- Display
- Events
- Animations
- Testing
- Advanced

### GIF
- General
- Output
- Media
- Event Mapping
- Playback
- Testing
- Advanced

### Autodarts
- Connection
- Game / Event State
- Players
- Diagnostics
- Advanced

### External Apps
- Name
- Executable
- Arguments
- Auto Start
- Restart on Crash
- Status
- PID
- Actions

### User Extensions
- Name
- Version
- Runtime
- Status
- API Version
- Permissions
- Connected / Disconnected
- Last Seen

### Logs
- Filter
- Search
- Live Update
- Level
- Source
- Message

### Settings
Nur globale Einstellungen.
Keine Modulkonfiguration in die globalen Settings verschieben.

### System
- Version
- Runtime Version
- OS
- Architecture
- App Data Path
- Config Path
- Log Path
- API State
- IPC State
- Uptime
- CPU
- RAM

## Komponenten
Wiederverwendbare UI-Bausteine:
- StatusCard
- ModuleCard
- SectionCard
- StatusBadge
- PageHeader
- SettingsSection
- LabeledToggle
- InfoRow
- EmptyState
- ErrorBanner
- HealthIndicator

## Verhalten
- Jeder Button braucht einen echten Command.
- Kein Control darf nur lokal togglen.
- Loading-, Error- und Empty-States sichtbar machen.
- Änderungen müssen in Runtime/Service/Module zurückfließen.
- Design-Time-Daten nur in Preview-Kontexten.

## Typografie und Abstände
- klare Hierarchie: Page Title, Section Header, Card Title, Body, Secondary, Caption
- konsistentes Spacing: 4, 8, 12, 16, 24, 32
- CornerRadius typischerweise 8–12

## TUI-Richtung
Die TUI folgt dem gleichen Informationsmodell wie die GUI, ist aber keyboard-first und Terminal.Gui v2-basiert.
Sie soll nicht wie ein einfacher Text-Explorer wirken.
