# Ereignisse sortieren / Reordering events

WLED, PixelIt und Awtrix: In den Erweiterungseinstellungen den Griff links an einer Ereigniskarte auf eine andere Karte ziehen. Die markierte Ober-/Unterkante zeigt die Einfügeposition. Kopfzeilen öffnen und schließen die Details. Mit fokussiertem Griff verschieben Pfeil hoch/runter das Ereignis. Die Reihenfolge mit **Speichern** übernehmen; Suche und Filter verändern die übrigen Ereignisse nicht.

TUI: Bei PixelIt/Awtrix ein Ereignis öffnen und **Nach oben verschieben** oder **Nach unten verschieben** wählen. Bei WLED im Einstellungseditor die Liste **Rules** öffnen, ein Ereignis markieren und dieselben Aktionen wählen. Anschließend speichern. GUI und TUI verwenden dieselbe gespeicherte Reihenfolge.

In the extension settings, drag an event's left grip onto another card. The highlighted top/bottom edge indicates the insertion position. Headers expand/collapse details. A focused grip supports the Up/Down arrows. **Save** the new order; searching and filtering preserve other events.

TUI: Open a PixelIt/Awtrix event and choose **Move up** or **Move down**. In the WLED settings editor, open **Rules**, select an event and use those actions. Save afterwards. Both frontends use the same persisted order.

The existing rule array stores the order; IDs, settings and step sequences stay attached to their event. No new legacy-import parameter is required. The order can also determine the execution order of rules matching the same event.
