from collections import Counter

# Sensor data calibration and noise filtering simulation
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
threshold = 4

# Count frequency of each reading
freq_counter = Counter(data_stream)

# Extract readings above threshold
dominant_readings = [k for k, v in freq_counter.items() if v >= 2 and k < threshold] or [0]

# Simulate secondary filter: only odd-indexed values in original stream
odd_index_values = [data_stream[i] for i in range(1, len(data_stream), 2)]

# Combine conditions: keep values that are in dominant_readings AND appear at odd indices
filtered_data = [val for val in odd_index_values if val in dominant_readings]

# Final computation step
filtered_sum = sum(filtered_data)

# Irrelevant auxiliary variable (minor distraction)
temp_scaling = 1.5

print(f"Result: {filtered_sum}")