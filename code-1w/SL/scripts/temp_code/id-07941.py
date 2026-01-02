def analyze_system_load(raw_data, threshold_config):
    # Irrelevant preprocessing (distractor)
    sanitized_data = [x.strip() for x in raw_data if x.strip()]
    filtered_data = []

    # Misleading data transformation
    temp_aggregates = {}
    for entry in sanitized_data:
        if 'ERROR' in entry:
            key = entry.split('|')[1].strip()
            temp_aggregates[key] = temp_aggregates.get(key, 0) + 1

    # Dead code path - never executed due to condition
    if len(temp_aggregates) > 100:
        backup_snapshot = {k: v for k, v in temp_aggregates.items()}
        for k in backup_snapshot:
            backup_snapshot[k] *= 2

    # Core processing begins here
    log_entries = []
    for line in raw_data:
        parts = line.split('|')
        if len(parts) == 4:
            try:
                timestamp = int(parts[0])
                cpu_load = float(parts[1])
                mem_usage = float(parts[2])
                disk_io = float(parts[3])
                log_entries.append((timestamp, cpu_load, mem_usage, disk_io))
            except ValueError:
                continue

    # Secondary irrelevant computation on same data
    anomaly_flags = []
    for _, cpu, mem, io in log_entries:
        score = (cpu * 0.6) + (mem * 0.3) + (io * 0.1)
        if score > 85.0:
            anomaly_flags.append(True)
        else:
            anomaly_flags.append(False)

    # Unused function - red herring
    def compute_entropy(data_list):
        from math import log
        freq = {}
        for item in data_list:
            freq[item] = freq.get(item, 0) + 1
        total = len(data_list)
        entropy = 0.0
        for count in freq.values():
            p = count / total
            entropy -= p * log(p)
        return entropy

    # Real logic starts: extract high-frequency metrics above threshold
    high_load_windows = list(filter(lambda x: x[1] > threshold_config['cpu'] and x[2] > threshold_config['mem'], log_entries))

    # Decoy aggregation with no effect on final result
    decoy_sum = 0
    for window in high_load_windows:
        decoy_sum += window[3] * 0.01
        decoy_sum = round(decoy_sum, 3)

    # Key transformation using tuple unpacking and destructuring
    def process_metrics(entries, config):
        base_factor = config['base']
        multiplier = config['mult']
        shift = config['shift']

        # Extract timestamps and compute time deltas
        timestamps = [entry[0] for entry in entries]
        if len(timestamps) < 2:
            return base_factor

        time_gaps = []
        for i in range(1, len(timestamps)):
            gap = timestamps[i] - timestamps[i - 1]
            if gap > 0:
                time_gaps.append(gap)

        # Compute harmonic mean of gaps (resistant to outliers)
        if not time_gaps:
            return base_factor + shift

        reciprocal_sum = sum(1.0 / gap for gap in time_gaps)
        harmonic_mean = len(time_gaps) / reciprocal_sum

        # Apply modular arithmetic to simulate cyclical load pattern
        cycle_phase = int(harmonic_mean) % 7
        adjustment = (cycle_phase * 3) ^ 5  # Bitwise XOR for obfuscation

        # Final calculation path
        raw_metric = harmonic_mean * multiplier
        intermediate = int(raw_metric) + adjustment
        final_score = (intermediate + shift) * base_factor

        # Additional irrelevant bit manipulation
        mask = 0b101010
        masked = final_score & mask
        flipped = final_score ^ 0xFFFF
        decoy_combine = (masked << 3) | (flipped >> 12)

        # Only final_score contributes to output
        return final_score

    # Threshold configuration with misleading extra keys
    system_threshold = {
        'cpu': 75.0,
        'mem': 80.0,
        'disk': 90.0,
        'base': 4,
        'mult': 1.75,
        'shift': 6
    }

    # Critical assignment point
    final_diagnostic = process_metrics(log_entries, system_threshold)

    # Unrelated cleanup operation
    del temp_aggregates['dummy_key'] if 'dummy_key' in temp_aggregates else None

    # Output target result
    print(f"Result: {final_diagnostic}")

# Simulated input data
input_logs = [
    "1000|76.2|81.5|40.1",
    "1005|77.1|82.3|41.0",
    "1012|78.0|83.0|42.5",
    "1020|79.5|84.1|43.2",
    "1029|80.2|85.0|44.0",
    "1039|81.0|86.2|45.1"
]

# Execute main analysis
analyze_system_load(input_logs, {'cpu': 75.0, 'mem': 80.0})