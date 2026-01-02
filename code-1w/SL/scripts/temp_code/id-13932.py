def evaluate_performance(metrics, threshold):
    score = 0
    penalty = 0
    bonus_tracker = []

    # Irrelevant string processing (distractor)
    system_logs = "error:456 warning:789 info:123"
    log_entries = system_logs.split(' ')
    error_count = sum(1 for log in log_entries if log.startswith("error"))

    # Real computation begins
    active_keys = [k for k in metrics.keys() if k.endswith('_active')]
    
    temp_sum = 0
    for key in active_keys:
        temp_sum += metrics[key]

    avg_activation = temp_sum / len(active_keys) if active_keys else 0

    # Misleading combinatorics (semi-relevant but unused later)
    from math import comb
    possible_combinations = comb(len(active_keys), 2) if len(active_keys) >= 2 else 0

    # Core logic with dictionary operations
    for k, v in metrics.items():
        if 'response' in k:
            normalized = v / (metrics.get(k + '_max', 1) or 1)
            if normalized > threshold:
                score += int(normalized * 10)
            else:
                penalty += 1

    # Bonus logic based on activation average
    if avg_activation > threshold:
        bonus_tracker.append(15)
    else:
        bonus_tracker.append(5)

    # Dummy recursion (distractor)
    def dummy_recursive(n):
        return n if n <= 1 else dummy_recursive(n-1) + dummy_recursive(n-2)
    
    _ = dummy_recursive(5)  # Dead computation

    # Final aggregation
    final_score = score - penalty * 2 + sum(bonus_tracker)

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Setup data
metric_map = {
    'latency_response': 0.85,
    'latency_response_max': 1.0,
    'throughput_response': 0.92,
    'throughput_response_max': 1.0,
    'cpu_active': 0.78,
    'memory_active': 0.65,
    'disk_active': 0.45,
    'network_active': 0.88
}
base_threshold = 0.7

final_score = evaluate_performance(metric_map, base_threshold)