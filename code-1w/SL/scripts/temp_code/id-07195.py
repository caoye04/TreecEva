from itertools import combinations

# Simulate sensor readings from a solar array over 5 time intervals
sensor_a = [12, 15, 10, 18, 22]
sensor_b = [14, 13, 11, 19, 20]
sensor_c = [10, 16, 14, 17, 21]

# Misleading derived metrics (distractor computations)
total_readings = len(sensor_a) * 3
average_raw = sum(sensor_a + sensor_b + sensor_c) / total_readings
drift_compensation = 0.95

# Compute pairwise correlation scores between sensors (semi-relevant)
correlations = []
for i in range(len(sensor_a)):
    corr_ab = abs(sensor_a[i] - sensor_b[i])
    corr_bc = abs(sensor_b[i] - sensor_c[i])
    correlations.append((corr_ab + corr_bc) / 2)

# Efficiency calculation per time interval using non-uniform weighting
weights = [0.3, 0.4, 0.3]  # Emphasize middle sensor
weighted_efficiency = []
for t in range(len(sensor_a)):
    raw_eff = weights[0] * sensor_a[t] + weights[1] * sensor_b[t] + weights[2] * sensor_c[t]
    adjusted = raw_eff * drift_compensation
    weighted_efficiency.append(round(adjusted, 2))

# Generate all possible 3-interval performance windows (combinatorics via itertools)
indices = list(range(len(weighted_efficiency)))
three_point_windows = list(combinations(indices, 3))

# Compute average efficiency for each window
window_averages = []
for window in three_point_windows:
    avg = sum(weighted_efficiency[i] for i in window) / len(window)
    window_averages.append(round(avg, 2))

# Normalize against maximum possible window average (theoretical)
max_possible = max(weighted_efficiency) * 3 / 3
normalized_scores = [score / max_possible for score in window_averages]

# Final system efficiencies with outlier suppression
efficiencies = []
for score in normalized_scores:
    if score > 0.7:  # Filter out low-performance windows
        efficiencies.append(score * 100)

# Critical statement
peak_efficiency = max(efficiencies)

# Irrelevant aggregation (dead code path)
summary_stats = {
    'count': len(efficiencies),
    'floor': min(efficiencies),
    'ceiling': max(efficiencies),
    'range': max(efficiencies) - min(efficiencies)
}

# Unused helper function (distractor)
def smooth(data, factor=0.1):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(smoothed[-1] * (1 - factor) + data[i] * factor)
    return smoothed

print(f'Result: {peak_efficiency}')