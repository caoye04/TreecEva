def analyze_readings(sensor_data, threshold=0.75):
    raw_magnitudes = [x * 1.8 + 32 for x in sensor_data if x > -40]
    normalized = [round(x / max(raw_magnitudes), 3) for x in raw_magnitudes]
    
    # Distractor: irrelevant temperature conversion
    celsius_list = [(f - 32) * 5/9 for f in raw_magnitudes]
    avg_celsius = sum(celsius_list) / len(celsius_list) if celsius_list else 0
    temp_offset = abs(avg_celsius) % 10

    # Distractor: unused frequency map
    frequency_map = {}
    for val in normalized:
        rounded = int(val * 100)
        frequency_map[rounded] = frequency_map.get(rounded, 0) + 1

    # Real logic begins: detect anomalies via deviation
    deviations = [abs(x - 0.5) for x in normalized]
    outlier_flags = [d > threshold for d in deviations]
    
    # Bitwise manipulation on index pattern (relevant)
    control_mask = 0
    for i, flag in enumerate(outlier_flags):
        if flag:
            control_mask ^= (i + 1)  # XOR index into mask

    # Distractor: dead code path (never called)
    def deprecated_calibrator(x):
        return (x ** 0.5) * 100 if x > 0 else 0

    # Distractor: misleading intermediate score
    pseudo_entropy = 0
    for x in normalized:
        if x > 0:
            pseudo_entropy += x * (-x) * 100

    # Real entropy calculation used later
    valid_norms = [x for x in normalized if x > 0]
    entropy_values = [-p * __import__('math').log(p) for p in valid_norms]
    total_entropy = sum(entropy_values)

    # Distractor: unused sorting operation
    sorted_normalized = sorted(normalized, reverse=True)
    median_index = len(sorted_normalized) // 2
    median_value = sorted_normalized[median_index]

    # Simulated calibration checksum (irrelevant)
    checksum = 0
    for i, val in enumerate(raw_magnitudes):
        if i % 3 == 0:
            checksum += int(val) & 255
    checksum = checksum % 1000

    # Real aggregation
    high_deviation_count = sum(1 for d in deviations if d > 0.6)
    aggregate_score = int(total_entropy * 100) + high_deviation_count

    # Conditional function definition (relevant)
    def anomaly_detector(entropies):
        base = sum(entropies) * 10
        length_factor = len(entropies) if len(entropies) > 3 else 5
        return int(base) ^ control_mask  # XOR with earlier bit mask

    # Key execution point
    final_diagnostic = aggregate_score + anomaly_detector(entropy_values)
    
    # Output required result
    print(f"Result: {final_diagnostic}")

# Input data
input_readings = [0.12, -5.3, 0.45, 0.67, 0.23, 0.89, -0.15, 0.77, 0.55]
analyze_readings(input_readings)