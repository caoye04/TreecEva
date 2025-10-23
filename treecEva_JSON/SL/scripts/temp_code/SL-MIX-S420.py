from math import factorial
from functools import reduce

def sensor_combinator(reading_values, combo_size):
    if combo_size <= 0 or combo_size > len(reading_values):
        return []
    if combo_size == 1:
        return [[x] for x in reading_values]
    result = []
    for i in range(len(reading_values)):
        sub_combos = sensor_combinator(reading_values[i+1:], combo_size-1)
        for sub in sub_combos:
            result.append([reading_values[i]] + sub)
    return result

def aggregate_readings(sensor_data):
    return reduce(lambda acc, val: acc + val if val > 0 else acc, sensor_data, 0)

environmental_readings = [3, -1, 4, 1, 5, -9, 2, 6, 5, 3, 5]
positive_readings = [r for r in environmental_readings if r > 0]

# Calculate combinations of positive readings taken 3 at a time
reading_combinations = sensor_combinator(positive_readings, 3)

# Process combinations with a lambda-based transformation
processed_combinations = [
    list(map(lambda x: x**2 if x % 2 == 0 else x**3, combo))
    for combo in reading_combinations
]

# Calculate aggregate metrics
combo_sums = [sum(combo) for combo in processed_combinations]
filtered_sums = [s for s in combo_sums if s > 100]

# Apply statistical transformation
mean_sum = sum(filtered_sums) / len(filtered_sums) if filtered_sums else 0
variance = sum((x - mean_sum)**2 for x in filtered_sums) / len(filtered_sums) if filtered_sums else 0

# Final metric calculation using ternary logic and combinatorics
combinatorial_factor = factorial(len(positive_readings)) // (factorial(3) * factorial(len(positive_readings) - 3))
final_metric = int(mean_sum + variance) if combinatorial_factor > 100 else int(mean_sum - variance)

print(f"Result: {final_metric}")