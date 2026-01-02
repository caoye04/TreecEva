def analyze_trend(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    trend_ratio = len(above_threshold) / len(below_threshold) if below_threshold else 0
    return trend_ratio

# Simulate sensor readings over time
data_stream = [0.1, 0.4, 0.3, 0.8, 0.9, 0.2, 0.6, 0.7, 0.5]

# Misleading auxiliary calculation (distractor)
smoothed_data = [sum(data_stream[i:i+3]) / 3 for i in range(len(data_stream) - 2)]
noise_level = sum(1 for x in smoothed_data if abs(x - 0.5) < 0.1)

# Slice relevant segment for evaluation
segment = data_stream[2:7]
trend_value = analyze_trend(segment)

# Weighted metrics with red herring components
raw_metrics = {
    'stability': 1.0 - trend_value * 0.1,
    'consistency': len([x for x in segment if x == 0.3 or x == 0.8]),
    'peak_count': len([x for x in segment if x >= 0.8]),
    'baseline_drift': segment[-1] - segment[0],
    'entropy_proxy': trend_value  # Semi-relevant but disguised
}

# Irrelevant transformation (dead code path)
def calculate_entropy(values):
    from math import log
    total = sum(values)
    if total == 0:
        return 0
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

entropy_estimate = calculate_entropy(list(raw_metrics.values()))

# Real computation begins here
weights = [0.2, 0.3, 0.25, -0.1, 0.15]  # Negative weight for drift
metric_values = [
    raw_metrics['stability'],
    raw_metrics['consistency'],
    raw_metrics['peak_count'],
    abs(raw_metrics['baseline_drift']),  # Use absolute value
    raw_metrics['entropy_proxy']
]

# Actual scoring logic
weighted_sum = sum(value * weight for value, weight in zip(metric_values, weights))
normalization_factor = sum(abs(w) for w in weights)

# Final performance score
final_score = weighted_sum / normalization_factor if normalization_factor != 0 else 0

# Print result as required
print(f"Target result: {final_score}")