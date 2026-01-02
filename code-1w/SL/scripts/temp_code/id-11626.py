from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 78, 'errors': 2, 'timestamp': 1001},
    {'node': 'B', 'load': 45, 'errors': 0, 'timestamp': 1002},
    {'node': 'C', 'load': 93, 'errors': 5, 'timestamp': 1003},
    {'node': 'A', 'load': 81, 'errors': 1, 'timestamp': 1004},
    {'node': 'B', 'load': 67, 'errors': 3, 'timestamp': 1005},
    {'node': 'C', 'load': 88, 'errors': 0, 'timestamp': 1006},
    {'node': 'D', 'load': 33, 'errors': 1, 'timestamp': 1007},
    {'node': 'D', 'load': 55, 'errors': 4, 'timestamp': 1008}
]

# Irrelevant red-herring data
historical_baselines = {
    'Q1_avg': 61.3, 'Q2_avg': 59.8, 'Q3_avg': 64.1, 'Q4_avg': 70.2,
    'maintenance_windows': [(15, 18), (47, 50), (88, 91)],
    'peak_loads': [94, 87, 91, 85]
}

# Misleading auxiliary function (never called)
def calculate_reliability_index(events):
    uptime = sum(1 for e in events if e['errors'] == 0)
    return uptime / len(events) if events else 0

# Another decoy: unused transformation
normalization_map = {i: round(math.log(i + 1), 3) for i in range(100)}

# Core processing variables
data_log = defaultdict(list)
error_flags = []
consistency_check = True

# Populate data log from stream
for entry in telemetry_stream:
    data_log[entry['node']].append({
        'load': entry['load'],
        'err': entry['errors'],
        'ts': entry['timestamp']
    })
    if entry['errors'] > 3:
        error_flags.append(entry['node'])

# Unused intermediate (red herring)
avg_load_per_node = {
    node: sum(rec['load'] for rec in records) / len(records)
    for node, records in data_log.items()
}

# Distractor: complex but unused analysis
cross_node_correlation = []
for i in range(len(telemetry_stream) - 1):
    curr, next_val = telemetry_stream[i], telemetry_stream[i+1]
    if abs(curr['load'] - next_val['load']) > 40:
        cross_node_correlation.append((curr['node'], next_val['node']))

# Configuration with plausible defaults
config = {
    'threshold': 85,
    'weight_factor': 0.85,
    'penalty_rate': 1.75,
    'activation_key': 'dynamic_scale'
}

# Simulated hardware constraints (unused)
hardware_limits = [85, 90, 95]
overload_buffer = list(filter(lambda x: x > 80, [v['load'] for v in telemetry_stream]))

# Main processing function
def process_metrics(log, settings):
    raw_scores = []
    penalty_accum = 0
    node_contributions = defaultdict(float)

    # First pass: compute base performance scores
    for node, readings in log.items():
        total_load = sum(r['load'] for r in readings)
        error_count = sum(r['err'] for r in readings)
        reading_count = len(readings)

        base_score = total_load / reading_count if reading_count else 0
        normalized_score = base_score * settings['weight_factor']

        # Apply penalty if error rate exceeds threshold
        error_ratio = error_count / reading_count if reading_count else 0
        if error_ratio > 0.1:
            penalty_accum += error_count * settings['penalty_rate']

        # Conditional activation based on config key
        if settings['activation_key'] == 'dynamic_scale':
            adjusted_score = normalized_score * (1 + 0.1 * (reading_count - 1))
        else:
            adjusted_score = normalized_score

        raw_scores.append(adjusted_score)
        node_contributions[node] = adjusted_score

    # Compute final efficiency score
    aggregate = sum(raw_scores)
    final_penalty = math.ceil(penalty_accum)
    efficiency_score = int(aggregate - final_penalty)

    # Dead code branch (never reached due to structure)
    if False:
        fallback = Counter([r['node'] for r in telemetry_stream])
        efficiency_score = max(efficiency_score, sum(fallback.values()))

    # Return multiple values; only first used
    return efficiency_score, node_contributions, final_penalty

# Execute main logic
final_output = process_metrics(data_log, config)
efficiency_score = final_output[0]

# Print result as required
print(f"Result: {efficiency_score}")