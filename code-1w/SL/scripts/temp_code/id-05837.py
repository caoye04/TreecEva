import math

# Simulated sensor readings with noise and calibration data
data_stream = [142, 127, 136, 151, 132, 145, 130, 139, 148, 124, 135, 140, 133, 146, 137]
calibration_offsets = [5, -3, 0, 2, -1, 4, -2, 3, 1, -4]

# Irrelevant transformation: frequency analysis (dead code path)
frequencies = {}
for val in data_stream:
    bin_key = val // 10
    frequencies[bin_key] = frequencies.get(bin_key, 0) + 1

# Distractor: complex trigonometric weighting (not used in final calculation)
weighted_readings = []
for i, val in enumerate(data_stream):
    angle = i * math.pi / 4
    weight = math.sin(angle) * math.cos(angle)
    weighted_readings.append(val * (1 + weight))

# Noise threshold calculation (misleading intermediate)
noise_floor = sum(calibration_offsets) / len(calibration_offsets)
adjusted_data = [x - noise_floor for x in data_stream]

# Real processing begins: filter out spikes using hysteresis window
spike_threshold_high = 144
spike_threshold_low = 128
hysteresis_buffer = []
in_alert_state = False
for val in adjusted_data:
    if not in_alert_state and val > spike_threshold_high:
        in_alert_state = True
    elif in_alert_state and val < spike_threshold_low:
        in_alert_state = False
    if not in_alert_state:
        hysteresis_buffer.append(val)

# Secondary filtering: remove outliers based on median (relevant)
def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    return sorted_lst[mid] if n % 2 else (sorted_lst[mid-1] + sorted_lst[mid]) / 2

med = median(hysteresis_buffer)
deviations = [abs(x - med) for x in hysteresis_buffer]
mad = median(deviations)  # Median Absolute Deviation

# Use MAD to define dynamic threshold
outlier_threshold = 2.5 * mad

cleaned_data = [x for x in hysteresis_buffer if abs(x - med) <= outlier_threshold]

# Final adjustment: apply unused calibration curve (distractor)
def calibration_curve(x):
    return int(x * 1.02 - 0.5) if x > 135 else int(x * 0.98 + 0.5)

calibrated_readings = [calibration_curve(x) for x in cleaned_data]  # Not used

# Actual target computation path
bit_flags = [x & 7 for x in cleaned_data]  # Extract last 3 bits
parity_check = sum(1 for flag in bit_flags if bin(flag).count('1') % 2 == 1)

# Key operation: only even-parity values contribute
filtered_data = [cleaned_data[i] for i in range(len(cleaned_data)) if bin(bit_flags[i]).count('1') % 2 == 0]

# Target result
total_energy = sum(x ** 2 for x in data_stream)  # Red herring
baseline_shift = sum(calibration_offsets) * 2  # Misleading
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")