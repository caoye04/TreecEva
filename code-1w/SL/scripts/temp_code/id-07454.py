def calculate_final_score(records, limit):
    # Precompute derived values
    filtered_ids = {i for i, r in enumerate(records) if r['value'] > 0.5}
    temp_sum = sum(r['value'] * 2 for r in records if r['active'])

    # Misleading intermediate calculations
    outlier_count = 0
    debug_trace = []
    for r in records:
        if r['value'] < 0.1:
            outlier_count += 1
        debug_trace.append(r['value'] ** 0.5)

    # Core logic: count how many exceed limit after transformation
    transformed = [r['value'] * (3 if r['flag'] else 1) for r in records]
    above_threshold = [v for v in transformed if v >= limit]
    
    # Secondary filter using set operations
    valid_indices = {i for i, r in enumerate(records) if r['flag']}
    used_indices = filtered_ids.intersection(valid_indices)

    # Conditional adjustment based on presence of high-flag entries
    bonus = 10 if any(records[i]['value'] > 0.9 for i in used_indices) else 0

    # Final score computation
    base_score = len(above_threshold) * 5
    penalty = len([r for r in records if not r['active']]) * 2
    final_score = base_score - penalty + bonus

    # Red herring: unused aggregation
    avg_debug = sum(debug_trace) / len(debug_trace) if debug_trace else 0
    max_outlier = max([r['value'] for r in records if r['value'] < 0.1], default=0)

    return final_score

# Input data
data_set = [
    {'value': 0.65, 'active': True, 'flag': True},
    {'value': 0.42, 'active': True, 'flag': False},
    {'value': 0.88, 'active': False, 'flag': True},
    {'value': 0.92, 'active': True, 'flag': True},
    {'value': 0.35, 'active': False, 'flag': False},
    {'value': 0.71, 'active': True, 'flag': True}
]
threshold = 0.75

# Execute
final_score = calculate_final_score(data_set, threshold)
print(f"Result: {final_score}")