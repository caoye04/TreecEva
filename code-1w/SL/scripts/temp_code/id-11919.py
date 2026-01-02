def evaluate_performance(data, importance):
    baseline = 100
    adjustment_factor = 0.85
    temp_result = 0
    weighted_sum = 0
    total_weight = sum(importance)

    # Normalize weights
    normalized = [round(w / total_weight, 4) for w in importance]

    # Misleading transformation - not actually used later
    inverted_data = list(map(lambda x: max(data) + min(data) - x, data))
    shadow_value = sum(inverted_data) // len(inverted_data)

    # Actual processing with nested logic and case handling
    for i, val in enumerate(data):
        if val >= baseline:
            if i % 2 == 0:
                temp_result += val * normalized[i] * 1.1
            else:
                temp_result += val * normalized[i] * 1.05
        else:
            deviation = baseline - val
            penalty = deviation * 0.05 if deviation > 10 else deviation * 0.02
            temp_result += (val - penalty) * normalized[i]

    # Simulate threshold check with red herring computation
    threshold_met = all(x >= 85 for x in data)
    bonus_applied = False
    if threshold_met:
        extra_boost = sum(data[i] * 0.02 for i in range(len(data)) if i % 3 == 0)
        temp_result += extra_boost
        bonus_applied = True  # unused flag

    # Dead code path - never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: {temp_result}')

    # Final aggregation using lambda for functional style
    aggregator = lambda x, y: x + y * 1.02
    final_score = int(aggregator(temp_result, -temp_result * 0.02))

    return final_score

# Input data
metrics = [95, 87, 92, 103, 88]
weights = [3, 2, 4, 3, 2]

# Execution point of interest
final_score = evaluate_performance(metrics, weights)
print(f'Target result: {final_score}')