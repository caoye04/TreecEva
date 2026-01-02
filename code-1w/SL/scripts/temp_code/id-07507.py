def evaluate_performance(data, weights):
    # Normalize data using min-max scaling (irrelevant for final logic but adds distraction)
    normalized = {k: (v - min(data.values())) / (max(data.values()) - min(data.values())) if max(data.values()) != min(data.values()) else 0 for k, v in data.items()}

    # Misleading transformation with lambda (not used later)
    transformed = list(map(lambda x: x ** 0.5 if x > 0 else 0, data.values()))

    # Key computation path begins here
    weighted_sum = 0
    total_weight = sum(weights.values())

    for metric, raw_value in data.items():
        if metric in weights:
            contribution = raw_value * weights[metric]
            weighted_sum += contribution

    # Simulate threshold-based adjustment using conditional expression
    adjustment_factor = 1.1 if weighted_sum > 85 else (0.95 if weighted_sum > 70 else 0.8)

    # Apply adjustment
    adjusted_score = weighted_sum * adjustment_factor

    # Distractor: complex string processing unrelated to result
    status_msg = "Performance: PASS" if adjusted_score >= 75 else "Performance: FAIL"
    tokens = status_msg.lower().split(':')
    code_word = ''.join([t[0] for t in tokens]).upper()  # DEAD CODE PATH

    # Another red herring: set operations with no impact
    valid_categories = {'speed', 'accuracy', 'reliability', 'efficiency'}
    observed = set(data.keys())
    missing = valid_categories - observed  # Computed but unused

    # Final score calculation – depends only on weighted_sum and adjustment
    final_score = int(round(adjusted_score))

    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    metrics = {
        'speed': 90,
        'accuracy': 88,
        'reliability': 82,
        'efficiency': 76
    }

    benchmark_weights = {
        'speed': 0.4,
        'accuracy': 0.3,
        'reliability': 0.2,
        'efficiency': 0.1
    }

    # Irrelevant pre-computation (distractor)
    avg_metric = sum(metrics.values()) / len(metrics)
    squared_deviations = [(v - avg_metric) ** 2 for v in metrics.values()]
    variance_estimate = sum(squared_deviations) / (len(squared_deviations) - 1) if len(squared_deviations) > 1 else 0

    # Key statement
    final_score = evaluate_performance(metrics, benchmark_weights)

    print(f"Result: {final_score}")