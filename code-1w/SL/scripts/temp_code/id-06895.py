def evaluate_performance(metrics, thresholds):
    # Irrelevant preprocessing: normalize unrelated dimensions
    normalized = {k: v / (sum(metrics.values()) + 1e-5) for k, v in metrics.items()}
    weighted = {k: v * 1.5 for k, v in normalized.items()}

    # Distractor: complex set operations with no impact
    all_keys = set(metrics.keys())
    required_keys = {'accuracy', 'latency', 'memory'}
    missing = required_keys - all_keys
    extra = all_keys - required_keys
    completeness = len(required_keys - missing) / len(required_keys)

    # Semi-relevant slicing on sorted values (only top 2 matter later)
    sorted_metrics = sorted(metrics.values(), reverse=True)
    top_two_avg = sum(sorted_metrics[:2]) / 2
    bottom_slice = sorted_metrics[-2:]  # unused

    # Core logic begins: threshold checks
    passed = 0
    for key in ['accuracy', 'latency', 'memory']:
        if key not in metrics:
            continue
        if key == 'accuracy':
            if metrics[key] >= thresholds[key]:
                passed += 1
        elif key == 'latency':
            if metrics[key] <= thresholds[key]:  # lower is better
                passed += 1
        elif key == 'memory':
            if metrics[key] <= thresholds[key]:
                passed += 1

    # Secondary logic: adjust by top-two average only if at least 2 passed
    adjustment_factor = 1.0
    if passed >= 2:
        adjustment_factor = min(1.2, top_two_avg / 80)  # scales up to 1.2 if top_two_avg >= 96

    # Final score computation
    base_score = passed * 25
    final_score = int(base_score * adjustment_factor)

    # Dead code path - never executed due to logic above
    if completeness < 0.5:
        final_score = -1  # invalid case, won't trigger

    return final_score

# Input data
metrics = {
    'accuracy': 92,
    'latency': 45,
    'memory': 1024,
    'throughput': 230,      # irrelevant metric
    'power': 78             # irrelevant metric
}
thresholds = {
    'accuracy': 90,
    'latency': 50,
    'memory': 1024
}

# Key execution point
final_score = evaluate_performance(metrics, thresholds)
print(f"Result: {final_score}")