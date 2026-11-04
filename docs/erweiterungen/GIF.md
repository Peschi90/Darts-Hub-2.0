# GIF – Funktionsübersicht

## Medien und Regeln

- Modul einschalten, Medienordner festlegen und lokale GIF-/PNG-/JPEG-Dateien verwenden.
- Direkte öffentliche HTTPS-Bildadresse oder Online-Suchbegriff wählen; Websuche optional deaktivieren.
- Quelle automatisch erkennen oder ausdrücklich lokal, URL bzw. Suche einstellen.
- [Alle Regeltypen](EREIGNISSE.md): Score, Scorebereich, Bust, Spiel-/Matchgewinn, High Finish, Feld, Multiplikator, Kombination.
- Optional Spielername, Score/Bereich und passende Dartbedingung filtern.
- Quelle **Zufällige Datei aus Unterordner** (`Folder`) wählen und einen Unterordner des Medienordners auswählen, etwa `180` oder `scores/180`. Pro Ereignis eine zufällige GIF-/PNG-/JPEG-Datei direkt aus diesem Ordner; weitere Unterordner werden nicht einbezogen. Neue Dateien werden beim nächsten Ereignis berücksichtigt.
- Mehrere Bilder als Zufallsalternativen je Regel; keine Sequenz. Nach Möglichkeit wird das zuletzt verwendete Bild nicht wiederholt.
- Dauer pro Bild: **0** bis zum Takeout, sonst Sekunden bis 3600.
- Bot-Score-/Bust-/Combo-/Cricket-Anzeigen überspringen; High-Finish-Schwelle und Timeout einstellen.

## Anzeige

- GUI-Anzeigefenster, Browseranzeige oder beides; Monitor, Vollbild und „immer im Vordergrund“ fürs GUI-Fenster einstellen.
- Browser-Port und optionale Netzwerkfreigabe; Viewer-Adresse enthält Zugangsschlüssel. Ohne Schlüssel wird die Anzeige nicht ausgeliefert.
- Doppelklick im Browser schaltet Vollbild.
- Aktuelles Bild, Ereignis, Anzeigezustand, Fehler und Viewer-Adresse sehen.
- Entwurf testen, ohne zu speichern; **Bild ausblenden** beendet die Anzeige sofort.
- Bei Takeout, neuem Match/Spiel, Match-Verlassen oder Trennung aufräumen. Match-Verlassen ist kein auswählbarer GIF-Exit-Trigger.

## Grenzen

TUI/Headless brauchen Browsermodus, da sie kein GUI-Fenster darstellen. Namensvergleich ignoriert Schreibweise; GIF hat jedoch keinen zusätzlichen Namensvorrang wie WLED/PixelIt/Awtrix. Lokale Quellen sind auf den Medienkatalog beschränkt; entfernte Quellen müssen zulässige öffentliche HTTPS-Adressen sein. Eine Suche kann ohne Ergebnis bleiben. WLED-Presets werden nicht automatisch zu GIFs konvertiert.

Weiterlesen: [Einrichtung](../GIF.md).

## Bedienung und Diagnose

GUI: Erweiterungsseite öffnen, Entwurf testen und speichern. TUI: `DartsHub --tui`, entsprechende Seite, **Enter** zum Bearbeiten und **Entwurf speichern**. Headless nutzt dieselbe Konfiguration. Vorschautests speichern nichts. Statuswerte und Fehler stehen auf Modulseite, Dashboard und Konsole.

[Gemeinsame Funktionen](GEMEINSAM.md) · [Zur Übersicht](README.md)

## Cricket-Erweiterungen

Gewertete Marks, Feldabschlüsse, tatsächliche Punkte, nicht gewertete Treffer und entdeckte Hidden-Cricket/Tactics-Felder als Regeln auswählen. Dieselbe Auswertung gilt für Tactics, Standard, Cut Throat und No Score. Details und Terminal-Bedienung: [Ereignisse und Textvariablen](EREIGNISSE.md#cricket-tactics-und-hidden-cricket).

## Zufällige Ordnerquelle / Random folder source

DE: Medienordner zunächst speichern. In der Ereignisregel eine Bildalternative mit Quelle **Zufällige Datei aus Unterordner** anlegen, den angebotenen relativen Unterordner auswählen und speichern. Beispielsweise liegt bei Medienordner `/home/autodarts/gifs` und Quelle `scores/180` der Pool in `/home/autodarts/gifs/scores/180`. Ordner werden vom Darts-Hub-Host geladen, auch bei GUI-Fernzugriff, Webapp und SSH/TUI. TUI: GIF → Ereignisse → Regel → Bildalternative → Ordnerquelle → Unterordner wählen. Bei leerer/veralteter Auswahl die Modulseite neu laden; bestehende Pfade werden nicht automatisch gelöscht.

Der Ordner wird pro Auslösung neu gelesen. Bei mindestens zwei Dateien wird die zuletzt daraus angezeigte Datei nach Möglichkeit ausgeschlossen; dies ist keine feste Durchlaufreihenfolge. Alle passenden Dateien direkt im gewählten Ordner werden berücksichtigt, ohne ihre Dateinamen dauerhaft im Arbeitsspeicher zu sammeln. Bis zu 2.048 Unterordner werden für die Auswahl angeboten (maximal acht Ebenen); ein tieferer gültiger relativer Pfad kann manuell eingetragen werden. Die bestehende Begrenzung von 64 Bildalternativen pro Regel betrifft nicht die Dateien innerhalb einer Ordnerquelle. Jede Ordnerquelle ist eine Alternative; mehrere Quellen werden zunächst als Alternativen ausgewählt. Absolute Pfade, `..`, Verzeichnis- und Datei-Symlinks innerhalb des Pools sind nicht zulässig. Leere/fehlende Ordner erzeugen eine sichtbare Fehlermeldung, keine automatische Websuche. Lokale Einzelfiles, URLs und Suchbegriffe bleiben unverändert. Konfiguration und Einstellungsbackup speichern nur den relativen Ordnerpfad und die Dauer; die Mediendateien selbst sind nicht enthalten. Medien beim Umzug separat mitnehmen.

EN: Save the media directory first. Add an image alternative with source **Random file from subfolder**, select a relative host subfolder and save. With media directory `/home/autodarts/gifs` and source `scores/180`, the pool is `/home/autodarts/gifs/scores/180`. GUI remote access, webapp and SSH/TUI all use the backend host catalog. TUI: GIF → events → rule → image alternative → folder source → select subfolder. Reload the module page for changed folder choices; existing source paths are not silently erased.

The folder is read on each trigger. With two or more files, the previously displayed file from the pool is excluded where possible; this is not a shuffled full-cycle queue. All supported GIF/PNG/JPEG files directly in the folder are considered without keeping a large filename array in memory. The picker lists up to 2,048 subfolders across eight levels; deeper valid relative paths may be entered manually. The existing limit of 64 alternatives does not limit the number of files in a folder pool. Each folder is one alternative; multiple sources are first selected as alternatives. Absolute paths, `..`, and directory/file symlinks inside the pool are rejected. Empty/missing pools report an error and never fall back to online search. Local files, URLs and search sources keep their existing behavior. Configuration/backups store the relative source path and duration, not the media files; transfer media separately when moving systems.
