def evaluate_performance(metrics, weights):
    # Initialize various intermediate values, some are red herrings
    base_score = 0
    adjustment_factor = 0.0
    temp_result = []
    outlier_count = 0  # Not actually used in final logic
    scaling_constant = 1.7  # Distractor variable

    # Simulate processing of multiple performance dimensions
    for key in ['latency', 'throughput', 'accuracy', 'energy']:
        if key in metrics and metrics[key] > 0:
            normalized = min(metrics[key] / 100.0, 1.0)
            weight = weights.get(key, 0.1)
            contribution = normalized * weight
            temp_result.append(contribution)

            # Conditional expression to add noise-like behavior
            adjustment_factor += 0.05 if normalized > 0.8 else -0.02

    # Real computation begins: weighted average with bias correction
    total_weighted = sum(temp_result)
    total_possible = sum(weights.get(k, 0.1) for k in ['latency', 'throughput', 'accuracy', 'energy'])
    raw_score = total_weighted / total_possible if total_possible > 0 else 0

    # Apply artificial penalty based on unused metric tracking
    recorded_metrics = [k for k, v in metrics.items() if v is not None]  # List comprehension
    bonus_eligible = len([m for m in recorded_metrics if m in ['accuracy', 'throughput']])  # Semi-relevant

    # Final score calculation – only this matters
    base_score = raw_score * 100
    if bonus_eligible >= 2:
        base_score += 5

    # Dead code path – misleading optimization attempt
    debug_mode = False
    if debug_mode:
        print(f'Debug: {base_score=}, {adjustment_factor=}')

    # Key statement
    final_score = int(base_score)  # Truncate to integer

    return final_score

# Main execution
metrics = {
    'latency': 85,
    'throughput': 92,
    'accuracy': 96,
    'energy': 70,
    'reliability': 45  # Unused in weights
}

weights = {
    'latency': 0.25,
    'throughput': 0.3,
    'accuracy': 0.35,
    'energy': 0.1
}

# Intermediate irrelevant computation
placeholder_sum = sum([x**2 for x in range(5)]) // 2  # Value: 15, not used

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")