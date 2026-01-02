from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and irrelevant tags
data_stream = [
    {'value': 144, 'type': 'temp', 'sensor_id': 'A7', 'status': 'ok', 'meta': {'x': 3}},
    {'value': 25, 'type': 'pressure', 'sensor_id': 'B2', 'status': 'ok'},
    {'value': -16, 'type': 'temp', 'sensor_id': 'A7', 'status': 'error'},
    {'value': 81, 'type': 'flow', 'sensor_id': 'C1', 'status': 'ok'},
    {'value': 0, 'type': 'temp', 'sensor_id': 'A7', 'status': 'ok'}
]

# Irrelevant statistical tracker (distractor)
class StatsTracker:
    def __init__(self):
        self.count = 0
        self.total = 0
    
    def update(self, x):
        self.count += 1
        self.total += x

# Unused helper (dead code path)
def analyze_trend(sequence):
    if len(sequence) < 3:
        return 'unstable'
    slope = (sequence[-1] - sequence[0]) / max(len(sequence) - 1, 1)
    return 'rising' if slope > 0 else 'falling' if slope < 0 else 'flat'

# Misleading transformation chain
def transform_value(x, mode='legacy'):
    if mode == 'legacy':
        return (x // 4) + 2
    elif mode == 'modern':
        return int(math.sqrt(abs(x)))
    else:
        return x % 17

# Decoy accumulator with red herring logic
def accumulate_noise(data_list):
    accumulator = defaultdict(int)
    noise_floor = 0.5
    for item in data_list:
        raw_val = item['value']
        # Complex but unused transformation
        transformed = math.log(abs(raw_val) + 1) * 3.7
        category = item.get('type', 'unknown')
        accumulator[category] += round(transformed, 2)
    return dict(accumulator)  # Computed but not used

# Real processing pipeline
valid_temp_values = []
error_count = 0
sensor_readings = Counter()

for entry in data_stream:
    val = entry['value']
    sensor_id = entry['sensor_id']
    status = entry['status']
    s_type = entry['type']
    
    # Track all sensor activity
    sensor_readings[sensor_id] += 1
    
    # Only process temperature readings with 'ok' status
    if s_type == 'temp' and status == 'ok' and val >= 0:
        # Apply integer division and rounding
        processed = int((val ** 0.5) // 1)  # Square root then floor divide by 1
        valid_temp_values.append(processed)
    elif status == 'error':
        error_count += 1

# Secondary filter: only keep values that pass bit condition
filtered_candidates = []
for v in valid_temp_values:
    # Bit manipulation test: check if even number of 1s in binary (even parity)
    if bin(v).count('1') % 2 == 0:
        filtered_candidates.append(v)

# Aggregate using modular arithmetic
aggregate = 0
for i, v in enumerate(filtered_candidates):
    weight = (i + 1) * 3
    aggregate += (v * weight) % 19

# Combine with counter metadata (cross-reference)
bonus = 0
if sensor_readings['A7'] > 2:
    bonus = len([x for x in valid_temp_values if x > 5])

# Final computation involving logical operations
is_stable = error_count == 0
has_data = len(valid_temp_values) > 0
requires_calibration = not is_stable or (has_data and aggregate < 10)

intermediate_result = aggregate + bonus

# Critical statement
final_output = None
if is_stable or not requires_calibration:
    shift_factor = 2 if has_data else 1
    adjusted = intermediate_result << shift_factor  # Left shift by 2
    normalized = adjusted / 4.0
    final_output = int(normalized) + 5
else:
    final_output = -1

# Distractor: complex unused pipeline
def process_advanced(stream):
    results = []
    for item in stream:
        x = item['value']
        c = Counter(str(x))
        results.append(sum(k * v for k, v in c.items()))
    return sum(results)

# Another decoy function with misleading name
def compute_thermal_load(data):
    total = 0
    for d in data:
        if d['type'] == 'temp':
            total += abs(d['value']) ** 0.5
    return round(total, 3)

# Unused accumulator call (red herring)
accumulate_noise(data_stream)

# The real execution point
final_output = process_pipeline(data_stream)

def process_pipeline(stream):
    local_vals = []
    for item in stream:
        if item['type'] == 'temp' and item['status'] == 'ok' and item['value'] >= 0:
            root = int(item['value'] ** 0.5)
            if bin(root).count('1') % 2 == 0:  # Even parity
                local_vals.append(root)
    base_sum = sum((i+1)*3 * v % 19 for i, v in enumerate(local_vals))
    b = len([x for x in local_vals if x > 5])
    temp_sensor_count = Counter(d['sensor_id'] for d in stream if d['type'] == 'temp')
    extra = len(local_vals) if temp_sensor_count.get('A7', 0) > 2 else 0
    mid = base_sum + b + extra
    return (mid << 2) // 4 + 5

# Print result
print(f"Target result: {final_output}")