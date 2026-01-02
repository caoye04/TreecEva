import math

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 1, 'val': 23.5, 'meta': 'A', 'temp_raw': 2350, 'status': 1},
    {'id': 2, 'val': -999, 'meta': 'X', 'temp_raw': 1820, 'status': 0},  # invalid reading
    {'id': 3, 'val': 19.8, 'meta': 'B', 'temp_raw': 1980, 'status': 1},
    {'id': 4, 'val': 21.0, 'meta': 'A', 'temp_raw': 2100, 'status': 1},
    {'id': 5, 'val': -999, 'meta': 'Z', 'temp_raw': 2050, 'status': 0},  # invalid reading
    {'id': 6, 'val': 22.3, 'meta': 'C', 'temp_raw': 2230, 'status': 1}
]

# Irrelevant auxiliary data (distractor)
system_log = [
    {'event': 'boot', 'code': 100},
    {'event': 'reset', 'code': 205},
    {'event': 'poll', 'code': 100}
]
event_count = sum(1 for log in system_log if log['code'] == 100)  # red herring

# Extraneous transformation (dead path)
raw_temps = [entry['temp_raw'] for entry in data_stream]
avg_raw = sum(raw_temps) / len(raw_temps)
normalized_offsets = [x - avg_raw for x in raw_temps]  # unused

# Faulty filtering attempt (misleading intermediate)
inactive_ids = [entry['id'] for entry in data_stream if entry['status'] == 0]
temp_lookup = {entry['id']: entry['val'] for entry in data_stream}

# Real processing begins here
valid_entries = [e for e in data_stream if e['val'] != -999]
filtered_data = [e['val'] for e in valid_entries if e['meta'] in ['A', 'C']]

# Decoy statistical computation
decoy_mean = sum(e['val'] for e in valid_entries) / len(valid_entries)
decoy_variance = sum((e['val'] - decoy_mean)**2 for e in valid_entries) / len(valid_entries)

# Calibration parameters (some misleading ones)
baseline_offset = 273.15
calibration_factor = 0.89
scaling_factor = 1.05  # not used
temp_correction = lambda x: x * 1.01 + 0.5  # defined but not used

# Complex conditional expression with list comprehension and zip (required features)
index_shift = [
    (i, val) for i, val in enumerate(
        [x * calibration_factor for x in filtered_data]
    ) if i % 2 == 0
]

# Secondary irrelevant structure
duplicate_check = {}
for idx, val in enumerate(filtered_data):
    if val in duplicate_check:
        duplicate_check[val].append(idx)
    else:
        duplicate_check[val] = [idx]

# Mock ML model weight (distractor)
weights = [0.1, 0.4, 0.3, 0.2]
predicted_score = sum(w * (idx + 1) for w, (idx, _) in zip(weights, index_shift))  # meaningless

# Actual core logic hidden among distractions
def process_readings(readings, factor):
    adjusted = [r * factor for r in readings]
    base_sum = sum(adjusted)
    
    # Apply non-linear correction using enumerate and conditional expression
    corrected = []
    for i, v in enumerate(adjusted):
        correction = v * 0.01 if i % 2 == 0 else v * 0.005
        corrected.append(v + correction)
    
    # Final aggregation using multiple steps
    total = sum(corrected)
    penalty = len(corrected) > 3 else 0.5  # boolean logic with short-circuit
    penalty *= 1.5
    return int(total - penalty)  # deterministic integer output

# Key execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

print(f"Result: {final_diagnostic}")