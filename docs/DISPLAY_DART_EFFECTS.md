# DMU und CMB / DMU and CMB

PixelIt, Awtrix und GIF unterstützen dieselben Feld-/Ring-Bedingungen wie WLED.
In der GUI eine Ereignisregel hinzufügen, **Dart-Feld**, **Multiplikator** oder
**Drei-Dart-Kombination** auswählen und die Bedingung unter dem Ereignis einstellen.
Anschließend die gewünschten Templates/Schritte beziehungsweise GIF-Bilder wählen und speichern.

- Feld: 0 = Fehlwurf, 1–20, 25 = Bull; Ring 0 = beliebig, 1 = Single, 2 = Double, 3 = Triple.
- Multiplikator: 1, 2 oder 3, unabhängig vom Feld; Fehlwürfe zählen nicht.
- Kombination: drei Felder, etwa `s20,d20,t20`; Reihenfolge egal, einmal pro Aufnahme,
  nicht bei Bust. Wiederholte Statusmeldungen und historische Aufnahmen beim Verbinden werden nicht abgespielt.

TUI: Erweiterung → Ereignisregel → Ereignis auswählen → Bedingungszeile öffnen.
Feld/Ring wird als `20|3`, der Multiplikator als `3`, die Kombination als `t20,t20,t20` eingegeben.
Die gleichen API-Validatoren prüfen GUI, TUI, Import und Headless-Konfiguration.

Headless / Import (Windows, Linux, macOS):
```
--pixelit-DMU "t20=templates/points" "double=templates/fire"
--pixelit-CMB "t20,t20,t20=templates/fire"
--awtrix-DMU "t20=throw" "double=throw"
--awtrix-CMB "t20,t20,t20=score180"
--gif-DMU "t20=triple.gif|3"
--gif-CMB "t20,t20,t20=180.gif|5"
```
Auch `dart_multiplier_effects` und `combo_effects` (bei GIF `*_images`) werden im Legacy-Import
berücksichtigt. `e:`-Ziele behalten die bestehenden Gerätezuordnungen. WLED-Presets sind
controllergebunden und werden nicht automatisch in Bilder oder Display-Templates umgewandelt.

English: Add an event rule in GUI or TUI and select **Dart field**, **Multiplier** or
**Three-dart combination**. Choose the condition and display steps/images, then save.
Field/ring is entered as `20|3` in TUI, multiplier as `3`, combo as `t20,t20,t20`.
Combos match regardless of order and run once per visit, excluding busts and historic
visits on connection. The examples above work on all supported operating systems.
