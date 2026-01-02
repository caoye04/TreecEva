def evaluate_performance(weights, results):
    # Normalize results using min-max scaling (irrelevant for final logic but adds distraction)
    min_val, max_val = min(results.values()), max(results.values())
    normalized = {k: (v - min_val) / (max_val - min_val + 1e-8) for k, v in results.items()}

    # Apply weighted sum using lambda for dynamic computation
    weighted_sum = sum(map(lambda item: weights.get(item[0], 0.1) * item[1], results.items()))

    # Secondary metric: count how many exceed threshold (distractor)
    above_threshold = len([v for v in results.values() if v > 0.7])
    bonus_multiplier = 1.0
    if above_threshold > 2:
        bonus_multiplier = 1.1
    elif above_threshold == 1:
        bonus_multiplier = 0.95

    # Simulate penalty for inconsistency (unused path - dead code)
    variance = sum((v - sum(results.values()) / len(results)) ** 2 for v in results.values()) / len(results)
    if variance > 0.1:
        pass  # No actual effect, just misleading

    # Core calculation: transform weighted sum through nonlinear function
    adjusted_score = (weighted_sum ** 1.5) / 2.0

    # Artificial complexity: iterate to simulate convergence (only runs once)
    for i in range(1):
        adjusted_score = (adjusted_score + weighted_sum / adjusted_score) / 2

    # Final adjustment based on number of metrics (relevant)
    metric_count_factor = len(results) / 5.0  # assumes expected 5 metrics
    final_score = adjusted_score * metric_count_factor * bonus_multiplier

    return final_score

# Main execution
metric_weights = {'accuracy': 0.3, 'latency': 0.2, 'throughput': 0.25, 'memory': 0.15, 'robustness': 0.1}
raw_results = {'accuracy': 0.92, 'latency': 0.65, 'throughput': 0.88, 'memory': 0.71, 'robustness': 0.79}

# Extraneous variables (distractions)
dummy_data = [0.1, 0.2, 0.3]
temp_cache = {}
scaling_mode = 'linear'

def unused_helper():
    return sum(dummy_data)

final_score = evaluate_performance(metric_weights, raw_results)
print(f"Target result: {final_score}")