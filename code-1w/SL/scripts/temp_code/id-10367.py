def transform_signal(raw_values, scale_factor):
    """Apply non-linear transformation to sensor signal (distractor function)."""
    transformed = []
    for v in raw_values:
        if v < 0:
            transformed.append(-1 * (abs(v) ** 0.5))
        else:
            transformed.append(v ** 0.5)
    return [round(x * scale_factor, 3) for x in transformed]


def validate_checksum(entry):
    """Validate data entry checksum (red herring logic)."""
    chk = 0
    for c in str(entry):
        if c.isdigit():
            chk += int(c)
    return chk % 7 == 0


def recursive_filter(items, depth=0):
    """Recursively filter items based on arbitrary rule (misleading path)."""
    if depth >= 3 or not items:
        return len(items)
    filtered = []
    for x in items:
        if isinstance(x, int) and x % 2 == 0:
            filtered.append(x // 2)
    return recursive_filter(filtered, depth + 1)

# Irrelevant sensor labels (distractor data)
sensor_labels = ['S1', 'S2', 'SYNC', 'S3', 'CTRL', 'S4']
label_stats = {lbl: len(lbl) + i for i, lbl in enumerate(sensor_labels)}

# Simulated raw data with noise (partially relevant)
raw_data_stream = [16, -8, 24, 4, -12, 36, 8, -20]
scaling_constant = 2.5
noisy_adjustment = sum([i * 0.1 for i in range(len(raw_data_stream))])

# Apply transformation (irrelevant but plausible)
filtered_signal = transform_signal(raw_data_stream, scaling_constant)

# Data ingestion pipeline
primary_entries = [
    {'id': 'A7', 'readings': [4, 16, 25], 'meta': 'CAL'},
    {'id': 'B2', 'readings': [9, 36, 49], 'meta': 'NORM'},
    {'id': 'C5', 'readings': [1, 64, 81], 'meta': 'CAL'}
]

# Checksum validation batch (dead code path)
validation_results = []
for entry in primary_entries:
    num_id = int(entry['id'][1])
    valid_chk = validate_checksum(num_id * 113)
    validation_results.append(valid_chk)

# Real processing begins here
processed_data = []
for record in primary_entries:
    base_sq = []    
    for val in record['readings']:
        root = int(val ** 0.5)
        if root * root == val:  # Perfect square check
            base_sq.append(root)
    processed_data.append({
        'key': record['id'],
        'values': base_sq,
        'flag': 'high' if record['meta'] == 'CAL' else 'low'
    })

# Threshold configuration map (critical)
threshold_map = {
    'high': {'base': 3, 'multiplier': 2},
    'low': {'base': 1, 'multiplier': 4}
}

# Diagnostic analysis engine
status_log = []
error_flags = set()

for item in processed_data:
    config = threshold_map[item['flag']]
    total_score = 0
    for v in item['values']:
        # Core computation
        if v > config['base']:
            total_score += v * config['multiplier']
        else:
            total_score += v
    status_log.append(total_score)
    
    # Decoy error detection
    if sum(item['values']) > 20 and item['flag'] == 'low':
        error_flags.add(item['key'])

# Final diagnostic calculation
final_diagnostic = 0
for score in status_log:
    final_diagnostic += score * 3

# Additional irrelevant aggregation
aggregate_metrics = {}
for label in sensor_labels:
    aggregate_metrics[label] = label_stats[label] * 1.5

# Spurious string-based filtering
active_keys = [r['key'] for r in processed_data]
normalized_keys = [k.lower().replace(' ', '') for k in active_keys]
key_concat = ''.join(normalized_keys)
key_checksum = sum(ord(c) for c in key_concat if c in 'aceg')

# Final output
print(f"Result: {final_diagnostic}")