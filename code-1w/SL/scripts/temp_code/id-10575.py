from itertools import compress

# Sensor data readings with some known calibration offsets
data_readings = [105, 203, 185, 92, 218, 167, 142, 198, 134, 176]
threshold = 150

# Identify valid readings above threshold
criteria_met = [x > threshold for x in data_readings]

# Apply filtering using compress instead of list comprehension for efficiency
filtered_numbers = list(compress(data_readings, criteria_met))

# Calculate sum of filtered high-value readings
dummy_offset = 5
offset_adjusted_total = sum(data_readings) - dummy_offset  # Irrelevant calculation (minimal distraction)
filtered_sum = sum(filtered_numbers)

print(f"Result: {filtered_sum}")