# AWTRIX NG: GIFs und Icons verwalten

GUI: AWTRIX → Geräte → Gerätekarte → „GIFs und Icons verwalten“. Ein eigener Dialog zeigt die Dateien links und die Matrixvorschau rechts. Oben eine neue Datei hochladen; eine ausgewählte Datei rechts ansehen oder löschen. Diese Funktionen sind auch für ein neu hinzugefügtes oder deaktiviertes Gerät verfügbar. Adresse und gegebenenfalls Benutzername/Passwort müssen stimmen. Gespeicherte Passwörter werden automatisch verwendet.

„Icons vom Controller laden“ zeigt vorhandene GIFs/JPEGs und die gesamte Speicherbelegung des Controllers. „GIF / JPEG hochladen“ wählt eine lokale Datei bis 4 MiB; der Dateiname ohne Endung wird zur Icon-ID. Der Name darf keine Pfade, Steuerzeichen oder `..` enthalten. PNG wird nicht unterstützt. Ersetzen eines vorhandenen Namens muss ausdrücklich bestätigt werden. Hochladen und Löschen wirken sofort auf den Controller, unabhängig vom Speichern der Moduleinstellungen.

Zum Löschen ein Icon auswählen, „Löschen“ anklicken und den Dialog mit dem konkreten Dateinamen bestätigen. Beim Hochladen einer vorhandenen Icon-ID wird direkt nach dem Ersetzen gefragt; zusätzliche Bestätigungshäkchen sind nicht nötig. Bestehende Ereignisregeln behalten ihre Icon-ID; ein gelöschtes Icon wird dann nicht mehr angezeigt. Die ursprüngliche lokale Datei bleibt erhalten.

Unter Ereignisse → Anzeigeschritt → Icon zeigt die Auswahlliste die IDs, die auf allen Zielgeräten vorhanden sind. Groß- und Kleinschreibung bleibt erhalten. Nach Änderungen auf einem anderen Gerät die Listen erneut laden. Eine eigene ID kann weiterhin eingegeben werden; fehlende oder offline befindliche Controller verhindern weder das Bearbeiten noch das Speichern bestehender Regeln. Nach einem Neustart werden die Listen beim Öffnen der AWTRIX-Seite neu geladen.

TUI: AWTRIX → Gerätename · GIFs und Icons → Vorhandene Icons anzeigen / GIF-JPEG hochladen / ausgewähltes Icon löschen. Ereignisregel → Anzeigeschritt → weitere Optionen → Icon lädt die Listen der Zielgeräte und bietet eine Auswahl oder manuelle Eingabe. Im Webinterface öffnet „GIFs und Icons verwalten“ ebenfalls einen Dialog aus der jeweiligen Gerätekarte.

Die Funktionen verwenden die AWTRIX-NG-Dateischnittstelle unter `/api/v1/files` mit dem Ordner `/ICONS`. Andere Ordner und Firmware werden durch diese Verwaltung nicht verändert. Referenz: https://blueforcer.github.io/awtrix-ng/tc002/reference/http/#files

## Animierte Matrixvorschau

GUI: Icon in der Gerätekarte auswählen → Matrixvorschau. Im Webinterface ist dieselbe Aktion neben der Icon-Auswahl verfügbar. TUI: Gerätename · GIFs und Icons → Matrixvorschau → Datei auswählen; das Fenster zeigt eine Animation mit farbigen LED-Zeichen.

Die Datei wird mit dem konfigurierten Gerätezugang direkt aus `/ICONS` geladen. Die Vorschau verändert die Anzeige des Controllers nicht. GIFs werden mit ihren Bildzeiten animiert, JPEGs bleiben statisch. Die Darstellung zeigt eine 32×8-Matrix; kleine Bilder bleiben in Originalgröße und werden zentriert, größere werden proportional mit pixelgenauer Skalierung passend verkleinert. Die Originalgröße steht darüber. Effekte, Helligkeit und Farbkalibrierung der tatsächlichen Hardware werden nicht simuliert.

Die Vorschau lädt nur auf Wunsch und hält nur die aktuell ausgewählte Animation vor. Ein Wechsel der Icon-Auswahl entfernt sie; beim Verlassen der Anzeige stoppt die Animation. Datei maximal 4 MiB, Bild maximal 1024×1024 und 262144 Pixel, Animation maximal 600 Bilder. Die Bilder werden für alle Oberflächen mit demselben betriebssystemunabhängigen Decoder verarbeitet. Es gibt keine neuen Moduleinstellungen oder Änderungen am Altimport.

Uploads werden nach dem Speichern vom Controller zurückgelesen und mit dem Original verglichen. Bei Abweichungen wird ein Fehler angezeigt; die Datei muss erneut hochgeladen werden. Dies gilt für GUI, TUI und Weboberfläche.

Gerätezugang: Benutzername und Passwort mit den Moduleinstellungen speichern. GUI, TUI und Weboberfläche zeigen an, ob ein Passwort gespeichert ist. Das Passwortfeld bleibt beim Laden leer und behält das verschlüsselt gespeicherte Passwort bei. In der TUI behält „Gespeichertes Passwort behalten“ den Zugang; zum Entfernen ausdrücklich die Löschoption wählen und speichern.

GIFs müssen zur tatsächlichen Matrixgröße passen (zum Beispiel maximal 32×8 bei einer 32×8-Matrix). Die verkleinerte lokale Vorschau ändert die Originaldatei nicht. Upload und Sequenztest prüfen die Größe anhand der Controllerangaben und melden zu große GIFs in GUI, TUI und Weboberfläche. Beim Upload bietet ein Dialog die proportionale Verkleinerung an und zeigt Original- und Zielauflösung. Kleine Details und Texte können verloren gehen. Nur nach Bestätigung wird die verkleinerte Animation hochgeladen; die lokale Originaldatei bleibt unverändert. Animation, Transparenz und Bildzeiten bleiben erhalten. Der Ablauf ist in GUI, TUI und Weboberfläche verfügbar.

Im Verwaltungsdialog startet die Matrixvorschau direkt bei der Dateiauswahl. Der Vorschauknopf dient zum erneuten Laden. API: `POST /api/v1/awtrix/icons/upload-plan` mit derselben Datei liefert die Zielgröße; `ResizeToFit: true` beim Upload bestätigt die Verkleinerung. Diese Bestätigung wird nicht in Moduleinstellungen gespeichert und ändert den Altimport nicht.
