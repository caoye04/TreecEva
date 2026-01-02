import math

# Simulated sensor data with noise and metadata
data_stream = [
    {'id': 101, 'val': 3.2, 'err': 0.1, 'active': True},
    {'id': 102, 'val': -1.4, 'err': 0.3, 'active': False},
    {'id': 103, 'val': 2.8, 'err': 0.15, 'active': True},
    {'id': 104, 'val': 0.0, 'err': 0.0, 'active': True},
    {'id': 105, 'val': 5.5, 'err': 0.5, 'active': True}
]

# Irrelevant lookup table for unused device types
device_map = {101: 'TEMP', 102: 'PRESS', 103: 'HUMID', 104: 'FLOW', 105: 'LEVEL'}
device_status = {k: 'CALIBRATED' for k in device_map}

# Decoy transformation - never used
def apply_calibration(x, e):
    return x * (1 + e) if x > 0 else x * (1 - e)

# Unused recursive helper for hypothetical drift correction
def adjust_drift(values, factor=0.95):
    if len(values) <= 1:
        return values
    mid = len(values) // 2
    return adjust_drift(values[:mid], factor) + [values[mid] * factor] + adjust_drift(values[mid+1:], factor)

# Real signal filter: extract active non-zero values
filtered_data = [entry['val'] for entry in data_stream if entry['active'] and entry['val'] != 0.0]

# Multiple configuration layers with red herrings
core_params = {'gain': 2.1, 'offset': -0.5, 'threshold': 1.0}
irrelevant_tuning = {'damping': 0.8, 'inertia': 2, 'response_curve': 'exponential'}
config = {**core_params, **irrelevant_tuning}  # Merged but only some used

# Bitwise mask simulation for channel selection (partially relevant)
channel_mask = 0b1101
valid_channels = [i for i in range(4) if channel_mask & (1 << i)]
channel_weights = {i: 1.0 + (i * 0.1) for i in valid_channels}  # Not used but looks important

# Enumerate-based compensation for time lag (unused path)
time_lag_table = [0.1, 0.15, 0.12, 0.18]
compensation_shift = 0.0
for idx, lag in enumerate(time_lag_table):
    compensation_shift += lag * (idx % 2 + 1)

# Real processing function with conditional logic and math
def process_signals(signals, cfg):
    base_result = 0.0
    temp_log_store = []  # Dead storage
    
    for i, val in enumerate(signals):
        # Apply gain and offset from config
        adjusted = val * cfg['gain'] + cfg['offset']
        
        # Conditional amplification based on threshold
        if abs(adjusted) > cfg['threshold']:
            adjusted = adjusted * 1.5  # Boost strong signals
        
        # Simulate phase inversion on even indices using XOR trick
        if i ^ 1 == i + 1:  # Only true when i is odd
            adjusted = -adjusted
        
        base_result += adjusted
        
        # Record to dead log
        temp_log_store.append({'step': i, 'value': adjusted})
    
    # Final nonlinear transformation
    if base_result > 0:
        result = math.log(base_result + 1) * 100
    else:
        result = -math.pow(abs(base_result) + 1, 0.5) * 50
    
    return int(result)  # Discretize final output

# Secondary decoy computation that looks important
aggregate_stats = {
    'count': len(data_stream),
    'active_ratio': sum(1 for d in data_stream if d['active']) / len(data_stream),
    'total_err': sum(d['err'] for d in data_stream)
}

# Key execution point
final_output = process_signals(filtered_data, config)

# Misleading post-processing block (never executed due to final print)
if final_output < 0:
    final_output = final_output ^ 256
    final_output = final_output & 511

print(f"Result: {final_output}")