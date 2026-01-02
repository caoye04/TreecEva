def evaluate_performance(metrics, data_map):
    base_weights = {'accuracy': 0.4, 'latency': -0.2, 'memory': -0.1, 'throughput': 0.3}
    adjustment_factor = 1.2
    temp_offset = 0.05
    
    # Irrelevant metric scaling (distractor)
    scaled_metrics = {k: v * adjustment_factor for k, v in base_weights.items()}
    inverse_weights = {k: 1 - v for k, v in base_weights.items()}

    score = 0.0
    penalty = 0.0
    
    # Real computation begins
    active_keys = set(base_weights.keys()) & set(data_map.keys())
    
    for key in active_keys:
        if key == 'accuracy':
            score += base_weights[key] * data_map[key]
        elif key == 'throughput':
            score += base_weights[key] * (data_map[key] / 100)
        else:
            # latency and memory contribute negatively
            penalty += abs(base_weights[key] * data_map[key])
    
    # Dummy loop with no effect (dead code path - distractor)
    cumulative = 0
    for i in range(3):
        for j in range(2):
            cumulative += i * j * temp_offset

    final_score = score - penalty
    
    # Additional irrelevant dictionary operation (set distraction)
    unused_combo = set(scaled_metrics.keys()) ^ set(inverse_weights.keys())
    
    return final_score

# Benchmark data input
benchmark_data = {
    'accuracy': 92,
    'latency': 15,
    'throughput': 220,
    'memory': 105
}

metric_set = {'accuracy', 'throughput', 'f1_score'}

# Execute evaluation
temp_result = evaluate_performance(metric_set, benchmark_data)
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")