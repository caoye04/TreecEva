import itertools

# System health monitoring simulation with diagnostic calibration
base_readings = [12, 15, 10, 8, 20, 14, 16, 11]

# Irrelevant transformation: frequency mapping (distractor)
frequency_map = {}
for val in base_readings:
    frequency_map[val] = frequency_map.get(val, 0) + 1

# Redundant smoothing pass (dead code path)
smoothed = []
for i in range(len(base_readings)):
    window = base_readings[max(0, i-1):min(i+2, len(base_readings))]
    smoothed.append(sum(window) / len(window))

# Unused recursive peak detector (decoy function)
def find_peak_recursive(data, idx=0):
    if idx == len(data) - 1:
        return data[idx]
    next_peak = find_peak_recursive(data, idx + 1)
    return max(data[idx], next_peak)

# Simulated noise threshold adjustment (misleading intermediate)
noise_floor = 9
adjusted_readings = [x if x > noise_floor else noise_floor for x in base_readings]

# Hidden relevant logic: group by magnitude and count outliers
grouped = {k: list(g) for k, g in itertools.groupby(sorted(adjusted_readings), key=lambda x: x // 5)}
outlier_groups = [k for k, v in grouped.items() if len(v) < 3]

# Secondary distractor: rolling average buffer
buffer = []
for i in range(len(adjusted_readings)):
    subset = adjusted_readings[:i+1]
    avg = sum(subset) / len(subset)
    buffer.append(round(avg, 2))

# Key computation chain begins here
aggregate_measure = 0
for group in grouped.values():
    for val in group:
        aggregate_measure += val * 0.75  # Weighted accumulation

# Phantom normalization (looks important but unused later)
normalized_total = sum([x ** 0.5 for x in adjusted_readings]) / len(adjusted_readings)

# Correction factor derived from outlier structure
correction_factor = len(outlier_groups) ** 2 if outlier_groups else 1

# Offset based on initial system bias
offset_value = base_readings[0] // 4

# Critical assignment with multiple dependencies
final_diagnostic = aggregate_measure * correction_factor + offset_value

# Dead code: attempt to log unused metric
log_entry = f"Final={final_diagnostic:.1f}"
placeholder_list = [log_entry] * 3

# Output the target result
print(f"Result: {final_diagnostic}")