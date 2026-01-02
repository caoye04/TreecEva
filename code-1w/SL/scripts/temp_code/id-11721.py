def transform(x):
    return x * x - 3

# Simulate sensor readings with noise
raw_readings = [i + 2 for i in range(15)]

# Irrelevant transformation (distractor)
distorted = list(map(lambda y: (y % 4) * 2, raw_readings))

# Actual processing path
smoothed = [x for x in raw_readings if x % 3 != 0]
offset = sum([1 for _ in range(4)])  # Red herring: just adds 4
adjusted = [z - offset for z in smoothed]

# Filter based on transformed threshold
threshold = transform(5)  # evaluates to 22
filtered_values = [v for v in adjusted if v > threshold // 2]  # > 11

# Secondary distractor: unused bitwise accumulation
temp_state = 0
for val in raw_readings:
    temp_state ^= val & 7

# Core logic: apply functional transform and accumulate
processed = list(map(lambda n: n + (n & 5), filtered_values))  # bitwise mix

# Accumulate with conditional adjustment
rolling_sum = 0
for num in processed:
    if num % 2 == 0:
        rolling_sum += num // 2
    else:
        rolling_sum += num

# Final computation
result = rolling_sum - len(processed) * 3

# Print final target result
print(f"Target result: {result}")