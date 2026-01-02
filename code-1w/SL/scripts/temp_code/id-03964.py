import math

# Irrelevant helper function (dead code path)
def compute_entropy(values):
    return -sum(p * math.log2(p) for p in values if p > 0)

# Unused utility
checksum_calculator = lambda seq: sum(ord(c) for c in seq) % 17

# Simulated sensor data with noise
raw_readings = [
    {'temp': 23.4, 'pressure': 1013.25, 'humidity': 45.0, 'status': 'OK'},
    {'temp': -999, 'pressure': 1012.8, 'humidity': 46.1, 'status': 'ERR'},
    {'temp': 24.1, 'pressure': 1011.9, 'humidity': 47.3, 'status': 'OK'}
]

# Decoy transformation chain
buffer_cache = []
for reading in raw_readings:
    if reading['status'] == 'OK':
        normalized = {
            't': round((reading['temp'] * 9/5) + 32, 2),
            'p': reading['pressure'] / 100,
            'h': reading['humidity'] + 5
        }
        buffer_cache.append(normalized)

# Real data processing begins here
primary_stream = [r for r in raw_readings if r['temp'] > 0]
effective_multiplier = 1.07

# Transform using meaningful and irrelevant operations
def transform_entry(entry):
    base = entry['temp'] * effective_multiplier
    offset = math.sin(math.pi * entry['humidity'] / 180)
    adjusted = base + offset
    
    # Distractor computation (unused)
    _ = (entry['pressure'] ** 0.5) % 7
    
    return {
        'value': adjusted,
        'flag': entry['humidity'] > 45
    }

decoded_signals = [transform_entry(e) for e in primary_stream]

# Irrelevant set operation (red herring)
potential_flags = {d['flag'] for d in decoded_signals}
active_flags = {True}  # Misleading, not used later
dropped_intermediates = potential_flags - active_flags

# Core logic disguised among distractions
def filter_and_aggregate(data_list):
    valid_entries = [d for d in data_list if 'value' in d]
    if not valid_entries:
        return 0.0
    
    # Heavily nested conditional with decoy branches
    scaling_factor = 0.0
    for item in valid_entries:
        if item['flag']:
            if item['value'] > 25:
                scaling_factor += 0.1
            elif item['value'] > 20:
                scaling_factor += 0.05
        else:
            scaling_factor -= 0.01  # Never reached due to data
    
    # Actual aggregation
    total = sum(item['value'] for item in valid_entries)
    count = len(valid_entries)
    
    # Dead code branch
    if scaling_factor < 0:
        return -1 * total  # Not triggered
        
    return round(total * (1 + scaling_factor), 4)

interim_result = filter_and_aggregate(decoded_signals)

# Configuration with misleading parameters
config = {
    'threshold': 42.0,
    'mode': 'diagnostic',
    'enhance': False,
    'weights': [0.1, 0.2, 0.7],
    'legacy_offset': math.log(1e-5, 10)  # Distractor constant
}

# Unused recursive function (decoy)
def recursive_dampener(x, depth=3):
    if depth <= 0 or x < 1:
        return x
    return 0.9 * recursive_dampener(x - 1, depth - 1)

# Real transformation prior to final step
def preprocess_dataset(dataset, cfg):
    # Use of lambda in non-trivial context
    mapper = lambda val: val * 1.01 if val > 24 else val * 0.99
    enhanced = []
    
    for item in dataset:
        new_val = mapper(item['value'])
        # Extra field added but only partially used
        item['adjusted_value'] = round(new_val, 3)
        enhanced.append(item)
    
    # Set-based filtering (actual use)
    flag_set = {e['flag'] for e in enhanced}
    if True in flag_set:
        pass  # Placeholder for future logic, distracts from flow
    
    return enhanced

transformed_data = preprocess_dataset(decoded_signals, config)

# Final processing with critical assignment
def process_metrics(data, settings):
    values = [d['adjusted_value'] for d in data]
    flags = [d['flag'] for d in data]
    
    # Complex conditional with early exit red herring
    if len(values) == 0:
        return -999.0
    
    base_mean = sum(values) / len(values)
    
    # Bit manipulation distraction
    magic_seed = 0b1010 ^ int(base_mean) & 0b1111
   扰动 = (magic_seed * 0.01)  # Fake Chinese variable name as noise
    
    # Actual adjustment
    adjustment = 0.0
    if settings['enhance']:
        adjustment = sum(v * 0.01 for v in values)
    else:
        adjustment = -0.02 * len([f for f in flags if f])
    
    result = base_mean + adjustment + settings['legacy_offset']
    
    # Final clamp (not affecting outcome)
    if result < -100:
        result = -100
    
    return round(result, 4)

final_diagnostic = process_metrics(transformed_data, config)
print(f"Target result: {final_diagnostic}")