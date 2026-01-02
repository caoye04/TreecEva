from collections import defaultdict, Counter

# Simulated sensor network data processing with red herrings
def analyze_sensor_network(raw_logs):
    # Irrelevant preprocessing (distractor)
    temp_offsets = [0.1, -0.3, 0.4, -0.2, 0.05]
    adjusted_logs = [log + temp_offsets[i % len(temp_offsets)] for i, log in enumerate(raw_logs[:10])]
    spike_count = sum(1 for x in adjusted_logs if abs(x) > 0.5)

    # Real filtering logic embedded within noise
    valid_ids = {i for i, val in enumerate(raw_logs) if val > 1.0}
    filtered_data = [raw_logs[i] for i in range(len(raw_logs)) if i in valid_ids]

    # Decoy statistical analysis
    mean_val = sum(raw_logs) / len(raw_logs) if raw_logs else 0
    variance = sum((x - mean_val) ** 2 for x in raw_logs) / len(raw_logs) if raw_logs else 0
    entropy_proxy = -sum(x * x for x in raw_logs)  # Nonsensical but looks meaningful

    # Unused transformation path (dead code)
    def transform_recursive(data, depth=0):
        if depth >= 3 or not data:
            return data
        return transform_recursive([d / 2 for d in data[::2]], depth + 1)

    # Another decoy structure
    stats_summary = defaultdict(lambda: 'unknown')
    stats_summary['spikes'] = spike_count
    stats_summary['entropy'] = round(entropy_proxy, 3)
    stats_summary['normalizations'] = len(temp_offsets)

    # Critical mapping setup buried in noise
    levels = ['low', 'medium', 'high', 'critical']
    threshold_map = defaultdict(int)
    for idx, level in enumerate(levels):
        threshold_map[level] = (idx + 1) * 1.5

    # Red herring: complex bit manipulation on irrelevant metric
    bitmask = 0
    for i in range(len(raw_logs)):
        if i % 3 == 0:
            bitmask ^= (i << 2)
    diagnostic_flag = bitmask & 0xFF

    # Hidden accumulator with real computation mixed in
    accumulation_chain = []
    running_total = 0
    for i, val in enumerate(filtered_data):
        if i % 2 == 0:
            running_total += val * 1.1
        else:
            running_total -= val * 0.9
        accumulation_chain.append(round(running_total, 4))

    # Actual target function defined inside to increase nesting
    def process_readings(data, thresholds):
        base_score = 0
        category_tally = Counter()

        # Real logic: classify and aggregate
        for reading in data:
            if reading < thresholds['low']:
                cat = 'low'
            elif reading < thresholds['medium']:
                cat = 'medium'
            elif reading < thresholds['high']:
                cat = 'high'
            else:
                cat = 'critical'
            category_tally[cat] += 1
            base_score += int(reading * 2)

        # Secondary adjustment based on distribution
        mode_category = category_tally.most_common(1)[0][0] if category_tally else 'none'
        modifier = {
            'low': -5,
            'medium': 2,
            'high': -10,
            'critical': 15
        }[mode_category]

        # Final result built from multiple steps
        intermediate = base_score + modifier
        checksum = sum(i * v for i, v in enumerate(category_tally.values()))
        final_score = intermediate * 3 - checksum

        # Decoy post-processing
        normalized = final_score / (1 + abs(final_score) * 0.01)
        rounded_diag = round(normalized, 6)

        return int(final_score)  # Only this matters

    # Key execution point buried in distractions
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # More irrelevant outputs
    debug_trace = list(zip(valid_ids, filtered_data))
    anomaly_pattern = ''.join('X' if x > 2.0 else '.' for x in raw_logs)

    # This print is required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data crafted to yield deterministic outcome
sensor_input = [0.8, 1.2, 0.9, 1.6, 2.1, 0.7, 1.3, 2.5, 1.1, 0.6, 1.8, 2.3]
analyze_sensor_network(sensor_input)