def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final logic)
    max_metric = max(metrics.values())
    min_metric = min(metrics.values())
    normalized = {k: (v - min_metric) / (max_metric - min_metric + 1e-8) for k, v in metrics.items()}

    # Weighted sum calculation - this is the key path
    weighted_sum = 0.0
    temp_debug = []
    for key, value in metrics.items():
        if key in weights:
            contribution = value * weights[key]
            weighted_sum += contribution
            temp_debug.append(contribution)  # Logged but not used

    # Additional distraction: simulate threshold filtering
    passing_metrics = set()
    for k, v in metrics.items():
        if v > 70:
            passing_metrics.add(k)
    
    # Simulate bonus condition (never triggered due to data)
    bonus_awarded = False
    if len(passing_metrics) >= 10:
        weighted_sum *= 1.1
        bonus_awarded = True

    # Distractor: unused transformation
    squared_metrics = {k: v**2 for k, v in metrics.items()}
    avg_square = sum(squared_metrics.values()) / len(squared_metrics)

    # Final adjustment based on diversity of metric values
    unique_values = set(int(v) for v in metrics.values())
    diversity_bonus = len(unique_values) * 0.5
    
    final_score = weighted_sum + diversity_bonus

    return final_score

# Main execution context
metrics = {
    'latency': 85,
    'throughput': 92,
    'accuracy': 78,
    'reliability': 88,
    'scalability': 95,
    'usability': 73,
    'security': 91
}

weights = {
    'latency': 0.15,
    'throughput': 0.20,
    'accuracy': 0.25,
    'reliability': 0.10,
    'scalability': 0.15,
    'usability': 0.08,
    'security': 0.07
}

# Irrelevant pre-computations
baseline_avg = sum(metrics.values()) / len(metrics)
metric_variance = sum((v - baseline_avg) ** 2 for v in metrics.values()) / len(metrics)
adjusted_metrics = {k: v * 1.02 for k, v in metrics.items() if v < 80}  # Unused

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")