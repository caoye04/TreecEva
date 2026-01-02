import itertools

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSETS = {'temp': 0.987, 'pressure': 1.013, 'humidity': 0.992}
BASELINE_CORRECTION = sum(CALIBRATION_OFFSETS.values()) / len(CALIBRATION_OFFSETS)

# Simulated raw sensor readings with noise and redundancy
def generate_raw_readings():
    raw = [
        (1204, 'temp', 36.5), (1205, 'temp', 37.1), (1206, 'heart', 76),
        (1207, 'temp', 36.9), (1208, 'pressure', 1013), (1209, 'heart', 78),
        (1210, 'humidity', 45), (1211, 'temp', 37.2), (1212, 'heart', 80),
        (1213, 'pressure', 1015), (1214, 'heart', 82), (1215, 'temp', 36.8)
    ]
    return raw

# Irrelevant data transformation: converts to dict but not used in critical path
def convert_to_dict(readings):
    result = {}
    for r in readings:
        if r[1] not in result:
            result[r[1]] = []
        result[r[1]].append(r[2])
    return result

# Redundant smoothing function (never called in main execution)
def smooth_signal(signal_list, factor=0.85):
    smoothed = [signal_list[0]]
    for i in range(1, len(signal_list)):
        smoothed.append(smoothed[-1] * factor + signal_list[i] * (1 - factor))
    return smoothed

# Core filtering logic based on type and thresholds
def filter_anomalies(readings, types_of_interest):
    filtered = []
    for reading in readings:
        seq_id, r_type, value = reading
        if r_type in types_of_interest:
            # Only heart rate above 77 and temp between 36.7 and 37.3 are valid
            if r_type == 'heart' and value > 77:
                filtered.append((seq_id, r_type, value))
            elif r_type == 'temp' and 36.7 <= value <= 37.3:
                filtered.append((seq_id, r_type, value))
    return filtered

# Bitwise-based integrity check (distractor - not actually used)
def verify_integrity(data_chunk):
    checksum = 0
    for item in data_chunk:
        seq_id = item[0]
        checksum ^= seq_id
        checksum = (checksum << 1) & 0xFFFF
    return checksum % 100

# Threshold mapping for processing (used in final step)
def build_threshold_map(config_level=2):
    base_map = {
        'mild': (37.0, 80),
        'elevated': (37.3, 85)
    }
    # Complex expansion using itertools (partially relevant)
    expanded = {}
    for key, (t, h) in base_map.items():
        expanded[key + '_low'] = (t - 0.2, h - 5)
        expanded[key + '_high'] = (t, h)
    
    # Apply config-based filter (only some entries survive)
    selected = {}
    keys = ['mild_low', 'mild_high', 'elevated_low']
    if config_level > 1:
        for k in keys:
            selected[k] = expanded[k]
    return selected

# Main processing with accumulation and cross-type logic
def process_readings(readings, thresholds):
    # Extract heart rates and temps
    heart_rates = [r[2] for r in readings if r[1] == 'heart']
    temperatures = [r[2] for r in readings if r[1] == 'temp']
    
    # Compute moving averages (distractor)
    avg_heart = sum(heart_rates) / len(heart_rates) if heart_rates else 0
    avg_temp = sum(temperatures) / len(temperatures) if temperatures else 0
    
    # Critical logic: count how many readings exceed 'mild' threshold
    temp_threshold = thresholds['mild_high'][0]  # 37.0
    heart_threshold = thresholds['mild_high'][1]  # 80
    temp_count = sum(1 for t in temperatures if t >= temp_threshold)
    heart_count = sum(1 for h in heart_rates if h >= heart_threshold)
    
    # Combine using XOR pattern (bit manipulation)
    combined_flags = (temp_count << 2) ^ (heart_count << 1) ^ 1
    
    # Accumulate diagnostic score
    score = 0
    score += temp_count * 15
    score += heart_count * 12
    score += combined_flags  # inject bitwise result
    
    # Linear search for specific pattern in sequence IDs (distractor)
    readings_sorted = sorted(readings, key=lambda x: x[0])
    gap_count = 0
    for i in range(1, len(readings_sorted)):
        if readings_sorted[i][0] - readings_sorted[i-1][0] > 2:
            gap_count += 1
    
    # Final adjustment: irrelevant offset
    environment_factor = 3.14159
    adjusted_score = score - int(environment_factor)  # subtract 3
    
    return adjusted_score

# Entry point
if __name__ == '__main__':
    # Generate raw data
    raw_data = generate_raw_readings()
    
    # Convert but do not use (dead path)
    unused_dict = convert_to_dict(raw_data)
    
    # Filter only relevant readings
    filtered_data = filter_anomalies(raw_data, ['temp', 'heart'])
    
    # Build threshold map for diagnosis
    threshold_map = build_threshold_map(config_level=2)
    
    # Process the filtered data into diagnostic value
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")