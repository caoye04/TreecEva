from itertools import compress

# Sensor readings with some noise
raw_readings = [102, 98, 97, 105, 110, 108, 95, 103]

# Threshold filter: consider only readings above 100
valid_mask = [x > 100 for x in raw_readings]

# Extract high-confidence readings
clean_readings = list(compress(raw_readings, valid_mask))

# Apply sorting to analyze trend
sorted_readings = sorted(clean_readings)

# Slice to get recent stable values (last three)
stabilized_slice = sorted_readings[-3:]

# Dummy variable - irrelevant to final result
temp_avg = sum(stabilized_slice) / len(stabilized_slice)

# Scale final value based on calibration factor
scaling_factor = 0.9

# Key computation step
result = stabilized_slice[-1] * scaling_factor

# Output result
print(f"Result: {result}")