def analyze_sensor_data(readings):
    base_threshold = 75
    secondary_limit = 90
    adjustment = 0.85
    correction_factor = 1.2

    # Normalize values above secondary limit
    normalized = [val * adjustment for val in readings if val > secondary_limit]

    # Filter readings based on dynamic threshold
    filtered_readings = [val for val in readings if val > base_threshold]

    # Apply conditional offset based on data size
    if len(normalized) > 2:
        filtered_readings = [val + 5 for val in filtered_readings]

    filtration_score = sum(filtered_readings) * correction_factor
    return filtration_score

sensor_readings = [68, 76, 82, 95, 79, 88, 91]
result = analyze_sensor_data(sensor_readings)
print(f"Target result: {result}")