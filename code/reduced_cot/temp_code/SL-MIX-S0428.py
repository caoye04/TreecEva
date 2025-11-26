sensor_readings = [18.5, 22.3, 19.8, 25.1, 17.6]
processed_temps = [int(temp) for temp in sensor_readings if temp > 20]
ambient_factor = len(sensor_readings) - 2
temperature_adjustment = processed_temps[1] | (processed_temps[0] & 0b1111)
print(f"Result: {temperature_adjustment}")