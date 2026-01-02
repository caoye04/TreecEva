def process_metrics(entries, importance_weights):
    base_modifier = 1.0
    temp_adjustment = 0.0
    cumulative = 0
    weight_sum = sum(importance_weights)
    normalized = [w / weight_sum for w in importance_weights]
    
    # Irrelevant preprocessing: sorting entries by id (not used later)
    sorted_entries = sorted(entries, key=lambda x: x['id'])
    entry_ids = [e['id'] for e in sorted_entries]
    
    # Distractor: unused transformation map
    transform_map = {i: (i * 1.5) ** 0.5 for i in entry_ids}
    
    # Actual computation path
    valid_data = [e for e in entries if e['active']]
    for item in valid_data:
        raw_value = item['value']
        index = item['group']
        weight = normalized[index] if index < len(normalized) else 0.1
        
        # Apply nonlinear scaling based on thresholds
        if raw_value > 100:
            scaled = raw_value * 0.8
        elif raw_value > 50:
            scaled = raw_value * 0.9
        else:
            scaled = raw_value * 1.0
        
        # Accumulate weighted contribution
        contribution = scaled * weight
        cumulative += contribution
    
    # Secondary adjustment using lambda-based smoothing
    adjustment_factor = lambda x: 0.95 if x > 75 else (0.98 if x > 50 else 1.02)
    smoothed = cumulative * adjustment_factor(cumulative)
    
    # Dead code branch: never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: {cumulative=}, {transform_map=}')
    
    # Final aggregation with rounding
    final_score = int(round(smoothed + base_modifier))
    return final_score

# Input data
weights = [3, 7, 2, 8]
data = [
    {'id': 101, 'value': 120, 'group': 1, 'active': True},
    {'id': 102, 'value': 65, 'group': 0, 'active': True},
    {'id': 103, 'value': 40, 'group': 2, 'active': False},
    {'id': 104, 'value': 90, 'group': 1, 'active': True},
    {'id': 105, 'value': 110, 'group': 3, 'active': True}
]

# Execution
result_var = process_metrics(data, weights)
print(f'Result: {result_var}')