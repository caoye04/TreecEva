def evaluate_performance(records, importance):
    total = 0
    bonus_tracker = []
    penalty = 0

    for record in records:
        # Extract components
        base_value = record['value']
        status_flag = record['status']
        category = record['type']

        # Irrelevant computation - distractor (bonus tracking not used)
        if status_flag == 'EXEMPLARY':
            bonus_tracker.append(base_value * 0.1)

        # Real logic: apply weight based on type
        modifier = importance.get(category, 1.0)
        contribution = base_value * modifier

        # Conditional penalty logic (only applies under specific pattern)
        binary_flag = int(status_flag[-1]) if status_flag.isdigit() else 0
        if binary_flag & 1:
            penalty += 5

        total += contribution

    # Secondary processing with lambda - relevant
    adjuster = lambda x, p: x * 0.95 if p > 10 else x
    adjusted_total = adjuster(total, penalty)

    # Unnecessary slicing distraction
    truncated_data = records[1:-1]
    dummy_sum = sum(r['value'] for r in truncated_data) if truncated_data else 0
    shadow_impact = dummy_sum * 0.05  # Not actually affecting final result

    # Final scoring with dictionary-based threshold mapping
    thresholds = {50: 100, 75: 200, 100: 300}
    base_award = thresholds.get(int(adjusted_total), 50)

    # Actual final score calculation
    final_score = int(adjusted_total + base_award - penalty)

    return final_score

# Input data setup
data = [
    {'value': 20, 'status': 'ACTIVE7', 'type': 'A'},
    {'value': 35, 'status': 'STANDBY', 'type': 'B'},
    {'value': 50, 'status': 'EXEMPLARY', 'type': 'A'},
    {'value': 45, 'status': 'ACTIVE1', 'type': 'C'}
]

weights = {'A': 1.2, 'B': 0.8, 'C': 1.5}

# Execution point
final_score = evaluate_performance(data, weights)
print(f"Result: {final_score}")