def analyze_sensor_data():
    raw_readings = [105, 92, 110, 87, 98, 103, 84, 95, 108, 91]
    offset_adjustment = 5
    adjusted_readings = [x + offset_adjustment for x in raw_readings]
    
    # Filter readings within normal operating range
    filtered_readings = [x for x in adjusted_readings if 95 <= x <= 110]
    
    # Calculate average using integer division
    filtration_score = sum(filtered_readings) // len(filtered_readings)
    
    # Irrelevant tracking variable (minimal interference)
    reading_count = len(raw_readings)
    
    print(f"Result: {filtration_score}")

analyze_sensor_data()