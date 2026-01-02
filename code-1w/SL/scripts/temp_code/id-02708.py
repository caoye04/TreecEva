from collections import defaultdict, Counter
import math

# Simulated sensor data with metadata (some fields are red herrings)
sensor_readings = [
    {'value': 5, 'type': 'alpha', 'status': 'ok', 'timestamp': 1001},
    {'value': 3, 'type': 'beta', 'status': 'error', 'timestamp': 1002},
    {'value': 8, 'type': 'alpha', 'status': 'ok', 'timestamp': 1003},
    {'value': 1, 'type': 'gamma', 'status': 'ok', 'timestamp': 1004},
    {'value': 9, 'type': 'beta', 'status': 'ok', 'timestamp': 1005}
]

# Irrelevant mapping table for hypothetical hardware calibration (distractor)
calibration_map = {
    'sensor_a': lambda x: x * 1.05,
    'sensor_b': lambda x: x + 0.5 if x < 10 else x * 0.95,
    'sensor_c': lambda x: math.sqrt(x) * 2
}

# Decoy function that is never called
def legacy_process(data):
    return [d['value'] * 2 for d in data if d['status'] == 'error']

# Misleading intermediate computation with unused result
temp_aggregate = sum(d['value'] for d in sensor_readings if d['type'] == 'gamma') * 100

# Real processing begins here
valid_entries = [entry for entry in sensor_readings if entry['status'] == 'ok']

# Extract values and count types
values_only = [entry['value'] for entry in valid_entries]
type_counter = Counter(entry['type'] for entry in valid_entries)

# Bit manipulation red herring (shifts and XOR with arbitrary constants)
magic_key = (len(values_only) << 3) ^ 255
checksum = 0
for v in values_only:
    checksum ^= (v * 7 + 11) & 0xFF

# Another decoy variable using string methods on numeric conversion (distraction)
diag_string = f"CHK:{''.join(map(str, sorted(values_only)))}"
encoded_diag = diag_string.replace('0', 'X').split(':')[-1].strip('X')

# Actual signal transformation: map type counts to weights via lambda
weight_func = lambda t, c: c * (3 if t == 'alpha' else 2 if t == 'beta' else 1)
weighted_contributions = [
    weight_func(t, cnt) for t, cnt in type_counter.items()
]

# Secondary transformation: cumulative effect with non-linear scaling
transformed = [
    int(v ** 0.5) if v % 2 == 0 else v + 1 for v in values_only
]

# Aggregation step: combine weighted contributions and transformed means
base_score = sum(weighted_contributions)
adjustment = sum(transformed) / len(transformed) if transformed else 0

# Hidden dependency: use of string method on a number-derived string (subtle but relevant)
dynamic_factor_str = str(int(sum(values_only) * 10))  # e.g., "160" -> has three digits
scaling_impact = len(dynamic_factor_str.strip('0'))  # removes trailing zeros, then counts length

# Core calculation buried among distractions
processed_data = base_score * adjustment / (scaling_impact or 1)

# Final analysis applies additional logic mask using bitwise and comparison ops
mask_filter = (magic_key & 0xF0) > 100  # evaluates to True

# The actual answer computation
final_diagnostic = processed_data if mask_filter else -1

# Extraneous print statements (simulating debug noise)
# print(f'Debug: {temp_aggregate=}')
# print(f'Metadata keys: {[k for k in sensor_readings[0].keys()]}')

# Critical output line — do not modify format
Result: {final_diagnostic}