def analyze_trend(data):
    trend_values = [data[i+1] - data[i] for i in range(len(data) - 1)]
    avg_change = sum(trend_values) / len(trend_values) if trend_values else 0
    volatility = sum((x - avg_change) ** 2 for x in trend_values) / len(trend_values) if trend_values else 0
    return avg_change, volatility

# Simulate sensor readings over time
temperature_readings = [20.1, 22.5, 19.8, 23.0, 24.2, 21.0, 20.5]

# Irrelevant computation: normalize values (not used later)
normalized_temps = [(t - min(temperature_readings)) / (max(temperature_readings) - min(temperature_readings)) for t in temperature_readings]

# Extract features from trend
mean_trend, stability_metric = analyze_trend(temperature_readings)

# Dummy transformation (distraction)
stability_adjusted = stability_metric * 1.5 if mean_trend > 0 else stability_metric * 0.8

# Weighted evaluation setup
baseline_offset = sum(temperature_readings) / len(temperature_readings)
drift_compensation = abs(mean_trend) * 10

# Define performance metrics (some are red herrings)
metrics = {
    'consistency': 100 - stability_metric * 5,
    'efficiency': baseline_offset * 2.1,
    'response_time': 45,  # Static placeholder
    'reliability': 92.5
}

# Misleading metric not used in final calculation
temporal_efficiency = metrics['efficiency'] * 0.9 + drift_compensation

weights = {
    'consistency': 0.4,
    'efficiency': 0.3,
    'reliability': 0.3
    # Note: 'response_time' is missing in weights → deliberate omission
}

# Apply bitwise mask to filter out low scores (XOR with control pattern)
filtered_metrics = {}
for k, v in metrics.items():
    if k in weights:
        # Use XOR to toggle based on threshold (bitwise distraction but still deterministic)
        control_flag = int(v * 100) & 0b11111  # Take lower 5 bits
        adjusted_value = v ^ (control_flag >> 3) * 0.05  # Tiny perturbation
        filtered_metrics[k] = adjusted_value

# Final weighted score computation
def evaluate_performance(met, wts):
    total_weight = sum(wts.values())
    weighted_sum = sum(met[key] * wts[key] for key in wts)
    return weighted_sum / total_weight

# Key statement
final_score = evaluate_performance(metrics, weights)

# Additional irrelevant state tracking
historical_scores = [final_score * (0.95 + i*0.01) for i in range(5)]
projected_growth = sum(historical_scores[i+1] - historical_scores[i] for i in range(4))

print(f"Result: {final_score}")