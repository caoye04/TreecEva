def analyze_events(raw_data, filters):
    event_count = 0
    temp_accum = {}
    for item in raw_data:
        key = item['type']
        if key not in temp_accum:
            temp_accum[key] = 0
        temp_accum[key] += 1
        event_count += 1

    filtered_results = {k: v for k, v in temp_accum.items() if k in filters}
    return filtered_results, event_count


def compute_checksum(data_list):
    # Irrelevant checksum function (dead code path)
    checksum = 0
    for entry in data_list:
        for char in str(entry):
            checksum ^= ord(char) % 7
    return checksum


def generate_sequence(n):
    # Distractor: generates Fibonacci-like sequence but unused
    seq = [1, 1]
    for i in range(2, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq


def evaluate_health_status(metrics, baseline):
    score = 0
    decay_factor = 0.95
    for i, (name, value) in enumerate(sorted(metrics.items()), start=1):
        if name in baseline:
            diff = abs(value - baseline[name])
            penalty = diff * (decay_factor ** i)
            score += penalty
    return round(score, 6)


def process_metrics(entries, thresholds):
    # Core logic hidden among distractors
    severity_map = {}
    total_load = 0
    critical_flags = []
    timestamp_index = {}

    # Real processing begins
    for idx, entry in enumerate(entries):
        category = entry['category']
        load = entry['load']
        status = entry['status']
        timestamp = entry['timestamp']

        if category not in severity_map:
            severity_map[category] = 0

        if status == 'ERROR':
            severity_map[category] += 3
        elif status == 'WARNING':
            severity_map[category] += 1

        total_load += load
        timestamp_index[timestamp] = idx

        if load > thresholds.get(category, 100):
            critical_flags.append((idx, load))

    # Real computation using dictionary and zip
    ranked_categories = sorted(severity_map.keys())
    severities = [severity_map[k] for k in ranked_categories]
    normalized = [s / (total_load or 1) * 100 for s in severities]

    # Use of enumerate and zip
    adjustment = 0
    for i, (cat, norm_val) in enumerate(zip(ranked_categories, normalized)):
        if i % 2 == 0:
            adjustment += norm_val * 0.1
        else:
            adjustment -= norm_val * 0.05

    # Final diagnostic calculation
    base_diagnostic = sum(severities)
    adjustment = round(adjustment, 4)
    final_diagnostic = int(base_diagnostic * 100 + adjustment)

    # Dead code: unused intermediate
    decoy_aggregate = 0
    for flag in critical_flags:
        decoy_aggregate += flag[1] * 0.1
    decoy_aggregate = int(decoy_aggregate // 1)

    return final_diagnostic

# Main execution data
log_entries = [
    {'timestamp': '2023-06-01T10:00:00', 'category': 'NETWORK', 'load': 85, 'status': 'OK'},
    {'timestamp': '2023-06-01T10:01:00', 'category': 'STORAGE', 'load': 110, 'status': 'WARNING'},
    {'timestamp': '2023-06-01T10:02:00', 'category': 'NETWORK', 'load': 95, 'status': 'ERROR'},
    {'timestamp': '2023-06-01T10:03:00', 'category': 'COMPUTE', 'load': 120, 'status': 'ERROR'},
    {'timestamp': '2023-06-01T10:04:00', 'category': 'STORAGE', 'load': 90, 'status': 'OK'},
    {'timestamp': '2023-06-01T10:05:00', 'category': 'COMPUTE', 'load': 130, 'status': 'WARNING'},
    {'timestamp': '2023-06-01T10:06:00', 'category': 'NETWORK', 'load': 140, 'status': 'ERROR'}
]

system_thresholds = {
    'NETWORK': 130,
    'STORAGE': 100,
    'COMPUTE': 115
}

# Irrelevant preprocessing
filter_set = ['ERROR', 'WARNING']
raw_event_data = [{'type': e['status'], 'val': e['load']} for e in log_entries]
analyze_events(raw_event_data, filter_set)

# Unused sequence generation
sequence = generate_sequence(10)

# Unused checksum
ids = [str(e['load']) for e in log_entries]
compute_checksum(ids)

# Actual target execution
final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Target result: {final_diagnostic}")