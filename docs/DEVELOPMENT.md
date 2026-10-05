# Darts-Hub Development

## Voraussetzungen
- .NET 10 SDK
- Visual Studio 2026 oder kompatible IDE

## Build
```powershell
dotnet restore DartsHub.sln
dotnet build DartsHub.sln
```

## Tests
```powershell
dotnet test DartsHub.sln
```

## Starten
### API
Startet den API-Host aus `src/DartsHub.Api`.

### GUI
Startet den Avalonia-Client aus `src/DartsHub.Gui`.

### TUI
Startet den Terminal-Client aus `src/DartsHub.Tui`.

### CLI
Startet den CLI-Client aus `src/DartsHub.Cli`.

## Arbeitsweise
- Erst analysieren, dann klein und gezielt ändern.
- Keine Fake-Funktionalität einführen.
- UI immer gegen echte Runtime-Services binden.
- Nach größeren Änderungen Build und Tests ausführen.
