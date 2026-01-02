from itertools import cycle

# Simulate a precision agriculture scenario with sensor data filtering and yield prediction
soil_moisture_levels = [0.3, 0.4, 0.6, 0.8, 0.9, 0.2, 0.5]
temperature_readings = [22, 25, 27, 30, 33, 19, 24]
humidity_readings = [60, 65, 70, 80, 85, 55, 68]

# Irrelevant environmental metrics (distractor variables)
solar_radiation_log = [200, 220, 250, 300, 320, 180, 240]  # Not used in final calculation
wind_speed_data = [10, 15, 12, 18, 20, 8, 14]  # Dead code path

# Preprocess: Normalize values to 0-1 scale using min-max (only moisture and temp matter)
normalized_moisture = [(x - min(soil_moisture_levels)) / (max(soil_moisture_levels) - min(soil_moisture_levels)) for x in soil_moisture_levels]
normalized_temp = [(x - 15) / (40 - 15) for x in temperature_readings]  # Assume ideal range 15-40°C

# Apply weighted health score per sensor node (moisture has higher weight)
node_health_scores = []
for m, t in zip(normalized_moisture, normalized_temp):
    # Complex but only partially relevant formula
    base_score = (0.7 * m + 0.3 * max(0, 1 - abs(t - 0.6)))  # Peak temp efficiency at ~27°C
    adjusted_score = base_score * (1 + 0.1 * (m > 0.5 and t < 0.8))  # Bonus if adequately watered and not too hot
    node_health_scores.append(round(adjusted_score, 3))

# Filter out low-performing zones (below threshold)
effective_zones = [score for score in node_health_scores if score >= 0.55]

# Simulate irrigation adjustment cycles (irrelevant loop - distractor)
irrigation_cycles = []
cycle_phases = cycle(['pressurize', 'flush', 'idle'])
for i in range(len(effective_zones)):
    phase = next(cycle_phases)
    if phase == 'pressurize':
        irrigation_cycles.append(1)
    elif phase == 'flush':
        irrigation_cycles.append(0)
    else:
        irrigation_cycles.append(-1)

# Calculate cumulative stress factors from humidity spikes (semi-relevant)
humidity_spikes = [h for h in humidity_readings if h > 75]
stress_factor = len(humidity_spikes) * 0.05 if humidity_spikes else 0.0

# Secondary validation: check string-encoded status logs for anomalies (distractor logic)
device_logs = "ERR OK OK WARN OK ERR OK"
log_tokens = device_logs.split(' ')
anomaly_count = sum(1 for token in log_tokens if token == "ERR" or token == "WARN")
reliability_penalty = 0.02 * anomaly_count  # Minor impact, but included

# Core yield model: average health of effective zones, adjusted for stress and reliability
total_health = sum(effective_zones)
zone_count = len(effective_zones)
baseline_efficiency = total_health / zone_count if zone_count > 0 else 0

# Final yield calculation after all adjustments
final_yield = baseline_efficiency - stress_factor - reliability_penalty
final_yield = round(final_yield, 4)

# Print result as required
print(f"Result: {final_yield}")