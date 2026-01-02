def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [round(m * 1.07 + 3, 2) for m in metrics]
    adjusted = []

    # Semi-relevant preprocessing
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted.append(val * 1.1)
        else:
            adjusted.append(val * 0.95)

    # Core logic: count how many exceed threshold with offset
    threshold_map = {i: thresholds[i % len(thresholds)] for i in range(len(metrics))}
    valid_count = 0
    penalty_factor = 0.0

    for i, metric in enumerate(metrics):
        if metric > threshold_map[i]:
            valid_count += 1
        else:
            penalty_factor += 0.05

    # Secondary distractor: unused statistical calculation
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    variance_proxy = sum((x - avg_normalized) ** 2 for x in normalized) / len(normalized)

    # Another red herring: complex but unused score variant
    robust_score = (sum(adjusted) / len(adjusted)) * (0.9 + penalty_factor) if adjusted else 0

    # Actual key computation
    base_score = sum(metrics) / len(metrics)
    bonus = valid_count * 2.5
    final_score = base_score + bonus - (penalty_factor * 100)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score


# Input data
performance_metrics = [88, 92, 76, 81, 95]
threshold_levels = [85, 75, 90]

# Call function
result = analyze_performance(performance_metrics, threshold_levels)
