import RPi.GPIO as GPIO
import time
import subprocess

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
logging.getLogger().addHandler(console_handler)

SENSOR_PIN = 17

SWITCH_OFF_DELAY = 180
# in Seconds

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
        logging.debug("Motion detected!")
        return True
    else:
        logging.debug("No Motion")
        return False
    
def waitToReactivate(hdmi_port=2):
    while True:
        if getMotionSensorStatus(SENSOR_PIN):
            switchOnHdmi(hdmi_port=hdmi_port)
            logging.info("Switched on HDMI output")
            return
        time.sleep(10)


GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

logging.info(f"Initialized PIR sensor on Pin {SENSOR_PIN}")

start_time = time.time()
switchOnHdmi()
logging.info(f"Startet ScreenHandler at {start_time} and startet HDMI output")
logging.info(f"Switch-Off delay is set to {SWITCH_OFF_DELAY} Seconds.")
last_active_time = start_time

while True:
    time_now = time.time()
    if getMotionSensorStatus(SENSOR_PIN):
        last_active_time = time_now
    elif time_now - last_active_time >= SWITCH_OFF_DELAY:
        logging.info("Switched of HDMI output")
        switchOffHdmi()
        waitToReactivate()
        last_active_time = time.time()
        
    time.sleep(30)