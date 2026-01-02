import itertools

# System health monitoring simulation with red herrings and complex logic paths
def analyze_subsystem_readings(sensor_data, threshold_config):
    # Irrelevant transformation (distractor)
    normalized = [max(0.0, min(x, 100.0)) for x in sensor_data]
    adjusted = [x * 1.05 if x > 50 else x * 0.95 for x in normalized]  # Misleading adjustment

    # Core logic: find first critical spike above dynamic threshold
    dynamic_threshold = threshold_config['base'] * (1 + threshold_config['variance_factor'])
    critical_spikes = []
    for i in range(1, len(adjusted)):
        if adjusted[i] > dynamic_threshold and adjusted[i-1] < dynamic_threshold:
            critical_spikes.append(i)

    return len(critical_spikes) > 0

# Decoy function – looks important but unused in final calculation
def compute_entropy(signal):
    from math import log
    counts = {}
    for x in signal:
        bucket = int(x // 10)
        counts[bucket] = counts.get(bucket, 0) + 1
    total = len(signal)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Data preprocessing decoy – populates irrelevant variables
def preprocess_logs(raw_entries):
    timestamps = [entry[0] for entry in raw_entries]
    statuses = [entry[1] for entry in raw_entries]
    codes = [entry[2] for entry in raw_entries]
    
    # Fake aggregation (dead code path)
    status_freq = {}
    for s in statuses:
        status_freq[s] = status_freq.get(s, 0) + 1
    
    return {'count': len(raw_entries)}

# Real computational core buried among distractions
def evaluate_stability_indices(indices, window_size=4):
    if len(indices) < window_size:
        return 0.0

    # Valid computation: rolling average of second differences
    first_diffs = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    second_diffs = [first_diffs[i+1] - first_diffs[i] for i in range(len(first_diffs)-1)]
    
    # Only use last complete window
    start_idx = max(0, len(second_diffs) - window_size)
    window = second_diffs[start_idx:start_idx + window_size]
    
    return sum(window) / len(window)

# Main diagnostic chain with multiple layers and decoys
def aggregate_metrics(input_stream, config):
    # Distractor: complex unpacking and irrelevant assignments
    header, *data_payload, footer = input_stream
    metadata_block = header.get('meta', {})
    timestamp_sequence = metadata_block.get('timestamps', list(range(10)))
    
    # Unused but plausible-looking analysis
    _ = compute_entropy(data_payload[0])
    _ = preprocess_logs(list(zip(timestamp_sequence, ['OK']*10, [200]*10)))

    # Key data extraction (hidden among noise)
    primary_signal = [x * config['gain'] for x in data_payload[1] if x >= 0]
    secondary_signal = [x for x in data_payload[2] if x % 2 == 1]  # Filtering odd values only

    # Conditional expression usage (required feature)
    active_mode = 'high' if sum(primary_signal) > 300 else 'low'
    
    # Red herring: elaborate but unused dictionary structure
    system_snapshot = {
        'mode': active_mode,
        'peak': max(primary_signal),
        'baseline_drift': primary_signal[-1] - primary_signal[0],
        'flags': [],
        'diagnostics': {
            'spike_count': sum(1 for i in range(1, len(primary_signal)) if primary_signal[i] - primary_signal[i-1] > 10),
            'noise_floor': min(primary_signal)
        }
    }

    # Real dependency: analyze subsystem using specific config
    fault_detected = analyze_subsystem_readings(
        sensor_data=primary_signal,
        threshold_config={'base': 45, 'variance_factor': 0.1}
    )

    # Critical calculation path (4 levels deep)
    stability_score = 0.0
    if not fault_detected:
        temp_series = []
        for group in itertools.groupby(primary_signal, key=lambda x: x // 10):
            segment_avg = sum(group[1]) / len(list(group[1]))
            temp_series.append(segment_avg)
            
            # Nested distraction
            if segment_avg > 60:
                temp_series.append(segment_avg * 0.5)  # Artificial dampening (misleading)
        
        if len(temp_series) >= 3:
            refined_input = [temp_series[i] - temp_series[i-1] for i in range(1, len(temp_series))]
            if len(refined_input) >= 4:
                stability_score = evaluate_stability_indices(refined_input, window_size=3)
    else:
        stability_score = -999.9  # Fault case (not triggered)

    # Final logic with conditional expression (second required feature)
    calibration_offset = 127 if config.get('secure_mode', False) else 0
    final_diagnostic = int(stability_score * 100) + calibration_offset

    return final_diagnostic

# Execution setup
if __name__ == '__main__':
    # Input construction with meaningful structure
    stream = [
        {'meta': {'version': '2.1', 'timestamps': [1000, 1001, 1002]}},
        [12, 15, 23, 35, 41, 48, 52, 58, 60, 59],  # Scaled by gain=2 → doubles
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],  # Odd filtering → 11,13,15,17,19
        'END'
    ]
    
    config = {
        'gain': 2,
        'secure_mode': True,
        'debug_trace': False  # Unused parameter (distractor)
    }
    
    # Actual answer depends on deep execution path
    final_diagnostic = aggregate_metrics(stream, config)
    print(f"Result: {final_diagnostic}")