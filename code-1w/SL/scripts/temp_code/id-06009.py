from collections import defaultdict

# Simulate environmental sensor data aggregation and thermal analysis
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0]
humidity_levels = [45, 47, 44, 50, 46, 48, 52]
pressure_data = [1013, 1012, 1014, 1015, 1011, 1013, 1016]

# Initialize data structures
sensor_stats = defaultdict(int)
aggregated_metrics = []

# Irrelevant statistical tracking (distractor)
for temp in temperature_readings:
    sensor_stats['total_temp'] += temp
    sensor_stats['reading_count'] += 1

for humidity in humidity_levels:
    sensor_stats['total_humidity'] += humidity

# Compute derived metrics with red herrings
dew_point_estimates = []
for i in range(len(temperature_readings)):
    # Misleading complex calculation
    alpha = temperature_readings[i] * 0.6 + humidity_levels[i] * 0.4
    beta = pressure_data[i] / 1000.0
    dew_point = alpha * beta
    dew_point_estimates.append(dew_point)

    # Dead code path - never used later
    if dew_point > 15.0:
        sensor_stats['high_dew_warning'] += 1

# Relevant computation begins
base_capacity = sum(temperature_readings) / len(temperature_readings)
fluctuation = max(temperature_readings) - min(temperature_readings)

# Efficiency depends on stability and average conditions
stability_score = 1.0 if fluctuation < 3.0 else 0.85
humidity_ratio = sum(humidity_levels) / len(humidity_levels)
efficiency_factor = stability_score

# Additional irrelevant check
if humidity_ratio > 45:
    efficiency_factor *= 0.95  # Minor degradation under high humidity

# Key assignment statement
thermal_capacity = base_capacity * efficiency_factor

# More distraction: unused post-processing
adjusted_capacity = thermal_capacity * 1.02
final_diagnostic = f"Capacity: {adjusted_capacity:.2f} MW"

# Output the required result
print(f"Result: {thermal_capacity}")