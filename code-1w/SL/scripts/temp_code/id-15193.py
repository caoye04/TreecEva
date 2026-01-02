from itertools import cycle, islice
import math

# System diagnostic parameters (some are decoys)
turbine_rpm = 12740
efficiency_ratio = 0.873
thermal_load = 421.6
vibration_threshold = 0.93
signal_noise_floor = 0.041
baseline_offset = 113
decoy_counter = 0

# Irrelevant sensor array (dead code path)
sensor_ids = ['S1A', 'S2B', 'X9C', 'R4D']
sensor_status = {sid: False for sid in sensor_ids}

# Core data transformation pipeline
raw_readings = [1.2, 0.8, 1.5, 0.7, 1.1, 1.3, 0.9]
filtered_readings = [x for x in raw_readings if x > 0.75]

# Bit manipulation red herring
temp_flag = 0b1010101
mask = 0b11110000
masked_flag = temp_flag & mask  # Unused

# Character-based key derivation (distraction)
device_fingerprint = 'TURBINE-XG-2023'
key_fragment = ''.join([c for c in device_fingerprint if c.isdigit()])
if len(key_fragment) == 0:
    key_fragment = '113'
validation_key = sum(ord(c) for c in device_fingerprint[:5]) % 17

# Complex processing chain with multiple stages
processing_stages = []
for i, val in enumerate(filtered_readings):
    stage_value = (val ** 2) * (i + 1)
    if i % 2 == 0:
        stage_value = math.sin(stage_value)  # Alternate trigonometric distortion
    else:
        stage_value = math.log(stage_value + 1)  # Natural log transformation
    processing_stages.append(round(stage_value, 6))

# Decoy function that is never called
def legacy_calibrate(data):
    return [d * 0.98 for d in data if d > 0.5]

# Real computation begins here — nested logic with distractions
critical_weights = list(islice(cycle([0.1, 0.2, 0.3]), len(processing_stages)))
weighted_sum = 0
index_tracker = []

for idx, (value, weight) in enumerate(zip(processing_stages, critical_weights)):
    if idx == 0:
        weighted_sum += value * weight * efficiency_ratio
    elif idx < 4:
        adjustment = math.sqrt(idx) if vibration_threshold > 0.9 else 1.0
        weighted_sum += value * weight * adjustment
    else:
        # This block is unreachable due to length of processing_stages
        decoy_counter += 1
        weighted_sum += value * 0.01  # Dead code

    index_tracker.append(idx * baseline_offset)

# Simulated fault injection (unused path)
current_fault_code = None
if weighted_sum < 0:
    current_fault_code = 'ERR_NEGATIVE_SUM'

# String method distraction
diag_header = 'System|Diagnostic|Report'
header_parts = diag_header.split('|')
if len(header_parts) == 4:
    header_parts.append('Legacy')

# Key conditional branch with comparison red herrings
if thermal_load >= 400 and turbine_rpm > 10000:
    scaling_factor = 2.1
else:
    scaling_factor = 1.5

# Final aggregation logic hidden among noise
intermediate_metric = weighted_sum * scaling_factor

# Another decoy variable
normalization_ref = sum(len(part) for part in header_parts)  # Unused

# Actual final computation
final_diagnostic = 0
for x in processing_stages:
    final_diagnostic += x * 100

final_diagnostic = int(final_diagnostic + intermediate_metric) % 100000

# Misleading print statements removed
# Result output (critical)
Result: {final_diagnostic}