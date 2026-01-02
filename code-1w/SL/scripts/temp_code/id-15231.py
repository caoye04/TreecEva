def evaluate_performance(metrics, weights):
    base = 0
    bonus = 0
    penalty = 0
    adjustment_factor = 1.0

    # Irrelevant temperature conversion (distractor)
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32

    # Summing relevant metric scores
    for key in metrics:
        if key in weights:
            base += metrics[key] * weights[key]

    # Bonus logic based on consistency (semi-relevant)
    values = list(metrics.values())
    if len(values) > 0:
        avg = sum(values) / len(values)
        if avg > 80:
            bonus = 10

    # Spurious statistical calculation (dead code)
    variance = sum((x - avg) ** 2 for x in values) / len(values) if values else 0
    std_dev = variance ** 0.5

    # Conditional penalty (not triggered)
    if metrics.get('reliability', 100) < 70:
        penalty = 5
    else:
        penalty = 0  # Explicit assignment for clarity

    # Unrelated data structure manipulation (tuples and dict copy)
    snapshot = tuple(metrics.items())
    temp_copy = metrics.copy()
    temp_copy['temp'] = 'irrelevant'

    # Final adjustment using a red herring variable
    red_herring_value = std_dev * adjustment_factor  # unused in logic

    final_score = int(base + bonus - penalty)
    return final_score

# Main execution
metrics_data = {
    'accuracy': 90,
    'latency': 85,
    'throughput': 75,
    'reliability': 95,
    'scalability': 80
}

weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.2,
    'reliability': 0.1
}

intermediate_total = sum(metrics_data[k] for k in ['accuracy', 'latency'])  # distractor calc

final_score = evaluate_performance(metrics_data, weights)
print(f"Result: {final_score}")