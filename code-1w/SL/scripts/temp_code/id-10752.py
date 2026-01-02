def calculate_final_score(raw_data, limits):
    # Preprocessing: extract relevant segments using slicing
    segment_a = raw_data[2:7]
    segment_b = raw_data[5:10]
    
    # Misleading intermediate computations (distractors)
    temp_sum = sum([x ** 0.5 for x in raw_data if x > 10])
    temp_avg = temp_sum / len(raw_data) if raw_data else 0
    adjustment_factor = len(segment_a) - len(segment_b)  # Always -2 due to overlap

    # Actual signal processing path
    filtered = [x for x in segment_a if x > limits['low']]
    peak_value = max(filtered) if filtered else 0

    # Dictionary-based threshold logic
    scores = {
        'base': sum(segment_b),
        'bonus': 0,
        'penalty': 0
    }

    if peak_value > limits['high']:
        scores['bonus'] += 15
    elif peak_value > limits['mid']:
        scores['bonus'] += 8
    else:
        scores['penalty'] -= 5

    # Linear search for anomaly (not strictly necessary but adds cognitive load)
    anomaly_found = False
    for i in range(len(segment_b)):
        if segment_b[i] < 0:
            anomaly_found = True
            break
    
    if anomaly_found:
        scores['penalty'] -= 10  # Not triggered in this case

    # Red herring: unused helper calculation
    def smooth_signal(s):
        return [round((s[i-1] + s[i] + s[i+1]) / 3, 2) for i in range(1, len(s)-1)]
    smoothed = smooth_signal(raw_data)  # Computed but not used

    # Final aggregation
    base_score = scores['base'] + scores['bonus'] + scores['penalty']
    final_score = int(base_score * 0.9)  # Apply fixed scaling
    
    return final_score

# Main execution context
sensor_readings = [4, 8, 12, 15, 9, 11, 13, 7, 5, 10, 6]
thresh = {
    'low': 6,
    'mid': 10,
    'high': 12
}

# Irrelevant preprocessing (adds distraction)
processed = [x for x in sensor_readings if x % 2 == 0]
duplicate_check = len(processed) != len(set(processed))

result = calculate_final_score(sensor_readings, thresh)
print(f"Result: {result}")