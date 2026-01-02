def analyze_set_overlap():
    sensor_a_readings = {1, 2, 3, 5, 8, 13, 21}
    sensor_b_readings = {3, 5, 7, 8, 13, 19, 21}
    
    # Filter valid range for both sensors
    valid_range = set(range(1, 25))
    filtered_a = sensor_a_readings & valid_range
    filtered_b = sensor_b_readings & valid_range
    
    # Compute intersection of readings within valid range
    common_elements = filtered_a.intersection(filtered_b)
    
    # Calculate sum of overlapping values
    overlap_sum = sum(common_elements)
    
    # Early return if no overlap (not triggered here)
    if not common_elements:
        return 0
    
    # Dummy auxiliary calculation (minimal interference)
    total_unique = len(filtered_a.union(filtered_b))
    
    return overlap_sum

result = analyze_set_overlap()
print(f"Result: {result}")