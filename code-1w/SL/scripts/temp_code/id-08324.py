def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation
    temp_data = {k: v * 1.05 for k, v in metrics.items()}
    adjusted = {}
    for key in metrics:
        if key == 'latency':
            adjusted[key] = max(0, 100 - metrics[key])
        elif key == 'throughput':
            adjusted[key] = min(100, (metrics[key] / 500) * 100)
        elif key == 'accuracy':
            adjusted[key] = metrics[key] * 100
    
    # Distractor: unused computation
    outlier_count = 0
    values = list(metrics.values())
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    for v in values:
        if abs(v - mean_val) > 2 * (variance ** 0.5):
            outlier_count += 1

    # Semi-relevant sorting
    sorted_keys = sorted(adjusted.keys(), key=lambda k: adjusted[k], reverse=True)
    
    # Weighted scoring with fixed weights
    weights = {'latency': 0.4, 'throughput': 0.35, 'accuracy': 0.25}
    raw_score = 0
    for metric, weight in weights.items():
        raw_score += adjusted[metric] * weight
    
    # Threshold penalty system (only triggers if below threshold)
    penalty = 0
    for key in thresholds:
        if metrics.get(key, 0) < thresholds[key]:
            penalty += 10
    
    # Final adjustment based on penalty and bonus logic
    bonus = 5 if metrics['accuracy'] >= 0.95 and metrics['throughput'] > 400 else 0
    final_score = raw_score - penalty + bonus
    
    # Dead code branch (never executed under current inputs)
    if False:
        fallback = sum(adjusted.values()) / len(adjusted)
        final_score = max(final_score, fallback)
    
    return final_score

# Main execution
metrics = {
    'latency': 20,      # milliseconds
    'throughput': 450,   # requests/sec
    'accuracy': 0.92     # model precision
}
thresholds = {
    'latency': 25,
    'throughput': 420,
    'accuracy': 0.9
}

# Intermediate irrelevant calculation
snapshot = tuple(sorted((v for v in metrics.values()), reverse=True))
checksum = snapshot[0] * 2 + snapshot[1] * 1 + snapshot[2] * 3

final_score = evaluate_performance(metrics, thresholds)
print(f"Result: {final_score}")