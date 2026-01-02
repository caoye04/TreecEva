from itertools import combinations

def analyze_utilization(records):
    total_load = 0
    peak_moment = 0
    temp_debug = []
    for entry in records:
        if 'usage' in entry and entry['usage'] > 0.8:
            total_load += entry['usage'] * entry['nodes']
            if entry['time'] % 10 == 0:
                peak_moment += 1
        else:
            temp_debug.append(entry['time'])  # Distractor: not used later
    return total_load

def validate_allocation(log):
    valid_count = 0
    for item in log:
        if item['status'] == 'active' and item['retries'] < 3:
            valid_count += 1
    threshold = 5
    if valid_count >= threshold:
        return True
    return False

def calculate_remaining_capacity(resources, log):
    base_capacity = 1000
    usage_deduction = 0
    metadata_tracker = {}
    
    # Simulate resource consumption
    for r_id, props in resources.items():
        if props['type'] == 'compute':
            usage_deduction += props['cores'] * 10
        elif props['type'] == 'storage':
            usage_deduction += props['size_gb'] * 2
    
    # Irrelevant combination analysis (distractor)
    keys = list(resources.keys())
    combo_total = 0
    for combo in combinations(keys, 2):
        combo_total += 1  # Count pairs, but not used in final result
    
    # Conditional override based on allocation log validity
    if validate_allocation(log):
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.1
    
    intermediate_result = base_capacity - usage_deduction
    final_capacity = int(intermediate_result * adjustment_factor)
    
    # Dead code path (misleading)
    if final_capacity < 0:
        final_capacity = 0
    
    # Additional red herring computation
    debug_snapshot = {'final': final_capacity, 'timestamp': 999}
    metadata_tracker['snapshot'] = debug_snapshot
    
    return final_capacity

def main():
    resource_map = {
        'r_001': {'type': 'compute', 'cores': 8, 'threads': 16},
        'r_002': {'type': 'storage', 'size_gb': 500, 'speed': 'ssd'},
        'r_003': {'type': 'compute', 'cores': 16, 'threads': 32},
        'r_004': {'type': 'storage', 'size_gb': 200, 'speed': 'hdd'}
    }
    
    allocation_log = [
        {'id': 'a1', 'status': 'active', 'retries': 1, 'time': 10},
        {'id': 'a2', 'status': 'failed', 'retries': 4, 'time': 15},
        {'id': 'a3', 'status': 'active', 'retries': 0, 'time': 20},
        {'id': 'a4', 'status': 'active', 'retries': 2, 'time': 25},
        {'id': 'a5', 'status': 'active', 'retries': 1, 'time': 30}
    ]
    
    # Misleading preliminary analysis
    load_analysis = analyze_utilization([
        {'usage': 0.85, 'nodes': 4, 'time': 10},
        {'usage': 0.7, 'nodes': 2, 'time': 12},
        {'usage': 0.92, 'nodes': 3, 'time': 20}
    ])
    
    # Key execution point
    final_capacity = calculate_remaining_capacity(resource_map, allocation_log)
    
    print(f"Result: {final_capacity}")

if __name__ == "__main__":
    main()