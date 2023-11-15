Was ist alles zu tun?

(1) Projektsetup
+ Github-Einrichtung mittels SSH

(2) Display
+ über HDMI auf Raspberry PI4 geschenkt

(3) Sensoren
+ BME280 laufen über I2C, zwei verschiedene Sensoren lassen sich über Pin-Induzierte Adressänderung realisieren
! vom sechspoligen Kabel zum Sensor werden dabei verwendet zwingend benötigt:
VCC, GND, SCL, SDA, zwei Leitungen sind noch frei
+ Formel zur Höhenkalibration umgesetzt

(4)
Anbindung der Abfahrtsanzeige der DVB


(5)
Anbindung von Wetter-API(s)

(6)
Anbindung von Regenradar, etc.

(7)
Datenbank aufsetzen, wo die Sensordaten landen

(8)
SSH-Verbindung auf Raspberry einrichten, um komfortabler auf ihm entwickeln zu können
- SSH über Settings aktiviert
- IP-Adresse des PI herausfinden (Fritz oder hostname -I auf dem PI)
- ssh username@IP-ADRESS, Passwort wird erfragt, das wars. :)


(9)
MQTT-Broker?

(10)
Backup-Strategie
