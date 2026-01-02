def analyze_sensor_data(raw_readings):
    # Preprocessing: remove outliers and normalize
    threshold = 50
    normalized = [x - 25 for x in raw_readings]
    filtered = [x for x in normalized if abs(x) < threshold]

    # Irrelevant transformation: frequency analysis (not used later)
    freq_map = {}
    for val in filtered:
        freq_map[val] = freq_map.get(val, 0) + 1
    avg_freq = sum(freq_map.values()) / len(freq_map) if freq_map else 0

    # Key processing with slicing and lambda
    shifted = [x + 10 for x in filtered][1:-1]  # Slice to remove edges
    processor = lambda x: x * 2 if x > 0 else x // 2
    processed_data = list(map(processor, shifted))

    # Dead code: simulated calibration (no impact)
    calibration_offset = 3.14
    adjusted_readings = [x + calibration_offset for x in processed_data]
    adjustment_factor = len(adjusted_readings) % 7 if adjusted_readings else 1

    # Final computation
    temp_result = sum(shifted) * 0.5  # Distractor calculation
    filtered_sum = sum(processed_data)
    
    # Additional red herring: bitwise obfuscation (unused)
    mask = 0b1101
    obfuscated = [x ^ mask for x in processed_data]

    print(f"Result: {filtered_sum}")
    return filtered_sum

# Simulated sensor input
data_stream = [78, 20, 35, 45, 60, 10, 85, 30]
analyze_sensor_data(data_stream)