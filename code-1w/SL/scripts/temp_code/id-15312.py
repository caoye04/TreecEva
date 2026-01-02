from collections import defaultdict, Counter
import math

# Simulated sensor data stream with noise and metadata
data_stream = [
    {'id': 101, 'value': 3.5, 'type': 'temp', 'status': 'active'},
    {'id': 102, 'value': -2.1, 'type': 'temp', 'status': 'active'},
    {'id': 103, 'value': 7.8, 'type': 'pressure', 'status': 'active'},
    {'id': 104, 'value': 0.0, 'type': 'temp', 'status': 'inactive'},
    {'id': 105, 'value': 5.2, 'type': 'temp', 'status': 'active'},
    {'id': 106, 'value': -1.3, 'type': 'temp', 'status': 'active'},
]

# Irrelevant statistical counters (distractors)
extreme_count = 0
null_entries = 0
rolling_avg = 0.0
snapshot_log = []

# Decoy transformation function (never called)
def transform_legacy(data):
    return [x * 1.8 + 32 for x in data if x > -100]

# Auxiliary filtering logic with red herring conditions
def is_valid_reading(entry):
    global null_entries
    if entry['value'] == 0.0:
        null_entries += 1
        return False
    if entry['status'] != 'active':
        return False
    # Misleading threshold
    if abs(entry['value']) > 10:
        global extreme_count
        extreme_count += 1
        return False
    return True

# Secondary processing with irrelevant aggregation
def aggregate_by_type(data_list):
    aggregates = defaultdict(list)
    type_count = Counter()
    for item in data_list:
        aggregates[item['type']].append(item['value'])
        type_count[item['type']] += 1
    # Dead computation path
    normalized = {}
    for t, vals in aggregates.items():
        mean = sum(vals) / len(vals)
        normalized[t] = [v - mean for v in vals]  # Never used
    return aggregates  # Not actually used in final flow

# Core signal extraction with conditional logic and distraction
valid_values = []
for record in data_stream:
    if record['type'] == 'temp' and is_valid_reading(record):
        adjusted = abs(record['value']) ** 0.5  # Non-linear transformation
        if adjusted > 1.0:
            valid_values.append(adjusted)

# Fake smoothing filter (unused)
if len(valid_values) > 3:
    smoothed = [sum(valid_values[i:i+3]) / 3 for i in range(len(valid_values) - 2)]
else:
    smoothed = valid_values[:]

# Complex pipeline combining arithmetic, logic, and data ops
def process_pipeline(raw_data):
    temp_vals = [
        abs(d['value']) ** 0.5 for d in raw_data 
        if d['type'] == 'temp' and d['status'] == 'active' and d['value'] != 0.0
    ]
    
    # Bitwise interference (red herring)
    magic_seed = 0
    for v in temp_vals:
        magic_seed ^= int(v * 100) & 0xFF
    
    # Conditional expression chain with fallbacks
    base_score = sum(temp_vals) if temp_vals else 0.0
    penalty = len([v for v in temp_vals if v < 0.5]) * 0.1
    adjusted_score = base_score - penalty if base_score > 0 else 0.0
    
    # Final nonlinear scaling with trigonometric decoy
    cos_factor = math.cos(len(temp_vals) * math.pi / 4) if len(temp_vals) % 2 == 0 else 0.5
    # BUT: actual formula ignores cos_factor — deliberate misdirection
    result = (adjusted_score * 1000) // 1  # Floor to integer scale
    
    # Additional distraction: update rolling average (irrelevant)
    global rolling_avg
    if len(temp_vals) > 0:
        rolling_avg = sum(temp_vals) / len(temp_vals)
    
    return int(result)

# Execute main logic
temp_snapshot = [d for d in data_stream if d['type'] == 'temp']  # Unused branch
dead_aggregate = aggregate_by_type(data_stream)  # Side effect with no use

# Critical execution point
final_output = process_pipeline(data_stream)

# Logging remnants (distraction)
snapshot_log.append((len(data_stream), final_output))

print(f"Result: {final_output}")