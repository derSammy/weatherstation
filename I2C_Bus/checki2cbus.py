import smbus

# Define the I2C bus number (usually 1 on Raspberry Pi)
bus_number = 1

# Create an I2C bus object
bus = smbus.SMBus(bus_number)

# Function to scan the I2C bus for connected devices
def scan_i2c_bus():
    devices = []
    for address in range(0, 128):
        try:
            bus.read_byte(address)
            devices.append(hex(address))
        except IOError:
            pass
    return devices

# Scan the I2C bus and print connected devices
connected_devices = scan_i2c_bus()
if connected_devices:
    print("Connected devices on I2C bus:")
    for device in connected_devices:
        print(device)
else:
    print("No devices found on the I2C bus.")
