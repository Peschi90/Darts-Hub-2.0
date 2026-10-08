# Linux installation paths

The online installer defaults to `~/dartshub` for both Linux x64 and ARM64. For the user `autodarts` this is `/home/autodarts/dartshub`.

The shared runtime data directory defaults to the same folder. With no caller media path configured, soundpacks are installed in `~/dartshub/soundpacks`. Settings, authentication data and runtime backups use the shared data directory; GUI preferences, custom translations and update downloads also use the visible folder. Logs are stored in the data directory’s `logs` subfolder.

GUI, TUI (`--tui`) and background mode (`--headless`) share the runtime defaults. An explicit `--DartsHub:DataDirectory PATH` or `DartsHub__DataDirectory` continues to override the runtime directory. An explicitly saved soundpack path or caller media path also remains effective.

Existing installation folders and files are not moved automatically. Close the application before moving an existing installation, and update its desktop/autostart entry by running the installer for the new folder. Preserve existing settings and authentication files when moving the runtime data; the default directory used previously was `~/.local/share/DartsHub`. Windows defaults to `%USERPROFILE%\DartsHub`, with `soundpacks`, `logs`, and `updates` subfolders. macOS defaults are unchanged.
