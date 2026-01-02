def analyze_sensor_data():
    base_readings = [12, -5, 8, 0, 15, -3, 9, 7]
    scaling_factor = 1.5
    min_valid_reading = -10
    max_valid_reading = 20
    adjustment_offset = 2

    # Normalize readings by offset (irrelevant to final result)
    normalized_readings = [x + adjustment_offset for x in base_readings]

    # Filter valid sensor readings within acceptable range
    filtered_readings = [x for x in base_readings if min_valid_reading <= x <= max_valid_reading]

    # Apply conditional scaling based on system mode (unused branch)
    system_mode = 'eco'
    if system_mode == 'performance':
        scaling_factor *= 1.2

    energy_threshold = sum(filtered_readings) * scaling_factor
    return energy_threshold

result = analyze_sensor_data()
print(f"Result: {result}")