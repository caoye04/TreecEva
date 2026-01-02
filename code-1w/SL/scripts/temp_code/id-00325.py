def analyze_trend(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    trend_value = len(above_threshold) - len(below_threshold)
    noise = sum([x * 0.1 for x in data])  # Irrelevant computation
    adjustment = 0
    if len(above_threshold) > 4:
        adjustment += 2
    return trend_value + adjustment


def calculate_stability(ratios):
    stability = 1.0
    for r in ratios:
        if r > 0:
            stability *= r
    inverse_sum = sum([1/(r+1e-5) for r in ratios])  # Distractor
    return min(stability, 10)


def filter_outliers(values, factor=1.5):
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    filtered = [v for v in values if lower_bound <= v <= upper_bound]
    outlier_count = len(values) - len(filtered)  # Unused
    return filtered

# Simulated sensor metrics over time
sensor_readings = [0.6, 0.7, 0.3, 0.8, 0.9, 0.2, 0.4, 0.65, 0.75, 0.1]

# Irrelevant preprocessing
normalized = [round(x * 1.05, 3) for x in sensor_readings]
sorted_vals = sorted(normalized, reverse=True)
duplicate_check = {x: normalized.count(x) for x in set(normalized)}

# Extract key performance indicators
trend_metrics = analyze_trend(sensor_readings, threshold=0.55)
ratio_sequence = [0.6/0.7, 0.3/0.8, 0.9/0.2, 0.65/0.75, 0.4/0.1]
stability_score = calculate_stability(ratio_sequence)

# Weighted components
weights = {
    'trend': 0.4,
    'stability': 0.35,
    'consistency': 0.25
}

# Simulate consistency via filtered variance
clean_data = filter_outliers(sensor_readings, factor=2.0)
mean_clean = sum(clean_data) / len(clean_data)
consistency_dev = sum([(x - mean_clean)**2 for x in clean_data])
consistency_score = 10 - min(consistency_dev * 2, 10)  # Scaled down

# Assemble metrics
dummy_metric = sum([int(x*10) for x in sorted_vals[:3]])  # Dead code path
metrics = {
    'trend': max(trend_metrics, 0),
    'stability': stability_score,
    'consistency': consistency_score
}

# Final evaluation function
def evaluate_performance(perf_dict, weight_dict):
    total = 0.0
    for key in perf_dict:
        if key in weight_dict:
            total += perf_dict[key] * weight_dict[key]
    calibration = 1.0
    if total > 5:
        calibration = 0.95
    elif total < 3:
        calibration = 1.05
    return int(total * calibration)  # Final integral score

# Execute critical statement
final_score = evaluate_performance(metrics, weights)

# Print result
print(f"Result: {final_score}")