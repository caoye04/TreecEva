def monitor_pressure(level):
    thresholds = {1: 101.3, 2: 202.6, 3: 405.2, 4: 810.4}
    adjustments = {1: 0.5, 2: 1.0, 3: 2.0, 4: 4.0}
    base = thresholds.get(level, 0)
    factor = adjustments.get(level, 1)
    
    # Simulate calibration offset (irrelevant for level 4)
    calibration_mode = False
    temp_offset = 2.5 if calibration_mode else 0.0
    
    if level > 0 and level <= 4:
        reading = base * factor
        if level >= 3:
            reading -= adjustments[3]  # correction step
        return reading
    return -1

# Irrelevant sensor initialization
sensor_status = 'active'
sensor_type = 'digital'

pressure_reading = monitor_pressure(4)
print(f'Result: {pressure_reading}')