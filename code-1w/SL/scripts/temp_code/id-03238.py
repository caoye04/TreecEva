def analyze_trend(data, threshold=0.5):
    moving_avg = []
    for i in range(2, len(data)):
        avg = sum(data[i-2:i+1]) / 3
        moving_avg.append(avg)
    
    trend_changes = 0
    for i in range(1, len(moving_avg)):
        if (moving_avg[i] - moving_avg[i-1]) > threshold:
            trend_changes += 1
    return trend_changes

# Simulate sensor data drift over time
data_stream = [0.1, 0.4, 0.8, 1.2, 0.9, 1.5, 2.0, 1.8, 2.1, 2.5]

# Irrelevant transformation - distractor
distorted = [round(x * 1.05, 2) for x in data_stream]
distorted_sliced = distorted[1:6:2]  # unused later

baseline = sum(data_stream) / len(data_stream)
above_baseline_count = len([x for x in data_stream if x > baseline])

# Secondary analysis - partially relevant
trend_intensity = analyze_trend(data_stream)

# Weighted metric evaluation
metrics = {
    'stability': 85,
    'consistency': 70 + trend_intensity,
    'drift_rate': above_baseline_count * 5,
    'noise_level': len(distorted_sliced) * 3  # misleading use of distractor variable
}

# Weights for performance evaluation (normalized)
weights = [0.3, 0.25, 0.35, 0.1]
metric_keys = list(metrics.keys())

# Normalize metrics to 0-100 scale (already are, but extra step for distraction)
max_possible = 100
normalized_metrics = [metrics[key] / max_possible for key in metric_keys]

# Apply weights and compute final score
weighted_sum = 0
for i in range(len(normalized_metrics)):
    weighted_sum += normalized_metrics[i] * weights[i]

final_score = int(weighted_sum * 100)  # convert back to integer scale

# Additional irrelevant computations to increase interference
shadow_copy = metrics.copy()
for k in shadow_copy:
    shadow_copy[k] = shadow_copy[k] ** 0.5
unused_aggregate = sum(shadow_copy.values()) / len(shadow_copy)

# Red herring: sorting unrelated values
auxiliary_data = [final_score, unused_aggregate, baseline * 10]
auxiliary_data.sort(reverse=True)

# Final output
print(f"Result: {final_score}")