# WLED: Geräte und Spielregeln / Devices and game rules

## Deutsch

1. Autodarts verbinden und das gewünschte Board auswählen; der Caller ist nicht nötig.
   Die Seite **WLED** öffnen und das Modul aktivieren.
2. Geräte mit Namen und Adresse hinzufügen und aktivieren.
   Bei unabhängig gesteuerten Controllern die WLED-UDP-Synchronisation deaktivieren.
3. Vor der Effektauswahl das Gerät manuell laden bzw. **Verbindung prüfen** wählen.
   Nach Änderungen in WLED den Effekt-, Paletten- und Preset-Katalog erneut laden.
4. Eine Regel anlegen: Auslöser, optional Spieler, Zielgeräte und Effekt oder Preset wählen.
   Für Spielregeln bedeutet Dauer **0**: bis zum Herausziehen der Darts (Takeout).
5. Mit **Test** den aktuellen Entwurf auf echten Geräten ausprobieren, ohne ihn zu speichern.
   Anschließend **Speichern** wählen, damit die Regeln für Spiele dauerhaft übernommen werden.

**Hinweise**
- Kataloge werden beim Start oder manuell geladen, nicht regelmäßig automatisch aktualisiert.
- Ein Test bleibt bis zum nächsten Controllerkommando sichtbar; keine automatische Rückkehr zur vorherigen Anzeige.
- Werden die gewählten Ziele gelöscht, wird die Regel deaktiviert; vor dem Aktivieren neue Ziele wählen.
- Manche erweiterten Regeln benötigen eine Lizenz.

## English

1. Connect Autodarts and select the intended board; Caller is not required.
   Open **WLED** and enable the module.
2. Add devices with names and addresses and enable them.
   Disable WLED UDP synchronisation on independently controlled controllers.
3. Manually load the device or choose **Test connection** before selecting effects.
   Reload the effect, palette and preset catalogue after changes in WLED.
4. Add a rule: select a trigger, optional player, target devices and an effect or preset.
   For game rules, duration **0** means until the darts are pulled (takeout).
5. Use **Test** to try the current draft on real devices without saving it.
   Then choose **Save** to persist and apply the rules for games.

**Notes**
- Catalogues load at startup or manually, not through regular automatic refreshes.
- A test remains visible until the next controller command; it does not automatically restore the previous display.
- Deleting the selected targets disables the rule; choose new targets before enabling it again.
- Some advanced rules require a licence.
