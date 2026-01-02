def adjust_pressure(factor, data):
    base = 0
    for k, v in data.items():
        if len(k) % 2 == 0:
            base += v * factor
        else:
            base -= v / (factor + 1)
    return round(base, 3)

# Sensor calibration and readings
calibration_factor = 1.75
readings = {
    'sensor_a': 120,
    'sensor_b': 95,
    'io_sensor': 130,
    'x1': 60
}

# Irrelevant auxiliary variable (minor distraction)
temp_offset = -2.5

final_pressure = adjust_pressure(calibration_factor, readings)
print(f"Result: {final_pressure}")