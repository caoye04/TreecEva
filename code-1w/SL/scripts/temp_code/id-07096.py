def evaluate_performance(metrics, weights):
    # Initialize intermediate variables (some are distractions)
    baseline = 100
    adjustment_factor = 0.95
    temp_result = 0
    cumulative = 0
    
    # Irrelevant computation - dead path
    if len(metrics) > 10:
        baseline *= 2
        temp_result += 50

    # Real logic begins: weighted sum with lambda for dynamic scaling
    scale_fn = lambda x, w: x * w * adjustment_factor
    
    # Distractor: unused helper function
    def dummy_helper(val):
        return (val ** 2 + 10) // 3
    
    # Main processing loop with dictionary operations
    for key in metrics:
        if key in weights:
            raw_value = metrics[key]
            # Apply scaling only if metric meets threshold
            if raw_value >= 50:
                scaled = scale_fn(raw_value, weights[key])
                cumulative += scaled
            else:
                cumulative += raw_value * 0.5  # Penalty for low performance

    # Bitwise manipulation as red herring (does not affect final result)
    masked_cumulative = int(cumulative) ^ 0xFF & 0x0F
    
    # Another distraction: unused max calculation
    peak_metric = max(metrics.values()) if metrics else 0
    normalized_peak = (peak_metric >> 2) * 1.1
    
    # Final adjustment using relevant logic
    stability_bonus = 10 if all(v >= 40 for v in metrics.values()) else 0
    final_score = int(cumulative + stability_bonus)
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Input data
metrics = {
    'latency': 85,
    'throughput': 92,
    'reliability': 78,
    'scalability': 65
}

weights = {
    'latency': 0.3,
    'throughput': 0.4,
    'reliability': 0.2,
    'scalability': 0.1
}

# Key execution point
final_score = evaluate_performance(metrics, weights)