def analyze_sensor_readings():
    raw_readings = [105, 92, 117, 88, 95, 120, 102, 98, 110, 90]
    threshold = 95
    
    # Normalize readings by subtracting baseline offset
    normalized_readings = [x - 85 for x in raw_readings]
    
    # Apply filtering: only keep values within safe operating range
    valid_range = (10, 25)
    filtered_data = [val for val in normalized_readings if valid_range[0] <= val <= valid_range[1]]
    
    # Further process with slicing: ignore first and last element to remove edge noise
    processed_data = filtered_data[1:-1]
    
    # Compute final diagnostic metric
    filtered_sum = sum(processed_data)
    
    # Irrelevant auxiliary variable (minimal distraction)
    average_normalized = sum(normalized_readings) / len(normalized_readings)
    
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()