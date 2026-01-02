import itertools

# Sensor array data processing simulation with noise filtering and calibration
raw_readings = [107, 214, 198, 205, 999, 201, 103, 200, 199, 500, 202]
noise_floor = 150
saturation_limit = 900

def detect_anomalies(data, threshold):
    """Identify indices where values exceed threshold (distractor function)"""
    return [i for i, x in enumerate(data) if x > threshold]

def apply_mask(sequence, mask_values):
    """Apply arbitrary transformation (red herring)"""
    return [a ^ b for a, b in zip(sequence, itertools.cycle(mask_values))]

# Irrelevant preprocessing steps
temp_buffer = [x for x in raw_readings if x < saturation_limit]
spike_indices = detect_anomalies(raw_readings, 200)
mask_pattern = [7, 13, 21]
applied_mask = apply_mask(temp_buffer, mask_pattern)

# Actual relevant signal extraction
valid_range = [x for x in raw_readings if 100 <= x <= 205]
outlier_count = len([x for x in raw_readings if x > 205])

# Decoy statistical analysis
mean_raw = sum(raw_readings) / len(raw_readings)
variance_proxy = sum((x - mean_raw) ** 2 for x in raw_readings) / len(raw_readings)
fluctuation_score = abs(mean_raw - variance_proxy) // 10

# Data normalization layer (some steps are distractions)
calibration_map = {107: 100, 103: 100, 198: 200, 199: 200, 200: 200, 201: 200, 202: 200, 205: 200}
normalized_signals = []
for val in valid_range:
    if val in calibration_map:
        normalized_signals.append(calibration_map[val])
    else:
        normalized_signals.append(val)

# Simulated environmental compensation (mixed relevance)
ambient_drift = 3
compensated = [val - ambient_drift for val in normalized_signals if val >= 150]

# Filtered data path (this is the actual input used later)
filtered_data = [x for x in compensated if x % 50 == 0]  # Only multiples of 50

# Redundant set operations for interference
unique_compensated = list(set(compensated))
sorted_unique = sorted(unique_compensated, reverse=True)
duplicate_check = len(compensated) - len(unique_compensated)

# Phantom aggregation using string methods (completely irrelevant)
status_log = "System operational at all times"
log_parts = status_log.split(' ')
word_lengths = [len(word) for word in log_parts]
checksum_tag = ''.join([part[0] for part in log_parts if len(part) > 1])

# Bit manipulation decoy chain
bitwise_accum = 0
for x in spike_indices:
    bitwise_accum ^= x << 2
    bitwise_accum |= 0b1010

# Core processing function (only this matters for final result)
def process_readings(readings, factor):
    base = sum(readings) * factor
    if len(readings) >= 3:
        base -= factor * 4
    return int(base)

# Multiple candidate calibration factors (only one is correct)
alt_cal_1 = fluctuation_score // 2
alt_cal_2 = outlier_count + 1
calibration_factor = len(filtered_data)  # This evaluates to 3

# Final computation depends only on filtered_data and correct calibration_factor
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output the required variable
print(f"Result: {final_diagnostic}")