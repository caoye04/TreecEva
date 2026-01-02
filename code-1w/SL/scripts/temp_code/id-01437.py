def evaluate_performance(metrics, weights):
    base = 0
    bonus = 0
    penalty = 0
    adjustment_factor = 1.0

    # Irrelevant preprocessing: normalize metrics (not used in final logic)
    normalized = {k: v / max(metrics.values()) for k, v in metrics.items()}

    # Distractor: unused helper calculation
    outlier_count = sum(1 for v in metrics.values() if v < 50)
    if outlier_count > 2:
        adjustment_factor *= 0.9

    # Core logic begins
    for key in ['accuracy', 'latency', 'throughput', 'reliability']:
        if key not in metrics:
            continue
        if metrics[key] >= 80:
            base += 20
            if key in weights:
                bonus += weights[key] * 0.5
        elif metrics[key] >= 60:
            base += 10
        else:
            penalty += 5

    # Secondary logic with partial relevance
    consistency_check = [v for v in metrics.values() if v > 75]
    if len(consistency_check) >= 3:
        bonus += 15

    # Dead code path (never reached due to logic above)
    debug_trace = []
    for i, val in enumerate(metrics.values()):
        if val < 0:
            debug_trace.append((i, "invalid"))

    # Final computation with red herring variables included
    intermediate = (base + bonus - penalty) * adjustment_factor
    noise = sum([i * 0 for i in range(5)])  # Purposeless computation
    final_score = int(intermediate - noise)

    return final_score

# Input data
metrics = {
    'accuracy': 85,
    'latency': 78,
    'throughput': 92,
    'reliability': 88,
    'scalability': 45  # Below threshold, not in core keys
}
weights = {'accuracy': 10, 'throughput': 8}  # Only two have weights

# Execution point of interest
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")