def analyze_trends(data, threshold=5.0):
    trends = []
    for i in range(1, len(data)):
        change = data[i] - data[i-1]
        if abs(change) > threshold:
            trends.append('significant')
        elif change > 0:
            trends.append('positive')
        else:
            trends.append('stable')
    return trends

# Simulate sensor readings over time
temperature_data = [20.1, 22.5, 25.3, 25.4, 28.9, 30.2, 29.8, 27.6]

trend_analysis = analyze_trends(temperature_data, threshold=2.0)

# Irrelevant auxiliary computation (distractor)
deviation_count = 0
for val in temperature_data:
    if val > sum(temperature_data) / len(temperature_data):
        deviation_count += 1

# Core metric calculation with slicing and weighting
baseline = temperature_data[:4]
current_phase = temperature_data[4:]

# Compute moving averages using slicing
moving_averages = []
for i in range(len(current_phase)):
    window = temperature_data[max(0, i+4-3):i+4]
    moving_averages.append(sum(window) / len(window))

# Set operations to identify unique trend transitions
unique_transitions = set()
for i in range(len(trend_analysis) - 1):
    transition = (trend_analysis[i], trend_analysis[i+1])
    unique_transitions.add(transition)

# Distractor: unused helper function
def normalize_values(arr):
    min_val, max_val = min(arr), max(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Dictionary-based weight assignment
weights = {
    'significant': 3.0,
    'positive': 1.5,
    'stable': 1.0
}

# Metric scoring based on trend frequency
metrics = {}
for trend in trend_analysis:
    metrics[trend] = metrics.get(trend, 0) + 1

# Augment metrics with average change magnitude (semi-relevant)
changes = [temperature_data[i] - temperature_data[i-1] for i in range(1, len(temperature_data))]
metrics['avg_magnitude'] = sum(abs(c) for c in changes) / len(changes)

# Dead code path (distractor)
if False:
    metrics['outlier_ratio'] = deviation_count / len(temperature_data)

# Key evaluation function
def evaluate_performance(met, w):
    score = 0.0
    for key in w:
        if key in met:
            score += met[key] * w[key]
    # Adjustment based on combinatorics of transitions
    transition_bonus = len(unique_transitions) * 0.5
    score += transition_bonus
    # Final adjustment using moving average stability
    stability_penalty = 0
    for i in range(1, len(moving_averages)):
        if abs(moving_averages[i] - moving_averages[i-1]) > 1.0:
            stability_penalty += 0.2
    score -= stability_penalty
    return round(score, 4)

# Execute critical statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")