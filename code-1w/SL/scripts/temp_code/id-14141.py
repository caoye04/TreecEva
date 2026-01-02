def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant preprocessing: normalize readings (not actually used in final path)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in raw_readings if x > thresholds[0]]

    # Distractor: complex but unused transformation chain
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 2 == 0:
            transformed.append(val ** 0.5 * (i + 1))
        else:
            transformed.append(val / (i + 1) + 2)

    # Dead code path: never executed due to prior condition
    auxiliary_cache = {}
    if len(thresholds) > 10:
        for idx, t in enumerate(thresholds):
            auxiliary_cache[idx] = t * 2.5 + idx

    # Real logic begins: extract peaks above threshold
    peak_values = []
    for i in range(1, len(raw_readings) - 1):
        if raw_readings[i] > thresholds[1] and raw_readings[i] > raw_readings[i-1] and raw_readings[i] > raw_readings[i+1]:
            peak_values.append(raw_readings[i])

    # Secondary distractor: string-based metadata parsing (unused)
    metadata = "sensor_v3_calibrated_unit7"
    parts = metadata.split('_')
    version = parts[1]  # v3
    unit_id = int(parts[-1])  # 7
    temp_offset = sum(ord(c) for c in version) / unit_id

    # Actual core accumulation logic
    cumulative_energy = 0
    for val in raw_readings:
        if val > thresholds[2]:
            cumulative_energy += val * 1.5

    # Intermediate result that looks important but isn't final
    preliminary_index = len(peak_values) * 100 + int(cumulative_energy // 100)

    # Another red herring: recursive function that's called but doesn't affect main flow
    def calculate_entropy(seq, depth=0):
        if depth >= 3 or len(seq) < 2:
            return len(seq)
        mid = len(seq) // 2
        left = seq[:mid]
        right = seq[mid:]
        return calculate_entropy(left, depth + 1) + calculate_entropy(right, depth + 1)

    entropy_estimate = calculate_entropy([int(x) for x in normalized])

    # Key data structure: rolling diagnostics
    rolling_diagnostics = []
    window_size = 3
    for i in range(len(raw_readings) - window_size + 1):
        window = raw_readings[i:i+window_size]
        avg = sum(window) / window_size
        if avg > thresholds[1]:
            rolling_diagnostics.append(avg * 1.1)

    # Real dependency: only this list matters
    stability_scores = []
    for i, score in enumerate(rolling_diagnostics):
        if i % 2 == 0:
            stability_scores.append(score * 0.9)

    # Distractor: tuple unpacking with irrelevant components
    config_defaults = (23.7, 1.05, 42, 'safe')
    base_level, _, override_flag, _ = config_defaults

    # Correction logic using zip and enumerate (required Python features)
    adjustments = [0.1, -0.2, 0.15, -0.05]
    aggregate_metrics = []
    for i, (score, adj) in enumerate(zip(stability_scores, adjustments)):
        adjusted = score + adj * (i + 1)
        aggregate_metrics.append(adjusted)

    # Fallback values that seem like they might be used
    fallback_threshold = sum(thresholds) / len(thresholds) * 0.8
    if not aggregate_metrics:
        aggregate_metrics = [fallback_threshold]

    # Final computation path
    if aggregate_metrics:
        max_metric = max(aggregate_metrics)
        min_metric = min(aggregate_metrics)
        spread = max_metric - min_metric
        safety_margin = 1.8 if spread < 50 else 1.2
        correction_factor = len(peak_values) or 1
        final_diagnostic = aggregate_metrics[-1] + correction_factor * safety_margin
    else:
        final_diagnostic = base_level

    # Unused but plausible-looking diagnostic
    integrity_check = all(x > 0 for x in transformed) and unit_id > 5

    print(f"Result: {final_diagnostic}")

# Inputs
readings = [12, 15, 18, 23, 19, 27, 33, 29, 21, 16, 14, 25, 31, 28, 20]
thresholds_config = [14, 20, 25]

analyze_sensor_data(readings, thresholds_config)