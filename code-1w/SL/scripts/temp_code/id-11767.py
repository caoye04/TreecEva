def analyze_system_load(raw_data, threshold_config):
    # Irrelevant preprocessing (distractor)
    normalized_data = [x * 1.05 for x in raw_data if x > 0]
    filtered_data = [x for x in normalized_data if x < 1000]
    aggregate_snapshot = sum(filtered_data) / len(filtered_data) if filtered_data else 0

    # Dead code path - never executed due to static condition (red herring)
    legacy_mode = False
    if legacy_mode:
        return {'status': 'inactive', 'value': -999}

    # Real processing begins: extract diagnostic windows
    windows = []
    for i in range(0, len(raw_data) - 4):
        if raw_data[i] % 2 == 0:
            window_avg = sum(raw_data[i:i+5]) / 5
            windows.append(window_avg)

    # Simulate bit manipulation for 'diagnostic signature' (misleading but unused)
    signature = 0
    for val in raw_data[:8]:
        signature ^= int(val) << 1
        signature &= 0xFFFF

    # Actual relevant logic: detect anomalies above threshold
    anomaly_count = 0
    for w in windows:
        if w > threshold_config['load_cap']:
            anomaly_count += 1

    # Conditional expression used (required language feature)
    status_flag = 1 if anomaly_count > threshold_config['anomaly_limit'] else 0

    # Distractor: complex string transformation (unused)
    debug_trace = ''.join(chr(97 + (int(x) % 26)) for x in filtered_data[:10])
    reversed_trace = debug_trace[::-1].upper()  # Case conversion (suggested paradigm)

    # Another red herring: linear search in irrelevant list
    search_list = [3, 7, 19, 31, 43, 67, 79, 97]
    found_index = -1
    for idx, item in enumerate(search_list):  # Linear search (suggested paradigm)
        if item > aggregate_snapshot:
            found_index = idx
            break  # Early break (suggested paradigm)

    # Core result computation (depends on prior steps)
    base_score = len(windows) * 17
    penalty = anomaly_count * 23
    raw_diagnostic = base_score - penalty

    # Final conditional adjustment
    final_diagnostic = raw_diagnostic + (100 if status_flag else -50)

    # Only this print statement matters for output
    return final_diagnostic

def process_metrics(entries, limit):
    # Wrapper that modifies input subtly
    adjusted = [x * 2 for x in entries]
    config = {
        'load_cap': limit,
        'anomaly_limit': 3
    }
    result = analyze_system_load(adjusted, config)
    return result

# Main execution
log_entries = [12, 18, 24, 30, 36, 42, 48, 54, 60]
system_threshold = 45
final_diagnostic = process_metrics(log_entries, system_threshold)
print(f"Target result: {final_diagnostic}")