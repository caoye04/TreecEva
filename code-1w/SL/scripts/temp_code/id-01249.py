from collections import defaultdict, Counter
from itertools import zip_longest, cycle

# Simulated sensor data stream with noise and metadata
data_stream = [
    {'id': 101, 'values': [3, 5, 7, None], 'type': 'A', 'active': True},
    {'id': 102, 'values': [2, 4, 6, 8], 'type': 'B', 'active': False},
    {'id': 103, 'values': [1, None, 5, 9], 'type': 'A', 'active': True},
    {'id': 104, 'values': [7, 7, 7], 'type': 'C', 'active': True}
]

# Irrelevant lookup table - decoy for type mappings (not used in final logic)
type_map = defaultdict(lambda: 'UNKNOWN')
type_map['A'] = 'Alpha'
type_map['B'] = 'Beta'
type_map['C'] = 'Gamma'

# Misleading statistical summary (dead computation path)
value_counter = Counter()
for entry in data_stream:
    for v in entry['values']:
        if v is not None:
            value_counter[v] += 1

# Unused transformation function - red herring
def legacy_normalize(data):
    return [x / max(data) if max(data) != 0 else 0 for x in data]

# Distractor: fake temporal smoothing (never invoked)
current_cycle = cycle([0.1, 0.2, 0.3])
temporal_buffer = []
for _ in range(5):
    temporal_buffer.append(next(current_cycle))

# Core processing begins here -------------------------

def clean_and_impute(entry_list):
    cleaned = []
    for entry in entry_list:
        # Only process active sensors
        if entry['active']:
            values = entry['values']
            mean_val = sum(v for v in values if v is not None) / len([v for v in values if v is not None])
            imputed = [v if v is not None else mean_val for v in values]
            cleaned.append({'id': entry['id'], 'imputed_values': imputed, 'type': entry['type']})
    return cleaned

def transform_entry(data_block):
    result_block = []
    for item in data_block:
        arr = item['imputed_values']
        # Apply non-linear transformation: square then log + 1
        transformed = [round((x ** 2 + 1) ** 0.5, 4) for x in arr]
        # Add checksum as last element (used later)
        checksum = sum(int(t * 100) for t in transformed) % 100
        transformed.append(checksum)
        result_block.append({
            'id': item['id'],
            'transformed_seq': transformed,
            'meta': f"TR-{item['type']}"
        })
    return result_block

# Weight configuration (some are misleading)
weights = {
    'base': [0.25, 0.25, 0.25, 0.25],  # Equal weights
    'bonus': [0.1, 0.1, 0.1],           # Unused bonus tier
    'penalty': 0.9                     # Not directly applied
}

# Secondary distractor: unused recursive function
def calculate_depth(obj):
    if isinstance(obj, dict) and 'children' in obj:
        return 1 + max(calculate_depth(child) for child in obj.get('children', []) or [{}])
    return 1

# Actual pipeline execution
filtered_data = clean_and_impute(data_stream)
transformed_data = transform_entry(filtered_data)

# Fake aggregation path - looks important but unused
dummy_aggregate = defaultdict(float)
for td in transformed_data:
    key = td['meta']
    dummy_aggregate[key] += sum(td['transformed_seq'])

# Real scoring logic
checksum_total = 0
valid_count = 0
for record in transformed_data:
    seq = record['transformed_seq']
    if len(seq) > 4:  # Only those with appended checksum
        weight_slice = weights['base'][:len(seq)-1]  # Trim weights to match length
        weighted_sum = sum(val * w for val, w in zip(seq[:-1], weight_slice))
        checksum_total += weighted_sum * 1000  # Scale up for precision
        valid_count += 1

intermediate_result = int(checksum_total // valid_count) if valid_count else 0

# Final nonlinear adjustment based on id parity pattern
id_parity = sum(1 for d in transformed_data if d['id'] % 2 == 1)
final_score = intermediate_result + (id_parity * 1007)

# Decoy print statements (not part of output)
# print(f'Debug: {dummy_aggregate}')
# print(f'Tracing: {value_counter}')

print(f"Result: {final_score}")