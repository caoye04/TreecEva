def analyze_trend(data):
    trend = {}
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend[f'up_{i}'] = data[i] - data[i-1]
        elif data[i] < data[i-1]:
            trend[f'down_{i}'] = data[i-1] - data[i]
    return trend

# Simulate sensor readings over time
readings = [10, 15, 12, 18, 16, 20, 19]

# Analyze directional trends (distraction: not directly used)
trends = analyze_trend(readings)

# Define performance metrics and corresponding weights
metrics = {
    'stability': 0.85,
    'consistency': 0.76,
    'peak_ratio': 18 / 20,
    'recovery_rate': 0.92
}

weights = {
    'stability': 0.3,
    'consistency': 0.25,
    'peak_ratio': 0.35,
    'recovery_rate': 0.1
}

# Auxiliary function to compute weighted score
process_results = lambda m, w: sum(m[k] * w[k] for k in m)

# Calculate intermediate statistics (distractor computations)
mean_reading = sum(readings) / len(readings)
variance = sum((x - mean_reading) ** 2 for x in readings) / len(readings)
std_dev = variance ** 0.5

# Normalize consistency metric using standard deviation (semi-relevant but overridden later)
normalized_metrics = {**metrics}
normalized_metrics['consistency'] = min(1.0, metrics['consistency'] + std_dev * 0.05)

# Recompute final score with original metrics (key point: uses original, not normalized)
final_score = process_results(metrics, weights)

# Additional red herring: unused transformation map
transform_map = {key: round(val ** 0.5, 3) for key, val in metrics.items()}

# Dead code branch (never executed)
if False:
    final_score *= 1.1

print(f"Result: {final_score}")