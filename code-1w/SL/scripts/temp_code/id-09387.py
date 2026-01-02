def analyze_sensor_data():
    # Simulated environmental sensor readings (irrelevant in part)
    temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8]
    humidity_levels = {t: (h * 0.8 + 10) for t, h in enumerate(temperature_readings)}
    pressure_log = set()
    for i in range(len(temperature_readings)):
        pressure_log.add(int(1013 + i * 3 - (i % 2) * 5))

    # Core data processing chain (relevant)
    signal_buffer = [18, 23, 15, 42, 33, 28, 37]
    checksum = 0
    for val in signal_buffer:
        checksum ^= val  # Bitwise XOR accumulation

    # Secondary transformation with distractor path
    temp_map = {}
    for idx, val in enumerate(signal_buffer):
        temp_map[f'idx_{idx}'] = val * 2 - 5 if val > 20 else val + 10  # Partially unused

    # Red herring: complex but unused computation
    outlier_candidates = []
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    for t in temperature_readings:
        if abs(t - avg_temp) > 1.5:
            outlier_candidates.append(t)

    # Key processing path begins
    raw_sequence = [x for x in signal_buffer if x % 2 == 1]  # Filter odd values
    normalized = [x - min(raw_sequence) for x in raw_sequence]  # Normalize to minimum

    # Destructuring and multiple assignments (distraction)
    a, b, *rest = normalized
    offset_correction = a * 2 + b - 3

    # Real computation: combinatorics on filtered set
    combination_count = 0
    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            if (normalized[i] + normalized[j]) % 4 == 0:
                combination_count += 1

    # Dictionary-based weight mapping (only one used)
    weights = {
        'base': 3.5,
        'legacy': 2.1,
        'experimental': 4.0,
        'calibration': 1.8
    }
    
    # Dead code path (never executed)
    debug_mode = False
    if debug_mode:
        print('Tracing deprecated path')
        for k in weights:
            weights[k] *= 0.5

    # Actual critical computation
    base_metric = sum(normalized) * combination_count
    adjustment_factor = weights['base']  # Only this weight matters
    aggregate_score = int(base_metric * adjustment_factor)

    # Refinement via set operations (distracting)
    index_set_a = {i for i in range(len(signal_buffer))}
    index_set_b = {i for i, x in enumerate(signal_buffer) if x > 25}
    overlap_size = len(index_set_a & index_set_b)  # Intersect: red herring

    refinement_factor = len(raw_sequence) + offset_correction  # Used in final step

    # Final diagnostic calculation (target)
    final_diagnostic = aggregate_score // refinement_factor

    # Irrelevant printing (distraction)
    if final_diagnostic > 100:
        status = "STABLE"
    else:
        status = "CAUTION"
    
    # Only this output matters
    return final_diagnostic

result = analyze_sensor_data()
print(f"Target result: {result}")