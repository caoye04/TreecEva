import itertools

def monitor_sensor_array(raw_readings, filter_mask, history_log):
    active_segments = []
    temp_cache = {}
    cumulative_energy = 0
    spike_count = 0

    for idx, reading in enumerate(raw_readings):
        if idx % 5 == 0:
            history_log.append(f'Snapshot-{idx}: {reading}')

        filtered_data = [x for x in reading if x & filter_mask > 0]
        segment_power = sum(x ** 0.5 for x in filtered_data) / (len(filtered_data) + 1e-8)

        if segment_power > 12.5:
            spike_count += 1
            active_segments.append((idx, segment_power))

        energy_contrib = sum(itertools.starmap(lambda a, b: (a + b) // 2, zip(filtered_data[:-1], filtered_data[1:])))
        cumulative_energy += energy_contrib

    efficiency_ratio = cumulative_energy / (spike_count + 1)
    return active_segments, efficiency_ratio, spike_count


def compute_entropy(signal_sequence):
    from math import log2
    freq_map = {}
    total = len(signal_sequence)
    for val in signal_sequence:
        freq_map[val] = freq_map.get(val, 0) + 1
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)


def validate_checksum(encoded_stream):
    # Irrelevant validation routine (dead-end)
    checksum = 0
    for byte in encoded_stream:
        checksum ^= byte ^ 0xFF
    return checksum == 0xAB


def analyze_pattern(signals, threshold):
    flat_signal = list(itertools.chain.from_iterable(signals))
    signal_stats = {
        'mean': sum(flat_signal) / len(flat_signal),
        'max': max(flat_signal),
        'min': min(flat_signal)
    }

    # Distractor block: unused transformation
    normalized = [(x - signal_stats['min']) / (signal_stats['max'] - signal_stats['min'] + 1e-8) for x in flat_signal]
    discretized = [int(n * 7) for n in normalized]

    # Key logic hidden among distractors
    pattern_runs = 0
    for i in range(1, len(discretized)):
        if discretized[i] == discretized[i-1]:
            pattern_runs += 1

    # Real computation path
    unique_values = set(flat_signal)
    distinct_peaks = sum(1 for v in unique_values if v > signal_stats['mean'] and v % 3 == 1)

    # Critical intermediate with misleading name
    shadow_metric = len([v for v in flat_signal if v in unique_values and v % 4 == 0])

    # Actual answer computation
    diagnostic_score = len(flat_signal) // (len(unique_values) or 1)
    adjustment_factor = 1 + (0.1 * pattern_runs)

    final_diagnostic = int((diagnostic_score * adjustment_factor) - shadow_metric + distinct_peaks)

    # Dead code path: never used
    if final_diagnostic < 0:
        fallback = compute_entropy(flat_signal)
        final_diagnostic = int(fallback * 100)

    return final_diagnostic

# Simulated sensor data
raw_data = [
    [12, 15, 18, 21, 9],
    [14, 16, 15, 12, 11],
    [19, 23, 25, 24, 20],
    [17, 13, 16, 19, 22],
    [21, 20, 18, 16, 14]
]

# Unused variables (distractors)
baseline_reference = [10, 12, 14, 13, 11]
calibration_curve = {i: i*1.05 for i in range(5)}
system_flags = {'active': True, 'mode': 'diagnostic', 'version': 3}

# Log array for irrelevant snapshots
log_archive = []

# Primary processing pipeline
segments, efficiency, spikes = monitor_sensor_array(raw_data, filter_mask=0b1111, history_log=log_archive)

# Dummy stream for checksum (decoy)
dummy_stream = [0xC3, 0x12, 0x45, 0x67, 0x89]
valid_checksum = validate_checksum(dummy_stream)

# Signal collection for analysis
collected_signals = []
for group in raw_data:
    processed_group = [val + 2 for val in group]
    collected_signals.append(processed_group)

system_threshold = 15

# Core execution point
final_diagnostic = analyze_pattern(collected_signals, system_threshold)

print(f"Result: {final_diagnostic}")