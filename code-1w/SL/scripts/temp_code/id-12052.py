def evaluate_performance(metrics, weights):
    # Normalize metrics (irrelevant for final result but adds cognitive load)
    normalized = {k: v / sum(metrics.values()) for k, v in metrics.items()}
    
    # Distractor: Compute entropy-like value (not used in final calculation)
    import math
    entropy = sum(-v * math.log(v) for v in normalized.values() if v > 0)
    temp_debug = f'Entropy: {entropy:.4f}'

    # Weighted sum computation (core logic)
    weighted_sum = 0
    for metric_name, value in metrics.items():
        weight = weights.get(metric_name, 0.1)
        contribution = value * weight
        weighted_sum += contribution

    # Additional distraction: simulate data smoothing
    smoothed_metrics = [0.9 * v + 0.1 for v in metrics.values()]
    avg_smoothed = sum(smoothed_metrics) / len(smoothed_metrics)
    adjustment_factor = avg_smoothed > 85  # boolean, not used

    # Secondary distractor path: unused conditional branch
    if len(metrics) > 10:
        fallback = sum(smoothed_metrics) * 0.05
    else:
        fallback = 0  # dead end

    # Final score computed via list comprehension (key step)
    bonuses = [10 if v >= 90 else 2 for v in metrics.values()]
    total_bonus = sum(bonuses) // len(bonuses)  # average bonus as integer

    final_score = int(weighted_sum + total_bonus)

    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    metrics = {
        'latency_ms': 87,
        'throughput_tps': 93,
        'error_rate': 76,
        'availability': 95,
        'scalability_index': 88
    }
    weights = {
        'latency_ms': 0.2,
        'throughput_tps': 0.3,
        'error_rate': 0.15,
        'availability': 0.25,
        'scalability_index': 0.1
    }

    # Irrelevant pre-processing
    metric_list = list(metrics.keys())
    sorted_pairs = sorted(metrics.items(), key=lambda x: x[1], reverse=True)
    median_value = sorted(metrics.values())[len(metrics)//2]

    # Key statement
    final_score = evaluate_performance(metrics, weights)

    # Output result
    print(f"Result: {final_score}")