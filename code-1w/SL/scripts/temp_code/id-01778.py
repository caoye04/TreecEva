def evaluate_performance(metrics, importance_weights):
    # Initialize tracking variables
    total_weight = sum(importance_weights)
    normalized_weights = [w / total_weight for w in importance_weights]
    
    # Secondary metric transformation using lambda
    transform = lambda x: (x ** 2 + 3 * x) // 2 if x > 5 else x
    adjusted_metrics = [transform(m) for m in metrics]

    # Irrelevant distraction: entropy calculation (not used later)
    import math
    entropy_distraction = sum([-w * math.log(w + 1e-9) for w in normalized_weights])
    entropy_normalized = round(entropy_distraction, 4)

    # Distractor loop: processes dummy data
    temp_buffer = [0] * len(metrics)
    for i in range(len(metrics)):
        for j in range(i + 1):
            temp_buffer[i] += (i - j) * 2

    # Core logic: weighted sum with threshold filtering
    filtered_contribution = 0.0
    threshold = 6.5
    for idx, val in enumerate(adjusted_metrics):
        if val >= threshold:
            filtered_contribution += val * normalized_weights[idx]

    # Additional red herring: unused recursive function
    def _recursive_sum(n):
        return n + _recursive_sum(n - 1) if n > 0 else 0
    
    unused_sum = _recursive_sum(5)  # This is never used

    # Final adjustment with rounding
    final_value = round(filtered_contribution, 2)
    return int(final_value)

# Main execution context
metric_set = [4, 7, 9, 5, 8]
weights = [1, 3, 4, 2, 5]

# Dead code path: simulation flag check
simulate_only = False
if simulate_only:
    final_score = -999
else:
    final_score = evaluate_performance(metric_set, weights)

print(f"Result: {final_score}")