from collections import defaultdict
import math

# Simulate system health metrics over time
def collect_metrics():
    data = defaultdict(lambda: [])
    for t in range(1, 11):
        data['cpu'].append(60 + (t % 7) * 3)
        data['memory'].append(70 + (t % 5) * 2)
        data['disk_io'].append(40 + (t % 3) * 5)
    return data

# Noise injection - irrelevant metric
def add_noise(metrics):
    noisy_copy = {k: v[:] for k, v in metrics.items()}
    for _ in range(3):
        noisy_copy['noise'] = [math.sin(i * 0.5) for i in range(len(noisy_copy['cpu']))]
    return noisy_copy

# Compute rolling average - useful preprocessing
def smooth(series, window=3):
    smoothed = []
    for i in range(len(series)):
        start = max(0, i - window + 1)
        smoothed.append(sum(series[start:i+1]) / (i - start + 1))
    return smoothed

# Analyze trend direction - misleading analysis
def trend_direction(series):
    if len(series) < 2:
        return 0
    return 1 if series[-1] > series[0] else (-1 if series[-1] < series[0] else 0)

# Weighted evaluation function
def evaluate_performance(raw_metrics, importance_weights):
    # Preprocess: smooth key metrics
    processed = {}
    for key in ['cpu', 'memory', 'disk_io']:
        if key in raw_metrics:
            processed[key] = smooth(raw_metrics[key])
    
    # Extract final values after smoothing
    final_values = {k: v[-1] for k, v in processed.items()}
    
    # Irrelevant trend analysis (distractor)
    trends = {k: trend_direction(v) for k, v in raw_metrics.items() if k in ['cpu', 'memory', 'disk_io']}
    trend_penalty = sum(abs(t) for t in trends.values()) * 0.1  # Unused distraction
    
    # Normalize metrics to 0-100 scale (inverse for better performance)
    normalized = {}
    caps = {'cpu': 90, 'memory': 85, 'disk_io': 75}
    for k, cap in caps.items():
        raw_final = raw_metrics[k][-1]
        normalized[k] = max(0, 100 - (raw_final / cap * 100))
    
    # Apply weights and compute weighted score
    weighted_sum = sum(normalized[k] * w for k, w in importance_weights.items())
    total_weight = sum(importance_weights.values())
    base_score = weighted_sum / total_weight if total_weight else 0
    
    # Additional irrelevant computation (dead path)
    anomaly_count = 0
    for vals in raw_metrics.values():
        for v in vals:
            if v > 95:
                anomaly_count += 1
    security_factor = 1.0
    if anomaly_count > 5:
        security_factor *= 0.95
    
    # Final scoring with red herring adjustment (not applied)
    final_score = base_score  # No actual adjustment despite complex setup
    
    # Debug print (irrelevant to logic)
    debug_info = {"base": base_score, "trend_effect": trend_penalty, "anomalies": anomaly_count}
    
    return final_score

# Main execution
metrics = collect_metrics()
noisy_metrics = add_noise(metrics)
weights = {'cpu': 0.5, 'memory': 0.3, 'disk_io': 0.2}

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")