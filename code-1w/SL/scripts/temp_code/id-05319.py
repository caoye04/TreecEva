def analyze_trend(data, threshold=0.5):
    trend = []
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            trend.append(1)
        elif data[i] - data[i-1] < -threshold:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

# Irrelevant helper function (decoy)
def normalize_vector(v):
    mag = sum(x**2 for x in v) ** 0.5
    return [x / mag for x in v] if mag else v

# Unused but plausible transformation
def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append(sum(signal[i-1:i+2]) / 3)
    smoothed.append(signal[-1])
    return smoothed

# Core logic disguised among distractions
weights = {'accuracy': 0.4, 'latency': 0.3, 'throughput': 0.2, 'stability': 0.1}

baseline_metrics = {
    'accuracy': [0.92, 0.94, 0.93, 0.95, 0.96],
    'latency': [120, 115, 118, 112, 110],
    'throughput': [88, 92, 95, 93, 97],
    'stability': [0.98, 0.97, 0.99, 0.96, 0.98]
}

# Distractor: fake aggregation
def compute_average(series):
    return sum(series) / len(series) if series else 0

# Real processing begins
metrics_log = {}
for key, values in baseline_metrics.items():
    if key == 'accuracy':
        metrics_log[key] = sum(values) / len(values)
    elif key == 'latency':
        # Invert latency since lower is better
        inverted = [1.0 / x for x in values]
        metrics_log[key] = sum(inverted) / len(inverted) * 100
    elif key == 'throughput':
        metrics_log[key] = sum(values) / len(values) / 10
    elif key == 'stability':
        # Apply decay weighting
        weighted = sum(values[i] * (0.8 ** (len(values)-1-i)) for i in range(len(values)))
        metrics_log[key] = weighted / sum(0.8 ** i for i in range(len(values)))

# Fake cross-correlation (dead code path)
correlation_matrix = {}
for k1 in metrics_log:
    correlation_matrix[k1] = {}
    for k2 in metrics_log:
        correlation_matrix[k1][k2] = 0.5  # Placeholder

# Red herring computation
deviation_report = {}
for k, v in baseline_metrics.items():
    mean_v = sum(v) / len(v)
    deviation_report[k] = sum((x - mean_v)**2 for x in v) / len(v)

# Critical function
def evaluate_performance(log, w):
    total = 0.0
    for metric, weight in w.items():
        if metric in log:
            total += log[metric] * weight
    # Additional adjustment based on trend analysis
    accuracy_trend = analyze_trend(baseline_metrics['accuracy'])
    recent_trend = accuracy_trend[-3:]  # Last three
    improvement_bonus = sum(recent_trend) * 0.05  # Bonus per upward trend
    total += improvement_bonus
    return round(total * 100, 4)

# Final computation
final_score = evaluate_performance(metrics_log, weights)

# Output result
print(f"Result: {final_score}")