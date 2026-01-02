def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda for dynamic scaling
    normalized = list(map(lambda x: x / max(metrics) if max(metrics) != 0 else 0, metrics))

    # Irrelevant transformation: reverse and shift (not used in final calculation)
    reversed_metrics = [x * 0.9 for x in metrics[::-1]]
    shifted = [x + 10 for x in reversed_metrics]

    # Compute weighted score using only original metrics and weights
    weighted_sum = 0.0
    total_weight = sum(weights)
    temp_result = []

    for i in range(len(metrics)):
        if weights[i] > 0:  # Only consider positive weights
            weighted_sum += metrics[i] * weights[i]
        temp_result.append(metrics[i] ** 2)  # Distractor computation

    # Additional unused intermediate calculations
    avg_metric = sum(metrics) / len(metrics) if metrics else 0
    penalty = 0
    for val in temp_result:
        if val > 500:
            penalty += 1  # Never actually applied

    # Final scoring logic
    if total_weight > 0:
        final_score = weighted_sum / total_weight
    else:
        final_score = 0

    # More red herring variables
    baseline = [x - avg_metric for x in metrics]
    adjusted = list(filter(lambda x: x > 0, baseline))

    return final_score

# Main execution
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Unused helper structure
config = {
    'version': '2.1',
    'active': True,
    'threshold': 80
}

intermediate = [x * 2 for x in weights]  # Dead code path

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")