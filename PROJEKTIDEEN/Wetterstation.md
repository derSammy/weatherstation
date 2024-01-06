Was ist alles zu tun?

(0) Raspian Image...
like here:
https://www.youtube.com/watch?v=1s4sBoDej4g

Imager: 64bit, mit Desktop, SSH via User&PW
normal installiert, mittels GUI, 64bit (recommended), SSH aktiviert
Nutzername&PW werden hier vergeben.

Raspi booten!

(01)
IP-Adresse vom RaspberryPi einrichten
hostname -I -> aktuelle IP-Adresse. Bei mir: 192.168.178.25
In Fritzbox: Haken gesetzt bei "immer die gleiche IPv4-Adresse zuweisen"
vgl. ggf. auch https://www.elektronik-kompendium.de/sites/raspberry-pi/1912151.htm

(02) Raspi über SSH
ssh <UserName>@192.168.178.25
-> Warnung
ssh-keygen -f "/home/<UserName>/.ssh/known_hosts" -R "192.168.178.25"

ssh <UserName>@192.168.178.25
Updates installieren (braucht Passwort vom User, was beim Imaging eingerichtet wurde)
sudo raspi-config
Locale habe ich geändert (de-UTF8), und TimeZone auf Berlin
Advanced Options / Expand Filesystem

sudo apt update
(sudo apt list --upgradeable)
sudo apt upgrade

sudo rpi-update
--> wird abgeraten, dann mache ich das auch nicht

sudo reboot

(02)
Docker-Installation:
sudo apt install curl --> sollte schon drauf sein
curl -fsSL https://get.docker.com -o get-docker.sh
ls -l (Kontrolle, ob geklappt)

sudo groupadd docker (sollte überflüssig sein)
sudo usermod -aG docker $USER

Konsole schließen, neu via SSH aufschalten

docker run hello-world sollte sich das passende Image ziehen und laufen. :)

docker volume create portainer_data

docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce


http://192.168.178.25:9000/
Passwort neu setzen, ist im KeePass

(02A)
Installation über IOT-Stack
https://learnembeddedsystems.co.uk/easy-raspberry-pi-iot-server


(1) Projektsetup
+ Github-Einrichtung mittels SSH
https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
Solange noch Dev-Code auszuchecken ist, müssen wir den Raspi befähigen mit GitHub interagieren zu können.
Vermutlich ist es möglich, dem Raspi direkt einen ssh-Key bei der Image-Erstellung verpassen zu können, dann könnte man den nehmen.
Ich bin den Weg über die Neuerstellung gegangen:

ssh-keygen -t ed25519 -C "your_email@example.com" (via SSH auf dem Pi)

Enter (default-Pfad für die Dateiablage von Public- und Private-Key nutzen)

Passphrase festlegen

eval "$(ssh-agent -s)"
-> man bekommt eine pid, unter welchem Prozess ssh-agent läuft

ssh-add ~/.ssh/id_ed25519
dies fügt diese Datei der ssh-Key-Verwaltung hinzu.

Jetzt muss der Key noch bei Github hinterlegt werden. Dazu hab ich die id_ed25519.pub-Datei geöffnet:
cd /home/samuel/.ssh
nano id_ed25519.pub
-> Inhalt kopieren und bei Github hinterlegen
ssh-ed25519 AAASomeStrangeStringmRH email@provider.de

auf Rasperry:
mkdir WeatherStation
cd WeatherStation



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
- oft benötigte Befehle: thonny (Editor), pcmanfm (File Manger)
- davor hatte ich sudo apt-get install tightvncserver // tightvncserver // vncserver :1 -geometry 1920x1080 -depth 24 ausgeführt, aber denke darauf sollte es nicht ankommen.
Vgl. auch hier:
https://www.heise.de/tipps-tricks/Raspberry-Pi-SSH-einrichten-so-geht-s-4190645.html



(9)
MQTT-Broker?
+ mosquitto scheint die verbreiteste Implementierung. Gibt es auch dockerisiert:
https://hub.docker.com/_/eclipse-mosquitto
Image: eclipse-mosquitto

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
Vitaldaten vom System lassen sich mit dem psutil-Paket auslesen
Siehe auch hier: https://indibit.de/raspberry-pi-cpu-auslastung-als-diagramm-auf-oled-display/
Script läuft
Dockerisierung:
docker build -t "luefter_pwm:v1" .
docker container run --privileged --name pwm_luefter -d luefter_pwm:v1


(13) Heimdall als Application Management System für alles auf dem Raspy nutzen
https://heimdall.site/
https://blog.berrybase.de/docker-auf-dem-raspberry-pi-basics/
docker container run --privileged --name pwm_luefter -d luefter_pwm:v1
... unklar, ob das "privileged" die beste option ist, tut aber mit der GPIO und CPU_temp_Auslesung
noch fehlend: Logging

Megacooles ähnliches Projekt:
+  https://www.haraldkreuzer.net/aktuelles/bauanleitung-raspberry-pi-wetterstation-mit-wettervorhersage-und-esp32-funksensoren
+  und auf Github: https://github.com/HarryVienna/WeatherStation-Raspberry-Pi-base-station


DEV-Aspects:
USE GPIO-Pins from docker:
https://iotbytes.wordpress.com/create-your-first-docker-container-for-raspberry-pi-to-blink-an-led/
Entscheidend: Die Pins sind wohl irgendein File, das muss entsprechend in den Container mit Lese/Schreibrechten hineingemountet werden.

