from collections import defaultdict

# Simulated sensor data over time (timestamp -> reading)
sensor_readings = [
    (100, 85), (101, 90), (102, 87), (103, 88), (104, 86),
    (105, 91), (106, 89), (107, 92), (108, 84), (109, 85)
]

# Irrelevant backup data (distractor)
backup_readings = [(t+1000, v*2) for t, v in sensor_readings]

# Metrics weighting factors (some are red herrings)
metric_weights = {
    'stability': 0.4,
    'trend': 0.35,
    'peak_ratio': 0.1,  # Not used but looks important
    'noise_floor': 0.05  # Also not used
}

# Extract values only
values = [v for _, v in sensor_readings]

# Compute rolling average for smoothing (3-point window)
smoothed = []
for i in range(1, len(values)-1):
    avg = (values[i-1] + values[i] + values[i+1]) / 3
    smoothed.append(round(avg, 2))

# Dummy transformation on smoothed (not affecting final result)
doubled_smoothed = [2 * x for x in smoothed]

# Analyze trend: count increasing vs decreasing steps
up_steps = 0
flat_or_down = 0
for i in range(1, len(smoothed)):
    if smoothed[i] > smoothed[i-1]:
        up_steps += 1
    else:
        flat_or_down += 1

trend_score = up_steps / (up_steps + flat_or_down) if (up_steps + flat_or_down) > 0 else 0

# Stability metric: inverse of variance
mean_val = sum(smoothed) / len(smoothed)
variance = sum((x - mean_val)**2 for x in smoothed) / len(smoothed)
stability_score = 1 / (1 + variance)  # Normalize to keep bounded

# Phantom metrics using unused weights (dead computations)
phantom_peak_count = 0
for i in range(1, len(values)-1):
    if values[i] > values[i-1] and values[i] > values[i+1]:
        phantom_peak_count += 1

peak_ratio_estimate = phantom_peak_count / len(values)
noise_floor_estimate = min(values) * metric_weights['noise_floor']

# Use enumerate and zip together in a semi-relevant way (tracking index pairs)
indexed_diffs = []
for i, (a, b) in enumerate(zip(smoothed[:-1], smoothed[1:])):
    indexed_diffs.append((i, abs(a - b)))

# Aggregate deviation from ideal flat line
consistency_penalty = sum(diff for _, diff in indexed_diffs) / len(indexed_diffs)

# Final performance score using only stability and trend (others unused)
final_score = stability_score * metric_weights['stability'] + \
              trend_score * metric_weights['trend']

# Additional unrelated computation (distractor)
histogram = defaultdict(int)
for v in values:
    histogram[v // 5] += 1

# Print result as required
print(f"Result: {final_score}")