def analyze_sensor_data(raw_readings):
    filtered_data = [x for x in raw_readings if x > 0]
    base_average = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    
    # Simulate auxiliary diagnostics (distractor: not used in final result)
    outlier_count = 0
    temp_flags = []
    for val in raw_readings:
        if val < -50 or val > 150:
            outlier_count += 1
            temp_flags.append(True)
        else:
            temp_flags.append(False)
    
    # Misleading transformation chain (partially irrelevant)
    transformed = []
    shift_key = len(temp_flags) % 7
    for i, val in enumerate(filtered_data):
        shifted = val ^ (shift_key + i)  # Bitwise XOR with index-augmented key
        normalized = (shifted % 100) + 10
        transformed.append(normalized)
    
    # Secondary distraction: simulate calibration lookup
    calibration_map = {i: (i * 0.95) for i in range(1, 51)}
    adjusted_values = [calibration_map.get(x//2, x) for x in transformed if x < 60]
    
    # Core computation begins here
    aggregate_score = 0
    for v in adjusted_values:
        if v > 25:
            aggregate_score += int(v // 3)
        else:
            aggregate_score += int(v * 0.7)
    
    # Red herring state tracking
    state_log = []
    for step in range(3):
        state_log.append(f'Step {step}: Active')
    
    # Another distraction: string-based checksum (unused)
    status_tag = "DIAG_" + "_".join(map(str, temp_flags[:3]))
    checksum = sum(ord(c) for c in status_tag) % 1000

    # Critical point: correction factor derived from modular arithmetic and bit ops
    size_flag = len(filtered_data) & 7  # Bitwise AND to get low-order bits
    modifier = (base_average % 4) * 2.5
    correction_factor = (size_flag ** 2) - modifier

    # Key assignment statement
    final_diagnostic = aggregate_score + correction_factor

    # Output required format
    print(f"Result: {final_diagnostic}")

# Input data (fixed seed-like pattern for determinism)
data_stream = [120, -8, 45, 0, 67, -105, 33, 91, 44, -3, 58]
analyze_sensor_data(data_stream)