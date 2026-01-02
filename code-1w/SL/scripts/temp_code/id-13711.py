import math

# Simulated sensor data with noise and redundant fields
data_packet = {
    'sensor_id': 'SND-7F3A',
    'readings': [23.5, 19.8, 45.2, 31.7, 28.3, 36.1, 25.4],
    'status_flags': [0b1010, 0b1100, 0b0010, 0b1111, 0b0101],
    'timestamp': '2023-11-05T14:23:17Z',
    'checksum': 'a3c7e9f2',
    'version': '2.1.0'
}

# Irrelevant auxiliary functions (distractor)
def validate_checksum(cs):
    return sum(ord(c) for c in cs) % 17 == 0
def decode_version(v):
    return tuple(map(int, v.split('.')))

def encrypt_signal(x):
    return (x * 2654435761) % 2**32  # Prime multiplier, irrelevant

def analyze_pattern(seq):
    # Complex but unused analysis
    if len(seq) < 5:
        return False
    trend = all(seq[i] <= seq[i+1] for i in range(len(seq)-1))
    oscillation = sum(1 for i in range(1, len(seq)-1) if seq[i-1] < seq[i] > seq[i+1])
    return trend or oscillation > 2

# Core processing chain
raw_readings = data_packet['readings']

# Step 1: Normalize readings using z-score (but only mean used later)
population_mean = sum(raw_readings) / len(raw_readings)
population_std = (sum((x - population_mean)**2 for x in raw_readings) / len(raw_readings))**0.5
normalized = [(x - population_mean) / population_std for x in raw_readings]

# Step 2: Apply non-linear transformation via lambda (required feature)
squash_fn = lambda val: math.log(val + 30)  # Shifted log to avoid negative logs
transformed_readings = [squash_fn(x) for x in raw_readings]

# Step 3: Aggregate via bitwise fusion of status flags (red herring)
flag_fuse = 0
for flag in data_packet['status_flags']:
    flag_fuse ^= flag  # XOR accumulation
    flag_fuse = (flag_fuse << 1) & 0b1111 | (flag_fuse >> 3)  # Rotate bits

# Step 4: Mask creation based on threshold (unused mask)
threshold_mask = [1 if x > population_mean else 0 for x in raw_readings]

# Step 5: String metadata processing (required string method)
encoded_id = data_packet['sensor_id'].lower().replace('-', '').upper()[::-1]  # distractor transform
id_hash = sum(ord(encoded_id[i]) * (7 ** i) for i in range(len(encoded_id))) % 10000

# Step 6: Data enrichment with windowed features
windowed_stats = []
for i in range(2, len(transformed_readings)):
    window = transformed_readings[i-2:i+1]
    win_avg = sum(window) / len(window)
    win_var = sum((x - win_avg)**2 for x in window) / len(window)
    windowed_stats.append({'avg': win_avg, 'variance': win_var})

# Step 7: Configuration profile (only some keys are used)
config = {
    'sensitivity': 0.85,
    'calibration_offset': -4.2,
    'activation_threshold': population_mean - 2.0,
    'log_base': math.e,
    'decay_factor': 0.9,
    'padding_char': '*',
    'temp_override': False
}

# Step 8: Transform data structure
transformed_data = {
    'items': [
        {'val': round(tr, 4), 'meta': f"V{idx}"} 
        for idx, tr in enumerate(transformed_readings)
    ],
    'seq_length': len(transformed_readings),
    'origin_hash': id_hash
}

# Step 9: Main diagnostic processor
def process_metrics(data_dict, cfg):
    values = [item['val'] for item in data_dict['items']]
    
    # Extract threshold from config
    thresh = cfg['activation_threshold']
    
    # Count how many exceed threshold (key computation)
    active_count = len([v for v in values if v > thresh])
    
    # Compute weighted signal (but weight decays exponentially)
    signal_sum = 0.0
    weight = 1.0
    for v in reversed(values):
        signal_sum += v * weight
        weight *= cfg['decay_factor']
    
    # Secondary metric: count of high-value entries with even index
    boosted_indices = [i for i, v in enumerate(values) if v > thresh and i % 2 == 0]
    
    # Apply calibration offset (this modifies final result)
    calibrated_sum = signal_sum + cfg['calibration_offset']
    
    # Final logic: complex condition that simplifies due to data
    if active_count > 3 and len(boosted_indices) >= 2:
        diagnostic_score = calibrated_sum * 123
    elif active_count > 0:
        diagnostic_score = calibrated_sum * 42
    else:
        diagnostic_score = 100.0
    
    # Inject integer conversion (answer becomes int-like)
    return int(round(diagnostic_score))

# Execute main logic
final_diagnostic = process_metrics(transformed_data, config)

# Print result as required
print(f"Result: {final_diagnostic}")