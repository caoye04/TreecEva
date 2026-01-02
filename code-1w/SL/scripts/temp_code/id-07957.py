def analyze_trends(data_points):
    trend_indicators = {}
    for i, point in enumerate(data_points):
        if i == 0:
            trend_indicators[i] = 0
        else:
            trend_indicators[i] = point - data_points[i-1]
    
    # Irrelevant transformation (distractor)
    squared_diffs = [x**2 for x in trend_indicators.values()]
    avg_change = sum(trend_indicators.values()) / len(trend_indicators) if trend_indicators else 0
    return avg_change

# Simulated sensor readings over time
temperature_readings = [22.1, 23.5, 24.8, 24.8, 25.1, 26.3, 27.0]

# Secondary metric with partial relevance
efficiency_flags = {i: temp > 24 for i, temp in enumerate(temperature_readings)}

# Historical baseline (mostly unused)
historical_norms = {"summer": 24.5, "winter": 20.0, "spring": 22.3, "autumn": 21.8}
seasonal_deviation = temperature_readings[-1] - historical_norms["spring"]

# Feedback loop analysis (core logic begins)
raw_trend = analyze_trends(temperature_readings)
adjusted_trend = abs(raw_trend) * 1.2

# Simulate multiple feedback sources
feedback_sources = ['sensor_a', 'sensor_b', 'calibration_x']
feedback_data = {
    'sensor_a': {'weight': 0.6, 'value': adjusted_trend},
    'sensor_b': {'weight': 0.3, 'value': adjusted_trend + 0.5},
    'calibration_x': {'weight': 0.1, 'value': 0.0}  # Neutral influence
}

# Distractor: unused health metrics
health_metrics = {
    'uptime_ratio': 0.998,
    'packet_loss': 0.002,
    'retries': 3
}

# Real aggregation step
feedback_summary = []
for src in feedback_sources:
    entry = feedback_data[src]
    contribution = entry['weight'] * entry['value']
    feedback_summary.append(contribution)

# Dead code path (mild red herring)
if False:
    fallback_value = sum(health_metrics.values())
    feedback_summary.append(fallback_value)

# Core computation
running_total = sum(feedback_summary)
penalty_factor = 0 if efficiency_flags[0] else 0.2
net_impact = running_total - penalty_factor

# Final integration
baseline_offset = seasonal_deviation * 0.5
final_score = net_impact + baseline_offset

# Print result as required
print(f"Target result: {final_score}")