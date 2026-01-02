from collections import defaultdict
from itertools import combinations

# Simulate sensor readings from a distributed energy grid over time
sensor_data = [
    [12, 15, 14, 13, 16],
    [8, 10, 9, 11, 12],
    [20, 18, 22, 19, 21],
    [5, 7, 6, 8, 9]
]

# Misleading auxiliary data - not used in final result
auxiliary_metrics = [[x**2 + 2*x + 1 for x in row] for row in sensor_data]
dummy_aggregates = [sum(row) * 0.5 for row in auxiliary_metrics]

# Track efficiency per node using meaningful computation
node_readings = defaultdict(list)
for i, readings in enumerate(sensor_data):
    for j, value in enumerate(readings):
        node_readings[f'node_{i}'].append(value * (1.1 + 0.05 * j))  # Time-decay adjusted

# Compute baseline averages (distractor)
baseline_averages = {k: sum(v) / len(v) for k, v in node_readings.items()}

# Real processing: calculate rolling window efficiency for valid nodes
filtered_nodes = []
for node_id, values in node_readings.items():
    if len(values) > 4:  # Only consider stable nodes
        # Apply smoothing filter
        smoothed = [sum(values[i:i+3]) / 3 for i in range(len(values) - 2)]
        filtered_nodes.append(smoothed)

# Extract peak transient responses (red herring)
transient_peaks = []
for series in filtered_nodes:
    for a, b in zip(series, series[1:]):
        if b - a > 0.5:
            transient_peaks.append(b)

# Core logic: compute efficiency ratios from stabilized values
stabilized_efficiencies = []
for series in filtered_nodes:
    mid_point = len(series) // 2
    # Use only post-stabilization segment
    stable_segment = series[mid_point:]
    efficiency_ratio = sum(stable_segment) / (len(stable_segment) * 10)
    stabilized_efficiencies.append(efficiency_ratio)

# Add dummy correction factor (has no effect due to normalization)
correction_map = defaultdict(float)
for idx in range(len(stabilized_efficiencies)):
    correction_map[idx] = sum(1/(i+1) for i in range(idx+1)) if idx % 2 == 0 else 0

# Final efficiency calculations with injected noise (neutralized)
efficiencies = []
for val in stabilized_efficiencies:
    raw_score = val * 100
    noise_adjusted = raw_score + sum([(-1)**n * 0.1 for n in range(5)])  # Net zero
    efficiencies.append(noise_adjusted)

# Critical statement
peak_efficiency = max(efficiencies)

print(f"Result: {peak_efficiency}")