def evaluate_performance(data, importance):
    base = sum(data.values())
    adjustments = 0
    temp_factor = 0

    # Irrelevant computation: tracking unused stats
    max_val = max(data.values())
    min_val = min(data.values())
    range_val = max_val - min_val
    temp_factor += range_val * 0.1

    # Real logic begins: weighted contribution
    weighted_sum = sum(data[k] * importance.get(k, 1) for k in data)

    # Distractor: complex lambda that isn't used later
    analyze = lambda x: (x ** 0.5 if x > 0 else 0) + len(importance)
    unused_analysis = [analyze(v) for v in data.values()]

    # Conditional adjustment based on threshold
    if base > 50:
        adjustments -= 5
    else:
        adjustments += 10

    # Set operation to filter high-importance keys (real use)
    key_set_a = set(importance.keys())
    key_set_b = set(['accuracy', 'latency', 'memory'])
    critical_dims = key_set_a & key_set_b  # intersection
    adjustments += len(critical_dims) * 2

    # More irrelevant variables
    phantom_score = base * 0.01
    debug_trace = []
    for k in data:
        debug_trace.append(f'{k}: {data[k]}')

    # Final score calculation (depends on prior steps)
    final_score = weighted_sum + adjustments

    return final_score

# Main execution
metrics = {
    'accuracy': 85,
    'latency': 45,
    'memory': 60,
    'throughput': 70
}

weights = {
    'accuracy': 1.2,
    'latency': 0.8,
    'memory': 1.0,
    'energy': 0.5  # Note: not in metrics
}

result = evaluate_performance(metrics, weights)
final_score = result
print(f"Target result: {final_score}")