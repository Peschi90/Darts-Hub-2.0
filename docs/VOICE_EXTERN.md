# darts-voice und darts-extern / Voice and Extern

Aktueller Quellstand für die nächste Beta. Bereits veröffentlichte Pakete enthalten diese Module möglicherweise noch nicht.

## Einrichtung (Deutsch)

Beide Module haben eigene Seiten **darts-voice** und **darts-extern** in GUI und TUI.
Sie verwenden gemeinsame Einstellungen, Validierung und echte Laufzeitmeldungen.
Ein separater alter darts-caller und dessen Socket.IO-Anmeldung werden nicht benötigt.
Die Hilfsprogramme sind in Darts-Hub eingebettet und werden vom Backend gestartet
und beim Deaktivieren, Speichern, Neustart oder Beenden geschlossen. Sie benötigen
einen lokal installierten Python-Interpreter mit den folgenden Paketen.

| Hub-System | Python / native Voraussetzungen |
| --- | --- |
| Windows x64 | Python x64, Vosk 0.3.45, sounddevice 0.5.3; für Extern Playwright 1.56.0 und Chrome/Edge/Chromium |
| Windows ARM64 | Für Voice Python **x64** unter Windows-Emulation auswählen, da Vosk kein Windows-ARM64-Wheel anbietet. Extern kann auch Python ARM64 verwenden. Befehle und Erkennung sind identisch. |
| Linux x64 / ARM64 | Python der passenden Architektur, Vosk 0.3.45, sounddevice 0.5.3, PortAudio (`libportaudio2`); für Extern Playwright 1.56.0 und Chromium sowie eine grafische Sitzung |
| macOS x64 / ARM64 | Python der passenden Architektur, Vosk **0.3.44** (Universal2), sounddevice 0.5.3, Mikrofonfreigabe; für Extern Playwright 1.56.0 und Chromium/Chrome/Edge |

Installation in genau der Python-Umgebung, die anschließend im Modul eingetragen wird:

```powershell
# Windows x64 (auch Voice auf Windows ARM64 mit x64-Python)
python -m pip install vosk==0.3.45 sounddevice==0.5.3 playwright==1.56.0
```

```sh
# Linux x64 / ARM64; PortAudio über die Paketverwaltung installieren
python3 -m pip install vosk==0.3.45 sounddevice==0.5.3 playwright==1.56.0
# macOS x64 / ARM64
python3 -m pip install vosk==0.3.44 sounddevice==0.5.3 playwright==1.56.0
```

Eine virtuelle Umgebung ist geeignet; den vollständigen Pfad zu deren Python
eintragen. Wer nur Extern verwendet, benötigt nur `playwright==1.56.0`.
Vosk-Modell, Python-Pakete und Browser werden nicht automatisch heruntergeladen.
Die eingebettete `requirements.txt` wird beim Modulstart zusätzlich im jeweiligen
Unterordner `integrations/voice` bzw. `integrations/extern` des
[Hub-Datenverzeichnisses](LINUX_PATHS.md) abgelegt. Browserprofile, Sprachmodelle
und ausführbare Programme sind kein Bestandteil von Einstellungsbackups.

### Voice

