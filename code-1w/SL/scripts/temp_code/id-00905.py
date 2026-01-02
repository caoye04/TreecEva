def process_sensor_readings():
    raw_readings = [105, 203, 98, 111, 201, 99, 107, 205]
    thresholds = {'min': 100, 'max': 200}
    valid_range_mask = [(thresholds['min'] <= x <= thresholds['max']) for x in raw_readings]
    selected_readings = [raw_readings[i] for i in range(len(raw_readings)) if valid_range_mask[i]]
    
    # Irrelevant auxiliary calculation (minor distraction)
    avg_reading = sum(raw_readings) / len(raw_readings) if raw_readings else 0
    
    # Core computation
    subset_slice = selected_readings[::2]  # Every other valid reading
    filtered_data = [x for x in subset_slice if x % 2 == 1]  # Keep only odd values
    filtered_sum = sum(filtered_data)
    
    # Print final result as required
    print(f"Result: {filtered_sum}")

process_sensor_readings()