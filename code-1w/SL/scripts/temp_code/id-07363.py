def evaluate_performance(metrics, weights):
    base_score = 0
    penalty_factor = 0.9
    bonus_tracker = []
    temp_result = 0

    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        weighted_val = metric * weight
        if weighted_val > 10:
            bonus_tracker.append(weighted_val * 0.1)
        temp_result += weighted_val

    base_score = sum(m * w for m, w in zip(metrics, weights))

    adjustment = 0
    for idx, val in enumerate(metrics):
        if idx % 2 == 0 and val > 5:
            adjustment += 1.5

    # Irrelevant computation - distractor
    outlier_check = [x for x in metrics if x < 0]
    valid_count = len([x for x in metrics if x >= 0])

    # Unused helper logic
    def normalize(x):
        return x / (sum(metrics) + 1e-8)

    scaling_factor = 1.0
    if sum(weights) != 0:
        scaling_factor = 100 / sum(weights)

    intermediate = base_score + adjustment

    final_score = int(intermediate + sum(bonus_tracker) + adjustment)

    # Dead code path
    if False:
        final_score *= penalty_factor

    return final_score

# Main execution
metrics = [7, 12, 6, 15, 4]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

outlier_buffer = [x * 2 for x in weights]  # Unused variable
scaling_constant = 1.0  # Unused

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")