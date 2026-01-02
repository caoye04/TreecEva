from itertools import combinations

# Simulate sensor data from a climate control system
sensor_readings = [22.1, 19.5, 23.4, 20.2, 21.8, 24.0, 18.7]
temperature_windows = list(combinations(sensor_readings, 3))

# Calculate rolling stability index
stability_measures = []
for window in temperature_windows:
    variance = sum((temp - sum(window)/3)**2 for temp in window) / 3
    if variance < 2.5:
        stability_measures.append(variance)

# Irrelevant: Analyze window patterns (not used later)
pattern_count = {}
for w in temperature_windows:
    key = tuple(sorted(w))
    pattern_count[key] = pattern_count.get(key, 0) + 1

# Key metrics
valid_stability_count = len(stability_measures)
dropout_rate = 0.15
base_rating = len(sensor_readings) * 10

# Simulate user preference bias (unused in final calculation)
user_bias_factors = {"morning": 1.1, "afternoon": 0.95, "night": 1.0}
preference_weight = user_bias_factors["afternoon"]

# Performance factor based on valid stability readings
if valid_stability_count > 10:
    performance_factor = 1.25
else:
    performance_factor = 0.85

# Adjustments due to system load
system_loads = [75, 82, 67, 90, 77]
overload_events = sum(1 for load in system_loads if load > 80)
adjustment = 5 - overload_events * 2

# Distractor: Compute average load (not used)
avg_load = sum(system_loads) / len(system_loads)

# Critical assignment with interference from prior calculations
efficiency_score = base_rating * performance_factor + adjustment

# Noise: unused health metrics
health_index = (base_rating - avg_load) / (1 + dropout_rate)

# Final output
print(f"Result: {efficiency_score}")