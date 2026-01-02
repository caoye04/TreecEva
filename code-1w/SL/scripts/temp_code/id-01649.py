def evaluate_performance(data, limits):
    baseline = 100
    adjustment = 0
    penalty = 0
    temp_result = 0

    for key in data:
        if key in limits:
            if data[key] > limits[key]:
                adjustment += 2
                temp_result += data[key] * 0.1
            elif data[key] == limits[key]:
                adjustment += 1
            else:
                penalty += 1

    # Distractor: complex string analysis with no impact on final score
    status_msg = "Performance review complete."
    if status_msg.startswith("Perf") and len(status_msg) > 10:
        flagged_chars = {c for c in status_msg if c.isalpha()}
        adjustment -= len(flagged_chars) % 3  # Minor red herring adjustment

    # Distractor: unused recursive function
    def calculate_depth(n):
        return 1 if n <= 1 else n + calculate_depth(n - 2)

    # Distractor: irrelevant list processing
    samples = [i * 2 for i in range(5)]
    outlier_count = 0
    for val in samples:
        if val > 15:
            outlier_count += 1

    # Real logic resumes: apply net adjustment only if criteria met
    net_trend = adjustment - penalty
    if net_trend >= 0:
        baseline += net_trend * 5
    else:
        baseline -= abs(net_trend) * 2

    # Final score depends only on baseline and one transformed data element
    focus_metric = data.get('efficiency', 0)
    scaling_factor = 1.5 if focus_metric > limits.get('efficiency', 0) else 0.8
    final_component = focus_metric * scaling_factor

    result = baseline + final_component
    return int(result)

# Main execution context
metric_data = {
    'efficiency': 48,
    'latency': 12,
    'throughput': 8,
    'accuracy': 95
}

thresholds = {
    'efficiency': 45,
    'latency': 10,
    'throughput': 7,
    'accuracy': 90
}

# Irrelevant set operation (distractor)
used_keys = set(metric_data.keys()) & set(thresholds.keys())
redundant_calc = len(used_keys) ** 2

initial_guess = 97
final_score = 0  # Will be updated below

# Key statement
final_score = evaluate_performance(metric_data, thresholds)

print(f"Result: {final_score}")