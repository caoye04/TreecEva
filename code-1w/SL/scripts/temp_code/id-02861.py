def analyze_sensor_data(raw_readings, calibration_table):
    # Irrelevant preprocessing: normalize strings (distractor)
    normalized_labels = [label.strip().lower().replace('_', '-') for label in ['Sensor_A', ' Sensor_B ', 'SENSOR_C']]
    temp_map = {k: v * 0.95 for k, v in calibration_table.items() if v > 50}  # Dead code path

    # Key data structures
    valid_readings = [x for x in raw_readings if 10 <= x <= 150]
    outlier_flags = set()
    for i, val in enumerate(valid_readings):
        if val > 140:
            outlier_flags.add(i)

    # Bit manipulation decoy
    masked_values = []
    for x in valid_readings:
        masked = x ^ 255  # Irrelevant transformation
        scaled = (masked & 127) >> 1
        masked_values.append(scaled)

    # Conditional logic with red herring branches
    if len(valid_readings) > 5:
        base_threshold = sum(valid_readings) / len(valid_readings)
    else:
        base_threshold = 75  # Misleading fallback

    # Dictionary-based adjustment (partially relevant)
    adjustment_map = {i: val * 0.1 for i, val in enumerate(valid_readings)}
    adjusted_readings = [val + adjustment_map[i] for i, val in enumerate(valid_readings)]

    # Real computation begins: statistical moments
    mean_val = sum(adjusted_readings) / len(adjusted_readings)
    variance = sum((x - mean_val) ** 2 for x in adjusted_readings) / len(adjusted_readings)
    std_dev = variance ** 0.5

    # Control flow distraction: unused function definition
    def decrypt_signal(seq):
        return [seq[-i] ^ 3 for i in range(1, len(seq)+1)]  # Never called

    # Set operations with partial relevance
    high_readings = {x for x in adjusted_readings if x > mean_val + std_dev}
    low_readings = {x for x in adjusted_readings if x < mean_val - std_dev}
    overlap_check = high_readings & low_readings  # Always empty - distractor

    # Core calculation chain
    signal_quality = len(high_readings) - len(low_readings)
    stability_index = 100 - (std_dev * 2)

    # Complex conditional expression
    aggregate_score = (stability_index * 0.7) if signal_quality >= 0 else (stability_index * 0.3)

    # Zip usage with filtered alignment
    paired_deltas = [a - b for a, b in zip(valid_readings[1:], valid_readings[:-1])]
    trend_shift = sum(1 for d in paired_deltas if d > 0) - sum(1 for d in paired_deltas if d < 0)

    # Correction factor based on trend and quality
    correction_factor = 0
    if signal_quality > 0:
        correction_factor += trend_shift * 1.5
    if len(outlier_flags) == 0:
        correction_factor += 5.5  # Hidden bonus condition

    # Final computation (target statement)
    final_diagnostic = aggregate_score + correction_factor

    # Unused complex data transformation
    diagnostic_log = [
        {'index': i, 'raw': r, 'adj': a, 'dev': abs(a - mean_val)}
        for i, (r, a) in enumerate(zip(raw_readings, adjusted_readings))
    ]
    summary_tree = {"depth": 3, "nodes": [1,2,3], "value": sum(diag['dev'] for diag in diagnostic_log)}  # Dead end

    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution entry point
readings = [88, 92, 85, 96, 89, 94, 87]
calibration = {'s1': 88, 's2': 92, 's3': 85, 'aux': 40}  # aux intentionally below threshold
result = analyze_sensor_data(readings, calibration)