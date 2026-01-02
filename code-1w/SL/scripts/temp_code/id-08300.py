def monitor_system_health(input_stream, thresholds):
    # Irrelevant signal processing (red herring)
    filtered_data = [x for x in input_stream if x > thresholds.get('noise_floor', 0.1)]
    normalized = [round(x / max(filtered_data), 3) for x in filtered_data]

    # Distractor: unused transformation chain
    transformed = []
    for val in normalized:
        if val > 0.5:
            transformed.append(pow(val, 2) * 1.5)
        else:
            transformed.append(val * 0.8)

    # Real computation begins: detect anomalies above critical threshold
    anomalies = set()
    for i, raw_val in enumerate(input_stream):
        if raw_val > thresholds.get('critical', 90):
            anomalies.add(i % 256)  # Modulo used to limit set growth

    # Secondary path: track recurring patterns (used later)
    pattern_counts = {}
    window_size = 4
    for i in range(len(input_stream) - window_size + 1):
        window = tuple(input_stream[i:i+window_size])
        pattern_counts[window] = pattern_counts.get(window, 0) + 1

    recurring_patterns = {k: v for k, v in pattern_counts.items() if v > 2}
    recurring_signals = set(recurring_patterns.keys())  # Convert to set for analysis

    # Dead code path: simulates calibration but unused
    def calibrate_sensors(data):
        return [d * 0.99 for d in data if d < 100]

    baseline = [x for x in input_stream if x < 70]
    avg_baseline = sum(baseline) / len(baseline) if baseline else 0

    # Unused diagnostic flags
    flag_codes = {
        'F1': False,
        'F2': True and len(anomalies) > 5,
        'F3': False
    }

    # System log built with selective entries (some relevant)
    system_log = []
    for idx, entry in enumerate(input_stream):
        if idx in anomalies and idx % 3 == 0:
            system_log.append(f'ERR_{idx}_{entry}')

    # Key recursive helper (simple recursion)
    def count_nested_patterns(pattern_set, depth=0):
        if depth >= 3 or not pattern_set:
            return depth
        new_patterns = set()
        for pat in pattern_set:
            if len(pat) >= 2 and pat[0] == pat[-1]:
                shifted = pat[1:-1]
                if len(shifted) >= 2:
                    new_patterns.add(shifted)
        return count_nested_patterns(new_patterns, depth + 1)

    # Decoy function that looks important but isn't called
    def compute_stability_index(log_entries):
        errors = [e for e in log_entries if 'ERR' in e]
        if not errors:
            return 100.0
        positions = [int(e.split('_')[1]) for e in errors]
        return sum(positions) / len(positions)

    # Actual fault analyzer
    def analyze_faults(patterns, log):
        # Use set operations: intersection across multi-element tuples
        common_elements = set()
        for p in patterns:
            common_elements.update(set(p))

        # Filter log-based indices
        log_indices = set()
        for record in log:
            try:
                idx = int(record.split('_')[1])
                log_indices.add(idx)
            except:
                continue

        # Combine two sources of indices
        fused_indices = anomalies.union(log_indices)

        # Final computation: weighted impact score
        base_score = len(common_elements) * 17
        adjustment = sum(fused_indices) % 19
        recursion_depth = count_nested_patterns(patterns)

        # Critical distraction: multiple similar variables
        temp_diagnostic = base_score + adjustment
        interim_result = temp_diagnostic * recursion_depth
        final_diagnostic = interim_result - (len(thresholds) * 100)

        return int(final_diagnostic)

    # Execution point of interest
    final_diagnostic = analyze_faults(recurring_signals, system_log)
    print(f"Result: {final_diagnostic}")

# Input data
sensor_stream = [102, 45, 67, 102, 88, 103, 45, 67, 102, 91, 103, 45, 67, 102, 95, 103, 45, 67, 102, 103]
system_thresholds = {'critical': 90, 'warning': 75, 'noise_floor': 5, 'calibration': 0.95}

# Run simulation
monitor_system_health(sensor_stream, system_thresholds)