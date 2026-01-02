from collections import Counter
import itertools

# Simulate sensor readings with some noise
temperature_readings = [23.5, 24.1, 24.1, 25.3, 23.5, 26.7, 24.1, 23.5, 27.2, 25.3]

# Count frequency of each reading
reading_counts = Counter(temperature_readings)

# Identify readings that occur more than once (potential stable states)
frequent_readings = list(filter(lambda x: reading_counts[x] > 1, reading_counts))

# Use itertools.groupby to organize consecutive duplicates (after sorting)
sorted_readings = sorted(temperature_readings)
grouped_readings = [list(group) for key, group in itertools.groupby(sorted_readings)]

# Extract unique values from groups longer than 1 (indicating repeated adjacent values)
repeated_groups = list(filter(lambda g: len(g) > 1, grouped_readings))
flattened_repeats = list(itertools.chain.from_iterable(repeated_groups))
unique_repeats = sorted(set(flattened_repeats))

# Filter original data to include only values present in both frequent and repeated groups
filtered_data = [val for val in temperature_readings if val in unique_repeats]

# Compute final result
filtered_sum = sum(filtered_data)
print(f"Result: {filtered_sum}")