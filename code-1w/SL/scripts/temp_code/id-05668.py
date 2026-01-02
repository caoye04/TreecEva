import math

# Simulated sensor data with noise and redundant metadata
data_stream = [127, 83, 156, 42, 91, 205, 64, 73, 112, 55, 134, 49, 88, 102, 77]
metadata_map = {'source': 'sensor_array_A', 'version': '3.1.4', 'calibration': 0.987}
noise_floor = 40
amplification_factor = 1.8
offset_correction = -5

# Irrelevant transformation: bit manipulation on metadata keys (dead path)
dummy_key_hash = 0
for char in metadata_map['source']:
    dummy_key_hash ^= ord(char) << 2

# Decoy list comprehensions with unused results
coarse_filtered = [x for x in data_stream if x > noise_floor + 10]
squared_signals = [x ** 2 for x in data_stream if x % 2 == 0]
shifted_noise = [x >> 2 for x in data_stream]

# Real signal processing begins here — masked by irrelevant prior ops
calibrated = [int((x + offset_correction) * amplification_factor) for x in data_stream]

# Apply non-linear correction using logarithmic scaling where applicable
log_corrected = []
for val in calibrated:
    if val > 0:
        log_val = int(math.log(val) * 10)
        log_corrected.append(log_val)
    else:
        log_corrected.append(0)

# Frequency masking simulation: keep only values in specific 'band'
frequency_band_mask = []
for idx, val in enumerate(log_corrected):
    band_lower = 8 + (idx % 3)  # Dynamic threshold
    band_upper = 24 - (idx % 4)
    if band_lower <= val <= band_upper:
        frequency_band_mask.append(True)
    else:
        frequency_band_mask.append(False)

# Destructuring a slice of the mask to simulate window analysis
window_start, window_end = 2, len(frequency_band_mask) - 2
active_window = frequency_band_mask[window_start:window_end]

# Secondary filter based on original magnitude thresholds (cross-reference)
magnitude_valid = [original > 85 for original in data_stream]

# Combine filters: both frequency response and magnitude must align
combined_mask = []
for i in range(len(frequency_band_mask)):
    if i < len(magnitude_valid) and i < len(frequency_band_mask):
        combined_mask.append(frequency_band_mask[i] and magnitude_valid[i])
    else:
        combined_mask.append(False)

# Extract filtered data from log_corrected using combined_mask
filtered_data = []
for i, valid in enumerate(combined_mask):
    if valid and i < len(log_corrected):
        filtered_data.append(log_corrected[i])

# Dead code path: reverse slicing with no usage
reversed_tail = log_corrected[-5:][::-1]
temp_aggregate = sum(reversed_tail) // 2  # Unused intermediate

# Critical computation point
filtered_result = sum(filtered_data)

# Red herring: floating-point conversion with truncation
final_output = float(filtered_result) / 1.000001

# Output target result
print(f"Result: {filtered_result}")