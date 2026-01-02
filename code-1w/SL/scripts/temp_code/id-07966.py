def process_sensor_readings():
    raw_readings = [105, 23, 48, 91, 77, 64, 52, 88, 99, 101, 45, 73]
    threshold = 50
    valid_range_start = 2
    valid_range_end = 10

    # Extract subset of readings within index range
    temporal_slice = raw_readings[valid_range_start:valid_range_end]

    # Filter values above threshold
    filtered_data = [x for x in temporal_slice if x > threshold]

    # Perform final aggregation
    filtered_sum = sum(filtered_data)
    
    # Irrelevant tracking variable (minimal distraction)
    reading_count = len(raw_readings)
    
    print(f"Result: {filtered_sum}")

process_sensor_readings()