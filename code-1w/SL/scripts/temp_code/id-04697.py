import math

# Simulated sensor data stream with noise and redundant metadata
data_packet = [0.1, -0.3, 0.5, 1.2, 2.4, 3.6, 4.1, 3.9, 2.8, 1.6, 0.4, -0.2, -1.5, -2.7, -3.3]
metadata = {'source': 'satellite_A', 'version': '3.1.4', 'calibration': 0.987, 'timestamp': 1678823456}

# Irrelevant checksum calculation (distractor)
def compute_checksum(arr):
    return sum([arr[i] * (i + 1) for i in range(len(arr))]) % 1024

checksum = compute_checksum(data_packet)  # Dead-end computation

# Signal preprocessing pipeline
filtered_data = [x for x in data_packet if abs(x) > 0.25]  # Remove low-amplitude noise
inverted_data = [-x for x in filtered_data]  # Inversion for phase correction (not used later)

# Amplify signal based on dynamic gain
amplification_levels = [1.0, 1.5, 2.0, 2.5, 3.0]
gain = amplification_levels[len(filtered_data) % 5]
amplified_data = [gain * x for x in filtered_data]

# Apply logarithmic compression to stabilize variance
compressed_data = [math.log(abs(x) + 1) for x in amplified_data]

# Normalize using min-max scaling
min_val, max_val = min(compressed_data), max(compressed_data)
normalized_data = [(x - min_val) / (max_val - min_val + 1e-8) for x in compressed_data]

# Slice central portion of signal for analysis
window_start = len(normalized_data) // 3
window_end = len(normalized_data) - window_start
processed_data = normalized_data[window_start:window_end]

# Identify trigger point via misleading peak detection (red herring)
peak_index = 0
for i in range(1, len(normalized_data)):
    if normalized_data[i] > normalized_data[peak_index]:
        peak_index = i

# Actual trigger logic: first value exceeding threshold after midpoint
midpoint = len(processed_data) // 2
candidate_indices = [i for i in range(midpoint, len(processed_data)) if processed_data[i] > 0.65]
if candidate_indices:
    trigger_index = candidate_indices[0]
else:
    trigger_index = -1

# Correction factor derived from irrelevant calibration constant
# (but actually depends on static known value)
correction_factor = metadata['calibration']
correction_factor *= (1 + 0.1 * math.sin(math.pi / 3))

# Final signal extraction — critical execution point
final_signal = processed_data[trigger_index] * correction_factor

# Print result for evaluation
print(f"Result: {final_signal}")