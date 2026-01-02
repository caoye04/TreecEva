import math

# Simulated sensor data with noise and metadata
data_stream = [
    {'id': 101, 'value': 85, 'status': 'active', 'timestamp': 1623456780},
    {'id': 102, 'value': 45, 'status': 'inactive', 'timestamp': 1623456781},
    {'id': 103, 'value': 70, 'status': 'active', 'timestamp': 1623456782},
    {'id': 104, 'value': 90, 'status': 'active', 'timestamp': 1623456783},
    {'id': 105, 'value': 55, 'status': 'active', 'timestamp': 1623456784},
    {'id': 106, 'value': 60, 'status': 'inactive', 'timestamp': 1623456785},
    {'id': 107, 'value': 78, 'status': 'active', 'timestamp': 1623456786}
]

# Irrelevant baseline constants (distractor)
BASELINE_OFFSET = 23.7
CALIBRATION_FACTOR = 1.05
MAX_TOLERANCE = 5

# Configuration map for processing (used later)
config = {
    'threshold': 65,
    'gain': 1.2,
    'mode': 'aggressive',
    'history_limit': 100
}

# Decoy function - looks important but unused
def calibrate_sensor(x):
    return (x * CALIBRATION_FACTOR) + BASELINE_OFFSET

# Another decoy: dead utility function
def normalize_values(data_list):
    max_val = max(d['value'] for d in data_list)
    return [d['value'] / max_val for d in data_list]

# Auxiliary transformation that's never called
def shift_timezones(timestamps):
    return [(ts + 3600) % 86400 for ts in timestamps]

# Real preprocessing: filter active signals above threshold
active_data = [entry for entry in data_stream if entry['status'] == 'active']
filtered_data = [e for e in active_data if e['value'] > config['threshold']]

# Red herring computation: complex-looking but unused bit manipulation
aggregate_key = 0
for item in data_stream:
    aggregate_key ^= (item['id'] << 2) | (item['value'] & 3)
    aggregate_key = (aggregate_key * 7) % 10007

# Unused sorting path (dead logic branch)
sorted_by_id = sorted(active_data, key=lambda x: x['id'])
temp_results = []
for i, record in enumerate(sorted_by_id):
    if i % 2 == 0:
        temp_results.append(math.log(record['value'] + 1))

# Dictionary mapping for mode-based behavior
mode_handlers = {
    'conservative': lambda x: x * 0.9,
    'balanced': lambda x: x * 1.0,
    'aggressive': lambda x: x * 1.2
}

# Complex multi-step signal processor
weighted_sum = 0.0
weight_sequence = [0.5, 1.0, 1.5, 2.0]

for idx, sample in enumerate(filtered_data):
    raw_val = sample['value']
    # Apply gain based on configuration
    adjusted = raw_val * config['gain']
    
    # Weight by position using sequence (wraps if needed)
    weight = weight_sequence[idx % len(weight_sequence)]
    weighted_sum += adjusted * weight

# Secondary metric: count of high-magnitude shifts (distractor)
prev = filtered_data[0]['value']
magnitude_shifts = 0
for pt in filtered_data[1:]:
    if abs(pt['value'] - prev) > 10:
        magnitude_shifts += 1
    prev = pt['value']

# Another decoy structure: zipped enumeration that does nothing
indices = list(range(len(filtered_data)))
for i, (idx, datum) in enumerate(zip(indices, filtered_data)):
    transformed = (datum['value'] >> 1) ^ 0xAA
    # No side effects, just burns cycles

# Real final processing function
def process_signals(signal_list, cfg):
    base_total = sum(item['value'] for item in signal_list)
    
    # Mode-based amplification
    handler = mode_handlers.get(cfg['mode'], lambda x: x)
    amplified = handler(base_total)
    
    # Double-check filtering (redundant but adds logic depth)
    if len(signal_list) >= 2:
        # Additional boost for multi-signal confirmation
        amplified *= 1.1
    
    # Final nonlinear transformation
    result = math.sqrt(amplified ** 2 / len(signal_list)) if signal_list else 0
    
    # Dead comparison with no effect (misdirection)
    if result > 1000:
        return int(result / 10)
    
    return int(result)

# Critical execution point
final_output = process_signals(filtered_data, config)

# Output the target result
print(f"Target result: {final_output}")