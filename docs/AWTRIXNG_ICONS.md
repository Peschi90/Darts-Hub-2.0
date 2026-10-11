# AWTRIX NG: GIFs und Icons verwalten

GUI: AWTRIX → Geräte → Gerätekarte → GIFs und Icons. Diese Funktionen sind auch für ein neu hinzugefügtes oder deaktiviertes Gerät verfügbar. Adresse und gegebenenfalls Benutzername/Passwort müssen stimmen. Gespeicherte Passwörter werden automatisch verwendet.

„Icons vom Controller laden“ zeigt vorhandene GIFs/JPEGs und die gesamte Speicherbelegung des Controllers. „GIF / JPEG hochladen“ wählt eine lokale Datei bis 4 MiB; der Dateiname ohne Endung wird zur Icon-ID. Der Name darf keine Pfade, Steuerzeichen oder `..` enthalten. PNG wird nicht unterstützt. Ersetzen eines vorhandenen Namens muss ausdrücklich bestätigt werden. Hochladen und Löschen wirken sofort auf den Controller, unabhängig vom Speichern der Moduleinstellungen.

Zum Löschen ein Icon auswählen, die Löschbestätigung aktivieren und „Ausgewähltes Icon löschen“ anklicken. Bestehende Ereignisregeln behalten ihre Icon-ID; ein gelöschtes Icon wird dann nicht mehr angezeigt. Die ursprüngliche lokale Datei bleibt erhalten.

Unter Ereignisse → Anzeigeschritt → Icon zeigt die Auswahlliste die IDs, die auf allen Zielgeräten vorhanden sind. Groß- und Kleinschreibung bleibt erhalten. Nach Änderungen auf einem anderen Gerät die Listen erneut laden. Eine eigene ID kann weiterhin eingegeben werden; fehlende oder offline befindliche Controller verhindern weder das Bearbeiten noch das Speichern bestehender Regeln. Nach einem Neustart werden die Listen beim Öffnen der AWTRIX-Seite neu geladen.

TUI: AWTRIX → Gerätename · GIFs und Icons → Vorhandene Icons anzeigen / GIF-JPEG hochladen / ausgewähltes Icon löschen. Ereignisregel → Anzeigeschritt → weitere Optionen → Icon lädt die Listen der Zielgeräte und bietet eine Auswahl oder manuelle Eingabe. Im Webinterface findet sich die Verwaltung ebenfalls in der jeweiligen Gerätekarte.

Die Funktionen verwenden die AWTRIX-NG-Dateischnittstelle unter `/api/v1/files` mit dem Ordner `/ICONS`. Andere Ordner und Firmware werden durch diese Verwaltung nicht verändert. Referenz: https://blueforcer.github.io/awtrix-ng/tc002/reference/http/#files

## Animierte Matrixvorschau

GUI: Icon in der Gerätekarte auswählen → Matrixvorschau. Im Webinterface ist dieselbe Aktion neben der Icon-Auswahl verfügbar. TUI: Gerätename · GIFs und Icons → Matrixvorschau → Datei auswählen; das Fenster zeigt eine Animation mit farbigen LED-Zeichen.

Die Datei wird mit dem konfigurierten Gerätezugang direkt aus `/ICONS` geladen. Die Vorschau verändert die Anzeige des Controllers nicht. GIFs werden mit ihren Bildzeiten animiert, JPEGs bleiben statisch. Die Darstellung zeigt eine 32×8-Matrix; kleine Bilder bleiben in Originalgröße und werden zentriert, größere werden proportional mit pixelgenauer Skalierung passend verkleinert. Die Originalgröße steht darüber. Effekte, Helligkeit und Farbkalibrierung der tatsächlichen Hardware werden nicht simuliert.

Die Vorschau lädt nur auf Wunsch und hält nur die aktuell ausgewählte Animation vor. Ein Wechsel der Icon-Auswahl entfernt sie; beim Verlassen der Anzeige stoppt die Animation. Datei maximal 4 MiB, Bild maximal 1024×1024 und 262144 Pixel, Animation maximal 600 Bilder. Die Bilder werden für alle Oberflächen mit demselben betriebssystemunabhängigen Decoder verarbeitet. Es gibt keine neuen Moduleinstellungen oder Änderungen am Altimport.

Uploads werden nach dem Speichern vom Controller zurückgelesen und mit dem Original verglichen. Bei Abweichungen wird ein Fehler angezeigt; die Datei muss erneut hochgeladen werden. Dies gilt für GUI, TUI und Weboberfläche.
