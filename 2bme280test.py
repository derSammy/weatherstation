import time
import smbus2
import bme280

# BME280 sensor address (default address)
address_out = 0x77
address_in = 0x76

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Load calibration parameters
calibration_params_out = bme280.load_calibration_params(bus, address_out)
calibration_params_in = bme280.load_calibration_params(bus, address_in)


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
        print(data_out)
        data_in = bme280.sample(bus, address_in, calibration_params_in	)
        print(data_in)


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
        print("Temperature out: {:.2f} °C".format(temperature_celsius_out))
        print("Absolute Pressure out: {:.2f} hPa".format(abs_pressure_out))
        print("Sea-level Pressure out: {:.2f} hPa".format(sealevel_pressure_out))
        print("Humidity out: {:.2f} %".format(humidity_out))
        
        print("Temperature in: {:.2f} °C".format(temperature_celsius_in))
        print("Absolute Pressure in: {:.2f} hPa".format(abs_pressure_in))
        print("Sea-level Pressure in: {:.2f} hPa".format(sealevel_pressure_in))
        print("Humidity in: {:.2f} %".format(humidity_in))

        # Wait for a few seconds before the next reading
        time.sleep(5)

    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        break