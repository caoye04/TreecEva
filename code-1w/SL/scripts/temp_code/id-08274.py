import math

# Simulated sensor data with noise and metadata
data_stream = [
    {'id': 101, 'val': 3.5, 'type': 'temp', 'active': True},
    {'id': 102, 'val': 7.2, 'type': 'pressure', 'active': True},
    {'id': 103, 'val': -1.0, 'type': 'temp', 'active': False},
    {'id': 104, 'val': 4.8, 'type': 'flow', 'active': True},
    {'id': 105, 'val': 6.1, 'type': 'temp', 'active': True}
]

# Irrelevant lookup table (distractor)
type_map = {'temp': 0, 'pressure': 1, 'flow': 2, 'level': 3}

# System thresholds (only partially used)
thresh = {
    'temp': (0.0, 5.0),
    'pressure': (1.0, 8.0),
    'flow': (2.0, 6.0)
}

# Unused calibration matrix (dead code path)
calibration_matrix = [
    [1.0, 0.1, -0.05],
    [0.05, 1.0, 0.02],
    [-0.03, 0.04, 1.0]
]

# Misleading intermediate transformation (not used in final result)
def apply_calibration(data):
    return [x * 1.05 for x in data]  # This function is never called

# Decoy statistical function with complex logic but no impact
def compute_robust_mean(values):
    if len(values) == 0:
        return 0.0
    sorted_vals = sorted(values)
    trim_count = max(1, len(sorted_vals) // 4)
    trimmed = sorted_vals[trim_count:-trim_count] if len(trimned) > 2 else sorted_vals
    return sum(trimmed) / len(trimmed)

# Real processing begins here
valid_ids = {101, 102, 104, 105}  # ID 103 excluded due to policy

# Filter active sensors with valid IDs
filtered_data = [entry for entry in data_stream 
                   if entry['active'] and entry['id'] in valid_ids]

# Extract base values for processing
base_values = [entry['val'] for entry in filtered_data]

# Spurious normalization (unused)
max_val = max(base_values) if base_values else 1.0
normalized = [v / max_val for v in base_values]  # Distractor

# Configuration dictionary with red herring keys
config = {
    'mode': 'aggressive',
    'threshold_adjust': 0.5,
    'use_enhancement': True,
    'decay_factor': 0.9,
    'dummy_flag': False,  # unused
    'version': '2.1b'     # unused
}

# Auxiliary mapping using enumerate and zip (required features)
indexed_types = {i: t for i, t in enumerate(set(entry['type'] for entry in data_stream))}
inverse_type_map = {v: k for k, v in indexed_types.items()}
type_order = ['temp', 'pressure', 'flow']
offset_map = dict(zip(type_order, [1, 2, 3]))  # Used in processing

# Secondary filter based on dynamic condition
reference_value = sum(base_values) / len(base_values) if base_values else 0

# Augment data with computed offsets
for item in filtered_data:
    t = item['type']
    if t in offset_map:
        # Apply offset only to certain types
        item['val'] += offset_map[t] * 0.1

# Complex conditional processing tree
bit_flags = 0
for i, val in enumerate([entry['val'] for entry in filtered_data]):
    if val > reference_value:
        bit_flags |= (1 << i)
    elif val == reference_value:
        bit_flags ^= (1 << (i // 2)) if i > 0 else 0

# Set-based exclusion zone (distractor)
exclusion_zone = {x for x in range(100, 200, 7) if x % 2 == 0}

# Real signal processor
def process_signals(signals, cfg):
    mode = cfg['mode']
    adjust = cfg['threshold_adjust']
    enhanced = cfg['use_enhancement']
    
    # Local accumulator
    accum = 0.0
    temp_sum = 0.0
    pressure_cnt = 0
    
    # Use of enumerate over filtered relevant entries
    for idx, sig in enumerate(signals):
        raw_val = sig['val']
        sig_type = sig['type']
        
        # Only process 'temp' and 'pressure' for final output
        if sig_type == 'temp':
            contrib = raw_val ** 2
            if enhanced:
                contrib *= 1.1
            temp_sum += contrib
        elif sig_type == 'pressure':
            pressure_cnt += 1
            contrib = math.log(raw_val + 1)
            accum += contrib
        
        # Dead branch: flow type handled but doesn't contribute
        elif sig_type == 'flow':
            dummy_result = raw_val * 0.5 - adjust  # No effect
            continue
            
    # Final composition uses multiple concepts
    if temp_sum > 0:
        accum += math.sqrt(temp_sum)
    
    # Bit manipulation integration
    popcount = bin(bit_flags).count('1')
    if popcount > 0:
        accum = accum * (popcount + 1) / 2.0
    
    # Final adjustment
    accum -= adjust * 0.5
    
    return accum

# Execute main computation
final_output = process_signals(filtered_data, config)

# Irrelevant aggregation (misleads with complexity)
detailed_report = []
for i, d in enumerate(filtered_data):
    zipped = list(zip([i, i+1], [d['val'], d.get('extra', 0)]))
    detail = {"index": i, "zdata": zipped, "flagged": bit_flags & (1 << i)}
    detailed_report.append(detail)

# Output the required result
print(f"Result: {final_output}")