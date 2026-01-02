def analyze_performance(metrics, thresholds):
    # Irrelevant transformation: bit manipulation red herring
    temp_data = [m ^ 255 for m in metrics if m > 10]
    masked_values = [t << 2 for t in thresholds]

    # Distractor: unused function call setup
    baseline = sum(thresholds) // len(thresholds)
    offset = baseline & 0xFF
    adjustment = offset + 17

    # Real logic begins: filtering and weighted scoring
    filtered = [m for m in metrics if 5 <= m <= 50]
    weights = [0.1, 0.2, 0.3, 0.4]
    weighted_sum = 0.0

    # Nested loop with enumerate and zip – actual computation path
    for i, val in enumerate(filtered):
        for j, thr in enumerate(thresholds):
            if i == j:
                weighted_sum += val * weights[i]

    # Decoy branching: looks important but doesn't affect final result
    if len(filtered) > len(thresholds):
        extra_penalty = 12
        normalized = weighted_sum - extra_penalty
    else:
        extra_penalty = 0
        normalized = weighted_sum

    # Critical distraction: multiple similar variables
    preliminary_score = int(weighted_sum)
    adjusted_score = preliminary_score + adjustment  # misleading!

    # Actual answer derivation (obscured by noise)
    scale_factor = 1.75
    raw_result = normalized * scale_factor

    # Dead code path: never executed due to data constraints
    overflow_correction = 0
    for x in temp_data:
        if x < 0:
            overflow_correction += 1

    # Key statement: final_score assignment
    final_score = int(raw_result + 0.5)  # rounding

    # More irrelevant cleanup
    cleanup_flags = [False] * len(metrics)
    for idx, m in enumerate(metrics):
        cleanup_flags[idx] = (m % 2 == 0)

    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    metrics = [8, 15, 22, 45, 12]
    thresholds = [10, 18, 25, 40]

    # Unused decoy variables
    shadow_metrics = [m | 0xAAAA for m in metrics]
    inverted_thresholds = [~t for t in thresholds]
    dummy_calc = sum(shadow_metrics) % 997

    # Critical execution point
    final_score = analyze_performance(metrics, thresholds)

    # Output result
    print(f"Result: {final_score}")