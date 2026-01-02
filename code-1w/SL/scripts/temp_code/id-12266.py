from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and irrelevant fields
data_packet = [
    {'type': 'temp', 'value': 25.3, 'status': 'ok', 'seq': 1},
    {'type': 'pressure', 'value': 1013.25, 'status': 'ok', 'seq': 2},
    {'type': 'temp', 'value': -999, 'status': 'err', 'seq': 3},
    {'type': 'humidity', 'value': 45.0, 'status': 'ok', 'seq': 4},
    {'type': 'temp', 'value': 27.8, 'status': 'ok', 'seq': 5},
    {'type': 'pressure', 'value': 1012.1, 'status': 'ok', 'seq': 6},
]

# Irrelevant baseline metrics (distractor)
baseline_metrics = {
    'avg_temp': 22.0,
    'tolerance': 3.5,
    'calibration': [0.98, 1.02, 0.99],
    'version': '2.1'
}

# Misleading transformation chain (dead path)
def legacy_calibrate(data):
    return [x * 1.05 for x in data if x > 0]  # Unused function

# Decoy processing that looks important but isn't used
class DataNormalizer:
    def __init__(self, factor=1.0):
        self.factor = factor

    def normalize(self, val):
        return val * self.factor + 10  # Never instantiated

# Real processing begins here
valid_temps = [
    p['value'] for p in data_packet 
    if p['type'] == 'temp' and p['status'] == 'ok' and p['value'] > -100
]

# Complex conditional expression with red herring logic
adjusted_temps = [
    t * 1.1 if t < 26 else t * 0.95 for t in valid_temps
]

# Bit manipulation decoy (irrelevant to final result)
checksum = 0
for t in valid_temps:
    checksum ^= int(t) & 0xFF

# Another distractor: unused statistical analysis
stats_summary = Counter()
for p in data_packet:
    stats_summary[p['type']] += 1

# Configuration with misleading keys
config = {
    'mode': 'aggressive',
    'threshold': 26.0,
    'scale_factor': 2.0,  # This will be used
    'debug_trace': True,
    'max_iterations': 999  # Red herring
}

# Transform data using multiple concepts
transformed_data = defaultdict(float)
for i, temp in enumerate(adjusted_temps):
    key = f'entry_{i}'
    transformed_data[key] = round(
        (temp ** 0.5) * config['scale_factor'], 3
    )

# Lambda-based filtering (some filtered out)
filter_func = lambda x: x > 8.0
filtered_entries = {
    k: v for k, v in transformed_data.items() if filter_func(v)
}

# Core logic hidden among distractions
intermediate_sum = sum(filtered_entries.values())

# Dead code path: looks recursive but unused
def recursive_boost(val, depth=0):
    if depth <= 0:
        return val
    return recursive_boost(val * 1.1, depth - 1)

# Actual critical computation
base_accum = 0
for val in filtered_entries.values():
    if val > 9.0:
        base_accum += math.log(val) * 10
    else:
        base_accum += val / 2

# Final transformation with conditional expression
final_output = 0
if len(filtered_entries) >= 2:
    adjustment = 50 if checksum > 100 else 25  # checksum is low -> 25
    final_output = int(base_accum + adjustment)
else:
    final_output = -999  # dead branch

# Additional distraction: unused nested structure
nested_map = [[[[{'dummy': 0}]]] for _ in range(2)]

# Output the target variable
print(f"Result: {final_output}")