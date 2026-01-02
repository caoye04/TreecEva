import itertools

def collect_metrics(data_stream):
    # Irrelevant aggregation function (dead path)
    return sum(len(record) for record in data_stream if 'status' in record)

def decode_signal(signal):
    # Misleading bit manipulation with decoy purpose
    shifted = (signal << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return toggled >> 1

def extract_features(records):
    # Unused feature engineering (distractor)
    features = []
    for r in records:
        if isinstance(r, dict) and 'values' in r:
            mean = sum(r['values']) / len(r['values'])
            features.append(mean * 0.97)
    return features

def filter_anomalies(cluster):
    # Core logic: identify non-anomalous nodes using XOR checksum
    valid_nodes = []
    for node in cluster:
        raw_id = int(node['id'].replace('N', ''))
        readings = node['readings']
        
        # Real anomaly detection: checksum via XOR of truncated readings
        checksum = 0
        for val in readings[:4]:
            checksum ^= int(abs(val)) % 256
        
        # Validation condition (key step)
        if checksum == decode_signal(raw_id):
            valid_nodes.append(readings)
    
    # Return flattened stream of valid readings
    return list(itertools.chain.from_iterable(valid_nodes))

def process_readings(stream):
    # Process filtered stream: compute weighted diagnostic score
    if not stream:
        return -1
    
    # Apply windowed transformation
    transformed = []
    for i in range(0, len(stream) - 1, 2):
        x, y = abs(stream[i]), abs(stream[i+1])
        if x + y > 0:
            # Weighted harmonic interaction
            transformed.append((2 * x * y) / (x + y) if x + y != 0 else 0)
    
    # Aggregate final metric
    total = 0.0
    weights = [0.5, 1.0, 1.5, 2.0]
    for idx, val in enumerate(transformed):
        weight = weights[idx % 4]
        total += val * weight * 0.1  # Dampening factor
    
    return round(total, 6)

# Simulated sensor network data (real input)
sensor_cluster = [
    {'id': 'N10', 'readings': [12.0, 8.0, 4.0, 0.0, 1.5], 'status': 'active'},
    {'id': 'N25', 'readings': [10.0, -6.0, 14.0, -2.0], 'status': 'active'},
    {'id': 'N42', 'readings': [7.0, 7.0, 7.0, 7.0], 'status': 'standby'},
    {'id': 'N19', 'readings': [-3.0, 5.0, -1.0, 9.0], 'status': 'active'}
]

# Dead code paths (distractions)
baseline_stats = collect_metrics(sensor_cluster)
diagnostic_features = extract_features(sensor_cluster)

# Key processing pipeline
filtered_data = filter_anomalies(sensor_cluster)
final_diagnostic = process_readings(filtered_data)

# Output result
print(f"Result: {final_diagnostic}")