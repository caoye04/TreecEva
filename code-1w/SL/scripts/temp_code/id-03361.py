def analyze_sensor_data():
    raw_readings = [105, 203, 98, -5, 110, 200, 95, 108, -10, 112]
    thresholds = (100, 200)
    
    # Normalize negative readings
    corrected_readings = [r if r >= 0 else 0 for r in raw_readings]
    
    # Identify valid readings within threshold range
    valid_readings = [val for val in corrected_readings if thresholds[0] <= val <= thresholds[1]]
    
    # Use enumerate to log positions of valid entries above median
    median_val = 104
    high_quality_indices = [i for i, val in enumerate(valid_readings) if val > median_val]
    
    # Extract high-quality entries using slicing
    sorted_valid = sorted(valid_readings)
    trimmed_data = sorted_valid[-len(high_quality_indices):]  # Top N matching count
    
    # Final filtered sum
    filtered_sum = sum(trimmed_data)
    
    # Irrelevant auxiliary calculation (minor distraction)
    avg_raw = sum(raw_readings) / len(raw_readings)
    
    print(f"Result: {filtered_sum}")

analyze_sensor_data()