def process_sensor_readings():
    raw_readings = [105, 92, 97, 110, 88, 95, 103, 98, 100, 90]
    threshold = 95
    
    # Normalize readings by subtracting baseline offset
    baseline_offset = 85
    normalized_readings = [x - baseline_offset for x in raw_readings]
    
    # Identify high-variance segments using slicing
    segment_a = normalized_readings[:5]
    segment_b = normalized_readings[5:]
    variance_a = max(segment_a) - min(segment_a)
    variance_b = max(segment_b) - min(segment_b)
    
    # Filter readings above threshold using lambda
    filter_func = lambda x: x > (threshold - baseline_offset)
    filtered_data = list(filter(filter_func, normalized_readings))
    
    # Compute final result
    filtered_sum = sum(filtered_data)
    print(f"Result: {filtered_sum}")

process_sensor_readings()