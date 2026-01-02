from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data streams with noise and calibration offsets
def generate_sensor_stream(base_value, length, noise_factor=0.1):
    return [base_value + i * noise_factor for i in range(length)]

# Irrelevant helper function - dead code path (distractor)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [x / mean_val for x in data]

# Core diagnostic engine
def compute_health_index(readings):
    trend_weights = [0.1, 0.2, 0.3, 0.4]
    weighted_trend = sum(readings[i] * trend_weights[i] for i in range(4))
    
    # Bit manipulation for fault pattern detection
    binary_signature = 0
    for val in readings[:4]:
        shifted = int(abs(val * 10)) & 0xFF
        binary_signature ^= shifted  # Accumulate XOR fingerprint
    
    # Health score calculation (relevant)
    base_score = sum(readings) / len(readings)
    penalty = 0
    for i in range(1, len(readings)):
        if readings[i] < readings[i-1]:
            penalty += 0.5
    
    health_score = base_score - penalty
    return health_score, binary_signature

# Main execution block
sensor_inputs = {
    'thermal': generate_sensor_stream(23.5, 8),
    'pressure': generate_sensor_stream(101.3, 8),
    'vibration': generate_sensor_stream(4.7, 8)
}

# Unused sensor group - red herring
test_sensors = defaultdict(float)
test_sensors['dummy'] = 0.0

# Data alignment using itertools (partially relevant)
streams = [sensor_inputs['thermal'], sensor_inputs['pressure'], sensor_inputs['vibration']]
cyclic_iterators = [cycle(stream) for stream in streams]
aligned_data = [tuple(next(it) for it in cyclic_iterators) for _ in range(5)]

# Extract flat sequence for processing
flattened_readings = [val for row in aligned_data for val in row]

# Statistical summary - mostly irrelevant
data_counter = Counter()
for val in flattened_readings:
    rounded = round(val)
    data_counter[rounded] += 1

# Primary analysis pipeline
aggregate_health_score = 0.0
signature_pool = []

for key, values in sensor_inputs.items():
    score, sig = compute_health_index(values)
    aggregate_health_score += score * 0.33  # Weighted contribution
    signature_pool.append(sig)

# Anomaly detection logic
anomaly_mask = 0
for sig in signature_pool:
    anomaly_mask ^= (sig & 0xFFFF)  # Combine signatures with XOR

# Decoy compensation logic (never used)
baseline_reference = defaultdict(list)
for temp in sensor_inputs['thermal']:
    baseline_reference['history'].append(temp - 0.5)

# Correction factor derived from bit patterns
correction_factor = 0
for i, val in enumerate(flattened_readings[::2]):
    if i % 3 == 0:
        correction_factor += int(val) & 0xF

correction_factor = (correction_factor << 2) & 0xFF  # Shift and mask

# Critical statement: final diagnostic computation
final_diagnostic = aggregate_health_score + (anomaly_mask ^ correction_factor)

# Distractor: unused data transformation
shifted_cyclic = list(islice(cycle([1,2,3]), 10))

# Output the target result
print(f"Result: {final_diagnostic}")