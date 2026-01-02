from itertools import combinations

# Simulate sensor data processing with weighted scoring
def evaluate_performance(metrics, weights):
    base_score = 0
    penalty_adjustment = 0
    temporal_factor = 1.2
    dummy_accumulator = 0

    # Irrelevant preprocessing: simulate noise filtering
    filtered_metrics = [m * 0.95 for m in metrics if m > 0]
    for val in filtered_metrics:
        dummy_accumulator += val ** 0.5  # Unused computation

    # Core logic: weighted sum with non-linear boost
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        if metric >= 50:
            base_score += metric * weight * 1.1
        else:
            base_score += metric * weight * 0.9

    # Conditional bonus based on metric diversity
    unique_pairs = list(combinations(metrics, 2))
    diversity_bonus = 0
    for pair in unique_pairs:
        if abs(pair[0] - pair[1]) > 30:
            diversity_bonus += 2.5

    # Apply artificial cap (not affecting result in this case)
    capped_bonus = min(diversity_bonus, 20)

    # Simulate environmental adjustment (constant in this input)
    environment_modifier = 0.98
    adjusted_score = (base_score + capped_bonus) * environment_modifier

    # Final nonlinear transformation
    final_score = int(adjusted_score + 0.5)  # Round to nearest integer

    # Dead code branch (never executed with current inputs)
    redundant_check = False
    if redundant_check and final_score < 100:
        final_score *= 2

    return final_score

# Additional irrelevant data structures
historical_logs = [
    {'timestamp': '2023-01-01', 'value': 45},
    {'timestamp': '2023-01-02', 'value': 52}
]

# Misleading auxiliary calculation
projected_growth = sum([x['value'] for x in historical_logs]) / len(historical_logs) * 1.05

# Input data
metrics = [65, 72, 48, 81, 53]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")