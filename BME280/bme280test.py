import time
import smbus2
import bme280

# BME280 sensor address (default address)
address = 0x77

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Load calibration parameters
calibration_params = bme280.load_calibration_params(bus, address)

def convert_to_sealevel(abs_preasure, temperature):
    # Alternativ: https://rechneronline.de/barometer/
    # gemessener Druck
    P = abs_preasure
    
    # durchschnittliche Temperaturabnahme pro Meter
    L = 0.0065
    
    # akutelle Höhe
    h = 210
    
    # temperature in K
    T0 = 273 + temperature
    
    # Fallbeschleunigung
    g = 9.80665
    
    # spezifische Gaskonstante
    R = 287.05
    correction_factor = (1 + (L*h)/T0)**(g/(R*L))
    sealevel_pressure = P * correction_factor
    print(correction_factor)
    return sealevel_pressure

while True:
    try:
        # Read sensor data
        data = bme280.sample(bus, address, calibration_params)
        print(data)

        # Extract temperature, pressure, and humidity
        temperature_celsius = data.temperature
        abs_pressure = data.pressure
        sealevel_pressure = convert_to_sealevel(data.pressure, data.temperature)
        humidity = data.humidity

        # Print the readings
        print("Temperature: {:.2f} °C".format(temperature_celsius))
        print("Absolute Pressure: {:.2f} hPa".format(abs_pressure))
        print("Sea-level Pressure: {:.2f} hPa".format(sealevel_pressure))
        print("Humidity: {:.2f} %".format(humidity))

        # Wait for a few seconds before the next reading
        time.sleep(15)

    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        break