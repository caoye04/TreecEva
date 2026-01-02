def calculate_final_score(items, importance_weights):
    base_score = 0
    bonus_factor = 0.0
    penalty_tracker = []
    temp_result_cache = {}

    for idx, (item, weight) in enumerate(zip(items, importance_weights)):
        raw_value = item * weight
        adjusted_value = raw_value + (idx % 3)

        # Distractor: caching intermediate values not fully used
        temp_result_cache[f'item_{idx}'] = adjusted_value * 1.1

        if adjusted_value > 25:
            bonus_factor += 1.5
        elif adjusted_value < 10:
            penalty_tracker.append(idx)

        # Core logic contribution
        base_score += adjusted_value

    # Irrelevant transformation
    transformed_data = [x * 0.95 for x in items if x % 2 == 0]
    average_transformed = sum(transformed_data) / len(transformed_data) if transformed_data else 0

    # Unused helper computation (distractor)
    outlier_count = sum(1 for v in items if v > 40)

    # Actual final score calculation
    final_score = base_score + bonus_factor * 10

    # Dead code branch (never executed due to constants)
    if False and len(penalty_tracker) > 5:
        final_score -= len(penalty_tracker) * 2

    return int(final_score)

# Input data
sensor_readings = [8, 12, 26, 31, 5]
feature_importance = [2, 3, 4, 5, 1]

# Execution point
final_score = calculate_final_score(sensor_readings, feature_importance)
print(f"Result: {final_score}")