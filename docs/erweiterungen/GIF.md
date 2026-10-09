# GIF – Funktionsübersicht

## Medien und Regeln

- Modul einschalten, Medienordner festlegen und lokale GIF-/PNG-/JPEG-Dateien verwenden.
- Direkte öffentliche HTTPS-Bildadresse oder Online-Suchbegriff wählen; Websuche optional deaktivieren.
- Quelle automatisch erkennen oder ausdrücklich lokal, URL bzw. Suche einstellen.
- [Neun Regeltypen](EREIGNISSE.md): Score, Scorebereich, Bust, Spiel-/Matchgewinn, High Finish, Feld, Multiplikator, Kombination.
- Optional Spielername, Score/Bereich und passende Dartbedingung filtern.
- Mehrere Bilder als Zufallsalternativen je Regel; keine Sequenz. Nach Möglichkeit wird das zuletzt verwendete Bild nicht wiederholt.
- Dauer pro Bild: **0** bis zum Takeout, sonst Sekunden bis 3600.
- Bot-Score-/Bust-/Combo-Anzeigen überspringen; High-Finish-Schwelle und Timeout einstellen.

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
