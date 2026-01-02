from collections import defaultdict, Counter
import math

# Simulated sensor array data with metadata
data_stream = [
    {'id': 'S1', 'val': 84, 'type': 'temp', 'status': 'active'},
    {'id': 'S2', 'val': 17, 'type': 'pressure', 'status': 'active'},
    {'id': 'S3', 'val': 91, 'type': 'temp', 'status': 'active'},
    {'id': 'S4', 'val': 23, 'type': 'humidity', 'status': 'failed'},
    {'id': 'S5', 'val': 87, 'type': 'temp', 'status': 'active'},
    {'id': 'S6', 'val': 12, 'type': 'pressure', 'status': 'active'},
    {'id': 'S7', 'val': 77, 'type': 'temp', 'status': 'active'},
    {'id': 'S8', 'val': 15, 'type': 'pressure', 'status': 'active'},
    {'id': 'S9', 'val': 88, 'type': 'temp', 'status': 'active'}
]

# Irrelevant mapping (distraction)
type_mapping = {'temp': 0, 'pressure': 1, 'humidity': 2, 'flow': 3}
status_weights = defaultdict(lambda: 0.5)
status_weights['active'] = 1.0
status_weights['standby'] = 0.3

# Misleading pre-processing (dead path)
def validate_entry(entry):
    if entry['val'] < 0:
        return False
    if entry['type'] not in ['temp', 'pressure']:
        return False
    return True

# Unused function (decoy)
calculate_bias = lambda x, w: sum(a * b for a, b in zip(x, w)) / len(x) if x else 0

# Distractor: historical averages (not used in final logic)
historical_averages = {
    'temp': [85, 83, 88, 86, 84],
    'pressure': [15, 16, 14, 15, 13],
    'humidity': [20, 22, 21, 19]
}

# Another decoy function (never called in critical path)
def analyze_trend(values):
    if len(values) < 2:
        return 0
    diffs = [values[i] - values[i-1] for i in range(1, len(values))]
    return sum(d for d in diffs if d > 0)

# Real processing begins here
working_sensors = [s for s in data_stream if s['status'] == 'active']

# Filter only temperature sensors
filtered_data = [s for s in working_sensors if s['type'] == 'temp']

# Compute moving average over sliding window of size 2 (irrelevant intermediate)
moving_avgs = []
vals = [d['val'] for d in filtered_data]
for i in range(len(vals) - 1):
    moving_avgs.append((vals[i] + vals[i+1]) / 2)

# Distractor: count distribution (looks important but unused)
dist_count = Counter([d['val'] for d in filtered_data])

# Decoy list comprehension with string operations (red herring)
encoded_ids = [f"{s['id']}_V{s['val']%10}" for s in filtered_data]
valid_encodings = [eid for eid in encoded_ids if eid.endswith('1') or eid.endswith('4')]

# Real logic: compute diagnostic score based on variance and median
sorted_vals = sorted(vals)
n = len(sorted_vals)
median_temp = (sorted_vals[n//2] + sorted_vals[n//2 - 1]) / 2 if n % 2 == 0 else sorted_vals[n//2]

mean_val = sum(vals) / len(vals)
variance = sum((x - mean_val) ** 2 for x in vals) / len(vals)
std_dev = math.sqrt(variance)

# Secondary metric: outlier score based on bitwise analysis (misleading)
bit_outlier_score = 0
for v in vals:
    high_bits = (v >> 4) & 0b1111
    low_bits = v & 0b1111
    bit_outlier_score += (high_bits ^ low_bits) & 0b1010

# Weighted combination using irrelevant status_weights (only one factor matters)
raw_score = 0.0
for s in filtered_data:
    raw_score += s['val'] * status_weights[s['status']]

# Final transformation: use only median and std deviation (others were distractions)
# Apply non-linear compression
if std_dev > 0:
    efficiency_factor = median_temp / (std_dev + 1)
else:
    efficiency_factor = median_temp

# Critical computation hidden among noise
scaling_constant = 17
offset_adjustment = 3

# Core formula disguised in complex expression
intermediate = int(efficiency_factor) ^ scaling_constant
intermediate = intermediate * 2 - offset_adjustment

# Final diagnostic uses modular arithmetic and rounding
final_diagnostic = round((intermediate + len(valid_encodings)) % 97 * math.log(median_temp + 1))

# Print result as required
print(f"Result: {final_diagnostic}")