def analyze_sensor_readings():
    raw_readings = [105, 92, -5, 88, 110, 95, -12, 99, 101]
    offset = 10
    adjusted_readings = [x + offset for x in raw_readings]
    
    # Irrelevant transformation (distractor)
    inverted = [1.0 / (x + 1) for x in adjusted_readings if x != -1]
    
    # Key filtering: only valid readings above threshold
    valid_readings = [x for x in adjusted_readings if 90 <= x <= 110]
    
    # Apply scaling factor to valid data
    scaled_valid = [int(x * 0.9) for x in valid_readings]
    
    # Slice to exclude first and last elements (slicing operation)
    trimmed_data = scaled_valid[1:-1]
    
    # Dictionary usage: count occurrences (set as default to remove dupes)
    unique_trimmed = list(set(trimmed_data))
    count_dict = {val: trimmed_data.count(val) for val in unique_trimmed}
    
    # Final computation on filtered data
    filtered_sum = sum(trimmed_data)
    
    # Print result as required
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()