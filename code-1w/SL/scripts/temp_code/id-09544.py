def evaluate_performance(metrics, weights):
    base_score = 0
    adjustment_factor = 0.0
    penalty = 0
    temp_result = []

    # Irrelevant pre-processing (distractor)
    for k in metrics:
        if 'temp' in k:
            temp_result.append(metrics[k] * 0.1)

    # Real scoring logic starts
    for key in weights:
        if key in metrics:
            contribution = metrics[key] * weights[key]
            base_score += contribution

            # Conditional adjustment (relevant)
            adjustment_factor += 0.05 if metrics[key] > 80 else -0.02

    # Simulated calibration (partially relevant)
    calibrated_adjustment = round(adjustment_factor * 100) / 100

    # Secondary validation pass (with early return red herring)
    validation_check = sum(1 for v in metrics.values() if v < 0)
    if validation_check > 0:
        return -1  # Dead code path — no negative values present

    # Apply non-linear bonus if high performance
    bonus = 10 if base_score > 90 else (5 if base_score > 70 else 0)

    # Dummy computations (distractors)
    dummy_sum = 0
    for i in range(3):
        for j in range(3):
            dummy_sum += i * j
    scaling_proxy = dummy_sum / 2.0  # Unused value

    # Final score computation
    final_score = base_score + (calibrated_adjustment * 10) + bonus

    # Extra misleading state update
    status_flags = {'optimized': True, 'adjusted': False}
    status_flags['finalized'] = final_score >= 85

    return final_score


# Main execution
metrics = {
    'accuracy': 88,
    'latency': 92,
    'throughput': 76,
    'memory_usage': 81,
    'temp_sensor_1': 45,  # Distractor metric
    'temp_sensor_2': 47   # Distractor metric
}

weights = {
    'accuracy': 0.3,
    'latency': 0.25,
    'throughput': 0.2,
    'memory_usage': 0.25
}

intermediate_total = sum(metrics.values())  # Irrelevant summary
filter_threshold = intermediate_total / len(metrics)  # Not used meaningfully

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")