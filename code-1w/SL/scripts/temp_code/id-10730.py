from collections import defaultdict
import math

# Simulate sensor data with timestamps and readings
timestamps = list(range(100, 200, 3))
raw_readings = [t * 0.7 + ((t % 11) ** 1.5) for t in timestamps]

# Misleading irrelevant data
noise_floor = 42.5
baseline_offset = sum([math.sin(t / 10) for t in range(50)]) / 50
offset_correction = lambda x: x - noise_floor if x > noise_floor else x

# Process data in chunks
data_chunks = defaultdict(list)
for i, (ts, val) in enumerate(zip(timestamps, raw_readings)):
    bucket = i // 5
    data_chunks[bucket].append(val)

# Extract statistical features (some used, some not)
means = {}
medians = {}
variances = {}  # distractor: calculated but not used later
deviation_sum = 0  # accumulator for relevant logic

for chunk_id, values in data_chunks.items():
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    means[chunk_id] = sum(sorted_vals) / n
    medians[chunk_id] = sorted_vals[n//2]
    mean_val = means[chunk_id]
    variances[chunk_id] = sum((x - mean_val) ** 2 for x in values) / n  # computed but unused
    deviation_sum += abs(mean_val - medians[chunk_id])

# Secondary processing: filter and transform
filtered_means = [m for m in means.values() if m > 60]
transformed = [math.log(m) ** 2 for m in filtered_means]

# Red herring function
def apply_calibration(data):
    """Irrelevant calibration that isn't applied"""
    return [d * 0.98 + 1.2 for d in data]

# Real processing path
def rolling_window_avg(lst, window=3):
    if len(lst) < window:
        return [sum(lst)/len(lst)] if lst else [0]
    return [sum(lst[i:i+window]) / window for i in range(len(lst)-window+1)]

smoothed = rolling_window_avg(transformed, 4)

# Distractor variables
peak_value = max(smoothed) if smoothed else 0
decay_factor = 0.95 ** len(smoothed)

# Final computation chain
aggregated = sum(smoothed) * (deviation_sum / len(means))
scaling_constant = len(filtered_means) / len(means) if means else 0
intermediate_score = aggregated * scaling_constant

# Key transformation
adjustment_map = {i: 0.1 * i for i in range(len(smoothed))}
adjustment = sum(adjustment_map.values()) if len(smoothed) > 1 else 0.5

final_score = 0
final_score += intermediate_score
final_score -= adjustment
final_score = round(final_score, 3)

# Additional dead-end calculation (distractor)
temp_analysis = list(map(lambda x: x ** 0.5, transformed[:5]))
invalidation_flag = any([t < 0 for t in temp_analysis])

Result: final_score