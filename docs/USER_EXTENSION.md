# User-Erweiterung / User extension

## Deutsch

Die **User-Erweiterung** verwaltet ein externes Skript und ist getrennt von gewöhnlichen **Eigenen Anwendungen**. Du benötigst eine vom Betreiber ausgestellte **Client-ID und ein Secret**.

1. Client-ID und Secret eingeben und den Zugriff freischalten.
2. Ein vertrauenswürdiges Skript importieren, den installierten Interpreter und erforderliche Startparameter einstellen.
3. Speichern und aktivieren. Start/Stop ist auch im Dashboard verfügbar.
4. In der eigenen Skriptkonsole Ausgaben, Fehlermeldungen und Start-/Stopstatus prüfen. Zugangsdaten werden geschützt gespeichert und in Ausgaben maskiert.
5. Zum Entfernen die angebotene Skript-entfernen-Aktion bestätigen. Das verwaltete Skript wird beendet und seine lokale Kopie entfernt.

Das Skript erhält gefilterte Spielinformationen, keine unveränderten Autodarts-Nachrichten. Für eigene Clients den Betreiber nach der Payload-Dokumentation fragen. Skripte laufen mit den Rechten des Darts-Hub-Benutzers; Python muss auf dem Host installiert sein, wenn es als Interpreter verwendet wird. Zugangsdaten nicht öffentlich teilen.

TUI: **User-Erweiterung** öffnen. Remote-Verwaltung über die Weboberfläche ist eingeschränkt; das Skript am Host über GUI/TUI verwalten.

## English

A **User extension** is a managed external script, separate from ordinary **Own applications**. Unlock it with an operator-issued client ID and secret, import a trusted script, select its installed interpreter, save and enable it. Use the dashboard for start/stop and its dedicated console for output/errors. Credentials are stored securely and redacted. Confirm script removal to stop and remove the managed copy.

Scripts receive filtered game information, not raw Autodarts messages. Ask the operator for the developer reference. Scripts run as the Darts-Hub user; Python scripts require Python on the host. Manage them locally through GUI/TUI; remote web management is restricted.
