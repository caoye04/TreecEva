def evaluate_performance(metrics, threshold):
    # Initialize relevant and irrelevant variables
    temp_adjustment = 0
    cumulative_weight = 0
    penalty_factor = 0.1  # Unused red herring
    debug_log = []

    # Simulate data preprocessing (some steps are distractions)
    processed = {}
    for key, value in metrics.items():
        if key.startswith('sys_'):
            normalized = (value - 50) / 10
            processed[key] = max(normalized, 0)

    # Core logic: score based on specific conditions
    high_count = 0
    for val in metrics.values():
        if val > threshold * 1.5:
            high_count += 1

    # Secondary loop with semi-relevant computation
    adjustment_sum = 0
    for i in range(len(metrics)):
        if i % 2 == 0:
            adjustment_sum += i * 0.5  # Slight distraction

    # Actual scoring logic
    base_score = 0
    for k, v in processed.items():
        if v > threshold / 10:
            base_score += int(v * 10)

    # Final decision with helper calculation
    multiplier = 2 if high_count >= 3 else 1
    final_score = base_score * multiplier + int(adjustment_sum)

    # Dead code path - never executed but adds cognitive load
    if False:
        fallback = sum(debug_log) if debug_log else -999
        final_score = fallback

    return final_score

# Main execution
metric_data = {
    'sys_response': 78,
    'sys_latency': 85,
    'sys_throughput': 92,
    'sys_error_rate': 45,
    'sys_uptime': 88,
    'temporal_jitter': 30,  # Irrelevant key (filtered out)
    'aux_diagnostic': 60   # Irrelevant key
}
base_threshold = 60

# Execute main logic
final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")