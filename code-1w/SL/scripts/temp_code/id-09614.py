def analyze_trend(data_points):
    trend_scores = {}
    for i, point in enumerate(data_points):
        if i == 0:
            trend_scores[i] = 0
        else:
            trend_scores[i] = data_points[i] - data_points[i-1]
    return trend_scores

# Simulate system health metrics over time
data_log = [100, 95, 98, 97, 102, 108, 105]

# Irrelevant transformation - distractor
distorted_log = [x * 1.05 for x in data_log]
distorted_log = [int(x) for x in distorted_log]

# Extract trend behavior
trends = analyze_trend(data_log)

# Define metric importance (weights)
metric_weights = {
    'stability': 0.3,
    'recovery': 0.4,
    'peak_gain': 0.3
}

# Compute auxiliary stats (semi-relevant)
stability_count = 0
for diff in trends.values():
    if abs(diff) <= 3:
        stability_count += 1

# Raw outcome components
raw_outcomes = {
    'stability': stability_count / len(trends),
    'recovery': sum(1 for i in range(1, len(data_log)) if data_log[i] > data_log[i-1]) / len(trends),
    'peak_gain': max(data_log) - min(data_log)
}

# Misleading normalization path - dead computation
normalized_peaks = []
for k, v in raw_outcomes.items():
    if k == 'peak_gain':
        norm_val = v / 50
        normalized_peaks.append(norm_val)

# Unused helper - distractor function
def adjust_for_noise(value, factor=0.95):
    return value * factor

# Actual evaluation logic
def evaluate_performance(weights, outcomes):
    score = 0.0
    for key in weights:
        if key == 'peak_gain':
            # Normalize peak gain to 0-1 scale based on expected max difference
            normalized_gain = outcomes['peak_gain'] / 20.0
            score += weights[key] * normalized_gain
        else:
            score += weights[key] * outcomes[key]
    return int(score * 100)  # Convert to integer percentage

# Final computation
temp_scaling = sum(raw_outcomes.values()) / 3  # Distractor calculation
final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Result: {final_score}")