import math

def analyze_signal(x):
    if x < 0:
        return abs(x) ** 0.5
    else:
        return math.log(x + 1)

# Irrelevant helper function (dead code path)
def unused_checksum(data):
    return sum(d % 7 for d in data) * 3

def transform_sequence(seq, factor):
    result = []
    for i, val in enumerate(seq):
        temp = val * factor
        if i % 2 == 0:
            temp += 2
        else:
            temp -= 1
        result.append(temp)
    return result

def decode_payload(payload):
    # Complex but ultimately unused transformation chain
    decoded = [p ^ 5 for p in payload]
    shifted = [(d >> 2) & 15 for d in decoded]
    return [s * 3 for s in shifted]

# Sensor simulation with red herring variables
baseline_offset = 1024
scaling_factor = 0.75
buffer_size = 64
sample_window = [i * 0.5 for i in range(10)]

# Calibration matrix with misleading entries
auxiliary_constants = [1.1, 0.9, 1.05, 0.95]
calibration_matrix = {
    'gain': [1.2, 0.8, 1.1, 0.9],
    'offset': [-0.5, 0.3, -0.2, 0.4],
    'active': True,
    'version': 'CAL-2.1'
}

# Sensor data with mixed relevance
sensor_data = {
    'readings': [16, 25, 36, 49],
    'mode': 'diagnostic',
    'timestamp': 1712345678,
    'sequence': (4, 9, 16),
    'flags': { 'valid': True, 'calibrated': False }
}

# Distractor: complex but unused data structure
fusion_engine = {
    'nodes': [
        {'id': 'A', 'weight': 0.8, 'inputs': [1, 2]},
        {'id': 'B', 'weight': 1.1, 'inputs': [3, 4]}
    ],
    'status': 'inactive',
    'cache': [transform_sequence([1,2,3], 2), decode_payload([10,20,30])]
}

# Key processing logic buried in distractions
def process_readings(data, calib):
    readings = data['readings']
    mode = data['mode']
    seq = data['sequence']
    
    # Step 1: Apply square root via analyze_signal (non-obvious use)
    processed = [analyze_signal(r) for r in readings]
    
    # Step 2: Use only first 3 elements
    truncated = processed[:3]
    
    # Step 3: Multiply by gain[0] and add offset[0]
    adjusted = []
    for v in truncated:
        adj_val = v * calib['gain'][0] + calib['offset'][0]
        adjusted.append(adj_val)
    
    # Step 4: Sum and apply modular arithmetic
    raw_sum = sum(adjusted)
    normalized = raw_sum % 100
    
    # Step 5: Conditional adjustment based on mode
    if mode == 'diagnostic':
        normalized += len(seq)  # adds 3
    
    # Step 6: Final transformation using string-based switch (red herring fallback)
    flag_key = 'calibrated'
    status_map = {'True': 10, 'False': -5}
    status_str = str(data['flags'].get(flag_key))
    decoy_adjust = status_map.get(status_str, 0)  # evaluates to -5, but not used
    
    # Actual final step (not decoy)
    final_value = int(normalized * 2)  # becomes integer
    
    return final_value

# Misleading pre-computations (irrelevant)
temp_analysis = transform_sequence(sensor_data['readings'], scaling_factor)
checksum_test = unused_checksum([7, 14, 21])

# Critical execution point
final_diagnostic = process_readings(sensor_data, calibration_matrix)

# Print required output
print(f"Result: {final_diagnostic}")