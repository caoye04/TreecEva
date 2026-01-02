def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda for dynamic scaling
    normalized = list(map(lambda x: (x - min(metrics)) / (max(metrics) - min(metrics) + 1e-5), metrics))

    # Irrelevant distraction: compute entropy-like measure (not used)
    import math
    shannon_entropy = sum(-x * math.log(x + 1e-5) for x in normalized)
    temp_buffer = [shannon_entropy * 2 for _ in range(3)]  # Dead computation

    # Weighted scoring with meaningful logic
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    bonus = 10 if all(m > 0.5 for m in normalized[:3]) else 0  # Conditional incentive

    # Secondary distraction: simulate unused ranking
    ranked_metrics = sorted(enumerate(metrics), key=lambda x: x[1], reverse=True)
    rank_shift = sum(abs(i - idx) for i, (idx, _) in enumerate(ranked_metrics))  # Unused

    # Core result calculation
    base_score = weighted_sum * 100
    final_score = base_score + bonus

    # Extra red herring: complex tuple unpacking with irrelevant data
    stats_summary = (len(metrics), len(weights), min(metrics), max(metrics))
    count, _, _, peak = stats_summary
    adjustment_factor = (count // 2) if peak > 50 else 0  # Not actually applied

    return final_score

# Main execution
metrics_data = [85, 90, 78, 92, 88]
weight_scheme = [0.2, 0.3, 0.15, 0.25, 0.1]

# Misleading pre-processing (semi-relevant but doesn't alter outcome)
doubled_metrics = [m * 2 for m in metrics_data]
scaled_weights = [w * 2 for w in weight_scheme]
_ = [doubled_metrics[i] * scaled_weights[i] for i in range(len(doubled_metrics))]  # Unused correlation

final_score = evaluate_performance(metrics_data, weight_scheme)
print(f"Result: {final_score}")