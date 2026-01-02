def analyze_sensor_data():
    raw_readings = [12.5, 18.2, 9.7, 25.1, 30.0, 14.3, 8.8, 22.6]
    offset = 2.1
    adjusted_readings = [x + offset for x in raw_readings]
    
    # Irrelevant metadata (minimal distraction)
    sensor_metadata = {'model': 'X27', 'calibration': '2023-10-05'}
    readings_count = len(adjusted_readings)
    
    # Key processing step
    valid_range = lambda x: 15 <= x <= 28
    filtered_readings = list(filter(valid_range, adjusted_readings))
    
    energy_threshold = max(filtered_readings)
    return energy_threshold

result = analyze_sensor_data()
print(f"Result: {result}")