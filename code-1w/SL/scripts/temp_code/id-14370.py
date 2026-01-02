import itertools

# Simulate sensor readings with periodic noise
data_stream = [12, 15, 10, 8, 20, 14, 9, 16, 11, 13]
base_threshold = 10

# Identify valid measurements above threshold
valid_readings = [x for x in data_stream if x > base_threshold]

# Use itertools to generate sliding pairs and compute differences
pairwise_deltas = [abs(a - b) for a, b in itertools.pairwise(valid_readings)]

# Filter out small fluctuations below 3 units
distinct_changes = [delta for delta in pairwise_deltas if delta >= 3]

# Apply decay factor to older readings (simulated via index-based weighting)
weighted_values = [valid_readings[i] * 0.9**i for i in range(len(valid_readings))]

# Final processing step: floor all values and remove duplicates using set
floored_unique = sorted(set(int(val) for val in weighted_values))

# Extract only even-valued stable readings
filtered_data = [x for x in floored_unique if x % 2 == 0]

result = sum(filtered_data)
print(f"Result: {result}")