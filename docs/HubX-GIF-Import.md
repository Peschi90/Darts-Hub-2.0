# HubX GIF import

## Deutsch
Einzelne GIF-Beiträge werden im HubX-Posteingang bestätigt. Wähle den AWTRIX-NG-Controller, auf den das GIF geladen werden soll. Bei gleichen Dateinamen zeigt Darts-Hub beide Bilder; du kannst überschreiben, umbenennen oder abbrechen. Die vorhandenen Gerätezugänge werden verwendet. Große GIFs werden nur mit deiner ausdrücklichen Zustimmung verkleinert. Das GIF ist danach als Icon für AWTRIX-Ereignisse auswählbar; eine Ereignisregel wird beim Upload nicht angelegt. GIF-Ereignispakete bleiben dem lokalen GIF-Modul zugeordnet.

GUI: Dashboard → HubX → Posteingang. Terminal: HubX-Posteingang öffnen, Übernehmen, Zielgerät wählen, optional Größenanpassung erlauben und Namenskonflikte auflösen. Lokale Weboberfläche und gekoppelte Webapp bieten denselben Ablauf. Auch heruntergeladene HubX-Paketdateien benutzen diese Prüfung.

## English
Confirm standalone GIF contributions in the HubX inbox and choose the AWTRIX NG controller to receive them. Matching filenames show a comparison with overwrite, rename and cancel actions. Stored device credentials are used. Oversized GIFs are resized only with explicit consent. The uploaded GIF is available as an AWTRIX event icon; uploading does not create an event rule. GIF event packages still belong to the local GIF module.

GUI: Dashboard → HubX → Inbox. Terminal: open the HubX inbox, accept, select the target device, optionally allow resizing and resolve filename conflicts. Local web UI, paired webapp and downloaded HubX package files use the same review and validation.

No legacy v1 configuration contract or HubX package schema changed. Upload destinations are derived from the existing standalone GIF kind.
