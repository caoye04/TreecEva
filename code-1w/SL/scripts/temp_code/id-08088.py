from collections import defaultdict
from itertools import cycle

# Simulate daily temperature readings over a week
temperatures = [20, 22, 19, 24, 23, 25, 21]

# Count frequency of each temperature
temp_counter = defaultdict(int)
for temp in temperatures:
    temp_counter[temp] += 1

# Apply modular weighting based on day of week
day_cycle = cycle(range(7))
weighted_sum = 0
for i, temp in enumerate(temperatures):
    day_weight = (next(day_cycle) + 1) % 5 or 5  # weights: 1-5, never 0
    weighted_sum += temp * day_weight

# Calculate base adjusted score
adjustment_factor = sum(temp_counter.keys()) / len(temp_counter)

# Use lambda to encapsulate final transformation
transform = lambda x, y: (x // 3) + (y * 2)

# Auxiliary irrelevant variable (minor distraction)
placeholder = [i**2 for i in range(5)]

result = transform(weighted_sum, adjustment_factor)
print(f"Target result: {result}")