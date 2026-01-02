from collections import defaultdict

# Simulate sensor data processing with noise filtering and scoring
raw_readings = [105, 210, -95, 450, 300, -150, 400]
offset_calibration = 50
decay_factor = 0.9
smoothing_window = 3

# Apply calibration and filter negative drifts
calibrated = [x + offset_calibration for x in raw_readings]
filtered = [x for x in calibrated if x > 0]

# Compute moving average for noise reduction
smoothed = []
for i in range(len(filtered)):
    window = filtered[max(0, i - smoothing_window + 1):i + 1]
    smoothed.append(sum(window) / len(window))

# Normalize values to percentage scale (relative to max)
max_value = max(smoothed)
normalized = [round((val / max_value) * 100, 2) for val in smoothed]

# Misleading: irrelevant frequency analysis
frequency_map = defaultdict(int)
for val in raw_readings:
    frequency_map[val] += 1

# Simulate multiple metric extraction
raw_metrics = {
    'peak_stability': sum(1 for i in range(1, len(smoothed)-1) if abs(smoothed[i]-smoothed[i-1]) < 10),
    'trend_consistency': len([i for i in range(1, len(normalized)) if normalized[i] >= normalized[i-1]]),
    'dynamic_range': normalized[-1] - normalized[0],
    'noise_ratio': len([x for x in calibrated if x < 100]) / len(calibrated)
}

# Weighted scoring system
metric_weights = {
    'peak_stability': 0.3,
    'trend_consistency': 0.4,
    'dynamic_range': 0.2,
    'noise_ratio': -0.1  # Negative weight: higher noise reduces score
}

# Auxiliary function for score aggregation
evaluate_performance = lambda weights, metrics: sum(weights[k] * metrics[k] for k in weights)

# Key computation step
intermediate_diagnostic = [round(x * decay_factor, 1) for x in normalized]
baseline_reference = sum(normalized) / len(normalized)
penalty_adjustment = 0.0 if raw_metrics['noise_ratio'] < 0.3 else -5.0

final_score = evaluate_performance(metric_weights, raw_metrics)

# Print result as required
print(f"Result: {final_score}")