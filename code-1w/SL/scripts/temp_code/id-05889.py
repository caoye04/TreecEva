def analyze_sensor_readings():
    raw_readings = [
        ('temp', 23.5), ('pressure', 1013.2), ('temp', 24.1),
        ('humidity', 45), ('temp', 22.8), ('pressure', 1012.8)
    ]

    # Extract only temperature readings using dictionary mapping for context
    sensor_types = {'temp': 'C', 'pressure': 'hPa', 'humidity': '%'}
    temp_only = [item for item in raw_readings if item[0] == 'temp']

    # Apply offset correction using a lambda (simulating calibration)
    calibrated_temps = list(map(lambda x: (x[0], round(x[1] + 0.2, 1)), temp_only))

    # Filter out any readings below threshold (e.g., sensor noise)
    filtered_data = [item for item in calibrated_temps if item[1] >= 23.0]

    # Final computation on cleaned and transformed data
    filtered_sum = sum(map(lambda x: x[1], filtered_data))

    # Irrelevant auxiliary variable (minor distraction)
    avg_pressure = sum(item[1] for item in raw_readings if item[0] == 'pressure') / 2

    print(f"Result: {filtered_sum}")

analyze_sensor_readings()