def process_sensor_data(raw_readings):
    scaling_factor = 0.85
    offset = 10
    
    # Normalize sensor readings
    normalized = [(x * scaling_factor) + offset for x in raw_readings]
    
    # Define threshold and filter active readings
    baseline = 50
    threshold = baseline * 1.1
    
    # Filter readings above threshold and compute average
    filter_func = lambda x: x > threshold
    filtered = list(filter(filter_func, normalized))
    
    if filtered:
        total = sum(filtered)
        average_val = total / len(filtered)
        filtered_avg = round(average_val, 3)
    else:
        filtered_avg = 0.0
    
    # Irrelevant auxiliary variable (minor distraction)
    status_flags = [True, False, True]
    
    # Final result output
    print(f"Result: {filtered_avg}")
    return filtered_avg

# Input data
readings = [70, 85, 90, 45, 60, 100, 55]
result = process_sensor_data(readings)