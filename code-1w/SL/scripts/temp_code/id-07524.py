def analyze_events(event_log):
    event_counts = {}
    severity_map = {'info': 1, 'warn': 2, 'error': 3, 'critical': 4}
    temporal_weights = []

    for entry in event_log:
        tag = entry.split()[0].lower()
        timestamp_str = entry.split(',')[0].split()[-1]
        time_weight = sum(int(x) for x in timestamp_str.split(':')) % 7
        temporal_weights.append(time_weight)

        if tag in severity_map:
            event_counts[tag] = event_counts.get(tag, 0) + 1

    # Irrelevant transformation - red herring
    weighted_scores = {k: v * (severity_map[k] ** 0.5) for k, v in event_counts.items()}
    avg_weight = sum(temporal_weights) / len(temporal_weights) if temporal_weights else 0

    # Dead code path - never used
    def legacy_adjustment(x):
        return (x + 10) // 3 * 2

    # Misleading aggregation
    phantom_total = 0
    for i in range(len(temporal_weights)):
        if i % 3 == 0:
            phantom_total += temporal_weights[i] * 2

    return event_counts, avg_weight


def compute_baseline(reference_data):
    total_chars = sum(len(item) for item in reference_data)
    char_freq = {}
    for item in reference_data:
        for c in item:
            char_freq[c] = char_freq.get(c, 0) + 1

    # Unused but plausible computation
    entropy = 0
    for count in char_freq.values():
        p = count / total_chars
        if p > 0:
            entropy -= p * __import__('math').log2(p)

    # Red herring: complex but unused result
    normalized_freq = {k: round(v / total_chars, 4) for k, v in char_freq.items()}

    return total_chars  # Only this is actually used


def filter_anomalies(raw_readings):
    filtered = []
    thresholds = {'temp': 75, 'pressure': 110, 'vibration': 8}
    units = ['C', 'psi', 'mm/s']

    for reading in raw_readings:
        parts = reading.replace(':', ',').replace('-', ',').split(',')
        sensor_type = parts[0].strip()
        try:
            value = float(parts[1])
        except:
            continue

        if sensor_type in thresholds and value > thresholds[sensor_type]:
            filtered.append(f'{sensor_type}:{value}')

    # Distractor: creates list but not central to final answer
    alert_codes = [f'A{idx+1}' for idx in range(len(filtered))]

    return len(filtered)


def process_metrics(summary_dict, flags_list):
    base_score = 0
    if 'error' in summary_dict:
        base_score += summary_dict['error'] * 10
    if 'critical' in summary_dict:
        base_score += summary_dict['critical'] * 25

    modifier = 1.0
    flag_values = []

    for f in flags_list:
        if f.startswith('SEC'):
            flag_values.append(3)
        elif f.isdigit():
            flag_values.append(int(f) % 5)
        else:
            flag_values.append(1)

    if flag_values:
        modifier = sum(flag_values) / len(flag_values)

    # Key calculation step
    adjusted_score = int(base_score * modifier)

    # Multiple decoy operations
    temp_result = adjusted_score ^ 1234
    temp_result = temp_result & (adjusted_score + 512)

    # Final relevant assignment
    final_diagnostic = adjusted_score + 50000

    # Unused derived values - misleading
    consistency_check = (final_diagnostic % 97) == 0
    audit_trace = bin(final_diagnostic ^ 0xF0F0)

    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    logs = [
        'ERROR, 14:22:05, Disk write failure on node 3',
        'CRITICAL, 14:23:11, Memory overflow in primary buffer',
        'WARN, 14:24:03, High latency detected on channel 2',
        'ERROR, 14:25:44, Checksum mismatch in packet stream',
        'CRITICAL, 14:26:19, System clock desynchronization',
        'INFO, 14:27:01, Heartbeat signal received'
    ]

    config_data = [
        'MAX_RETRIES:3',
        'TIMEOUT-15',
        'RECONNECT_DELAY:2',
        'BUFFER_SIZE-8192'
    ]

    sensor_inputs = [
        'temp:85',
        'humidity:45',
        'pressure:115',
        'vibration:9',
        'temp:65'
    ]

    # Irrelevant pre-processing steps
    log_analysis = analyze_events(logs)
    log_summary = log_analysis[0]  # Extract event counts
    system_baseline = compute_baseline(config_data)
    anomaly_count = filter_anomalies(sensor_inputs)

    # Critical flags with mixed types - some relevant, some distracting
    system_flags = ['SECURE_BOOT', 'DEBUG_OFF', '7', 'TRACE_MODE', 'SEC_LVL_2', '9']

    # Key statement
    final_diagnostic = process_metrics(log_summary, system_flags)

    print(f'Target result: {final_diagnostic}')