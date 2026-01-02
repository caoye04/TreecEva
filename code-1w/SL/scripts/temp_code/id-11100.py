import itertools

# Simulated system performance metrics from various subsystems
temp_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.4, 23.2]

# Irrelevant sensor data (distractor)
pressure_readings = [101.3, 102.1, 99.8, 100.5, 103.2]  # kPa
humidity_readings = [45, 47, 50, 44, 46]  # percent

# Historical baselines (misleading reference values)
baseline_temp = sum(temp_readings[:3]) / 3
baseline_deviation = abs(temp_readings[0] - baseline_temp) * 1.5

# Data transformation pipeline
smoothed_temps = [round((a + b + c) / 3, 2) for a, b, c in zip(temp_readings, temp_readings[1:], temp_readings[2:])]
spike_count = sum(1 for i in range(1, len(smoothed_temps)) if abs(smoothed_temps[i] - smoothed_temps[i-1]) > 0.5)

# Complex feature engineering with red herring calculations
rolling_ranges = [max(window) - min(window) for window in itertools.zip_longest(temp_readings[::2], temp_readings[1::2], fillvalue=23.0)]
avg_range = sum(rolling_ranges) / len(rolling_ranges)

# Unused but plausible intermediate (dead path)
adjusted_ranges = [r * 0.9 for r in rolling_ranges if r > 0.3]

# Core evaluation parameters
stability_factor = 1.0 if spike_count == 0 else 1.0 / (spike_count ** 0.5)
consistency_bonus = 1.0 if avg_range < 0.8 else 0.9

# Weight configuration for different metrics (some weights unused)
weights = {
    'stability': 0.4,
    'trend': 0.3,
    'spikes': 0.2,
    'range': 0.1,
    'dummy_metric': 0.0  # Explicit zero-weight decoy
}

# Fictitious trend analysis (partially irrelevant)
temp_trend = sum(max(0, temp_readings[i] - temp_readings[i-1]) for i in range(1, len(temp_readings)))
decay_trend = sum(0.95 ** i * (temp_readings[i] - temp_readings[0]) for i in range(len(temp_readings)))
composite_trend = (temp_trend * 0.7) + (decay_trend * 0.3)

# Secondary derived metrics (only one used)
metrics = {
    'stability': stability_factor,
    'trend': composite_trend / 100.0,
    'spikes': max(0, 10 - spike_count * 2),
    'range': 10 * (1 - min(avg_range / 2.0, 1)),
    'placeholder': 0.0  # Dead entry
}

# Misleading normalization chain (unused)
normalized_metrics = {k: v / (sum(metrics.values()) + 1e-8) for k, v in metrics.items()}
scaled_metrics = {k: v * 10 for k, v in normalized_metrics.items()}

# Core evaluation logic
valid_keys = set(weights.keys()) & set(metrics.keys())
active_weights_sum = sum(weights[k] for k in valid_keys if weights[k] > 0)

# Final weighted scoring (this is the critical computation)
weighted_sum = sum(metrics[k] * weights[k] for k in valid_keys if weights[k] > 0)
final_score = round(weighted_sum / active_weights_sum if active_weights_sum > 0 else 0, 6)

# Output the result as required
print(f"Result: {final_score}")