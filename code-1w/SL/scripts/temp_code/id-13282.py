def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    temp_data = [x * 1.05 for x in metrics if x > 0]
    temp_data = [x for x in temp_data if x < 100]

    # Real logic begins: compute weighted compliance
    weights = (0.4, 0.3, 0.2, 0.1)
    compliance = [
        metrics[0] >= thresholds['latency'],
        metrics[1] <= thresholds['error_rate'],
        metrics[2] >= thresholds['throughput'],
        metrics[3] == True
    ]

    # Conditional expression used here
    base_score = 100 if all(compliance) else 75 if any(compliance) else 50

    # Secondary adjustment based on bonus rule (semi-relevant)
    bonus_applied = False
    surge_factor = 1.0
    if metrics[0] < thresholds['latency'] * 0.9 and metrics[2] > thresholds['throughput'] * 1.1:
        surge_factor = 1.15
        bonus_applied = True

    # Dead code path (irrelevant but plausible)
    debug_log = []
    if bonus_applied:
        debug_log.append("Surge bonus triggered")
        # This branch is never reached due to condition above
        dummy_var = sum(debug_log.count(x) for x in debug_log)

    # Compute final score with distractor-weighted average (only base_score and surge matter)
    phantom_weight = sum(weights[i] * metrics[i] for i in range(3)) / 3  # unused
    phantom_correction = max(temp_data) - min(temp_data) if temp_data else 0  # unused

    final_score = int(base_score * surge_factor)

    # Additional red herring variables
    efficiency_rank = 'A' if final_score >= 90 else 'B' if final_score >= 75 else 'C'
    calibration_offset = (metrics[0] + metrics[1]) % 7

    return final_score

# Input data
system_metrics = [85, 0.04, 1150, True]
threshold_config = {
    'latency': 90,
    'error_rate': 0.05,
    'throughput': 1000
}

# Execution point of interest
final_score = evaluate_performance(system_metrics, threshold_config)
print(f"Result: {final_score}")