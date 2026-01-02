import itertools

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 1, 'val': 85, 'type': 'A', 'meta': 'x1'},
    {'id': 2, 'val': 90, 'type': 'B', 'meta': 'x2'},
    {'id': 3, 'val': 78, 'type': 'A', 'meta': 'x3'},
    {'id': 4, 'val': 92, 'type': 'C', 'meta': 'x4'},
    {'id': 5, 'val': 88, 'type': 'A', 'meta': 'x5'},
    {'id': 6, 'val': 76, 'type': 'B', 'meta': 'x6'},
    {'id': 7, 'val': 83, 'type': 'A', 'meta': 'x7'},
]

# Irrelevant transformation map for unused feature expansion
expansion_map = {
    'A': lambda x: x * 1.1,
    'B': lambda x: x + 5,
    'C': lambda x: x ** 0.5 * 10
}

# Dead code path: never invoked but looks relevant
def legacy_transform(data):
    return [d['val'] * 0.9 for d in data if d['type'] in ['A', 'B']]

# Unused helper with misleading name
calculate_bias = lambda vals: sum(vals) / len(vals) if vals else 0

# Redundant preprocessing step that computes but doesn't use stats
mean_val = sum(item['val'] for item in data_stream) / len(data_stream)
std_dev = (sum((item['val'] - mean_val)**2 for item in data_stream) / len(data_stream))**0.5
normalized_data = [(item['val'] - mean_val) / std_dev for item in data_stream]

# Distractor: complex filtering using itertools that is not used
grouped_by_type = {k: list(g) for k, g in itertools.groupby(sorted(data_stream, key=lambda x: x['type']), key=lambda x: x['type'])}
expanded_values = []
for entry in data_stream:
    if entry['type'] == 'A':
        expanded_values.append(expansion_map['A'](entry['val']))
    elif entry['type'] == 'B':
        expanded_values.append(expansion_map['B'](entry['val']))
    else:
        expanded_values.append(entry['val'])

# Actual relevant logic begins here
valid_ids = [item['id'] for item in data_stream if item['val'] > 80]
filtered_data = [item['val'] for item in data_stream if item['id'] in valid_ids and item['type'] != 'C']

# Threshold function based on conditional expression
threshold_func = lambda x: True if x > 85 else False

# Another irrelevant accumulator
rolling_sum = 0
history = []
for v in filtered_data:
    rolling_sum += v
    history.append(rolling_sum)

# Core processing function with embedded logic
process_signals = lambda data, thresh: sum(1 for val in data if thresh(val)) * min(data) // max(data) if data else 0

# Key assignment - this is where the answer is determined
final_output = process_signals(filtered_data, threshold_func)

# Final print statement to expose result
print(f"Result: {final_output}")