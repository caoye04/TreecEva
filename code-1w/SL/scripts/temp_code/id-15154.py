from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant readings
data_stream = [
    {'id': 'A7', 'val': 3.2, 'type': 'temp', 'seq': 1},
    {'id': 'B4', 'val': 1.8, 'type': 'humid', 'seq': 2},
    {'id': 'A7', 'val': 3.4, 'type': 'temp', 'seq': 3},
    {'id': 'C9', 'val': 2.1, 'type': 'pressure', 'seq': 4},
    {'id': 'B4', 'val': 1.9, 'type': 'humid', 'seq': 5},
    {'id': 'A7', 'val': 3.3, 'type': 'temp', 'seq': 6},
]

# Irrelevant backup data (distractor)
backup_data = [dict(d) for d in data_stream[::-1]]

# Mapping sensor types to processing functions (unused entries are red herrings)
type_handlers = {
    'temp': lambda x: x ** 2,
    'humid': lambda x: x * 1.8 + 32,
    'pressure': lambda x: x * 100,
    'flow': lambda x: abs(x - 0.5),
    'vibration': lambda x: x / 2
}

# Weights for final aggregation (some are misleading)
weights = {
    'temp': 0.4,
    'humid': 0.3,
    'pressure': 0.3,
    'light': 0.1,  # unused
    'co2': 0.05   # unused
}

# Decoy transformation matrix (never used)
transform_matrix = [[i*j for j in range(5)] for i in range(5)]

# Aggregate raw values by sensor ID and type
devices = defaultdict(list)
for entry in data_stream:
    devices[entry['id']].append(entry)

total_entries = sum(len(logs) for logs in devices.values())

# Compute rolling averages per device (some intermediate results)
avg_per_device = {}
for dev_id, records in devices.items():
    vals = [r['val'] for r in records]
    avg_per_device[dev_id] = sum(vals) / len(vals)

# Group by type instead (this is what matters)
type_values = defaultdict(list)
for entry in data_stream:
    raw_val = entry['val']
    if entry['type'] in type_handlers:
        processed = type_handlers[entry['type']](raw_val)
        type_values[entry['type']].append(processed)

# Misleading normalization pass (not actually used in final logic)
normalized_types = {}
for t, vals in type_values.items():
    mean_val = sum(vals) / len(vals)
    normalized_types[t] = [v / mean_val for v in vals]

# Another distraction: character encoding simulation
token_key = "SensorFusion2024"
shifted = ''.join(chr((ord(c) - ord('A') + 3) % 26 + ord('A')) if c.isalpha() else c for c in token_key.upper())

# Real computation begins: use only latest reading per type for scoring
latest_per_type = {}
for entry in reversed(data_stream):
    t = entry['type']
    if t not in latest_per_type:
        latest_per_type[t] = entry['val']

# Apply transformations to latest values
transformed_latest = {}
for t, val in latest_per_type.items():
    if t in type_handlers:
        transformed_latest[t] = type_handlers[t](val)

# Calculate composite index using weights
composite_index = 0.0
weight_sum = 0.0
for t, score in transformed_latest.items():
    if t in weights:
        composite_index += score * weights[t]
        weight_sum += weights[t]

# Normalize by total active weight
if weight_sum > 0:
    composite_index /= weight_sum

# Additional validation layer (dead code path - never triggered under current input)
status_flags = Counter()
for entry in data_stream:
    flag = 'critical' if entry['val'] > 3.0 else 'normal'
    status_flags[flag] += 1

# Final processing function
def process_results(log, w):
    # Extract unique types present
    present_types = {e['type'] for e in log if e['type'] in w and w[e['type']] > 0}
    
    # Spurious string analysis (distractor)
    type_names = ','.join(sorted(present_types))
    magic_offset = sum(ord(c) for c in type_names if c in 'AEIOU') - len(type_names)
    
    # Actual relevant logic: recompute transformed latest from log
    latest = {}
    for e in reversed(log):
        if e['type'] not in latest:
            raw = e['val']
            # Only apply handler if type exists
            if e['type'] in type_handlers:
                latest[e['type']] = type_handlers[e['type']](raw)
    
    # Weighted average
    total_weight = sum(w[t] for t in latest if t in w)
    if total_weight == 0:
        return 0.0
    
    weighted_sum = sum(latest[t] * w[t] for t in latest if t in w)
    base_result = weighted_sum / total_weight
    
    # Final adjustment: add length of active types string (minor but deterministic)
    adjustment = len(type_names.replace(',', '')) * 0.01
    return base_result + adjustment

# Execute main computation
final_score = process_results(data_stream, weights)

# Print result as required
print(f"Target result: {final_score}")