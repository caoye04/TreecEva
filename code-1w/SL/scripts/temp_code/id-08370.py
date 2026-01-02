def evaluate_performance(metrics, base):
    adjustment_factor = 0.85
    threshold = 75
    penalty_rate = 0.1

    # Irrelevant metric tracking (distractor)
    historical_data = {2019: 68, 2020: 71, 2021: 73, 2022: 70}
    avg_historical = sum(historical_data.values()) / len(historical_data)

    # Core logic begins
    valid_metrics = {m for m in metrics if m >= threshold}  # set comprehension
    underperforming = {m for m in metrics if m < threshold}

    base_count = len([x for x in metrics if x == base])

    # Secondary adjustment using logical and arithmetic operations
    if len(valid_metrics) > 0 and base in valid_metrics:
        bonus = len(valid_metrics) * 2.5
    else:
        bonus = 0.0

    # Complex conditional expression with nested logic
    multiplier = 1.2 if (len(valid_metrics) >= 3 or (base > threshold and adjustment_factor > 0.8)) else 1.0

    # Simulated score calculation with distractor variables
    raw_score = sum(valid_metrics) / len(valid_metrics) if valid_metrics else 0
    penalty = len(underperforming) * penalty_rate * raw_score

    # Dead code path (irrelevant but plausible)
    if avg_historical < 72:
        adjustment_factor *= 1.05  # never actually used later

    projected_improvement = 0
    for i in range(3):
        projected_improvement += (raw_score * 0.05)  # irrelevant growth projection

    # Key computation
    final_score = (raw_score - penalty) * multiplier + bonus

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
metric_set = [88, 92, 76, 81, 64, 90]
baseline = 81
evaluate_performance(metric_set, baseline)