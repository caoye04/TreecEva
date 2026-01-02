def analyze_sensor_data():
    sensory_readings = [34, 56, 78, 23, 89]
    system_active = len(sensory_readings) > 4
    calibration_offset = 1.5  # unused in final computation
    temp_log = [x * 0.1 for x in sensory_readings]  # auxiliary logging
    energy_threshold = max(sensory_readings) if system_active else sum(sensory_readings)
    return energy_threshold

result = analyze_sensor_data()
print(f"Target result: {result}")