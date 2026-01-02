from collections import defaultdict
from itertools import accumulate

# Simulate sensor readings over time with noise filtering
time_series_data = [105, 110, 98, 120, 125, 118, 130, 140, 138, 150, 160, 155]
noise_floor = 100
filtered_readings = [x for x in time_series_data if x > noise_floor]

# Compute rolling average for smoothing
def rolling_average(data, window_size=3):
    smoothed = []
    for i in range(len(data) - window_size + 1):
        avg = sum(data[i:i+window_size]) / window_size
        smoothed.append(round(avg))
    return smoothed

smoothed_data = rolling_average(filtered_readings)

# Track phase transitions in system state
state_log = defaultdict(int)
prev = smoothed_data[0]
for val in smoothed_data[1:]:
    if val > prev:
        state_log['increase'] += 1
    elif val < prev:
        state_log['decrease'] += 1
    prev = val

# Calculate efficiency ratios per phase
efficiency_ratios = [(b - a) / a for a, b in zip(smoothed_data, smoothed_data[1:])]

# Misleading computation: irrelevant harmonic mean
total_inv = sum(1/x for x in smoothed_data)
harm_mean = len(smoothed_data) / total_inv  # unused distractor

# Normalize efficiency ratios to percentage scale
normalized_scores = [max(0, min(100 * r, 100)) for r in efficiency_ratios]

# Apply artificial damping factor based on transition count
damping_factor = 1 - (state_log['decrease'] / (state_log['increase'] + state_log['decrease'] + 1))
damped_scores = [score * damping_factor for score in normalized_scores]

# Accumulate trend strength as red herring
trend_strength = list(accumulate(damped_scores, lambda x, y: x + y * 0.9))

# Core result: peak efficiency after damping
efficiencies = [r * 100 for r in efficiency_ratios]  # raw efficiency before damping used in final step
peak_efficiency = max(efficiencies)

# Dead code path - never executed due to prior logic
if False:
    backup_peak = max(normalized_scores)
    peak_efficiency = backup_peak

print(f"Result: {peak_efficiency}")