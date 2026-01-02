import math

# Simulated sensor array data with noise and calibration offsets
data_stream = [127, 255, 0, 64, 192, 32, 160, 96, 224, 15]
calibration_map = {i: round(math.sin(i * 0.1) * 5, 2) for i in range(10)}
noise_floor = 42
offset_correction = -3

# Irrelevant pre-processing: checksum validation (never used)
total_checksum = sum(d ^ 0x5F for d in data_stream) % 256
if total_checksum > 100:
    adjustment_factor = 1.5
else:
    adjustment_factor = 0.8

# Decoy function: simulates temperature compensation but unused
def apply_thermal_compensation(values, ambient=23.5):
    return [v + round(math.cos(ambient) * 2) for v in values]

# Real processing begins: extract high-confidence readings
high_confidence_indices = []
for idx, val in enumerate(data_stream):
    if val > 30 and val != 255:  # exclude max outlier
        high_confidence_indices.append(idx)

# Misleading intermediate: partial transform (only referenced once, then ignored)
partial_transform = [data_stream[i] >> 2 for i in high_confidence_indices]
decay_sequence = [int(100 / (i + 1)) for i in range(5)]  # unused decay model

# Core logic: filter and calibrate relevant sensor values
filtered_data = []
for i, value in enumerate(data_stream):
    if i in high_confidence_indices:
        calibrated = value + calibration_map.get(i % 10, 0) + offset_correction
        if calibrated > 0:
            filtered_data.append(int(calibrated))

# Dead code path: simulation of redundant sensor fusion (unreachable)
"""
for reading in filtered_data:
    fused = reading * 1.1 + noise_floor // 10
    break  # early exit never reached due to string block
"""

# Auxiliary transformation: bit manipulation and scaling
scaled_bits = []
for val in filtered_data:
    temp = (val << 1) ^ 0b1010  # shift and XOR mask
    if temp & 0b1000:  # check if 4th bit set
        temp -= 8
    scaled_bits.append(temp % 100)

# Conditional reduction with zip and enumerate (required Python features)
accumulated = 0
for i, (a, b) in enumerate(zip(scaled_bits, scaled_bits[1:])):
    if i % 2 == 0:
        accumulated += a ^ b
    else:
        accumulated -= a & b

# Secondary decoy: string-based status encoding (irrelevant to final result)
status_flags = ['OK', 'ERR', 'WARN']
flag_summary = ''.join([f'{s[0]}' for s in status_flags])  # 'OEW'
annotation_log = f'Status:{flag_summary}|Code:{noise_floor}'

# Critical function: processes cleaned sensor data into diagnostic score
def process_readings(readings):
    base_score = 0
    for j, val in enumerate(readings):
        if j == 0:
            base_score += val * 2
        elif j % 2 == 0:
            base_score += int(math.sqrt(val)) * 3
        else:
            base_score += val // 4
    # Apply non-linear correction based on accumulated bit metric
    correction = int(math.log(accumulated + 10, 1.5))  # avoid log(0)
    return base_score - correction

# Final computation point — target of evaluation
final_diagnostic = process_readings(filtered_data)

# Output result as required
print(f"Target result: {final_diagnostic}")