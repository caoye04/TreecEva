from collections import defaultdict
import itertools

# Simulate sensor readings with some noise
data_stream = [3, -1, 4, 1, 5, -2, 9, 2, 6]
noise_mask = [1, -1, 1, -1, 1, -1, 1, -1, 1]

corrected_readings = [d + n for d, n in zip(data_stream, noise_mask)]

# Use lambda to filter out negative corrected values
valid_readings = list(filter(lambda x: x > 0, corrected_readings))

duplicate_counter = defaultdict(int)
for val in valid_readings:
    duplicate_counter[val] += 1

# Extract unique values maintaining order
seen = set()
unique_ordered = [x for x in valid_readings if not (x in seen or seen.add(x))]

# Apply transformation: square even numbers, leave odd unchanged
transformed_data = [x**2 if x % 2 == 0 else x for x in unique_ordered]

# Final filtering: keep only numbers that appear at least once in original data above threshold
target_threshold = 3
filtered_data = [x for x in transformed_data if x in data_stream and x >= target_threshold]

filtered_sum = sum(filtered_data)
print(f"Result: {filtered_sum}")