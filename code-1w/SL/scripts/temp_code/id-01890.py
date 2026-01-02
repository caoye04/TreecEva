import itertools

# Simulated sensor array diagnostics with noise filtering and mode analysis
def analyze_sensor_modes(readings):
    modes = {}
    for sensor_id, data in readings.items():
        frequency = len([x for x in data if x > 0])
        avg_val = sum(data) / len(data) if data else 0
        modes[sensor_id] = {'freq': frequency, 'avg': avg_val, 'active': frequency > 2}
    return modes

# Irrelevant auxiliary function: signal smoothing (not used in final path)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Secondary validation check (dead code path - never called)
def validate_calibration(sequence):
    return all(x % 2 == 0 for x in sequence if x > 0)

# Core processing pipeline
def filter_anomalies(raw_samples, baseline):
    result = []
    for sample in raw_samples:
        adjusted = [val - baseline[i % len(baseline)] for i, val in enumerate(sample)]
        if sum(abs(x) for x in adjusted) < 150:
            result.append(adjusted)
    return result

# Misleading aggregation function (used to create decoy variables)
def compute_health_score(metrics):
    score = 0
    for m in metrics:
        if m['critical']:
            score += 10
        elif m['warning']:
            score += 3
    return max(0, 100 - score)  # Not actually used

# Key function that contributes to final answer
def extract_critical_indices(data_stream):
    indices = set()
    for idx, entry in enumerate(data_stream):
        if isinstance(entry, list) and sum(entry) > 40:
            indices.add(idx)
    return indices

# Main processing logic
def process_readings(data_chunk, thresholds):
    temp_results = []
    running_total = 0

    # Decoy variables with plausible but irrelevant calculations
    decoy_normalization = 0.87
    artifact_mask = [i ** 2 for i in range(12) if i % 3 != 0]
    shadow_buffer = list(itertools.accumulate([2, 4, 1, 8, 5]))  # Unused accumulation

    # Real processing begins
    for segment in data_chunk:
        segment_sum = sum(abs(x) for x in segment)
        cap = thresholds.get('cap_limit', 200)
        if segment_sum > cap:
            truncated = [x for x in segment if abs(x) < 50]
            temp_results.append(truncated)
        else:
            temp_results.append(segment)

    # Merging results with slicing and flattening
    flat_temp = list(itertools.chain.from_iterable(temp_results))
    trimmed_view = flat_temp[::2]  # Every second element

    # Real computation branch
    high_freq_vals = [v for v in trimmed_view if abs(v) > 25]
    aggregated = sum(high_freq_vals) if high_freq_vals else 0

    # Additional distractor: unused statistical calculation
    mean_decoy = sum(flat_temp) / len(flat_temp) if flat_temp else 0
    outlier_set = {x for x in flat_temp if x > 30 or x < -30}
    cardinality_offset = len(outlier_set) * 2  # Looks important, not used

    # Final calculation using correct path
    scale_factor = thresholds.get('scale', 1.75)
    adjustment = len(trimmed_view) - len(high_freq_vals)
    running_total += int((aggregated * scale_factor) - adjustment)

    # Critical red herring: early return that looks plausible but is bypassed
    # if running_total < 0: return running_total + 100  # Commented out - misleading

    # Actual final transformation
    diagnostic_weight = len([x for x in flat_temp if x > 0])
    final_diagnostic = running_total + (diagnostic_weight * 3)

    return final_diagnostic

# Simulated input data
sensor_inputs = {
    'A1': [12, -5, 8, 19, 4],
    'B2': [3, 17, 22, 4, 9, 11],
    'C3': [6, -8, 1, 33, 14, 7],
    'D4': [19, 2, 5, 8]
}

baseline_correction = [3, 7, 1, 4]

raw_data_batch = [
    [28, -12, 45, 7, 19],
    [11, 33, -8, 27, 14],
    [41, 9, 16, -22, 38],
    [13, 29, 5, 17, 21]
]

# Dead assignment - looks like configuration but partially unused
threshold_map = {
    'cap_limit': 105,
    'scale': 1.75,
    'tolerance': 0.05,
    'buffer_size': 8
}

# Irrelevant pre-processing step (creates illusion of complexity)
mode_analysis = analyze_sensor_modes(sensor_inputs)
valid_ids = [sid for sid, m in mode_analysis.items() if m['active']]

# Real data flow initiation
filtered_data = filter_anomalies(raw_data_batch, baseline_correction)

# Extract indices that seem important but are only used for distraction
critical_positions = extract_critical_indices(filtered_data)
decoys_removed = [filtered_data[i] for i in range(len(filtered_data)) if i not in {1, 3}]

# Final execution point
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")