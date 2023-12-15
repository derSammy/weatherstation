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
InfluxDB
https://pimylifeup.com/raspberry-pi-influxdb/

(8)
SSH-Verbindung auf Raspberry einrichten, um komfortabler auf ihm entwickeln zu können
- SSH über Settings aktiviert
- IP-Adresse des PI herausfinden (Fritz oder hostname -I auf dem PI)
- ssh username@IP-ADRESS, Passwort wird erfragt, das wars. :)
- ssh -Y username@IP-ADRESS, dann wird auch der X-Server durchgereicht, also z.B. mit "thonny" kann man den Editor auf dem PI aufmachen
- davor hatte ich sudo apt-get install tightvncserver // tightvncserver // vncserver :1 -geometry 1920x1080 -depth 24 ausgeführt, aber denke darauf sollte es nicht ankommen.
Vgl. auch hier:
https://www.heise.de/tipps-tricks/Raspberry-Pi-SSH-einrichten-so-geht-s-4190645.html


(9)
MQTT-Broker?
+ 

(10)
Anzeige-App https://kivy.org/
https://buildmedia.readthedocs.org/media/pdf/kivy/latest/kivy.pdf

Kivy-Framework:
- sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
- sudo apt-get install libmtdev1
beides habe ich ausgespart; weil die Kivy-Doku von diesem Weg abzuraten scheint:
https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip
python -m pip install "kivy[base]" kivy_examples
das habe ich aber ausgeführt, bzw. auch in die requirements.txt aufgenommen
Zusätzlich habe ich noch die sdl-Dependencies handisch installiert. Dazu zuerst:
sudo apt-get install cmake
und dann wie hier beschrieben:
https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip


(10a) System-Optimierungen
https://www.haraldkreuzer.net/aktuelles/bauanleitung-raspberry-pi-wetterstation-mit-wettervorhersage-und-esp32-funksensoren

(10b) Python-Umgebung mit System-Start aktivieren.

(10c) Projekt Dockerisieren

(11)
Backup-Strategie

(12)
PWM-Luefter-Steuerung
https://www.raspberry-pi-geek.de/ausgaben/rpg/2022/08/temperaturabhaengige-lueftersteuerung-per-pwm/


Megacooles ähnliches Projekt:
+  https://www.haraldkreuzer.net/aktuelles/bauanleitung-raspberry-pi-wetterstation-mit-wettervorhersage-und-esp32-funksensoren
+  und auf Github: https://github.com/HarryVienna/WeatherStation-Raspberry-Pi-base-station

