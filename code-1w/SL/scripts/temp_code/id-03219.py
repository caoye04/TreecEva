def evaluate_performance(metrics, threshold):
    # Initialize various tracking variables
    count_valid = 0
    temp_sum = 0.0
    adjusted_values = []
    outlier_count = 0  # Track outliers (not directly used)
    scaling_factor = 1.75  # Distractor: not used in final logic

    for entry in metrics:
        raw_value = entry['value']
        category = entry['type']
        
        # Irrelevant transformation based on category
        if category == 'A':
            transformed = raw_value * 0.9
        elif category == 'B':
            transformed = raw_value * 1.1
        else:
            transformed = raw_value

        # Actual logic: only values above threshold contribute
        if raw_value > threshold:
            temp_sum += raw_value
            count_valid += 1

        # Dead code path - never affects result
        if raw_value < 10:
            outlier_count += 1

    # Simulated adjustment (distractor computation)
    if count_valid > 5:
        temp_sum *= 1.1
    else:
        temp_sum *= 0.95  # Misleading branch

    # Core result calculation
    average_contribution = temp_sum / count_valid if count_valid > 0 else 0

    # Additional irrelevant aggregation
    phantom_score = 0
    for i in range(3):
        phantom_score += i * 2  # Useless loop

    # Final score derived from average contribution and fixed offset
    final_result = int(average_contribution + 17)  # Deterministic integer output

    return final_result

# Main data setup
dataset = [
    {'value': 23, 'type': 'A'},
    {'value': 45, 'type': 'B'},
    {'value': 12, 'type': 'C'},
    {'value': 67, 'type': 'A'},
    {'value': 34, 'type': 'B'},
    {'value': 8,  'type': 'C'},
    {'value': 55, 'type': 'A'},
    {'value': 14, 'type': 'B'}
]

base_threshold = 20
metric_summary = {k: 0 for k in ['A', 'B', 'C']}  # Unused dictionary tracking

for item in dataset:
    metric_summary[item['type']] += 1

# Key execution point
final_score = evaluate_performance(dataset, base_threshold)

print(f"Result: {final_score}")