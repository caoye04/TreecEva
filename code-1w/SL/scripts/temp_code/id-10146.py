from collections import Counter
import itertools

# Simulate sensor readings over time with repeating patterns
time_series_data = [1, 2, 2, 3, 3, 3, 2, 2, 1, 4, 4, 4, 4, 2, 2, 3, 3, 3, 1]

# Group consecutive values to identify sustained measurement intervals
consecutive_groups = [list(g) for k, g in itertools.groupby(time_series_data)]

duration_map = {k: 0 for k in set(time_series_data)}
for group in consecutive_groups:
    key_value = group[0]
    duration_map[key_value] += len(group)

# Count how many times each distinct value appears in the original data (not used directly)
value_counts = Counter(time_series_data)

# Compute frequency of occurrence (how many separate bursts)
frequency_map = {k: 0 for k in set(time_series_data)}
for group in consecutive_groups:
    key_value = group[0]
    frequency_map[key_value] += 1

# Identify the highest number of occurrences across separate events
peak_frequency = max(frequency_map.values())

# Print result
print(f"Target result: {peak_frequency}")