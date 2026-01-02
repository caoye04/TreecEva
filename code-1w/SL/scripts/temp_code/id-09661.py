import math

# Simulated sensor data with noise and metadata
data_stream = [
    {'id': 101, 'val': 3.2, 'type': 'temp', 'status': 'active', 'seq': 1},
    {'id': 102, 'val': 1.8, 'type': 'pressure', 'status': 'active', 'seq': 2},
    {'id': 103, 'val': 2.5, 'type': 'temp', 'status': 'noisy', 'seq': 3},
    {'id': 104, 'val': 4.0, 'type': 'flow', 'status': 'active', 'seq': 4},
    {'id': 105, 'val': 2.1, 'type': 'temp', 'status': 'active', 'seq': 5},
    {'id': 106, 'val': 3.6, 'type': 'pressure', 'status': 'active', 'seq': 6},
    {'id': 107, 'val': 2.9, 'type': 'temp', 'status': 'inactive', 'seq': 7},
    {'id': 108, 'val': 1.9, 'type': 'flow', 'status': 'active', 'seq': 8}
]

# System configuration with irrelevant parameters
config = {
    'threshold': 2.3,
    'calibration_factor': 1.05,
    'max_records': 100,
    'debug_mode': False,
    'sampling_rate': 10,
    'units': {'temp': 'C', 'pressure': 'kPa', 'flow': 'L/min'},
    'scaling_power': 2,
    'baseline_offset': 0.5
}

# Irrelevant auxiliary function (decoy)
def analyze_trend(data_list):
    if not data_list:
        return 0
    values = [d['val'] for d in data_list if d['type'] == 'temp']
    if len(values) < 2:
        return 0
    return sum(b - a for a, b in zip(values, values[1:]))

# Unused transformation map
type_multiplier = {
    'temp': 1.2,
    'pressure': 1.5,
    'flow': 0.8
}

# Decoy statistical computation
avg_val = sum(d['val'] for d in data_stream) / len(data_stream)
median_val = sorted(d['val'] for d in data_stream)[len(data_stream)//2]

# Linear search for active temperature sensors (critical filtering step)
filtered_data = []
for record in data_stream:
    if record['type'] == 'temp' and record['status'] == 'active':
        filtered_data.append(record)

# Red herring: complex but unused bitwise operation on IDs
distinct_ids = 0
for d in filtered_data:
    distinct_ids ^= d['id'] << 1

# Another decoy list comprehension: transforms all pressure readings (not used)
compensated_pressure = [
    {'raw': d['val'], 'adjusted': d['val'] * config['calibration_factor']}
    for d in data_stream if d['type'] == 'pressure'
]

# Key processing function that uses only filtered temp data and config
def process_signals(signal_list, cfg):
    # Extract values and apply threshold filtering
    valid_signals = [s['val'] for s in signal_list if s['val'] > cfg['threshold']]
    
    # Compute weighted sum using scaling power from config
    weighted_sum = 0.0
    for i, val in enumerate(valid_signals):
        exponent = cfg['scaling_power'] - (i * 0.1)  # decaying exponent
        weighted_sum += val ** exponent
    
    # Apply baseline offset from config
    result = weighted_sum + cfg['baseline_offset']
    
    # Dead code branch: never executed due to debug_mode=False
    if cfg['debug_mode'] and len(valid_signals) > 10:
        backup = 0
        for v in valid_signals:
            backup += math.log(v + 1) * 2
        result = backup  # never reached
    
    return result

# Misleading intermediate aggregation (unused)
total_energy = sum(
    math.exp(d['val'] * 0.1) for d in data_stream if d['status'] == 'active'
)

# Critical execution point
final_output = process_signals(filtered_data, config)

# Output result
print(f"Result: {final_output}")