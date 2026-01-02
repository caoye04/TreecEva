def process_sensor_array(raw_stream, config_params):
    # Irrelevant pre-processing block (distractor)
    temp_cache = []
    for val in raw_stream:
        if val > 50:
            temp_cache.append(val ** 0.5)
    temp_cache.clear()  # Unused result

    # Core data extraction with slicing and filtering
    time_slice = raw_stream[10:30:2]  # Every 2nd reading from interval
    offset_correction = sum([x // 7 for x in time_slice if x % 3 == 0])

    # Misleading transformation branch (dead path)
    if len(time_slice) > 100:
        normalized = [x / (offset_correction + 1) for x in time_slice]
    else:
        normalized = [x + offset_correction for x in time_slice]  # Actually used

    # Decoy statistical calculation
    avg_val = sum(normalized) / len(normalized)
    peak_noise = max(normalized) - min(normalized)
    entropy_proxy = 0
    for x in normalized:
        if x > avg_val:
            entropy_proxy += 1

    # Conditional data routing (red herring)
    routing_key = config_params.get('mode', 'A')
    if routing_key == 'DEBUG':
        debug_log = [f"{i}:{v}" for i, v in enumerate(normalized)]
        debug_log = None  # Simulate logging, not used

    # Actual relevant path begins here
    filtered_data = [x for x in normalized if x % 2 == 1]  # Only odd values retained

    # Complex threshold map creation with zip and enumerate
    base_levels = config_params['thresholds']
    adjustment_factors = [1.1, 0.9, 1.05, 0.95, 1.0]
    threshold_map = {}
    for i, (level, factor) in enumerate(zip(base_levels, adjustment_factors)):
        adjusted = level * factor
        if i % 2 == 0:
            adjusted = round(adjusted, 1)
        else:
            adjusted = int(adjusted)
        threshold_map[f'sensor_{i}'] = adjusted

    # Another decoy: cumulative shift analysis
    shift_accumulator = 0
    for j in range(len(normalized) - 1):
        diff = abs(normalized[j+1] - normalized[j])
        if diff > 5:
            shift_accumulator += 1

    # Function defined inside to increase nesting and distraction
    def analyze_readings(data, thresholds):
        # Unused diagnostic variables
        sample_trace = []
        outlier_count = 0
        valid_count = 0

        # Real logic: cross-reference with threshold_map keys
        active_sensors = list(thresholds.keys())[:len(data)]
        composite_score = 0

        for idx, reading in enumerate(data):
            # Use of enumerate with zipped auxiliary structure
            sensor_id = active_sensors[idx % len(active_sensors)]
            ref_threshold = thresholds[sensor_id]

            # Bit manipulation red herring
            binary_tag = reading ^ 255
            if binary_tag < 0:
                continue

            # Actual scoring logic
            if isinstance(ref_threshold, int):
                contribution = reading // ref_threshold
            else:
                contribution = int(reading / ref_threshold)

            if contribution > 2:
                valid_count += 1
            else:
                outlier_count += 1

            composite_score += contribution * (idx + 1)  # Weighted by position

        # Final computation chain
        stability_factor = len(data) - abs(valid_count - outlier_count)
        final_score = composite_score * stability_factor

        # Dead code: entropy-based penalty (never applied)
        if 'entropy_penalty' in config_params:
            final_score -= entropy_proxy * config_params['entropy_penalty']

        return final_score

    # Key execution point
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input setup
sensor_input = list(range(40, 68))  # Deterministic input stream
config = {
    'mode': 'OPERATIONAL',
    'thresholds': [10, 15, 20, 25, 30],
    'entropy_penalty': 3  # Present but unused
}

# Execute
process_sensor_array(sensor_input, config)