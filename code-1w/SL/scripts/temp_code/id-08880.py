def calculate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_values = [entry['metric'] for entry in data if entry['active']]
    
    # Irrelevant distraction: counting inactive entries
    inactive_count = sum(1 for entry in data if not entry['active'])
    dummy_sum = sum(i * 2 for i in range(inactive_count))  # Dead-end computation

    # Core logic begins
    baseline = len(raw_values) * 1.5
    adjusted = [x - baseline / len(raw_values) if len(raw_values) > 0 else 0 for x in raw_values]
    
    # State tracking with dictionary
    stats = {}
    stats['max_adj'] = max(adjusted) if adjusted else 0
    stats['min_adj'] = min(adjusted) if adjusted else 0
    stats['range'] = stats['max_adj'] - stats['min_adj']

    # Secondary processing: apply weight based on index parity
    weighted_devs = []
    for i, val in enumerate(adjusted):
        weight = 1.2 if i % 2 == 0 else 0.8
        deviation = abs(val - (baseline / len(raw_values)))
        weighted_devs.append(deviation * weight)
    
    # Red herring: sort but don't use sorted result directly
    sorted_devs = sorted(weighted_devs, reverse=True)
    trimmed = sorted_devs[1:-1]  # Remove extremes, but this version isn't used

    # Actual aggregation
    aggregate = sum(weighted_devs) / len(weighted_devs) if weighted_devs else 0

    # Final adjustment using unused stats
    threshold = stats['range'] * 0.5
    bonus = 10 if aggregate < threshold else -5

    # Key result calculation
    final_score = int(aggregate * 3 + bonus)
    return final_score

# Simulated benchmark dataset
benchmark_data = [
    {'metric': 25, 'active': True},
    {'metric': 30, 'active': True},
    {'metric': 18, 'active': False},
    {'metric': 35, 'active': True},
    {'metric': 28, 'active': True},
    {'metric': 12, 'active': False},
    {'metric': 40, 'active': True}
]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")