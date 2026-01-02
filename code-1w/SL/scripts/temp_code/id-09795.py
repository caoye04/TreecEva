def monitor_system_load(base_signal, threshold_factor):
    signal_peaks = []
    noise_floor = 0.1 * base_signal
    temp_buffer = [0] * 5
    for i in range(1, 6):
        adjusted_peak = (base_signal * i) ** 0.5 + noise_floor
        if adjusted_peak > 3 * noise_floor:
            signal_peaks.append(int(adjusted_peak))
        temp_buffer[i-1] = adjusted_peak * 2  
    return signal_peaks


def detect_anomalies(event_log):
    critical_flags = set()
    shadow_copy = event_log.copy()
    for idx, val in enumerate(event_log):
        if val % 7 == 0 and val > 10:
            critical_flags.add(val)
        elif val % 5 == 0:
            critical_flags.discard(val // 2)
    return critical_flags


def compute_stability_index(raw_data):
    cumulative_score = 0
    decay_factor = 0.85
    history_window = []
    for step in range(len(raw_data)):
        if step % 3 == 0:
            cumulative_score += raw_data[step] * decay_factor
        else:
            cumulative_score -= raw_data[step] // 4
        history_window.append(cumulative_score)
    
    temp_analysis = [x for x in history_window if x > 5]
    adjustment_offset = len(temp_analysis) - len(history_window) // 2
    return int(cumulative_score + adjustment_offset)


def extract_signature_sequence(values):
    signature = []
    for v in values:
        if v < 0:
            signature.append(abs(v) % 11)
        elif v > 50:
            signature.append(v // 10)
        else:
            signature.append(v + 3)
    return signature


def analyze_pattern(events, baseline):
    filtered_set = {e for e in events if e > baseline}
    inverse_map = {i: events.count(i) for i in set(events)}
    redundant_counter = 0
    for k in inverse_map:
        if inverse_map[k] > 1:
            redundant_counter += 1
    
    mode_hint = max(inverse_map, key=lambda x: inverse_map[x])
    
    working_stack = []
    for e in events:
        if e in filtered_set:
            working_stack.append(e * 2)
        elif e < baseline:
            working_stack.append(e // 2)
    
    aggregation_key = sum(working_stack) // len(filtered_set) if filtered_set else 0
    
    # Distractor: unused complex structure
    metadata_trace = {
        'version': '2.1',
        'checksum': sum([len(str(x)) for x in events]) * 3,
        'flags': [f"ERR_{i}" for i in range(redundant_counter)]
    }
    
    # Critical red herring calculation
    phantom_score = 0
    for i in range(3):
        phantom_score += (aggregation_key >> i) & 1
    phantom_score *= len(metadata_trace['flags'])
    
    # Actual logic path
    stability_anchor = compute_stability_index(list(filtered_set))
    anomaly_tags = detect_anomalies(events)
    final_adjustment = len(anomaly_tags.intersection(filtered_set))
    
    result = stability_anchor + final_adjustment * 100 - mode_hint
    
    return result

# Irrelevant initialization block
system_status = {'state': 'active', 'uptime': 12345, 'users': 7}
system_status['diagnostics'] = [0] * 4

# Unused helper function (red herring)
def deprecated_calibrate(x):
    return (x * 17) % 13 + 2

# Simulated input data
collected_events = [8, 14, 21, 25, 32, 49, 56, 63, 70]
baseline_threshold = 20

# Key execution point
final_diagnostic = analyze_pattern(collected_events, baseline_threshold)

print(f"Result: {final_diagnostic}")