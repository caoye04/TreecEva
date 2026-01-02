from collections import defaultdict, Counter

# Simulated sensor array data processing with diagnostic validation
sensor_readings = [14, 28, 14, 35, 42, 28, 14, 56, 49, 35, 70]
configuration_flags = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
baseline_threshold = 14
temporal_weights = [0.8, 1.2, 0.9, 1.1, 1.0, 0.85, 0.95, 1.15, 1.05, 0.75, 1.25]

# Irrelevant transformation: frequency analysis (unused)
frequency_map = defaultdict(int)
for reading in sensor_readings:
    frequency_map[reading] += 1

# Distractor: noise estimation with dead-end logic
noise_estimate = 0
for i, val in enumerate(sensor_readings):
    if val % 7 == 0 and configuration_flags[i]:
        noise_estimate += val * 0.05

# Decoy function: never called
def calculate_robustness_index(data):
    return sum(d ** 0.5 for d in data if d > 20) / len(data)

# Misleading intermediate metric (appears important but unused)
stability_ratio = sum(1 for x in sensor_readings if x >= baseline_threshold) / len(sensor_readings)

# Real processing begins: filter valid high-confidence readings
valid_indices = []
weighted_sum = 0
for i in range(len(sensor_readings)):
    if configuration_flags[i] == 1 and sensor_readings[i] % 7 == 0:
        valid_indices.append(i)

# Apply temporal weights to valid readings
adjusted_values = []
for idx in valid_indices:
    adjusted_values.append(sensor_readings[idx] * temporal_weights[idx])

# Aggregate using sliding window analysis (3-element)
aggregated_windows = []
for i in range(len(adjusted_values) - 2):
    window_avg = sum(adjusted_values[i:i+3]) / 3
    aggregated_windows.append(window_avg)

# Use set operations to deduplicate close values (within tolerance)
deduplicated = set()
for val in aggregated_windows:
    rounded_val = round(val)
    deduplicated.add(rounded_val)

# Compute aggregate score as sum of unique window averages
deep_analysis_trace = []
aggregate_score = 0
for val in sorted(deduplicated):
    if val > 30:
        aggregate_score += val * 1.1
    else:
        aggregate_score += val * 0.9
    deep_analysis_trace.append(val)

# Correction factor based on pattern analysis of original sequence
pattern_counter = Counter()
for i in range(len(sensor_readings) - 1):
    diff = sensor_readings[i+1] - sensor_readings[i]
    pattern_counter[diff > 0] += 1

positive_trend = pattern_counter[True]
negative_trend = pattern_counter[False]
correction_factor = (positive_trend - negative_trend) * 2.5

# Secondary distractor: slicing operation with unused result
slice_analysis = sensor_readings[::2][1:4]
outlier_check = [x for x in slice_analysis if x < 50]

# Final diagnostic computation (critical execution point)
final_diagnostic = aggregate_score + correction_factor

# Red herring: unused conditional branch
if final_diagnostic < 100:
    final_diagnostic *= 1.5

# Answer output
print(f"Result: {final_diagnostic}")