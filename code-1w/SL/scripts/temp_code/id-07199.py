from collections import defaultdict, Counter
from itertools import compress, cycle

# Simulated sensor readings over time with some noise
data_stream = [107, 214, 107, 321, 428, 214, 535, 642, 535, 535, 749, 856, 749]

# Irrelevant transformation: circular shift (distraction)
shifted_data = data_stream[-3:] + data_stream[:-3]

# Distractor: frequency analysis of values (not directly used in final logic)
frequency_map = defaultdict(int)
for val in data_stream:
    frequency_map[val] += 1
duplicate_values = [k for k, v in frequency_map.items() if v > 1]

# Decoy function: appears useful but unused
def analyze_trend(seq):
    return 'increasing' if seq[-1] > seq[0] else 'decreasing'

# Another red herring: grouping by magnitude bands (unused later)
magnitude_groups = defaultdict(list)
for x in data_stream:
    band = x // 100
    magnitude_groups[band].append(x)

# Real logic begins: identify non-repeating elements using Counter
element_counts = Counter(data_stream)
unique_only = [x for x in data_stream if element_counts[x] == 1]

# Apply transformation: square unique values and filter those above threshold
transformed_unique = [x**2 for x in unique_only]
threshold_filtered = [x for x in transformed_unique if x > 30000]

# Misleading conditional check (dead code path)
if len(threshold_filtered) > 10:
    threshold_filtered.append(sum(threshold_filtered) // 10)

# Real filtering criterion: keep only values divisible by 7
valid_candidates = [x for x in threshold_filtered if x % 7 == 0]

# Simulate a mask using itertools.cycle (complex but necessary step)
mask_pattern = list(cycle([True, False, True]))
masked_data = list(compress(valid_candidates, mask_pattern))

# Final processing: remove outliers above 90% percentile (only two elements, so 90% is just max)
if masked_data:
    sorted_vals = sorted(masked_data)
    cutoff = sorted_vals[-1]  # effectively max since few elements
    filtered_data = [x for x in masked_data if x <= cutoff]
else:
    filtered_data = []

# Key statement
filtered_sum = sum(filtered_data)

# Distractor: secondary calculation with no impact
average_shift = sum(shifted_data) / len(shifted_data) if shifted_data else 0

# Output the target result
print(f"Result: {filtered_sum}")