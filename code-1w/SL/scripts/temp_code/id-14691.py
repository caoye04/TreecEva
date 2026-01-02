def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda for dynamic scaling
    normalized = list(map(lambda x: x / max(metrics) if max(metrics) != 0 else 0, metrics))

    # Irrelevant distraction: Compute variance (not used in final result)
    mean_metric = sum(metrics) / len(metrics)
    variance = sum((x - mean_metric) ** 2 for x in metrics) / len(metrics)
    std_dev = variance ** 0.5

    # Weighted aggregation with misleading intermediate blends
    raw_weighted = sum(m * w for m, w in zip(normalized, weights))
    adjustment_factor = 1.0 + (sum(weights) - 1.0) / len(weights)  # Always 1.0 due to weight normalization

    # Conditional bonus logic based on performance thresholds (mostly not triggered)
    bonus = 0.0
    if all(m > 0.5 for m in normalized):
        bonus = 0.1
    elif normalized[0] > 0.7 and normalized[2] > 0.6:
        bonus = 0.05

    # Simulate legacy compatibility mode (dead code path, never executed)
    legacy_mode = False
    legacy_score = 0
    if legacy_mode:
        legacy_score = sum(m * 0.33 for m in metrics)

    # Final score calculation
    final_score = raw_weighted * adjustment_factor + bonus
    return final_score

# Main execution context
metrics = [85, 90, 78, 92]
weights = [0.25, 0.25, 0.25, 0.25]

# Red herring: unused data structure
performance_log = {
    'entries': [],
    'version': '2.1',
    'debug': False
}

# Additional distraction: spurious loop with no side effects
for i in range(3):
    temp = i ** 2 - i
    performance_log['entries'].append(temp)  # Only modifies log, not used later

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")