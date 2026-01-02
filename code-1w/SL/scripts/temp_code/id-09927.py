def analyze_sensor_data(raw_readings, threshold, calibration_factor):
    # Simulate preprocessing steps with some irrelevant computations
    normalized = [x * calibration_factor for x in raw_readings]
    squared_devs = [(x - sum(normalized) / len(normalized)) ** 2 for x in normalized]  # Unused metric
    avg_power = sum([x**2 for x in normalized]) / len(normalized)  # Red herring statistic

    # Conditional filtering based on dynamic criteria
    high_confidence = [x for x in normalized if x > threshold]
    adjusted_offsets = [abs(x - 25.0) for x in high_confidence]  # Distractor list

    # Key logic: classify and select based on pattern
    classification_flags = ['high' if x >= 30 else 'medium' if x >= 20 else 'low' for x in high_confidence]
    valid_indices = [i for i, flag in enumerate(classification_flags) if flag in {'high', 'medium'}]

    # Use slicing to extract relevant segment
    candidate_data = [high_confidence[i] for i in valid_indices][1:]  # Skip first valid

    # Introduce set operations for overlap analysis (partly irrelevant)
    baseline_set = {round(x) for x in raw_readings}
    adjusted_set = {round(x + 0.5) for x in adjusted_offsets}
    common_elements = baseline_set & adjusted_set  # Not used later

    # Final filtering using conditional expression within list comprehension
    filtered_data = [x for x in candidate_data if (lambda val: True if val < 45 else False)(x)]

    # Critical execution point
    filtered_sum = sum(filtered_data)
    
    # Print result as required
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Input data
sensor_inputs = [18.2, 22.1, 25.6, 31.8, 36.3, 19.7, 42.0, 24.9]
THRESH = 21.0
CALIB = 1.05

# Execute function
data_sum = analyze_sensor_data(sensor_inputs, THRESH, CALIB)