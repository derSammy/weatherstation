import RPi.GPIO as GPIO
import time
import subprocess

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
logging.getLogger().addHandler(console_handler)

SENSOR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

logging.info(f"Initialized PIR sensor on Pin {SENSOR_PIN}")

def switchOffHdmi(hdmi_port=2):
	befehl = ["xrandr", "--output", f"HDMI-{hdmi_port}", "--off"]
	umgebung = {"DISPLAY": ":0.0"}
	subprocess.run(befehl, env=umgebung)
	
def switchOnHdmi(hdmi_port=2):
	befehl = ["xrandr", "--output", f"HDMI-{hdmi_port}", "--mode", "1024x600", "--rate", "60"]
	umgebung = {"DISPLAY": ":0.0"}
	subprocess.run(befehl, env=umgebung)

def getMotionSensorStatus(SENSOR_PIN):
    try:
        motionDetected = GPIO.input(SENSOR_PIN)
    except KeyboardInterrupt:
        logging.info('Program stopped')
    except Exception as e:
        logging.exception('An unexpected error occurred:', str(e))
    
    if motionDetected:
        logging.info("Motion detected!")
        return True
    else:
        logging.info("No Motion")
        return False


while True:
	switchOnHdmi()
	
	time.sleep(15)
	
	switchOffHdmi()
	
	time.sleep(15)

#    
#    getMotionSensorStatus(SENSOR_PIN)
#    
#    time.sleep(10)