1. In Autodarts das Board auswählen und die Geräteanmeldung abschließen.
2. Ein passendes [Vosk-Modell](https://alphacephei.com/vosk/models) herunterladen
   und entpacken. Unter **darts-voice** dessen Ordner und Python eintragen.
3. Sprache wählen: **1 = Englisch**, **2 = Deutsch**, **0 = nur eigene Wörter**.
   Eigene Schlüsselwörter ergänzen die Vorgaben; ein Ausdruck pro Zeile in der GUI,
   einzelne Listeneinträge im TUI-Editor. Optional Mikrofonname oder Geräteindex
   von sounddevice eintragen; leer verwendet das Standardmikrofon des Hub-Rechners.
4. Aktivieren und **Speichern und anwenden**. **Hört zu** bestätigt die geöffnete
   Erkennung. Bei Mikrofonverlust wird nach fünf Sekunden erneut versucht.
5. Mit **Gespeicherte Schlüsselwörter testen** einen Text prüfen. Dieser Test
   parst ausschließlich und führt keinen Spiel- oder Boardbefehl aus.

Beispiele: `next`, `next game`, `undo`, `start board`, `calibrate board`,
`first is twenty five`, `second and last is miss`, `weiter`, `nächstes spiel`,
`zurück`, `kalibrieren`, `dritter ist doppel zehn`.
Mehrere referenzierte Darts werden gemeinsam korrigiert. Caller-Wechsel und
Caller-Ausschluss verwenden installierte passende Stimmen; Ausschlüsse gelten
bis zum nächsten Hub-Neustart und löschen keine Soundpacks.

Audio wird offline erkannt und nicht hochgeladen oder aufgezeichnet.
Die Diagnose zeigt Zustand und ausgeführten Befehl, keine freie Transkription.
Spiel- und Boardaktionen verwenden die vorhandene Autodarts-Geräteanmeldung.

### Extern

1. Python, den **ausführbaren Browserpfad**, Plattform und den **lokalen
   Autodarts-Spielernamen** eintragen. Das Board muss in Hub ausgewählt sein.
2. Aktivieren und speichern. Im separaten Browserprofil bei der Plattform
   anmelden und ein Spiel starten. Beim ersten lokalen Lobbyaufbau zusätzlich
   interaktiv bei Autodarts im Modulbrowser anmelden. Hub exportiert keine
   OAuth-Tokens oder Passwörter in diesen Browser.
3. Die Browsersteuerung erstellt wie im Vorgänger eine private lokale
   Autodarts-Lobby mit den externen Anfangspunkten und dem gewählten Board.
   Der Hub-Ereignisbus liefert die Aufnahmen; nur menschliche Spieler mit
   passendem Namen und passendem Board werden berücksichtigt.
4. Bei X01 wird beim Ziehen der Darts die endgültige Aufnahme übertragen;
   Korrekturen davor werden berücksichtigt. Gewinnaufnahmen werden sofort
   übertragen und bei anschließendem Takeout nicht verdoppelt. Auf Lidarts bleibt
   eine X01-Gewinnaufnahme wie im Vorgänger zur manuellen Bestätigung im Feld.
5. Bei Zeitüberschreitung oder unklarem Übertragungsergebnis wird kein Score
   automatisch wiederholt. Spielstände prüfen und mit gespeicherten Einstellungen
   neu starten. Nach Matchende schließt der Browser nach der eingestellten Wartezeit.

Unterstützt: **Lidarts, Nakka und Dartboards – X01**; **Cricket nur Lidarts**.
Webcamdarts war im bereitgestellten Vorgänger nicht als Plattform freigegeben
und wird nicht als funktionierende Integration angeboten. Extern hängt von den
Seitenstrukturen der Plattformen ab; ein erfolgreicher Test mit lokalen Testseiten
belegt keinen aktuellen Live-Spielbetrieb dieser fremden Dienste.
Lidarts unterstützt optionale Start-/Endnachrichten und Jitsi-Kamera-Vollbild.
Die Dart-Abfragepräferenzen bleiben je Plattform getrennt erhalten; wie im
Vorgänger existieren für Dartboards keine implementierten Bestätigungsschaltflächen.

### TUI, Headless, Import und Zurücksetzen

`DartsHub --tui` → **darts-voice** bzw. **darts-extern** → **Einstellungen bearbeiten**
→ speichern. Dort stehen derselbe Status, Neustart und der Voice-Texttest bereit.
Die Konfiguration von Interpreter und Hostpfaden erfolgt ausschließlich in einer
lokalen GUI/TUI. Netzwerk-GUI, Webapp und mobile App führen diese Hostprogramme
nicht über die neuen Einstellungsendpunkte aus. Laufende Voice-Erkennung ist
auch bei Headless-Betrieb möglich; Extern benötigt weiterhin einen Desktop auf
dem Hub-Rechner.

```powershell
DartsHub --headless --voice-model-path "C:\models\vosk-de" --voice-language 2 --voice-enabled true
DartsHub --tui --extern-browser-path "C:\Program Files\Google\Chrome\Application\chrome.exe" --extern-platform lidarts --extern-player-name "Mein Spieler"
```

Alle Konfigurationsfelder sind über `--voice-PROPERTY` bzw. `--extern-PROPERTY`
adressierbar; `--voice-keywords` nimmt ein JSON-Objekt mit Listen entgegen.
Startparameter konfigurieren nur einen neu gestarteten Host; bei bereits
laufendem Backend die Modulmenüs verwenden.
Der v1-Import übernimmt Modellpfad, Sprache, Schlüsselwortlisten und unterstützte
Extern-Optionen. Alte Feeder-/Debug-Optionen werden ausdrücklich als nicht
unterstützt gemeldet. Anmeldebenutzer und Passwörter werden ausgeschlossen;
der Spielername muss neu gesetzt werden. Importierte und aus Backups
wiederhergestellte Module bleiben deaktiviert. Teilbackups und Zurücksetzen
unterstützen beide Module; Browserprofile werden dabei nicht exportiert oder gelöscht.

## Setup (English)

The current source adds **darts-voice** and **darts-extern** pages to both GUI and
TUI. Published packages may not include them yet. The backend owns both embedded
workers; no legacy Caller socket or separate Caller process is required.
Install Python packages using the OS-specific commands above and configure that
same interpreter. Windows ARM64 Voice uses x64 Python because upstream Vosk has
no Windows ARM64 wheel; macOS uses Vosk 0.3.44 Universal2. Linux needs PortAudio.
Extern also needs an installed Chromium browser and a desktop session on the Hub
host. Dependencies, speech models and browsers are not downloaded automatically.

For Voice, complete the existing Autodarts device login, select an extracted Vosk
model, language (0 custom only / 1 English / 2 German), optional microphone name
or index, enable and save. Custom phrase lists extend the defaults. The saved
keyword test only parses text; it never executes commands. Examples and Caller
ban lifetime are listed above. Recognition runs offline; microphone loss retries
after five seconds. No audio, recordings or free transcripts enter diagnostics.

For Extern, set Python, a browser executable, platform and your local Autodarts
player name. Sign in interactively to the target platform and Autodarts in the
dedicated browser profile; Hub never exports its device tokens to that browser.
The browser creates a private local practice lobby using the external starting
score and selected board. Visits come from native Hub events. Only the selected
board's matching human player is relayed, after takeout or immediately on a win.
Corrections before takeout are respected; winning visits are not sent twice.
Lidarts X01 wins remain filled for manual confirmation, matching the predecessor.

Supported: X01 on Lidarts, Nakka and Dartboards; Cricket on Lidarts only.
Webcamdarts was not enabled in the supplied predecessor. Browser selectors depend
on third-party page structures: local HTML tests do not verify live platform
games. An ambiguous submission is never retried; check scores before restarting.
Optional Lidarts chat messages and Jitsi camera fullscreen are supported.
Dart-dialog preferences are retained separately; Dartboards has no implemented
dialog-confirmation selectors, as in the predecessor.

Terminal equivalents: `DartsHub --tui` → module → **Edit settings**, save,
**Restart with saved settings**, or **Test saved keywords**. Headless startup
accepts every field via `--voice-PROPERTY` / `--extern-PROPERTY`; host program
configuration requires the local native GUI/TUI. Network GUI, web and mobile
clients cannot use these new endpoints to configure host interpreters.
Legacy imports preserve supported values, explicitly report unsupported options,
exclude login credentials and keep workers disabled. Restored backups also keep
workers disabled. Models, executables and browser profiles are excluded from
backups. Module reset preserves the browser profile.

Dependency references: [Vosk wheels](https://pypi.org/project/vosk/0.3.44/#files),
[Vosk 0.3.45](https://pypi.org/project/vosk/0.3.45/#files),
[Playwright wheels](https://pypi.org/project/playwright/1.56.0/#files).


## Oberfläche / Interface

Die GUI verwendet denselben Modulkopf und dieselben kompakten Einstellkarten wie
Caller. Aktivierung und Speichern stehen oben. Verbindung und Voraussetzungen
finden sich unter Einstellungen; eigene Wörter bzw. Plattformoptionen in einem
eigenen Reiter. Der Voice-Texttest hat einen separaten Reiter. Feldhilfen sind am
Fragezeichen erreichbar; Zahlen verwenden Zahlenfelder und Pfade bieten eine
Datei-/Ordnerauswahl. Die TUI bearbeitet dieselben Werte über Einstellungen
bearbeiten und die verschachtelte Schlüsselwortliste; Pfade werden dort als Text
angegeben. Reiterwechsel verändert keine gespeicherten Werte.

The GUI uses the same module header and compact setting cards as Caller. Enable
and save actions stay at the top. Settings contains connection fields and
expandable prerequisites; custom keywords/platform options and the Voice text
test have separate tabs. Field help is available at the question mark; numbers
use numeric controls and paths offer file/folder selection. The TUI edits the
same values through Edit settings and the nested keyword list, with paths entered
as text. Switching tabs does not change persisted values.
