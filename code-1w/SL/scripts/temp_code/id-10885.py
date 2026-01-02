import math

# Simulated sensor array data with calibration offsets
data_stream = [14, 17, 23, 34, 45, 52, 67, 71, 83, 94, 105, 113, 127, 136, 149]
offsets = [0.5, -1.2, 0.8, -0.3, 1.1, -0.9, 0.4, -1.0, 0.7, -0.6, 1.3, -0.2, 0.9, -0.8, 1.0]

# Irrelevant backup buffer (distractor)
backup_buffer = data_stream[::-2]
temp_shadow = [x * 1.05 for x in data_stream if x > 50]

# Apply offset corrections to raw data
calibrated_readings = [data_stream[i] + offsets[i] for i in range(len(data_stream))]

# Derive secondary metrics (some used, some not)
rolling_avg = sum(calibrated_readings[5:10]) / 5
variance_estimate = sum((x - rolling_avg) ** 2 for x in calibrated_readings[5:10]) / 5
std_deviation = math.sqrt(variance_estimate)

# Noise threshold calculation (partially relevant)
noise_floor = std_deviation * 0.75
signal_peaks = [x for x in calibrated_readings if x > rolling_avg + noise_floor]

# Decoy statistical analysis (dead path)
entropy_proxy = 0.0
if len(signal_peaks) > 3:
    entropy_proxy = math.log(len(signal_peaks)) * 1.5

# Primary processing pipeline
baseline_reference = sum(calibrated_readings[:7]) // 7  # Integer division
adjusted_values = [int(x - baseline_reference) for x in calibrated_readings]

# Mask generation using bitwise logic (mixed paradigm)
activation_mask = [(x & 1) == 1 for x in adjusted_values]
indexed_signals = [i for i, active in enumerate(activation_mask) if active]

# Red herring: unused recursive function
def integrate_signal(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return 0
    return seq[0] + integrate_signal(seq[1:], depth + 1)

# Real path: filtering and transformation
aggregate_metrics = []
for val in adjusted_values:
    if val > 0:
        transformed = int(math.sqrt(val) * 10)
        aggregate_metrics.append(transformed)
    else:
        aggregate_metrics.append(abs(val))

# Slice-based selection with obfuscation
slice_proxy = slice(2, None, 3)
provisional_set = aggregate_metrics[slice_proxy]

# Filtering logic with misleading intermediate
threshold_criterion = min(provisional_set) * 2
filtered_indices = [i for i, v in enumerate(aggregate_metrics) if v > threshold_criterion and i % 2 == 1]

# Dead code branch (never executed but looks important)
if len(filtered_indices) > 10:
    filtered_indices = filtered_indices[:5]
elif sum(filtered_indices) > 1000:
    filtered_indices = [x - 1 for x in filtered_indices]

# Correction factor derived from multiple sources (key computation)
correction_factor = int((rolling_avg - baseline_reference) / 2) + len(indexed_signals) % 4

# Critical statement: final diagnostic value
final_diagnostic = aggregate_metrics[filtered_indices[-1]] + correction_factor

# Output target result
print(f"Target result: {final_diagnostic}")