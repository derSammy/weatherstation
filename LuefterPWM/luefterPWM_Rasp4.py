import time

import RPi.GPIO as GPIO
from gpiozero import CPUTemperature

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
logging.getLogger().addHandler(console_handler)



cpu = CPUTemperature()


cpu_temperature = cpu.temperature

# Pin12, das ist der GPIO18, mit eigener Platine weiß kodiert
pwm_pin = 18

pwm_frequency = 100

GPIO.setmode(GPIO.BCM)

GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, pwm_frequency)


def set_pwm_level_by_temp(cpu_temperature):
    # (temperature_cutoff, set_pwm_level)
    
    fan_levels_by_cutoff = [(80, 100),
                            (77,  67),
                            (73,  40),
                            (70,  30),
                            (65,  24),
                            (60,  18),
                            (55,  14),
                            (40,  11),
                            (30,   0)
    ]
    for (temperature_cutoff, pwm_level) in fan_levels_by_cutoff:
        if cpu_temperature >= temperature_cutoff:
            return pwm_level
    #if not above 30 at all
    return 0


# GPIO.cleanup() necessary?

# start fan with some moderate speed
duty_cycle_percent = 18
pwm.start(duty_cycle_percent)


while True:
    cpu_temperature = cpu.temperature
    new_duty_cycle_percent = set_pwm_level_by_temp(cpu_temperature)
    
    if new_duty_cycle_percent != duty_cycle_percent:
        duty_cycle_percent = new_duty_cycle_percent
        logging.info(f"Set PWM level to {duty_cycle_percent}%, since CPU temp is {cpu_temperature}°C")
        pwm.ChangeDutyCycle(duty_cycle_percent)
    
    time.sleep(5)
