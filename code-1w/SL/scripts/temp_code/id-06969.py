import itertools

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'temp': 23.5, 'humidity': 45.2, 'pressure': 1013, 'status': 'OK', 'timestamp': '2023-07-12T10:00:00'},
    {'temp': 24.1, 'humidity': 47.8, 'pressure': 1012, 'status': 'OK', 'timestamp': '2023-07-12T10:01:00'},
    {'temp': 22.9, 'humidity': 44.1, 'pressure': 1014, 'status': 'ERROR', 'timestamp': '2023-07-12T10:02:00'},
    {'temp': 25.3, 'humidity': 50.5, 'pressure': 1011, 'status': 'OK', 'timestamp': '2023-07-12T10:03:00'}
]

# Irrelevant auxiliary mappings (distractor)
status_codes = {'OK': 200, 'WARNING': 300, 'ERROR': 500}
category_map = {'A': 'Normal', 'B': 'Caution', 'C': 'Alert'}

# Decoy transformation functions (dead code path)
def legacy_normalize(data):
    return [d['temp'] * 1.8 + 32 for d in data if d['status'] == 'OK']

def deprecated_filter(stream):
    return list(filter(lambda x: x['pressure'] > 1010, stream))

# Real processing pipeline
config = {
    'threshold': 24.0,
    'scale_factor': 0.75,
    'offset': 2.5,
    'active': True
}

# Misleading intermediate aggregation (red herring)
raw_averages = {
    'avg_temp': sum(d['temp'] for d in data_stream) / len(data_stream),
    'avg_humidity': sum(d['humidity'] for d in data_stream) / len(data_stream)
}

# String-based timestamp parser (partially relevant)
def parse_time_segment(ts):
    return int(ts.split('T')[1].split(':')[0])

# Bitwise diagnostic flag generator (distractor)
def generate_flag(value):
    return (int(value * 10) ^ 0xFF) & 0x7F

# Core transformation function
transformed_data = []
for entry in data_stream:
    hour = parse_time_segment(entry['timestamp'])
    base_value = entry['temp']
    
    # Apply conditional scaling based on time and status
    if entry['status'] == 'OK' and hour < 12:
        adjusted = base_value * config['scale_factor'] + config['offset']
    else:
        adjusted = base_value + config['offset']
    
    # Add derived features (some used, some not)
    transformed_entry = {
        'value': adjusted,
        'flag': generate_flag(adjusted),
        'source_hour': hour,
        'valid': entry['status'] == 'OK'
    }
    transformed_data.append(transformed_entry)

# Filter only valid entries
filtered_data = [item for item in transformed_data if item['valid']]

# Extract values for metric computation
values = [v['value'] for v in filtered_data]

# Decoy statistical functions (unused)
calculate_median = lambda x: sorted(x)[len(x)//2] if len(x) % 2 == 1 else (sorted(x)[len(x)//2-1] + sorted(x)[len(x)//2]) / 2
calculate_mode = lambda x: max(set(x), key=x.count) if x else None

# Real metric processor
def compute_metric_series(vals, cfg):
    if not vals:
        return [0.0]
    
    # Generate rolling differences
    diffs = [abs(a - b) for a, b in itertools.pairwise(vals)]
    
    # Apply exponential weighting (simulated)
    weights = [0.5 ** i for i in range(len(diffs))]
    weighted_diffs = [d * w for d, w in zip(diffs, weights)]
    
    # Aggregate with offset
    total = sum(weighted_diffs) + cfg['offset']
    
    # Normalize by count (if any diffs)
    if len(weighted_diffs) > 0:
        result = total / len(weighted_diffs)
    else:
        result = total
    
    return [result, len(vals)]

# Process metrics function
def process_metrics(data_list, settings):
    raw_vals = [item['value'] for item in data_list]
    metrics = compute_metric_series(raw_vals, settings)
    
    # Secondary adjustment
    primary_score = metrics[0] * settings['scale_factor']
    secondary_weight = metrics[1] * 0.1
    
    # Final diagnostic calculation
    final_score = (primary_score + secondary_weight) * 100
    
    # Dead code branch (never executed due to settings['active'] being True)
    if not settings['active']:
        fallback = sum(generate_flag(v['value']) for v in data_list)
        final_score = fallback / 10.0
    
    return final_score

# Execute critical statement
final_diagnostic = process_metrics(transformed_data, config)

# Print result as required
print(f"Target result: {final_diagnostic}")