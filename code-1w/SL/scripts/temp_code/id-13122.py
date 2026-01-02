from itertools import compress

def calculate_system_pressure(sensors, calib):
    valid_sensors = list(compress(sensors, [s > 0 for s in sensors]))
    calibrated = [s * calib.get(f'sensor_{i+1}', 1.0) for i, s in enumerate(valid_sensors)]
    total_pressure = sum(calibrated)
    return total_pressure

# Sensor readings in kPa
sensors = [101.3, -5, 98.7, 102.1, 0, 99.9]

# Calibration multipliers for active sensors
calibration_data = {'sensor_1': 1.02, 'sensor_3': 0.99, 'sensor_4': 1.01, 'sensor_6': 1.05}

# Compute final pressure
total_pressure = calculate_system_pressure(sensors, calibration_data)

Result: {total_pressure}