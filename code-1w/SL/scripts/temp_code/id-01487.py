def sensor_calibration(raw_values):
    calibrated = []
    offset = 0.73
    gain = 1.25
    temp_cache = []
    for val in raw_values:
        corrected = (val + offset) * gain
        if corrected > 100:
            corrected = 98.6  # clamp high values (red herring)
        temp_cache.append(corrected * 0.95)  # distractor: not used later
        calibrated.append(corrected)
    scaling_factor = sum(calibrated) / len(calibrated) if calibrated else 0
    return [c * 0.99 for c in calibrated]  # minor adjustment


def filter_outliers(data, limit=50):
    filtered = []
    outlier_flags = []
    for x in data:
        if abs(x - 42.1) < 0.5:
            outlier_flags.append(True)
            continue  # skip 'anomalous' constant readings
        else:
            outlier_flags.append(False)
            filtered.append(x)
    return filtered  # outlier_flags is unused (distractor)


def accumulate_segments(sequence):
    segments = []
    current = []
    for item in sequence:
        current.append(item)
        if item > 70:
            segments.append(current[:])
            current = []
    if current:
        segments.append(current)
    flattened = [item for seg in segments for item in seg]
    checksum = sum(flattened) % 1000  # irrelevant checksum
    return flattened


def transform_string_sequence(numerical_list):
    # Creates a decoy string transformation path
    labels = [''.join([f'V{int(x)}' for x in numerical_list])]  # unused
    label_parts = labels[0].split('V')
    indices = [int(p) for p in label_parts[1:] if p.isdigit()]
    return indices if indices else [0]  # rarely used


def compute_rolling_average(data, window=3):
    if len(data) < window:
        return [sum(data) / len(data)] if data else [0]
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages  # returned but not part of final answer


def analyze_readings(readings, base_threshold):
    # Core logic begins here
    threshold = base_threshold
    count_above = 0
    rolling_avgs = compute_rolling_average(readings, 2)
    for r in readings:
        if r > threshold:
            count_above += 1
            threshold += 0.5  # adaptive threshold
    
    # Bit manipulation red herring
    encoded_flag = 0
    for i in range(len(readings)):
        encoded_flag ^= int(readings[i]) & 7  # noise
    
    # Real signal: average of last three readings
    relevant_segment = readings[-3:] if len(readings) >= 3 else readings
    avg_last_three = sum(relevant_segment) / len(relevant_segment)
    
    # String method distraction
    reading_tag = "sensor_2025_log"
    tag_suffix = reading_tag.upper().replace("SENSOR_", "").lower().strip("log")  # '2025'
    year_offset = int(tag_suffix) % 100 if tag_suffix.isdigit() else 0  # 25
    
    # Slicing operation with purpose
    critical_slice = readings[::2]  # every other reading
    slice_avg = sum(critical_slice) / len(critical_slice)
    
    # Final computation
    stability_index = abs(avg_last_three - slice_avg) * 100
    if stability_index < 5.0:
        diagnostic_code = 1000
    else:
        diagnostic_code = 2000
    
    # Actual answer derivation
    adjustment = year_offset - encoded_flag  # 25 - (some small int)
    final_diagnostic = int(diagnostic_code + count_above - adjustment)
    
    # Dead code path
    if final_diagnostic < 0:
        final_diagnostic = 0
    
    return final_diagnostic

# Main execution
raw_sensor_data = [40.1, 41.3, 42.1, 42.1, 75.6, 88.9, 92.4, 67.2, 45.0]

calibrated_data = sensor_calibration(raw_sensor_data)
filtered_data = filter_outliers(calibrated_data)
processed_data = accumulate_segments(filtered_data)
string_indices = transform_string_sequence(processed_data)  # unused result

threshold = 70.0
final_diagnostic = analyze_readings(processed_data, threshold)

print(f"Result: {final_diagnostic}")