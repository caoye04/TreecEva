from itertools import combinations, chain

def analyze_component_health(raw_signals, fault_codes):
    # Irrelevant preprocessing (distractor)
    filtered_signals = [x for x in raw_signals if x > -50]
    normalized = [abs(x) ** 0.5 for x in filtered_signals]
    entropy_proxy = sum([n * n for n in normalized[:5]])

    # Critical but obscured logic: count valid fault patterns
    active_faults = [code for code in fault_codes if code % 2 == 1 and code < 500]
    fault_pairs = list(combinations(active_faults, 2))
    critical_count = len([p for p in fault_pairs if (p[0] + p[1]) % 7 == 0])

    # Dead code path (red herring)
    if len(normalized) > 100:
        return -999  # Never reached

    return critical_count


def compute_stability_index(config_matrix):
    # Distractor function: looks important but unused in final result
    total = 0
    for row in config_matrix:
        for val in row:
            total += val % 3
    return total * 1.5


def calculate_load_distribution(nodes):
    # Another red herring: complex but irrelevant
    weights = []
    for node in nodes:
        load = node.get('load', 0)
        priority = node.get('priority', 1)
        weights.append(load * (priority ** 0.3))
    return sum(weights)


def extract_timestamp_groups(entries):
    # Partially relevant but ultimately unused aggregation
    timestamps = [e['ts'] for e in entries if e['level'] == 'ERROR']
    groups = {}
    for ts in timestamps:
        sec = ts // 1000
        groups[sec] = groups.get(sec, 0) + 1
    return {k: v for k, v in groups.items() if v > 2}


def process_metrics(log_entries, thresholds):
    # Core logic buried in distractions
    
    # Misleading early computation
    error_count = sum(1 for e in log_entries if e['level'] == 'ERROR')
    warning_ratio = sum(1 for e in log_entries if e['level'] == 'WARN') / max(len(log_entries), 1)

    # Key data transformation
    severity_scores = []
    for entry in log_entries:
        if entry['component'] in thresholds:
            base_score = entry['value'] * thresholds[entry['component']]
            if entry['flags'] & 0x01:
                base_score *= 1.2
            severity_scores.append(base_score)

    # Accumulation with filtering
    filtered_scores = [s for s in severity_scores if s > 50]
    if not filtered_scores:
        return 0

    # Real answer derived here through non-obvious chain
    avg_severity = sum(filtered_scores) / len(filtered_scores)
    peak = max(filtered_scores)
    score_product = avg_severity * peak

    # Decoy normalization
    normalized_diagnostic = (score_product % 897) + 100

    # Final answer based on discrete condition
    if normalized_diagnostic > 500:
        final_value = int(normalized_diagnostic - 402)
    else:
        final_value = int(normalized_diagnostic + 98)

    return final_value

# Simulated input data
log_entries = [
    {'ts': 1678812000000, 'level': 'INFO', 'component': 'sensor_A', 'value': 45, 'flags': 0x01},
    {'ts': 1678812000100, 'level': 'WARN', 'component': 'sensor_B', 'value': 60, 'flags': 0x00},
    {'ts': 1678812000200, 'level': 'ERROR', 'component': 'sensor_A', 'value': 88, 'flags': 0x01},
    {'ts': 1678812000300, 'level': 'ERROR', 'component': 'sensor_C', 'value': 72, 'flags': 0x01},
    {'ts': 1678812000400, 'level': 'ERROR', 'component': 'sensor_A', 'value': 94, 'flags': 0x01},
    {'ts': 1678812000500, 'level': 'INFO', 'component': 'sensor_B', 'value': 33, 'flags': 0x00},
    {'ts': 1678812000600, 'level': 'ERROR', 'component': 'sensor_C', 'value': 81, 'flags': 0x01},
]

system_thresholds = {
    'sensor_A': 1.8,
    'sensor_B': 1.2,
    'sensor_C': 2.1
}

# Unused data structures (distractors)
config_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
fault_codes = [101, 204, 305, 408, 499, 502]
node_list = [
    {'name': 'n1', 'load': 75, 'priority': 2},
    {'name': 'n2', 'load': 88, 'priority': 3},
    {'name': 'n3', 'load': 62, 'priority': 1}
]
raw_sensor_data = [12, -30, 45, 67, -8, 23, 55, 78, 11, 89]

# Execution of key functions (only one matters)
analyze_component_health(raw_sensor_data, fault_codes)
calculate_load_distribution(node_list)
extract_timestamp_groups(log_entries)

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Target result: {final_diagnostic}")