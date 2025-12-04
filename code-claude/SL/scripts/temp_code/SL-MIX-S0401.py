import itertools

def calculate_sensor_data(readings):
    # Process sensor readings with various filters
    baseline = sum(readings) / len(readings)
    calibration_factor = 2.5
    
    # Apply first-level processing
    processed = []
    for i, reading in enumerate(readings):
        if i % 3 == 0:
            # Special processing for every third reading
            processed.append(reading * 1.2)
        else:
            processed.append(reading)
    
    # Calculate noise threshold
    noise_threshold = baseline * 0.4
    max_reading = max(processed)
    min_reading = min(processed)
    
    # Unused metrics for diagnostic purposes
    range_value = max_reading - min_reading
    variance = sum((x - baseline)**2 for x in readings) / len(readings)
    
    # Apply secondary filter based on distance from baseline
    filtered_values = []
    outlier_count = 0
    
    for reading in processed:
        if abs(reading - baseline) > noise_threshold:
            outlier_count += 1
            continue
        filtered_values.append(int(reading / calibration_factor))
    
    # Calculate some additional metrics (not directly used)
    pairs = list(itertools.combinations(filtered_values[:3], 2))
    pair_diffs = [abs(x - y) for x, y in pairs]
    
    # Map values through a transformation function
    transform = lambda x: x + 2 if x % 2 == 0 else x
    transformed = list(map(transform, filtered_values))
    
    # Extract the values we're interested in
    filtered_sum = sum(x for x in filtered_values)
    transformed_sum = sum(transformed)
    
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Sample sensor readings
readings = [10, 12, 9, 14, 8, 15, 11]
calculate_sensor_data(readings)