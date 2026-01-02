def calculate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_values = [x['metric'] for x in data if x['active']]
    offsets = [len(x['name']) for x in data]  # Distractor: not used later
    
    # Normalization step (relevant)
    max_val = max(raw_values)
    normalized = [round(v / max_val, 4) for v in raw_values]
    
    # Apply weighting based on priority (relevant)
    weights = []
    for x in data:
        if x['priority'] == 'high':
            weights.append(1.5)
        elif x['priority'] == 'medium':
            weights.append(1.0)
        else:
            weights.append(0.5)
    
    # Weighted sum calculation (key logic)
    weighted_sum = sum(normalized[i] * weights[i] for i in range(len(normalized)))
    
    # Irrelevant string processing (distractor)
    labels = [x['name'].upper().replace('_', '') for x in data]
    checksum = sum(ord(labels[0][i]) * (i + 1) for i in range(len(labels[0]))) % 100
    
    # Final scaling with fixed multiplier (relevant)
    final_score = round(weighted_sum * 10, 2)
    return final_score

# Input data setup
benchmark_data = [
    {'name': 'task_A', 'metric': 85, 'active': True, 'priority': 'high'},
    {'name': 'task_B', 'metric': 70, 'active': True, 'priority': 'medium'},
    {'name': 'task_C', 'metric': 90, 'active': False, 'priority': 'low'},  # Inactive
    {'name': 'task_D', 'metric': 95, 'active': True, 'priority': 'high'},
    {'name': 'task_E', 'metric': 60, 'active': True, 'priority': 'low'}
]

# Execute main logic
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")