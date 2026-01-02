def analyze_sensor_readings(readings):
    # Irrelevant transformation: normalize to z-scores (not used in final result)
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_val) / std_dev for x in readings] if std_dev != 0 else [0] * len(readings)

    # Semi-relevant preprocessing: apply moving average filter (partially used)
    smoothed = []
    window_size = 3
    for i in range(len(readings) - window_size + 1):
        window_avg = sum(readings[i:i+window_size]) / window_size
        smoothed.append(window_avg)

    # Core logic: detect anomalies using lambda threshold function
    threshold_func = lambda x: abs(x) > 25
    anomalies = list(filter(threshold_func, readings))

    # Distractor: simulate redundant classification pass
    classification_tags = []
    for val in readings:
        if val < 10:
            classification_tags.append('LOW')
        elif val > 90:
            classification_tags.append('HIGH')
        else:
            classification_tags.append('NORMAL')
    
    # Actual processing chain: slice middle segment and transform
    mid_segment = readings[2:-2]  # Remove edge effects
    squared_noisy = [x**2 + 1 for x in mid_segment]  # Artificial noise addition
    clipped_values = [min(x, 100) for x in squared_noisy]  # Cap at 100

    # Final processing with slicing and filtering
    processed_data = [x for x in clipped_values if x % 2 == 1]  # Keep only odd values
    filtered_sum = sum(processed_data)

    # Dead code path: unused conditional branch
    if len(anomalies) > 10:
        fallback = 0
        for i in range(len(z_scores)):
            fallback += int(z_scores[i])

    return filtered_sum

# Input data: simulated IoT sensor stream
sensor_input = [5, 12, 64, 33, 87, 41, 92, 74, 23, 18, 4]
result = analyze_sensor_readings(sensor_input)
print(f"Result: {result}")