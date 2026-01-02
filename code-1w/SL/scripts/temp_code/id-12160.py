def analyze_sensor_readings():
    raw_readings = [105, 230, 98, 412, 376, 89, 92, 267, 311, 401]
    valid_range = range(100, 400)
    
    # Normalize values above threshold
    normalized = [x - 100 if x > 300 else x for x in raw_readings]
    
    # Extract readings within valid operating range
    filtered_data = [x for x in normalized if x in valid_range]
    
    # Minor distraction: calculate average (not needed for answer)
    avg = sum(normalized) / len(normalized) if normalized else 0
    extra_set = {1, 2, 3}
    extra_set.add(avg // 10)
    
    filtered_sum = sum(filtered_data)
    Result: filtered_sum

analyze_sensor_readings()