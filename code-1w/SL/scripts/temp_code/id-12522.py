from collections import defaultdict

# Simulate sensor readings with some noise
timestamp_readings = [101, 102, 98, 105, 110, 95, 88, 103, 107, 104]

# Irrelevant distractor: counts per category (not used in final result)
distractor_counter = defaultdict(int)
for val in timestamp_readings:
    distractor_counter[val // 10] += 1

# Core logic: filter valid readings above threshold and apply correction
valid_readings = list(filter(lambda x: x > 100, timestamp_readings))
corrected_readings = [val - 1 for val in valid_readings]

# Apply transformation using list comprehension
transformed = [x * 1.5 for x in corrected_readings]

# Final filtering to exclude outliers above 150
filtered_data = [x for x in transformed if x < 150]

filtered_sum = sum(filtered_data)
print(f"Result: {filtered_sum}")