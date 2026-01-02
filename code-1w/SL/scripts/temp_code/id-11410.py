import math

# Simulated sensor readings from a water treatment plant
sensor_readings = [32.4, 35.1, 38.7, 40.2, 36.8, 34.0, 39.5]

temperature_offset = 0.0
for temp in sensor_readings:
    temperature_offset += (temp - 35.0) ** 2

temperature_offset /= len(sensor_readings)
temperature_offset = round(temperature_offset, 2)

# Red herring: pressure calculations with no impact on final result
pressure_sensors = [101.3, 102.5, 99.8, 103.1, 100.4]
avg_pressure = sum(pressure_sensors) / len(pressure_sensors)
pressure_variance = sum((p - avg_pressure) ** 2 for p in pressure_sensors) / len(pressure_sensors)
normalized_pressure_index = max(pressure_sensors) - min(pressure_sensors)

# Flow dynamics
base_flow_rate = 125.6
flow_fluctuation = sum(abs(sensor_readings[i] - sensor_readings[i-1]) for i in range(1, len(sensor_readings)))
adjusted_flow = base_flow_rate - (flow_fluctuation * 0.8)

# Chemical dosage tracking (unused distractor)
dosage_schedule = {'chlorine': 3.2, 'ozone': 5.1, 'coagulant': 2.7}
current_dosage = sum(dosage_schedule.values())
projected_daily_usage = current_dosage * 24

# Efficiency calculation using lambda and set operations
valid_ranges = set(range(30, 41))
reading_ints = {int(x) for x in sensor_readings}  # set operation
coverage_ratio = len(reading_ints & valid_ranges) / len(valid_ranges)

adjustment_fn = lambda x: round(math.log(x + 1) * 0.75, 3)
efficiency_factor = adjustment_fn(coverage_ratio * 100)

# Secondary flow adjustments (distractor)
altitude_influence = 12.4
humidity_factor = 0.92
theoretical_capacity = adjusted_flow * altitude_influence / (1 + humidity_factor)

# Critical path: filtration performance metric
operational_hours = 18
total_volume_processed = adjusted_flow * operational_hours
maintenance_downtime_loss = total_volume_processed * 0.05  # 5% loss
net_flow = total_volume_processed - maintenance_downtime_loss

# Key assignment - this is where the answer is determined
filtration_score = net_flow * efficiency_factor

# Dead code path - misleading post-calculation adjustment
if filtration_score > 1000:
    filtration_score *= 0.95
elif filtration_score < 500:
    filtration_score += 50
# Note: score is ~845, so no branch taken

# Additional decoy variables
load_balancing_factor = 1.05
stress_test_result = filtration_score ** 0.5 * 0.1
redundancy_adjustment = stress_test_result / load_balancing_factor

# Output the target result
print(f"Result: {filtration_score}")