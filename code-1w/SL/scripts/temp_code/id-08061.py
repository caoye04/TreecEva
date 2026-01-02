def analyze_trends(data, window_size):
    trends = []
    for i in range(len(data) - window_size + 1):
        segment = data[i:i + window_size]
        avg = sum(segment) / window_size
        trends.append(avg > data[i + window_size - 1])
    return trends

# Simulate sensor readings over time
readings = [23.5, 24.1, 25.3, 24.9, 26.0, 26.8, 27.2, 26.5, 25.8, 25.0, 24.5, 24.8]

# Misleading computation: normalized readings (not used in final result)
normalized_readings = [round((r - min(readings)) / (max(readings) - min(readings)), 3) for r in readings]
baseline = sum(readings) / len(readings)
adjusted = [round(baseline * 1.05 if r > baseline else baseline * 0.95, 2) for r in readings]

# Extract rolling trend signals
trend_signals = analyze_trends(readings, 3)

# Define performance metrics based on trend consistency
metrics = {
    'positive_runs': 0,
    'negative_runs': 0,
    'volatility_index': 0,
    'stability_points': 0
}

# Count consecutive trend patterns
current_run = 0
prev = None
for signal in trend_signals:
    if prev is not None:
        if signal == prev:
            current_run += 1
        else:
            if signal:
                metrics['negative_runs'] += max(0, current_run - 1)
            else:
                metrics['positive_runs'] += max(0, current_run - 1)
            current_run = 0
    prev = signal

# Compute volatility using absolute differences (semi-relevant)
diffs = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
metrics['volatility_index'] = round(sum(diffs) / len(diffs), 3)

# Stability points based on small fluctuations
threshold_dev = [1 if abs(readings[i+1] - readings[i]) < 0.8 else 0 for i in range(len(readings)-1)]
metrics['stability_points'] = sum(threshold_dev)

# Dummy transformation (distractor)
transformed_metrics = {k: v * 1.1 for k, v in metrics.items() if 'points' in k}

# Thresholds for evaluation (key parameters)
thresholds = {
    'min_stability': 6,
    'max_volatility': 1.0,
    'required_runs': 2
}

# Evaluate system performance against thresholds
def evaluate_performance(met, thres):
    score = 100
    if met['stability_points'] < thres['min_stability']:
        score -= 25
    if met['volatility_index'] > thres['max_volatility']:
        score -= 30
    if met['positive_runs'] < thres['required_runs'] and met['volatility_index'] > thres['max_volatility']:
        score -= 45
    # Additional penalty if negative trends dominate
    if met['negative_runs'] > met['positive_runs'] + 1:
        score -= 15
    return int(score)

# Final evaluation
final_score = evaluate_performance(metrics, thresholds)

# Print result as required
print(f"Result: {final_score}")