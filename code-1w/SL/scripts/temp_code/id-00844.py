def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final score but adds distraction)
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics)) if max(metrics) != min(metrics) else 0 for m in metrics]

    # Apply weighted sum using lambda for element-wise multiplication
    weighted_sum = sum(map(lambda x: x[0] * x[1], zip(metrics, weights)))

    # Calculate harmonic mean as alternative metric (distractor)
    harmonic_mean = len(metrics) / sum(1/m if m != 0 else 0 for m in metrics) if all(m != 0 for m in metrics) else 0

    # Track state across iterations (semi-relevant tracking)
    cumulative = 0
    history = []
    for val in metrics:
        cumulative += val
        if cumulative > 50:  # arbitrary threshold
            history.append(cumulative)
            cumulative = 0  # reset counter

    # Compute efficiency ratio (not used in final score - red herring)
    efficiency_ratio = len(history) / (sum(metrics) or 1)

    # Actual scoring logic: clip weights to [0.1, 0.9], then compute capped weighted sum
    clipped_weights = [max(0.1, min(0.9, w)) for w in weights]
    capped_weighted_sum = sum(m * cw for m, cw in zip(metrics, clipped_weights))

    # Bonus adjustment if more than half metrics exceed 40
    high_performers = len([m for m in metrics if m > 40])
    bonus = 10 if high_performers > len(metrics) // 2 else 0

    # Final score calculation point
    final_score = capped_weighted_sum + bonus
    return final_score

# Main execution context
metrics_data = [45, 38, 52, 61, 43]
weight_scheme = [1.2, -0.3, 0.85, 0.7, 1.5]  # some out-of-bounds values to be clipped

# Irrelevant preprocessing: reverse slice and set intersection (adds complexity without impact)
decoy_data = metrics_data[::-1]
overlap_check = set(metrics_data) & set([38, 43, 55, 61])
filtered_metrics = [x for x in metrics_data if x in overlap_check]  # subset that isn't used later

# Unused helper function simulating dead code path
def debug_trace(data):
    return [f"Value:{d}:Status=OK" for d in data]

# Key statement execution
target_result = evaluate_performance(metrics_data, weight_scheme)
print(f"Result: {target_result}")