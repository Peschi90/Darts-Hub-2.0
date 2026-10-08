# Linux installation paths

The online installer defaults to `~/dartshub` for both Linux x64 and ARM64. For the user `autodarts` this is `/home/autodarts/dartshub`.

The shared runtime data directory defaults to the same folder. With no caller media path configured, soundpacks are installed in `~/dartshub/soundpacks`. Settings, authentication data and runtime backups use the shared data directory; GUI preferences, custom translations and update downloads also use the visible folder. Logs are stored in the data directory’s `logs` subfolder.

GUI, TUI (`--tui`) and background mode (`--headless`) share the runtime defaults. An explicit `--DartsHub:DataDirectory PATH` or `DartsHub__DataDirectory` continues to override the runtime directory. An explicitly saved soundpack path or caller media path also remains effective.

Existing installation folders and files are not moved automatically. Close the application before moving an existing installation, and update its desktop/autostart entry by running the installer for the new folder. Preserve existing settings and authentication files when moving the runtime data; the default directory used previously was `~/.local/share/DartsHub`. Windows defaults to `%USERPROFILE%\DartsHub`, with `soundpacks`, `logs`, and `updates` subfolders. macOS defaults are unchanged.

## In-place updates and existing data

Updates initiated in GUI or TUI replace the running published installation at its actual location, including custom folders. They do not use the installer’s default folder. Linux/macOS packages are validated and extracted outside the installation, a helper waits for shutdown, preserves user files and event libraries, backs up replaced files, and restores them if copying fails. The application restarts with its original arguments. The helper log and backup remain in the system temporary `dartshub-update-*` folder for diagnostics/recovery. Registered matching background services are stopped and restored.

Older data directories with `settings.json` are detected when the current installation does not already contain settings. Settings and their encryption keys remain together in the old directory, so logins and absolute soundpack paths stay usable. Explicit data-directory overrides take precedence. A newer existing configuration is never automatically overwritten; files deleted during a previous manual update cannot be reconstructed.

Linux desktop and autostart shortcuts use the packaged `dartshub-logo.png`; matching existing shortcuts are repaired during an update. macOS continues to use its app-bundle icon. No native Linux/macOS session is available on the Windows development host; shell integration tests validate custom-path updates and rollback with simulated Linux and app-bundle layouts.
