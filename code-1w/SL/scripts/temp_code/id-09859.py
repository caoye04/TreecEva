from collections import defaultdict, Counter

# Simulated sensor data stream with noise and metadata
data_stream = [
    (100, 'temp', 'A'), (105, 'temp', 'B'), (98, 'temp', 'A'),
    (203, 'pressure', 'A'), (198, 'pressure', 'B'), (200, 'pressure', 'A'),
    (54, 'humidity', 'A'), (56, 'humidity', 'B'), (55, 'humidity', 'A'),
    (102, 'temp', 'B'), (201, 'pressure', 'B'), (57, 'humidity', 'B')
]

# Irrelevant auxiliary mappings (distractor)
status_map = {'A': 'active', 'B': 'standby'}
unit_scale = {'temp': 1.0, 'pressure': 0.5, 'humidity': 2.0}
calibration_offsets = defaultdict(lambda: 0)
calibration_offsets['temp'] = -2
calibration_offsets['pressure'] = +3
calibration_offsets['humidity'] = -1

# Data aggregation structures (mixed relevance)
raw_by_type = defaultdict(list)
processed_by_node = defaultdict(list)
aggregated_stats = {}

# Dead code path - never invoked (red herring)
def legacy_filter(x):
    return x > 100 if x % 2 == 0 else x < 50

# Unused transformation function (decoy)
def normalize(value, mode='linear'):
    if mode == 'linear':
        return value / 100.0
    elif mode == 'log':
        return log(value + 1)

# Main processing pipeline
for value, sensor_type, node_id in data_stream:
    raw_by_type[sensor_type].append(value)
    # Apply calibration offset (relevant)
    corrected = value + calibration_offsets[sensor_type]
    processed_by_node[node_id].append((corrected, sensor_type))

# Compute baselines (partially relevant)
for stype, values in raw_by_type.items():
    avg = sum(values) / len(values)
    aggregated_stats[stype] = {
        'mean': avg,
        'deviation': sum((v - avg)**2 for v in values) / len(values),
        'peak': max(values)
    }

# Transform data into rolling differential pattern (key step)
transformed_data = []
for node_id, readings in processed_by_node.items():
    sorted_vals = sorted(readings, key=lambda x: x[0])
    diffs = []
    for i in range(1, len(sorted_vals)):
        diff = sorted_vals[i][0] - sorted_vals[i-1][0]
        diffs.append(diff)
    transformed_data.extend(diffs)

# Decoy statistical summary (irrelevant)
summary_report = {
    'node_count': len(processed_by_node),
    'total_observations': len(data_stream),
    'sensor_types': list(raw_by_type.keys())
}

# Auxiliary bitmask analysis (misleading intermediate)
bit_analysis = 0
for d in transformed_data:
    bit_analysis ^= int(d)  # XOR all integer parts
    bit_analysis += d % 3   # Add modulo residue (confusing but unused later)

# Threshold determination using modular arithmetic (relevant)
base_threshold = int(aggregated_stats['temp']['mean'])
threshold = (base_threshold % 13) * 2.5  # Magic factor scaling

# Real-time anomaly detection via pattern frequency (core logic)
def analyze_pattern(data, thresh):
    # Count frequency of values above threshold
    count_above = sum(1 for x in data if x > thresh)
    count_below = len(data) - count_above
    
    # Use conditional expression to decide weighting (critical)
    weight = 3.0 if count_above > count_below else 1.5
    
    # Frequency-weighted signal strength
    signal = (count_above * weight) - (count_below * 0.8)
    
    # Inject irrelevant bitwise twist (distraction)
    temp_signal = int(signal) & 0xFF  # Mask to 8 bits
    temp_signal |= (count_above << 2)  # Shift-in frequency (unused effect)
    
    # Final diagnostic is based on original signal, not masked version
    return round(signal * 0.7, 4)  # Dampened diagnostic score

# Execute main analysis
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")