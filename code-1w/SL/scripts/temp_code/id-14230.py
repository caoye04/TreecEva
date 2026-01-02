import itertools

# Simulated sensor array data with noise and redundancy
data_stream = [18, 22, 19, 25, 24, 20, 21, 17, 23, 26]
noise_floor = [3, -1, 2, 0, -2, 1, 0, -3, 1, 2]
calibration_map = {i: val * 0.95 for i, val in enumerate(data_stream)}

# Irrelevant pre-processing: signal smoothing (unused later)
smoothed = []
for i in range(len(data_stream)):
    if i == 0:
        smoothed.append(data_stream[i])
    else:
        smoothed.append(0.7 * data_stream[i] + 0.3 * smoothed[-1])

# Distractor: Frequency domain transformation (dead end)
frequency_components = []
for k in range(5):
    comp = 0
    for n, x in enumerate(data_stream):
        comp += x * (k * n % 7)  # Arbitrary phase
    frequency_components.append(comp % 100)

# Real processing begins: filter valid readings above dynamic threshold
baseline = sum(data_stream) / len(data_stream)
valid_indices = [i for i, x in enumerate(data_stream) if x > baseline + noise_floor[i]]
filtered_readings = [data_stream[i] for i in valid_indices]

# Apply calibration only to valid sensors
calibrated_readings = [calibration_map[i] for i in valid_indices]

# Compute entropy-like complexity measure (distractor)
from math import log2
if filtered_readings:
    probs = [x / sum(filtered_readings) for x in filtered_readings]
    entropy = -sum(p * log2(p) for p in probs if p > 0)
else:
    entropy = 0

# String-based identifier generation (partially relevant)
sensor_ids = ['S1A', 'S2B', 'S3C', 'S4D', 'S5E', 'S6F', 'S7G', 'S8H', 'S9I', 'S10J']
active_sensors = [sensor_ids[i][:2] for i in valid_indices]  # Use only first two chars

# Generate all possible two-sensor pairs for interference analysis
interference_pairs = list(itertools.combinations(active_sensors, 2))
interference_score = 0
for a, b in interference_pairs:
    interference_score += ord(a[1]) ^ ord(b[1])  # XOR of second characters

# Real path: compute amplitude-weighted temporal shift
weighted_sum = 0
temporal_weight = 0
for idx, i in enumerate(valid_indices):
    weighted_sum += data_stream[i] * (i + 1)
    temporal_weight += i + 1

aggregate_score = weighted_sum / temporal_weight if temporal_weight else 0

# Secondary adjustment based on string pattern count
pattern_count = sum(1 for sid in active_sensors if sid.endswith('1') or sid.endswith('2'))
correction_factor = pattern_count * 1.5

# Critical assignment — target execution point
final_diagnostic = aggregate_score + correction_factor

# Dead code path: unused optimization
optimized_map = {}
for k, v in calibration_map.items():
    if v > 20:
        optimized_map[k] = v * 0.9

# Unused complex transformation chain
transform_chain = (
    lambda x: x ** 0.5,
    lambda x: x * 1.1,
    lambda x: round(x, 1)
)
fake_result = calibrated_readings[:]
for op in transform_chain:
    fake_result = [op(y) for y in fake_result]

# Output the target result
print(f"Result: {final_diagnostic}")