import math

# Simulated sensor array data with calibration offsets
data_stream = [142, 137, 146, 158, 133, 141, 155, 139, 144, 152, 135, 148, 143, 151, 136]

calibration_factor = 0.98
offset_map = {i: (i % 3) * 0.1 for i in range(len(data_stream))}
adjusted_readings = [round(d * calibration_factor + offset_map[i]) for i, d in enumerate(data_stream)]

# Irrelevant transformation: frequency analysis on index patterns
index_freq = [i for i in range(len(adjusted_readings)) if i % 2 == 0 and i > 5]
decoys = [x * 2 + 1 for x in index_freq if x < 10]
phantom_shift = sum(decoys) % 7 if decoys else 0

# Signal integrity check (distractor)
noise_floor = 130
is_signal_valid = all(val > noise_floor for val in adjusted_readings)
redundant_checksum = 0
for idx, val in enumerate(adjusted_readings):
    if idx % 4 == 0:
        redundant_checksum ^= int(val) % 17

# Critical path begins: filter anomalies using moving threshold
baseline = sum(adjusted_readings) / len(adjusted_readings)
anomaly_threshold = baseline * 1.08

# Masked filtering logic with red herring condition
strict_mode = False
temp_buffer = []
for reading in adjusted_readings:
    if reading < baseline * 0.92:
        temp_buffer.append(reading)
    elif reading > anomaly_threshold and not strict_mode:
        # This branch is never taken due to strict_mode=False, but looks important
        temp_buffer.append(int(reading * 0.85))
    else:
        temp_buffer.append(reading)

# Secondary filter: exclude values deviating by more than 12% from local window
local_window_size = 3
smoothed = []
for i in range(len(temp_buffer)):
    start = max(0, i - local_window_size // 2)
    end = min(len(temp_buffer), i + local_window_size // 2 + 1)
    window_avg = sum(temp_buffer[start:end]) / (end - start)
    if abs(temp_buffer[i] - window_avg) / window_avg <= 0.12:
        smoothed.append(temp_buffer[i])

# Decoy structure: unused filtered set
exclusion_set = {x for x in temp_buffer if x in [133, 155, 158]}
filtered_measurements = [x for x in smoothed if x not in exclusion_set]

# Tertiary distraction: recursive validation (unused result)
def validate_sequence(seq, depth=0):
    if depth >= 3 or len(seq) < 2:
        return len(seq) % 4
    return validate_sequence(seq[::2], depth + 1)

_ = validate_sequence(filtered_measurements)

# Key computation point — answer determined here
filtration_yield = sum(filtered_measurements) // len(filtered_measurements)

# Dead code path: obfuscated alternate calculation
if __debug__:
    backup_weights = [math.log(x + 1) for x in filtered_measurements if x > 140]
    if backup_weights:
        alternative = sum(backup_weights) / len(backup_weights)
        filtration_yield = int(alternative * 10)  # Never executed in optimized mode

print(f"Result: {filtration_yield}")