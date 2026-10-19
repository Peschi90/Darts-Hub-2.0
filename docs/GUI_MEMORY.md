# GUI-Speichernutzung / GUI memory use

## Deutsch

Die GUI baut nur die gerade benötigten Seiten auf. Beim Seitenwechsel werden deren Bedienelemente freigegeben; Einstellungen und ungespeicherte Eingaben bleiben im gemeinsamen Datenmodell. Die vorhandene Nachfrage zum Speichern oder Verwerfen gilt weiterhin. Beim Zurückkehren wird der ausgewählte Reiter wiederhergestellt.

Die Details zugeklappter Ereigniskarten werden nicht aufgebaut. AWTRIX- und PixelIt-Matrixvorschauen werden erst berechnet, wenn die Vorschau sichtbar im Ausschnitt liegt. Zuklappen, Wegscrollen oder Verlassen gibt die vorberechneten Vorschau-Bilder frei. Zurückkehren erstellt die Vorschau aus den aktuellen Eingaben neu.

Dies betrifft nur die grafische Bearbeitung. Gespeicherte Einstellungen, Geräteeffekte, Timing, Lizenzprüfung und Importformate ändern sich nicht. Die TUI (`--tui`) und der Headless-Modus (`--headless`) bleiben vollständig nutzbar; dort ist keine zusätzliche Einstellung nötig. Der vom Betriebssystem angezeigte Prozessspeicher muss nach dem Freigeben nicht sofort sinken. Eine feste Einsparung ist vom Umfang der Ereignisse und Medien abhängig.

## English

The GUI builds only the pages currently needed. Leaving a page releases its controls; settings and unsaved edits remain in the shared model. The existing save/discard prompt still applies. Returning restores the selected tab.

Collapsed event cards do not build their detailed editors. AWTRIX and PixelIt matrix previews are computed only while visible within the viewport. Collapsing, scrolling away or leaving releases their prepared preview frames. Returning rebuilds the preview using the latest edits.

This affects graphical editing only. Persisted settings, device effects, timing, licensing and import formats are unchanged. The TUI (`--tui`) and headless mode (`--headless`) remain fully available without any extra setting. Process memory reported by the operating system may not fall immediately after release. Savings depend on the number of events and their media.
