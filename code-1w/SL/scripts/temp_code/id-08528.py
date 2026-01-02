def evaluate_performance(data, config):
    # Irrelevant transformation
    temp_data = [x * 1.05 for x in data]
    adjusted = [max(0, x - 0.5) for x in temp_data]

    # Distractor: complex-looking but unused calculation
    outlier_count = 0
    for val in adjusted:
        if val > 90:
            outlier_count += 1
    secondary_adjustment = outlier_count * 0.75

    # Real logic begins: normalize data using min-max scaling
    min_val = min(adjusted)
    max_val = max(adjusted)
    if max_val == min_val:
        normalized = [0 for _ in adjusted]
    else:
        normalized = [(x - min_val) / (max_val - min_val) for x in adjusted]

    # Weighted sum using configuration
    weighted_sum = 0
    for i in range(len(normalized)):
        weighted_sum += normalized[i] * config[i]

    # Apply non-linear boost (sigmoid-like) if performance is high
    boosted_score = 100 * (weighted_sum / (1 + weighted_sum))

    # Final adjustment based on trend in last 3 metrics (slicing used here)
    recent_trend = normalized[-3:]
    trend_slope = (recent_trend[2] - recent_trend[0]) * 50  # Amplified slope

    # Only positive trends give bonus
    if trend_slope > 0:
        boosted_score += trend_slope

    return int(round(boosted_score))

# Main execution
raw_metrics = [85, 92, 78, 88, 95, 87, 90]
weights = [0.1, 0.15, 0.1, 0.2, 0.15, 0.1, 0.2]

# Irrelevant preprocessing
scaled_metrics = [x * 1.1 for x in raw_metrics]
decay_factor = 0.95
filtered_metrics = [x for x in scaled_metrics if x > 80]

# More distraction: tuple unpacking and unused grouping
group_a, group_b = (raw_metrics[:4], raw_metrics[4:])
summary_stats = (sum(group_a), len(group_a), sum(group_b), len(group_b))

# Core computation chain
processed = [min(x, 100) for x in raw_metrics]  # Cap at 100
smoothed = [round(x * 1.02, 1) for x in processed]  # Minor enhancement

# Key assignment with slicing influence
window_avg = sum(smoothed[1:6]) / 5
reference_point = smoothed[3]

# Actual evaluation call
final_score = evaluate_performance(smoothed, weights)

print(f"Result: {final_score}")