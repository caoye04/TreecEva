from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and redundant readings
data_stream = [
    (1, [3.2, 3.4, 3.3, 3.5, 3.6]),
    (2, [4.1, 4.0, 4.2, 4.1, 4.3]),
    (3, [2.9, 3.0, 2.8, 3.1, 3.0]),
    (4, [5.2, 5.4, 5.3, 5.5, 5.6]),
    (5, [3.8, 3.9, 3.7, 4.0, 3.8])
]

# Irrelevant diagnostic flag (red herring)
system_status_flag = True
error_log = []

# Misleading pre-processing: computes per-sensor average but not used in final result
sensor_averages = {}
for sensor_id, readings in data_stream:
    sensor_averages[sensor_id] = sum(readings) / len(readings)

# Decoy function that appears important but is never called
def compute_health_index(logs):
    return sum([len(log) for log in logs]) * 0.5

# Real processing begins: extract valid signals above threshold
valid_signals = []
threshold = 3.0
for _, readings in data_stream:
    filtered = [r for r in readings if r > threshold]
    valid_signals.extend(filtered)

# Compute statistical profile (only some values are used later)
stats = defaultdict(float)
stats['count'] = len(valid_signals)
stats['total'] = sum(valid_signals)
stats['mean'] = stats['total'] / stats['count']
stats['squared_sum'] = sum(x**2 for x in valid_signals)
stats['variance'] = (stats['squared_sum'] / stats['count']) - (stats['mean'] ** 2)

# Distractor: unused complex transformation
transformed_data = [math.log(x + 1) for x in valid_signals if x > 4.0]
deep_analysis = Counter(transformed_data)

# Bit manipulation decoy - simulates checksum but unused
checksum = 0
for i, val in enumerate(valid_signals):
    checksum ^= int(val * 10) << (i % 4)

# Real computation path starts here
signal_strength = stats['mean'] * stats['count']
noise_ratio = len([x for x in valid_signals if x < 3.5]) / stats['count']

# Key intermediate values
aggregate_score = signal_strength * (1 - noise_ratio)
correction_factor = 1.0 + math.sin(math.pi * noise_ratio)
offset_value = -50  # calibration offset

# Dead code path: looks like it updates correction but doesn't affect flow
if correction_factor > 1.5:
    adjustment_map = {k: v * 0.9 for k, v in sensor_averages.items()}
    offset_value += 10
else:
    baseline_shift = [x - 3.0 for x in valid_signals]

# Final diagnostic calculation - this is where the answer comes from
final_diagnostic = aggregate_score * correction_factor + offset_value

# Print result for evaluation
target_result: {final_diagnostic}