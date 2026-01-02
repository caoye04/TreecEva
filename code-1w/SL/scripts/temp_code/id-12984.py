from itertools import combinations
from math import log

# Sensor data processing simulation with diagnostic logic
raw_readings = [145, 256, 98, 412, 333, 77, 192, 88, 301]
baseline_offset = 88
noise_floor = {x % 17 for x in raw_readings}  # Irrelevant noise profile

def apply_calibration(data, offset):
    """Calibrate sensor readings by offset (unused branch)"""
    return [d - offset + 1 for d in data]

def detect_anomalies(seq, limit):
    """Find values exceeding limit (red herring function)"""
    anomalies = []
    for val in seq:
        if val > limit:
            anomalies.append(val)
    return anomalies  # Never actually used

temp_buffer = []
for reading in raw_readings:
    if reading > 100:
        temp_buffer.append(reading)

# Multiple filtering stages with distractor logic
primary_filter = [x for x in raw_readings if x % 2 == 0]
secondary_filter = [x for x in primary_filter if x > 90]

# Bit manipulation decoy: simulates signal encoding
encoded_signals = []
for val in secondary_filter:
    encoded = (val << 2) ^ 255  # Shift and XOR (not used later)
    normalized = encoded / 255.0
    encoded_signals.append(normalized)

# Distractor: combinatorial analysis of irrelevant pairs
pair_analysis = list(combinations([77, 88, 98], 2))
count_invalid = 0
for a, b in pair_analysis:
    if (a + b) % 13 == 0:
        count_invalid += 1  # Dead computation

# Real processing begins here — obscure due to prior noise
working_set = set(raw_readings)
threshold_set = {x for x in working_set if x > 200}

# Simulated environmental compensation (partial use)
compensation_map = {}
for key in threshold_set:
    comp_val = int(log(key, 2)) if key != 0 else 0
    compensation_map[key] = comp_val  # Used later

# Filtering chain with misleading intermediate
intermediate_mask = [x for x in raw_readings if x < 350]
filtered_data = [x for x in intermediate_mask if x in threshold_set]

# Decoy statistical summary (never used)
mean_proxy = sum(filtered_data) / len(filtered_data) if filtered_data else 0
variance_snapshot = sum((x - mean_proxy) ** 2 for x in filtered_data) / len(filtered_data) if filtered_data else 0

# Core diagnostic logic — depends on map and bit count
running_diagnostic = 0
for val in filtered_data:
    bits = bin(val).count('1')
    comp_factor = compensation_map[val]
    contribution = bits * comp_factor
    running_diagnostic += contribution

# Final adjustment using set intersection decoy
auxiliary_keys = {256, 412, 999, 123}
dynamic_weight = len(threshold_set & auxiliary_keys)  # Only some overlap

# Key statement
final_diagnostic = process_readings(filtered_data, threshold_set)

# Actual implementation hidden below (simulates late binding)
def process_readings(data_list, thresholds):
    local_sum = 0
    for item in data_list:
        if item in thresholds:
            shift_op = (item ^ 211) >> 3  # Bitwise mix
            bit_density = bin(shift_op).count('1')
            local_sum += bit_density * 3
    return local_sum + dynamic_weight

print(f"Result: {final_diagnostic}")