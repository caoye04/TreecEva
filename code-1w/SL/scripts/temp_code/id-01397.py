from collections import defaultdict, Counter
from itertools import cycle

# Simulated sensor network data with multiple node types
def collect_sensor_data():
    raw_data = [
        {'node': 'A7', 'type': 'temp', 'value': 23.5, 'status': 'active'},
        {'node': 'B4', 'type': 'pressure', 'value': 1013, 'status': 'active'},
        {'node': 'A7', 'type': 'temp', 'value': 24.1, 'status': 'active'},
        {'node': 'C9', 'type': 'humidity', 'value': 45, 'status': 'failed'},
        {'node': 'B4', 'type': 'pressure', 'value': 1015, 'status': 'active'},
        {'node': 'D2', 'type': 'temp', 'value': 19.8, 'status': 'active'},
        {'node': 'A7', 'type': 'temp', 'value': 22.9, 'status': 'active'},
        {'node': 'C9', 'type': 'humidity', 'value': 47, 'status': 'failed'}
    ]
    return raw_data

# Irrelevant helper - looks important but unused in critical path
def compute_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

# Decoy function that appears related but isn't used
def analyze_node_health(records):
    health = defaultdict(int)
    for r in records:
        health[r['node']] += 1 if r['status'] == 'active' else -1
    return health

# Real processing begins here
def filter_active_streams(data, target_type='temp'):
    active_only = [entry for entry in data if entry['status'] == 'active']
    type_filtered = [entry for entry in active_only if entry['type'] == target_type]
    
    # Distractor: counting irrelevant categories
    counter_aux = Counter(entry['node'] for entry in data if entry['type'] == 'humidity')
    dummy_sum = sum(counter_aux.values()) * 0  # dead computation
    
    return type_filtered

# Threshold system with red herring mappings
def generate_thresholds(node_list, base_offset=0.5):
    thresholds = {}
    for node in node_list:
        prefix = node[0]
        # Complex but partially irrelevant logic
        if prefix == 'A':
            thresholds[node] = 25.0 - base_offset
        elif prefix == 'B':
            thresholds[node] = 1020.0 - base_offset * 5
        else:
            thresholds[node] = 30.0 + base_offset  # misleading default
    # But only 'temp' nodes matter; others are distractions
    return thresholds

# Core logic with interdependent steps
def process_readings(readings, thresholds):
    aggregation = defaultdict(list)
    for record in readings:
        aggregation[record['node']].append(record['value'])
    
    # Compute averages per node - relevant
    averages = {node: sum(vals)/len(vals) for node, vals in aggregation.items()}
    
    # Distractor: elaborate cycle-based weighting (unused)
    weights = cycle([0.9, 1.0, 1.1])
    weighted_mask = {node: avg * next(weights) for node, avg in averages.items()}
    
    # Critical decision logic
    alert_count = 0
    for node, avg in averages.items():
        expected_max = thresholds.get(node, 20.0)  # fallback is misleading
        if avg > expected_max:
            alert_count += 1
    
    # Secondary trap: bit manipulation on alert count (looks complex but irrelevant)
    masked_alert = alert_count ^ 5 & (~3)
    
    # Final diagnostic depends only on original alert_count, not masked
    final_score = 0
    if alert_count == 0:
        final_score = 1248
    elif alert_count == 1:
        final_score = 1872
    else:
        final_score = 2496
    
    # Key assignment statement
    final_diagnostic = final_score + len(aggregation) * 10
    
    # Dead code path - never executed due to above logic
    if False:
        backup = sum(averages.values())
        final_diagnostic = int(backup)
    
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    all_data = collect_sensor_data()
    
    # Step 2: Filter for valid temperature readings
    filtered_data = filter_active_streams(all_data, 'temp')
    
    # Step 3: Extract node list for thresholding
    node_set = list(set(d['node'] for d in all_data))
    
    # Step 4: Generate thresholds (only A7 and D2 matter for temp)
    threshold_map = generate_thresholds(node_set)
    
    # Step 5: Process readings and compute final result
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")