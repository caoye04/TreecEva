def analyze_sensor_data():
    raw_readings = [105, 203, 98, 110, 250, 95, 102, 88, 315, 290]
    threshold = 100
    offset_correction = 5

    corrected_readings = [x - offset_correction for x in raw_readings]
    
    # Apply filter to retain only readings within normal operating range
    filtered_readings = [val for val in corrected_readings if 90 < val < 275]
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_reading = max(corrected_readings)
    
    filtration_score = sum(filtered_readings)
    
    # Additional minor distraction: unused transformation
    normalized = ''.join(str(int(x // 10)) for x in filtered_readings)
    
    print(f"Result: {filtration_score}")

analyze_sensor_data()