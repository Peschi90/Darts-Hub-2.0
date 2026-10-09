# HTTPS für Darts-Hub / HTTPS for Darts-Hub

## Gemeinsame Online-Webapp

**webapp.darts-hub.de** bleibt auf dem zentralen Server. Jeder Browser wird per Code mit seiner eigenen Darts-Hub-Installation gekoppelt. Die Domain wird nicht auf lokale IP-Adressen weitergeleitet.

GUI: **Einstellungen → Weboberfläche → Online-Webapp**. TUI: **Allgemein → Online-Webapp**. Im lokalen Browser: **Einstellungen → Online-Webapp**.

1. Verbindung aktivieren, Installationsnamen vergeben und speichern. Standardmäßig ist sie ausgeschaltet; sie wird ohne Neustart aktiv.
2. **Kopplungscode erzeugen**, `https://webapp.darts-hub.de/` am Handy öffnen und den Code eingeben. Er gilt zehn Minuten und nur einmal. Weitere Browser brauchen neue Codes.
3. Die Oberfläche zeigt nun diese Installation. **Audio hier aktivieren** im Dashboard einschalten und die angebotene Webapp-Installation verwenden. iOS: Safari → **Teilen → Zum Home-Bildschirm**. Die Kopplung wird beim ersten App-Start automatisch übernommen, auch bei getrenntem Cookiespeicher. Die App innerhalb von 24 Stunden nach der Installation erstmals öffnen; abgelaufene oder widerrufene Kopplungen erfordern einen neuen Code.
4. **Browser entkoppeln** trennt diesen Browser. Die Verbindung lokal ausschalten stoppt die Vermittlung und widerruft bei erreichbarem Server alle Kopplungen dieser Installation.

Handy und Host benötigen Internetzugang. Der Host verbindet sich ausgehend; Router-Portfreigaben, lokales DNS und Zertifikate am Handy sind dafür nicht erforderlich. Einstellungen und Caller-Audio bleiben pro Installation getrennt. Der direkte lokale Zugriff bleibt verfügbar.

Internetlatenz kann Start und Unterbrechung einzelner Caller-Ansagen verzögern. Die Webapp garantiert keine Wiedergabe bei gesperrtem Bildschirm. Für direkten Zugriff ohne Vermittler dient die lokale HTTPS-Alternative unten.

Der Serverbetreiber muss zuerst `webapp-public/`, Datenbank und `.env` gemäß `docs/WEBAPP-PLESK.md` im Serverrepository `support.darts-hub` einrichten. Die Supportdomain bleibt auf `public/`. Erst danach ist die öffentliche Domain nutzbar.

GUI/TUI/lokaler Browser teilen `GET/POST /api/v1/web/relay` und `POST /api/v1/web/relay/pair`. Einstellungen und geschützte Kopplungsdaten liegen unter `<DartsHub-Datenordner>/web-relay/`. Der alte JSON-Import verändert diese installationsbezogenen Daten nicht. Der Vermittler kann keine lokalen Authentifizierungstokens ausgeben oder seine eigene Kopplung über eine vermittelte Anfrage ändern.

## Lokales Zertifikat

GUI: **Einstellungen → Weboberfläche**. TUI: **Allgemein → HTTPS und Webapp**. Browser: **Einstellungen → HTTPS und Webapp**.

1. **Lokales Zertifikat** wählen. Die erkannte LAN-IP übernehmen oder passende IP-Adressen/Hostnamen mit Komma eingeben. Bei mehreren Netzwerkkarten die Adresse wählen, die das Handy erreicht.
2. HTTPS-Port festlegen (Standard **8443**), speichern und Darts-Hub neu starten. Eingehende Verbindungen im Heimnetz auf diesem Port erlauben.
3. Das Stammzertifikat exportieren. Die GUI schreibt `dartshub-root-ca.cer` in Downloads und meldet den Pfad. Die TUI fragt nach einem Zielpfad. Im Browser erscheint nach erneutem Öffnen der Einstellungsseite ein Download-Link.
4. Auf jedem Handy das Stammzertifikat installieren und ihm vertrauen. iOS: Profil installieren, danach unter **Allgemein → Info → Zertifikatsvertrauenseinstellungen** volles Vertrauen aktivieren. Android: in den Sicherheitseinstellungen als **CA-Zertifikat** installieren; Herstellerbezeichnungen variieren.
5. Die angezeigte Adresse, etwa `https://192.168.1.20:8443/`, ohne Zertifikatswarnung öffnen und die Webapp installieren.

Die Zertifizierungsstelle ist pro Installation individuell. Nur das öffentliche Stammzertifikat exportieren; ihr privater Schlüssel bleibt auf dem Host. Bei IP-Änderungen Adressen aktualisieren, speichern und neu starten. Mit demselben Datenordner bleibt die Zertifizierungsstelle erhalten. Das Serverzertifikat gilt ein Jahr, das Stammzertifikat zehn Jahre. Erneutes Speichern im lokalen Modus erneuert das Serverzertifikat. Vor Ablauf erneuern; eine automatische Erneuerung ist derzeit nicht eingerichtet.

