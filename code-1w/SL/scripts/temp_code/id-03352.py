def sensor_calibration(value, config_map):
    if value < 0:
        value = abs(value)
    multiplier = config_map['gain']
    offset = config_map['offset']
    adjusted = value * multiplier + offset
    return adjusted

raw_value = -45
adjustment_map = {'gain': 2.5, 'offset': -10.3}
pressure_reading = sensor_calibration(raw_value, adjustment_map)
print(f"Result: {pressure_reading}")