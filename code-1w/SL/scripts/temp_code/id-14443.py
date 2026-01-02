from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion (irrelevant in part)
sensor_feeds = {
    'temp': [23.5, 24.1, 22.7, 25.0, 26.3],
    'pressure': [1013, 1011, 1015, 1009, 1018],
    'humidity': [45, 47, 50, 52, 49]
}

# Irrelevant baseline calibration map
baseline_calibrations = defaultdict(lambda: 1.0)
for k in sensor_feeds:
    baseline_calibrations[k] = sum(sensor_feeds[k]) / len(sensor_feeds[k])

# System state vectors with red herring transformations
raw_signal = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]
filtered_signal = [x for x in raw_signal if x > 0.5]  # Decoy filtering
extended_profile = filtered_signal[::2] + [x * 0.1 for x in range(8)]  # Unused extended data

# Core diagnostic parameters
health_signature = [
    int(math.sin(math.pi * i / 4) * 100) for i in range(8)
]
system_load = [i ** 2 % 79 for i in range(1, 9)]

# Misleading entropy calculation (dead path)
entropy_vector = [math.log(x) if x > 0 else 0 for x in system_load]
entropy_sum = sum(entropy_vector)  # Not used later

# Auxiliary transformation matrix (partially relevant)
transform_matrix = []
for i in range(8):
    row = []
    for j in range(8):
        val = (health_signature[i] ^ system_load[j]) & 0x7F
        if j % 2 == 0:
            val = abs(val - 50)
        row.append(val)
    transform_matrix.append(row)

# Secondary decoy: frequency analysis on unused signal
signal_counter = Counter([int(x * 10) for x in extended_profile])
frequency_bias = sum(signal_counter.values()) / len(signal_counter)  # Distractor

# Key intermediate: cross-correlation slice
correlation_slice = []
for i in range(8):
    acc = 0
    for j in range(8):
        acc += transform_matrix[i][j] * ((i + j) % 3 + 1)
    correlation_slice.append(acc % 1000)

# Dummy control flow with misleading branch
adjustment_factor = 1
if sum(correlation_slice) > 5000:
    adjustment_factor = 0.9
elif sum(correlation_slice) < 3000:
    adjustment_factor = 1.1  # This block does not trigger
else:
    adjustment_factor = 1.0  # Actual path, but factor unused

# Critical data refinement using slicing and masking
refined_diagnostics = correlation_slice[1:7:2]  # Take indices 1,3,5
mask = [0x55, 0xAA, 0xF0]  # Bit manipulation pattern
masked_values = []
for i, val in enumerate(refined_diagnostics):
    masked_val = (val ^ mask[i % 3]) & 0xFF
    masked_values.append(masked_val)

# Final computation chain
aggregated_metric = 0
for v in masked_values:
    aggregated_metric += (v * (v + 5)) // 17

# Secondary metric from health signature (case conversion as red herring)
status_flags = ['OK', 'WARN', 'ERROR']
case_shifted = [flag.lower() for flag in status_flags]  # Irrelevant

# Real final processing
def process_metrics(hs, sl):
    base = sum(hs[i] * sl[i] for i in range(len(hs)))
    offset = 0
    for i in range(0, len(hs), 2):
        offset += math.ceil(math.sin(hs[i] * 0.01) * 10)
    return (base + offset) % 99997

final_diagnostic = process_metrics(health_signature, system_load)
print(f"Result: {final_diagnostic}")