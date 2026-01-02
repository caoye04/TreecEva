def analyze_sensor_stream(raw_samples, config_params):
    # Irrelevant preprocessing block (dead path)
    if len(raw_samples) == 0:
        return -999  # Dead code; dataset always non-empty

    # Distractor: complex but unused transformation
    scaled_buffer = [x * 1.05 for x in raw_samples if x > 0]
    reversed_copy = scaled_buffer[::-1]
    cumulative_shift = 0
    for idx, val in enumerate(reversed_copy):
        cumulative_shift += val % (idx + 1) if idx % 2 == 0 else 0

    # Real data pipeline begins
    valid_entries = []
    for sample in raw_samples:
        if -100 < sample < 1000:  # Valid range filter
            valid_entries.append(sample)

    # Secondary filtering based on index parity and magnitude
    indexed_pairs = list(enumerate(valid_entries))
    filtered_data = []
    for i, val in indexed_pairs:
        if i % 2 == 0 and val > 50:
            filtered_data.append(val)
        elif i % 3 == 0 and val < 200:
            filtered_data.append(val * 0.5)  # Partial inclusion with transform

    # Decoy statistical computation (never used)
    mean_value = sum(valid_entries) / len(valid_entries)
    variance_proxy = sum((x - mean_value) ** 2 for x in valid_entries) / len(valid_entries)
    outlier_flags = [abs(x - mean_value) > 2 * variance_proxy**0.5 for x in valid_entries]

    # Threshold logic setup (only this matters)
    base_threshold = config_params.get('base', 75)
    dynamic_boost = len([x for x in filtered_data if x > base_threshold]) * 1.5
    upper_limit = base_threshold + dynamic_boost

    threshold_map = {
        'low': base_threshold * 0.8,
        'high': upper_limit,
        'critical': upper_limit * 1.2
    }

    # Actual result computation
    final_diagnostic = process_readings(filtered_data, threshold_map)
    return final_diagnostic


def process_readings(data_list, limits):
    # Unused intermediate calculation (distractor)
    zipped_view = list(zip(data_list, [x*0.9 for x in data_list]))
    normalized = [min(x, limits['high']) for x in data_list]

    # Core logic masked by noise
    high_count = 0
    critical_sum = 0.0
    for val in data_list:
        if limits['low'] < val <= limits['high']:
            high_count += 1
        if val > limits['critical']:
            critical_sum += val

    # Final diagnostic score
    stability_index = len(data_list) * 10
    fluctuation_penalty = int(critical_sum / 100) if critical_sum > 0 else 0
    adjustment_factor = 1 if high_count > 3 else 0.8

    # Key assignment
    final_diagnostic = int((stability_index - fluctuation_penalty) * adjustment_factor)

    # Red herring: alternate path never taken
    if len(data_list) > 100:
        backup_score = sum(data_list) // 100
        final_diagnostic = backup_score  # Not triggered

    return final_diagnostic

# Simulated sensor input (deterministic)
data_stream = [120, 45, 88, 155, 67, 210, 92, 33, 177, 144, 58, 191]
settings = {'base': 80}

# Execution entry point
result = analyze_sensor_stream(data_stream, settings)
print(f"Target result: {result}")