import time
import smbus2
import bme280

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
logging.getLogger().addHandler(console_handler)


# BME280 sensor address (default address)
address_out = 0x76
address_in = 0x77

# Initialize I2C bus
bus = smbus2.SMBus(1)
logging.info("Initialized I2C bus")


# Load calibration parameters
calibration_params_out = bme280.load_calibration_params(bus, address_out)
calibration_params_in = bme280.load_calibration_params(bus, address_in)
logging.info("Loaded Calibrations")


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
        data_out = bme280.sample(bus, address_out, calibration_params_out)
        #print(data_out)
        data_in = bme280.sample(bus, address_in, calibration_params_in	)
        #print(data_in)


        # Extract temperature, pressure, and humidity
        temperature_celsius_out = data_out.temperature
        abs_pressure_out = data_out.pressure
        sealevel_pressure_out = convert_to_sealevel(data_out.pressure, data_out.temperature)
        humidity_out = data_out.humidity
        
        temperature_celsius_in = data_in.temperature
        abs_pressure_in = data_in.pressure
        sealevel_pressure_in = convert_to_sealevel(data_in.pressure, data_in.temperature)
        humidity_in = data_in.humidity

        # Print the readings
        print("=== OUT ===")
        print("Temperature out: {:.2f} °C".format(temperature_celsius_out))
        #print("Absolute Pressure out: {:.2f} hPa".format(abs_pressure_out))
        print("Sea-level Pressure out: {:.2f} hPa".format(sealevel_pressure_out))
        print("Humidity out: {:.2f} %\n".format(humidity_out))
        logging.info("OUT: {:.2f} °C == ".format(temperature_celsius_out) +
                     "{:.2f} hPa == ".format(sealevel_pressure_out) +
                     "{:.2f} % LF".format(humidity_out))
        
        print("--- IN ---")
        print("Temperature in: {:.2f} °C".format(temperature_celsius_in))
        #print("Absolute Pressure in: {:.2f} hPa".format(abs_pressure_in))
        print("Sea-level Pressure in: {:.2f} hPa".format(sealevel_pressure_in))
        print("Humidity in: {:.2f} %\n".format(humidity_in))
        logging.info("IN:  {:.2f} °C == ".format(temperature_celsius_in) +
                     "{:.2f} hPa == ".format(sealevel_pressure_in) +
                     "{:.2f} % LF".format(humidity_in))


        # Wait for a few seconds before the next reading
        time.sleep(60)

    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        break
