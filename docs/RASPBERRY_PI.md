# Raspberry Pi OS / Linux-Audio

## Deutsch

Verwende **Raspberry Pi OS 64 Bit** und das Paket **linux-arm64**. Dafür ist kein eigener Pi-Build nötig. Die aktuellen Releases enthalten kein 32-Bit-ARM-Paket. Der Installer prüft Kernelarchitektur und Benutzerbereich getrennt; `uname -m` alleine reicht nicht, da ein 64-Bit-Kernel auch mit einem 32-Bit-System betrieben werden kann.

```sh
uname -m
getconf LONG_BIT
```

Typisch für die passende Installation: `aarch64` und `64`. Die Anwendung zeigt unter System die Betriebssystem- und Prozessarchitektur separat an, statt 64 Bit pauschal als x64 zu bezeichnen.

Die ältere Meldung **No native audio backend ... caller audio will be skipped** bedeutete, dass noch kein Linux-Audioplayer implementiert war. DartsHub erkennt beim Start `ffplay`, `paplay` und `aplay` und wählt pro Datei einen geeigneten Player. `ffplay` spielt WAV und MP3; `paplay` und `aplay` werden für WAV genutzt. Ist ein geeigneter Player vorhanden, ist keine weitere Installation erforderlich. `aplay` nutzt die Systemlautstärke; Stummschalten funktioniert auch im Caller. Fehlt ein passender Player, empfiehlt sich FFmpeg. Auf Raspberry Pi OS / Debian:

```sh
sudo apt update
sudo apt install ffmpeg
ffplay -nodisp -autoexit /pfad/zu/einem/sound.wav
```

Danach DartsHub neu starten, Caller und lokale Wiedergabe aktivieren, ein installiertes Soundpack auswählen und testen. Wähle im Betriebssystem den gewünschten Audioausgang, beispielsweise HDMI oder USB. Die Caller-Lautstärke und die Systemlautstärke müssen hörbar eingestellt sein.

Wenn der manuelle `ffplay`-Test bereits keinen Ton erzeugt, prüfe den Audioausgang und die Benutzersitzung. Ein Headless-Dienst muss Zugriff auf die Audioausgabe seines Benutzers haben; ein Dienst vor der Anmeldung besitzt gegebenenfalls noch keine laufende PipeWire-/PulseAudio-Sitzung. Im Caller-Log stehen das gewählte Backend sowie echte Player-Fehler. Linux-TTS ist weiterhin nicht implementiert; die Soundpack-Wiedergabe benötigt kein TTS.

## English

Use **64-bit Raspberry Pi OS** and the **linux-arm64** package. No dedicated Pi build is required; current releases do not include a 32-bit ARM package. Check both `uname -m` and `getconf LONG_BIT`; the expected combination is `aarch64` and `64`. System settings show OS and application architectures separately.

Old releases deliberately skipped Linux caller audio. DartsHub detects `ffplay`, `paplay` and `aplay` at startup and selects a suitable player for each file. FFplay supports WAV/MP3; paplay and aplay are used for WAV. No additional installation is required when a suitable player is available. Aplay uses system volume; Caller mute still works. If no suitable player is installed, install `ffmpeg`, restart DartsHub and enable Caller/local playback with an installed soundpack. Use the commands above to test a WAV/MP3 file independently. Check HDMI/USB output, system volume and audio-session access for headless services. Linux TTS remains unavailable; soundpack playback does not require it.

Player options: [official ffplay documentation](https://ffmpeg.org/ffplay.html).
