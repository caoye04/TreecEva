import itertools

# Simulated sensor data chunks with metadata
raw_sensor_data = [
    {'id': 'S1', 'values': [3, 5, 7], 'type': 'thermal', 'valid': True},
    {'id': 'S2', 'values': [2, 4, 6], 'type': 'pressure', 'valid': True},
    {'id': 'S3', 'values': [1, 8, 9], 'type': 'thermal', 'valid': False},
    {'id': 'S4', 'values': [5, 5, 5], 'type': 'flow', 'valid': True}
]

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * (x / 10)  # nonsense calculation
    return round(total, 3)

# Another decoy: unused statistical transformation
def normalize_series(series):
    m = sum(series) / len(series)
    return [round((x - m) / m, 4) for x in series]

# Misleading intermediate processing step (dead path)
partial_aggregates = {}
for entry in raw_sensor_data:
    sensor_id = entry['id']
    vals = entry['values']
    partial_aggregates[sensor_id] = {
        'sum_sq': sum(x ** 2 for x in vals),
        'range': max(vals) - min(vals),
        'mode_hint': max(set(vals), key=vals.count) if len(set(vals)) < 3 else -1
    }

# Real but obscured logic begins here
filtered_data = [
    entry['values'] for entry in raw_sensor_data 
    if entry['type'] == 'thermal' and entry['valid']
]

# Distractor: unused set operation involving IDs
declared_types = {'thermal', 'pressure', 'flow', 'humidity'}
active_sensors = {entry['id'] for entry in raw_sensor_data if entry['valid']}
redundant_set_op = declared_types - {'humidity'}  # unused later

# Chunking into pairs using itertools (real usage)
flattened = list(itertools.chain.from_iterable(filtered_data))
chunked_pairs = list(itertools.zip_longest(flattened[::2], flattened[1::2], fillvalue=0))

processed_chunks = []
for a, b in chunked_pairs:
    # Apply modular arithmetic and bit manipulation
    val_a = (a * 3) % 11
    val_b = (b * 5) % 13
    combined = (val_a ^ val_b) + (val_a & 7)  # XOR and bitwise AND
    processed_chunks.append(combined)

# Decoy: this function is defined but not used
def evaluate_stability(seq):
    if len(seq) < 2:
        return False
    diffs = [abs(seq[i] - seq[i+1]) for i in range(len(seq)-1)]
    return sum(diffs) / len(diffs) < 2.0

# Real transformation function
def transform_data(chunks):
    result = 0
    for i, val in enumerate(chunks):
        if i % 2 == 0:
            result += val * (i + 1)
        else:
            result -= val // (i + 1)
    
    # Inject irrelevant dictionary mapping
    status_map = {0: 'nominal', 1: 'alert', 2: 'caution'}
    temp_debug = {i: pow(val, 2, 17) for i, val in enumerate(chunks)}  # unused
    
    # Final adjustment using tuple unpacking (relevant)
    multiplier, offset = (3, 7)
    final_raw = result * multiplier + offset
    
    # Red herring: floating point conversion that looks important
    smoothed = round(final_raw / 2.5, 4)
    normalized_again = (smoothed * 1.01)  # distraction
    
    # Actual answer derivation
    core_value = int(smoothed)  # final truncation
    return core_value

# Execution point of interest
core_result = transform_data(processed_chunks)

# Print required output
print(f"Target result: {core_result}")