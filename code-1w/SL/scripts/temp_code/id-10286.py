def evaluate_performance(metrics, base):
    adjustment_factor = 0.85
    penalty_rate = 0.12
    temp_result = 0
    final_score = 0

    # Irrelevant tracking variables (distractors)
    outlier_count = 0
    normalized_values = []
    temp_aggregate = 0

    for val in metrics:
        if val > base * 1.5:
            outlier_count += 1
        normalized_values.append(val / (base + 1))

    # Actual computation path
    raw_total = sum(metrics)
    metric_average = raw_total / len(metrics)

    # Secondary distraction: unused complex transformation
    transformed = [x ** 0.5 for x in normalized_values if x > 0.5]
    temp_aggregate = sum(transformed)  # Not used later

    # Core logic with modular arithmetic and conditional scaling
    if metric_average >= base:
        stability_bonus = (metric_average % base) * 2.1
    else:
        stability_bonus = -((base - metric_average) // 3) * 0.7

    # Set difference operation (semi-relevant, distracts from main flow)
    metric_set = set(metrics)
    base_set = {base - 1, base, base + 1}
    unique_metrics = metric_set - base_set  # Distractor: computed but not critical

    # Main scoring formula
    base_component = metric_average * adjustment_factor
    risk_penalty = len([x for x in metrics if x < base]) * penalty_rate
    final_score = base_component + stability_bonus - risk_penalty

    # Red herring: this block doesn't alter anything
    if len(unique_metrics) > 2:
        dummy = 0
        for x in unique_metrics:
            dummy += x % 7
        temp_result = dummy / 2.0  # Dead code path

    return int(final_score)  # Deterministic integer result

# Input data
baseline = 42
metric_data = [38, 45, 47, 40, 39, 50, 44]

# Execution point of interest
final_score = evaluate_performance(metric_data, baseline)
print(f"Result: {final_score}")