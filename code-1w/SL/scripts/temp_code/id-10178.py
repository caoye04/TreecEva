def analyze_surplus(resources):
    surplus = 0
    for val in resources.values():
        if val > 100:
            surplus += val - 100
    return surplus


def calculate_threshold(length):
    return (length * 3) // 2


def validate_sequence(seq):
    return all(x > 0 for x in seq)


def filter_active_nodes(node_map):
    active = []
    for k, v in node_map.items():
        if v['status'] == 'active' and v['load'] < 80:
            active.append(k)
    # Irrelevant computation (distractor)
    temp_score = sum(len(k) for k in active) * 0.5
    return active


def optimize_distribution(resource_map, constraints):
    total = 0
    base_keys = [k for k in resource_map.keys() if 'core' in k]
    
    # Real logic begins
    filtered_values = [v for v in resource_map.values() if isinstance(v, int) and v % 2 == 0]
    temp_sum = sum(filtered_values)
    
    # Dummy transformation (distractor)
    adjusted_values = [v * 1.1 for v in filtered_values if v < 50]
    dummy_aggregate = sum(adjusted_values) + 10  # Not used later
    
    constraint_limit = constraints.get('limit', 1000)
    scaling_factor = constraints.get('scale', 1.0)
    
    intermediate = 0
    for key in base_keys:
        raw_val = resource_map[key]
        if raw_val > 50:
            intermediate += raw_val // 4
        else:
            intermediate += raw_val // 2
    
    # Key calculation
    total += intermediate * scaling_factor
    
    # Additional logic using dictionary slicing
    ordered_items = sorted(resource_map.items())
    slice_portion = ordered_items[1:4]
    for k, v in slice_portion:
        if isinstance(v, int):
            total += v % 7
    
    # Dead code path (distractor)
    if len(slice_portion) > 10:
        fallback = 0
        for item in slice_portion:
            fallback += hash(item[0]) % 5
        total -= fallback  # unreachable
    
    return int(total)

# Main execution
resource_map = {
    'core_alpha': 120,
    'core_beta': 88,
    'aux_power': 200,
    'core_gamma': 44,
    'meta_data': {'config': 1},
    'temp_buffer': 33
}

constraints = {
    'limit': 900,
    'scale': 1.5,
    'enabled': True
}

# Unused helper variables (distractors)
baseline = [x for x in range(10)]
surplus_check = analyze_surplus(resource_map)
sequence_test = validate_sequence(baseline)
nodes = {'node_x': {'status': 'active', 'load': 75}, 'node_y': {'status': 'idle', 'load': 90}}
active_list = filter_active_nodes(nodes)

# Critical statement
final_capacity = optimize_distribution(resource_map, constraints)

print(f"Result: {final_capacity}")