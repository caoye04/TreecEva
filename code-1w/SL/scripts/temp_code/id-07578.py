def evaluate_performance(metrics, weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = {}

    # Initialize tracking for various performance dimensions
    for key in metrics:
        if key not in bonus_tracker:
            bonus_tracker[key] = 0

    # Apply weighted scoring with conditional bonuses
    temp_values = []
    for i, (k, v) in enumerate(metrics.items()):
        weight = weights.get(k, 1.0)
        raw_contribution = v * weight
        
        # Conditional bonus logic based on threshold
        if v > 80 and k in ['efficiency', 'reliability', 'latency']:
            bonus_tracker[k] = 5
        elif v < 50:
            penalty_adjustment -= 3
        
        temp_values.append(raw_contribution)

    # Simulated noise calculation (not actually used in final result)
    noise_accumulator = 0
    for t in temp_values:
        if t > 100:
            noise_accumulator += t % 7
        else:
            noise_accumulator -= t // 10

    # Actual score computation
    base_score = sum(temp_values)
    bonus_sum = sum(bonus_tracker.values())
    
    # Irrelevant secondary loop – dead computation path
    debug_log = {}
    for metric_name in ['throughput', 'efficiency', 'reliability']:
        status_flag = 'high' if metrics.get(metric_name, 0) > 75 else 'low'
        debug_log[metric_name] = {'flag': status_flag, 'offset': 0}

    final_score = base_score + bonus_sum + penalty_adjustment
    return final_score

# Main execution context
metrics = {
    'efficiency': 85,
    'reliability': 92,
    'latency': 45,
    'throughput': 67,
    'bandwidth': 73
}

weights = {
    'efficiency': 1.2,
    'reliability': 1.5,
    'latency': 0.8,
    'throughput': 1.0,
    'bandwidth': 0.9
}

intermediate_result = [x * 0.5 for x in range(10)]  # Unused auxiliary list

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")