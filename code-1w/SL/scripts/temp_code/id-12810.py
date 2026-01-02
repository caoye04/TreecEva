import itertools

# Simulated sensor data stream with noise and metadata
data_stream = [
    {'id': 101, 'val': 5.4, 'type': 'temp', 'active': True},
    {'id': 102, 'val': 3.2, 'type': 'pressure', 'active': True},
    {'id': 103, 'val': 7.8, 'type': 'temp', 'active': False},
    {'id': 104, 'val': 6.1, 'type': 'flow', 'active': True},
    {'id': 105, 'val': 4.9, 'type': 'temp', 'active': True},
    {'id': 106, 'val': 8.3, 'type': 'pressure', 'active': True},
    {'id': 107, 'val': 2.7, 'type': 'flow', 'active': True},
    {'id': 108, 'val': 6.6, 'type': 'temp', 'active': True}
]

# Irrelevant baseline calibration map (distractor)
calibration_map = {t: (i * 0.3) for i, t in enumerate(['A', 'B', 'C', 'D'])}

# Thresholds by type — relevant for filtering
threshold_map = {
    'temp': 5.0,
    'pressure': 6.5,
    'flow': 5.5
}

# Decoy transformation using lambda and itertools (unused path)
decoy_pairs = list(itertools.combinations([x['val'] for x in data_stream if x['type'] == 'temp'], 2))
processed_decoy = list(map(lambda pair: abs(pair[0] - pair[1]), decoy_pairs))
avg_decoy = sum(processed_decoy) / len(processed_decoy) if processed_decoy else 0

# Misleading intermediate aggregation (dead code)
false_aggregation = {}
for entry in data_stream:
    key = entry['type']
    if key not in false_aggregation:
        false_aggregation[key] = []
    false_aggregation[key].append(entry['val'] * 0.1)  # scaled meaninglessly

# Real processing begins: extract active entries
effective_data = [e for e in data_stream if e['active']]

# Extract indices and values using enumerate (relevant)
indexed_values = [(i, e['val']) for i, e in enumerate(effective_data)]

# Filter by threshold per type — key logic step
filtered_data = []
for item in effective_data:
    t = item['type']
    v = item['val']
    if t in threshold_map and v >= threshold_map[t]:
        filtered_data.append(v)

# Another distraction: zipping unrelated sequences
dummy_ids = [d['id'] for d in data_stream]
dummy_vals = [d['val'] for d in data_stream]
mapped_deltas = [abs(a - b) for a, b in zip(dummy_ids, [x * 10 for x in dummy_vals])]
mean_delta = sum(mapped_deltas) / len(mapped_deltas)

# Core processing function with nested logic
def process_signals(values, thresholds):
    if not values:
        return -1
    
    # Simulate signal weighting
    weights = [0.8 ** i for i in range(len(values))]
    weighted_sum = sum(val * w for val, w in zip(values, weights))
    
    # Apply decay factor based on count
    decay_factor = 1 / (1 + len(values))
    
    # Hidden offset from unused calibration (red herring)
    hidden_offset = sum(calibration_map.values())  # This looks important but isn't
    
    # Actual computation ignores hidden_offset
    result = weighted_sum * decay_factor * 100
    
    # Extra distraction: unused recursive helper
    def _recursive_normalize(data):
        if len(data) <= 1:
            return data[0] if data else 0
        return _recursive_normalize(data[:-1]) + data[-1] * 0.5
    
    return int(result)  # deterministic integer output

# Critical execution point
final_output = process_signals(filtered_data, threshold_map)

# Output result
print(f"Result: {final_output}")