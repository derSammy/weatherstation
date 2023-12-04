Was ist alles zu tun?

(1) Projektsetup
+ Github-Einrichtung mittels SSH

(2) Display
+ über HDMI auf Raspberry PI4 geschenkt
+ Auflösung 1024 x 600

(3) Sensoren
+ BME280 laufen über I2C, zwei verschiedene Sensoren lassen sich über Pin-Induzierte Adressänderung realisieren
! vom sechspoligen Kabel zum Sensor werden dabei verwendet zwingend benötigt:
VCC, GND, SCL, SDA, zwei Leitungen sind noch frei
+ Formel zur Höhenkalibration umgesetzt

(4)
Anbindung der Abfahrtsanzeige der DVB
+ DVB-Monitor angebunden

(5)
Anbindung von Wetter-API(s)
+ OpenWeatherAPI angebunden
  https://rapidapi.com/blog/openweathermap-api-overview/python/
  https://www.instructables.com/Get-Weather-Data-Using-Python-and-Openweather-API/

(6)
Anbindung von Regenradar, etc.

(7)
Datenbank aufsetzen, wo die Sensordaten landen

(8)
SSH-Verbindung auf Raspberry einrichten, um komfortabler auf ihm entwickeln zu können
- SSH über Settings aktiviert
- IP-Adresse des PI herausfinden (Fritz oder hostname -I auf dem PI)
- ssh username@IP-ADRESS, Passwort wird erfragt, das wars. :)
- ssh -Y username@IP-ADRESS, dann wird auch der X-Server durchgereicht, also z.B. mit "thonny" kann man den Editor auf dem PI aufmachen
- davor hatte ich sudo apt-get install tightvncserver // tightvncserver // vncserver :1 -geometry 1920x1080 -depth 24 ausgeführt, aber denke darauf sollte es nicht ankommen.


(9)
MQTT-Broker?
+ 

(10)
Anzeige-App https://kivy.org/
https://buildmedia.readthedocs.org/media/pdf/kivy/latest/kivy.pdf


(11)
Backup-Strategie

(12)
PWM-Luefter-Steuerung
https://www.raspberry-pi-geek.de/ausgaben/rpg/2022/08/temperaturabhaengige-lueftersteuerung-per-pwm/


Megacooles ähnliches Projekt:
+  https://www.haraldkreuzer.net/aktuelles/bauanleitung-raspberry-pi-wetterstation-mit-wettervorhersage-und-esp32-funksensoren
+  und auf Github: https://github.com/HarryVienna/WeatherStation-Raspberry-Pi-base-station

