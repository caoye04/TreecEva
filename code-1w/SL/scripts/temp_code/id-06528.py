import math

# Simulated sensor data with noise and redundant metrics
data_points = [127, 255, 98, 44, 211, 77, 150, 63]
noise_floor = 32
amplification_factor = 2.5

# Irrelevant signal processing functions (dead code path)
def apply_fft(signal):
    return [abs(x * 1j**i) for i, x in enumerate(signal)]

def normalize_signal(s):
    max_val = max(s)
    return [x / max_val for x in s]

# Decoy variables with misleading intermediate values
baseline_offset = 1024
temp_correction = sum([x % 17 for x in data_points])  # Distractor computation
scaling_bias = math.log(baseline_offset + temp_correction)  # Misleading but unused

# Core configuration parameters
weights = {'w1': 0.3, 'w2': 0.5, 'w3': 0.2}
thresholds = {'low': 50, 'high': 200}

# Raw data with embedded metadata and junk entries
raw_data = {
    'readings': data_points,
    'meta': {
        'version': '2.1',
        'calibration': [0.98, 1.02, 0.99],
        'checksum': 'a9f'
    },
    'flags': ['OK', 'VALID', 'SYNC'],
    'debug_info': [
        {'cycle': 1, 'status': 'PASS'},
        {'cycle': 2, 'status': 'PASS'}
    ]
}

# Auxiliary function that appears relevant but is not used
def compute_rolling_avg(data, window=3):
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

# String-based validation (irrelevant to final result)
def validate_data_integrity(raw):
    flags = raw.get('flags', [])
    return 'ERROR' not in [f.upper() for f in flags if isinstance(f, str)]

# Unused transformation using string methods
status_summary = ''.join(raw_data['flags']).lower()
active_modes = status_summary.replace('sync', '').strip()

# Conditional branch with red herring logic
if len(data_points) > 5:
    adjusted_points = [x - noise_floor for x in data_points]
else:
    adjusted_points = [x + noise_floor for x in data_points]

# Bit manipulation decoy
bit_analysis = [x ^ 0xFF for x in adjusted_points]  # Inverted but unused

# Key processing pipeline
valid_readings = [x for x in adjusted_points if thresholds['low'] < x < thresholds['high']]

# Apply weighting using multiple steps and list comprehensions
weighted_components = {
    'w1': sum([x * weights['w1'] for x in valid_readings if x < 100]),
    'w2': sum([x * weights['w2'] for x in valid_readings if 100 <= x < 150]),
    'w3': sum([x * weights['w3'] for x in valid_readings if x >= 150])
}

# Secondary filter based on digit analysis (string method distractor)
digit_filtered = []
for val in valid_readings:
    digits = ''.join(sorted(str(val)))
    if '1' in digits and '2' not in digits:  # Complex but irrelevant condition
        digit_filtered.append(val)

# Main result processor (only this affects final_score)
def process_results(data, w):
    readings = data['readings']
    adj = [x - noise_floor for x in readings]
    filtered = [x for x in adj if 50 < x < 200]
    total = 0.0
    total += sum(x * w['w1'] for x in filtered if x < 100)
    total += sum(x * w['w2'] for x in filtered if 100 <= x < 150)
    total += sum(x * w['w3'] for x in filtered if x >= 150)
    return total

# Final computation
final_score = process_results(raw_data, weights)

# Output result as required
print(f"Target result: {final_score}")