def analyze_trend(data, threshold=0.5):
    above_threshold = list(filter(lambda x: x > threshold, data))
    below_threshold = [x for x in data if x <= threshold]
    trend_ratio = len(above_threshold) / len(data) if data else 0
    return trend_ratio

# Simulated sensor readings over time (normalized)
sensor_readings = [0.6, 0.4, 0.7, 0.3, 0.8, 0.2, 0.9]

# Secondary diagnostic check (irrelevant to final score but looks important)
diagnostic_flags = []
for reading in sensor_readings:
    if reading > 0.75:
        diagnostic_flags.append("HIGH")
    elif reading < 0.25:
        diagnostic_flags.append("LOW")
    else:
        diagnostic_flags.append("NORMAL")

# Auxiliary computation - distractor
total_fluctuation = 0
for i in range(1, len(sensor_readings)):
    total_fluctuation += abs(sensor_readings[i] - sensor_readings[i-1])
avg_fluctuation = total_fluctuation / (len(sensor_readings) - 1) if len(sensor_readings) > 1 else 0

# Core metrics for performance evaluation
baseline_adjustment = sum([x * 0.1 for x in sensor_readings])  # minor correction factor
efficiency_metric = analyze_trend(sensor_readings, 0.5)
reliability_metric = sum(1 for x in sensor_readings if x > 0.6) / len(sensor_readings)
consistency_metric = 1 - (sum((x - 0.5)**2 for x in sensor_readings) / len(sensor_readings))**0.5

# Weight distribution (optimized for balanced systems)
weights = {
    'efficiency': 0.4,
    'reliability': 0.35,
    'consistency': 0.25
}

# Metric mapping for aggregation
metrics = {
    'efficiency': efficiency_metric,
    'reliability': reliability_metric,
    'consistency': consistency_metric
}

# Irrelevant transformation (looks like preprocessing)
processed_metrics = {k: v * 100 for k, v in metrics.items()}
metric_variance = sum((v - 50) ** 2 for v in processed_metrics.values()) / len(processed_metrics)

# Final weighted aggregation function
def aggregate_performance(metrs, wts):
    combined = 0
    for key in wts:
        if key in metrs:
            combined += wts[key] * metrs[key]
    return int(combined * 100)  # scale to integer percentage

final_score = aggregate_performance(metrics, weights)
print(f"Result: {final_score}")