def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result)
    normalized = {}
    for k, v in metrics.items():
        normalized[k] = (v - 50) / 50 if v > 50 else 0.0

    # Irrelevant aggregation: harmonic mean (not used in final computation)
    harmonic_mean = 0
    if all(v > 0 for v in metrics.values()):
        harmonic_mean = len(metrics) / sum(1/v for v in metrics.values())

    # Weighted sum calculation — only this affects the final result
    weighted_sum = sum(metrics[metric] * weight for metric, weight in weights.items() if metric in metrics)

    # Simulated adjustment based on threshold logic
    adjustment = 0
    if metrics['accuracy'] > 75:
        adjustment += 10
    if metrics['latency'] < 100:
        adjustment -= 5  # penalty reduction

    # Final score computed here
    final_score = weighted_sum + adjustment

    # Dead code path: never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: {normalized}, Harmonic: {harmonic_mean}')

    return final_score

# Main execution block
metrics = {
    'accuracy': 85,
    'latency': 95,
    'throughput': 120,
    'memory_usage': 60
}

weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.2,
    'memory_usage': 0.1
}

# Auxiliary data structures for distraction (unused in final logic)
data_points = [(x, x**2) for x in range(10) if x % 2 == 0]
log_entries = set(['init', 'load', 'process', 'init'])  # duplicate removed
summary_stats = {k: v * 1.05 for k, v in metrics.items()}

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f'Result: {final_score}')