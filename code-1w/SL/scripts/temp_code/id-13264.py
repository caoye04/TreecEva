import itertools

# Simulated sensor array data with metadata
data_stream = [
    {'id': 'S1', 'val': 5.1, 'type': 'temp', 'active': True},
    {'id': 'S2', 'val': 7.3, 'type': 'pressure', 'active': True},
    {'id': 'S3', 'val': 5.0, 'type': 'temp', 'active': False},
    {'id': 'S4', 'val': 8.2, 'type': 'flow', 'active': True},
    {'id': 'S5', 'val': 5.2, 'type': 'temp', 'active': True},
    {'id': 'S6', 'val': 6.9, 'type': 'pressure', 'active': True},
    {'id': 'S7', 'val': 5.15, 'type': 'temp', 'active': True}
]

# Irrelevant helper function (decoy)
def calculate_average(values):
    return sum(values) / len(values) if values else 0

def normalize_string(s):
    return s.upper().strip().replace('_', '')

# Unused transformation map
type_mapping = {
    'temp': 'T',
    'pressure': 'P',
    'flow': 'F'
}

# Red herring: complex-looking but unused bit manipulation
def obfuscate_id(sensor_id):
    bits = 0
    for c in sensor_id:
        bits ^= ord(c) << (len(sensor_id) % 4)
    return bits ^ 0xABCDEF

# Misleading intermediate computation (dead path)
aggregated_stats = {}
dummy_vals = [d['val'] for d in data_stream if d['type'] == 'temp']
if len(dummy_vals) > 3:
    avg_temp = calculate_average(dummy_vals)
    temp_variance = sum((v - avg_temp)**2 for v in dummy_vals) / len(dummy_vals)
    # This block runs but doesn't contribute to final result
    aggregated_stats['apparent_trend'] = 'stable' if temp_variance < 0.1 else 'fluctuating'

# Real processing begins here
active_temps = filter(lambda x: x['active'] and x['type'] == 'temp', data_stream)
sorted_active = sorted(active_temps, key=lambda x: x['val'])

# Group by value clusters (within 0.1)
grouped = []
for k, g in itertools.groupby(sorted_active, key=lambda x: round(x['val'], 1)):
    group_items = list(g)
    if len(group_items) >= 2:  # Only consider duplicates
        grouped.append({'key': k, 'items': group_items, 'count': len(group_items)})

# Extract raw values from groups
flat_grouped_vals = list(itertools.chain.from_iterable(
    [item['val'] for item in g['items']] for g in grouped
))

# Threshold logic obscured among distractions
def is_critical(v):
    return v > 5.1 and v < 5.2

def count_critical(data_list):
    return len([v for v in data_list if is_critical(v)])

# Unused recursive variant (decoy)
def recursive_count(arr, idx=0, acc=0):
    if idx >= len(arr):
        return acc
    return recursive_count(arr, idx + 1, acc + (1 if is_critical(arr[idx]) else 0))

# Distractor: string-based analysis of sensor IDs (irrelevant)
id_parts = [s['id'][0] for s in data_stream]
unique_prefixes = set(id_parts)
prefix_count = {p: id_parts.count(p) for p in unique_prefixes}

# Critical variable construction
reference_frame = {'base': 5.0, 'tolerance': 0.15}
filtered_data = [d['val'] for d in data_stream 
                   if d['type'] == 'temp' 
                   and d['active']
                   and abs(d['val'] - reference_frame['base']) <= reference_frame['tolerance']]

# Complex-looking but ultimately unused matrix
weight_matrix = [[i * 0.1 + j * 0.01 for j in range(3)] for i in range(len(filtered_data))]
matrix_trace = sum(weight_matrix[i][i] for i in range(min(len(weight_matrix), 3))) if weight_matrix else 0

# Real threshold function used in final call
criticality_score = lambda x: (x - 5.0) * 100
threshold_func = lambda vals: sum(map(criticality_score, vals))

# Core processing function
def process_readings(readings, scorer):
    if not readings:
        return 0
    
    # Secondary filtering: only values near cluster center
    mean_val = sum(readings) / len(readings)
    deviants = [v for v in readings if abs(v - mean_val) > 0.05]
    core_values = [v for v in readings if v not in deviants]
    
    # Apply scoring function
    raw_score = scorer(core_values)
    
    # Adjust for precision confidence
    precision_factor = 1.0 + (0.01 * len(core_values))
    return int(raw_score * precision_factor)

# Final computation
final_diagnostic = process_readings(filtered_data, threshold_func)

# Output result
print(f"Result: {final_diagnostic}")