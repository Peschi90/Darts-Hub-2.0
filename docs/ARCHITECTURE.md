# Darts-Hub Architecture

## Zielbild
Darts-Hub ist eine plattformübergreifende Darts-Automation-Runtime für Windows, Linux und macOS.

## Schichten
- `DartsHub.Contracts`: gemeinsame Verträge, Modelle und Statusobjekte
- `DartsHub.Core`: Runtime-Services, Modul-Management, Health, Configuration, EventBus
- `DartsHub.App`: Headless Runtime-Host
- `DartsHub.Api`: REST- und WebSocket-API
- `DartsHub.Gui`: Avalonia Desktop-Client
- `DartsHub.Tui`: Terminal-Client
- `DartsHub.Cli`: Kommandozeilen-Client
- `DartsHub.Api.Client`: gemeinsamer HTTP/WebSocket-Client
- `DartsHub.Modules.*`: offizielle Module
- `DartsHub.Autodarts`: Autodarts-Integration
- `DartsHub.ProcessManager`: externe Apps und Prozesse

## Runtime first
Die Runtime ist der Mittelpunkt des Systems.
GUI, TUI und CLI sind Clients derselben Runtime und dürfen keine eigene Business-Logik duplizieren.

## Beobachtete Ist-Situation
- Core-Services existieren.
- API besitzt Auth, Status und WebSocket-Endpunkte.
- GUI nutzt den API-Client und zeigt Dashboard / Settings / Events.
- TUI ist aktuell noch ein textbasierter Konsolen-Client.
- Die offiziellen Module existieren als Projekte, sind aber noch nicht als vollständiger Runtime-Stack zentral bootstrapped.

## Zielzustand
- Runtime initialisiert Module zentral.
- GUI, TUI und CLI reagieren auf dieselben State-Änderungen.
- Einstellungen werden persistent gespeichert.
- Status- und Event-Daten stammen aus echten Services.
