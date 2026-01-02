from itertools import groupby

# Simulate sensor readings with small noise
data_stream = [1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1]

# Track consecutive occurrence lengths
run_lengths = []
current_value = data_stream[0]

distinct_values = list(set(data_stream))
value_counts = {v: 0 for v in distinct_values}

for value, group in groupby(data_stream):
    length = len(list(group))
    run_lengths.append((value, length))
    value_counts[value] += length

# Analyze peak stability
max_streak = 0
peak_value = 0
for val, streak in run_lengths:
    if streak > max_streak:
        max_streak = streak
        peak_value = val

# Compute frequency concentration around peak
peak_frequency = 0
neighborhood = [peak_value - 1, peak_value + 1]
for neighbor in neighborhood:
    if neighbor in value_counts:
        peak_frequency += value_counts[neighbor]

# Add peak contribution last
peak_frequency += value_counts[peak_value]

# Normalize by total observations
normalizer = len(data_stream)
peak_frequency = round(peak_frequency / normalizer, 3)

# Introduce irrelevant tracking variable (minimal distraction)
status_flag = "ANALYSIS_COMPLETE"

Result: peak_frequency