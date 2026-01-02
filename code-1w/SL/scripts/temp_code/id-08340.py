def calculate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_values = [x['metric'] for x in data if x['active']]
    offsets = [x['offset'] for x in data if not x['active']]  # Unused distractor list
    
    # Irrelevant transformation (dead computation)
    transformed_offsets = [abs(o) ** 0.5 for o in offsets if o < -5]
    temp_buffer = sum(transformed_offsets) * 0.1  # Not used later

    # Core logic: compute weighted score
    base_sum = sum(raw_values)
    adjustment_factor = 0.0
    
    if len(raw_values) > 3:
        adjustment_factor += 1.5
        if base_sum > 20:
            adjustment_factor += 2.25
    else:
        adjustment_factor -= 1.0

    # Simulate performance decay over iterations (nested loop red herring)
    decay_accumulator = 0.0
    for i in range(2):
        for j in range(3):
            decay_accumulator += (i + j) * 0.05  # Minor distraction

    # Final calculation with slicing and conditional boost
    recent_metrics = raw_values[-2:]  # Last two values
    bonus = 10 if all(m > 4 for m in recent_metrics) else 0

    final_score = int(base_sum * adjustment_factor + bonus - 2)  # Key result
    return final_score

# Input data with mixed active/inactive entries
benchmark_data = [
    {'metric': 5, 'offset': -10, 'active': True},
    {'metric': 6, 'offset': 8, 'active': True},
    {'metric': 3, 'offset': -12, 'active': False},
    {'metric': 7, 'offset': -6, 'active': True},
    {'metric': 8, 'offset': 15, 'active': True},
    {'metric': 2, 'offset': -20, 'active': False}
]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")