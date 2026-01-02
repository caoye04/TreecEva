def analyze_sensor_readings():
    raw_readings = [105, 92, 97, 110, 88, 95, 103, 98, 100, 90]
    threshold = 95
    
    # Normalize readings by subtracting baseline offset
    normalized_readings = [x - 5 for x in raw_readings]
    
    # Identify anomalous values above threshold
    anomalies = {x for x in normalized_readings if x > threshold}
    
    # Filter valid operational range (85 <= x <= 100) using slicing to examine middle segment
    candidate_region = sorted(normalized_readings)[1:-1]  # Exclude min and max potential outliers
    filtered_data = [x for x in candidate_region if 85 <= x <= 100]
    
    # Compute final diagnostic metric
    filtered_sum = sum(filtered_data)
    
    # Irrelevant debugging trace (minimal interference)
    debug_flag = True
    if debug_flag:
        pass  # No effect on computation
        redundant_check = len(anomalies) > 0
    
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()