from collections import defaultdict
from itertools import combinations

# Simulate sensor readings from a distributed energy grid over time
sensor_data = [
    [12, 15, 14, 13, 16],
    [9, 11, 10, 12, 11],
    [18, 17, 19, 20, 18],
    [7, 8, 7, 9, 6],
    [14, 15, 15, 16, 14]
]

# Irrelevant metadata (distractor)
location_names = ['North', 'South', 'East', 'West', 'Central']
timestamps = [1623456000, 1623456600, 1623457200, 1623457800, 1623458400]

# Track node contributions (semi-relevant)
node_contributions = defaultdict(float)
for i, readings in enumerate(sensor_data):
    for j, value in enumerate(readings):
        node_contributions[f'Node_{i}'] += value * (0.95 + j*0.01)  # Weighted by time decay

# Compute rolling averages per sensor (distraction computation)
rolling_averages = []
for readings in sensor_data:
    averages = []
    for k in range(2, len(readings)):
        avg = sum(readings[k-2:k+1]) / 3
        averages.append(round(avg, 2))
    rolling_averages.append(averages)

# Extract peak values and baseline stability check (mixed relevance)
stability_flags = {}
baseline_peaks = []
for idx, readings in enumerate(sensor_data):
    sorted_readings = sorted(readings)
    median_val = sorted_readings[len(sorted_readings)//2]
    q1 = sorted_readings[len(sorted_readings)//4]
    q3 = sorted_readings[3*len(sorted_readings)//4]
    iqr = q3 - q1
    stability_flags[f'Zone_{idx}'] = (iqr <= 3)
    baseline_peaks.append(max(readings) - min(readings))

# Core efficiency calculation: normalize each sensor's output relative to its range
range_normalized = []
for readings in sensor_data:
    data_min, data_max = min(readings), max(readings)
    if data_max == 0:
        normalized = [0 for _ in readings]
    else:
        normalized = [(x - data_min) / (data_max - data_min) for x in readings]
    range_normalized.append(normalized)

# Calculate efficiency score using combinatorics on normalized peaks
efficiencies = []
for norm_set in range_normalized:
    # Consider top-2 combinations for load balancing score
    valid_peaks = [p for p in norm_set if p > 0.5]
    combo_scores = []
    for combo in combinations(valid_peaks, max(1, len(valid_peaks)//2)):
        combo_score = sum(combo) / len(combo) if combo else 0
        combo_scores.append(combo_score)
    final_score = sum(combo_scores) / len(combo_scores) if combo_scores else 0
    efficiencies.append(round(final_score * 100, 2))

# Introduce irrelevant transformation (dead path)
distorted_efficiencies = [e * 1.5 for e in efficiencies if e > 60]
if len(distorted_efficiencies) > 3:
    distorted_efficiencies = [d - 10 for d in distorted_efficiencies]

# Key statement
peak_efficiency = max(efficiencies)

# Debug print removed to avoid hinting
# Final output
print(f"Result: {peak_efficiency}")