from itertools import combinations

# Simulate sensor readings from a thermal regulation system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 23.7]
humidity_readings = [45, 47, 46, 50, 48, 49, 44]

# Misleading preprocessing: irrelevant transformations
deviation_offset = sum([abs(t - 24) for t in temperature_readings]) / len(temperature_readings)
scaled_humidity = [h * 0.85 for h in humidity_readings if h > 45]
filtered_pairs = list(combinations([int(t) for t in temperature_readings], 2))

# State tracking variables with partial relevance
counter = 0
stable_intervals = 0
for i in range(1, len(temperature_readings)):
    if abs(temperature_readings[i] - temperature_readings[i-1]) < 0.6:
        stable_intervals += 1
    else:
        counter += 1

# Secondary metric (distractor)
avg_fluctuation = sum(
    abs(temperature_readings[i] - temperature_readings[i-1]) 
    for i in range(1, len(temperature_readings))
) / (len(temperature_readings) - 1)

# Core logic: system performance evaluation
base_rating = 85
threshold_met = stable_intervals >= 4
device_load = len(temperature_readings) * 1.5

# Conditional branch with early decision impact
if threshold_met:
    adjustment_factor = 1.1
    # Nested condition to compute multiplier
    if avg_fluctuation < 0.8:
        performance_multiplier = 1.25
    else:
        performance_multiplier = 1.15
else:
    performance_multiplier = 0.95
    adjustment_factor = 0.85

# Key computation involving multiple concepts
intermediate_metric = (base_rating + device_load) / 2
adjusted_rating = intermediate_metric * adjustment_factor

# Final efficiency score calculation
efficiency_score = base_rating * performance_multiplier

# Irrelevant aggregation (dead-end computation)
total_combinations = len(filtered_pairs)
phantom_index = sum(scaled_humidity) / (total_combinations or 1)

# Output target result
print(f"Result: {efficiency_score}")