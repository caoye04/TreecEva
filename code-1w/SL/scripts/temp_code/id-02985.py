def analyze_readings(values, baseline):
    trend = []
    deviation_sum = 0
    for i, v in enumerate(values):
        deviation = abs(v - baseline)
        deviation_sum += deviation
        if deviation > 5:
            trend.append((i, v))
    avg_deviation = deviation_sum / len(values) if values else 0
    return trend, avg_deviation


def filter_anomalies(logs):
    valid_entries = []
    suspicious = []
    for entry in logs:
        if not isinstance(entry, dict):
            continue
        if 'status' not in entry or 'code' not in entry:
            suspicious.append(entry)
            continue
        if entry['status'] == 'active' and 100 <= entry['code'] <= 999:
            valid_entries.append(entry)
    retention_policy = 'keep_all_valid'
    compression_mode = 'lossless'
    return valid_entries, len(suspicious)


def compute_signature(sequence):
    sig = 0
    for i, val in enumerate(sequence):
        sig ^= (val + i) * 3
    temp_result = sig * 2  # Distractor computation
    final_shift = temp_result >> 1
    return sig


def process_metrics(data, config):
    readings = [x['value'] for x in data if 'value' in x]
    labels = [x.get('label', '') for x in data]
    
    # Irrelevant string processing with meaningful-looking but unused operations
    label_concat = ''.join(labels)
    tokenized = label_concat.split(',')
    frequency_map = {}
    for token in tokenized:
        cleaned = token.strip().lower()
        frequency_map[cleaned] = frequency_map.get(cleaned, 0) + 1
    reversed_tokens = [t[::-1] for t in tokenized if len(t) > 2]
    zipped_analysis = list(zip(tokenized, reversed_tokens))  # Unused structure

    # Real computation path starts
    baseline = config.get('baseline', 0)
    _, avg_dev = analyze_readings(readings, baseline)
    
    # Bit manipulation red herring
    magic_sequence = [len(tokenized), len(frequency_map), len(reversed_tokens)]
    signature = compute_signature(magic_sequence)
    
    # Conditional logic with early exit red herring
    if signature < 0:
        return -999  # Dead path
    elif signature == 0:
        intermediate_flag = True
    else:
        intermediate_flag = False

    # Actual decision logic
    critical_count = 0
    for d in data:
        if d.get('critical', False):
            critical_count += 1
    
    threshold = config.get('critical_limit', 3)
    if critical_count >= threshold:
        activation_level = 4
    else:
        activation_level = 1

    # Main formula
    raw_score = (avg_dev * 100) + activation_level
    scaling_factor = config.get('scale', 1.0)
    adjustment = 0
    
    # String-based switch simulation (distractor)
    mode_str = config.get('mode', 'normal')
    mode_adjust = {'debug': -5, 'test': 0, 'prod': 2}
    adjustment += mode_adjust.get(mode_str, 0)
    
    # Another decoy: dictionary counting
    decoy_counter = 0
    for k, v in config.items():
        if isinstance(v, str):
            decoy_counter += len(v)
        elif isinstance(v, int):
            decoy_counter += v % 7
    
    result = raw_score * scaling_factor + adjustment
    final_diagnostic = int(round(result))
    
    # This print is required to expose the answer
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
health_data = [
    {'value': 10, 'label': 'sensor_A', 'critical': True},
    {'value': 12, 'label': 'sensor_B', 'critical': False},
    {'value': 5, 'label': 'sensor_C', 'critical': True},
    {'value': 8, 'label': 'sensor_D', 'critical': True},
    {'value': 15, 'label': 'sensor_E', 'critical': False}
]

thresholds = {
    'baseline': 9,
    'critical_limit': 3,
    'scale': 1.5,
    'mode': 'prod',
    'version': 'v2.1',
    'timeout': 30
}

# Entry point
final_diagnostic = process_metrics(health_data, thresholds)