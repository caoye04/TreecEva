from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant fields
data = [
    {'temp': 25, 'humidity': 60, 'pressure': 1013, 'status': 'OK', 'seq': 1},
    {'temp': 26, 'humidity': 62, 'pressure': 1012, 'status': 'OK', 'seq': 2},
    {'temp': 27, 'humidity': 65, 'pressure': 1011, 'status': 'ERROR', 'seq': 3},
    {'temp': 28, 'humidity': 63, 'pressure': 1010, 'status': 'OK', 'seq': 4},
    {'temp': 29, 'humidity': 64, 'pressure': 1009, 'status': 'OK', 'seq': 5}
]

# Irrelevant baseline mappings (distractor)
baseline_map = defaultdict(lambda: 100)
baseline_map.update({(25, 60): 95, (26, 62): 96, (27, 65): 98})

# Weight configuration for scoring (critical)
weights = {'temp': 0.5, 'humidity': 0.3, 'pressure': 0.2}

# Noise filter mask (partially relevant but overcomplicated)
noise_filter = [entry['status'] == 'OK' for entry in data]
filtered_data = [entry for entry in data if entry['status'] == 'OK']

# Redundant frequency counter (distractor)
status_counter = Counter(entry['status'] for entry in data)

# Decoy function that looks important but isn't used in final path
def analyze_trend(seq_data):
    diff = [seq_data[i+1] - seq_data[i] for i in range(len(seq_data)-1)]
    return sum(diff) / len(diff) if diff else 0

# Auxiliary transformation with side effects (misleading)
transformed = []
for d in filtered_data:
    temp_c = d['temp']
    temp_f = (temp_c * 9/5) + 32
    scaled_humidity = d['humidity'] / 100.0
    encoded = f'{temp_f:.1f}:{scaled_humidity:.2f}'
    transformed.append(encoded)

# Bitwise integrity check (red herring)
integrity_key = 0
for d in data:
    integrity_key ^= d['seq']
integrity_key &= 0xFF  # Mask to byte

# Real processing function with nested logic
def process_metrics(entries, weight_config):
    base_values = defaultdict(float)
    adjustment_factor = 1.0
    
    # First pass: extract and normalize
    for entry in entries:
        base_values['temp'] += entry['temp']
        base_values['humidity'] += entry['humidity']
        base_values['pressure'] += entry['pressure']
    
    # Normalize by count (excluding ERROR entries already filtered)
    count = len(entries)
    for k in base_values:
        base_values[k] /= count
    
    # Apply weights
    weighted_sum = 0.0
    for k, v in base_values.items():
        weighted_sum += v * weight_config[k]
    
    # Conditional adjustment based on sequence pattern (subtle relevance)
    seqs = [e['seq'] for e in data]
    if all(s % 2 == 1 for s in seqs[::2]) and all(s % 2 == 0 for s in seqs[1::2]):
        adjustment_factor = 0.95
    
    # Secondary adjustment based on pressure trend (irrelevant due to filter)
    pressure_vals = [e['pressure'] for e in entries]
    pressure_trend = pressure_vals[-1] - pressure_vals[0]
    if pressure_trend < 0:
        adjustment_factor *= 0.98
    
    # Core computation
    raw_score = weighted_sum * 10
    
    # Destructuring assignment (tuple unpacking)
    offset, multiplier = (5, 1.05)
    
    # Final adjustment using conditional expression
    final_raw = raw_score + offset if raw_score < 30 else raw_score * multiplier
    
    # Apply adjustment factor from sequence logic only
    result = final_raw * adjustment_factor
    
    # Dead code branch (never reached - dead end)
    if integrity_key < 0:
        result = abs(result) ** 0.5
    
    return result

# Additional unused transformation (distractor)
aggregated = {}
for key in ['temp', 'humidity', 'pressure']:
    aggregated[key] = [d[key] for d in data]

# Critical execution point
temp_snapshot = [d['temp'] for d in data]
humidity_slice = [d['humidity'] for d in filtered_data][1:3]

# Main computation
final_score = process_metrics(filtered_data, weights)

# Print result as required
print(f"Target result: {final_score}")