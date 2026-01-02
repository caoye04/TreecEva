def analyze_sensor_data():
    base_readings = [12, 15, 8, 23, 17, 4, 19, 11]
    thresholds = [x for x in base_readings if x > 10]
    
    # Irrelevant auxiliary list (minor distraction)
    aux_data = [x * 0.1 for x in base_readings]
    
    scaled_values = [x * 1.2 for x in thresholds]
    correction_factor = 0.9
    
    # Extract every second reading starting from index 1
    filtered_readings = scaled_values[1::2]
    
    energy_threshold = sum(filtered_readings) * correction_factor
    
    # Dummy variable to slightly distract without adding complexity
    status_flag = len(scaled_values) > 5
    
    return energy_threshold

result = analyze_sensor_data()
print(f"Result: {result}")