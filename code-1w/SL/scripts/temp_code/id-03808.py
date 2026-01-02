def analyze_component_health(sensor_readings, threshold_map):
    health_flags = {}
    for component, readings in sensor_readings.items():
        avg_reading = sum(readings) / len(readings)
        health_flags[component] = avg_reading < threshold_map.get(component, 75)
    return health_flags


def transform_data_sequence(raw_sequence):
    transformed = [x ** 2 for x in raw_sequence if x % 2 == 0]
    shifted = [x >> 1 for x in transformed]
    return shifted[::-1]

# Irrelevant helper function (dead code path)
def calculate_efficiency_factor(input_stream):
    total = 0
    for val in input_stream:
        if val > 0:
            total += int(val * 0.76) ^ 3
    return total % 19

# Misleading intermediate computation
temp_calibration = sum([i * (i - 1) for i in range(12)]) / 4
offset_matrix = [[j * i for j in range(3)] for i in range(3)]

baseline_config = {
    'response_time': 45,
    'throughput': 80,
    'latency': 50,
    'reliability': 70
}

metrics_log = [
    {'timestamp': '2023-05-01T10:00', 'response_time': 42, 'throughput': 85, 'latency': 48, 'reliability': 72},
    {'timestamp': '2023-05-01T10:05', 'response_time': 46, 'throughput': 78, 'latency': 52, 'reliability': 69},
    {'timestamp': '2023-05-01T10:10', 'response_time': 44, 'throughput': 82, 'latency': 49, 'reliability': 74},
]

# Decoy data structure with plausible but unused values
audit_trail = {
    'user': 'sysadmin',
    'actions': ['init', 'scan', 'verify'],
    'permissions': (2, 1, 3),
    'flags': {k: False for k in ['f1', 'f2', 'f3']}
}

# Core logic buried among distractions
def evaluate_performance(log_entries, config):
    scores = []
    weight_map = {
        'response_time': 0.3,
        'throughput': 0.25,
        'latency': 0.25,
        'reliability': 0.2
    }
    
    # Aggregation across time-series entries
    aggregated = {}
    for key in config.keys():
        aggregated[key] = sum(entry[key] for entry in log_entries) / len(log_entries)
    
    # Compute weighted deviation score (lower is better)
    deviation_score = 0
    for metric, avg_val in aggregated.items():
        target = config[metric]
        weight = weight_map[metric]
        deviation_score += weight * abs(avg_val - target)
    
    # Apply non-linear penalty curve
    penalty_factor = 1 + (deviation_score ** 2) / 100
    
    # Convert to performance score out of 100
    raw_score = 100 - (deviation_score * penalty_factor)
    
    # Slicing operation on irrelevant list (distractor)
    history_buffer = list(range(100, 200, 5))
    snapshot = history_buffer[10:15]
    dummy_sum = sum(snapshot) / len(snapshot)
    
    # Dictionary-based adjustment using version info (red herring)
    system_profile = {'version': '2.1.9', 'mode': 'prod'}
    version_adjust = float(system_profile['version'].split('.')[1])
    
    # Final adjustment - only this matters
    final_normalized = raw_score - version_adjust  # version part '1' -> subtract 1
    
    return int(final_normalized)

# Additional distraction: unused recursive function
def traverse_node_tree(node, depth=0):
    if not node or 'children' not in node:
        return depth
    return max(traverse_node_tree(child, depth + 1) for child in node.get('children', []))

node_structure = {
    'id': 'root',
    'children': [
        {'id': 'A', 'children': [{'id': 'A1'}, {'id': 'A2'}]},
        {'id': 'B', 'children': []}
    ]
}

# Actual execution point of interest
current_state = {'status': 'active', 'stage': 3}
final_score = evaluate_performance(metrics_log, baseline_config)

# Print required output
print(f"Result: {final_score}")