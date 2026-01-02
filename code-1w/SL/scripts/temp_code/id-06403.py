def analyze_trends(raw_values, base_threshold=0.5):
    trends = []
    cumulative = 0
    for i, val in enumerate(raw_values):
        deviation = val - base_threshold
        if deviation > 0:
            trends.append((i, 'positive', deviation))
        elif deviation < 0:
            trends.append((i, 'negative', deviation))
        else:
            trends.append((i, 'neutral', 0))
        cumulative += abs(deviation)
    
    avg_deviation = cumulative / len(raw_values) if raw_values else 0
    return trends, avg_deviation


def normalize_dataset(entries):
    min_val, max_val = min(entries), max(entries)
    range_val = max_val - min_val if max_val != min_val else 1
    normalized = [(x - min_val) / range_val for x in entries]
    return normalized

# Simulate sensor data from three sources
data_stream_a = [0.3, 0.7, 0.4, 0.9, 0.2]
data_stream_b = [0.6, 0.8, 0.5, 0.7, 0.3]
data_stream_c = [0.4, 0.6, 0.3, 0.8, 0.5]

# Combine using zip and calculate element-wise averages
combined_data = [sum(x)/3 for x in zip(data_stream_a, data_stream_b, data_stream_c)]

# Normalize the combined data
normalized_data = normalize_dataset(combined_data)

# Analyze trend patterns (this result is not used in final score but adds distraction)
trend_analysis, avg_variation = analyze_trends(normalized_data, base_threshold=0.4)

# Define metric weights for performance evaluation
metric_weights = {
    'stability': 0.3,
    'consistency': 0.25,
    'response_rate': 0.2,
    'outlier_resistance': 0.25
}

# Dummy variables to increase cognitive load
baseline_metrics = {k: 0.75 for k in metric_weights}
drift_compensation = sum([abs(a-b) for a,b in zip(data_stream_a, data_stream_b)]) / len(data_stream_a)

# Auxiliary function to compute consistency score
def measure_consistency(values):
    diffs = [abs(values[i] - values[i+1]) for i in range(len(values)-1)]
    return 1 - (sum(diffs) / len(diffs)) if diffs else 1

# Compute various intermediate scores
stability_score = 1 - avg_variation
consistency_score = measure_consistency(normalized_data)

# Simulate response rate based on threshold crossings
threshold_crossings = sum(1 for x in normalized_data if x > 0.6)
response_rate_score = threshold_crossings / len(normalized_data)

# Outlier detection using set operations
high_outliers = {i for i, x in enumerate(normalized_data) if x > 0.9}
low_outliers = {i for i, x in enumerate(normalized_data) if x < 0.1}
outlier_set = high_outliers | low_outliers
outlier_resistance_score = 1 - (len(outlier_set) / len(normalized_data))

# Final performance evaluation
def evaluate_performance(weights, norm_data):
    # Recompute some already computed values (distractor)
    dummy_trend_check = [x for x in norm_data if x > 0.5]
    dummy_ratio = len(dummy_trend_check) / len(norm_data) if norm_data else 0
    
    # Actual scoring
    s1 = stability_score * weights['stability']
    s2 = consistency_score * weights['consistency']
    s3 = response_rate_score * weights['response_rate']
    s4 = outlier_resistance_score * weights['outlier_resistance']
    total = s1 + s2 + s3 + s4
    return round(total, 4)

# Key execution point
final_score = evaluate_performance(metric_weights, normalized_data)

# Unused debug print that could distract
# print('Trend:', trend_analysis[:2])

Result: {final_score}