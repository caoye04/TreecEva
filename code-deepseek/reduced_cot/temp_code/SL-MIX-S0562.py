import itertools

# Sensor data processing simulation
raw_readings = [12, 8, 15, 6, 9, 11, 7, 14]
threshold = 10

# Filter readings above threshold
filtered_readings = [x for x in raw_readings if x > threshold]

# Calculate combinations of filtered readings (distractor)
combo_calc = sum(itertools.combinations(filtered_readings, 2), ())
combo_sum = sum(combo_calc) if combo_calc else 0

# Process metrics with rolling average
processed_metrics = []
current_avg = 0

for i, reading in enumerate(filtered_readings):
    current_avg = (current_avg * i + reading) / (i + 1)
    processed_metrics.append(int(current_avg))

# Calculate adjustment based on set operations (partially relevant)
reading_set = set(filtered_readings)
baseline_set = {12, 15, 14}
common_elements = reading_set.intersection(baseline_set)
uncommon_elements = reading_set.symmetric_difference(baseline_set)

# Adjustment calculation
adjustment_offset = len(common_elements) * 2 - len(uncommon_elements)

# Final result calculation
final_measurement = processed_metrics[-1] + adjustment_offset

print(f"Result: {final_measurement}")