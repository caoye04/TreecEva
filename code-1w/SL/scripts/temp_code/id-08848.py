def evaluate_performance(metrics, weights):
    base = 0
    bonus = 0
    penalty = 0
    adjustment_factor = 1.0

    # Irrelevant intermediate calculation (distractor)
    temp_sum = sum([v**2 for v in metrics.values() if v > 5])
    temp_avg = temp_sum / len(metrics) if metrics else 1

    # Real computation begins
    for key, value in metrics.items():
        weight = weights.get(key, 1)
        contribution = value * weight

        if value >= 8:
            bonus += contribution * 0.1
        elif value < 5:
            penalty += contribution * 0.15

        base += contribution

    # Another distractor: unused conditional path
    if base > 100:
        adjustment_factor = 0.95
    elif base < 30:
        adjustment_factor = 1.05

    # Actual adjustment not based on above
    stability_check = all(v >= 4 for v in metrics.values())
    sector_boost = {'network': 1.1, 'compute': 1.05, 'storage': 1.0}
    
    for component in metrics:
        if component in sector_boost:
            base *= sector_boost[component]
            break  # Only apply first boost

    final_score = base + bonus - penalty

    # Dead code - never executed due to logic
    if False:
        final_score = max(final_score, 50)

    return int(final_score)

# Main execution
metrics = {
    'network': 9,
    'compute': 7,
    'storage': 6,
    'latency': 4,
    'throughput': 8
}

weights = {
    'network': 1.2,
    'compute': 1.0,
    'storage': 0.9,
    'throughput': 1.1
}

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")