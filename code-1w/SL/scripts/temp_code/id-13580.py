def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda for dynamic scaling
    normalized = list(map(lambda x: x / max(metrics) if max(metrics) != 0 else 0, metrics))

    # Irrelevant transformation: reverse and scale (not used in final calculation)
    reversed_scaled = [val * 1.5 for val in reversed(normalized)]
    temp_offset = sum(reversed_scaled) - min(reversed_scaled)

    # Weighted aggregation with distraction from unused intermediate
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    total_weight = sum(weights)

    # Simulated threshold check with early return red herring
    if weighted_sum < 0.5:
        return 0  # Not triggered in this case

    # Secondary validation: count how many metrics exceed average (distractor)
    avg_metric = sum(metrics) / len(metrics)
    above_avg_count = len([m for m in metrics if m > avg_metric])
    adjustment_factor = above_avg_count * 0.1  # Computed but not used

    # Final performance score computation
    final_score = (weighted_sum / total_weight) * 100

    # Dead code path: debugging artifact
    debug_snapshot = {"raw": metrics.copy(), "norm": normalized[:]}

    return int(final_score)

# Main execution context
metrics_data = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Unused backup weights (distractor)
bak_weights = [w * 0.95 for w in weights]
alt_scaling = sum(bak_weights)

# Key statement
final_score = evaluate_performance(metrics_data, weights)

# Output result
print(f"Result: {final_score}")