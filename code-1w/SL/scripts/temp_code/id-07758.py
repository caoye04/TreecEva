def process_sensor_data():
    raw_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8]
    scaling_factor = 1.05
    offset = -2.5
    
    # Normalize readings using min-max scaling
    min_val, max_val = min(raw_readings), max(raw_readings)
    normalized_readings = [(x - min_val) / (max_val - min_val) for x in raw_readings]
    
    # Apply calibration adjustment
    adjusted_readings = [val * 100 for val in normalized_readings]
    
    # Add environmental offset and scale
    final_temperature = adjusted_readings[-1] * scaling_factor + offset
    
    # Irrelevant tracking variable (minimal interference)
    total_processed = len(adjusted_readings)
    
    print(f"Result: {final_temperature}")

process_sensor_data()