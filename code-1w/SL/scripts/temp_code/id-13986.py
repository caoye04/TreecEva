def analyze_sensor_data(raw_readings, threshold):
    # Initialize tracking and processed variables
    cumulative_noise = 0
    valid_segments = []
    temp_buffer = []

    # Simulate noise filtering with sliding window
    for i in range(len(raw_readings) - 2):
        window = raw_readings[i:i+3]
        avg = sum(window) / 3
        if avg > threshold:
            temp_buffer.extend(window)
        else:
            cumulative_noise += avg

    # Misleading dead code path: never reached due to logic above
    if len(temp_buffer) == 0:
        temp_buffer.append(99999)  # red herring

    # Actual processing uses different logic
    processed_data = []
    for val in raw_readings:
        if val % 2 == 0 and val > threshold * 1.5:
            processed_data.append(val * 0.5)
        elif val > threshold:
            processed_data.append(val * 0.7)

    # Secondary distraction: unused statistical calculation
    mean_processed = sum(processed_data) / len(processed_data) if processed_data else 0
    std_dev = (sum((x - mean_processed) ** 2 for x in processed_data)) ** 0.5 if processed_data else 0

    # Key statement
    filtered_sum = sum(processed_data)

    # Debug logs (irrelevant to result)
    debug_flag = False
    if debug_flag:
        print(f"Noise: {cumulative_noise}, Buffer: {temp_buffer}")

    return filtered_sum

# Main execution
sensor_readings = [12, 15, 8, 21, 16, 7, 10, 14]
trigger_level = 10
result = analyze_sensor_data(sensor_readings, trigger_level)
print(f"Result: {result}")