## Betrieb und Schnittstellen

HTTP bleibt für Einrichtung und native API-Clients erreichbar. HTTPS nutzt einen zusätzlichen Port. Alle Oberflächen zeigen die konfigurierte URL und einen Neustarthinweis; Änderungen werden erst nach Neustart aktiv. Die bisherige HTTP-Webadresse bleibt zur Korrektur falscher HTTPS-Einstellungen nutzbar.

GUI/TUI/Browser verwenden dieselben authentifizierten Endpunkte: `GET/POST /api/v1/web/https`, `GET /api/v1/web/https/root-certificate`. Konfiguration und Zertifikate liegen unter `<DartsHub-Datenordner>/web-https/`. Sie werden nicht durch den alten JSON-Import geändert. Private Schlüssel werden nicht in API-Antworten oder Konfigurationsexporten ausgegeben. Alle unterstützten Desktop-Systeme und Architekturen verwenden dieselbe .NET-Implementierung.

Die Installation garantiert weiterhin keine Caller-Hintergrundwiedergabe.

## English

For the shared **https://webapp.darts-hub.de/** service, enable **Online web app** in GUI Web settings, TUI General or the local browser settings, save a device name and generate a pairing code. Enter it on the phone; it lasts ten minutes and is single-use. Each browser pairs with its own installation. Install from the Android offer or Safari's **Share → Add to Home Screen** on iOS; pairing transfers automatically even with separate cookie storage. First launch must occur within 24 hours; expired or revoked pairings require a new code. Enable dashboard audio on that device. Saving enables the connection without restarting.

Both devices need internet. The host connects outbound; users need no router forwarding, local DNS changes or phone certificates. Disabling stops forwarding and revokes all its pairings when the server is reachable. Unpairing affects only that browser. Internet latency may delay playback and cancellation; installation does not guarantee locked-screen playback. Direct local HTTPS remains an alternative. The server operator must deploy the companion server project's `webapp-public/` following `docs/WEBAPP-PLESK.md` before the domain is usable.

Configure **HTTPS and web app** from GUI application settings, the TUI general page or browser settings. For **Local certificate**, choose the host's reachable LAN addresses, save, restart, export the root certificate and trust it on each phone. GUI exports to Downloads; TUI asks for a destination; browser offers a download after refreshing settings. On iOS install the profile and enable full trust in **General → About → Certificate Trust Settings**. On Android install as a CA certificate in security settings. Open the displayed HTTPS address without certificate warnings, then install the web app.

The local authority is unique to the installation. Updating addresses retains the authority. Server certificates last one year; the root lasts ten years. Saving again renews the server certificate; automatic renewal is not implemented.

HTTP remains available for setup and native clients. GUI/TUI/browser share authenticated HTTPS settings endpoints. The host configuration is preserved independently of legacy JSON import. Private keys are not returned by the API. All supported desktop platforms use the same implementation. Webapp installation does not guarantee background Caller playback.

## Nicht erreichbare Installation / Unreachable installation

Eine gekoppelte Online-Webapp zeigt auf Deutsch oder Englisch eine deutliche Meldung, wenn Darts-Hub offline ist. Darts-Hub auf dem gekoppelten Rechner starten und geöffnet lassen; Internetverbindung und aktivierte Online-Webapp prüfen. Ein neuer Code ist nicht erforderlich. Bei einem Netzwerk- oder Serverfehler wird stattdessen die Internetverbindung des Browsers angesprochen. Die Verbindung wird automatisch erneut geprüft. Beim Wiederverbinden verschwindet die Meldung; eine zuvor nicht geladene Oberfläche wird erneut geladen.

A paired online web app displays a prominent German or English message when Darts-Hub is offline. Start and keep Darts-Hub open on the paired computer; check internet access and that the online web app is enabled. No new code is needed. Network/server failures show a separate internet-connection message. Reconnection is automatic and retries initial UI loading when needed.

GUI: Einstellungen → Weboberfläche → Online-Webapp. Terminal equivalent: TUI → Allgemein → Online-Webapp; check the existing connection status there.

## Kopplung per QR-Code / QR pairing

Nach **Kopplungscode erzeugen** den QR-Code mit der Smartphone-Kamera scannen. Die Webapp öffnet sich und koppelt das Gerät automatisch. Der Code gilt zehn Minuten und einmalig; bei Ablauf oder erneuter Kopplung einen neuen erzeugen. GUI und lokale Weboberfläche zeigen eine QR-Grafik, die TUI unter **Allgemein → Online-Webapp → Kopplungscode erzeugen** eine Textgrafik mit Link. Den QR-Code oder Link nur für das eigene Gerät verwenden; er gewährt Zugriff auf die Installation. Manuelle Codeeingabe bleibt möglich.

After **Generate pairing code**, scan the QR with your phone camera to open the web app and pair automatically. The code is single-use and expires after ten minutes. GUI and local web settings display an image; TUI **General → Online web app → Generate pairing code** displays a terminal QR and link. Keep it private: it grants access to your installation. Manual entry remains available.
