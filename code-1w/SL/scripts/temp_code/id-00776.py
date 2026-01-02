from collections import defaultdict
import math

# Simulate sensor data chunk with redundant fields
data_chunk = [
    {'id': 'A7', 'raw_val': 23, 'status': 'active', 'meta': 'X'},
    {'id': 'B4', 'raw_val': -15, 'status': 'idle', 'meta': 'Y'},
    {'id': 'C9', 'raw_val': 8, 'status': 'active', 'meta': 'Z'},
    {'id': 'D2', 'raw_val': 0, 'status': 'active', 'meta': 'X'}
]

# Irrelevant aggregation for distraction
dummy_stats = defaultdict(int)
for entry in data_chunk:
    dummy_stats[entry['status']] += 1
    dummy_stats['total'] += abs(entry['raw_val'])

# Transform: filter active, square raw values, apply modulo threshold
cleaned_vals = []
for entry in data_chunk:
    if entry['status'] == 'active':
        processed = (entry['raw_val'] ** 2) % 17
        cleaned_vals.append(processed)

# Secondary transformation: map via lambda with bit manipulation
transformation_key = lambda x: (x ^ 5) + (x & 3)
transformed_chunk = list(map(transformation_key, cleaned_vals))

# Dummy set operation for interference
distinct_temp = set(transformed_chunk)
distinct_temp.add(99)
distinct_temp.discard(99)

# Real processing path begins here
buffer_state = [math.sin(math.pi * x / 6) for x in transformed_chunk if x > 3]
aggregate_phase = sum(buffer_state) * len(transformed_chunk)

# Core logic: count high-frequency signals using shifted XOR pattern
signal_mask = 0
for val in transformed_chunk:
    if val > 10:
        signal_mask ^= val << 1
    elif val > 5:
        signal_mask ^= val

# Final computation
intermediate_score = aggregate_phase + signal_mask
scaling_factor = len(data_chunk) / (dummy_stats['total'] + 1)
final_output = int(intermediate_score * scaling_factor)

# Output result
print(f"Result: {final_output}")