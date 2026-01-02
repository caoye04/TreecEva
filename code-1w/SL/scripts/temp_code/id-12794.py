def evaluate_performance(metrics, baseline):
    # Irrelevant tracking variables
    temp_sum = 0
    debug_log = []
    outlier_count = 0

    # Semi-relevant preprocessing
    normalized = {}
    for key, value in metrics.items():
        if value > 2 * baseline.get(key, 1):
            outlier_count += 1
        norm_value = round((value - baseline.get(key, 0)) / (baseline.get(key, 1) + 0.1), 2)
        normalized[key] = max(0, norm_value)

    # Distractor: dead computation on set operations
    keys_set = set(metrics.keys())
    base_set = set(baseline.keys())
    extra_fields = keys_set - base_set
    shared_fields = keys_set & base_set
    temp_intersection_size = len(shared_fields)

    # Actual logic begins: score based on specific conditions
    raw_score = 0
    penalty = 0

    for k in ['throughput', 'latency', 'reliability']:
        ref = baseline.get(k, 1)
        val = metrics.get(k, 0)
        if k == 'latency':
            # Lower latency is better
            contribution = ref / (val + 1e-5) if val < 2 * ref else 0.5
            raw_score += contribution * 10
            if val > 1.8 * ref:
                penalty += 15
        else:
            # Higher throughput and reliability is better
            factor = val / ref
            raw_score += factor * 20 if factor < 3 else 60  # Cap at 3x

    # Bitwise flag check for system state (semi-relevant)
    status_flag = metrics.get('status', 0)
    if status_flag & 1:  # Indicates warm-up phase, reduce score
        raw_score *= 0.9

    # Final scoring with artificial complexity
    adjustment = len(extra_fields) * 5  # Unused distraction
    final_score = int(raw_score - penalty)

    # Irrelevant dictionary aggregation
    summary = {"score": final_score, "outliers": outlier_count}
    summary["debug"] = debug_log

    return final_score

# Main execution
baseline_config = {
    'throughput': 100,
    'latency': 50,
    'reliability': 0.95
}

system_metrics = {
    'throughput': 250,
    'latency': 75,
    'reliability': 0.98,
    'power_draw': 120,  # Not used in score
    'temperature': 68,   # Not used
    'status': 1          # Activates the bitwise flag
}

# Call function and output result
final_score = evaluate_performance(system_metrics, baseline_config)
print(f"Result: {final_score}")