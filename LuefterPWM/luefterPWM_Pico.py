import machine
from machine import I2C, Pin, PWM
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from utime import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

luefter_out_pin = 10

pin_rot_button = 19


pwm_freq = 1000

pin_luefter_pwm = PWM(Pin(luefter_out_pin))

pin_luefter_pwm.freq(1000)


button_rot = Pin(pin_rot_button, Pin.IN, Pin.PULL_DOWN)


lcd.putstr("PWM Level")
lcd.putstr("\n100")

def convert_pwm_value(percent):
    percent_check(percent)
    return int(65535 * percent / 100)

def get_three_digits(value):
    return "{: >3}".format(value)

def percent_check(percent):
    try:
        float(percent)
    except ValueError:
        raise ValueError("Der Eingabewert 'percent' ist keine Zahl")
    if percent <0 or percent >100:
        raise ValueError("Der Eingabwert 'percent' muss zwischen 0 und 100 liegen")

luefter_level = 0

while True:
    if button_rot.value():
        luefter_level += 1
        if luefter_level == 101:
            luefter_level = 0
    
    percent_check(luefter_level)
    
    lcd.move_to(0,1)        
    lcd.putstr(get_three_digits(luefter_level))
    
    pin_luefter_pwm.duty_u16(convert_pwm_value(luefter_level))
 
    
    sleep(.01)

