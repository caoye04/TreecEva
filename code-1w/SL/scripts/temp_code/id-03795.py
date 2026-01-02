import itertools

# Simulated sensor data stream with noise and valid readings
data_stream = [15, 0, 23, 0, 47, 12, 0, 31, 19, 0, 44]

# Thresholds for signal validation
valid_threshold = 20
noise_marker = 0

# Tracking variables (some are just for logging or debugging)
count_valid = 0
total_raw = 0
count_noise = 0
signal_history = []

# Intermediate processing list
filtered_data = []
for val in data_stream:
    total_raw += val
    if val == noise_marker:
        count_noise += 1
    else:
        if val > valid_threshold:
            filtered_data.append(val)
            count_valid += 1
            signal_history.append((len(signal_history), val))

# Additional distraction: analyze gaps between valid signals
gap_analysis = []
last_index = -1
for i, val in enumerate(data_stream):
    if val != noise_marker and val > valid_threshold:
        if last_index != -1:
            gap_analysis.append(i - last_index - 1)
        last_index = i

# Use itertools to generate rolling window of filtered data (distraction)
windowed_pairs = list(itertools.pairwise(filtered_data))
edge_transitions = 0
for a, b in windowed_pairs:
    if (a % 2) != (b % 2):  # Count odd-even transitions
        edge_transitions += 1

# Real computation begins: compute weighted sum using enumerate
weighted_sum = 0
for idx, value in enumerate(filtered_data):
    weight = 1 + (idx * 0.1)
    weighted_sum += value * weight

# Secondary distraction: zipping unrelated sequences
aux_indices = list(range(len(signal_history)))
mapped_pairs = list(zip(aux_indices, [x[1] for x in signal_history]))
sum_mapped_keys = sum(k for k, v in mapped_pairs if v % 3 == 0)

# Core logic disguised among distractions
baseline_estimate = sum(filtered_data)
adjustment = len(windowed_pairs) * 1.5
processed_sum = int(weighted_sum - baseline_estimate + adjustment)

correction_factor = 3
final_output = processed_sum * correction_factor

# Dummy dictionary operations for interference
diag_log = {
    'readings': len(data_stream),
    'valid_count': count_valid,
    'noise_count': count_noise,
    'transitions': edge_transitions,
    'sum_filtered': sum(filtered_data),
    'gap_total': sum(gap_analysis) if gap_analysis else 0
}

# Irrelevant stat calculation
avg_gap = diag_log['gap_total'] / (len(gap_analysis) or 1)

# Only this line matters for the answer
print(f"Target result: {final_output}")