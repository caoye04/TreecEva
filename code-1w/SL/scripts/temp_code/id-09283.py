from collections import defaultdict

# Simulate system health metrics over time
def collect_metrics():
    data = [10, 15, 20, 25, 30]
    timestamps = [1, 2, 3, 4, 5]
    readings = defaultdict(float)
    
    for i in range(len(data)):
        readings[timestamps[i]] = data[i] * 1.5
    
    return list(readings.values())

# Analyze trend and detect anomalies
def analyze_trend(values):
    diff = [values[i+1] - values[i] for i in range(len(values)-1)]
    avg_change = sum(diff) / len(diff)
    
    # Distractor: irrelevant smoothing
    smoothed = [values[0]]
    for i in range(1, len(values)):
        smoothed.append(smoothed[-1] * 0.9 + values[i] * 0.1)
    
    anomaly_count = 0
    for d in diff:
        if abs(d - avg_change) > 5:
            anomaly_count += 1
    
    return avg_change, anomaly_count, smoothed

# Evaluate performance against baseline
def evaluate_performance(metrics, baseline):
    base_val = sum(baseline) / len(baseline)
    current_total = sum(metrics)
    
    # Secondary processing: scale based on trend
    trend, anomalies, _ = analyze_trend(metrics)
    
    adjustment_factor = 1.0
    if trend > 10:
        adjustment_factor = 1.2
    elif trend < 5:
        adjustment_factor = 0.8
    
    # Irrelevant intermediate calculation (distractor)
    temp_result = 0
    for x in metrics:
        for y in metrics:
            if x > y:
                temp_result += x - y
    temp_result = temp_result / (len(metrics) or 1)
    
    # Main scoring logic
    raw_score = current_total / (base_val or 1)
    final_score = raw_score * adjustment_factor
    
    # Additional distraction: unused branching
    if anomalies > 2:
        final_score *= 0.95
    else:
        status_buffer = [0] * 5
        for i in range(len(status_buffer)):
            status_buffer[i] = i * 2
    
    return int(final_score)

# Setup baseline
baseline = [5, 10, 15]
metrics = collect_metrics()

# Key execution point
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")