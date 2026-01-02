from itertools import compress, count

# Simulated sensor data stream with metadata
data_stream = [
    (102, 'temp', True), (205, 'pressure', False), (308, 'temp', True),
    (411, 'humidity', True), (514, 'temp', False), (617, 'pressure', True),
    (720, 'temp', True), (823, 'humidity', False)
]

# Irrelevant transformation: reverse mapping for unused diagnostic mode
diag_map = {v: k for k, v, _ in data_stream}
reverse_lookup = [diag_map.get(i * 100) for i in range(1, 9)]

# Extract components
timestamps = list(count(1000, step=3))  # Simulated timestamps (unused in logic)
values, types, statuses = zip(*data_stream)

# Distractor: complex filtering using irrelevant criteria
status_filter = [s and v % 2 == 1 for v, s in zip(values, statuses)]
type_mask = [t == 'temp' or t == 'pressure' for t in types]
primary_filter = [a and b for a, b in zip(status_filter, type_mask)]

# Another red herring: attempt to correlate with timestamp parity (not actually used)
timestamp_parities = [t % 2 for t in timestamps[:len(data_stream)]]
parity_influence = sum(1 for p in timestamp_parities if p == 1)

# Real logic begins: identify entries where type is 'temp' AND status is True
is_temp = [entry[1] == 'temp' for entry in data_stream]
effective_status = [entry[2] for entry in data_stream]
valid_entries_mask = [is_temp[i] and effective_status[i] for i in range(len(data_stream))]

# Use enumerate to find indices of valid temperature readings (distractor usage)
valid_indices = [i for i, valid in enumerate(valid_entries_mask) if valid]
index_offset = sum(valid_indices) % 4  # Unused offset

# Extract actual values where mask is True
valid_values = [values[i] for i in range(len(values)) if valid_entries_mask[i]]

# Critical statement: compute sum of valid temperature readings
filtered_sum = sum(valid_values)

# More distractions: tuple unpacking and unused transformations
aggregated = []
for idx, (val, typ, stat) in enumerate(zip(values, types, statuses)):
    if typ == 'humidity':
        transformed = (val * 1.05) // 1
        aggregated.append((idx, transformed, 'adjusted'))
    elif val > 500:
        aggregated.append((idx, val + 10, 'boosted'))  # Dead code path due to masking above

# Spurious sorting operation on unrelated data
sorted_diag = sorted(diag_map.items(), key=lambda x: x[0] % 3)

# Final red herring: bitwise manipulation on sum components (never executed)
if parity_influence > 5:
    filtered_sum = filtered_sum ^ 0xFF

# Correct result output
print(f"Result: {filtered_sum}")