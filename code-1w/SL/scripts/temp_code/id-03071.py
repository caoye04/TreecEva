def analyze_sensor(node_id, readings):
    if not readings:
        return 0
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    normalized_score = (avg * 0.7 + (1 / (1 + variance)) * 0.3) * 100
    return int(normalized_score)

# Irrelevant helper - looks useful but unused in critical path
def calculate_health_index(logs):
    total = 0
    for log in logs:
        total += sum(ord(c) for c in log) % 7
    return total // len(logs) if logs else 0

# Decoy function that mimics real processing
def legacy_process(data_list):
    accumulator = []
    for item in data_list:
        temp_val = 0
        for k, v in item.items():
            if len(k) % 2 == 0:
                temp_val -= hash(k) % 5
            else:
                temp_val += v % 3
        accumulator.append(temp_val)
    return sum(accumulator)

# Real processing function with red herrings
def process_readings(data, config):
    result_map = {}
    temp_cache = []
    
    # Irrelevant pre-scan (distractor)
    for node, values in data.items():
        if 'debug' in node:
            temp_cache.append(sum(values) % 11)
    
    # Actual logic begins
    active_nodes = 0
    total_yield = 0.0
    
    for node_id, readings in data.items():
        if 'sensor' not in node_id:  # filter only sensor nodes
            continue
            
        base_metric = analyze_sensor(node_id, readings)
        
        # Conditional threshold logic
        zone = config.get(node_id.split('_')[1], 'default')
        thresh_entry = config.get(zone, {})
        critical_level = thresh_entry.get('limit', 65)
        
        # Weighted adjustment based on zone importance
        weight = thresh_entry.get('weight', 1.0)
        adjusted_metric = base_metric * weight
        
        if adjusted_metric >= critical_level:
            decision_flag = 1
        else:
            decision_flag = 0
        
        # Accumulate only active nodes
        if decision_flag:
            active_nodes += 1
            total_yield += adjusted_metric

    # Dead code branch - never reached due to logic above
    if len(temp_cache) > 100:
        fallback = sum(temp_cache) / len(temp_cache)
        total_yield = fallback  # decoy assignment

    # Final computation - only this matters
    if active_nodes == 0:
        final_diagnostic = -1
    else:
        final_diagnostic = int((total_yield / active_nodes) + 0.5)  # rounded average

    # Spurious dictionary updates (irrelevant)
    result_map['timestamp'] = 'ignored_timestamp'
    result_map['version'] = 'v2.1-alpha'
    result_map['diagnostic'] = 'completed'

    return final_diagnostic

# Simulated input data
collected_data = {
    'node_01': [12, 15, 14, 13],
    'sensor_a1': [23, 25, 24, 26, 22],
    'sensor_b2': [18, 19, 20, 17, 16],
    'debug_log_01': [1, 1, 0, 1],
    'sensor_c3': [30, 33, 31, 29, 32],
    'metadata_x': [99]
}

threshold_map = {
    'a1': {'limit': 70, 'weight': 1.1},
    'b2': {'limit': 68, 'weight': 0.9},
    'c3': {'limit': 75, 'weight': 1.2},
    'default': {'limit': 65, 'weight': 1.0}
}

# Execution point of interest
final_diagnostic = process_readings(collected_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")