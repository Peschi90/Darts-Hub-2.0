# Caller: Stimme und Ansagen / Voice and announcements

## Deutsch

In der Websteuerung öffnet **Herunterladen** einen Fortschrittsdialog. Er zeigt Downloadmenge und Prozentwert getrennt vom Entpacken des Paketarchivs, dem Entpacken der Audiodateien und der Soundzuordnung mit Dateizähler. 100 % beim Download bedeutet nur, dass die Übertragung fertig ist. Beim abschließenden Aufräumen bleibt eine Warteanzeige sichtbar. Nach erfolgreicher Installation aktualisiert sich die Soundpack-Liste automatisch und der Dialog schließt sich. Fehler und Abbrüche bleiben sichtbar. **Schließen** lässt die Installation weiterlaufen; **Fortschritt anzeigen** öffnet den Dialog erneut. **Abbrechen** stoppt den laufenden Download oder die Verarbeitung vor der fertigen Installation. Ungespeicherte Caller-Einstellungen und die Browser-Audiowiedergabe bleiben beim Aktualisieren der Liste erhalten.

Eigene Soundpacks bauen: [vollständige Key-Referenz mit Auslösern, Ersatzsounds und Beispielen](CALLER_SOUNDPACKS.de.md).

1. Für Live-Ansagen Autodarts verbinden und das gewünschte Board auswählen.
   Anschließend die Seite **Caller** öffnen.
2. **Caller aktivieren** einschalten.
   Die Soundpack-Bibliothek aufklappen.
3. Nach Sprache oder Stimme suchen und mit **Anhören** eine Hörprobe abspielen.
   Die gewünschte Stimme **Herunterladen** und danach **Verwenden** wählen.
4. Lautstärke und gewünschte Ansagen einstellen, etwa Scores und Checkout-Hinweise.
   Die Hilfetexte an den Einstellungen erklären die einzelnen Optionen.
5. **Einstellungen übernehmen** wählen, um die Werte zu speichern und live anzuwenden.
   Die gespeicherten Einstellungen bleiben nach einem Neustart erhalten.

**Hinweise**
- TTS (Sprachausgabe als Ersatz) ist optional und standardmäßig aus; fehlende Sounds bleiben sonst stumm.
- Die Sprache der Oberfläche unter **Einstellungen** ist unabhängig von der Stimme und der TTS-Sprache.
- Stimmen ausdrücklich herunterladen; Downloads erfolgen nicht automatisch bei jedem Start.
- Bei Fehlern die [Runtime-Konsole](RUNTIME_CONSOLE.md) öffnen.

## English

In web control, **Download** opens a progress dialog. It shows transferred data and percentage separately from package extraction, audio extraction and sound mapping with file counts. A download at 100% only means the transfer has finished. Final cleanup keeps a waiting indicator visible. After successful installation the soundpack list refreshes automatically and the dialog closes. Errors and cancellations remain visible. **Close** lets installation continue; **Show progress** reopens the dialog. **Cancel** stops the download or processing before installation finishes. Unsaved Caller settings and browser audio playback survive the list refresh.

Build custom soundpacks: [complete key reference with triggers, fallbacks and examples](CALLER_SOUNDPACKS.en.md).

1. Connect Autodarts and select the intended board for live announcements.
   Then open the **Caller** page.
2. Enable **Caller**.
   Expand the soundpack library.
3. Search by language or voice and choose **Preview** to hear a sample.
   **Download** the desired voice, then select **Use**.
4. Set the volume and desired announcements, such as scores and checkout hints.
   The help text beside each setting explains its options.
5. Choose **Apply settings** to save the values and apply them live.
   Saved settings remain available after restarting.

**Notes**
- TTS (spoken fallback) is optional and off by default; missing sounds otherwise remain silent.
- The interface language under **Settings** is independent of the voice and TTS language.
- Download voices explicitly; downloads do not run automatically at every startup.
- For errors, open the [runtime console](RUNTIME_CONSOLE.md).
