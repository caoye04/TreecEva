def analyze_signal(samples):
    if not samples:
        return 0
    magnitude = sum(abs(s) for s in samples)
    threshold = 100
    return magnitude > threshold

# Irrelevant helper function (dead code path)
def legacy_encode(data):
    encoded = ''
    for d in data:
        encoded += chr(ord(d) + 1)
    return encoded

# Unused transformation function
def transform_coordinates(x, y):
    return (x * 2 + y, y - x)

# Simulated sensor readings
sensor_A = [12, -45, 67, -23, 89, -12]
sensor_B = [5, 18, -60, 44, -91, 30]

# Misleading intermediate aggregation
aggregate_power = sum([abs(val) for val in sensor_A]) + sum([val**2 for val in sensor_B[:3]])

# System health indicators (some irrelevant)
health_flags = {
    'voltage_stable': True,
    'thermal_margin': 0.78,
    'cache_integrity': False,
    'io_latency': 120
}

# Calibration sequence with red herring operations
calibration_sequence = []
for i in range(8):
    if i % 3 == 0:
        calibration_sequence.append(i * 17)
    elif i % 5 == 0:
        calibration_sequence.append(-i)
    else:
        calibration_sequence.append(i + 2)

# Add decoy element (not used in final logic)
calibration_sequence.append(999)  # red herring

# System state setup
system_state = {
    'mode': 'diagnostic',
    'version': '2.1.5',
    'active_sensors': len(sensor_A),
    'last_reset': None
}

# Complex conditional expression evaluating signal quality
signal_quality = 'high' if analyze_signal(sensor_A) and analyze_signal(sensor_B) else 'low'

# Unused diagnostic log
log_entries = []
for i, sample in enumerate(sensor_A):
    if sample < 0:
        log_entries.append(f"Negative reading at index {i}")

# Primary processing function with nested logic
def process_metrics(seq, state):
    if state['mode'] != 'diagnostic':
        return -1
    
    # Bit manipulation on sequence indices
    transformed = 0
    for idx, val in enumerate(seq):
        if idx & 1:  # odd index
            transformed ^= (val & 255)  # byte mask
        else:
            transformed += (val % 19) * 3
    
    # Conditional override based on version (irrelevant check)
    if state.get('version') == '1.0.0':
        transformed = 0
    
    # String-based fallback (never reached due to mode)
    fallback_key = ''.join([chr(97 + (idx % 26)) for idx in range(5)]) if transformed < 0 else ''
    
    # Core arithmetic chain
    accumulator = 0
    for x in seq[:7]:  # skip last (decoy) element
        if x > 0:
            accumulator += x * x
        else:
            accumulator -= x // 2
    
    # Final computation combining multiple concepts
    adjustment = len(state['mode']) * 13
    result = (transformed + accumulator) - adjustment
    
    # Early termination condition (not triggered)
    if result > 10000:
        return 9999
    
    return result

# Execute critical statement
final_diagnostic = process_metrics(calibration_sequence, system_state)

# Print result as required
print(f"Result: {final_diagnostic}")