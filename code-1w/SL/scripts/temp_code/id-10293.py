def analyze_component(metrics, threshold=0.75):
    above_threshold = [m for m in metrics if m > threshold]
    below_threshold = [m for m in metrics if m <= threshold]
    ratio = len(above_threshold) / len(metrics) if metrics else 0
    return ratio, above_threshold

# Simulated sensor benchmark data (normalized performance scores)
sensor_readings = {
    'temp': [0.82, 0.67, 0.91, 0.76, 0.88],
    'pressure': [0.73, 0.69, 0.75, 0.81, 0.77],
    'humidity': [0.54, 0.63, 0.71, 0.66, 0.69],
    'light': [0.90, 0.94, 0.88, 0.92, 0.85]
}

# Secondary system diagnostics (irrelevant to final score but looks important)
diag_codes = ['OK', 'WARN', 'OK', 'OK']
temp_fluctuation_index = sum(abs(a - b) for a, b in zip(sensor_readings['temp'][1:], sensor_readings['temp'][:-1]))

# Aggregate all metrics into one list for analysis
all_metrics = []
for key in sensor_readings:
    if key != 'humidity':  # Exclude humidity due to known sensor instability
        all_metrics.extend(sensor_readings[key])

# Misleading intermediate calculation (not used in final logic)
avg_metric = sum(all_metrics) / len(all_metrics) if all_metrics else 0
variance_proxy = sum((x - avg_metric) ** 2 for x in all_metrics) / len(all_metrics) if all_metrics else 0

# Core evaluation logic
conformance_map = {}
for sensor, readings in sensor_readings.items():
    conformance_ratio, passing = analyze_component(readings)
    conformance_map[sensor] = {
        'ratio': conformance_ratio,
        'passing_count': len(passing),
        'stability': readings[-1] - readings[0]  # minor fluctuation metric
    }

# Weighted contribution based on sensor criticality (only temp and light are weighted)
weights = {'temp': 0.4, 'pressure': 0.2, 'light': 0.4}
weighted_score = 0
for sensor, weight in weights.items():
    weighted_score += conformance_map[sensor]['ratio'] * weight

# Final nonlinear adjustment based on stability trend
stability_trend = sum(conformance_map[s]['stability'] for s in ['temp', 'light'])
correction_factor = 1.0 + (stability_trend * 0.05) if stability_trend > 0 else 0.95

# Key statement
final_score = calculate_performance(benchmark_results)

# Supporting function defined after use (adds cognitive load)
def calculate_performance(data):
    base = weighted_score
    adjusted = base * correction_factor
    # Normalize to percentage scale with ceiling
    result = min(int(adjusted * 100), 100)
    return result

# Print result for execution visibility
Result: {final_score}